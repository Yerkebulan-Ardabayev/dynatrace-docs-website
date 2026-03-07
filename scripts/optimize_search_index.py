#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Оптимизация search_index.json после mkdocs build.
Удаляет тяжёлые/ненужные записи и обрезает текст для быстрой загрузки.

Запуск: python scripts/optimize_search_index.py
"""

import json
import sys
from pathlib import Path

SITE_DIR = Path(__file__).parent.parent / 'site'
INDEX_PATH = SITE_DIR / 'search' / 'search_index.json'

# Префиксы для исключения
EXCLUDE_PREFIXES = ('notebooklm/', 'DYNATRACE_MANAGED_FULL/')

# Максимальная длина текста на запись
MAX_TEXT_LENGTH = 200


def optimize():
    if not INDEX_PATH.exists():
        print(f"search_index.json not found at {INDEX_PATH}")
        sys.exit(1)

    original_size = INDEX_PATH.stat().st_size
    data = json.loads(INDEX_PATH.read_text(encoding='utf-8'))
    docs = data.get('docs', [])
    original_count = len(docs)

    optimized = []
    for doc in docs:
        location = doc.get('location', '')

        # Исключаем ненужные разделы
        if any(location.startswith(p) for p in EXCLUDE_PREFIXES):
            continue

        # Исключаем якорные записи (дубли с #)
        if '#' in location:
            continue

        # Обрезаем текст
        text = doc.get('text', '')
        if len(text) > MAX_TEXT_LENGTH:
            doc['text'] = text[:MAX_TEXT_LENGTH]

        optimized.append(doc)

    data['docs'] = optimized
    INDEX_PATH.write_text(json.dumps(data, ensure_ascii=False), encoding='utf-8')

    new_size = INDEX_PATH.stat().st_size
    print(f"Search index optimized:")
    print(f"  Entries: {original_count} -> {len(optimized)}")
    print(f"  Size: {original_size / 1024 / 1024:.1f} MB -> {new_size / 1024:.0f} KB")


if __name__ == '__main__':
    optimize()
