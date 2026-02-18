#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Автоматически обновляет mkdocs.yml nav на основе переведённых ru/ файлов.
Читает заголовки H1 из файлов и использует русские названия разделов.
"""

import sys
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
MKDOCS_YML = BASE_DIR / 'mkdocs.yml'

# Русские названия для разделов (папок)
SECTION_LABELS = {
    'analyze-explore-automate':          '🔍 Анализ и автоматизация',
    'deliver':                           '🚀 Развёртывание',
    'discover-dynatrace':                '💡 Знакомство с Dynatrace',
    'dynatrace-intelligence':            '🤖 ИИ и аналитика',
    'ingest-from':                       '📥 Источники данных',
    'license':                           '📋 Лицензирование',
    'manage':                            '⚙️ Управление',
    'managed':                           '🖥️ Managed',
    'observe':                           '👁️ Мониторинг',
    'platform':                          '🏗️ Платформа',
    'secure':                            '🔒 Безопасность',
    'whats-new':                         '🆕 Что нового',
    # Подразделы
    'anomaly-detection':                 'Обнаружение аномалий',
    'anomaly-detection-app':             'Приложение аномалий',
    'adjust-sensitivity-anomaly-detection': 'Настройка чувствительности',
    'metric-events':                     'События метрик',
    'root-cause-analysis':               'Анализ первопричин',
    'davis-problems-app':                'Davis Problems',
    'copilot':                           'Copilot',
    'use-cases':                         'Примеры использования',
    'ai-models':                         'AI модели',
    'dynatrace-intelligence-integrations': 'Интеграции ИИ',
    'configuration-as-code':             'Конфигурация как код',
    'monaco':                            'Monaco',
    'terraform':                         'Terraform',
    'ownership':                         'Владение',
    'service-level-objectives':          'SLO',
    'site-reliability-guardian':         'SRG',
    'release-monitoring':                'Мониторинг релизов',
    'deliver-pipeline':                  'CI/CD пайплайн',
    'dashboards-and-notebooks':          'Дашборды и ноутбуки',
    'logs':                              'Логи',
    'lma-logs-app':                      'Приложение журналов',
    'log-analytics':                     'Аналитика логов',
    'notifications-and-alerting':        'Уведомления и оповещения',
    'grail':                             'Grail',
    'reference':                         'Справочник',
    'application-observability':         'Наблюдаемость приложений',
    'infrastructure-observability':      'Наблюдаемость инфраструктуры',
    'digital-experience':                'Цифровой опыт',
    'container-platform-monitoring':     'Kubernetes мониторинг',
    'kubernetes-app':                    'Kubernetes App',
    'cloud-platform-monitoring':         'Облачный мониторинг',
    'databases':                         'Базы данных',
    'services':                          'Сервисы',
    'synthetic-monitoring':              'Синтетический мониторинг',
    'synthetic-on-grail':                'Synthetic on Grail',
    'dynatrace-oneagent':                'OneAgent',
    'threat-observability':              'Наблюдаемость угроз',
    'pipeline-observability-sdlc-events': 'Pipeline наблюдаемость',
    'tutorials':                         'Туториалы',
    'configuration':                     'Конфигурация',
    'ready-made-documents':              'Готовые документы',
    'capabilities':                      'Возможности',
    'explorer':                          'Обозреватель',
    'facets':                            'Фасеты',
    'problem-notifications':             'Уведомления о проблемах',
    'compliance-and-resilience':         'Соответствие требованиям',
    'dashboards-new':                    'Новые дашборды',
    'workflows':                         'Рабочие процессы',
}


def get_title(filepath: Path, max_len: int = 55) -> str:
    """Читает H1 заголовок из markdown файла, правильно пропуская frontmatter."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        i = 0
        n = len(lines)

        # Пропускаем YAML frontmatter (--- ... ---)
        if i < n and lines[i].strip() == '---':
            i += 1
            while i < n and lines[i].strip() != '---':
                i += 1
            i += 1  # пропускаем закрывающий ---

        # Ищем первый H1 в оставшемся тексте
        for j in range(i, min(i + 30, n)):
            stripped = lines[j].strip()
            if stripped.startswith('# '):
                title = stripped[2:].strip()
                # Убираем markdown-разметку
                title = re.sub(r'[*_`]', '', title)
                title = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', title)
                title = title.strip()
                if title:
                    if len(title) > max_len:
                        title = title[:max_len - 3] + '...'
                    return title
    except Exception:
        pass
    return None


