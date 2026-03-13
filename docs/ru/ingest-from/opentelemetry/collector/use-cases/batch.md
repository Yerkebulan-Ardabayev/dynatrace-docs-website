---
title: Batch OTLP requests with the OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/batch
scraped: 2026-03-06T21:31:54.689204
---

# Пакетная обработка OTLP-запросов с помощью OpenTelemetry Collector

# Пакетная обработка OTLP-запросов с помощью OpenTelemetry Collector

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Oct 11, 2023

Следующий пример конфигурации показывает, как настроить экземпляр Collector и его встроенный пакетный процессор для постановки в очередь и пакетной обработки OTLP-запросов с целью повышения пропускной способности.

Рекомендуемая конфигурация

Для оптимальной производительности вашего экземпляра Collector мы рекомендуем применять эту конфигурацию для всех установок.

Если вы используете другие процессоры, убедитесь, что пакетный процессор настроен последним в вашем конвейере.

## Предварительные требования

* Один из следующих дистрибутивов Collector с [пакетным процессором (batch processor)](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/processor/batchprocessor):

  + [Dynatrace Collector](../../collector.md#dt-collector-dist "Learn about the Dynatrace OTel Collector.")
  + Дистрибутив OpenTelemetry [Core](../../collector.md#collector-core "Learn about the Dynatrace OTel Collector.") или [Contrib](../../collector.md#collector-contrib "Learn about the Dynatrace OTel Collector.")
  + [Пользовательская версия Builder](../../collector.md#collector-builder "Learn about the Dynatrace OTel Collector.")
* [URL конечной точки API Dynatrace](../../otlp-api.md "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."), куда должны экспортироваться данные
* [API-токен](../../otlp-api.md#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate)

См. [Развёртывание Collector](../deployment.md "How to deploy Dynatrace OTel Collector.") и [Конфигурация Collector](../configuration.md "How to configure the OpenTelemetry Collector.") для настройки Collector с приведённой ниже конфигурацией.

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



batch/traces:



send_batch_size: 5000



send_batch_max_size: 5000



timeout: 60s



batch/metrics:



send_batch_size: 3000



send_batch_max_size: 3000



timeout: 60s



batch/logs:



send_batch_size: 1800



send_batch_max_size: 2000



timeout: 60s



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



traces:



receivers: [otlp]



processors: [batch/traces]



exporters: [otlp_http]



metrics:



receivers: [otlp]



processors: [batch/metrics]



exporters: [otlp_http]



logs:



receivers: [otlp]



processors: [batch/logs]



exporters: [otlp_http]
```

Валидация конфигурации

[Проверьте ваши настройки](../configuration.md#validate "How to configure the OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

Для нашей конфигурации мы настраиваем следующие компоненты.

### Приёмники (Receivers)

В разделе `receivers` мы указываем стандартный приёмник `otlp` в качестве активного компонента-приёмника для нашего экземпляра Collector.

Это сделано в демонстрационных целях. Вы можете указать здесь любой другой допустимый приёмник (например, `zipkin`).

### Процессоры (Processors)

В разделе `processors` мы указываем отдельный [пакетный процессор `batch`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/processor/batchprocessor)
для каждого сигнала телеметрии со следующими параметрами:

* `send_batch_size`: устанавливает минимальное количество записей, которое процессор будет накапливать перед отправкой всего пакета.
* `send_batch_max_size`: устанавливает максимальное количество записей, которое может содержать пакет. Если записей больше, пакет будет разделён на несколько меньших.
* `timeout`: определяет время, по истечении которого пакет будет отправлен. Пакет отправляется по таймауту только в том случае, если условие `send_batch_size` не достигнуто.

С этой конфигурацией Collector накапливает записи телеметрии в пакеты, обеспечивая хороший баланс между размером и количеством запросов экспорта
к API Dynatrace.

Значения размера пакета

На конечный размер пакета влияет не только количество отдельных записей телеметрии, но и количество связанных атрибутов и их размер.

Например, атрибуты на спанах/метриках/логах могут увеличить размер пакета с тем же количеством записей
в зависимости от того, сколько атрибутов и какого они размера.

Используйте приведённые выше значения конфигурации в качестве отправной точки, но обязательно адаптируйте их под ваш объём данных
и соответствие лимитам API Dynatrace для каждого типа сигнала ([трассировки](../../otlp-api/ingest-traces.md#ingestion-limits "Learn how Dynatrace ingests OpenTelemetry traces and what limitations apply."),
[метрики](../../otlp-api/ingest-otlp-metrics/about-metrics-ingest.md#limits "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply."), [логи](../../otlp-api/ingest-logs.md#ingestion-limits "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")), чтобы избежать отклонения запросов.

Вы можете использовать [метрики самомониторинга ActiveGate](../../../dynatrace-activegate/activegate-sfm-metrics.md#rest "Explore ActiveGate self-monitoring  metrics.")
для устранения неполадок с отклонёнными запросами. Например, вы можете использовать: `dsfm:active_gate.rest.request_count` с фильтрацией по измерению `operation`
(`POST /otlp/v1/<...>` для приёма OTLP) и разделением по `response_code`. Слишком большие запросы отклоняются с HTTP-кодом состояния `413`.

Другой вариант — проверка логов Collector на наличие сообщений об ошибках, таких как: `HTTP Status Code 413, Message=Max Payload size of`.

### Экспортёры (Exporters)

В разделе `exporters` мы указываем стандартный [экспортёр `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) и настраиваем его с URL нашего API Dynatrace и необходимым токеном аутентификации.

Для этого мы устанавливаем следующие две переменные окружения и ссылаемся на них в значениях конфигурации для `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL конечной точки API Dynatrace](../../otlp-api.md#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [API-токен](../../otlp-api.md#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Конвейеры сервиса (Service pipelines)

В разделе `service` мы собираем наши объекты приёмников и экспортёров в конвейеры для трассировок, метрик и логов и включаем наш пакетный процессор, ссылаясь на него в `processors` для каждого соответствующего конвейера.

## Лимиты и ограничения

Данные поступают с использованием протокола OpenTelemetry (OTLP) через [API Dynatrace OTLP](../../otlp-api.md "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") и подчиняются лимитам и ограничениям API.
Для получения дополнительной информации см.:

* [Ограничения метрик OpenTelemetry](../../otlp-api/ingest-otlp-metrics/about-metrics-ingest.md "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Сопоставление метрик Dynatrace](../../otlp-api/ingest-otlp-metrics/about-metrics-ingest.md#dynatrace-mapping "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Приём логов OpenTelemetry](../../otlp-api/ingest-logs.md "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")

## Связанные темы

* [Обогащение поступающих данных полями, специфичными для Dynatrace](../../../extend-dynatrace/extend-data.md "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")
* [Обогащение OTLP-запросов данными Kubernetes](kubernetes/k8s-enrich.md "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")