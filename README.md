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
- Кураторский навигатор: `docs/ru` (структура меню сайта).
- В сборку сайта идут только RU-деревья (`docs/ru`, `docs/managed-ru`, `docs/common`);
  EN-сырьё (`docs/en`, `docs/managed`) исключено из сборки (`exclude_docs` в `mkdocs.yml`),
  а `search_index.json` пере-кодируется в UTF-8 хуком `hooks/utf8_search_index.py`.

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
