---
title: Метаданные пользовательских метрик
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/extend-metrics/reference/custom-metric-metadata
scraped: 2026-05-12T11:37:59.140301
---

# Метаданные пользовательских метрик

# Метаданные пользовательских метрик

* 4-min read
* Updated on Mar 16, 2023

Метаданные метрик позволяют добавлять описательную информацию к пользовательским метрикам.

## Параметры метаданных

| Параметр | Описание |
| --- | --- |
| `displayName` | Отображаемое имя метрики |
| `description` | Описание метрики |
| `unit` | Единица измерения |
| `sourceEntityType` | Тип сущности-источника |
| `tags` | Теги метрики |
| `metricProperties` | Свойства метрики |
| `dimensions` | Измерения метрики |

## Объект MetricProperties

```json
{
  "impact": "Performance",
  "linearity": "linear",
  "rootCauseRelevant": false,
  "valueRange": {
    "min": 0,
    "max": 100
  }
}
```

## Объект MetricDimensions

```json
{
  "key": "host",
  "name": "Host name",
  "description": "The name of the monitored host"
}
```

## Пример JSON

```json
{
  "displayName": "Custom Request Rate",
  "description": "Number of requests per second",
  "unit": "PerSecond",
  "sourceEntityType": "HOST",
  "dimensions": [
    {
      "key": "host",
      "name": "Host"
    }
  ]
}
```

## Вызов Settings API

Для создания метаданных метрики используйте Settings API (POST):

```bash
curl -X POST "https://<your-environment>/api/v2/settings/objects" \
  -H "Authorization: Api-Token <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "schemaId": "builtin:metric.metadata",
    "value": {
      "displayName": "Custom Metric",
      "unit": "Count"
    }
  }'
```

## Просмотр метаданных

Метаданные метрик можно просмотреть в Data Explorer через Metrics Selector.

## Связанные темы

* [Протокол приёма метрик](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Узнайте о протоколе приёма метрик.")
* [Расширение наблюдаемости метрик](/managed/ingest-from/extend-dynatrace/extend-metrics "Расширьте наблюдаемость метрик с помощью Dynatrace.")