#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
СУПЕР-БЫСТРЫЙ перевод документации Dynatrace с помощью Groq API
Llama 3.1 70B - БЕСПЛАТНО и в 10 раз быстрее!
"""

import os
import sys
import json
import time
import hashlib
import requests
from pathlib import Path

# Groq API - ключ берётся ТОЛЬКО из переменной окружения
API_KEY = os.environ.get('GROQ_API_KEY', '')
GROQ_API_URL = 'https://api.groq.com/openai/v1/chat/completions'

# Директории
DOCS_DIR = Path('../docs')
EN_DIR = DOCS_DIR / 'en'
RU_DIR = DOCS_DIR / 'ru'

# Кеш переводов
CACHE_FILE = Path('.translation_cache_groq.json')
cache = {}

if CACHE_FILE.exists():
    with open(CACHE_FILE, 'r', encoding='utf-8') as f:
        cache = json.load(f)

# Максимальный размер чанка (~4000 токенов ≈ 12000 символов, оставляем запас для промпта)
MAX_CHUNK_CHARS = 10000

import re

def split_into_chunks(text: str, max_chars: int = MAX_CHUNK_CHARS) -> list:
    """Разбивает текст на чанки по Markdown-заголовкам, не превышая max_chars"""
    if len(text) <= max_chars:
        return [text]

    chunks = []
    # Разбиваем по заголовкам ## (второго уровня и ниже)
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

    # Если какой-то чанк всё ещё слишком большой — режем по абзацам
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


def translate_text(text: str, source_file: str) -> str:
    """Супер-быстрый перевод через Groq + Llama 3.1 70B"""

    # Проверка кеша (hashlib для стабильности между сессиями)
    cache_key = f"{source_file}:{hashlib.sha256(text.encode('utf-8')).hexdigest()[:16]}"
    if cache_key in cache:
        print(f"  ↻ Из кеша")
        return cache[cache_key]

    try:
        print(f"  🚀 Перевод через Groq (Llama 3.1 70B - супер быстро!)...")

        # Промпт для Llama с полным глоссарием Dynatrace
        prompt = f"""Переведи следующую техническую документацию Dynatrace с английского на русский.

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

        # Вызов Groq API с retry и exponential backoff
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = requests.post(
                    GROQ_API_URL,
                    headers={
                        'Content-Type': 'application/json',
                        'Authorization': f'Bearer {API_KEY}'
                    },
                    json={
                        'model': 'llama-3.3-70b-versatile',
                        'messages': [{
                            'role': 'user',
                            'content': prompt
                        }],
                        'temperature': 0.3,
                        'max_tokens': 8000,
                        'top_p': 1,
                        'stream': False
                    },
                    timeout=60
                )

                if response.status_code == 429:
                    # Rate limited — backoff
                    wait_time = 2 ** (attempt + 1)
                    print(f"  ⏳ Rate limit, жду {wait_time}с (попытка {attempt + 1}/{max_retries})...")
                    time.sleep(wait_time)
                    continue

                if response.status_code != 200:
                    print(f"  ❌ Ошибка API: {response.status_code} - {response.text[:200]}")
                    if attempt < max_retries - 1:
                        time.sleep(2 ** attempt)
                        continue
                    return text

                result = response.json()

                if 'choices' not in result or not result['choices']:
                    print(f"  ❌ Нет ответа от API")
                    return text

                translation = result['choices'][0]['message']['content'].strip()

                # Сохранение в кеш
                cache[cache_key] = translation

                # Задержка между запросами (Groq: 30 req/min)
                time.sleep(2.0)

                return translation

            except requests.Timeout:
                wait_time = 2 ** (attempt + 1)
                print(f"  ⏳ Таймаут, жду {wait_time}с (попытка {attempt + 1}/{max_retries})...")
                time.sleep(wait_time)
                continue
            except requests.ConnectionError:
                wait_time = 2 ** (attempt + 1)
                print(f"  ⏳ Ошибка соединения, жду {wait_time}с (попытка {attempt + 1}/{max_retries})...")
                time.sleep(wait_time)
                continue

        print(f"  ❌ Все {max_retries} попытки исчерпаны")
        return text

    except Exception as e:
        print(f"  ❌ Ошибка перевода: {str(e)}")
        return text  # Возвращаем оригинал при ошибке

