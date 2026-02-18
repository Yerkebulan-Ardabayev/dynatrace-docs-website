#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Автоматически обновляет mkdocs.yml nav на основе переведённых ru/ файлов.
Генерирует навигацию которая включает все файлы из docs/ru/
"""

import sys
import io
import os
import re
from pathlib import Path

if sys.platform == 'win32':
    try:
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8', errors='replace')
            sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

BASE_DIR = Path(__file__).parent.parent
DOCS_DIR = BASE_DIR / 'docs'
RU_DIR = DOCS_DIR / 'ru'
EN_DIR = DOCS_DIR / 'en'
MKDOCS_YML = BASE_DIR / 'mkdocs.yml'

# Человекочитаемые названия для разделов
SECTION_NAMES = {
    'dynatrace-intelligence': 'ИИ и аналитика',
    'deliver': 'Развёртывание',
    'analyze-explore-automate': 'Анализ и автоматизация',
    'observe': 'Мониторинг',
    'license': 'Лицензирование',
    'platform': 'Платформа',
    'discover-dynatrace': 'Знакомство',
    'whats-new': 'Что нового',
    'ingest-from': 'Источники данных',
    'secure': 'Безопасность',
    'manage': 'Управление',
    'managed': 'Managed',
    # Subsections
    'anomaly-detection': 'Обнаружение аномалий',
    'copilot': 'Copilot',
    'use-cases': 'Примеры использования',
    'configuration-as-code': 'Конфигурация как код',
    'monaco': 'Monaco',
    'terraform': 'Terraform',
    'ownership': 'Владение',
    'service-level-objectives': 'SLO',
    'site-reliability-guardian': 'SRG',
    'release-monitoring': 'Мониторинг релизов',
    'deliver-pipeline': 'CI/CD',
    'dashboards-and-notebooks': 'Дашборды',
    'logs': 'Логи',
    'notifications-and-alerting': 'Уведомления',
    'grail': 'Grail',
    'anomaly-detection-app': 'Приложение',
    'metric-events': 'Метрики',
    'adjust-sensitivity-anomaly-detection': 'Настройка',
    'root-cause-analysis': 'Анализ причин',
    'davis-problems-app': 'Davis Problems',
    'dynatrace-intelligence-integrations': 'Интеграции',
    'reference': 'Справочник',
    'ai-models': 'AI модели',
    'lma-logs-app': 'LMA Logs',
    'application-observability': 'Приложения',
    'infrastructure-observability': 'Инфраструктура',
    'digital-experience': 'Digital Experience',
    'container-platform-monitoring': 'Kubernetes',
    'kubernetes-app': 'Kubernetes App',
    'cloud-platform-monitoring': 'Облако',
    'databases': 'Базы данных',
    'services': 'Сервисы',
    'synthetic-monitoring': 'Синтетика',
    'dynatrace-oneagent': 'OneAgent',
    'threat-observability': 'Угрозы',
    'pipeline-observability-sdlc-events': 'Pipeline',
    'tutorials': 'Туториалы',
    'configuration': 'Конфигурация',
    'ready-made-documents': 'Готовые документы',
    'log-analytics': 'Log Analytics',
    'capabilities': 'Возможности',
    'synthetic-on-grail': 'Synthetic on Grail',
}

# Названия для конкретных файлов
FILE_NAMES = {
    'index.md': 'Обзор',
    'getting-started.md': 'Начало работы',
    'whats-new.md': 'Что нового',
    'dynatrace-api.md': 'API Dynatrace',
    'dynatrace-intelligence.md': 'ИИ Dynatrace',
    'ingest-from.md': 'Источники данных',
    'license.md': 'Лицензирование',
    'semantic-dictionary.md': 'Словарь',
    'faq.md': 'FAQ',
    'overview.md': 'Обзор',
    'reference.md': 'Справочник',
    'quickstart.md': 'Быстрый старт',
    'tutorial.md': 'Туториал',
    'configuration.md': 'Конфигурация',
    'installation.md': 'Установка',
    'setup.md': 'Настройка',
    'monitor.md': 'Мониторинг',
    'copilot-faq.md': 'FAQ по Copilot',
    'groq.md': 'Groq AI',
}


def get_display_name(path_part: str) -> str:
    """Получить человекочитаемое название для пути."""
    if path_part in SECTION_NAMES:
        return SECTION_NAMES[path_part]
    if path_part in FILE_NAMES:
        return FILE_NAMES[path_part]
    # Try to get name from file content
    return path_part.replace('-', ' ').replace('_', ' ').title()


def get_file_title(filepath: Path) -> str:
    """Попробовать прочитать заголовок из файла."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('# '):
                    title = line[2:].strip()
                    # Limit length
                    if len(title) > 60:
                        title = title[:57] + '...'
                    return title
                if line and not line.startswith('---') and not line.startswith('title:') and not line.startswith('source:'):
                    if len(line) > 5:
                        break
    except Exception:
        pass
    return None


