# Dynatrace Docs RU

Документация Dynatrace на русском. Автоперевод + ежедневная синхронизация.

[![Deploy](https://github.com/Yerkebulan-Ardabayev/dynatrace-docs-website/actions/workflows/deploy.yml/badge.svg)](https://github.com/Yerkebulan-Ardabayev/dynatrace-docs-website/actions/workflows/deploy.yml)
[![Update](https://github.com/Yerkebulan-Ardabayev/dynatrace-docs-website/actions/workflows/update-docs.yml/badge.svg)](https://github.com/Yerkebulan-Ardabayev/dynatrace-docs-website/actions/workflows/update-docs.yml)

https://yerkebulan-ardabayev.github.io/dynatrace-docs-website/

## Как работает

Ночью GitHub Actions скрейпит `docs.dynatrace.com/managed/`, детектит изменения
по хэшу содержимого, переводит новое/изменённое через AI и коммитит в `main`; пуш
в `main` собирает MkDocs и публикует на GitHub Pages.

- Канонический корпус: `docs/managed` (EN-исходники) -> `docs/managed-ru` (RU-перевод).
- Сайт Managed-only: в сборку идут `docs/managed-ru` + кастомные страницы
  (`ru/getting-started.md`, `ru/training/`, `ai/groq.md`, `index.md`); остальные деревья
  исключены через `exclude_docs` в `mkdocs.yml` (паттерны ЗАЯКОРЕНЫ ведущим `/`,
  незаякоренный `managed/` молча выкидывал вложенный `managed-ru/whats-new/managed/`).
- Хуки сборки (`mkdocs.yml` -> `hooks/`):
  - `utf8_search_index.py`: `search_index.json` в UTF-8 (иначе кириллица в `\uXXXX`
    раздувает индекс свыше лимита GitHub Pages 100 МБ);
  - `rewrite_managed_links.py`: абсолютные `/managed/...`-ссылки корпуса становятся
    внутренними относительными, а для ещё не переведённых страниц ведут на живой
    upstream (docs.dynatrace.com) вместо 404;
  - `full_nav.py`: боковое меню строится из файловой системы при каждой сборке
    (кураторские топ-разделы заданы в хуке, новые страницы после sync попадают сами).

## Пайплайн (GitHub Actions)

- `.github/workflows/update-docs.yml` (Sync): cron 21:00 UTC (02:00 Алматы) + ручной
  запуск. Стадии: scrape -> verify_corpus (Gate A) -> detect -> translate -> validate
  (Gate B) -> PDF -> commit -> issue -> Telegram -> build+deploy.
- `.github/workflows/deploy.yml` (Deploy): на push в `main` по путям `docs/**`,
  `mkdocs.yml`, `scripts/**`. Стадии: `mkdocs build --strict` (гейт) -> build -> публикация в gh-pages.

Скрипты, которые реально дёргает CI: `scrape_docs.py`, `detect_changes.py`,
`translate_changed.py`, `validate_translations.py`, `verify_corpus.py`, `generate_pdfs.py`.

## Локальный запуск

```bash
git clone https://github.com/Yerkebulan-Ardabayev/dynatrace-docs-website.git
cd dynatrace-docs-website
pip install -r requirements.txt
mkdocs serve            # локальный предпросмотр
mkdocs build --strict   # как в CI-гейте
```

## Автор

**Yerkebulan Ardabayev** — [@Yerkebulan-Ardabayev](https://github.com/Yerkebulan-Ardabayev)
