---
title: Протокол приёма метрик
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol
scraped: 2026-05-12T11:37:59.140301
---

# Протокол приёма метрик

# Протокол приёма метрик

* 6-min read
* Updated on Mar 16, 2023

Протокол приёма метрик Dynatrace использует текстовый формат для передачи метрик через OneAgent Metric API или инструмент `dynatrace_ingest`.

## Общий синтаксис

```
metric.key[,dimension1=value1[,dimension2=value2]] payload [timestamp]
```

## Правила для ключей метрик

* Ключ метрики начинается с буквы или цифры.
* Допустимые символы: буквы, цифры, точка (`.`), дефис (`-`), нижнее подчёркивание (`_`).
* Максимальная длина: 250 символов.

## Формат измерений

```
metric.key,dim1=val1,dim2=val2 gauge,42
```

Ключи и значения измерений чувствительны к регистру.

## Зарезервированные измерения Dynatrace

Зарезервированные измерения `dt.entity.<entity_type>` связывают метрику с топологической сущностью:

```
custom.metric,dt.entity.host=HOST-1234567890ABCDEF gauge,42
```

## Форматы payload

### gauge

```
metric.key gauge,42
metric.key gauge,min=0,max=100,sum=420,count=10
```

### count (delta)

```
metric.key count,delta=5
```

## Метки времени (timestamp)

Метка времени указывается в миллисекундах Unix epoch:

```
metric.key gauge,42 1609459200000
```

Если метка времени не указана, используется текущее время.

## Метаданные через протокол приёма

```
#metric.key gauge description="My metric" unit="Count"
metric.key gauge,42
```

## Примеры

### С измерениями

```
custom.requests,host=webserver01,env=prod gauge,1250
```

### GAUGE с агрегацией

```
custom.response.time gauge,min=10,max=500,sum=1200,count=5
```

### COUNT

```
custom.errors count,delta=3
```

### Через API-вызов

```bash
curl -X POST "http://localhost:14499/metrics/ingest" \
  -H "Content-Type: text/plain; charset=utf-8" \
  -d "custom.requests,host=webserver01 gauge,1250"
```

## Связанные темы

* [OneAgent Metric API](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Используйте Dynatrace API для получения метрик мониторируемых сущностей.")
* [Метаданные пользовательских метрик](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/custom-metric-metadata "Узнайте о параметрах метаданных метрик.")