---
title: Мониторинг Kafka с помощью OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/kafka/kafkametrics
scraped: 2026-05-12T12:15:08.106842
---

# Мониторинг Kafka с помощью OTel Collector

# Мониторинг Kafka с помощью OTel Collector

* Практическое руководство
* Чтение: 3 мин
* Опубликовано 26 ноября 2025 г.

В следующем примере конфигурации показано, как настроить экземпляр OTel Collector для сбора метрик Kafka с помощью компонента receiver `kafkametrics` и их приёма в виде запросов OTLP в Dynatrace.

## Предварительные требования

Для настройки этой конфигурации убедитесь, что у вас есть следующее:

* Один из следующих дистрибутивов Collector с [receiver kafkametrics](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/kafkametricsreceiver) и [processor cumulativetodelta](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/cumulativetodeltaprocessor)

  + [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* Развёрнутый сервер Kafka с доступным `BROKER_ADDRESS`.
  Дополнительные сведения см. в [руководстве по быстрому старту Apache Kafka](https://kafka.apache.org/quickstart).
* [URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."), на который должны экспортироваться данные.
* [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate).

См. [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.") и [Настройку Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector."), чтобы узнать, как настроить ваш Collector с приведённой ниже конфигурацией.

## Демонстрационная конфигурация

```
receivers:



kafkametrics:



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



receivers: [kafkametrics]



processors: [cumulativetodelta]



exporters: [otlp_http]
```

## Компоненты

Для нашей конфигурации мы настраиваем следующие компоненты.

### Receivers

В разделе `receivers` мы указываем receiver `kafkametrics`.
Мы настраиваем его для сбора метрик с брокера Kafka, указанного в переменной окружения `BROKER_ADDRESS`.
Receiver настроен на сбор метрик по брокерам, топикам и потребителям.

### Processors

Processor `cumulativetodelta` необходим для преобразования кумулятивных метрик (в том виде, в каком их сообщает Kafka) в [формат дельта-агрегации](/managed/ingest-from/opentelemetry/collector/configuration#delta-metrics "Как настроить OpenTelemetry Collector.") для совместимости с API приёма метрик Dynatrace.

### Exporters

В разделе `exporters` мы указываем стандартный [exporter `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) и настраиваем его с помощью URL нашего Dynatrace API и необходимого токена аутентификации.

Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`).
* `DT_API_TOKEN` содержит [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.").

### Службы

В разделе `service` мы собираем наши компоненты receiver, processor и exporter в конвейер `metrics`. Этот конвейер:

1. Собирает метрики из Kafka.
2. Преобразует кумулятивные метрики в дельта-метрики.
3. Экспортирует данные в Dynatrace.

## Пределы и ограничения

### Как избежать дублирования данных

Чтобы избежать дублирования данных, убедитесь, что данные с конкретной цели собирает только один OTel Collector (например, брокер Kafka или эндпоинт Prometheus).

Если вы запускаете несколько реплик OTel Collector, настройте каждую из них на отдельную цель. Это предотвращает дублирование метрик и лишние затраты на приём данных.

[Target Allocator](https://opentelemetry.io/docs/platforms/kubernetes/operator/target-allocator/) автоматически распределяет цели Prometheus внутри пула экземпляров OTel Collector.

### Использование processor `cumulativetodelta`

Многие компоненты receiver OpenTelemetry, включая receiver `kafkametrics`, по умолчанию сообщают кумулятивные метрики. Dynatrace требует дельта-метрики для корректной визуализации и анализа.

Чтобы преобразовать кумулятивные метрики в дельта-метрики, включите processor `cumulativetodelta` в ваш конвейер метрик.
Мы рекомендуем использовать этот processor, даже если вы ожидаете, что часть метрик уже имеет дельта-темпоральность, поскольку такие метрики будут пересылаться без дополнительной обработки.

Сохранение состояния

Processor cumulativetodelta вычисляет дельту, запоминая предыдущее значение метрики. По этой причине вычисление является точным только в том случае, если метрика непрерывно отправляется в один и тот же экземпляр OTel Collector.
В результате processor cumulativetodelta может работать не так, как ожидается, если используется в развёртывании с несколькими экземплярами OTel Collector. При использовании этого processor лучше всего, чтобы источник данных отправлял данные в один экземпляр OTel Collector.
Если вам нужно масштабировать OTel Collector с сохранением состояния processor, используйте [масштабирование с сохранением состояния](/managed/ingest-from/opentelemetry/collector/scaling#scaling-stateful-processing-using-non-pooled-collectors "Как масштабировать OpenTelemetry Collector.")

## Связанные темы

* [OTel Collector для приёма телеметрии в Dynatrace](/managed/ingest-from/opentelemetry/collector "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* [Развёртывание Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.")
* [Настройка OTel Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector.")
* [Приём данных OpenTelemetry с помощью receiver Kafka](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/receiver "Как настроить receiver Kafka в OpenTelemetry Collector для приёма OpenTelemetry из Kafka.")
* [Пересылка данных OpenTelemetry с помощью exporter Kafka](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/exporter "Как настроить OpenTelemetry Collector для пересылки данных OpenTelemetry с помощью exporter Kafka.")