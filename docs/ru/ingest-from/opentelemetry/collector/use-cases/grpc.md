---
title: Transform OTLP gRPC to HTTP with the OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/grpc
scraped: 2026-03-03T21:32:35.758185
---

# Преобразование OTLP gRPC в HTTP с помощью OpenTelemetry Collector

# Преобразование OTLP gRPC в HTTP с помощью OpenTelemetry Collector

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Oct 11, 2023

В следующем примере конфигурации показано, как настроить экземпляр Collector для преобразования gRPC OTLP-запроса в его HTTP-аналог.

## Предварительные требования

* Один из следующих дистрибутивов Collector:

  + [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте о Dynatrace OTel Collector.")
  + OpenTelemetry [Core](/docs/ingest-from/opentelemetry/collector#collector-core "Узнайте о Dynatrace OTel Collector.") или [Contrib](/docs/ingest-from/opentelemetry/collector#collector-contrib "Узнайте о Dynatrace OTel Collector.")
  + [Пользовательская версия Builder](/docs/ingest-from/opentelemetry/collector#collector-builder "Узнайте о Dynatrace OTel Collector.")
* [URL-адрес конечной точки API Dynatrace](/docs/ingest-from/opentelemetry/otlp-api "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."), в которую должны экспортироваться данные
* [Токен API](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate)

Сведения о настройке Collector с приведённой ниже конфигурацией см. в разделах [Развёртывание Collector](/docs/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OTel Collector.") и [Конфигурация Collector](/docs/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector.").

## Демонстрационная конфигурация

```
receivers:



otlp:



protocols:



grpc:



endpoint: 0.0.0.0:4317



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



traces:



receivers: [otlp]



processors: []



exporters: [otlp_http]



metrics:



receivers: [otlp]



processors: []



exporters: [otlp_http]



logs:



receivers: [otlp]



processors: []



exporters: [otlp_http]
```

Проверка конфигурации

[Проверьте ваши настройки](/docs/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

Для нашей конфигурации мы настраиваем следующие компоненты.

### Receivers (получатели)

В разделе `receivers` мы указываем gRPC [`otlp` receiver](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/receiver/otlpreceiver) как активный компонент получателя для нашего экземпляра Collector.

### Exporters (экспортёры)

В разделе `exporters` мы указываем стандартный [`otlp_http` exporter](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) и настраиваем его с URL-адресом API Dynatrace и необходимым токеном аутентификации.

Для этого мы задаём следующие две переменные среды и ссылаемся на них в значениях конфигурации для `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL конечной точки API Dynatrace](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [токен API](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Конвейеры служб

В разделе `service` мы в итоге собираем объекты получателя и экспортёра в конвейеры, которые явно принимают gRPC-запросы и пересылают их в Dynatrace по HTTP.

## Ограничения

Данные принимаются с использованием протокола OpenTelemetry (OTLP) через [Dynatrace OTLP APIs](/docs/ingest-from/opentelemetry/otlp-api "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") и подпадают под ограничения и лимиты API.
Дополнительные сведения см. в:

* [Ограничения метрик OpenTelemetry](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")
* [Сопоставление метрик Dynatrace](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")
* [Приём журналов OpenTelemetry](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Узнайте, как Dynatrace принимает записи журналов OpenTelemetry и какие ограничения применяются.")

## Связанные темы

* [Обогащение принятых данных полями, специфичными для Dynatrace](/docs/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.")
* [Обогащение OTLP-запросов данными Kubernetes](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Настройте OpenTelemetry Collector для обогащения OTLP-запросов данными Kubernetes.")
