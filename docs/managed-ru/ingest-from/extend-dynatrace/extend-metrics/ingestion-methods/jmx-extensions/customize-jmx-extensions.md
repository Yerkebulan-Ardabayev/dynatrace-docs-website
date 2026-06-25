---
title: Настройка JMX-расширений
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/jmx-extensions/customize-jmx-extensions
scraped: 2026-05-12T11:37:59.140301
---

# Настройка JMX-расширений

# Настройка JMX-расширений

* 8-min read
* Updated on Mar 16, 2023

JMX-расширения описываются в формате JSON. Эта страница содержит справочник по всем полям конфигурации.

## Формат JSON расширения

```json
{
  "name": "custom.jmx.myextension",
  "version": "1.0",
  "metricGroup": "jmx.my_app",
  "technologies": ["JAVA"],
  "source": {
    "domain": "com.example",
    "keyProperties": {
      "type": "MyBean"
    }
  },
  "metrics": [
    {
      "timeseries": {
        "key": "jmx.my_app.requests",
        "displayname": "Requests count",
        "dimensions": ["type"],
        "unit": "Count"
      },
      "source": {
        "attribute": "RequestCount"
      }
    }
  ]
}
```

## Поля метаданных

| Поле | Описание |
| --- | --- |
| `name` | Уникальный идентификатор расширения |
| `version` | Версия расширения |
| `metricGroup` | Группа метрик для организации в интерфейсе |
| `technologies` | Список применимых технологий |

## Определение метрик (timeseries)

Каждая метрика описывается через объект `timeseries`:

| Поле | Описание |
| --- | --- |
| `key` | Уникальный ключ метрики |
| `displayname` | Отображаемое имя |
| `dimensions` | Список измерений |
| `unit` | Единица измерения |

## alert_settings

Поле `alert_settings` позволяет настроить алерты для метрики:

```json
"alert_settings": [
  {
    "alert_condition": "ABOVE",
    "threshold": 100,
    "severity": "PERFORMANCE",
    "samples": 5,
    "violating_samples": 3,
    "dealerting_samples": 5
  }
]
```

## Разделения (splitting)

Разделения позволяют получать метрики в разрезе отдельных значений:

```json
"splitting": {
  "name": "type",
  "type": "keyProperty",
  "keyProperty": "type"
}
```

## CompositeData и attributePath

Для доступа к вложенным атрибутам CompositeData используйте нотацию `attributePath`:

```json
"source": {
  "attribute": "HeapMemoryUsage",
  "path": "used"
}
```

## Настройка интерфейса (keymetrics, keycharts, charts)

Поля конфигурации UI позволяют настроить отображение метрик:

```json
"ui": {
  "keymetrics": [
    {
      "key": "jmx.my_app.requests",
      "aggregation": "avg",
      "displayname": "Avg Requests"
    }
  ],
  "charts": [
    {
      "group": "Requests",
      "title": "Request Metrics",
      "series": [
        {
          "key": "jmx.my_app.requests",
          "displayname": "Requests",
          "seriestype": "line"
        }
      ]
    }
  ]
}
```

## Связанные темы

* [JMX-расширения](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/jmx-extensions "Узнайте, как расширить мониторинг Dynatrace с помощью JMX.")