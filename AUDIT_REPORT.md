# Комплексный аудит: Dynatrace Documentation Website + LLM Integration

**Дата аудита:** 2026-02-13
**Аудитор:** Claude Opus 4.6 (автоматизированный Code Review + Logic Review)
**Репозиторий:** https://github.com/Yerkebulan-Ardabayev/dynatrace-docs-website
**Целевое RAG-хранилище:** NotebookLM

---

## 1. Технический анализ архитектуры

### 1.1. Общая схема системы

```
┌──────────────────────────────────────────────────────────────────┐
│                     DATA PIPELINE                                │
│                                                                  │
│  docs.dynatrace.com ──► scrape_docs.py ──► organize_docs.py     │
│         (HTML)           (BFS Crawler)     (Managed/General)     │
│                              │                    │              │
│                              ▼                    ▼              │
│                    scripts/dynatrace-docs/    docs/en/           │
│                         (cache)              docs/en/managed/    │
│                                                   │              │
│                                                   ▼              │
│                              translate_docs_groq.py (PRIMARY)    │
│                              translate_docs_gemini.py (ALT)      │
│                              translate_docs_quality.py (ALT)     │
│                                                   │              │
│                                                   ▼              │
│                                              docs/ru/            │
│                                                   │              │
│                                                   ▼              │
│                                            mkdocs build          │
│                                                   │              │
│                                                   ▼              │
│                                              site/ (static)      │
│                                                   │              │
│                                    ┌──────────────┼──────────┐   │
│                                    ▼              ▼          ▼   │
│                             Flask Server   GitHub Pages  [MISSING]│
│                            (local_server)  (deploy.yml) NotebookLM│
└──────────────────────────────────────────────────────────────────┘
```

### 1.2. Как работает парсинг (Think step-by-step)

**Мой анализ логики `scrape_docs.py`:**

1. **Инициализация:** Создается BFS-краулер с начальным URL `https://www.dynatrace.com/support/help/`. Используется `requests.Session` с фейковым User-Agent.
2. **Обход:** BFS (Breadth-First Search) по очереди `to_visit`. Для каждого URL — загрузка HTML, извлечение ссылок через `extract_links()`, конвертация в Markdown.
3. **Фильтрация URL:** Проверка домена (`dynatrace.com`), пути (`/docs/` или `/support/help/`), исключение блогов, community, downloads.
4. **Конвертация:** HTML → Markdown через `markdownify`. Поиск `<main>`, `<article>`, `<div.content>` — с fallback на `<body>`.
5. **Кеширование:** Хеш URL → JSON-файл в `.cache/pages_cache.json`. Но кеш не используется для проверки актуальности — только для хранения метаданных.
6. **Rate limiting:** `time.sleep(1)` между запросами.

**Критические наблюдения:**

- **Динамический контент НЕ обрабатывается.** Сайт docs.dynatrace.com использует React/SPA с client-side rendering. `requests.get()` получает только серверный HTML, а динамически загружаемый контент (табы, expandable sections, interactive examples) будет утерян.
- **Авторизация отсутствует.** Для Dynatrace Managed-документации часть страниц может требовать авторизации (например, release notes для конкретных версий). Скрипт не поддерживает cookie-based или token-based auth.
- **Кеш не валидирует ETag/Last-Modified** — при повторном запуске всегда перекачивает все страницы заново (кеш записывается, но не читается для skip-логики в `scrape_page()`).

### 1.3. Как работает перевод (Think step-by-step)

**Мой анализ логики `translate_docs_groq.py` (PRIMARY):**

1. **Итерация:** Находит все `docs/en/**/*.md` файлы.
2. **Skip-логика:** Если `docs/ru/<path>` существует И его mtime > mtime английского файла — пропускает.
3. **Кеш:** `cache_key = f"{source_file}:{hash(text)}"` — использует Python `hash()` (нестабилен между сессиями!).
4. **API вызов:** POST к `https://api.groq.com/openai/v1/chat/completions` с моделью `llama-3.1-70b-versatile`, temperature=0.3, max_tokens=8000.
5. **Промпт:** Инструкция сохранять Markdown, технические термины (OneAgent, Smartscape, Davis AI, Grail, DQL, Kubernetes), профессиональный перевод.
6. **Fallback:** При ошибке API возвращается оригинальный английский текст (записывается в `docs/ru/` как есть).
7. **Rate limit:** `time.sleep(0.5)` → ~120 req/min при лимите Groq 30 req/min для free tier.

