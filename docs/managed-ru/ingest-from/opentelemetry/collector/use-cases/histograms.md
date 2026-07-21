---
title: Вычисление сводных данных гистограмм с помощью OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/histograms
---

# Вычисление сводных данных гистограмм с помощью OTel Collector

# Вычисление сводных данных гистограмм с помощью OTel Collector

* Практическое руководство
* Чтение за 3 минуты
* Опубликовано 08 апр. 2024 г.

На этой странице описано, как принимать гистограммы через OTel Collector, что помогает снизить затраты, связанные с приёмом данных.

Можно также использовать OTLP-приём API для приёма гистограмм напрямую, без дополнительной обработки данных.

Следующий пример конфигурации показывает, как использовать Collector для вычисления и приёма сводных данных по бакетам гистограммы, таких как общая сумма всех значений в бакете и их общее количество.

## Предварительные требования

* Один из следующих дистрибутивов Collector с процессорами [transform﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/transformprocessor) и [filter﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/filterprocessor):

  + [OTel Collector Dynatrace](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + OpenTelemetry [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [Пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* [URL конечной точки Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."), на которую должны экспортироваться данные
* [Токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") с необходимой областью доступа (требуется только для SaaS и ActiveGate)

Информацию о том, как настроить Collector с приведённой ниже конфигурацией, см. в разделах [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.") и [Конфигурация Collector](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.").

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



transform:



metric_statements:



- context: metric



statements:



# Get count from the histogram. The new metric name will be <histogram_name>_count



- extract_count_metric(true) where type == METRIC_DATA_TYPE_HISTOGRAM



# Get sum from the histogram. The new metric name will be <histogram_name>_sum



- extract_sum_metric(true) where type == METRIC_DATA_TYPE_HISTOGRAM



# convert the <histogram_name>_sum metrics to gauges.



- convert_sum_to_gauge() where IsMatch(name, ".*_sum")



filter:



metrics:



metric:



# Drop metrics of type histogram. The _count and _sum metrics will still be exported.



- type == METRIC_DATA_TYPE_HISTOGRAM



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



metrics:



receivers: [otlp]



processors: [transform,filter]



exporters: [otlp_http]
```

Проверка конфигурации

[Проверьте свои настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

Для нашей конфигурации настраиваются следующие компоненты.

### Receivers (приёмники)

В разделе `receivers` указывается стандартный приёмник `otlp` как активный компонент-приёмник для экземпляра Collector, и он настраивается на приём OTLP-запросов по gRPC и HTTP.

### Processors (процессоры)

В разделе `processors` настраиваются следующие два экземпляра процессоров:

* [`transform`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/transformprocessor), для вычисления нужных значений суммы и количества гистограмм:

  + Сначала используется функция [`extract_count_metric`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/processor/transformprocessor/README.md#extract_count_metric) для вычисления количества значений в каждом бакете гистограммы.
  + Затем используется функция [`extract_sum_metric`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/processor/transformprocessor/README.md#extract_sum_metric) для вычисления общей суммы всех её значений и преобразования её в gauge с помощью [`convert_sum_to_gauge`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/processor/transformprocessor/README.md#convert_sum_to_gauge).
* [`filter`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/filterprocessor), для отбрасывания существующих бакетов гистограммы (на основе `type`) и предотвращения сообщений об ошибках, связанных с гистограммами.

При такой конфигурации Collector отбрасывает метрики гистограмм и создаёт вместо них две новые метрики: сумму и количество элементов для каждой соответствующей гистограммы.

### Exporters (экспортёры)

В разделе `exporters` указывается стандартный [экспортёр `otlp_http`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter), и он настраивается с URL API Dynatrace и необходимым токеном аутентификации.

Для этого задаются следующие две переменные окружения, на которые есть ссылки в значениях конфигурации для `endpoint` и `Authorization`:

* `DT_ENDPOINT` содержит [базовый URL конечной точки API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Пайплайны служб

В разделе `service` объекты receiver и exporter объединяются в пайплайн метрик, и оба процессора включаются путём ссылки на них в разделе `processors`.

## Ограничения

Метрики принимаются с использованием протокола OpenTelemetry (OTLP) через [OTLP API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") и подчиняются ограничениям и лимитам API.
Подробнее см.:

* [Ограничения метрик OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Сопоставление метрик Dynatrace](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")

## Связанные темы

* [Обогащение принятых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")