def build_nav_tree(directory: Path, base_docs: Path, depth=0) -> list:
    """Рекурсивно строит nav-дерево из директории."""
    items = []

    if not directory.exists():
        return items

    # Get all items sorted: files first (index.md first), then dirs
    all_items = list(directory.iterdir())

    md_files = sorted([f for f in all_items if f.is_file() and f.suffix == '.md'],
                      key=lambda f: (f.name != 'index.md', f.name))
    subdirs = sorted([d for d in all_items if d.is_dir()])

    for f in md_files:
        rel_path = f.relative_to(base_docs).as_posix()
        # Try to get display name
        name = FILE_NAMES.get(f.name) or get_file_title(f) or get_display_name(f.stem)
        items.append({name: rel_path})

    for d in subdirs:
        subname = get_display_name(d.name)
        subtree = build_nav_tree(d, base_docs, depth + 1)
        if subtree:
            items.append({subname: subtree})

    return items


def nav_to_yaml(nav_items, indent=0) -> str:
    """Конвертирует nav-дерево в YAML строку."""
    lines = []
    prefix = '  ' * indent

    for item in nav_items:
        for key, value in item.items():
            if isinstance(value, str):
                # Leaf node (file)
                lines.append(f"{prefix}- {key}: {value}")
            elif isinstance(value, list):
                # Section with children
                lines.append(f"{prefix}- {key}:")
                for child in value:
                    lines.append(nav_to_yaml([child], indent + 1))

    return '\n'.join(lines)


def main():
    print("=" * 60)
    print("Обновление nav в mkdocs.yml")
    print("=" * 60)

    # Count translated files
    ru_files = list(RU_DIR.rglob('*.md'))
    print(f"Найдено {len(ru_files)} переведённых файлов в docs/ru/")

    # Build nav for ru/ content
    ru_nav = build_nav_tree(RU_DIR, DOCS_DIR)

    if not ru_nav:
        print("❌ Нет файлов в docs/ru/")
        return

    # Generate YAML for the ru section
    ru_nav_yaml = nav_to_yaml(ru_nav, indent=2)

    print("\nГенерирую nav секцию для переведённых файлов...")
    print(f"Секций верхнего уровня: {len(ru_nav)}")

    # Read current mkdocs.yml
    with open(MKDOCS_YML, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the nav section and the ru/ section if it exists
    # We'll add/replace the 📚 Документация (RU) section

    ru_section = f"""
  # ПЕРЕВЕДЁННАЯ ДОКУМЕНТАЦИЯ (RU)
  - 📚 Документация:
{ru_nav_yaml}"""

    # Check if ru section already exists
    if '# ПЕРЕВЕДЁННАЯ ДОКУМЕНТАЦИЯ (RU)' in content:
        # Replace existing
        old_start = content.index('  # ПЕРЕВЕДЁННАЯ ДОКУМЕНТАЦИЯ (RU)')
        # Find next top-level nav entry or end
        rest = content[old_start:]
        # Find next section at same indent level
        next_section = re.search(r'\n  - [^\s]', rest[10:])
        if next_section:
            old_end = old_start + 10 + next_section.start()
            content = content[:old_start] + ru_section + '\n' + content[old_end:]
        else:
            # It's the last section, find where nav ends
            nav_end = content.find('\nmarkdown_extensions:')
            content = content[:old_start] + ru_section + '\n\n' + content[nav_end:]
        print("✅ Обновлена существующая секция документации")
    else:
        # Insert before AI section or before markdown_extensions
        insert_before = '  # AI\n'
        if insert_before in content:
            content = content.replace(insert_before, ru_section + '\n\n  # AI\n')
        else:
            # Insert before markdown_extensions
            content = content.replace('\nmarkdown_extensions:', ru_section + '\n\nmarkdown_extensions:')
        print("✅ Добавлена новая секция документации")

    # Write back
    with open(MKDOCS_YML, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n✅ mkdocs.yml обновлён!")
    print(f"   Добавлено {len(ru_files)} файлов в nav")
    print(f"\nДля проверки запустите: mkdocs build")


if __name__ == '__main__':
    main()
