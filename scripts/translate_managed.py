#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Перевод файлов docs/managed/ (подкаталогов) на русский язык.
Использует Gemini Flash (1500 req/day бесплатно) + Groq + OpenRouter как fallback.

Запуск: cd scripts && python translate_managed.py [--limit 10] [--dry-run]

Файлы переводятся in-place (английский текст заменяется русским).
Уже переведённые файлы пропускаются (проверка по наличию кириллицы в заголовке).
"""

import os
import sys
import io
import json
import time
import re
import argparse
from pathlib import Path

# Fix Windows encoding
if sys.platform == 'win32':
    try:
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8', errors='replace')
            sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# Load .env
def _load_dotenv():
    env_paths = [
        Path(__file__).parent.parent / '.env',
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

import requests

GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')
GROQ_API_KEY = os.environ.get('GROQ_API_KEY', '')
OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY', '')

GEMINI_API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent'
GROQ_API_URL = 'https://api.groq.com/openai/v1/chat/completions'
OPENROUTER_API_URL = 'https://openrouter.ai/api/v1/chat/completions'
OPENROUTER_MODELS = [
    'google/gemma-3-27b-it:free',
    'meta-llama/llama-3.3-70b-instruct:free',
    'qwen/qwen3-8b:free',
]

MANAGED_DIR = Path(__file__).parent.parent / 'docs' / 'managed'
CACHE_FILE = Path(__file__).parent / '.translation_cache_managed.json'

cache = {}
if CACHE_FILE.exists():
    with open(CACHE_FILE, 'r', encoding='utf-8') as f:
        cache = json.load(f)

MAX_CHUNK_CHARS = 10000

# Protected brand terms
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


def post_fix(text):
    fixes = {
        'Один Агент': 'OneAgent', 'ОдинАгент': 'OneAgent',
        'Активный шлюз': 'ActiveGate', 'Активгейт': 'ActiveGate',
        'Чистый путь': 'PurePath', 'Умная карта': 'Smartscape',
    }
    for wrong, correct in fixes.items():
        text = text.replace(wrong, correct)
    return text


PROMPT = """Переведи следующую техническую документацию Dynatrace с английского на русский.

