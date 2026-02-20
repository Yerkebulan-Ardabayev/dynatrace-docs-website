#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Перевод документации Dynatrace
Основной: Google Gemini Flash (1500 req/day бесплатно)
Fallback:  Groq Llama 3.3 70B (100K tokens/day бесплатно)

Ключи берутся ТОЛЬКО из переменных окружения (никогда не в коде):
  GEMINI_API_KEY  — https://aistudio.google.com/apikey
  GROQ_API_KEY    — https://console.groq.com
"""

import os
import sys
import io
import json
import time
import hashlib
import requests
from pathlib import Path

# Fix Windows encoding (cp1251 can't handle emoji)
if sys.platform == 'win32':
    try:
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8', errors='replace')
            sys.stderr.reconfigure(encoding='utf-8', errors='replace')
        elif hasattr(sys.stdout, 'buffer'):
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
            sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    except Exception:
        pass

# Загрузка .env файла (если есть)
def _load_dotenv():
    env_paths = [
        Path(__file__).parent.parent / '.env',  # корень проекта
        Path(__file__).parent / '.env',
        Path('.env'),
    ]
    for env_path in env_paths:
        if env_path.exists():
            with open(env_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, _, val = line.partition('=')
                        key = key.strip()
                        val = val.strip().strip('"').strip("'")
                        if key and key not in os.environ:
                            os.environ[key] = val
            break
_load_dotenv()

# API ключи из окружения (или .env)
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')
GROQ_API_KEY   = os.environ.get('GROQ_API_KEY', '')
OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY', '')

GROQ_API_URL   = 'https://api.groq.com/openai/v1/chat/completions'
GEMINI_API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent'
OPENROUTER_API_URL = 'https://openrouter.ai/api/v1/chat/completions'
# Бесплатные модели OpenRouter — пробуем по очереди при rate limit
OPENROUTER_MODELS = [
    'google/gemma-3-27b-it:free',           # Google Gemma 3 27B (работает!)
    'meta-llama/llama-3.3-70b-instruct:free', # Llama 3.3 70B
    'microsoft/phi-4-reasoning-plus:free',   # Microsoft Phi-4
    'qwen/qwen3-8b:free',                   # Qwen 3 8B
]

# Директории
DOCS_DIR = Path('../docs')
EN_DIR   = DOCS_DIR / 'en'
RU_DIR   = DOCS_DIR / 'ru'

# Кеш переводов
CACHE_FILE = Path('.translation_cache_groq.json')
cache = {}
if CACHE_FILE.exists():
    with open(CACHE_FILE, 'r', encoding='utf-8') as f:
        cache = json.load(f)

MAX_CHUNK_CHARS = 10000

import re

# ============================================================================
# ЗАЩИТА BRAND-ТЕРМИНОВ (placeholder-подход — 100% надёжность)
# ============================================================================
# LLM иногда игнорирует инструкцию "не переводи".
# Решение: заменяем термины на плейсхолдеры ПЕРЕД отправкой,
# восстанавливаем ПОСЛЕ получения перевода. Модель физически
# не может перевести то, чего нет в тексте.

PROTECTED_TERMS = [
    # Dynatrace products (порядок важен! Длинные первыми)
    'Cluster Management Console', 'Real User Monitoring',
    'Synthetic Monitoring', 'Session Replay', 'Service Flow',
    'Management Zone', 'Mission Control', 'Host Group', 'Host Unit',
    'OneAgent', 'ActiveGate', 'Smartscape', 'PurePath', 'Davis AI',
    'AppEngine', 'Dynatrace', 'Extensions', 'Environment',
    'Grail', 'DQL', 'CMC', 'Hub',
    # Cloud / DevOps
    'Kubernetes', 'OpenShift', 'Docker', 'Ansible', 'Helm',
    'REST API', 'gRPC', 'AWS', 'Azure', 'GCP',
    'API', 'SDK', 'JSON', 'YAML', 'XML',
]

def protect_terms(text: str) -> tuple[str, dict]:
    """Заменяет protected terms на плейсхолдеры. Возвращает (text, mapping)."""
    mapping = {}
    counter = 0
    for term in PROTECTED_TERMS:
        # Case-sensitive поиск
        pattern = re.compile(re.escape(term))
        if pattern.search(text):
            placeholder = f'__KEEP{counter:03d}__'
            mapping[placeholder] = term
            text = pattern.sub(placeholder, text)
            counter += 1
    return text, mapping

def restore_terms(text: str, mapping: dict) -> str:
    """Восстанавливает оригинальные термины из плейсхолдеров."""
    for placeholder, term in mapping.items():
        text = text.replace(placeholder, term)
    return text

def post_fix_known_errors(text: str) -> str:
    """Исправляет известные ошибочные переводы (на случай старого кеша)."""
    fixes = {
        'Один Агент': 'OneAgent', 'ОдинАгент': 'OneAgent',
        'Один агент': 'OneAgent', 'одинагент': 'OneAgent',
        'Активный шлюз': 'ActiveGate', 'Активгейт': 'ActiveGate',
        'Активный Шлюз': 'ActiveGate',
        'Чистый путь': 'PurePath', 'Чистый Путь': 'PurePath',
        'Умная карта': 'Smartscape', 'Умный ландшафт': 'Smartscape',
        'Консоль управления кластером': 'Cluster Management Console',
        'Центр управления': 'Mission Control',
        'Единица хоста': 'Host Unit', 'Группа хостов': 'Host Group',
    }
    for wrong, correct in fixes.items():
        text = text.replace(wrong, correct)
    return text

TRANSLATION_PROMPT = """Переведи следующую техническую документацию Dynatrace с английского на русский.