**Критические наблюдения:**

- **`hash()` в Python не детерминирован между процессами** (с Python 3.3+ используется рандомизация хешей). Кеш `cache_key = f"{source_file}:{hash(text)}"` будет генерировать разные ключи при каждом запуске → кеш фактически бесполезен.
- **max_tokens=8000 при модели llama-3.1-70b-versatile** — документация Groq указывает, что контекстное окно модели 128K, но output limit может быть меньше. Длинные документы будут обрезаны без уведомления.
- **Fallback записывает английский текст в `docs/ru/`** — пользователь видит "переведенный" файл, который на самом деле на английском. Нет маркировки таких файлов.
- **Несогласованность rate limiting:** 0.5s delay = ~120 req/min, но Groq free tier = 30 req/min. Приведет к 429 ошибкам.

---

## 2. Таблица выявленных рисков

| # | Компонент | Проблема | Критичность | Рекомендация |
|---|-----------|----------|-------------|--------------|
| 1 | **groq-chat.js** | API-ключ Groq (`gsk_jx32...`) захардкожен в публичном JS-файле в GitHub-репозитории. Любой может его использовать или заблокировать. | **Critical** | Перенести ключ на backend (proxy через Flask `/api/chat`). На клиенте не должно быть API-ключей. |
| 2 | **translate_docs_gemini.py** | API-ключ Google Gemini (`AIzaSyDvAv31Q97V...`) захардкожен в исходном коде (строка 16). | **Critical** | Использовать `os.environ.get('GEMINI_API_KEY')` как в translate_docs_groq.py. |
| 3 | **scrape_docs.py** | Не обрабатывает динамический контент (React SPA). `requests.get()` получает только SSR-HTML. Табы, expandable sections, API examples теряются. | **High** | Использовать Playwright/Selenium для headless browser rendering. Или использовать API docs.dynatrace.com (если доступен). |
| 4 | **translate_docs_groq.py** | `hash()` в Python 3.3+ нестабилен между процессами (PYTHONHASHSEED). Кеш переводов фактически не работает при перезапуске. | **High** | Заменить `hash(text)` на `hashlib.md5(text.encode()).hexdigest()` для стабильного кеширования. |
| 5 | **translate_docs_groq.py** | Rate limit: `time.sleep(0.5)` = ~120 req/min при лимите Groq free tier 30 req/min. Массовые 429 ошибки. | **High** | Установить `time.sleep(2.0)` для соответствия 30 req/min. Добавить exponential backoff при 429. |
| 6 | **translate_docs_groq.py** | При ошибке API — записывает английский текст в `docs/ru/` без маркировки. Пользователь не знает, что "перевод" — это оригинал. | **High** | Добавить маркер `<!-- TRANSLATION_FAILED -->` в файл, либо не записывать файл при ошибке. Вести лог неудачных переводов. |
| 7 | **translate_docs_groq.py** | max_tokens=8000 — длинные документы обрезаются без предупреждения. Markdown может быть повреждён (незакрытые блоки кода, таблицы). | **High** | Реализовать chunking: разбивать длинные документы на секции по заголовкам, переводить по частям, объединять. |
| 8 | **Терминология** | "Grail" переводится как "Грааль" в некоторых файлах. Несогласованность: иногда "Grail", иногда "Грааль" в одном документе. | **High** | Расширить whitelist в промпте: добавить PurePath, ActiveGate, Management Zone, Host Group, Process Group, Grail, Environment, Tenant. Добавить post-processing валидацию. |
| 9 | **Кодировка** | В переведённых файлах обнаружены артефакты кодировки: `â¦`, `ï»¿`, `â` — вместо спецсимволов. | **High** | Добавить UTF-8 BOM stripping (`text.lstrip('\ufeff')`) и post-processing для замены mojibake-артефактов. |
| 10 | **scrape_docs.py** | BFS использует `list.pop(0)` — O(n) операция. При 1000+ URL в очереди деградирует производительность. | **Medium** | Заменить `list` на `collections.deque` и `popleft()` — O(1). |
| 11 | **local_server.py** | `/api/update` выполняет `subprocess.run()` синхронно с timeout=7200 (2 часа). Flask thread блокируется. Нет аутентификации. | **High** | Добавить аутентификацию на `/api/update`. Вынести в background task (Celery/threading). Добавить rate limiting. |
| 12 | **local_server.py** | Несоответствие: сервер вызывает `translate_docs_gemini.py` (строка 109), но README и auto_update.py используют `translate_docs_groq.py`. | **Medium** | Унифицировать: использовать один скрипт перевода или добавить конфигурационный параметр. |
| 13 | **update-docs.yml** | GitHub Action вызывает `translate_docs.py` (legacy googletrans), а не `translate_docs_groq.py` (primary). | **High** | Обновить workflow: заменить `translate_docs.py` на `translate_docs_groq.py` и добавить `GROQ_API_KEY` в GitHub Secrets. |
| 14 | **organize_docs.py** | Дефолтный source path: `../dynatrace-link-finder/dynatrace-docs` не совпадает с output path скрапера (`dynatrace-docs` или `temp_docs`). Pipeline разорван. | **High** | Синхронизировать пути между скриптами. Использовать единый конфиг (config.yaml или env vars). |
| 15 | **test_website.py** | Тесты ищут `gemini-chat.js`, но в проекте используется `groq-chat.js`. Тесты не пройдут. Hardcoded API key check. | **Medium** | Обновить тесты под текущую архитектуру (Groq вместо Gemini). Удалить проверку hardcoded API keys. |
| 16 | **NotebookLM** | Полностью отсутствует интеграция с NotebookLM. Нет скриптов экспорта/синхронизации. | **Critical** | Реализовать модуль `sync_notebooklm.py` с batch-загрузкой документов. NotebookLM API пока не публичный — рассмотреть альтернативы (Google Drive sync, manual upload pipeline). |
| 17 | **scrape_docs.py** | URL `https://www.dynatrace.com/support/help/` — это legacy URL. Актуальная документация на `https://docs.dynatrace.com/docs/`. | **High** | Обновить BASE_URL на `https://docs.dynatrace.com/docs/` (scrape_managed.py уже использует правильный URL). |
| 18 | **Все translation скрипты** | Весь файл отправляется одним запросом, включая frontmatter YAML. LLM может повредить frontmatter (перевести title, изменить source URL). | **Medium** | Отделять frontmatter от тела документа перед переводом. Переводить только body. Собирать обратно после перевода. |
| 19 | **scrape_managed.py** | URL `https://docs.dynatrace.com/managed` и подразделы — не факт что существуют. Dynatrace Managed docs были на `/docs/managed/` или другом пути. | **Medium** | Верифицировать актуальные URL через ручную проверку. Dynatrace Managed документация может быть на `https://docs.dynatrace.com/docs/manage/` или в отдельном разделе. |
| 20 | **auto_update.py** | Использует `schedule` (in-process cron). При краше процесса — автообновление останавливается без уведомления. Нет мониторинга. | **Medium** | Использовать системный cron/systemd timer или GitHub Actions scheduled workflow. Добавить healthcheck endpoint. |

