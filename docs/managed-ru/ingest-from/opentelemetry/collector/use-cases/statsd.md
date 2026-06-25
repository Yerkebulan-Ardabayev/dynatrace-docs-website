---
title: Приём данных StatsD с помощью OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/statsd
scraped: 2026-05-12T11:50:07.550301
---

# Приём данных StatsD с помощью OTel Collector

# Приём данных StatsD с помощью OTel Collector

* Практическое руководство
* Чтение: 2 мин
* Опубликовано 09 июля 2024 г.

В следующем примере конфигурации показано, как настроить экземпляр Collector для приёма данных из существующей установки StatsD и их импорта в виде запроса OTLP в Dynatrace.

## Предварительные требования

* Приложение, генерирующее [сообщения StatsD](https://github.com/statsd/statsd/blob/master/docs/metric_types.md)
* Один из следующих дистрибутивов Collector с [receiver StatsD](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/statsdreceiver), [processor transform](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor) и [processor filter](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/filterprocessor):

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + OpenTelemetry [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* [URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."), на который должны экспортироваться данные
* [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate)

См. [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.") и [Настройку Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector."), чтобы узнать, как настроить ваш Collector с приведённой ниже конфигурацией.

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

[Проверьте ваши настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

Для нашей конфигурации мы настраиваем следующие компоненты.

### Receivers

В разделе `receivers` мы указываем receiver `statsd` в качестве активного компонента receiver для нашего экземпляра Collector. Мы настраиваем receiver на прослушивание всех сетевых интерфейсов на порту `8125`, который обычно используется для StatsD.

Receiver настроен на агрегирование сообщений histogram, timer и distribution в экспоненциальные гистограммы, которые затем обрабатываются для приёма в Dynatrace. Receiver использует экспоненциальные гистограммы с автомасштабированием, и мы выбрали максимальный размер `100`. Это означает, что гистограмма начинается с очень детальных границ интервалов и автоматически перемасштабируется, если получает точки данных, которые привели бы к более чем `100` интервалам.

Полный список параметров конфигурации и поддерживаемых типов метрик StatsD см. в [документации по receiver StatsD](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/receiver/statsdreceiver/README.md).

### Exporters

В разделе `exporters` мы указываем стандартный [exporter `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) и настраиваем его с помощью URL нашего Dynatrace API и необходимого токена аутентификации.

Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `headers`.

* `DT_ENDPOINT` содержит [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Сервисный конвейер

В разделе `service` мы собираем наши объекты receiver, processor и exporter в конвейер метрик, который принимает данные StatsD и передаёт их в Dynatrace.

## Пределы и ограничения

Метрики принимаются с помощью протокола OpenTelemetry (OTLP) через [Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") и подчиняются ограничениям и лимитам этого API.
Дополнительные сведения см.:

* [Ограничения метрик OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")
* [Сопоставление метрик Dynatrace](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")

## Связанные темы

* [Сбор метрик Prometheus с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus "Настройте OpenTelemetry Collector для сбора ваших данных Prometheus.")