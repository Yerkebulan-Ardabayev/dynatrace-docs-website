---
title: Применение ограничений памяти к OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/memory
---

# Применение ограничений памяти к OTel Collector

# Применение ограничений памяти к OTel Collector

* Практическое руководство
* Чтение: 2 мин
* Обновлено 08 января 2026 г.

Следующий пример конфигурации показывает, как настроить экземпляр Collector и его встроенный процессор ограничителя памяти, чтобы гарантировать выделение памяти в рамках указанных параметров.

Рекомендуемая конфигурация

Для оптимального использования памяти с экземпляром Collector рекомендуется
применять эту конфигурацию для большинства контейнеризированных сред. Подробнее
см. раздел [соображения по развёртыванию](#deployment-considerations).

## Предварительные требования

* Один из следующих дистрибутивов Collector с [процессором ограничителя памяти﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/processor/memorylimiterprocessor):

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + OpenTelemetry [Core](/managed/ingest-from/opentelemetry/collector#collector-core "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.") или [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [Собственная версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* [URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."), на который нужно экспортировать данные
* [Токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate)

О том, как настроить Collector с приведённой ниже конфигурацией, см. [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.") и [Конфигурация Collector](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.").

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



memory_limiter:



check_interval: 1s



limit_percentage: 90



spike_limit_percentage: 20



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



traces:



receivers: [otlp]



processors: [memory_limiter]



exporters: [otlp_http]



metrics:



receivers: [otlp]



processors: [memory_limiter]



exporters: [otlp_http]



logs:



receivers: [otlp]



processors: [memory_limiter]



exporters: [otlp_http]
```

Проверка конфигурации

[Проверьте свои настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

В нашей конфигурации настроены следующие компоненты.

### Receivers

В разделе `receivers` указан стандартный ресивер `otlp` как активный компонент-ресивер для экземпляра Collector.

Это в основном для демонстрационных целей. Здесь можно указать любой другой допустимый ресивер (например, `zipkin`).

### Processors

В разделе `processors` указан [процессор `memory_limiter`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/processor/memorylimiterprocessor) со следующими параметрами:

* `check_interval` настроен на проверку состояния памяти каждую секунду
* `limit_percentage` настроен на допустимое максимальное выделение памяти в 90 процентов
* `spike_limit_percentage` настроен на допустимое максимальное всплесковое использование памяти в 20 процентов

При такой конфигурации OTel Collector проверяет выделение памяти каждую секунду
и начинает применять давление с помощью отдельных механизмов после достижения
следующих пределов:

* Мягкий предел (`limit_percentage - spike_limit_percentage`): после достижения
  этого предела процессор отклоняет полезные нагрузки, пока использование памяти
  не окажется ниже предела. Отправка правильных сообщений об отклонении
  ложится на ресивер, находящийся выше по потоку от процессора.
* Жёсткий предел (`limit_percentage`): после достижения этого предела процессор
  будет принудительно запускать сборку мусора, пока использование памяти
  не окажется ниже предела. Данные продолжат отклоняться, пока использование
  не окажется ниже мягкого предела.

Помимо процессора ограничителя памяти, настоятельно рекомендуется установить
переменную среды `GOMEMLIMIT` в значение, равное 80% от жёсткого предела.
Обратите внимание, что для `GOMEMLIMIT` нужно указывать абсолютное значение
в байтах. Например, можно установить `GOMEMLIMIT=1024MiB`, чтобы начать
увеличивать частоту циклов сборки мусора, как только Collector достигнет
1024 МиБ использованной памяти в куче Go VM. Подробнее см. [документацию
пакета Go﻿](https://pkg.go.dev/runtime#hdr-Environment_Variables), описывающую
работу этой переменной среды.

#### Соображения по развёртыванию

В контейнеризированных средах или других местах, где хостовая среда
устанавливает максимально допустимый объём памяти для Collector, рекомендуется
использовать параметры `limit_percentage` и `spike_limit_percentage`.

Для развёртываний на виртуальных машинах или физическом оборудовании, где
Collector не получает явную квоту памяти, вместо этого рекомендуется
использовать параметры `limit_mib` и `spike_limit_mib`.

### Exporters

В разделе `exporters` указан стандартный [экспортер `otlp_http`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter), настроенный с URL Dynatrace API и необходимым токеном аутентификации.

Для этого задаются следующие две переменные среды, на которые есть ссылки в значениях конфигурации для `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Сервисные пайплайны

В разделе `service` объекты ресивера и экспортера собираются в пайплайны для трейсов, метрик и логов, и процессор ограничителя памяти включается путём указания на него в `processors` для каждого соответствующего пайплайна.

## Пределы и ограничения

Данные принимаются с использованием протокола OpenTelemetry (OTLP) через [эндпоинты OTLP Dynatrace](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") и подчиняются пределам и ограничениям API.
Подробнее см.:

* [Ограничения метрик OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Сопоставление метрик Dynatrace](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Приём логов OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")

## Связанные темы

* [Обогащение принятых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")
* [Обогащение запросов OTLP данными Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")