ВАЖНО:
- Сохрани всё форматирование Markdown (заголовки, списки, код, ссылки, YAML frontmatter)
- Все слова вида __KEEP000__, __KEEP001__ и т.д. — это плейсхолдеры. НЕ ПЕРЕВОДИ их, оставь как есть!
- Переведи качественно и профессионально
- НЕ добавляй никаких комментариев, только перевод
- Не добавляй вводные фразы типа "Вот перевод:" — сразу начинай с перевода

Текст для перевода:

{text}"""


def split_into_chunks(text: str, max_chars: int = MAX_CHUNK_CHARS) -> list:
    """Разбивает текст на чанки по Markdown-заголовкам"""
    if len(text) <= max_chars:
        return [text]

    chunks = []
    sections = re.split(r'(^#{1,3} .+$)', text, flags=re.MULTILINE)
    current_chunk = ""
    for section in sections:
        if len(current_chunk) + len(section) > max_chars and current_chunk:
            chunks.append(current_chunk)
            current_chunk = section
        else:
            current_chunk += section
    if current_chunk:
        chunks.append(current_chunk)

    final_chunks = []
    for chunk in chunks:
        if len(chunk) <= max_chars:
            final_chunks.append(chunk)
        else:
            paragraphs = chunk.split('\n\n')
            sub_chunk = ""
            for para in paragraphs:
                if len(sub_chunk) + len(para) + 2 > max_chars and sub_chunk:
                    final_chunks.append(sub_chunk)
                    sub_chunk = para
                else:
                    sub_chunk += ('\n\n' if sub_chunk else '') + para
            if sub_chunk:
                final_chunks.append(sub_chunk)

    return final_chunks


def translate_via_gemini(text: str) -> str | None:
    """Перевод через Gemini Flash. Возвращает None при ошибке/лимите."""
    if not GEMINI_API_KEY:
        return None

    prompt = TRANSLATION_PROMPT.format(text=text)
    max_retries = 5
    for attempt in range(max_retries):
        try:
            response = requests.post(
                f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
                headers={'Content-Type': 'application/json'},
                json={
                    'contents': [{'parts': [{'text': prompt}]}],
                    'generationConfig': {
                        'temperature': 0.3,
                        'maxOutputTokens': 8192,
                    }
                },
                timeout=90
            )

            if response.status_code == 429:
                # Check if it's daily quota exhausted vs per-minute limit
                err_text = response.text
                if 'limit: 0' in err_text or 'quota' in err_text.lower():
                    print(f"  ⏳ Gemini дневная квота исчерпана — пропускаю на Groq")
                    return None
                wait = 20 * (attempt + 1)  # 20, 40, 60, 80, 100 sec
                print(f"  ⏳ Gemini rate limit, жду {wait}с...")
                time.sleep(wait)
                continue

            if response.status_code == 403 or response.status_code == 401:
                print(f"  ❌ Gemini: неверный ключ или квота исчерпана ({response.status_code})")
                return None

            if response.status_code != 200:
                print(f"  ❌ Gemini API ошибка: {response.status_code}")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
                    continue
                return None

            data = response.json()
            candidates = data.get('candidates', [])
            if not candidates:
                print(f"  ❌ Gemini: пустой ответ")
                return None

            translation = candidates[0]['content']['parts'][0]['text'].strip()
            time.sleep(4.0)  # Gemini free: 15 req/min = 4 sec between requests
            return translation

        except requests.Timeout:
            wait = 2 ** (attempt + 1)
            print(f"  ⏳ Gemini таймаут, жду {wait}с...")
            time.sleep(wait)
        except Exception as e:
            print(f"  ❌ Gemini исключение: {e}")
            if attempt < max_retries - 1:
                time.sleep(2)
                continue
            return None

    return None


def translate_via_groq(text: str) -> str | None:
    """Перевод через Groq Llama. Возвращает None при ошибке/лимите."""
    if not GROQ_API_KEY:
        return None

    prompt = TRANSLATION_PROMPT.format(text=text)
    max_retries = 6
    for attempt in range(max_retries):
        try:
            response = requests.post(
                GROQ_API_URL,
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {GROQ_API_KEY}'
                },
                json={
                    'model': 'llama-3.3-70b-versatile',
                    'messages': [{'role': 'user', 'content': prompt}],
                    'temperature': 0.3,
                    'max_tokens': 8000,
                    'top_p': 1,
                    'stream': False
                },
                timeout=90
            )

            if response.status_code == 429:
                retry_after = response.headers.get('retry-after', '')
                wait = int(retry_after) if retry_after.isdigit() else min(10 * (attempt + 1), 60)
                # Если ждать слишком долго (>60с) — сразу на следующий API
                if wait > 60:
                    print(f"  ⏳ Groq rate limit {wait}с — слишком долго, передаю следующему API")
                    return None
                print(f"  ⏳ Groq rate limit, жду {wait}с... (попытка {attempt+1}/{max_retries})")
                time.sleep(wait)
                continue

            if response.status_code != 200:
                print(f"  ❌ Groq API ошибка: {response.status_code}")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
                    continue
                return None

            result = response.json()
            if 'choices' not in result or not result['choices']:
                print(f"  ❌ Groq: пустой ответ")
                return None

            translation = result['choices'][0]['message']['content'].strip()
            time.sleep(2.0)  # Groq: 30 req/min
            return translation

        except requests.Timeout:
            wait = 2 ** (attempt + 1)
            print(f"  ⏳ Groq таймаут, жду {wait}с...")
            time.sleep(wait)
        except Exception as e:
            print(f"  ❌ Groq исключение: {e}")
            if attempt < max_retries - 1:
                time.sleep(2)
                continue
            return None

    return None


def translate_via_openrouter(text: str) -> str | None:
    """Перевод через OpenRouter (бесплатные модели). 3-й fallback.
    Перебирает несколько бесплатных моделей при rate limit."""
    if not OPENROUTER_API_KEY:
        return None

    prompt = TRANSLATION_PROMPT.format(text=text)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {OPENROUTER_API_KEY}',
        'HTTP-Referer': 'https://github.com/Yerkebulan-Ardabayev/dynatrace-docs-website',
        'X-Title': 'Dynatrace Docs Translator'
    }

    for model in OPENROUTER_MODELS:
        for attempt in range(3):
            try:
                response = requests.post(
                    OPENROUTER_API_URL,
                    headers=headers,
                    json={
                        'model': model,
                        'messages': [{'role': 'user', 'content': prompt}],
                        'temperature': 0.3,
                        'max_tokens': 8000,
                    },
                    timeout=120
                )

                if response.status_code == 429:
                    wait = min(15 * (attempt + 1), 45)
                    print(f"  ⏳ OpenRouter [{model}] rate limit, жду {wait}с...")
                    time.sleep(wait)
                    continue

                if response.status_code != 200:
                    err = response.json().get('error', {}).get('message', '')[:80]
                    print(f"  ❌ OpenRouter [{model}] ошибка {response.status_code}: {err}")
                    break  # Попробовать следующую модель

                result = response.json()
                if 'choices' not in result or not result['choices']:
                    print(f"  ❌ OpenRouter [{model}]: пустой ответ")
                    break

                translation = result['choices'][0]['message']['content'].strip()
                time.sleep(2.0)
                print(f"  ✅ OpenRouter [{model}]")
                return translation

            except requests.Timeout:
                print(f"  ⏳ OpenRouter [{model}] таймаут, повтор...")
                time.sleep(5)
            except Exception as e:
                print(f"  ❌ OpenRouter [{model}] исключение: {e}")
                break

    return None


def translate_text(text: str, source_file: str) -> str:
    """
    Переводит текст. Стратегия:
    1. Проверяем кеш
    2. Защищаем brand-термины плейсхолдерами
    3. Пробуем Gemini Flash (основной)
    4. Fallback на Groq (если Gemini недоступен)
    5. Fallback на OpenRouter (если Groq недоступен)
    6. Восстанавливаем термины + пост-фикс ошибок
    6. Возвращаем оригинал если оба недоступны
    """
    cache_key = f"{source_file}:{hashlib.sha256(text.encode('utf-8')).hexdigest()[:16]}"
    if cache_key in cache:
        print(f"  ↻ Из кеша")
        # Пост-фикс даже для кешированных (на случай старых ошибок)
        return post_fix_known_errors(cache[cache_key])

    # Защищаем термины плейсхолдерами
    protected_text, term_mapping = protect_terms(text)

    translation = None

    # 1. Пробуем Gemini
    if GEMINI_API_KEY:
        print(f"  🌟 Перевод через Gemini Flash...")
        translation = translate_via_gemini(protected_text)
        if translation:
            print(f"  ✅ Gemini успешно!")

    # 2. Fallback на Groq
    if translation is None and GROQ_API_KEY:
        print(f"  🔄 Fallback: Groq Llama 3.3 70B...")
        translation = translate_via_groq(protected_text)
        if translation:
            print(f"  ✅ Groq успешно!")

    # 3. Fallback на OpenRouter (бесплатные модели)
    if translation is None and OPENROUTER_API_KEY:
        print(f"  🔄 Fallback 2: OpenRouter (Llama 3.3 70B free)...")
        translation = translate_via_openrouter(protected_text)
        if translation:
            print(f"  ✅ OpenRouter успешно!")

    # 4. Все API недоступны — возвращаем None (НЕ записываем оригинал!)
    if translation is None:
        print(f"  ⚠️  Все API недоступны — пропускаю файл")
        return None

    # Восстанавливаем brand-термины и фиксим известные ошибки
    translation = restore_terms(translation, term_mapping)
    translation = post_fix_known_errors(translation)

    # Сохраняем в кеш
    cache[cache_key] = translation
    return translation


def translate_file(en_file: Path):
    """Перевод одного файла"""
    relative_path = en_file.relative_to(EN_DIR)
    ru_file = RU_DIR / relative_path

    print(f"\n📄 {relative_path}")

    if ru_file.exists():
        en_mtime = en_file.stat().st_mtime
        ru_mtime = ru_file.stat().st_mtime
        if ru_mtime > en_mtime:
            print(f"  ✓ Уже переведен (пропуск)")
            return

    try:
        with open(en_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ❌ Ошибка чтения: {e}")
        return

    if len(content) > MAX_CHUNK_CHARS:
        print(f"  📏 Большой файл ({len(content)} символов) — разбиваю на части...")
        chunks = split_into_chunks(content)
        translated_parts = []
        for ci, chunk in enumerate(chunks, 1):
            print(f"  📦 Часть {ci}/{len(chunks)}...")
            result = translate_text(chunk, f"{relative_path}#chunk{ci}")
            if result is None:
                print(f"  ⚠️  Не удалось перевести часть {ci} — пропускаю файл")
                return
            translated_parts.append(result)
        translated = '\n\n'.join(translated_parts)
    else:
        translated = translate_text(content, str(relative_path))
        if translated is None:
            return

    try:
        ru_file.parent.mkdir(parents=True, exist_ok=True)
        with open(ru_file, 'w', encoding='utf-8') as f:
            f.write(translated)
        print(f"  ✅ Сохранено!")
    except Exception as e:
        print(f"  ❌ Ошибка записи: {e}")


def main():
    print("=" * 70)
    print("🌐 ПЕРЕВОД ДОКУМЕНТАЦИИ DYNATRACE")
    print("=" * 70)

    # Статус ключей
    if GEMINI_API_KEY:
        print("✅ Gemini Flash — АКТИВЕН (основной, 1500 req/day)")
    else:
        print("⚠️  GEMINI_API_KEY не задан — Gemini пропускается")

    if GROQ_API_KEY:
        print("✅ Groq Llama 3.3 70B — АКТИВЕН (fallback 1, 100K tokens/day)")
    else:
        print("⚠️  GROQ_API_KEY не задан — Groq пропускается")

    if OPENROUTER_API_KEY:
        print("✅ OpenRouter (Llama 3.3 free) — АКТИВЕН (fallback 2)")
    else:
        print("⚠️  OPENROUTER_API_KEY не задан — OpenRouter пропускается")

    if not GEMINI_API_KEY and not GROQ_API_KEY and not OPENROUTER_API_KEY:
        print("\n❌ Ни один API ключ не задан! Перевод невозможен.")
        print("   GEMINI_API_KEY    → https://aistudio.google.com/apikey")
        print("   GROQ_API_KEY      → https://console.groq.com")
        print("   OPENROUTER_API_KEY → https://openrouter.ai/keys")
        return

    print("=" * 70)
    print()

    if not EN_DIR.exists():
        print(f"❌ Директория не найдена: {EN_DIR}")
        return

    en_files = list(EN_DIR.rglob('*.md'))
    if not en_files:
        print(f"❌ Нет файлов для перевода в {EN_DIR}")
        return

    print(f"📚 Найдено файлов: {len(en_files)}")
    print()

    translated = 0
    skipped = 0
    errors = 0
    start_time = time.time()

    for i, en_file in enumerate(en_files, 1):
        print(f"[{i}/{len(en_files)}]", end=" ")
        try:
            before_skipped = skipped
            translate_file(en_file)
            translated += 1
        except KeyboardInterrupt:
            print("\n\n⚠️  Прервано пользователем")
            break
        except Exception as e:
            print(f"  ❌ Ошибка: {e}")
            errors += 1

        if i % 10 == 0:
            with open(CACHE_FILE, 'w', encoding='utf-8') as f:
                json.dump(cache, f, ensure_ascii=False, indent=2)

    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

    elapsed = time.time() - start_time
    print()
    print("=" * 70)
    print("📊 ГОТОВО")
    print("=" * 70)
    print(f"✅ Обработано: {translated}")
    print(f"❌ Ошибок:    {errors}")
    print(f"⏱️  Время:     {int(elapsed//60)}м {int(elapsed%60)}с")
    print()

    # Автоматически обновляем nav в mkdocs.yml
    try:
        import subprocess
        update_nav_script = Path(__file__).parent / 'update_nav.py'
        if update_nav_script.exists():
            print("🔄 Обновляю nav в mkdocs.yml...")
            result = subprocess.run(
                [sys.executable, str(update_nav_script)],
                capture_output=True, text=True, encoding='utf-8'
            )
            if result.returncode == 0:
                print("✅ Nav обновлён!")
            else:
                print(f"⚠️  Nav не обновлён: {result.stderr[:200]}")
    except Exception as e:
        print(f"⚠️  Ошибка обновления nav: {e}")


if __name__ == '__main__':
    main()
