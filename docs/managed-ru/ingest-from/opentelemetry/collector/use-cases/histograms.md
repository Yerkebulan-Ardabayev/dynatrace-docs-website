---
title: Вычисление сводок гистограмм с помощью OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/histograms
scraped: 2026-05-12T12:10:42.304439
---

# Вычисление сводок гистограмм с помощью OTel Collector

# Вычисление сводок гистограмм с помощью OTel Collector

* Практическое руководство
* Чтение: 3 мин
* Опубликовано 08 апреля 2024 г.

На этой странице описывается, как принимать гистограммы с помощью OTel Collector, что может помочь сократить затраты, связанные с приёмом данных.

Можно также использовать OTLP ingest API для прямого приёма гистограмм без дополнительной обработки данных.

В следующем примере конфигурации показано, как использовать Collector для вычисления и приёма сводок по интервалам гистограмм, таких как общая сумма всех значений в интервале и их общий счётчик.

## Предварительные требования

* Один из следующих дистрибутивов Collector с processor [transform](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor) и [filter](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/filterprocessor):

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + OpenTelemetry [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* [URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."), на который должны экспортироваться данные
* [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate)

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

[Проверьте ваши настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

Для нашей конфигурации мы настраиваем следующие компоненты.

### Receivers

В разделе `receivers` мы указываем стандартный receiver `otlp` в качестве активного компонента receiver для нашего экземпляра Collector и настраиваем его на приём запросов OTLP по gRPC и HTTP.

### Processors

В разделе `processors` мы настраиваем следующие два экземпляра processor:

* [`transform`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor), чтобы вычислить нужные значения суммы и счётчика для гистограмм:

  + Сначала мы используем функцию [`extract_count_metric`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/processor/transformprocessor/README.md#extract_count_metric) для вычисления числа значений в каждом интервале гистограммы.
  + Затем мы используем функцию [`extract_sum_metric`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/processor/transformprocessor/README.md#extract_sum_metric) для вычисления общей суммы всех его значений и преобразуем её в gauge с помощью [`convert_sum_to_gauge`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/processor/transformprocessor/README.md#convert_sum_to_gauge).
* [`filter`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/filterprocessor), чтобы отбросить существующие интервалы гистограмм (на основе `type`) и избежать сообщений об ошибках, связанных с гистограммами.

При такой конфигурации Collector отбрасывает метрики-гистограммы и создаёт вместо них две новые метрики для суммы и счётчика элементов каждой соответствующей гистограммы.

### Exporters

В разделе `exporters` мы указываем стандартный [exporter `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) и настраиваем его с помощью URL нашего Dynatrace API и необходимого токена аутентификации.

Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `Authorization`:

* `DT_ENDPOINT` содержит [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Сервисные конвейеры

В разделе `service` мы собираем наши объекты receiver и exporter в конвейер метрик и включаем оба экземпляра processor, ссылаясь на них в разделе `processors`.

## Пределы и ограничения

Метрики принимаются с помощью протокола OpenTelemetry (OTLP) через [Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") и подчиняются ограничениям и лимитам этого API.
Дополнительные сведения см.:

* [Ограничения метрик OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")
* [Сопоставление метрик Dynatrace](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")

## Связанные темы

* [Обогащение принимаемых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.")