FILE_FALLBACKS = {
    'index':               'Обзор',
    'overview':            'Обзор',
    'getting-started':     'Начало работы',
    'dynatrace-api':       'Dynatrace API',
    'dynatrace-intelligence': 'ИИ Dynatrace',
    'ingest-from':         'Источники данных',
    'license':             'Лицензирование',
    'semantic-dictionary': 'Семантический словарь',
    'whats-new':           'Что нового',
    'faq':                 'FAQ',
    'reference':           'Справочник',
    'quickstart':          'Быстрый старт',
    'tutorial':            'Туториал',
    'configuration':       'Конфигурация',
    'installation':        'Установка',
    'setup':               'Настройка',
}


def folder_label(name: str) -> str:
    """Возвращает русское название раздела или файла."""
    if name in SECTION_LABELS:
        return SECTION_LABELS[name]
    if name in FILE_FALLBACKS:
        return FILE_FALLBACKS[name]
    # Fallback: капитализация с заменой дефисов
    return name.replace('-', ' ').replace('_', ' ').title()


def build_nav(directory: Path, docs_base: Path) -> list:
    """Рекурсивно строит nav-дерево из директории."""
    if not directory.exists():
        return []

    all_items = list(directory.iterdir())
    md_files = sorted(
        [f for f in all_items if f.is_file() and f.suffix == '.md'],
        key=lambda f: (f.name != 'index.md', f.name.lower())
    )
    subdirs = sorted([d for d in all_items if d.is_dir()], key=lambda d: d.name.lower())

    items = []

    for f in md_files:
        rel_path = f.relative_to(docs_base).as_posix()
        title = get_title(f) or FILE_FALLBACKS.get(f.stem) or folder_label(f.stem)
        items.append({title: rel_path})

    for d in subdirs:
        subtree = build_nav(d, docs_base)
        if subtree:
            label = folder_label(d.name)
            items.append({label: subtree})

    return items


def nav_to_yaml(nav_items: list, indent: int = 0) -> str:
    """Конвертирует nav-дерево в YAML строки."""
    lines = []
    prefix = '    ' * indent  # 4 пробела на уровень

    for item in nav_items:
        for key, value in item.items():
            if isinstance(value, str):
                lines.append(f"{prefix}- \"{key}\": {value}")
            elif isinstance(value, list):
                lines.append(f"{prefix}- \"{key}\":")
                sub = nav_to_yaml(value, indent + 1)
                if sub:
                    lines.append(sub)

    return '\n'.join(filter(None, lines))


def main():
    print('=' * 60)
    print('  Обновление nav в mkdocs.yml (с русскими заголовками)')
    print('=' * 60)

    ru_files = list(RU_DIR.rglob('*.md'))
    print(f'\n  Найдено файлов в docs/ru/: {len(ru_files)}')

    ru_nav = build_nav(RU_DIR, DOCS_DIR)
    if not ru_nav:
        print('❌ docs/ru/ пуст!')
        return

    ru_nav_yaml = nav_to_yaml(ru_nav, indent=2)

    # Блок для вставки в mkdocs.yml
    ru_block = (
        '\n  # ПЕРЕВЕДЁННАЯ ДОКУМЕНТАЦИЯ (RU)\n'
        '  - "📚 Документация":\n'
        f'{ru_nav_yaml}'
    )

    with open(MKDOCS_YML, 'r', encoding='utf-8') as f:
        content = f.read()

    marker = '  # ПЕРЕВЕДЁННАЯ ДОКУМЕНТАЦИЯ (RU)'

    if marker in content:
        start = content.index(marker)
        rest_after = content[start + len(marker):]
        # Ищем следующий top-level nav entry (две пробела + дефис + не-пробел)
        m = re.search(r'\n  - [^\s]', rest_after)
        if m:
            end = start + len(marker) + m.start()
            content = content[:start] + ru_block + '\n' + content[end:]
        else:
            # Последняя секция nav — ищем конец nav
            nav_end_markers = ['\nmarkdown_extensions:', '\nplugins:', '\nextra:']
            end = len(content)
            for nm in nav_end_markers:
                idx = content.find(nm, start)
                if idx != -1 and idx < end:
                    end = idx
            content = content[:start] + ru_block + '\n\n' + content[end:]
        print('  ✅ Обновлена существующая RU-секция')
    else:
        # Вставляем перед markdown_extensions или в конец nav
        for anchor in ['\nmarkdown_extensions:', '\nplugins:']:
            if anchor in content:
                content = content.replace(anchor, ru_block + '\n' + anchor)
                break
        print('  ✅ Добавлена новая RU-секция')

    with open(MKDOCS_YML, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f'  ✅ mkdocs.yml обновлён! Файлов в nav: {len(ru_files)}')
    print('\n  Проверка: mkdocs build')


if __name__ == '__main__':
    main()
