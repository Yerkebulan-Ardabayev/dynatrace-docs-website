---
title: Группирование запросов OTLP с помощью OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/batch
scraped: 2026-05-12T12:10:54.176008
---

# Группирование запросов OTLP с помощью OTel Collector

# Группирование запросов OTLP с помощью OTel Collector

* Практическое руководство
* Чтение: 3 мин
* Опубликовано 11 октября 2023 г.

В следующем примере конфигурации показано, как настроить экземпляр Collector и его встроенный processor `batch` для постановки в очередь и группирования запросов OTLP и повышения производительности по пропускной способности.

Рекомендуемая конфигурация

Для оптимальной производительности вашего экземпляра Collector мы рекомендуем применять эту конфигурацию во всех установках.

Если вы используете другие processor, убедитесь, что processor `batch` настроен последним в вашем конвейере.

## Предварительные требования

* Один из следующих дистрибутивов Collector с [processor `batch`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/processor/batchprocessor):

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + Дистрибутив OpenTelemetry [Core](/managed/ingest-from/opentelemetry/collector#collector-core "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.") или [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
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

Проверка конфигурации

[Проверьте ваши настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

Для нашей конфигурации мы настраиваем следующие компоненты.

### Receivers

В разделе `receivers` мы указываем стандартный receiver `otlp` в качестве активного компонента receiver для нашего экземпляра Collector.

Это сделано в демонстрационных целях. Здесь можно указать любой другой допустимый receiver (например, `zipkin`).

### Processors

В разделе `processors` мы указываем отдельный [processor `batch`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/processor/batchprocessor)
для каждого сигнала телеметрии со следующими параметрами:

* `send_batch_size`: задаёт минимальное число записей, которые processor поставит в очередь перед отправкой всей группы.
* `send_batch_max_size`: задаёт максимальное число записей, которые может содержать группа. При большем числе записей группа разбивается на более мелкие.
* `timeout`: определяет длительность, по истечении которой группа будет отправлена. Группа отправляется по `timeout` только тогда, когда условие `send_batch_size` не достигнуто.

При такой конфигурации OTel Collector ставит записи телеметрии в очередь группами, обеспечивая хороший баланс между размером и числом запросов на экспорт
к Dynatrace API.

Значения размера группы

На итоговый размер группы влияет не только число отдельных записей телеметрии,
но и число связанных атрибутов и их размер.

Например, атрибуты на спанах/метриках/логах могут увеличить размер группы с тем же числом записей
в зависимости от того, сколько атрибутов и насколько они велики.

Используйте приведённые выше значения конфигурации как отправную точку, но обязательно адаптируйте их под ваш объём данных
и соблюдайте лимиты Dynatrace API для каждого типа сигнала ([трассировки](/managed/ingest-from/opentelemetry/otlp-api/ingest-traces#ingestion-limits "Узнайте, как Dynatrace принимает трассировки OpenTelemetry и какие ограничения применяются."),
[метрики](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#limits "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются."), [логи](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs#ingestion-limits "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения применяются.")), чтобы избежать отклонения запросов.

Для устранения проблем с отклонёнными запросами можно использовать [метрики самомониторинга ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-sfm-metrics#rest "Изучите метрики самомониторинга ActiveGate.").
Например, можно использовать: `dsfm:active_gate.rest.request_count` с фильтрацией по измерению `operation`
(`POST /otlp/v1/<...>` для приёма OTLP) и разбивкой по `response_code`. Большие запросы отклоняются с кодом состояния HTTP `413`.

Ещё один вариант: проверить логи Collector на наличие сообщений об ошибках, таких как: `HTTP Status Code 413, Message=Max Payload size of`.

### Exporters

В разделе `exporters` мы указываем стандартный [exporter `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) и настраиваем его с помощью URL нашего Dynatrace API и необходимого токена аутентификации.

Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Сервисные конвейеры

В разделе `service` мы собираем наши объекты receiver и exporter в конвейеры для трассировок, метрик и логов и включаем наш processor `batch`, ссылаясь на него в разделе `processors` для каждого соответствующего конвейера.

## Пределы и ограничения

Данные принимаются с помощью протокола OpenTelemetry (OTLP) через [Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") и подчиняются ограничениям и лимитам этого API.
Дополнительные сведения см.:

* [Ограничения метрик OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")
* [Сопоставление метрик Dynatrace](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")
* [Приём логов OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения применяются.")

## Связанные темы

* [Обогащение принимаемых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.")
* [Обогащение запросов OTLP данными Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Настройте OpenTelemetry Collector для обогащения запросов OTLP данными Kubernetes.")