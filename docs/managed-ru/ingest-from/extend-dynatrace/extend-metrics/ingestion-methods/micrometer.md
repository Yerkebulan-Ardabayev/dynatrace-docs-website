---
title: Интеграция с Micrometer
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/micrometer
scraped: 2026-05-12T11:37:59.140301
---

# Интеграция с Micrometer

# Интеграция с Micrometer

* 6-min read
* Updated on Mar 16, 2023

Micrometer — это библиотека метрик для JVM-приложений, широко применяемая в Spring Boot. Dynatrace поддерживает два канала приёма метрик Micrometer.

## Каналы приёма

1. **OneAgent Metric API** — метрики отправляются через локальный эндпоинт OneAgent.
2. **Metrics API v2** — метрики отправляются напрямую через Dynatrace API.

## Dynatrace Registry v2

Для интеграции используйте Dynatrace Registry v2. Добавьте зависимость в `pom.xml`:

```xml
<dependency>
  <groupId>io.micrometer</groupId>
  <artifactId>micrometer-registry-dynatrace</artifactId>
  <version>${micrometer.version}</version>
</dependency>
```

## Настройка через YAML

```yaml
management:
  metrics:
    export:
      dynatrace:
        uri: http://localhost:14499/metrics/ingest
        api-token: ""
        v2:
          metric-key-prefix: "custom.micrometer"
```

## Настройка через application.properties

```properties
management.metrics.export.dynatrace.uri=http://localhost:14499/metrics/ingest
management.metrics.export.dynatrace.api-token=
management.metrics.export.dynatrace.v2.metric-key-prefix=custom.micrometer
```

## Типы метрик

| Тип Micrometer | Тип Dynatrace |
| --- | --- |
| Counter | count,delta |
| Gauge | gauge |
| Timer | gauge,min,max,count,sum |
| DistributionSummary | gauge,min,max,count,sum |

## Метаданные метрик (meter metadata)

Micrometer передаёт метаданные метрик, включая описание и единицы измерения, которые Dynatrace сохраняет как метаданные метрики.

## Особенности Kubernetes

В Kubernetes-окружении убедитесь, что OneAgent доступен на хосте, где запущен под приложения.

## Отключение метрик

Для отключения отдельных метрик используйте:

```yaml
management:
  metrics:
    enable:
      jvm: false
```

## Устранение неполадок через логи

Для диагностики проблем включите отладочный уровень логирования для Micrometer:

```yaml
logging:
  level:
    io.micrometer: DEBUG
```

## Сводные инструменты Dynatrace (Dynatrace summary instruments)

Dynatrace предоставляет специальные инструменты для передачи предварительно агрегированных данных, совместимых с форматом метрик Dynatrace.

## Связанные темы

* [OneAgent Metric API](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Используйте Dynatrace API для получения метрик мониторируемых сущностей.")
* [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Узнайте об API метрик v2.")