---

## 3. Анализ лимитов: стратегия для NotebookLM (300 источников)

### 3.1. Текущее состояние

- **Английских файлов:** ~500
- **Русских файлов:** ~49
- **Managed-specific:** ~200
- **Common:** ~100
- **Лимит NotebookLM:** 300 источников

### 3.2. Проблема

500+ файлов документации не помещаются в лимит 300 источников NotebookLM. При полной синхронизации придётся выбирать, какие документы загружать.

### 3.3. Рекомендованная стратегия

**Вариант A: Приоритизация и мёрж (рекомендуется)**

```
Приоритет 1 (обязательно):
  - Managed: installation, configuration, operations, security, backup, cluster
  - ~50 файлов → 50 источников

Приоритет 2 (важно):
  - Common: OneAgent, Davis AI, Grail, DQL, ActiveGate
  - ~80 файлов → объединить по разделам → ~20 источников

Приоритет 3 (справочно):
  - SaaS reference, API documentation
  - ~200 файлов → объединить по категориям → ~30 источников

ИТОГО: ~100 источников (запас 200)
```

**Реализация: скрипт `merge_for_notebooklm.py`:**
1. Группировать файлы по разделам (directory-based)
2. Объединять мелкие файлы одного раздела в один документ (конкатенация с разделителями)
3. Добавлять metadata-заголовки для навигации внутри объединённого документа
4. Контролировать размер каждого источника (NotebookLM: ~500K символов на источник)
5. Генерировать manifest.json с маппингом "файл → источник NotebookLM"

