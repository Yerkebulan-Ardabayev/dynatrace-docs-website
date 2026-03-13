---
title: Enrich OTLP with OneAgent data (non-containerized)
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/enrich
scraped: 2026-03-06T21:26:31.410651
---

# Обогащение OTLP данными OneAgent (неконтейнерная среда)

# Обогащение OTLP данными OneAgent (неконтейнерная среда)

* Latest Dynatrace
* Руководство
* Чтение: 2 мин
* Обновлено 17 дек. 2025

Следующий пример конфигурации показывает, как настроить экземпляр Collector для обогащения данных OpenTelemetry сущностями хостов OneAgent.

Обогащение используется для связывания данных OpenTelemetry с соответствующим хостом OneAgent и правильной ассоциации их в рамках модели топологии. Например, при приёме логов с различных хостов привязка сущности хоста к соответствующим данным логов позволяет выполнять аналитические задачи на уровне хоста.

Контейнерные среды

Обогащение предназначено для неконтейнерных сред OneAgent. Настройка обогащения для контейнеризированного Collector может привести к некорректным ассоциациям хостов и топологии.

## Предварительные требования

* Один из следующих дистрибутивов Collector с процессором [Resource Detection](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/resourcedetectionprocessor):

  + [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте о Dynatrace OTel Collector.")
  + OpenTelemetry [Contrib](/docs/ingest-from/opentelemetry/collector#collector-contrib "Узнайте о Dynatrace OTel Collector.")
  + [Пользовательская версия Builder](/docs/ingest-from/opentelemetry/collector#collector-builder "Узнайте о Dynatrace OTel Collector.")
* OneAgent, работающий на том же хосте, что и Collector, где OneAgent осуществляет мониторинг в режиме Full-Stack, Infrastructure или Foundation & Discovery.
* [URL-адрес конечной точки API Dynatrace](/docs/ingest-from/opentelemetry/otlp-api "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."), на которую должны экспортироваться данные, настроенный как системная переменная окружения
* [Токен API](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate), настроенный как системная переменная окружения

См. разделы [Развёртывание Collector](/docs/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OTel Collector.") и [Настройка Collector](/docs/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector.") для получения информации о настройке вашего Collector с приведённой ниже конфигурацией.

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

[Проверьте ваши настройки](/docs/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

Для нашей конфигурации мы настраиваем следующие компоненты.

### Приёмники (Receivers)

В разделе `receivers` мы указываем стандартный приёмник `otlp` в качестве активного компонента приёма для нашего экземпляра Collector.

Это сделано в основном для демонстрационных целей. Здесь можно указать любой другой допустимый приёмник (например, `zipkin`).

### Процессоры (Processors)

В разделе `processors` мы указываем [процессор `resourcedetection`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/resourcedetectionprocessor) и настраиваем его с [детектором, специфичным для Dynatrace, `dynatrace`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/resourcedetectionprocessor/README.md#dynatrace).

При такой конфигурации процессор обнаружения ресурсов попытается загрузить следующие три атрибута из [файла обогащения OneAgent](/docs/ingest-from/extend-dynatrace/extend-data#dynatrace-oneagent "Узнайте, как автоматически обогатить ваши телеметрические данные полями, специфичными для Dynatrace."):

* `dt.entity.host`
* `host.name`
* `dt.smartscape.host`

Если детектор ресурсов успешно загрузил эти значения, он добавит их как атрибуты ресурса в запрос OTLP. Дополнительная настройка процессора не требуется.

### Экспортёры (Exporters)

В разделе `exporters` мы указываем стандартный [экспортёр `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) и настраиваем его с URL-адресом API Dynatrace и необходимым токеном аутентификации.

Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации для `endpoint` и `headers`.

* `DT_ENDPOINT` содержит [базовый URL конечной точки API Dynatrace](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [токен API](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Конвейер сервиса (Service pipeline)

В разделе `service` мы собираем наши объекты приёмника, процессора и экспортёра в конвейеры сервиса, которые будут выполнять следующие шаги:

* принимать OTLP-запросы на настроенных портах
* обогащать их данными хоста, релевантными для Dynatrace, с помощью процессора обнаружения ресурсов
* экспортировать обогащённые данные в Dynatrace
