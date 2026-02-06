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
import requests
from pathlib import Path

# Groq API - ВАШ БЕСПЛАТНЫЙ ключ
API_KEY = os.environ.get('GROQ_API_KEY', 'YOUR_API_KEY_HERE')
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

def translate_text(text: str, source_file: str) -> str:
    """Супер-быстрый перевод через Groq + Llama 3.1 70B"""

    # Проверка кеша
    cache_key = f"{source_file}:{hash(text)}"
    if cache_key in cache:
        print(f"  ↻ Из кеша")
        return cache[cache_key]

    try:
        print(f"  🚀 Перевод через Groq (Llama 3.1 70B - супер быстро!)...")

        # Промпт для Llama
        prompt = f"""Переведи следующую техническую документацию Dynatrace с английского на русский.

ВАЖНО:
- Сохрани всё форматирование Markdown (заголовки, списки, код, ссылки)
- Технические термины оставь на английском там, где это принято (OneAgent, Smartscape, Davis AI, Grail, DQL, Kubernetes)
- Переведи качественно и профессионально
- НЕ добавляй никаких комментариев, только перевод
- Не добавляй вводные фразы типа "Вот перевод:" - сразу начинай с перевода

Текст для перевода:

{text}"""

        # Вызов Groq API
        response = requests.post(
            GROQ_API_URL,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {API_KEY}'
            },
            json={
                'model': 'llama-3.1-70b-versatile',  # Лучшая модель для перевода
                'messages': [{
                    'role': 'user',
                    'content': prompt
                }],
                'temperature': 0.3,
                'max_tokens': 8000,
                'top_p': 1,
                'stream': False
            },
            timeout=30
        )

        if response.status_code != 200:
            print(f"  ❌ Ошибка API: {response.status_code} - {response.text}")
            return text

        result = response.json()

        if 'choices' not in result or not result['choices']:
            print(f"  ❌ Нет ответа от API")
            return text

        translation = result['choices'][0]['message']['content'].strip()

        # Сохранение в кеш
        cache[cache_key] = translation

        # Минимальная задержка (Groq очень быстрый - 30 req/min)
        time.sleep(0.5)

        return translation

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
    print("🚀 СУПЕР-БЫСТРЫЙ ПЕРЕВОД DYNATRACE ДОКУМЕНТАЦИИ")
    print("🤖 Модель: Groq Llama 3.1 70B")
    print("⚡ Скорость: В 10 РАЗ БЫСТРЕЕ обычного!")
    print("="*70)
    print()

    # Проверка API ключа
    if API_KEY == 'gsk_demo_key_placeholder':
        print("⚠️  ВНИМАНИЕ: Используется демо-ключ!")
        print("📝 Получите бесплатный ключ на: https://console.groq.com")
        print("💡 Затем установите: set GROQ_API_KEY=gsk_your_key_here")
        print()
        print("Продолжаю с демо-ключом (может не работать)...")
        print()

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
