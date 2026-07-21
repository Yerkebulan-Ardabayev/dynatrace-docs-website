---
title: Преобразование и фильтрация данных с помощью OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/transform
---

# Преобразование и фильтрация данных с помощью OTel Collector

# Преобразование и фильтрация данных с помощью OTel Collector

* Практическое руководство
* 4 минуты чтения
* Опубликовано 19 авг. 2024 г.

Следующий пример конфигурации показывает, как настроить экземпляр Collector для преобразования и обработки OTLP-запросов перед их отправкой в Dynatrace.

Используя процессоры, показанные в этом примере (`filter` и `transform`), можно упорядочить запросы перед отправкой в Dynatrace и исключить данные, которые могут быть нерелевантны для конкретной задачи, а также снизить затраты на биллинг.

## Предварительные требования

* Один из следующих дистрибутивов Collector с процессорами [transform﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/transformprocessor) и [filter﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/filterprocessor)

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + OpenTelemetry [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* [URL API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.") окружения Dynatrace
* [Токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа

О том, как настроить Collector с приведённой ниже конфигурацией, см. [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.") и [Конфигурация Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector.").

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

[Проверьте настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

В нашей конфигурации настроены следующие компоненты.

### Receiver

В разделе `receivers` указан стандартный ресивер `otlp` в качестве активного компонента-ресивера для нашего экземпляра Collector.

Это сделано в демонстрационных целях. Здесь можно указать любой другой допустимый ресивер (например, `zipkin`).

### Processor

#### Transform

В разделе `processors` указан [процессор `transform`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/transformprocessor) с набором различных инструкций по изменению атрибутов. `context` указывает область, к которой должны применяться инструкции (здесь: `resource` для атрибутов ресурса, `span` для атрибутов спана и `metric` для метрик).

Подробнее об отдельных параметрах конфигурации см. в [документации OpenTelemetry по процессору transform﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/processor/transformprocessor/README.md).

В приведённом выше примере конфигурации используются следующие инструкции:

| Инструкция | Описание |
| --- | --- |
| [`keep_matching_keys`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/pkg/ottl/ottlfuncs/README.md#keep_matching_keys) | Оценивает имена ключей атрибутов и оставляет только те, чьи имена соответствуют заданным регулярным выражениям: `^(aaa|bbb|ccc).*` для атрибутов ресурса и `(^xyz.pqr$)|(^(aaa|bbb|ccc).*)` для атрибутов спана. |
| [`set`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/pkg/ottl/ottlfuncs/README.md#set) | Добавляет/изменяет следующие два атрибута спана:  * `svc.marker`, со статическим значением `purchasing` * `purchase.id`, преобразуя его значение в верхний регистр с помощью [`ConvertCase`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/pkg/ottl/ottlfuncs/README.md#convertcase) |
| [`delete_key`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/pkg/ottl/ottlfuncs/README.md#delete_key) | Удаляет атрибуты с именем `message`. |
| [`replace_pattern`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/pkg/ottl/ottlfuncs/README.md#replace_pattern) | Сопоставляет строку с заданным регулярным выражением и выполняет замену строки во всех совпадающих записях.  В нашем примере мы сначала используем это для трасс, чтобы сопоставить имя с регулярным выражением `^.*(DataSubmission-\d+).*$` и заменить его содержимое первой захваченной группой (`$$1`) нашего выражения. По сути, это означает, что мы ищем в строках `DataSubmission` с числовым суффиксом и, если находим, оставляем только значение найденного совпадения.  Мы также используем эту функцию для метрик с регулярным выражением `(.*)_bad$`, чтобы изменить суффикс `_bad` на `_invalid`. |

#### Filter

Кроме того, настроен экземпляр [процессора `filter`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/filterprocessor) для фильтрации сигналов по следующим критериям:

| Сигнал | Описание |
| --- | --- |
| Traces | Использует [`IsMatch`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/pkg/ottl/ottlfuncs/README.md#ismatch) для сопоставления имени атрибутов ресурса с регулярным выражением `^my-pod-name.*`, отбрасывая спаны с атрибутами, чьи имена начинаются с `my-pod-name`. |
| Metrics | Использует [`HasAttrKeyOnDatapoint`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/processor/filterprocessor/README.md#HasAttrKeyOnDatapoint) для проверки, есть ли у точек данных атрибуты с именем `bad.metric`. |
| Logs | Использует строгое сопоставление строк атрибута ресурса `service.name` со строками `service1` и `service2`. |

Подробнее об отдельных параметрах конфигурации см. в [документации OpenTelemetry по процессору filter﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/processor/filterprocessor/README.md).

### Exporter

В разделе `exporters` указан стандартный [экспортёр `otlp_http`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter), настроенный с URL API Dynatrace и необходимым токеном авторизации.

Для этого заданы следующие две переменные окружения, на которые есть ссылки в значениях конфигурации для `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL эндпоинта API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Service pipeline

В разделе `service` собраны объекты ресивера, процессора и экспортёра в конвейер (pipeline) для трасс, который принимает трассы OTLP на настроенных эндпоинтах, преобразует атрибуты трасс согласно заданным правилам и затем пересылает всё в Dynatrace с помощью экспортёра.

## Ограничения

Данные принимаются с помощью протокола OpenTelemetry (OTLP) через [эндпоинты Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") и подчиняются ограничениям и лимитам API.
Подробнее см.:

* [Ограничения метрик OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Сопоставление метрик Dynatrace](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Прием логов OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")

## Смежные темы

* [Обогащение принятых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")