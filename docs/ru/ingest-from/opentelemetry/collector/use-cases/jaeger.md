---
title: Прием данных Jaeger с помощью OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/jaeger
scraped: 2026-03-03T21:22:57.338777
---

# Приём данных Jaeger с помощью OpenTelemetry Collector


Следующий пример конфигурации показывает, как настроить экземпляр Collector для приёма данных Jaeger, преобразования их в OTLP и отправки в бэкенд Dynatrace.

## Предварительные требования

* Одна из следующих дистрибуций Collector с [приёмником Jaeger](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/receiver/jaegerreceiver):

  + [Dynatrace Collector](../../collector.md#dt-collector-dist "Узнайте о Dynatrace OTel Collector.")
  + [OpenTelemetry Contrib](../../collector.md#collector-contrib "Узнайте о Dynatrace OTel Collector.")
  + [Пользовательская версия Builder](../../collector.md#collector-builder "Узнайте о Dynatrace OTel Collector.")
* [URL конечной точки Dynatrace API](../../otlp-api.md "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."), на которую должны экспортироваться данные
* [Токен API](../../otlp-api.md#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate)

Подробнее о настройке Collector с приведённой ниже конфигурацией см. в разделах [Развёртывание Collector](../deployment.md "Как развернуть Dynatrace OTel Collector.") и [Конфигурация Collector](../configuration.md "Как настроить OpenTelemetry Collector.").

## Пример конфигурации

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

[Проверьте свои настройки](../configuration.md#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

В нашей конфигурации мы настраиваем следующие компоненты.

### Приёмники (Receivers)

В разделе `receivers` мы указываем приёмник `jaeger` в качестве активного компонента-приёмника для нашего экземпляра Collector.

Приёмник Jaeger можно настроить с помощью [нескольких дополнительных атрибутов](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/receiver/jaegerreceiver), которые в нашем примере оставлены со значениями по умолчанию.

### Экспортёры (Exporters)

В разделе `exporters` мы указываем стандартный [экспортёр `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) и настраиваем его с URL Dynatrace API и необходимым токеном аутентификации.

Для этого мы задаём следующие две переменные среды и ссылаемся на них в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL конечной точки Dynatrace API](../../otlp-api.md#export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [токен API](../../otlp-api.md#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Сервисные конвейеры (Service pipelines)

В разделе `service` мы объединяем объекты приёмника и экспортёра в конвейер трассировок, который будет выполнять преобразование данных Jaeger в OTLP.

## Связанные темы

* [Обогащение принятых данных полями, специфичными для Dynatrace](../../../extend-dynatrace/extend-data.md "Узнайте, как автоматически обогащать телеметрические данные полями, специфичными для Dynatrace.")
* [Обогащение запросов OTLP данными Kubernetes](kubernetes/k8s-enrich.md "Настройте OpenTelemetry Collector для обогащения запросов OTLP данными Kubernetes.")
