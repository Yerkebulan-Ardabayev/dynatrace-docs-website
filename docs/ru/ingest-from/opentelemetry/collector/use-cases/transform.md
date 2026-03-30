---
title: Преобразование и фильтрация данных с помощью OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/transform
scraped: 2026-03-06T21:35:50.810381
---

* Latest Dynatrace

Следующий пример конфигурации показывает, как настроить экземпляр Collector для преобразования и манипулирования OTLP-запросами перед их пересылкой в Dynatrace.

С помощью процессоров, показанных в этом примере (`filter` и `transform`), можно оптимизировать запросы перед отправкой в Dynatrace, исключить данные, возможно нерелевантные для вашего сценария использования, и снизить расходы на биллинг.

## Предварительные требования

* Один из следующих дистрибутивов Collector с процессорами [transform](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/transformprocessor) и [filter](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/filterprocessor)

  + [Dynatrace Collector](../../collector.md#dt-collector-dist "Узнайте о Dynatrace OTel Collector.")
  + OpenTelemetry [Contrib](../../collector.md#collector-contrib "Узнайте о Dynatrace OTel Collector.")
  + [Пользовательская сборка Builder](../../collector.md#collector-builder "Узнайте о Dynatrace OTel Collector.")
* [URL API](../../otlp-api.md#export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") вашей среды Dynatrace
* [API-токен](../../otlp-api.md#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа

Информацию о настройке вашего Collector с приведенной ниже конфигурацией см. в разделах Развертывание Collector и Конфигурация Collector.

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


trace_statements:


- context: resource


statements:


# Only keep a certain set of resource attributes


- keep_matching_keys(attributes, "^(aaa|bbb|ccc).*")


- context: span


statements:


# Only keep a certain set of span attributes


- keep_matching_keys(attributes, "(^xyz.pqr$)|(^(aaa|bbb|ccc).*)")


# Set a static key


- set(attributes["svc.marker"], "purchasing")


# Delete a specific key


- delete_key(attributes, "message")


# Rewrite a key


- set(attributes["purchase.id"], ConvertCase(attributes["purchase.id"], "upper"))


# Apply regex replacement


- replace_pattern(name, "^.*(DataSubmission-\d+).*$", "$$1")


metric_statements:


- context: metric


statements:


# Rename all metrics containing '_bad' suffix in their name with `_invalid`


- replace_pattern(name, "(.*)_bad$", "$${1}_invalid")


filter:


error_mode: ignore


traces:


span:


# Filter spans with resource attributes matching the provided regular expression


- IsMatch(resource.attributes["k8s.pod.name"], "^my-pod-name.*")


metrics:


metric:


# Filter metrics which contain at least one data point with a "bad.metric" attribute


- 'HasAttrKeyOnDatapoint("bad.metric")'


logs:


log_record:


# Filter logs with resource attributes matching the configured names


- resource.attributes["service.name"] == "service1"


- resource.attributes["service.name"] == "service2"


exporters:


otlp_http:


endpoint: ${env:DT_ENDPOINT}


headers:


Authorization: "Api-Token ${env:DT_API_TOKEN}"


service:


pipelines:


traces:


receivers: [otlp]


processors: [filter,transform]


exporters: [otlp_http]


metrics:


receivers: [otlp]


processors: [filter]


exporters: [otlp_http]


logs:


receivers: [otlp]


processors: [filter]


exporters: [otlp_http]
```

Валидация конфигурации

[Проверьте ваши настройки](../configuration.md#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

Для нашей конфигурации мы настраиваем следующие компоненты.

### Приемник

В разделе `receivers` мы указываем стандартный приемник `otlp` как активный компонент-приемник для нашего экземпляра Collector.

Это сделано в демонстрационных целях. Здесь вы можете указать любой другой допустимый приемник (например, `zipkin`).

### Процессор

#### Transform

В разделе `processors` мы указываем [процессор `transform`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/transformprocessor) с набором различных операторов модификации атрибутов. `context` указывает область, к которой должны применяться операторы (здесь `resource` для атрибутов ресурса, `span` для атрибутов спана и `metric` для метрик).

Подробнее об отдельных параметрах конфигурации см. в [документации OpenTelemetry по процессору transform](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/transformprocessor/README.md).

Приведенная выше примерная конфигурация использует следующие операторы:

#### Filter

Кроме того, мы также настраиваем экземпляр [процессора `filter`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/filterprocessor) для фильтрации сигналов по следующим критериям:

Подробнее об отдельных параметрах конфигурации см. в [документации OpenTelemetry по процессору filter](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/filterprocessor/README.md).

### Экспортер

В разделе `exporters` мы указываем стандартный [экспортер `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) и настраиваем его с URL API Dynatrace и необходимым токеном аутентификации.

Для этого мы устанавливаем следующие две переменные окружения и ссылаемся на них в значениях конфигурации для `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL конечной точки Dynatrace API](../../otlp-api.md#export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [API-токен](../../otlp-api.md#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Конвейер сервиса

В разделе `service` мы собираем наши объекты приемника, процессора и экспортера в конвейер трассировок, который принимает OTLP-трассировки на настроенных конечных точках и преобразует атрибуты трассировок в соответствии с настроенными правилами, прежде чем переслать все в Dynatrace с помощью экспортера.

## Ограничения

Данные принимаются с использованием протокола OpenTelemetry (OTLP) через Dynatrace OTLP API и подчиняются ограничениям и ограничениям API.
Дополнительную информацию см. в:

* Ограничения метрик OpenTelemetry
* [Маппинг метрик Dynatrace](../../otlp-api/ingest-otlp-metrics/about-metrics-ingest.md#dynatrace-mapping "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")
* Прием журналов OpenTelemetry

## Связанные темы

* Обогащение принимаемых данных полями, специфичными для Dynatrace
