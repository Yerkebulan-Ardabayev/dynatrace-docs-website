---
title: Получение данных OpenTelemetry с помощью Kafka receiver
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/kafka/receiver
---

# Получение данных OpenTelemetry с помощью Kafka receiver

# Получение данных OpenTelemetry с помощью Kafka receiver

* Практическое руководство
* 3 мин на чтение
* Опубликовано 5 нояб. 2025 г.

В следующем примере конфигурации показано, как настроить Kafka для чтения данных из топиков и передачи этих данных через OTLP.

## Предварительные требования

* Развёрнутый и настроенный дистрибутив коллектора, будь то

  + [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии от OpenTelemetry.")
  + [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии от OpenTelemetry.")
  + [собственная версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии от OpenTelemetry.")
* Компонент [`kafkareceiver`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/kafkareceiver).
* Развёрнутый сервер Kafka с доступным `BROKER_ADDRESS`.
  Подробнее см. [руководство по быстрому старту Kafka Apache﻿](https://kafka.apache.org/quickstart).
* [URL конечной точки Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте про конечные точки OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace."), на которую нужно экспортировать данные.
* [Токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте про конечные точки OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа. (Только для экспорта в SaaS и ActiveGate.)

## Демонстрационная конфигурация

Ниже приведён пример файла YAML для базовой конфигурации коллектора, которую можно использовать для получения трасс, метрик и логов OpenTelemetry из Kafka.

```
receivers:



kafka:



tls:



insecure: true # Необходимо только в том случае, если сервер Kafka не предоставляет сертификат, которому доверяет OTel Collector.



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

Чтобы эта конфигурация работала, нужно задать следующие переменные окружения.

* `BROKER_ADDRESS`: значение, специфичное для сервера Kafka.
* `DT_ENDPOINT`: [базовый URL конечной точки Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте про конечные точки OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`).
* `DT_API_TOKEN`: [токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте про конечные точки OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.").

Проверка конфигурации

[Проверьте свои настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

В нашей конфигурации мы настраиваем определённые компоненты, описанные в разделах ниже.

### Receivers

В разделе `receivers` мы указываем [`kafka`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/kafkareceiver) в качестве активного компонента receiver для нашего развёртывания.
Это необходимо для получения данных с сервера Kafka.

### Exporters

В разделе `exporters` мы указываем [экспортёр `otlp_http`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter) для передачи данных в Dynatrace.

Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL конечной точки Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте про конечные точки OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`).
* `DT_API_TOKEN` содержит [токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте про конечные точки OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.").

### Конвейер сервиса

В разделе `service` мы собираем объекты receiver и exporter в конвейеры сервиса, которые выполняют следующие шаги:

1. Получение данных с сервера Kafka.
2. Экспорт данных в Dynatrace.

## Связанные темы

* [OTel Collector для приёма телеметрии в Dynatrace](/managed/ingest-from/opentelemetry/collector "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии от OpenTelemetry.")
* [Буферизация данных через Kafka с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/kafka "Как настроить OpenTelemetry Collector для буферизации данных через Kafka.")
* [Передача данных OpenTelemetry с помощью Kafka exporter](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/exporter "Как настроить OpenTelemetry Collector для передачи данных OpenTelemetry с помощью Kafka exporter.")
* [Развёртывание Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.")
* [Настройка OTel Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector.")