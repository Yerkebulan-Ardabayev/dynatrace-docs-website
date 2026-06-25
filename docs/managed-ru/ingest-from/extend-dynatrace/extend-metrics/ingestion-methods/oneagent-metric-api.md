---
title: OneAgent Metric API
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api
scraped: 2026-05-12T11:37:59.140301
---

# OneAgent Metric API

# OneAgent Metric API

* 3-min read
* Updated on Mar 16, 2023

OneAgent предоставляет локальный HTTP-эндпоинт для приёма метрик по адресу `http://localhost:<port>/metrics/ingest`.

## Включение EEC

Для использования OneAgent Metric API необходимо включить Extension Execution Controller (EEC) в настройках окружения.

## Топологическая осведомлённость

Метрики, отправленные через OneAgent Metric API, автоматически связываются с топологическими сущностями, такими как хосты, процессы и сервисы.

## Формат метрик

Используется текстовый формат `text/plain`:

```
metric.key,dimension1=value1,dimension2=value2 gauge,42 1609459200000
```

## Пример запроса

```bash
curl -X POST "http://localhost:14499/metrics/ingest" \
  -H "Content-Type: text/plain; charset=utf-8" \
  -d "custom.metric,host=myhost gauge,42"
```

## Порт связи

По умолчанию используется порт `14499`. Порт настраивается через конфигурацию OneAgent.

## Альтернатива: Metrics API v2

В качестве альтернативы можно использовать [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Узнайте об API метрик v2.") для отправки метрик напрямую в Dynatrace.

## Связанные темы

* [Протокол приёма метрик](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Узнайте о протоколе приёма метрик.")
* [Расширение наблюдаемости метрик](/managed/ingest-from/extend-dynatrace/extend-metrics "Расширьте наблюдаемость метрик с помощью Dynatrace.")