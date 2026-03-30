---
title: Прием данных Zipkin с помощью OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/zipkin
scraped: 2026-03-05T21:40:00.956915
---

# Приём данных Zipkin с помощью OpenTelemetry Collector


Следующий пример конфигурации показывает, как настроить экземпляр Collector для приёма данных Zipkin, их преобразования в OTLP и отправки в серверную часть Dynatrace.

## Ограничения

### Требования B3

Обратите внимание на требования B3, чтобы избежать отбрасывания спанов из-за общих и дублирующихся идентификаторов спанов. Подробнее см. в [спецификации пропагатора](https://opentelemetry.io/docs/specs/otel/context/api-propagators/#b3-requirements).

Например, если вы используете [Spring Cloud Sleuth](https://cloud.spring.io/spring-cloud-sleuth/2.1.x/multi/multi__propagation.html#_extracting_a_propagated_context), для отключения совместного использования спанов можно применить следующую настройку конфигурации:

```
spring:


sleuth:


supports-join: false
```

### Маршрутизация через единый Collector

Убедитесь, что все связанные спаны Zipkin/B3 маршрутизируются через один и тот же экземпляр Collector для обеспечения полного приёма данных. Если часть спанов принимается только через OneAgent, они могут быть не связаны должным образом и не отображаться как связанные с вашими спанами Zipkin.

## Предварительные требования

* Один из следующих дистрибутивов Collector с [приёмником Zipkin](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/receiver/zipkinreceiver):

  + [Dynatrace Collector](../../collector.md#dt-collector-dist "Learn about the Dynatrace OTel Collector.")
  + OpenTelemetry [Contrib](../../collector.md#collector-contrib "Learn about the Dynatrace OTel Collector.")
  + [Пользовательская версия Builder](../../collector.md#collector-builder "Learn about the Dynatrace OTel Collector.")
* URL-адрес конечной точки Dynatrace API, на который должны отправляться данные
* [Токен API](../../otlp-api.md#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") с соответствующей областью доступа (требуется для ActiveGate)

Сведения о настройке Collector с конфигурацией ниже см. в разделах Развёртывание Collector и Конфигурация Collector.

## Пример конфигурации

```
receivers:


zipkin:


exporters:


otlp_http:


endpoint: ${env:DT_ENDPOINT}


headers:


Authorization: "Api-Token ${env:DT_API_TOKEN}"


service:


pipelines:


traces:


receivers: [zipkin]


processors: []


exporters: [otlp_http]
```

Проверка конфигурации

[Проверьте свои настройки](../configuration.md#validate "How to configure the OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

Для нашей конфигурации мы настраиваем следующие компоненты.

### Приёмники

В разделе `receivers` мы указываем приёмник `zipkin` как активный компонент-приёмник для нашего экземпляра Collector.

Приёмник Zipkin можно настроить с помощью [нескольких дополнительных атрибутов](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/receiver/zipkinreceiver), которые в нашем примере оставлены со значениями по умолчанию.

### Экспортёры

В разделе `exporters` мы указываем стандартный [экспортёр `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) и настраиваем его с помощью URL-адреса Dynatrace API и необходимого токена аутентификации.

Для этого мы задаём следующие две переменные среды и ссылаемся на них в значениях конфигурации для `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL-адрес конечной точки Dynatrace API](../../otlp-api.md#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [токен API](../../otlp-api.md#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Конвейеры сервиса

В разделе `service` мы в итоге объединяем объекты приёмника и экспортёра в конвейер трассировок, который будет обрабатывать преобразование Zipkin в OTLP.

## Связанные темы

* Обогащение принятых данных полями, специфичными для Dynatrace
* Обогащение OTLP-запросов данными Kubernetes
