---
title: Приём данных Jaeger с помощью OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/jaeger
---

# Приём данных Jaeger с помощью OTel Collector

# Приём данных Jaeger с помощью OTel Collector

* Практическое руководство
* 1 минута на чтение
* Опубликовано 11 окт. 2023 г.

Пример конфигурации ниже показывает, как настроить экземпляр Collector для приёма данных Jaeger, преобразования их в OTLP и отправки в бэкенд Dynatrace.

## Предварительные требования

* Один из следующих дистрибутивов Collector с [приёмником Jaeger﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/jaegerreceiver):

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [Пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* [URL конечной точки Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте о конечных точках OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.") для экспорта данных
* [Токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate)

О том, как настроить Collector с приведённой ниже конфигурацией, см. в разделах [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.") и [Конфигурация Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector.").

## Демонстрационная конфигурация

```
receivers:



jaeger:



protocols:



grpc:



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



traces:



receivers: [jaeger]



processors: []



exporters: [otlp_http]
```

Проверка конфигурации

[Проверьте свои настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

В нашей конфигурации мы настраиваем следующие компоненты.

### Receivers

В разделе `receivers` мы указываем приёмник `jaeger` в качестве активного компонента-приёмника для нашего экземпляра Collector.

Приёмник Jaeger можно настроить с помощью [ещё нескольких атрибутов﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/jaegerreceiver), которые в нашем примере оставлены со значениями по умолчанию.

### Exporters

В разделе `exporters` мы указываем стандартный [экспортёр `otlp_http`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter) и настраиваем его с помощью URL Dynatrace API и необходимого токена аутентификации.

Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL конечной точки Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте о конечных точках OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Пайплайны service

В разделе `service` мы, наконец, собираем объекты приёмника и экспортёра в пайплайн трасс, который будет обрабатывать преобразование данных Jaeger в OTLP.

## Похожие темы

* [Обогащение принимаемых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать телеметрические данные полями, специфичными для Dynatrace.")
* [Обогащение запросов OTLP данными Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Настройте OpenTelemetry Collector для обогащения запросов OTLP данными Kubernetes.")