# Инструкция проекта dynatrace-docs-website

> Последняя верификация: 2026-03-26 (рефакторинг: полное разделение Managed/SaaS)

## Контекст проекта

Автоматический скрейпинг англоязычной документации Dynatrace Managed, AI-перевод на русский язык и публикация на сайте.

- **Репозиторий**: [github.com/Yerkebulan-Ardabayev/dynatrace-docs-website](https://github.com/Yerkebulan-Ardabayev/dynatrace-docs-website)
- **Сайт**: [yerkebulan-ardabayev.github.io/dynatrace-docs-website](https://yerkebulan-ardabayev.github.io/dynatrace-docs-website/)
- **Автор**: Yerkebulan Ardabayev
- **Лицензия**: MIT

---

## Архитектура

| Компонент | Технология |
|---|---|
| Генератор сайта | MkDocs + Material for MkDocs (тема: `material`, язык: `ru`) |
| Хостинг | GitHub Pages (ветка `gh-pages`) |
| CI/CD | GitHub Actions — 2 workflow |
| Уведомления | Telegram Bot API (`TG_BOT_TOKEN` + `TG_CHAT_ID` в GitHub Secrets) |
| AI-перевод | Multi-provider: Gemini Flash → Groq (Llama 3.3 70B) → OpenRouter (fallback-цепочка) |
| AI-ассистент на сайте | Groq Chat Widget (`groq-chat.js`) — Llama 3.3 70B |
| Кэш переводов | JSON-файл, SHA256-хэши, TTL 30 дней |
| Очередь задач | SQLite (`.translation_queue.db`, WAL mode) |
| Метрики | Dynatrace Managed Metrics API v2 (`DT_MANAGED_URL`, `DT_API_TOKEN`) |
| Терминология | `scripts/terminology.yaml` — 100+ защищённых терминов |

---

## Структура репозитория

> **Важно**: Managed и SaaS документация строго разделены по папкам (без смешения).

```
dynatrace-docs-website/
├── docs/
│   ├── en/                    # SaaS — английские исходники (1 547 файлов .md)
│   ├── ru/                    # SaaS — русские переводы (1 547 файлов .md)
│   ├── managed/               # Managed — EN (263 файла .md)
│   ├── managed-ru/            # Managed — RU перевод (67 файлов .md)
│   ├── common/                # Общий контент (Managed + SaaS, 101 файл)
│   ├── notebooklm/            # NotebookLM-контент
│   ├── ai/                    # AI-ассистент (страница)
│   ├── assets/
│   │   ├── stylesheets/extra.css
│   │   ├── javascripts/groq-chat.js
│   │   └── ai-config.json     # Конфигурация AI-виджета
│   ├── overrides/main.html    # Кастомный шаблон Material
│   └── index.md               # Главная страница (RU)
├── scripts/
│   ├── scrape_docs.py         # Скрейпер docs.dynatrace.com → Markdown
│   ├── detect_changes.py      # Diff EN vs RU (SHA256 hash registry)
│   ├── organize_docs.py       # Организация скрейпнутых файлов
│   ├── place_translation.py   # Размещение перевода + обновление nav
│   ├── translate_docs_groq.py # Основной переводчик (multi-provider)
│   ├── translate_missing.py   # Перевод из списка missing
│   ├── translate_titles_only.py / translate_titles_parallel.py
│   ├── cleanup_docs.py        # Очистка дубликатов h1, BOM, метаданных
│   ├── fix_docs_links.py      # Фикс абсолютных ссылок → относительные
│   ├── validate_translations.py # Валидация качества перевода
│   ├── sanitize_secrets.py    # Удаление секретов перед коммитом
│   ├── sync_and_deploy.py     # Единый оркестратор пайплайна
│   ├── terminology.yaml       # Глоссарий защищённых терминов
│   ├── setup_thin_clone.sh    # Sparse checkout для экономии места
│   ├── .change_tracking/
│   │   └── hash_registry.json # Реестр хэшей для отслеживания изменений
│   ├── pipeline/              # Модуль пайплайна (11 файлов)
│   │   ├── config.py          # Централизованная конфигурация
│   │   ├── translator.py      # Multi-provider перевод с fallback
│   │   ├── cache_manager.py   # Кэш переводов (SHA256, TTL 30 дней)
│   │   ├── validator.py       # Валидатор документов и навигации
│   │   ├── nav_updater.py     # Обновление mkdocs.yml (en/ → ru/)
│   │   ├── terminology.py     # Движок терминологии (placeholder protection)
│   │   ├── job_queue.py       # SQLite очередь с retry + dead letter
│   │   ├── metrics_reporter.py # Отправка метрик в Dynatrace
│   │   ├── structured_logger.py # JSON Lines логирование
│   │   └── run_pipeline.py    # CLI: scrape, detect, place, validate, nav-stats
│   └── quality/               # Модуль качества
│       ├── test_docs.py       # Тесты: nav, ссылки, CJK, CSS artifacts
│       └── check_coverage.py  # Проверка покрытия (порог 80%)
├── .github/workflows/
│   ├── deploy.yml             # Deploy: push to main → validate → build → gh-pages
│   └── update-docs.yml        # Sync: daily 02:00 KZ → scrape → detect → issue → deploy
├── .skills/dynatrace-translate/SKILL.md  # Skill для Claude Cowork
├── mkdocs.yml                 # Конфигурация MkDocs (14 секций, 99 nav-записей)
├── requirements.txt           # Python-зависимости (12 пакетов)
├── .env.example               # Шаблон переменных окружения
└── README.md                  # Документация проекта
```

---

## Текущий статус (верифицировано 2026-03-26)

| Метрика | Значение |
|---|---|
| SaaS EN-файлов (`docs/en/`) | 1 547 |
| SaaS RU-файлов (`docs/ru/`) | 1 547 |
| Managed EN-файлов (`docs/managed/`) | 263 |
| Managed RU-файлов (`docs/managed-ru/`) | 67 |
| Общих файлов (`docs/common/`) | 101 |
| SaaS покрытие | **100%** (полный паритет EN = RU) |
| Managed RU покрытие | **25%** (67 из 263 переведены) |
| Nav-записей в mkdocs.yml | 99 ссылок на `.md` |
| Ссылок на `en/` в nav | **0** (вся навигация указывает на `ru/` и `managed/`) |
| Разделов в nav | 14 основных секций |
| Смешение Managed/SaaS | **0** (полное разделение) |

**SaaS секции** (`docs/en/`, `docs/ru/`): analyze-explore-automate, deliver, discover-dynatrace, dynatrace-api, dynatrace-intelligence, ingest-from, license, manage, observe, platform, secure, semantic-dictionary, whats-new

**Managed секции** (`docs/managed/`): analyze-explore-automate, deliver, discover-dynatrace, dynatrace-api, dynatrace-intelligence, ingest-from, license, manage, managed-cluster, observe, platform, secure, whats-new

---

## CI/CD: два workflow

### 1. `deploy.yml` — Deploy to GitHub Pages

- **Триггер**: push в main (docs/**, mkdocs.yml, scripts/**) + manual dispatch
- **Шаги**: validate (test_docs.py + pipeline validation) → build MkDocs → deploy gh-pages
- **Деплоер**: `peaceiris/actions-gh-pages@v4`

### 2. `update-docs.yml` — Update & Translate Documentation

- **Триггер**: cron `0 21 * * *` (ежедневно 02:00 по Казахстану) + manual dispatch
- **Inputs**: `max_pages` (default 1000), `skip_scrape` (boolean)
- **Timeout**: 30 минут
- **Шаги**:
  1. **Scrape**: `scrape_docs.py` — скачивает с docs.dynatrace.com
  2. **Verify**: минимум 5 файлов скрейпнуто (иначе fail)
  3. **Organize**: `organize_docs.py` — структурирование
  4. **Detect**: `detect_changes.py` — JSON + Markdown отчёт (новые/обновлённые)
  5. **Commit**: коммит EN-файлов в main
  6. **GitHub Issue**: создание Issue с лейблами `translation`, `documentation`, `automated`
  7. **Telegram**: уведомление (если есть изменения)
  8. **Validate**: проверка качества
  9. **Build & Deploy**: MkDocs build → gh-pages
  10. **Summary**: Step Summary с метриками

---

## Пайплайн перевода (полная схема)

### Автоматический путь (CI/CD)
```
Scrape → Detect Changes → Create Issue → [ожидание перевода] → Validate → Deploy
```

### Ручной перевод через Claude Cowork
```
Пользователь: «переведи observe/dashboards.md»
→ Claude читает docs/en/<path>
→ Загружает terminology.yaml (защищённые термины)
→ Переводит по правилам (см. ниже)
→ Пишет в docs/ru/<path>
→ Запускает place_translation.py (обновляет nav)
→ Пользователь делает git push
```

### Автоматический перевод через API
```
translate_docs_groq.py / translate_missing.py
→ Gemini Flash (primary) → Groq Llama 3.3 (fallback) → OpenRouter (last resort)
→ Chunk-based (max 10 000 символов)
→ Кэш (SHA256 + 30-day TTL)
→ Терминология (placeholder protection → перевод → restoration)
→ Валидация (CJK, CSS artifacts, ссылки, frontmatter)
```

---

## Правила перевода

### Терминология — НЕ переводить:
Все термины из `scripts/terminology.yaml` (100+): Dynatrace, OneAgent, ActiveGate, Grail, Davis, DQL, Smartscape, OpenPipeline, SaaS, Managed, Kubernetes, Docker, OpenTelemetry, AppEngine, и т.д.

### Markdown — сохранять:
- Все заголовки (#), ссылки [text](url), блоки кода, таблицы, списки
- Все примеры кода, CLI-команды, API-эндпоинты, пути к файлам
- YAML frontmatter (`---`) — переводить только поле `title:`
- Ссылки на изображения — без изменений

### Стиль:
- Профессиональный технический русский, формальный стиль (вы, не ты)
- Короткие, чёткие предложения
- Устоявшаяся русская IT-терминология где она существует
- Если нет хорошего русского эквивалента — оставить английский термин

### Проверки качества после перевода:
- Нет CJK-символов (китайские/японские/корейские)
- Нет CSS-артефактов (`.css-abc123-xyz`)
- Защищённые термины остались на английском
- Все markdown-ссылки целые
- Файл не пустой / не только frontmatter

---

## Переменные окружения

| Переменная | Назначение | Где хранится |
|---|---|---|
| `GROQ_API_KEY` | Groq API (перевод + чат-виджет) | GitHub Secrets / .env |
| `GEMINI_API_KEY` | Google Gemini Flash (primary translator) | GitHub Secrets / .env |
| `OPENROUTER_API_KEY` | OpenRouter (last-resort fallback) | GitHub Secrets / .env |
| `TG_BOT_TOKEN` | Telegram Bot (уведомления) | GitHub Secrets |
| `TG_CHAT_ID` | Telegram Chat ID | GitHub Secrets |
| `DT_MANAGED_URL` | Dynatrace Managed URL (метрики) | GitHub Secrets |
| `DT_API_TOKEN` | Dynatrace API Token (метрики) | GitHub Secrets |

---

## CLI-команды пайплайна

```bash
# Основной оркестратор
python scripts/sync_and_deploy.py [--skip-scrape] [--dry-run] [--force]

# Отдельные команды через run_pipeline.py
python scripts/pipeline/run_pipeline.py scrape       # Скрейпинг
python scripts/pipeline/run_pipeline.py detect       # Обнаружение изменений
python scripts/pipeline/run_pipeline.py place        # Размещение перевода
python scripts/pipeline/run_pipeline.py validate     # Валидация
python scripts/pipeline/run_pipeline.py nav-stats    # Статистика навигации
python scripts/pipeline/run_pipeline.py nav-upgrade  # Обновление nav (en/ → ru/)

# Перевод
python scripts/translate_docs_groq.py                # Полный перевод
python scripts/translate_missing.py                  # Только отсутствующие
python scripts/translate_titles_only.py              # Только заголовки

# Утилиты
python scripts/detect_changes.py --source-dir docs/en --target-dir docs/ru --report /tmp/changes.json
python scripts/place_translation.py --file docs/ru/<path>
python scripts/cleanup_docs.py
python scripts/fix_docs_links.py
python scripts/validate_translations.py
python scripts/sanitize_secrets.py
```

---

## Важные нюансы

1. **Источник**: СТРОГО `docs.dynatrace.com/managed` (НЕ SaaS-документация, если не просят явно)
2. **Git**: репо большое (1 600+ файлов, ~70 MB docs/) — операции могут таймаутить в песочнице, пуш делать локально из PowerShell
3. **Git config**: в песочнице может быть повреждён (line 14) — не влияет на production
4. **AI-виджет**: Gemini API key в `docs/assets/ai-config.json` — намеренно публичный (GitHub Pages fallback)
5. **Навигация**: вся nav в mkdocs.yml указывает на `ru/` и `managed/` (0 ссылок на `en/`)
6. **Разделение Managed/SaaS**: `docs/en/` и `docs/ru/` — ТОЛЬКО SaaS; `docs/managed/` и `docs/managed-ru/` — ТОЛЬКО Managed. Никаких подпапок `managed/` внутри `en/` или `ru/`
7. **Skill**: `.skills/dynatrace-translate/SKILL.md` содержит путь от старой сессии — при использовании в Cowork нужно подставлять актуальный путь
8. **Валидация при деплое**: test_docs.py + check_coverage.py (порог 80%) — блокирует деплой при проблемах
9. **Secret sanitization**: `sanitize_secrets.py` маскирует токены перед коммитом (Slack webhooks, dt0c01, dt0s02, Google/Groq API keys)
10. **Терминология**: 100+ терминов с word-boundary matching, placeholder protection при переводе
11. **Кэш**: `scripts/.change_tracking/hash_registry.json` — отслеживание изменений между запусками