def translate_file(en_file: Path):
    """Перевод одного файла"""

    # Путь к русскому файлу
    relative_path = en_file.relative_to(EN_DIR)
    ru_file = RU_DIR / relative_path

    print(f"\n📄 {relative_path}")

    # Проверка, нужен ли перевод
    if ru_file.exists():
        en_mtime = en_file.stat().st_mtime
        ru_mtime = ru_file.stat().st_mtime

        if ru_mtime > en_mtime:
            print(f"  ✓ Уже переведен (пропуск)")
            return

    # Чтение оригинала
    try:
        with open(en_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ❌ Ошибка чтения: {e}")
        return

    # Перевод с chunking для больших файлов
    if len(content) > MAX_CHUNK_CHARS:
        print(f"  📏 Большой файл ({len(content)} символов) - разбиваю на части...")
        chunks = split_into_chunks(content)
        translated_parts = []
        for ci, chunk in enumerate(chunks, 1):
            print(f"  📦 Часть {ci}/{len(chunks)}...")
            translated_parts.append(translate_text(chunk, f"{relative_path}#chunk{ci}"))
        translated = '\n\n'.join(translated_parts)
    else:
        translated = translate_text(content, str(relative_path))

    # Сохранение
    try:
        ru_file.parent.mkdir(parents=True, exist_ok=True)

        with open(ru_file, 'w', encoding='utf-8') as f:
            f.write(translated)

        print(f"  ✅ Переведено!")

    except Exception as e:
        print(f"  ❌ Ошибка записи: {e}")

def main():
    """Главная функция"""

    print("="*70)
    print("🚀 СУПЕР-БЫСТРЫЙ ПЕРЕВОД DYNATRACE ДОКУМЕНТАЦИИ")
    print("🤖 Модель: Groq Llama 3.1 70B")
    print("⚡ Скорость: В 10 РАЗ БЫСТРЕЕ обычного!")
    print("="*70)
    print()

    # Проверка API ключа
    if not API_KEY:
        print("❌ GROQ_API_KEY не задан!")
        print("📝 Получите бесплатный ключ на: https://console.groq.com")
        print("💡 Затем установите: set GROQ_API_KEY=gsk_your_key_here")
        return

    # Поиск всех английских файлов
    if not EN_DIR.exists():
        print(f"❌ Директория не найдена: {EN_DIR}")
        return

    en_files = list(EN_DIR.rglob('*.md'))

    if not en_files:
        print(f"❌ Нет файлов для перевода в {EN_DIR}")
        return

    print(f"📚 Найдено файлов: {len(en_files)}")
    print()

    # Перевод каждого файла
    translated = 0
    skipped = 0
    errors = 0

    start_time = time.time()

    for i, en_file in enumerate(en_files, 1):
        print(f"[{i}/{len(en_files)}]", end=" ")

        try:
            translate_file(en_file)
            translated += 1
        except KeyboardInterrupt:
            print("\n\n⚠️  Прервано пользователем")
            break
        except Exception as e:
            print(f"  ❌ Ошибка: {e}")
            errors += 1

        # Сохранение кеша каждые 10 файлов
        if i % 10 == 0:
            with open(CACHE_FILE, 'w', encoding='utf-8') as f:
                json.dump(cache, f, ensure_ascii=False, indent=2)

    # Финальное сохранение кеша
    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

    elapsed_time = time.time() - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)

    # Статистика
    print()
    print("="*70)
    print("📊 СТАТИСТИКА")
    print("="*70)
    print(f"✅ Переведено: {translated}")
    print(f"↻ Пропущено: {skipped}")
    print(f"❌ Ошибок: {errors}")
    print(f"⏱️  Время: {minutes}м {seconds}с")
    if translated > 0:
        avg_time = elapsed_time / translated
        print(f"⚡ Скорость: {avg_time:.1f}с на файл")
    print()
    print("💰 Стоимость: БЕСПЛАТНО! 🎉")
    print("🚀 Groq - самый быстрый бесплатный AI!")
    print()

if __name__ == '__main__':
    main()
