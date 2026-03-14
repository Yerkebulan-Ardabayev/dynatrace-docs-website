#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Принудительный перевод файлов из real_missing.txt
"""

import os
import sys
import io
import json
import time
import hashlib
import re
import requests
from pathlib import Path

if sys.platform == 'win32':
    try:
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8', errors='replace')
            sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

def _load_dotenv():
    env_paths = [
        Path(__file__).parent.parent / '.env',
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

GEMINI_API_KEYS = [val for key, val in os.environ.items() if key.startswith('GEMINI_API_KEY') and val]
GEMINI_API_KEY = GEMINI_API_KEYS[0] if GEMINI_API_KEYS else ''
GROQ_API_KEY   = os.environ.get('GROQ_API_KEY', '')
OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY', '')

GROQ_API_URL   = 'https://api.groq.com/openai/v1/chat/completions'
GEMINI_API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent'
OPENROUTER_API_URL = 'https://openrouter.ai/api/v1/chat/completions'
OPENROUTER_MODELS = [
    'google/gemma-3-27b-it:free',
    'meta-llama/llama-3.3-70b-instruct:free',
    'microsoft/phi-4-reasoning-plus:free',
    'qwen/qwen3-8b:free',
]

BASE_DIR = Path(__file__).parent.parent
EN_DIR   = BASE_DIR / 'docs' / 'en'
RU_DIR   = BASE_DIR / 'docs' / 'ru'
MISSING_FILE = BASE_DIR / 'real_missing.txt'
CACHE_FILE = BASE_DIR / '.translation_cache_groq.json'

cache = {}
if CACHE_FILE.exists():
    with open(CACHE_FILE, 'r', encoding='utf-8') as f:
        cache = json.load(f)

MAX_CHUNK_CHARS = 10000

PROTECTED_TERMS = [
    'Cluster Management Console', 'Real User Monitoring',
    'Synthetic Monitoring', 'Session Replay', 'Service Flow',
    'Management Zone', 'Mission Control', 'Host Group', 'Host Unit',
    'OneAgent', 'ActiveGate', 'Smartscape', 'PurePath', 'Davis AI',
    'AppEngine', 'Dynatrace', 'Extensions', 'Environment',
    'Grail', 'DQL', 'CMC', 'Hub',
    'Kubernetes', 'OpenShift', 'Docker', 'Ansible', 'Helm',
    'REST API', 'gRPC', 'AWS', 'Azure', 'GCP',
    'API', 'SDK', 'JSON', 'YAML', 'XML',
]

def protect_terms(text):
    mapping = {}
    counter = 0
    for term in PROTECTED_TERMS:
        pattern = re.compile(re.escape(term))
        if pattern.search(text):
            placeholder = f'__KEEP{counter:03d}__'
            mapping[placeholder] = term
            text = pattern.sub(placeholder, text)
            counter += 1
    return text, mapping

def restore_terms(text, mapping):
    for placeholder, term in mapping.items():
        text = text.replace(placeholder, term)
    return text

def post_fix_known_errors(text):
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


def split_into_chunks(text, max_chars=MAX_CHUNK_CHARS):
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


def translate_via_gemini(text):
    if not GEMINI_API_KEYS:
        return None
    prompt = TRANSLATION_PROMPT.format(text=text)
    for api_key in GEMINI_API_KEYS:
        for attempt in range(5):
            try:
                response = requests.post(
                    f"{GEMINI_API_URL}?key={api_key}",
                    headers={'Content-Type': 'application/json'},
                    json={
                        'contents': [{'parts': [{'text': prompt}]}],
                        'generationConfig': {'temperature': 0.3, 'maxOutputTokens': 8192}
                    },
                    timeout=90
                )
                if response.status_code == 429:
                    err_text = response.text
                    if 'limit: 0' in err_text or 'quota' in err_text.lower():
                        print(f"  Gemini квота исчерпана, пробую следующий ключ...")
                        break
                    wait = 20 * (attempt + 1)
                    print(f"  Gemini rate limit, жду {wait}с...")
                    time.sleep(wait)
                    continue
                if response.status_code in (401, 403):
                    print(f"  Gemini: неверный ключ ({response.status_code})")
                    break
                if response.status_code != 200:
                    print(f"  Gemini API ошибка: {response.status_code}")
                    if attempt < 4:
                        time.sleep(2 ** attempt)
                    continue
                data = response.json()
                candidates = data.get('candidates', [])
                if not candidates:
                    print(f"  Gemini: пустой ответ")
                    break
                translation = candidates[0]['content']['parts'][0]['text'].strip()
                time.sleep(4.0)
                return translation
            except requests.Timeout:
                wait = 2 ** (attempt + 1)
                print(f"  Gemini таймаут, жду {wait}с...")
                time.sleep(wait)
            except Exception as e:
                print(f"  Gemini исключение: {e}")
                if attempt < 4:
                    time.sleep(2)
    return None


def translate_via_groq(text):
    if not GROQ_API_KEY:
        return None
    prompt = TRANSLATION_PROMPT.format(text=text)
    for attempt in range(6):
        try:
            response = requests.post(
                GROQ_API_URL,
                headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {GROQ_API_KEY}'},
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
                if wait > 60:
                    print(f"  Groq rate limit {wait}с — передаю следующему API")
                    return None
                print(f"  Groq rate limit, жду {wait}с...")
                time.sleep(wait)
                continue
            if response.status_code != 200:
                print(f"  Groq API ошибка: {response.status_code}")
                if attempt < 5:
                    time.sleep(2 ** attempt)
                continue
            result = response.json()
            if 'choices' not in result or not result['choices']:
                return None
            translation = result['choices'][0]['message']['content'].strip()
            time.sleep(2.0)
            return translation
        except requests.Timeout:
            wait = 2 ** (attempt + 1)
            print(f"  Groq таймаут, жду {wait}с...")
            time.sleep(wait)
        except Exception as e:
            print(f"  Groq исключение: {e}")
            if attempt < 5:
                time.sleep(2)
    return None


def translate_via_openrouter(text):
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
                    json={'model': model, 'messages': [{'role': 'user', 'content': prompt}], 'temperature': 0.3, 'max_tokens': 8000},
                    timeout=120
                )
                if response.status_code == 429:
                    wait = min(15 * (attempt + 1), 45)
                    print(f"  OpenRouter [{model}] rate limit, жду {wait}с...")
                    time.sleep(wait)
                    continue
                if response.status_code != 200:
                    err = response.json().get('error', {}).get('message', '')[:80]
                    print(f"  OpenRouter [{model}] ошибка {response.status_code}: {err}")
                    break
                result = response.json()
                if 'choices' not in result or not result['choices']:
                    break
                translation = result['choices'][0]['message']['content'].strip()
                time.sleep(2.0)
                print(f"  OpenRouter [{model}] успешно")
                return translation
            except requests.Timeout:
                print(f"  OpenRouter [{model}] таймаут, повтор...")
                time.sleep(5)
            except Exception as e:
                print(f"  OpenRouter [{model}] исключение: {e}")
                break
    return None


def translate_text(text, source_file):
    cache_key = f"FORCE:{source_file}:{hashlib.sha256(text.encode('utf-8')).hexdigest()[:16]}"
    if cache_key in cache:
        print(f"  Из кеша")
        return post_fix_known_errors(cache[cache_key])

    protected_text, term_mapping = protect_terms(text)
    translation = None

    if GEMINI_API_KEY:
        print(f"  Перевод через Gemini Flash...")
        translation = translate_via_gemini(protected_text)
        if translation:
            print(f"  Gemini успешно!")

    if translation is None and GROQ_API_KEY:
        print(f"  Fallback: Groq...")
        translation = translate_via_groq(protected_text)
        if translation:
            print(f"  Groq успешно!")

    if translation is None and OPENROUTER_API_KEY:
        print(f"  Fallback 2: OpenRouter...")
        translation = translate_via_openrouter(protected_text)

    if translation is None:
        print(f"  Все API недоступны — пропускаю")
        return None

    translation = restore_terms(translation, term_mapping)
    translation = post_fix_known_errors(translation)

    cache[cache_key] = translation
    return translation


def save_cache():
    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)


def main():
    print("=" * 70)
    print("ПРИНУДИТЕЛЬНЫЙ ПЕРЕВОД НЕДОПЕРЕВЕДЁННЫХ ФАЙЛОВ")
    print("=" * 70)
    print(f"EN: {EN_DIR}")
    print(f"RU: {RU_DIR}")
    print(f"Список: {MISSING_FILE}")
    print()

    if not MISSING_FILE.exists():
        print("Файл real_missing.txt не найден! Запустите check_real_missing.py")
        return

    with open(MISSING_FILE, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    # Парсим пути (убираем " (Mostly English)" и " (Missing)")
    file_paths = []
    for line in lines:
        path = line.replace(' (Mostly English)', '').replace(' (Missing)', '').strip()
        file_paths.append(path)

    print(f"Файлов для перевода: {len(file_paths)}")
    print()

    translated = 0
    skipped = 0
    errors = 0
    start_time = time.time()

    for i, rel_path in enumerate(file_paths, 1):
        # На Windows пути с обратными слешами — нормализуем
        rel_path_obj = Path(rel_path)
        en_file = EN_DIR / rel_path_obj
        ru_file = RU_DIR / rel_path_obj

        print(f"[{i}/{len(file_paths)}] {rel_path}")

        if not en_file.exists():
            print(f"  EN файл не найден: {en_file}")
            errors += 1
            continue

        try:
            with open(en_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"  Ошибка чтения: {e}")
            errors += 1
            continue

        if len(content) > MAX_CHUNK_CHARS:
            print(f"  Большой файл ({len(content)} символов) — разбиваю на части...")
            chunks = split_into_chunks(content)
            translated_parts = []
            success = True
            for ci, chunk in enumerate(chunks, 1):
                print(f"  Часть {ci}/{len(chunks)}...")
                result = translate_text(chunk, f"{rel_path}#chunk{ci}")
                if result is None:
                    print(f"  Не удалось перевести часть {ci} — пропускаю файл")
                    success = False
                    break
                translated_parts.append(result)
            if not success:
                errors += 1
                continue
            final_translation = '\n\n'.join(translated_parts)
        else:
            final_translation = translate_text(content, str(rel_path))
            if final_translation is None:
                errors += 1
                continue

        try:
            ru_file.parent.mkdir(parents=True, exist_ok=True)
            with open(ru_file, 'w', encoding='utf-8') as f:
                f.write(final_translation)
            print(f"  Сохранено!")
            translated += 1
        except Exception as e:
            print(f"  Ошибка записи: {e}")
            errors += 1

        if i % 10 == 0:
            save_cache()
            elapsed = time.time() - start_time
            remaining = len(file_paths) - i
            avg = elapsed / i
            eta = int(avg * remaining)
            print(f"\n  [Прогресс: {i}/{len(file_paths)}, ETA: {eta//60}м {eta%60}с]\n")

    save_cache()

    elapsed = time.time() - start_time
    print()
    print("=" * 70)
    print("ГОТОВО")
    print("=" * 70)
    print(f"Переведено: {translated}")
    print(f"Ошибок:     {errors}")
    print(f"Время:      {int(elapsed//60)}м {int(elapsed%60)}с")


if __name__ == '__main__':
    main()
