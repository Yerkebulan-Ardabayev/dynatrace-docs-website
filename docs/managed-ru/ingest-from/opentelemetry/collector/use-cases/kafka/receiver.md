---
title: Приём данных OpenTelemetry с помощью receiver Kafka
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/kafka/receiver
scraped: 2026-05-12T12:15:06.191704
---

# Приём данных OpenTelemetry с помощью receiver Kafka

# Приём данных OpenTelemetry с помощью receiver Kafka

* Практическое руководство
* Чтение: 3 мин
* Опубликовано 05 ноября 2025 г.

В следующем примере конфигурации показано, как настроить Kafka для чтения данных из топиков и передачи этих данных через OTLP.

## Предварительные требования

* Развёрнутый и настроенный дистрибутив Collector, будь то

  + [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* Компонент [`kafkareceiver`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/kafkareceiver).
* Развёрнутый сервер Kafka с доступным `BROKER_ADDRESS`.
  Дополнительные сведения см. в [руководстве по быстрому старту Apache Kafka](https://kafka.apache.org/quickstart).
* [URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."), на который должны экспортироваться данные.
* [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа. (Только для экспорта в SaaS и ActiveGate.)

## Демонстрационная конфигурация

Ниже приведён пример YAML-файла для базовой конфигурации Collector, который можно использовать для приёма трассировок, метрик и логов OpenTelemetry из Kafka.

```
receivers:



kafka:



tls:



insecure: true # Only necessary if your Kafka server does not provide a certificate that's trusted by the OTel Collector.



traces:



metrics:



logs:



brokers: ["${env:BROKER_ADDRESS}"]



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



traces:



receivers: [kafka]



exporters: [otlp_http]



metrics:



receivers: [kafka]



exporters: [otlp_http]



logs:



receivers: [kafka]



exporters: [otlp_http]
```

Чтобы эта конфигурация работала, необходимо задать следующие переменные окружения.

* `BROKER_ADDRESS`: зависит от вашего сервера Kafka.
* `DT_ENDPOINT`: [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`).
* `DT_API_TOKEN`: [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.").

Проверка конфигурации

[Проверьте ваши настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

Для нашей конфигурации мы настраиваем определённые компоненты, как описано в разделах ниже.

### Receivers

В разделе `receivers` мы указываем [`kafka`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/kafkareceiver) в качестве активного компонента receiver для нашего развёртывания.
Это необходимо для приёма данных с сервера Kafka.

### Exporters

В разделе `exporters` мы указываем [exporter `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) для пересылки данных в Dynatrace.

Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`).
* `DT_API_TOKEN` содержит [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.").

### Сервисный конвейер

В разделе `service` мы собираем наши объекты receiver и exporter в сервисные конвейеры, которые выполняют следующие шаги:

1. Принимают данные с сервера Kafka.
2. Экспортируют данные в Dynatrace.

## Связанные темы

* [OTel Collector для приёма телеметрии в Dynatrace](/managed/ingest-from/opentelemetry/collector "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* [Буферизация данных через Kafka с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/kafka "Как настроить OpenTelemetry Collector для буферизации данных через Kafka.")
* [Пересылка данных OpenTelemetry с помощью exporter Kafka](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/exporter "Как настроить OpenTelemetry Collector для пересылки данных OpenTelemetry с помощью exporter Kafka.")
* [Развёртывание Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.")
* [Настройка OTel Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector.")