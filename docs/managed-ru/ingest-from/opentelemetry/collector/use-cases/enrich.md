---
title: Обогащение OTLP данными OneAgent (вне контейнеров)
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/enrich
scraped: 2026-05-12T12:10:48.299967
---

# Обогащение OTLP данными OneAgent (вне контейнеров)

# Обогащение OTLP данными OneAgent (вне контейнеров)

* Практическое руководство
* Чтение: 2 мин
* Обновлено 17 декабря 2025 г.

В следующем примере конфигурации показано, как настроить экземпляр Collector для обогащения данных OpenTelemetry сущностями хостов OneAgent.

Обогащение используется для связывания данных OpenTelemetry с их хостом OneAgent и корректного сопоставления в модели топологии. Например, при приёме логов с разных хостов привязка сущности хоста к соответствующим данным логов позволяет выполнять задачи аналитики логов на основе хостов.

Контейнерные среды

Обогащение применимо только к неконтейнерным средам OneAgent. Настройка обогащения в контейнеризированном Collector может привести к некорректным сопоставлениям хостов и топологии.

## Предварительные требования

* Один из следующих дистрибутивов Collector с [processor Resource Detection](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/processor/resourcedetectionprocessor):

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + OpenTelemetry [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* OneAgent, работающий на том же хосте, что и OTel Collector, при этом OneAgent ведёт мониторинг в режиме Full-Stack, Infrastructure или Foundation & Discovery.
* [URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."), на который должны экспортироваться данные, заданный как системная переменная окружения
* [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate), заданный как системная переменная окружения

См. [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.") и [Настройку Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector."), чтобы узнать, как настроить ваш Collector с приведённой ниже конфигурацией.

## Демонстрационная конфигурация

```
receivers:



otlp:



protocols:



grpc:



endpoint: 0.0.0.0:4317



http:



endpoint: 0.0.0.0:4318



processors:



resourcedetection/dynatrace:



detectors: [dynatrace]



override: false



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



traces:



receivers: [otlp]



processors: [resourcedetection/dynatrace]



exporters: [otlp_http]



metrics:



receivers: [otlp]



processors: [resourcedetection/dynatrace]



exporters: [otlp_http]



logs:



receivers: [otlp]



processors: [resourcedetection/dynatrace]



exporters: [otlp_http]
```

Проверка конфигурации

[Проверьте ваши настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

Для нашей конфигурации мы настраиваем следующие компоненты.

### Receivers

В разделе `receivers` мы указываем стандартный receiver `otlp` в качестве активного компонента receiver для нашего экземпляра Collector.

Это сделано в основном в демонстрационных целях. Здесь можно указать любой другой допустимый receiver (например, `zipkin`).

### Processors

В разделе `processors` мы указываем [processor `resourcedetection`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/processor/resourcedetectionprocessor) и настраиваем его с помощью [специфичного для Dynatrace детектора `dynatrace`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/processor/resourcedetectionprocessor/README.md#dynatrace).

При такой конфигурации processor определения ресурсов попытается загрузить следующие три атрибута из [файла обогащения OneAgent](/managed/ingest-from/extend-dynatrace/extend-data#dynatrace-oneagent "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace."):

* `dt.entity.host`
* `host.name`
* `dt.smartscape.host`

Если processor определения ресурсов смог успешно загрузить эти значения, он добавит их в запрос OTLP в качестве атрибутов ресурса. Дополнительная настройка processor не требуется.

### Exporters

В разделе `exporters` мы указываем стандартный [exporter `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) и настраиваем его с помощью URL нашего Dynatrace API и необходимого токена аутентификации.

Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `headers`.

* `DT_ENDPOINT` содержит [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Сервисный конвейер

В разделе `service` мы собираем наши объекты receiver, processor и exporter в сервисные конвейеры, которые выполнят следующие шаги:

* принимают запросы OTLP на настроенных портах
* обогащают их данными хоста, релевантными для Dynatrace, с помощью processor определения ресурсов
* и экспортируют обогащённые данные в Dynatrace