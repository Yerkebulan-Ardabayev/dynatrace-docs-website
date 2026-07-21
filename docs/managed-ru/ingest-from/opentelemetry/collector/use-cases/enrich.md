---
title: Обогащение OTLP данными OneAgent (без контейнеризации)
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/enrich
---

# Обогащение OTLP данными OneAgent (без контейнеризации)

# Обогащение OTLP данными OneAgent (без контейнеризации)

* Практическое руководство
* Чтение 2 минуты
* Обновлено 17 декабря 2025 г.

Следующий пример конфигурации показывает, как настроить экземпляр Collector для обогащения данных OpenTelemetry сущностями хостов OneAgent.

Обогащение используется для связывания данных OpenTelemetry с их хостом OneAgent и корректной ассоциации в модели топологии. Например, при приёме логов с разных хостов привязка сущности хоста к соответствующим данным логов позволяет запускать задачи аналитики логов на основе хоста.

Контейнерные среды

Обогащение специфично для неконтейнерных сред OneAgent. Настройка обогащения контейнеризированного Collector может привести к некорректным ассоциациям хостов и топологии.

## Предварительные требования

* Один из следующих дистрибутивов Collector с [Resource Detection processor﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/processor/resourcedetectionprocessor):

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + OpenTelemetry [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [Пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* OneAgent, запущенный на том же хосте, что и OTel Collector, где OneAgent работает в режиме Full-Stack, Infrastructure или Foundation & Discovery.
* [URL конечной точки Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."), в которую нужно экспортировать данные, настроенный как системная переменная окружения
* [Токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate), настроенный как системная переменная окружения

О том, как настроить Collector с приведённой ниже конфигурацией, см. в разделах [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.") и [Конфигурация Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector.").

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



resource_detection/dynatrace:



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



processors: [resource_detection/dynatrace]



exporters: [otlp_http]



metrics:



receivers: [otlp]



processors: [resource_detection/dynatrace]



exporters: [otlp_http]



logs:



receivers: [otlp]



processors: [resource_detection/dynatrace]



exporters: [otlp_http]
```

Проверка конфигурации

[Проверьте настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

В нашей конфигурации настроены следующие компоненты.

### Приёмники (Receivers)

В разделе `receivers` указан стандартный приёмник `otlp` в качестве активного компонента-приёмника для экземпляра Collector.

Это в основном для демонстрационных целей. Здесь можно указать любой другой допустимый приёмник (например, `zipkin`).

### Процессоры (Processors)

В разделе `processors` указан [процессор `resource_detection`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/processor/resourcedetectionprocessor) с настройкой [специфичного для Dynatrace детектора `dynatrace`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/processor/resourcedetectionprocessor/README.md#dynatrace).

При такой конфигурации процессор resource detector попытается загрузить следующие три атрибута из [файла обогащения OneAgent](/managed/ingest-from/extend-dynatrace/extend-data#dynatrace-oneagent "Узнайте, как автоматически обогащать данные телеметрии специфичными для Dynatrace полями."):

* `dt.entity.host`
* `host.name`
* `dt.smartscape.host`

Если resource detector смог успешно загрузить эти значения, он добавит их как атрибуты ресурса в запрос OTLP. Дополнительная настройка процессора не требуется.

### Экспортёры (Exporters)

В разделе `exporters` указан стандартный [экспортёр `otlp_http`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter) с настройкой на URL API Dynatrace и требуемый токен аутентификации.

Для этого задаются следующие две переменные окружения, на которые идёт ссылка в значениях конфигурации `endpoint` и `headers`.

* `DT_ENDPOINT` содержит [базовый URL конечной точки API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Конвейер сервиса (Service pipeline)

В разделе `service` объекты приёмника, процессора и экспортёра собираются в сервисные конвейеры, которые выполняют следующие шаги:

* принимают запросы OTLP на настроенных портах
* обогащают их релевантными данными хоста Dynatrace с помощью процессора resource detector
* и экспортируют обогащённые данные в Dynatrace