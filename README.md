# Dynatrace Docs RU

Документация Dynatrace на русском. Автоперевод + ежедневная синхронизация.

[![Deploy](https://github.com/Yerkebulan-Ardabayev/dynatrace-docs-website/actions/workflows/deploy.yml/badge.svg)](https://github.com/Yerkebulan-Ardabayev/dynatrace-docs-website/actions/workflows/deploy.yml)
[![Update](https://github.com/Yerkebulan-Ardabayev/dynatrace-docs-website/actions/workflows/update-docs.yml/badge.svg)](https://github.com/Yerkebulan-Ardabayev/dynatrace-docs-website/actions/workflows/update-docs.yml)

https://yerkebulan-ardabayev.github.io/dynatrace-docs-website/

## Как работает

Scrape docs.dynatrace.com -> AI-перевод -> GitHub Pages. Обновляется каждый день в 02:00 (Алматы).

## Локальный запуск

```bash
git clone https://github.com/Yerkebulan-Ardabayev/dynatrace-docs-website.git
cd dynatrace-docs-website
pip install -r requirements.txt
mkdocs serve
```

## Пайплайн

```bash
python scripts/sync_and_deploy.py           # полный цикл
python scripts/sync_and_deploy.py --dry-run  # без пуша
```

## Автор

**Yerkebulan Ardabayev** — [@Yerkebulan-Ardabayev](https://github.com/Yerkebulan-Ardabayev)
