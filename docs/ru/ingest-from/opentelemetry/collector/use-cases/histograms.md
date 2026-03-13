---
title: Compute histogram summaries with the OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/histograms
scraped: 2026-03-06T21:37:18.282146
---

# Вычисление сводных данных гистограмм с помощью OpenTelemetry Collector

# Вычисление сводных данных гистограмм с помощью OpenTelemetry Collector

* Последняя версия Dynatrace
* Практическое руководство
* Время чтения: 3 мин.
* Опубликовано 8 апреля 2024 г.

Прямая загрузка гистограмм

Начиная с версии Dynatrace 1.300, загрузка гистограмм поддерживается напрямую через API загрузки OTLP. Соответственно, использование Collector в качестве обходного решения больше не требуется. Dynatrace рекомендует загружать гистограммы напрямую без дополнительных манипуляций с данными.

Следующий пример конфигурации показывает, как использовать Collector для вычисления и загрузки сводных данных корзин гистограмм, таких как общая сумма всех значений в корзине и их количество.

## Предварительные требования

* Один из следующих дистрибутивов Collector с процессорами [transform](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/transformprocessor) и [filter](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/filterprocessor):

  + [Dynatrace Collector](../../collector.md#dt-collector-dist "Узнайте о дистрибутиве Dynatrace OTel Collector.")
  + OpenTelemetry [Contrib](../../collector.md#collector-contrib "Узнайте о дистрибутиве Dynatrace OTel Collector.")
  + [Пользовательская сборка Builder](../../collector.md#collector-builder "Узнайте о дистрибутиве Dynatrace OTel Collector.")
* [URL конечной точки API Dynatrace](../../otlp-api.md "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."), на который должны экспортироваться данные
* [API-токен](../../otlp-api.md#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate)

Информацию о развёртывании и настройке см. в разделах [Развёртывание Collector](../deployment.md "Развёртывание Dynatrace OTel Collector.") и [Настройка Collector](../configuration.md "Настройка OpenTelemetry Collector.").

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

[Проверьте ваши настройки](../configuration.md#validate "Настройка OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

Для нашей конфигурации мы настраиваем следующие компоненты.

### Приёмники

В разделе `receivers` мы указываем стандартный приёмник `otlp` в качестве активного компонента приёмника для нашего экземпляра Collector и настраиваем его на приём запросов OTLP по протоколам gRPC и HTTP.

### Процессоры

В разделе `processors` мы настраиваем два экземпляра процессоров:

* [`transform`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/transformprocessor) — для вычисления нужных значений суммы и количества из гистограмм:

  + Сначала мы используем функцию [`extract_count_metric`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/transformprocessor/README.md#extract_count_metric) для вычисления количества значений в каждой корзине гистограммы.
  + Затем мы используем функцию [`extract_sum_metric`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/transformprocessor/README.md#extract_sum_metric) для вычисления общей суммы всех значений и преобразования её в gauge с помощью [`convert_sum_to_gauge`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/transformprocessor/README.md#convert_sum_to_gauge).
* [`filter`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/filterprocessor) — для удаления существующих корзин гистограмм (на основе `type`) и предотвращения сообщений об ошибках, связанных с гистограммами.

С этой конфигурацией Collector удаляет метрики гистограмм и создаёт вместо них две новые метрики для суммы и количества элементов каждой соответствующей гистограммы.

### Экспортёры

В разделе `exporters` мы указываем стандартный [экспортёр `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) и настраиваем его с URL API Dynatrace и необходимым токеном аутентификации.

Для этого мы устанавливаем следующие две переменные окружения и ссылаемся на них в значениях конфигурации для `endpoint` и `Authorization`:

* `DT_ENDPOINT` содержит [базовый URL конечной точки API Dynatrace](../../otlp-api.md#export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [API-токен](../../otlp-api.md#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Конвейеры сервиса

В разделе `service` мы собираем наши объекты приёмника и экспортёра в конвейер метрик и включаем два процессора, указывая их в разделе `processors`.

## Ограничения и лимиты

Метрики загружаются по протоколу OpenTelemetry (OTLP) через [OTLP API Dynatrace](../../otlp-api.md "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") и подчиняются лимитам и ограничениям API.
Дополнительную информацию см. в разделах:

* [Ограничения метрик OpenTelemetry](../../otlp-api/ingest-otlp-metrics/about-metrics-ingest.md "Узнайте, как Dynatrace загружает метрики OpenTelemetry и какие ограничения применяются.")
* [Маппинг метрик Dynatrace](../../otlp-api/ingest-otlp-metrics/about-metrics-ingest.md#dynatrace-mapping "Узнайте, как Dynatrace загружает метрики OpenTelemetry и какие ограничения применяются.")

## Связанные темы

* [Обогащение загруженных данных полями, специфичными для Dynatrace](../../../extend-dynatrace/extend-data.md "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.")
