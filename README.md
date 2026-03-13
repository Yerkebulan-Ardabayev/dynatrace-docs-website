# Dynatrace Documentation - Русская версия с AI-переводом

Автоматизированная документация Dynatrace с переводом на русский через AI (Gemini, Groq, OpenRouter) и ежедневной синхронизацией.

[![Deploy](https://github.com/Yerkebulan-Ardabayev/dynatrace-docs-website/actions/workflows/deploy.yml/badge.svg)](https://github.com/Yerkebulan-Ardabayev/dynatrace-docs-website/actions/workflows/deploy.yml)
[![Update](https://github.com/Yerkebulan-Ardabayev/dynatrace-docs-website/actions/workflows/update-docs.yml/badge.svg)](https://github.com/Yerkebulan-Ardabayev/dynatrace-docs-website/actions/workflows/update-docs.yml)

**Сайт:** https://yerkebulan-ardabayev.github.io/dynatrace-docs-website/

## Что делает проект

- Скрейпит документацию с docs.dynatrace.com
- Переводит на русский через AI (3 провайдера с fallback)
- Публикует на GitHub Pages автоматически
- Обновляется каждый день в 02:00 (Алматы)

## Архитектура пайплайна

```
Scrape -> Diff -> Translate -> Nav Update -> Validate -> Deploy
  |         |        |             |            |          |
  v         v        v             v            v          v
docs/en/  хеши    docs/ru/     mkdocs.yml   ссылки    gh-pages
          контента  Gemini ->    en/ -> ru/   CJK
                    Groq ->                   markdown
                    OpenRouter
```

Все этапы работают в одном CI job (файлы не теряются между этапами).
При исчерпании квоты API перевод останавливается gracefully - то что переведено деплоится, остальное переводится на следующий день.

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

### Тонкий клон (экономия места на ноутбуке)

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
2. Settings -> Secrets -> добавить `GEMINI_API_KEY`
3. Settings -> Pages -> Source: `gh-pages` branch
4. CI будет автоматически обновлять вашу копию

## API ключи

Для перевода нужен хотя бы один ключ (все бесплатные):

| Провайдер | Лимит | Где получить |
|-----------|-------|-------------|
| **Gemini** (основной) | 1500 req/day | https://aistudio.google.com/apikey |
| **Groq** (резервный) | ~100K tokens/day | https://console.groq.com |
| **OpenRouter** (запасной) | 50 req/day (free tier) | https://openrouter.ai/keys |

### Настройка локально

```bash
cp .env.example .env
# Отредактировать .env:
# GEMINI_API_KEY=your_key
# GROQ_API_KEY=your_key
```

### Настройка в GitHub Actions

```
Repo -> Settings -> Secrets and variables -> Actions -> New repository secret:
  GEMINI_API_KEY
  GROQ_API_KEY
  OPENROUTER_API_KEY  (опционально)
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
├── .gitattributes             # Git LFS для изображений
└── .env.example               # Шаблон переменных окружения
```

## Как работает перевод

1. **Diff по хешам** - переводятся только изменённые файлы
2. **Fallback chain** - Gemini -> Groq -> OpenRouter (автоматическое переключение)
3. **Graceful quota** - при исчерпании токенов: переведённое деплоится, остальное ждёт следующий день
4. **Кэш** - SHA256 хеш контента, TTL 30 дней, повторный перевод не нужен
5. **Терминология** - 100+ записей: Dynatrace, OneAgent, Davis остаются без перевода
6. **Валидация** - проверка CJK-символов, битых ссылок, структуры markdown

## Требования

- Python 3.8+
- Git (с LFS для изображений)
- Хотя бы один API ключ (Gemini / Groq / OpenRouter)

```bash
pip install -r requirements.txt
```

## Автор

**Yerkebulan Ardabayev** - [@Yerkebulan-Ardabayev](https://github.com/Yerkebulan-Ardabayev)

## Лицензия

MIT License
