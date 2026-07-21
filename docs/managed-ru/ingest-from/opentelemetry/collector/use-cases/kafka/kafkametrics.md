---
title: Мониторинг Kafka с помощью OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/kafka/kafkametrics
---

# Мониторинг Kafka с помощью OTel Collector

# Мониторинг Kafka с помощью OTel Collector

* Практическое руководство
* Чтение 3 мин
* Опубликовано 26 нояб. 2025 г.

Следующий пример конфигурации показывает, как настроить экземпляр OTel Collector для сбора метрик Kafka через компонент-приёмник `kafka_metrics` и приёма их в виде запросов OTLP в Dynatrace.

## Предварительные требования

Для настройки этой конфигурации нужно следующее:

* Один из следующих дистрибутивов Collector с [приёмником kafka\_metrics﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/kafkametricsreceiver) и [процессором cumulativetodelta﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/cumulativetodeltaprocessor)

  + [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [Custom Builder version](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* Сервер Kafka, развёрнутый с доступным `BROKER_ADDRESS`.
  Подробнее см. [руководство по быстрому старту Kafka Apache﻿](https://kafka.apache.org/quickstart).
* [URL конечной точки Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."), в которую нужно экспортировать данные.
* [Токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate).

О том, как настроить Collector с приведённой ниже конфигурацией, см. в разделах [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.") и [Настройка Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector.").

## Демонстрационная конфигурация

```
receivers:



kafka_metrics:



brokers: ["${env:BROKER_ADDRESS}"]



scrapers:



- brokers



- topics



- consumers



processors:



cumulativetodelta:



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



metrics:



receivers: [kafka_metrics]



processors: [cumulativetodelta]



exporters: [otlp_http]
```

## Компоненты

В данной конфигурации настраиваются следующие компоненты.

### Приёмники

В разделе `receivers` указывается приёмник `kafka_metrics`.
Он настроен на сбор метрик с брокера Kafka, указанного в переменной окружения `BROKER_ADDRESS`.
Приёмник настроен на сбор метрик по брокерам, топикам и потребителям.

### Процессоры

Процессор `cumulativetodelta` необходим для преобразования кумулятивных метрик (в том виде, в котором их предоставляет Kafka) в [формат дельта-агрегации](/managed/ingest-from/opentelemetry/collector/configuration#delta-metrics "Как настроить OpenTelemetry Collector."), для совместимости с API приёма метрик Dynatrace.

### Экспортёры

В разделе `exporters` указывается стандартный [экспортёр `otlp_http`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter), который настраивается с URL API Dynatrace и необходимым токеном аутентификации.

Для этого задаются следующие две переменные окружения, на которые идёт ссылка в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL конечной точки API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`).
* `DT_API_TOKEN` содержит [токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.").

### Сервисы

В разделе `service` компоненты приёмника, процессора и экспортёра собираются в конвейер `metrics`. Этот конвейер:

1. Собирает метрики из Kafka.
2. Преобразует кумулятивные метрики в дельта-метрики.
3. Экспортирует данные в Dynatrace.

## Ограничения

### Избежание дублирования данных

Чтобы избежать дублирования данных, нужно убедиться, что только один OTel Collector собирает данные с заданной цели (например, брокер Kafka или конечная точка Prometheus).

При запуске нескольких реплик OTel Collector нужно настроить каждую из них на свою цель. Это предотвращает дублирование метрик и лишние затраты на приём данных.

[Target Allocator](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus/standard#architecture-overview "Разверните многоуровневую архитектуру Target Allocator, Scraper и Gateway для промышленного сбора метрик Prometheus с помощью OpenTelemetry Collector.") автоматически распределяет цели Prometheus между пулом экземпляров OTel Collector.

### Использование процессора `cumulativetodelta`

Многие приёмники OpenTelemetry, включая приёмник `kafka_metrics`, по умолчанию предоставляют кумулятивные метрики. Dynatrace требует дельта-метрики для корректной визуализации и анализа.

Чтобы преобразовать кумулятивные метрики в дельта-метрики, нужно включить процессор `cumulativetodelta` в конвейер метрик.
Рекомендуется использовать этот процессор, даже если ожидается, что часть метрик уже имеет дельта-темпоральность: такие метрики будут переданы дальше без дополнительной обработки.

Сохранение состояния

Процессор cumulativetodelta вычисляет дельту, запоминая предыдущее значение метрики. По этой причине вычисление точно только в том случае, если метрика непрерывно отправляется на один и тот же экземпляр OTel Collector.
Из-за этого процессор cumulativetodelta может работать не так, как ожидается, при использовании в развёртывании с несколькими экземплярами OTel Collector. При использовании этого процессора источнику данных лучше всего отправлять данные на единственный экземпляр OTel Collector.
Если нужно масштабировать экземпляры OTel Collector с сохранением состояния процессора, используйте [масштабирование с сохранением состояния](/managed/ingest-from/opentelemetry/collector/scaling#scaling-stateful-processing-using-non-pooled-collectors "Как масштабировать OpenTelemetry Collector.")

## Связанные темы

* [OTel Collector для приёма телеметрии в Dynatrace](/managed/ingest-from/opentelemetry/collector "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* [Развёртывание Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.")
* [Настройка OTel Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector.")
* [Приём данных OpenTelemetry с помощью приёмника Kafka](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/receiver "Как настроить приёмник Kafka в OpenTelemetry Collector для приёма OpenTelemetry из Kafka.")
* [Пересылка данных OpenTelemetry с помощью экспортёра Kafka](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/exporter "Как настроить OpenTelemetry Collector для пересылки данных OpenTelemetry с помощью экспортёра Kafka.")