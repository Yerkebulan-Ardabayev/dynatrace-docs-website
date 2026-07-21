---
title: Преобразование OTLP gRPC в HTTP с помощью OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/grpc
---

# Преобразование OTLP gRPC в HTTP с помощью OTel Collector

# Преобразование OTLP gRPC в HTTP с помощью OTel Collector

* Практическое руководство
* Чтение за 1 минуту
* Опубликовано 11 октября 2023 г.

Следующий пример конфигурации показывает, как настроить экземпляр Collector для преобразования запроса gRPC OTLP в его HTTP-аналог.

## Предварительные требования

* Один из следующих дистрибутивов Collector:

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + OpenTelemetry [Core](/managed/ingest-from/opentelemetry/collector#collector-core "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.") или [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [Пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* [URL конечной точки Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."), в которую нужно экспортировать данные
* [Токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate)

О том, как настроить Collector с приведённой ниже конфигурацией, см. [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.") и [Конфигурация Collector](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.").

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

[Проверьте свои настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

Для нашей конфигурации настраиваются следующие компоненты.

### Приёмники (Receivers)

В разделе `receivers` указывается gRPC [`otlp` receiver﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/receiver/otlpreceiver) в качестве активного компонента-приёмника для нашего экземпляра Collector.

### Экспортёры (Exporters)

В разделе `exporters` указывается стандартный [`otlp_http` exporter﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter), и он настраивается с указанием URL Dynatrace API и необходимого токена аутентификации.

Для этого задаются следующие две переменные окружения, на которые есть ссылки в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL конечной точки Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Пайплайны сервиса (Service pipelines)

В разделе `service` в итоге собираются объекты приёмника и экспортёра в пайплайны, которые явно принимают запросы gRPC и пересылают их по HTTP в Dynatrace.

## Ограничения

Данные поступают с использованием протокола OpenTelemetry (OTLP) через [API-ы OTLP Dynatrace](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") и подчиняются ограничениям и лимитам API.
Подробнее см.:

* [Ограничения метрик OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Сопоставление метрик Dynatrace](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Приём логов OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")

## Похожие темы

* [Обогащение поступающих данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")
* [Обогащение запросов OTLP данными Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")