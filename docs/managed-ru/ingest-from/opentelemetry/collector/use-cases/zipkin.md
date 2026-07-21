---
title: Приём данных Zipkin с помощью OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/zipkin
---

# Приём данных Zipkin с помощью OTel Collector

# Приём данных Zipkin с помощью OTel Collector

* Практическое руководство
* Чтение за 2 минуты
* Опубликовано 11 окт. 2023 г.

Следующий пример конфигурации показывает, как настроить экземпляр Collector для приёма данных Zipkin, преобразования их в OTLP и отправки в бэкенд Dynatrace.

## Ограничения

### Требования B3

Обратить внимание на требования B3, чтобы избежать отбрасывания спанов из-за общих и дублирующихся идентификаторов спанов. Подробнее см. [спецификацию propagator﻿](https://opentelemetry.io/docs/specs/otel/context/api-propagators/#b3-requirements).

Например, при использовании [Spring Code Sleuth﻿](https://cloud.spring.io/spring-cloud-sleuth/2.1.x/multi/multi__propagation.html#_extracting_a_propagated_context) можно применить следующую настройку конфигурации, чтобы отключить совместное использование спанов:

```
spring:



sleuth:



supports-join: false
```

### Маршрутизация через один Collector

Необходимо направлять все связанные спаны Zipkin/B3 через один и тот же экземпляр Collector, чтобы гарантировать полный приём данных. Если часть спанов принимается только через OneAgent, они могут быть связаны неправильно и не будут отображаться как связанные со спанами Zipkin.

## Предварительные требования

* Один из следующих дистрибутивов Collector с [Zipkin receiver﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/zipkinreceiver):

  + [OTel Collector Dynatrace](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + OpenTelemetry [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [Пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* [URL-адрес конечной точки Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."), на который должны экспортироваться данные
* [Токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate)

О том, как настроить Collector с приведённой ниже конфигурацией, см. [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.") и [Конфигурация Collector](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.").

## Демонстрационная конфигурация

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

[Проверить настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

В этой конфигурации настраиваются следующие компоненты.

### Receivers

В разделе `receivers` указывается receiver `zipkin` в качестве активного компонента-приёмника для экземпляра Collector.

Receiver Zipkin можно настроить с помощью [ещё нескольких атрибутов﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/zipkinreceiver), которые в этом примере остаются со значениями по умолчанию.

### Exporters

В разделе `exporters` указывается стандартный [exporter `otlp_http`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter) и настраивается с помощью URL API Dynatrace и необходимого токена аутентификации.

Для этого задаются следующие две переменные окружения, на которые делаются ссылки в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL конечной точки Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Пайплайны службы

В разделе `service` в итоге собираются объекты receiver и exporter в пайплайн traces, который будет выполнять преобразование Zipkin в OTLP.

## Связанные темы

* [Обогащение принятых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")
* [Обогащение запросов OTLP данными Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")