ВАЖНО:
- Сохрани всё форматирование Markdown (заголовки #, списки, код, ссылки, таблицы)
- Сохрани YAML frontmatter (--- блок) — переведи только title
- Все слова вида __KEEP000__ — это плейсхолдеры. НЕ ПЕРЕВОДИ их!
- Переведи качественно и профессионально
- НЕ добавляй вводных фраз — сразу начинай с перевода
- Убери дублирование заголовков (если # заголовок повторяется 2 раза — оставь один)
- Убери строки "* Overview", "* X-min read", "* Published/Updated" — это мета-информация

Текст:

{text}"""


def translate_via_gemini(text):
    if not GEMINI_API_KEY:
        return None
    try:
        resp = requests.post(
            f'{GEMINI_API_URL}?key={GEMINI_API_KEY}',
            json={'contents': [{'parts': [{'text': PROMPT.format(text=text)}]}],
                  'generationConfig': {'temperature': 0.3, 'maxOutputTokens': 8192}},
            timeout=60
        )
        if resp.status_code == 429:
            return None
        if resp.ok:
            data = resp.json()
            return data['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        print(f'  Gemini error: {e}')
    return None


def translate_via_groq(text):
    if not GROQ_API_KEY:
        return None
    try:
        resp = requests.post(
            GROQ_API_URL,
            headers={'Authorization': f'Bearer {GROQ_API_KEY}', 'Content-Type': 'application/json'},
            json={'model': 'llama-3.3-70b-versatile',
                  'messages': [{'role': 'user', 'content': PROMPT.format(text=text)}],
                  'temperature': 0.3, 'max_tokens': 8192},
            timeout=60
        )
        if resp.status_code == 429:
            return None
        if resp.ok:
            return resp.json()['choices'][0]['message']['content']
    except Exception as e:
        print(f'  Groq error: {e}')
    return None


def translate_via_openrouter(text):
    if not OPENROUTER_API_KEY:
        return None
    for model in OPENROUTER_MODELS:
        try:
            resp = requests.post(
                OPENROUTER_API_URL,
                headers={'Authorization': f'Bearer {OPENROUTER_API_KEY}', 'Content-Type': 'application/json'},
                json={'model': model,
                      'messages': [{'role': 'user', 'content': PROMPT.format(text=text)}],
                      'temperature': 0.3, 'max_tokens': 8192},
                timeout=60
            )
            if resp.status_code == 429:
                continue
            if resp.ok:
                return resp.json()['choices'][0]['message']['content']
        except Exception:
            continue
    return None


def translate_text(text):
    """Переводит текст, пробуя Gemini -> Groq -> OpenRouter."""
    protected, mapping = protect_terms(text)

    result = translate_via_gemini(protected)
    if result is None:
        result = translate_via_groq(protected)
    if result is None:
        result = translate_via_openrouter(protected)
    if result is None:
        return None

    result = restore_terms(result, mapping)
    result = post_fix(result)
    return result


def is_already_translated(content):
    """Проверяет наличие кириллицы в заголовке (значит уже переведён)."""
    for line in content.split('\n'):
        if line.startswith('# '):
            return bool(re.search('[а-яА-ЯёЁ]', line))
    return False


def is_error_page(content):
    """Проверяет, является ли файл страницей 404 или мусором."""
    return '404' in content[:200] and ("can't find" in content[:200].lower() or 'self.__next_f' in content)


def find_files_to_translate():
    """Находит все MD файлы в подкаталогах managed/, которые нужно перевести."""
    files = []
    for md_file in sorted(MANAGED_DIR.rglob('*.md')):
        # Пропускаем top-level файлы (уже переведены вручную)
        if md_file.parent == MANAGED_DIR:
            continue
        content = md_file.read_text(encoding='utf-8')
        if is_error_page(content):
            continue
        if is_already_translated(content):
            continue
        if len(content.strip()) < 50:
            continue
        files.append(md_file)
    return files


def main():
    parser = argparse.ArgumentParser(description='Перевод managed/ документации на русский')
    parser.add_argument('--limit', type=int, default=0, help='Максимум файлов для перевода (0 = все)')
    parser.add_argument('--dry-run', action='store_true', help='Только показать список файлов')
    args = parser.parse_args()

    files = find_files_to_translate()
    print(f'Найдено файлов для перевода: {len(files)}')

    if args.dry_run:
        for f in files[:30]:
            rel = f.relative_to(MANAGED_DIR)
            print(f'  {rel}')
        if len(files) > 30:
            print(f'  ... и ещё {len(files) - 30} файлов')
        return

    apis = []
    if GEMINI_API_KEY:
        apis.append('Gemini')
    if GROQ_API_KEY:
        apis.append('Groq')
    if OPENROUTER_API_KEY:
        apis.append('OpenRouter')
    print(f'Доступные API: {", ".join(apis) or "НЕТ! Установите ключи в .env"}')

    if not apis:
        print('Ошибка: нет доступных API ключей')
        sys.exit(1)

    limit = args.limit if args.limit > 0 else len(files)
    translated = 0
    errors = 0

    for i, md_file in enumerate(files[:limit]):
        rel = md_file.relative_to(MANAGED_DIR)
        print(f'\n[{i+1}/{min(limit, len(files))}] {rel}')

        content = md_file.read_text(encoding='utf-8')

        # Check cache
        import hashlib
        content_hash = hashlib.md5(content.encode()).hexdigest()
        if content_hash in cache:
            print('  [cache] Используем кешированный перевод')
            md_file.write_text(cache[content_hash], encoding='utf-8')
            translated += 1
            continue

        # Translate
        result = translate_text(content)
        if result is None:
            print('  [ERROR] Не удалось перевести (все API недоступны)')
            errors += 1
            time.sleep(5)
            continue

        # Save
        md_file.write_text(result, encoding='utf-8')
        cache[content_hash] = result
        translated += 1
        print(f'  [OK] Переведён ({len(content)} -> {len(result)} chars)')

        # Save cache periodically
        if translated % 10 == 0:
            with open(CACHE_FILE, 'w', encoding='utf-8') as f:
                json.dump(cache, f, ensure_ascii=False)

        # Rate limit: ~2 sec between requests
        time.sleep(2)

    # Save final cache
    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(cache, f, ensure_ascii=False)

    print(f'\n{"="*50}')
    print(f'Итого: переведено {translated}, ошибок {errors}, осталось {len(files) - limit}')


if __name__ == '__main__':
    main()
