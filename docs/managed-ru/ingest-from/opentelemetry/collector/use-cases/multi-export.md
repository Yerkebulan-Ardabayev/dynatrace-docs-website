---
title: Отправка данных OpenTelemetry в несколько бэкендов
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/multi-export
---

# Отправка данных OpenTelemetry в несколько бэкендов

# Отправка данных OpenTelemetry в несколько бэкендов

* Практическое руководство
* Чтение 2 мин
* Опубликовано 26 января 2024 г.

Пример конфигурации ниже показывает, как настроить экземпляр Collector для одновременной отправки телеметрических данных в несколько бэкендов.

## Предварительные требования

* Один из следующих дистрибутивов Collector:

  + [OTel Collector Dynatrace](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + OpenTelemetry [Core](/managed/ingest-from/opentelemetry/collector#collector-core "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.") или [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [Пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* Для Dynatrace:

  + [URL конечной точки API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."), на который нужно экспортировать данные
  + [Токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate)
* URL для приёма данных и все применимые учётные данные для аутентификации для остальных бэкендов

О том, как настроить Collector с указанной ниже конфигурацией, см. в разделах [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.") и [Настройка Collector](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.").

## Демонстрационная конфигурация

```
receivers:



otlp:



protocols:



grpc:



endpoint: 0.0.0.0:4317



http:



endpoint: 0.0.0.0:4318



exporters:



otlp_http/dynatrace:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



otlp_grpc/coldstorage:



endpoint: my.coldstorage.example:4317



service:



pipelines:



traces:



receivers: [otlp]



processors: []



exporters: [otlp_http/dynatrace, otlp_grpc/coldstorage]



metrics:



receivers: [otlp]



processors: []



exporters: [otlp_http/dynatrace, otlp_grpc/coldstorage]



logs:



receivers: [otlp]



processors: []



exporters: [otlp_http/dynatrace, otlp_grpc/coldstorage]
```

Проверка конфигурации

[Проверьте свои настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

В нашей конфигурации настраиваются следующие компоненты.

### Receivers

В разделе `receivers` мы указываем [приёмник `otlp`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/receiver/otlpreceiver) в качестве активного компонента-приёмника для нашего экземпляра Collector.

### Exporters

В разделе `exporters` мы указываем следующие экземпляры экспортёров для наших бэкендов.

* [Экспортёр `otlp_http`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter) для Dynatrace
* Экспортёр gRPC [`otlp`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlpexporter) для системы холодного хранения

Для экспортёра Dynatrace мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации для `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL конечной точки API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Пайплайны службы

В разделе `service` мы в итоге собираем объекты приёмника и экспортёра в пайплайны, которые принимают любой запрос OTLP (HTTP и gRPC) и пересылают его в настроенные бэкенды, используя настроенные экспортёры.

## Лимиты и ограничения

Данные принимаются с использованием протокола OpenTelemetry (OTLP) через [APIы OTLP Dynatrace](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") и подпадают под лимиты и ограничения API.
Подробнее см.:

* [Ограничения метрик OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Сопоставление метрик Dynatrace](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Приём логов OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")

## Похожие темы

* [Обогащение принимаемых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")
* [Обогащение запросов OTLP данными Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")