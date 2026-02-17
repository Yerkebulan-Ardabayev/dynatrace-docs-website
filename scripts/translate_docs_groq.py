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
import json
import time
import hashlib
import requests
from pathlib import Path

# API ключи ТОЛЬКО из окружения
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')
GROQ_API_KEY   = os.environ.get('GROQ_API_KEY', '')

GROQ_API_URL   = 'https://api.groq.com/openai/v1/chat/completions'
GEMINI_API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent'

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

TRANSLATION_PROMPT = """Переведи следующую техническую документацию Dynatrace с английского на русский.

ВАЖНО:
- Сохрани всё форматирование Markdown (заголовки, списки, код, ссылки, YAML frontmatter)
- НЕ переводи следующие термины (оставь на английском как есть):
  Dynatrace, OneAgent, ActiveGate, Smartscape, PurePath, Davis AI, Grail, DQL,
  Cluster Management Console (CMC), Mission Control, Management Zone, Host Unit,
  Host Group, Service Flow, Session Replay, Real User Monitoring (RUM),
  Synthetic Monitoring, AppEngine, Hub, Extensions, Environment,
  Kubernetes, Docker, Helm, OpenShift, Ansible, AWS, Azure, GCP,
  API, SDK, REST API, gRPC, JSON, YAML, XML
- Переведи качественно и профессионально
- НЕ добавляй никаких комментариев, только перевод
- Не добавляй вводные фразы типа "Вот перевод:" - сразу начинай с перевода

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
    max_retries = 3
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
                timeout=60
            )

            if response.status_code == 429:
                wait = 2 ** (attempt + 1)
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
            time.sleep(0.5)  # Gemini: 1500 req/day, ~1 req/min — небольшая пауза
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
    max_retries = 3
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
                timeout=60
            )

            if response.status_code == 429:
                wait = 2 ** (attempt + 1)
                print(f"  ⏳ Groq rate limit, жду {wait}с...")
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


def translate_text(text: str, source_file: str) -> str:
    """
    Переводит текст. Стратегия:
    1. Проверяем кеш
    2. Пробуем Gemini Flash (основной, быстрый лимит)
    3. Fallback на Groq (если Gemini недоступен или лимит)
    4. Возвращаем оригинал если оба недоступны
    """
    cache_key = f"{source_file}:{hashlib.sha256(text.encode('utf-8')).hexdigest()[:16]}"
    if cache_key in cache:
        print(f"  ↻ Из кеша")
        return cache[cache_key]

    translation = None

    # 1. Пробуем Gemini
    if GEMINI_API_KEY:
        print(f"  🌟 Перевод через Gemini Flash...")
        translation = translate_via_gemini(text)
        if translation:
            print(f"  ✅ Gemini успешно!")

    # 2. Fallback на Groq
    if translation is None and GROQ_API_KEY:
        print(f"  🔄 Fallback: Groq Llama 3.3 70B...")
        translation = translate_via_groq(text)
        if translation:
            print(f"  ✅ Groq успешно!")

    # 3. Оба недоступны — возвращаем оригинал
    if translation is None:
        print(f"  ⚠️  Оба API недоступны — оставляю оригинал")
        return text

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
            translated_parts.append(translate_text(chunk, f"{relative_path}#chunk{ci}"))
        translated = '\n\n'.join(translated_parts)
    else:
        translated = translate_text(content, str(relative_path))

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
        print("✅ Groq Llama 3.3 70B — АКТИВЕН (fallback, 100K tokens/day)")
    else:
        print("⚠️  GROQ_API_KEY не задан — Groq пропускается")

    if not GEMINI_API_KEY and not GROQ_API_KEY:
        print("\n❌ Ни один API ключ не задан! Перевод невозможен.")
        print("   GEMINI_API_KEY → https://aistudio.google.com/apikey")
        print("   GROQ_API_KEY   → https://console.groq.com")
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


if __name__ == '__main__':
    main()
