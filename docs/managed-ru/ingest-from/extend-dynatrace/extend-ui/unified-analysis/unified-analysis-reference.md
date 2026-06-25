---
title: Справочник по унифицированному анализу
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference
scraped: 2026-05-12T11:37:59.140301
---

# Справочник по унифицированному анализу

# Справочник по унифицированному анализу

* 20-min read
* Updated on Mar 16, 2023

Этот справочник содержит полное описание конфигурационных параметров для страниц унифицированного анализа (unified analysis pages).

Страницы унифицированного анализа настраиваются через файл `extension.yaml` расширения Dynatrace.

> _Reference-таблица на английском._

## Структура конфигурации

Конфигурация страниц состоит из следующих основных разделов:

* `detailsSettings` — настройки страницы деталей сущности.
* `listSettings` — настройки страницы списка сущностей.
* `detailsInjections` — инъекции карточек на страницу деталей.
* `listInjections` — инъекции карточек на страницу списка.

## detailsSettings

Раздел `detailsSettings` управляет конфигурацией страницы деталей:

```yaml
detailsSettings:
  staticContent:
    showGlobalFilter: false
    breadcrumb:
      - entityType: SERVICE
  layout:
    autoGenerate: false
    cards:
      - key: overview_chart
        type: CHART_GROUP
```

## listSettings

Раздел `listSettings` управляет конфигурацией страницы списка:

```yaml
listSettings:
  staticContent:
    showGlobalFilter: true
  layout:
    autoGenerate: false
    cards:
      - key: entity_list
        type: ENTITIES_LIST
```

## Карточки типа CHART_GROUP

Карточки графиков отображают метрики в виде временных рядов.

### Поддерживаемые типы графиков

| Тип | Описание |
| --- | --- |
| GRAPH_CHART | Линейный или столбчатый график |
| PIE_CHART | Круговая диаграмма |
| SINGLE_VALUE | Отображение одного значения |

### Конфигурация series

```yaml
series:
  - key: my_metric
    displayName: "My Metric"
    aggregation: AVG
    type: AUTO
    seriesType: LINE
```

## Карточки типа ENTITIES_LIST

Карточки списка сущностей отображают связанные сущности.

```yaml
- key: related_services
  type: ENTITIES_LIST
  displayName: Related Services
  entitySelectorTemplate: "type(SERVICE),fromRelationships.calls($(entityConditions))"
  columns:
    - columnId: name
      displayName: Name
      attribute: dt.entity.name
      type: ATTRIBUTE
```

## Условия (conditions)

Условия управляют видимостью карточек:

| Оператор | Описание |
| --- | --- |
| EQUALS | Точное совпадение значения |
| NOT_EQUALS | Несовпадение значения |
| CONTAINS | Содержит подстроку |
| EXISTS | Атрибут существует |

## Карточки событий (events)

```yaml
- key: events_card
  type: EVENTS
  displayName: Events
  pageSize: 20
  eventTypes:
    - AVAILABILITY_EVENT
    - PERFORMANCE_EVENT
```

## Карточки логов (logs)

```yaml
- key: logs_card
  type: LOGS
  displayName: Logs
  pageSize: 50
```

## Карточка problems

```yaml
- key: problems_card
  type: PROBLEMS
  displayName: Open Problems
```

## Действия (actions)

### Стандартные действия (core actions)

| Действие | Описание |
| --- | --- |
| BROWSE_EVENTS | Просмотр событий |
| BROWSE_LOGS | Просмотр логов |
| OPEN_WITH_DT | Открыть в Dynatrace |

### Пользовательские действия

```yaml
actions:
  - actionType: OPEN_URL
    displayName: Open Dashboard
    url: "https://example.com/dashboard"
```

## Карточки метрических таблиц (metric table)

```yaml
- key: metric_table
  type: METRIC_TABLE
  displayName: Performance Metrics
  metrics:
    - key: custom.metric.requests
      displayName: Requests
    - key: custom.metric.errors
      displayName: Errors
```

## Карточки работоспособности (health)

```yaml
- key: health_card
  type: HEALTH
  displayName: Health Status
```

## Связанные темы

* [Обучающий пример](/managed/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-tutorial "Пошаговое создание страниц унифицированного анализа.")
* [Расширение встроенных страниц](/managed/ingest-from/extend-dynatrace/extend-ui/extend-unified-analysis-pages "Добавление карточек на встроенные страницы.")