**Вариант B: Динамическая ротация**

Менее предпочтителен. Предполагает замену "устаревших" документов на "актуальные" при обновлении. Сложнее в реализации, теряется полнота.

**Вариант C: Ожидание NotebookLM API**

NotebookLM пока не имеет публичного API для автоматической загрузки. Текущий вариант — ручная загрузка через Google Drive интеграцию или UI. Отслеживать появление API.

### 3.4. Критическое замечание

**В репозитории полностью отсутствует какая-либо интеграция с NotebookLM.** Нет:
- Скрипта экспорта документов в формат, совместимый с NotebookLM
- Скрипта загрузки в Google Drive (как прокси для NotebookLM)
- Мониторинга количества загруженных источников
- Стратегии приоритизации документов

Это один из главных пробелов проекта.

---

## 4. Оценка UX и качества перевода

### 4.1. Качество перевода (на основе анализа ~5 файлов в `docs/ru/`)

| Критерий | Оценка | Комментарий |
|----------|--------|-------------|
| Общая читабельность | 6/10 | Профессиональный стиль, но есть артефакты кодировки |
| Сохранение Markdown | 7/10 | Структура сохраняется, но frontmatter иногда повреждается |
| Терминология | 5/10 | "Grail" → "Грааль" — критическая ошибка. Несогласованность в рамках одного документа |
| Полнота перевода | 4/10 | Некоторые файлы обрезаны (max_tokens). Release notes truncated до 14 строк |
| Кодировка | 3/10 | Массовые mojibake-артефакты: `â¦`, `ï»¿`, `â`, `»` |

### 4.2. Проблемы терминологии

**Термины, которые ДОЛЖНЫ оставаться на английском (но иногда переводятся):**

| Термин | Найденный перевод | Статус |
|--------|------------------|--------|
| Grail | "Грааль" | **ОШИБКА** — должно быть "Grail" |
| OneAgent | OneAgent | OK |
| Davis AI | Davis AI | OK |
| DQL | DQL | OK |
| ActiveGate | ActiveGate | OK |
| Smartscape | "Смартскейп" (в alt-text) | **Частичная ошибка** |
| PurePath | Не найден в выборке | Требует проверки |
| Management Zone | Не найден в выборке | Требует проверки |
| Host Group | Не найден в выборке | Требует проверки |
| Process Group | Не найден в выборке | Требует проверки |
| Environment | Не найден в выборке | Требует проверки |
| Tenant | Не найден в выборке | Требует проверки |

### 4.3. Рекомендации по улучшению UX

