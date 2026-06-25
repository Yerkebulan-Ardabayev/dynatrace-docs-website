---
title: Преобразование и фильтрация данных с помощью OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/transform
scraped: 2026-05-12T12:11:02.090951
---

# Преобразование и фильтрация данных с помощью OTel Collector

# Преобразование и фильтрация данных с помощью OTel Collector

* Практическое руководство
* Чтение: 4 мин
* Опубликовано 19 августа 2024 г.

В следующем примере конфигурации показано, как настроить экземпляр Collector для преобразования OTLP-запросов и манипуляций с ними перед их пересылкой в Dynatrace.

С помощью processor, показанных в этом примере (`filter` и `transform`), можно упорядочить запросы перед их отправкой в Dynatrace, опустить данные, возможно нерелевантные для вашего сценария использования, и сократить расходы на биллинг.

## Предварительные требования

* Один из следующих дистрибутивов Collector с processor [transform](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor) и [filter](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/filterprocessor)

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + OpenTelemetry [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* [URL API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") вашей среды Dynatrace
* [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа

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

Проверка конфигурации

[Проверьте ваши настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

Для нашей конфигурации мы настраиваем следующие компоненты.

### Receiver

В разделе `receivers` мы указываем стандартный receiver `otlp` в качестве активного компонента receiver для нашего экземпляра Collector.

Это сделано в демонстрационных целях. Здесь можно указать любой другой допустимый receiver (например, `zipkin`).

### Processor

#### Transform

В разделе `processors` мы указываем [processor `transform`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor) с набором различных инструкций изменения атрибутов. `context` указывает область, к которой должны применяться инструкции (здесь `resource` для атрибутов ресурса, `span` для атрибутов спана и `metric` для метрик).

Подробнее об отдельных параметрах конфигурации см. в [документации OpenTelemetry по processor transform](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/processor/transformprocessor/README.md).

В приведённой выше примерной конфигурации используются следующие инструкции:

| Инструкция | Описание |
| --- | --- |
| [`keep_matching_keys`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/ottl/ottlfuncs/README.md#keep_matching_keys) | Оценивает имена ключей атрибутов и сохраняет только те, чьи имена соответствуют заданным регулярным выражениям `^(aaa|bbb|ccc).*` для атрибутов ресурса и `(^xyz.pqr$)|(^(aaa|bbb|ccc).*)` для атрибутов спана. |
| [`set`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/ottl/ottlfuncs/README.md#set) | Добавляет/изменяет следующие два атрибута спана:  * `svc.marker` со статическим значением `purchasing` * `purchase.id`, преобразуя его значение в верхний регистр с помощью [`ConvertCase`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/ottl/ottlfuncs/README.md#convertcase) |
| [`delete_key`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/ottl/ottlfuncs/README.md#delete_key) | Удаляет атрибуты с именем `message`. |
| [`replace_pattern`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/ottl/ottlfuncs/README.md#replace_pattern) | Сопоставляет строку с заданным регулярным выражением и выполняет подстановку строки для всех совпадающих записей.  В нашем примере мы сначала используем её для трассировок, чтобы сопоставить имя с регулярным выражением `^.*(DataSubmission-\d+).*$` и заменить его содержимое первой группой захвата (`$$1`) нашего выражения. По сути это означает, что мы ищем в строках `DataSubmission` с последующим числом и, если оно найдено, сохраняем только значение найденного совпадения.  Мы также используем эту функцию для метрик с регулярным выражением `(.*)_bad$`, чтобы изменить суффикс `_bad` на `_invalid`. |

#### Filter

Кроме того, мы также настраиваем экземпляр [processor `filter`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/filterprocessor) для фильтрации сигнала по следующим критериям:

| Сигнал | Описание |
| --- | --- |
| Traces | Использует [`IsMatch`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/ottl/ottlfuncs/README.md#ismatch) для сопоставления имени атрибутов ресурса с регулярным выражением `^my-pod-name.*`, отбрасывая спаны с атрибутами, имена которых начинаются с `my-pod-name`. |
| Metrics | Использует [`HasAttrKeyOnDatapoint`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/processor/filterprocessor/README.md#HasAttrKeyOnDatapoint) для оценки того, есть ли у точек данных атрибуты с именем `bad.metric`. |
| Logs | Использует строгое строковое сопоставление атрибута ресурса `service.name` со строками `service1` и `service2`. |

Подробнее об отдельных параметрах конфигурации см. в [документации OpenTelemetry по processor filter](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/processor/filterprocessor/README.md).

### Exporter

В разделе `exporters` мы указываем стандартный [exporter `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) и настраиваем его с помощью URL нашего Dynatrace API и необходимого токена аутентификации.

Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Сервисный конвейер

В разделе `service` мы собираем наши объекты receiver, processor и exporter в конвейер трассировок, который принимает трассировки OTLP на настроенных эндпоинтах и преобразует атрибуты трассировок согласно настроенным правилам перед пересылкой всего в Dynatrace с помощью exporter.

## Пределы и ограничения

Данные принимаются с помощью протокола OpenTelemetry (OTLP) через [Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") и подчиняются ограничениям и лимитам этого API.
Дополнительные сведения см.:

* [Ограничения метрик OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")
* [Сопоставление метрик Dynatrace](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")
* [Приём логов OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения применяются.")

## Связанные темы

* [Обогащение принимаемых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.")