---
title: Приём данных StatsD с помощью OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/statsd
---

# Приём данных StatsD с помощью OTel Collector

# Приём данных StatsD с помощью OTel Collector

* Практическое руководство
* Чтение за 2 мин
* Опубликовано 09 июля 2024

Следующий пример конфигурации показывает, как настроить экземпляр Collector для приёма данных из существующей настройки StatsD и импорта их в виде запроса OTLP в Dynatrace.

## Предварительные требования

* Приложение, генерирующее [сообщения StatsD﻿](https://github.com/statsd/statsd/blob/master/docs/metric_types.md)
* Один из следующих дистрибутивов Collector с [приёмником StatsD﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/statsdreceiver), [процессором transform﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/transformprocessor) и [процессором filter﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/filterprocessor):

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + OpenTelemetry [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* [URL конечной точки Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте о конечных точках OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace."), в которую нужно экспортировать данные
* [Токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate)

О том, как настроить Collector с приведённой ниже конфигурацией, см. [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.") и [Настройка Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector.").

## Демонстрационная конфигурация

```
receivers:



statsd:



endpoint: 0.0.0.0:8125



timer_histogram_mapping:



- statsd_type: "histogram"



observer_type: "histogram"



histogram:



# max size for the auto-scaling exponential histogram OTLP metric



# see below for details



max_size: 100



- statsd_type: "timing"



observer_type: "histogram"



histogram:



max_size: 100



- statsd_type: "distribution"



observer_type: "histogram"



histogram:



max_size: 100



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



metrics:



receivers: [statsd]



exporters: [otlp_http]
```

Проверка конфигурации

[Проверьте настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

В нашей конфигурации настроены следующие компоненты.

### Приёмники (Receivers)

В разделе `receivers` указан приёмник `statsd` как активный компонент-приёмник для нашего экземпляра Collector. Приёмник настроен на прослушивание всех сетевых интерфейсов на порту `8125`, который обычно используется для StatsD.

Приёмник настроен на агрегирование сообщений histogram, timer и distribution в экспоненциальные гистограммы, которые затем обрабатываются для приёма в Dynatrace. Приёмник использует автомасштабируемые экспоненциальные гистограммы, и мы выбрали максимальный размер `100`. Это значит, что гистограмма начнёт с очень детализированных границ бакетов и автоматически изменит масштаб, если получит точки данных, которые привели бы к появлению более `100` бакетов.

Полный список параметров конфигурации и поддерживаемых типов метрик StatsD см. в [документации приёмника StatsD﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/receiver/statsdreceiver/README.md).

### Экспортёры (Exporters)

В разделе `exporters` указан стандартный [экспортёр `otlp_http`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter), настроенный с URL API Dynatrace и необходимым токеном аутентификации.

Для этого задаются следующие две переменные окружения, на которые есть ссылки в значениях конфигурации для `endpoint` и `headers`.

* `DT_ENDPOINT` содержит [базовый URL конечной точки API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте о конечных точках OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Конвейер сервиса (Service pipeline)

В разделе `service` собираются объекты приёмника, процессоров и экспортёра в конвейер метрик, который принимает данные StatsD и передаёт их в Dynatrace.

## Ограничения

Метрики принимаются с использованием протокола OpenTelemetry (OTLP) через [OTLP API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api "Узнайте о конечных точках OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.") и подчиняются ограничениям и лимитам API.
Дополнительную информацию см. в:

* [Ограничения метрик OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")
* [Сопоставление метрик Dynatrace](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")

## Похожие темы

* [Сбор метрик Prometheus с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus "Настройте OpenTelemetry Collector для сбора данных с конечных точек Prometheus и приёма данных в Dynatrace.")