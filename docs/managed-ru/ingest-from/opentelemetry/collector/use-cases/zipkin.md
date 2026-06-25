---
title: Приём данных Zipkin с помощью OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/zipkin
scraped: 2026-05-12T12:10:58.126890
---

# Приём данных Zipkin с помощью OTel Collector

# Приём данных Zipkin с помощью OTel Collector

* Практическое руководство
* Чтение: 2 мин
* Опубликовано 11 октября 2023 г.

В следующем примере конфигурации показано, как настроить экземпляр Collector для приёма данных Zipkin, их преобразования в OTLP и отправки в бэкенд Dynatrace.

## Ограничения

### Требования B3

Обратите внимание на требования B3, чтобы избежать отбрасывания спанов из-за общих и дублирующихся идентификаторов спанов. Подробнее см. в [спецификации пропагатора](https://opentelemetry.io/docs/specs/otel/context/api-propagators/#b3-requirements).

Например, если вы используете [Spring Code Sleuth](https://cloud.spring.io/spring-cloud-sleuth/2.1.x/multi/multi__propagation.html#_extracting_a_propagated_context), для отключения совместного использования спанов можно задать следующий параметр конфигурации:

```
spring:



sleuth:



supports-join: false
```

### Маршрутизация через один Collector

Убедитесь, что все связанные спаны Zipkin/B3 маршрутизируются через один и тот же экземпляр Collector, чтобы гарантировать полный приём данных. Если часть спанов принимается только с помощью OneAgent, они могут быть связаны некорректно и не отображаться как соединённые с вашими спанами Zipkin.

## Предварительные требования

* Один из следующих дистрибутивов Collector с [receiver Zipkin](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/zipkinreceiver):

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + OpenTelemetry [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* [URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."), на который должны экспортироваться данные
* [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate)

См. [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.") и [Настройку Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector."), чтобы узнать, как настроить ваш Collector с приведённой ниже конфигурацией.

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

[Проверьте ваши настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

Для нашей конфигурации мы настраиваем следующие компоненты.

### Receivers

В разделе `receivers` мы указываем receiver `zipkin` в качестве активного компонента receiver для нашего экземпляра Collector.

Receiver Zipkin можно настроить с помощью [нескольких дополнительных атрибутов](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/zipkinreceiver), которые в нашем примере мы оставляем со значениями по умолчанию.

### Exporters

В разделе `exporters` мы указываем стандартный [exporter `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) и настраиваем его с помощью URL нашего Dynatrace API и необходимого токена аутентификации.

Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Сервисные конвейеры

В разделе `service` мы в итоге собираем наши объекты receiver и exporter в конвейер трассировок, который выполнит преобразование наших данных Zipkin в OTLP.

## Связанные темы

* [Обогащение принимаемых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.")
* [Обогащение запросов OTLP данными Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Настройте OpenTelemetry Collector для обогащения запросов OTLP данными Kubernetes.")