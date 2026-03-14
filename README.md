# Dynatrace Documentation - Русская версия

Документация Dynatrace на русском языке с автоматическим переводом и ежедневной синхронизацией.

[![Deploy](https://github.com/Yerkebulan-Ardabayev/dynatrace-docs-website/actions/workflows/deploy.yml/badge.svg)](https://github.com/Yerkebulan-Ardabayev/dynatrace-docs-website/actions/workflows/deploy.yml)
[![Update](https://github.com/Yerkebulan-Ardabayev/dynatrace-docs-website/actions/workflows/update-docs.yml/badge.svg)](https://github.com/Yerkebulan-Ardabayev/dynatrace-docs-website/actions/workflows/update-docs.yml)

**Сайт:** https://yerkebulan-ardabayev.github.io/dynatrace-docs-website/

## Что делает проект

- Скрейпит документацию с docs.dynatrace.com
- Переводит на русский язык через AI
- Публикует на GitHub Pages автоматически
- Обновляется каждый день в 02:00 (Алматы)

## Архитектура пайплайна

```
Scrape -> Diff -> Translate -> Nav Update -> Validate -> Deploy
  |         |        |             |            |          |
  v         v        v             v            v          v
docs/en/  хеши    docs/ru/     mkdocs.yml   ссылки    gh-pages
          контента  AI-перевод   en/ -> ru/   CJK
                    с fallback               markdown
```

Все этапы работают в одном CI job (файлы не теряются между этапами).
При исчерпании квоты API перевод останавливается gracefully — переведённое деплоится, остальное переводится на следующий день.

## Быстрый старт

### Посмотреть сайт

Просто откройте: https://yerkebulan-ardabayev.github.io/dynatrace-docs-website/

### Развернуть локально

```bash
git clone https://github.com/Yerkebulan-Ardabayev/dynatrace-docs-website.git
cd dynatrace-docs-website
pip install -r requirements.txt
mkdocs serve
# Открыть http://127.0.0.1:8000
```

### Тонкий клон (экономия места)

```bash
bash scripts/setup_thin_clone.sh \
  https://github.com/Yerkebulan-Ardabayev/dynatrace-docs-website.git \
  ~/docs-thin

cd ~/docs-thin
pip install -r requirements.txt
mkdocs serve
```

Sparse checkout загружает только `scripts/`, `docs/ru/`, конфиги. Без `docs/en/` и истории.

### Fork (своя копия с автообновлением)

1. Fork репозитория на GitHub
2. Settings -> Secrets -> добавить API ключ для AI-перевода
3. Settings -> Pages -> Source: `gh-pages` branch
4. CI будет автоматически обновлять вашу копию

## AI-перевод

Для автоматического перевода можно использовать любой совместимый AI API. Настройте ключ в переменных окружения:

```bash
cp .env.example .env
# Отредактировать .env — указать свой API ключ
```

В GitHub Actions:

```
Repo -> Settings -> Secrets and variables -> Actions -> New repository secret
```

## Запуск пайплайна

### Автоматически (CI/CD)

Пайплайн запускается:
- Каждый день в 02:00 (Алматы) / 21:00 UTC
- Вручную: Actions -> Update & Translate Documentation -> Run workflow

### Локально

```bash
# Полный пайплайн (scrape + translate + deploy)
python scripts/sync_and_deploy.py

# Только перевод (без скрейпинга)
python scripts/sync_and_deploy.py --skip-scrape

# Тестовый прогон (без push)
python scripts/sync_and_deploy.py --dry-run

# Принудительный переперевод
python scripts/sync_and_deploy.py --force --skip-scrape
```

### CLI команды

```bash
python scripts/pipeline/run_pipeline.py scrape --max-pages 100
python scripts/pipeline/run_pipeline.py translate --target-lang ru
python scripts/pipeline/run_pipeline.py validate
python scripts/pipeline/run_pipeline.py nav-stats
python scripts/pipeline/run_pipeline.py nav-upgrade --apply
python scripts/pipeline/run_pipeline.py cache-stats
python scripts/pipeline/run_pipeline.py cache-clean
```

## Структура проекта

```
dynatrace-docs-website/
├── docs/
│   ├── en/                    # Английские доки (скрейпятся автоматически)
│   ├── ru/                    # Русские доки (AI-перевод)
│   ├── assets/                # Стили, скрипты, изображения
│   └── index.md
├── scripts/
│   ├── pipeline/              # Модули пайплайна
│   │   ├── config.py          # Конфигурация (пути, API, лимиты)
│   │   ├── translator.py      # Мульти-провайдер перевод с fallback
│   │   ├── cache_manager.py   # Кэш переводов (SHA256, TTL 30 дней)
│   │   ├── validator.py       # Валидация (ссылки, CJK, markdown)
│   │   ├── nav_updater.py     # Обновление навигации en/ -> ru/
│   │   ├── terminology.py     # Словарь терминов (100+ записей)
│   │   └── run_pipeline.py    # CLI точка входа
│   ├── scrape_docs.py         # Скрейпер docs.dynatrace.com
│   ├── sync_and_deploy.py     # Единый оркестратор пайплайна
│   └── setup_thin_clone.sh    # Настройка тонкого клона
├── .github/workflows/
│   ├── update-docs.yml        # Ежедневный scrape + translate + deploy
│   └── deploy.yml             # Deploy на push в main
├── mkdocs.yml                 # Конфигурация MkDocs Material
├── requirements.txt           # Python зависимости
└── .env.example               # Шаблон переменных окружения
```

## Как работает перевод

1. **Diff по хешам** — переводятся только изменённые файлы
2. **Fallback chain** — автоматическое переключение при ошибках
3. **Graceful quota** — при исчерпании токенов: переведённое деплоится, остальное ждёт следующий день
4. **Кэш** — SHA256 хеш контента, TTL 30 дней, повторный перевод не нужен
5. **Терминология** — 100+ записей: Dynatrace, OneAgent, Davis остаются без перевода
6. **Валидация** — проверка CJK-символов, битых ссылок, структуры markdown

## Требования

- Python 3.8+
- Git
- API ключ для AI-перевода

```bash
pip install -r requirements.txt
```

## Автор

**Yerkebulan Ardabayev** — [@Yerkebulan-Ardabayev](https://github.com/Yerkebulan-Ardabayev)

## Лицензия

MIT License
