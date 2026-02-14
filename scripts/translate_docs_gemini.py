#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
КАЧЕСТВЕННЫЙ перевод документации Dynatrace с помощью Gemini API
БЕСПЛАТНО и качественно!
"""

import os
import sys
import json
import time
import hashlib
import requests
from pathlib import Path

# API ключ берётся ТОЛЬКО из переменной окружения
API_KEY = os.environ.get('GEMINI_API_KEY', '')
GEMINI_API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent'

# Директории
DOCS_DIR = Path('../docs')
EN_DIR = DOCS_DIR / 'en'
RU_DIR = DOCS_DIR / 'ru'

# Кеш переводов
CACHE_FILE = Path('.translation_cache_gemini.json')
cache = {}

if CACHE_FILE.exists():
    with open(CACHE_FILE, 'r', encoding='utf-8') as f:
        cache = json.load(f)

def translate_text(text: str, source_file: str) -> str:
    """Качественный перевод текста с помощью Gemini"""

    # Проверка кеша (hashlib для стабильности между сессиями)
    cache_key = f"{source_file}:{hashlib.sha256(text.encode('utf-8')).hexdigest()[:16]}"
    if cache_key in cache:
        print(f"  ↻ Из кеша")
        return cache[cache_key]

    try:
        print(f"  🤖 Перевод через Gemini API (бесплатно)...")

        # Промпт для Gemini с полным глоссарием Dynatrace
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

Текст для перевода:

{text}

Переведенный текст:"""

        # Вызов Gemini API с retry и exponential backoff
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = requests.post(
                    f'{GEMINI_API_URL}?key={API_KEY}',
                    headers={'Content-Type': 'application/json'},
                    json={
                        'contents': [{
                            'parts': [{
                                'text': prompt
                            }]
                        }],
                        'generationConfig': {
                            'temperature': 0.3,
                            'maxOutputTokens': 8000,
                        }
                    },
                    timeout=60
                )

                if response.status_code == 429:
                    wait_time = 2 ** (attempt + 1)
                    print(f"  ⏳ Rate limit, жду {wait_time}с (попытка {attempt + 1}/{max_retries})...")
                    time.sleep(wait_time)
                    continue

                if response.status_code != 200:
                    print(f"  ❌ Ошибка API: {response.status_code}")
                    if attempt < max_retries - 1:
                        time.sleep(2 ** attempt)
                        continue
                    return text

                result = response.json()

                if 'candidates' not in result or not result['candidates']:
                    print(f"  ❌ Нет ответа от API")
                    return text

                translation = result['candidates'][0]['content']['parts'][0]['text'].strip()

                # Сохранение в кеш
                cache[cache_key] = translation

                # Задержка для rate limiting (Gemini free tier: 60 req/min)
                time.sleep(1.5)

                return translation

            except requests.Timeout:
                wait_time = 2 ** (attempt + 1)
                print(f"  ⏳ Таймаут, жду {wait_time}с (попытка {attempt + 1}/{max_retries})...")
                time.sleep(wait_time)
                continue
            except requests.ConnectionError:
                wait_time = 2 ** (attempt + 1)
                print(f"  ⏳ Ошибка соединения, жду {wait_time}с...")
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

    # Перевод
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
    print("🌍 КАЧЕСТВЕННЫЙ ПЕРЕВОД DYNATRACE ДОКУМЕНТАЦИИ")
    print("🤖 Модель: Gemini 1.5 Pro (БЕСПЛАТНО!)")
    print("="*70)
    print()

    # Проверка API ключа
    if not API_KEY:
        print("❌ GEMINI_API_KEY не задан!")
        print("📝 Получите бесплатный ключ на: https://aistudio.google.com/apikey")
        print("💡 Затем установите: set GEMINI_API_KEY=AIza...")
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

    # Статистика
    print()
    print("="*70)
    print("📊 СТАТИСТИКА")
    print("="*70)
    print(f"✅ Переведено: {translated}")
    print(f"↻ Пропущено: {skipped}")
    print(f"❌ Ошибок: {errors}")
    print()
    print("💰 Стоимость: БЕСПЛАТНО! 🎉")
    print()

if __name__ == '__main__':
    main()
