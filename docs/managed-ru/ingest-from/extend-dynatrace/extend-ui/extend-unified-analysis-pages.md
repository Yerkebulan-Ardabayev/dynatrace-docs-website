---
title: Расширение встроенных страниц унифицированного анализа
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/extend-ui/extend-unified-analysis-pages
scraped: 2026-05-12T11:37:59.140301
---

# Расширение встроенных страниц унифицированного анализа

# Расширение встроенных страниц унифицированного анализа

* 4-min read
* Updated on Mar 16, 2023

Расширения Dynatrace позволяют добавлять пользовательские карточки на встроенные страницы унифицированного анализа (unified analysis pages).

## Инъекция карточек (card injections)

Карточки можно добавлять на следующие типы страниц:
* Страница деталей сущности (details screen) через секцию `detailsInjections`.
* Страница списка сущностей (list screen) через секцию `listInjections`.

## Пример конфигурации extension.yaml

```yaml
detailsInjections:
  - type: CHART_GROUP
    key: my_custom_charts
    entitySelectorTemplate: type(SERVICE),entityId(ATTR.dt.entity.service)
    width: 2
    conditions:
      - entityAttribute: SERVICE_TYPE
        operator: EQUALS
        value: WEB_REQUEST_SERVICE

listInjections:
  - type: METRIC_TABLE
    key: my_metric_table
    entitySelectorTemplate: type(SERVICE)
```

## Параметры карточки

| Параметр | Описание |
| --- | --- |
| `type` | Тип карточки (CHART_GROUP, METRIC_TABLE, и др.) |
| `key` | Уникальный идентификатор карточки |
| `entitySelectorTemplate` | Шаблон выбора сущностей |
| `width` | Ширина карточки (1 или 2) |
| `conditions` | Условия отображения карточки |

## Связанные темы

* [Страницы унифицированного анализа](/managed/ingest-from/extend-dynatrace/extend-ui/unified-analysis "Обзор страниц унифицированного анализа.")
* [Расширения](/managed/ingest-from/extensions "Узнайте, как создавать расширения Dynatrace.")