1. **Post-processing pipeline:** После перевода — запускать скрипт валидации:
   - Проверка, что термины из whitelist не переведены
   - Проверка целостности Markdown (парные ```, незакрытые таблицы)
   - Проверка encoding (отсутствие mojibake)
   - Проверка минимальной длины файла (защита от truncation)

2. **Glossary injection в промпт:**
   ```
   НЕ ПЕРЕВОДИТЬ СЛЕДУЮЩИЕ ТЕРМИНЫ:
   OneAgent, ActiveGate, Smartscape, PurePath, Davis AI, Grail, DQL,
   Management Zone, Host Group, Process Group, Environment, Tenant,
   Dynatrace Cluster, Cluster Management Console (CMC),
   AppMon, Synthetic, RUM, Session Replay, USQL
   ```

3. **A/B тестирование моделей:** Groq Llama 3.1 70B vs Claude Sonnet vs Gemini 1.5 Pro — на одинаковом наборе из 20 файлов. Метрики: BLEU score, терминологическая корректность, процент mojibake.

---

## 5. Дополнительные архитектурные замечания

### 5.1. Безопасность (Security Review)

| Проблема | Файл | Строка | Критичность |
|----------|------|--------|-------------|
| Hardcoded Groq API key (публичный) | `groq-chat.js` | 8 | **Critical** |
| Hardcoded Gemini API key | `translate_docs_gemini.py` | 16 | **Critical** |
| Unauthenticated `/api/update` endpoint | `local_server.py` | 59 | **High** |
| Command injection risk via subprocess | `local_server.py` | 70-128 | **Medium** (args hardcoded, but pattern risky) |
| Flask debug=False (correct) | `local_server.py` | 222 | OK |
| No CORS configuration | `local_server.py` | - | **Medium** |

### 5.2. Рассогласование компонентов

Система имеет 4 скрипта перевода, но разные точки входа используют разные:

| Точка входа | Скрипт перевода | Модель |
|-------------|----------------|--------|
| `run_complete.py` | `translate_docs_groq.py` | Llama 3.1 70B |
| `local_server.py` | `translate_docs_gemini.py` | Gemini 1.5 Pro |
| `auto_update.py` | `translate_docs_groq.py` | Llama 3.1 70B |
| `update-docs.yml` (GH Actions) | `translate_docs.py` | googletrans (legacy) |
| Chat widget | `groq-chat.js` | Llama 3.3 70B |

Это создаёт риск получения различного качества перевода в зависимости от того, как был запущен пайплайн.

### 5.3. Отсутствующие компоненты

1. **NotebookLM sync** — полностью отсутствует
2. **Мониторинг и alerting** — нет healthcheck, нет уведомлений при отказе
3. **Validation pipeline** — нет проверки качества перевода после генерации
4. **Versioning** — нет версионирования документации (какой версии Dynatrace соответствует)
5. **Diff-based обновление** — при изменении одного абзаца переводится весь файл заново
6. **Retry logic** — при 429/5xx от API нет retry с backoff (кроме простого fallback на оригинал)

---

## 6. Итоговый Score

| Критерий | Score (0-10) | Комментарий |
|----------|-------------|-------------|
| **Функциональность** | **5/10** | Базовый pipeline работает (scrape → translate → serve). Но: кеш сломан, URL устарел, пайплайн рассогласован, NotebookLM отсутствует. |
| **Масштабируемость** | **3/10** | Лимит 300 источников NotebookLM не адресован. Нет chunking для длинных документов. BFS с list.pop(0). Синхронный subprocess в Flask. |
| **Стабильность** | **3/10** | API ключи захардкожены (один уже в публичном доступе). Кеш не работает между запусками. Rate limiting недостаточен. Fallback пишет EN в RU без маркировки. Нет retry. Нет мониторинга. |
| **Безопасность** | **2/10** | Публичные API-ключи в исходном коде. Неаутентифицированный endpoint обновления. Нет CORS. |
| **Качество перевода** | **5/10** | Базово — читабельно. Но: mojibake, truncation, inconsistent terminology (Grail→Грааль). |
| **Тестирование** | **2/10** | Единственный тест (test_website.py) устарел (ищет Gemini вместо Groq). Нет unit-тестов. Нет integration-тестов. |
| **Общий Score** | **3.3/10** | Проект находится на стадии PoC/MVP. Основная функциональность реализована, но не production-ready. Необходимы: секьюрити-фикс (API keys), стабилизация pipeline, интеграция NotebookLM, quality gates. |

---

## 7. Приоритизированный план действий

### Немедленно (P0 — Critical):
1. **Убрать API-ключи из исходного кода** (groq-chat.js:8, translate_docs_gemini.py:16). Ротировать скомпрометированные ключи.
2. **Добавить аутентификацию** на `/api/update` endpoint.

### В ближайшее время (P1 — High):
3. Исправить `hash()` → `hashlib.md5()` в кеше переводов.
4. Исправить rate limiting (0.5s → 2.0s) в translate_docs_groq.py.
5. Обновить BASE_URL в scrape_docs.py на `https://docs.dynatrace.com/docs/`.
6. Синхронизировать пути между organize_docs.py и scrape_docs.py.
7. Унифицировать скрипт перевода во всех точках входа.
8. Обновить GitHub Actions workflow на актуальный скрипт перевода.
9. Добавить расширенный whitelist терминов в промпт.

### Среднесрочно (P2 — Medium):
10. Реализовать `merge_for_notebooklm.py` для подготовки документов к загрузке.
11. Добавить post-processing validation pipeline.
12. Реализовать chunking для длинных документов.
13. Заменить `requests` на `Playwright` для обработки SPA-контента.
14. Обновить test_website.py под текущую архитектуру.
15. Добавить diff-based инкрементальный перевод.

---

*Отчёт сгенерирован автоматически в рамках аудита. Все рекомендации привязаны к конкретным файлам и строкам кода.*
