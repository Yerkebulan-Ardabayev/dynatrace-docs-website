---
title: Маскирование конфиденциальных данных с помощью OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/redact
scraped: 2026-05-12T11:08:54.703064
---

# Маскирование конфиденциальных данных с помощью OTel Collector

# Маскирование конфиденциальных данных с помощью OTel Collector

* Практическое руководство
* Чтение: 5 мин
* Обновлено 12 января 2026 г.

Данные телеметрии нередко содержат конфиденциальные данные (например, [PII](https://en.wikipedia.org/wiki/Personal_data)), которые может потребоваться маскировать по соображениям безопасности и нормативным требованиям. Хотя это можно реализовать на стороне приложения, обычно лучше выполнять это централизованно с помощью шлюзов, таких как OTel Collector. Это обеспечивает управление правилами маскирования из единой точки во всех ваших приложениях и сервисах, без необходимости обновлять код каждый раз, когда требуется новое правило маскирования.

На этой странице показаны примеры конфигураций Collector для маскирования конкретных конфиденциальных данных (например, номеров кредитных карт или адресов электронной почты), которые могут появиться в данных телеметрии и которые следует маскировать перед выходом из вашей сети.

## Предварительные требования

* Один из следующих дистрибутивов Collector с processor [transform](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor) и/или [redaction](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/redactionprocessor):

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* [URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."), на который должны экспортироваться данные
* [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate)

См. [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.") и [Настройку Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector."), чтобы узнать, как настроить ваш Collector с приведённой ниже конфигурацией.

## Processor redaction в сравнении с processor transform

В следующих примерах используются эти два [processor](https://opentelemetry.io/docs/collector/architecture/#processors) Collector:

* processor [transform](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/processor/transformprocessor/README.md)
* processor [redaction](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/processor/redactionprocessor/README.md)

Хотя в следующих примерах для маскирования данных используются оба компонента processor, у каждого из них своё назначение. Processor redaction прост: он принимает список значений, на основе которых совпадающие данные будут полностью замаскированы. Назначение же processor transform более универсально и выходит за рамки простого маскирования данных.

Для маскирования данных обычно можно использовать любой из двух компонентов processor, и стоит выбрать тот, который лучше подходит для вашего сценария использования. Например, для полного маскирования данных processor redaction может быть проще в использовании. С другой стороны, частичное маскирование данных можно реализовать только с помощью processor transform. Кроме того, processor transform может также фильтровать по данным в теле логов, тогда как processor redaction имеет доступ только к атрибутам.

## Ограничения и замечания

Приведённые на этой странице примеры демонстрируют распространённые сценарии маскирования. Обратите внимание на следующее:

* Примеры могут не охватывать все сценарии использования. Возможно, потребуется адаптировать их под ваши конкретные требования.
* Шаблоны regex и сопоставление атрибутов работают только тогда, когда всё значение атрибута соответствует шаблону для маскирования. Для частичных совпадений внутри более длинных строк могут потребоваться более сложные шаблоны или дополнительная обработка.
* Имя спана хранится в структуре сообщения OTLP как отдельное поле, а не как атрибут. Поэтому processor redaction, нацеленные на атрибуты, по умолчанию не влияют на имена спанов. О том, как с этим работать, см. пример [Имена спанов](#span-names).
* Порядок processor в конвейерах имеет значение. Применяйте transform/redaction до маршрутизации или экспорта и держите связанные processor рядом, чтобы последующие шаги видели очищенные данные.

## Демонстрационная конфигурация

Этот документ YAML представляет собой базовый каркас конфигурации Collector, содержащий основные общие компоненты (то есть receivers, exporters и определение конвейера).

```
receivers:



otlp:



protocols:



grpc:



endpoint: 0.0.0.0:4317



http:



endpoint: 0.0.0.0:4318



processors:



PLACEHOLDER-FOR-PROCESSOR-CONFIGURATIONS



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



"Authorization": "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



traces:



receivers: [otlp]



processors: [PLACEHOLDER-FOR-PROCESSOR-REFERENCES]



exporters: [otlp_http]



metrics:



receivers: [otlp]



processors: [PLACEHOLDER-FOR-PROCESSOR-REFERENCES]



exporters: [otlp_http]



logs:



receivers: [otlp]



processors: [PLACEHOLDER-FOR-PROCESSOR-REFERENCES]



exporters: [otlp_http]
```

Обязательно замените значения-заполнители в документе соответствующими конфигурациями:

* `PLACEHOLDER-FOR-PROCESSOR-CONFIGURATIONS`: соответствующая конфигурация processor
* `PLACEHOLDER-FOR-PROCESSOR-REFERENCES`: ссылки на применимые объекты processor для отдельных типов сигналов

### IP-адреса

С помощью processor transform мы маскируем атрибут `client.address` с помощью [инструкции `set`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/ottl/ottlfuncs/README.md#set).

```
transform:



error_mode: ignore



trace_statements:



- context: span



statements: &filter-statements



# this will not only mask end user client IP addresses,



# but also the address of a server acting as a client when establishing a connection to another server



- set(attributes["client.address"], "<masked-clientip-ot>")



metric_statements:



- context: datapoint



statements: *filter-statements



log_statements:



- context: log



statements: *filter-statements
```

### Адреса электронной почты

С помощью processor transform мы маскируем атрибут `user.email` с помощью [инструкции `set`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/ottl/ottlfuncs/README.md#set).

```
transform:



error_mode: ignore



trace_statements:



- context: span



statements: &filter-statements



- set(attributes["user.email"], "<masked-email-ot>")



metric_statements:



- context: datapoint



statements: *filter-statements



log_statements:



- context: log



statements: *filter-statements
```

### API-токены Dynatrace

С помощью processor redaction мы используем регулярное выражение `dt0[a-z]0[1-9]\.[A-Za-z0-9]{24}\.([A-Za-z0-9]{64})`, чтобы замаскировать все вхождения [API-токенов Dynatrace](/managed/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как пройти аутентификацию для использования Dynatrace API.") в наших данных телеметрии.

```
redaction:



allow_all_keys: true



blocked_values:



- dt0[a-z]0[1-9]\.[A-Za-z0-9]{24}\.([A-Za-z0-9]{64})



summary: info
```

### Имена пользователей

С помощью processor transform мы маскируем атрибуты `user.id`, `user.name` и `user.full_name` с помощью [инструкции `set`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/ottl/ottlfuncs/README.md#set).

```
transform:



error_mode: ignore



trace_statements:



- context: span



statements: &filter-statements



- set(attributes["user.id"], "<masked-userid-ot>")



- set(attributes["user.name"], "<masked-username-ot>")



- set(attributes["user.full_name"], "<masked-userfullname-ot>")



metric_statements:



- context: datapoint



statements: *filter-statements



log_statements:



- context: log



statements: *filter-statements
```

### Номера кредитных карт

С помощью processor transform мы настраиваем три [инструкции `replace_all_patterns`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/ottl/ottlfuncs/README.md#replace_all_patterns), чтобы замаскировать любые вхождения номеров кредитных карт, скрывая все цифры, кроме последних четырёх.

```
transform:



error_mode: ignore



trace_statements:



- context: span



statements: &filter-statements



- replace_all_patterns(attributes, "value", "^3\\s*[47](\\s*[0-9]){9}((\\s*[0-9]){4})$", "<masked-pcard$$2-ot>") where IsValidLuhn(attributes["value"])



- replace_all_patterns(attributes, "value", "^(5[1-5]([0-9]){2}|222[1-9]|22[3-9]\\d|2[3-6]\\d{2}|27[0-1]\\d|2720)(\\s*[0-9]){8}\\s*([0-9]{4})$", "<masked-pcard$$4-ot>") where IsValidLuhn(attributes["value"])



- replace_all_patterns(attributes, "value", "^4(\\s*[0-9]){8,14}\\s*(([0-9]\\s*){4})$", "<masked-pcard$$2-ot>") where IsValidLuhn(attributes["value"])



metric_statements:



- context: datapoint



statements: *filter-statements



log_statements:



- context: log



statements: *filter-statements
```

Для номеров кредитных карт вместо регулярных выражений можно также использовать встроенную [стандартную функцию OTTL `IsValidLuhn()`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/pkg/ottl/ottlfuncs#isvalidluhn), если вы предпочитаете полностью блокировать значения, а не просто маскировать их.

### Номера IBAN

С помощью processor redaction мы используем регулярное выражение `^[A-Z]{2}[0-9]{2}(\\s*[A-Z0-9]){8,30}$`, чтобы замаскировать все вхождения IBAN в наших данных телеметрии.

```
redaction:



allow_all_keys: true



blocked_values:



- "^[A-Z]{2}[0-9]{2}(\\s*[A-Z0-9]){8,30}$"



summary: info
```

### Имена спанов

Имена спанов не хранятся в структуре сообщения OTLP как атрибуты, поэтому маскирование на основе атрибутов к ним не применяется.
Есть несколько способов маскировать и упростить имена спанов:

#### Создание нового имени спана

Рекомендуется

`set_semconv_span_name` доступна начиная с версии Collector Contrib 0.142.0 и версии Dynatrace Collector 0.42.0.

Используйте функцию processor transform [`set_semconv_span_name`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor#set_semconv_span_name), чтобы получить имя с низкой кардинальностью, соответствующее семантическим соглашениям OpenTelemetry. Для создания нового имени спана будут использоваться (низкокардинальные) `http.request.method` и `http.route`. Это сохраняет имя согласованным с соглашениями HTTP/RPC/messaging/database и предотвращает утечку идентификаторов.

```
transform:



error_mode: ignore



trace_statements:



- context: span



statements:



- set_semconv_span_name("1.37.0")
```

#### Явное маскирование имени спана

```
transform:



error_mode: ignore



trace_statements:



- context: span



statements:



- replace_pattern(name, "(GET /api/v1/users/)\\d+", "$$1{id}")
```

Проверка конфигурации

[Проверьте ваши настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

Для нашей конфигурации мы используем следующие компоненты.

### Receivers

В разделе `receivers` мы указываем стандартный receiver `otlp` в качестве активного компонента receiver для нашего экземпляра Collector.

### Processors

В разделе `processors` мы размещаем конфигурацию для соответствующих экземпляров processor.

### Exporters

В разделе `exporters` мы указываем стандартный [exporter `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) и настраиваем его с помощью URL нашего Dynatrace API и необходимого токена аутентификации.

Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Сервисные конвейеры

В разделе `service` мы в итоге собираем все настроенные объекты в конвейеры для отдельных сигналов телеметрии (трассировки и т. д.) и заставляем экземпляр Collector выполнять настроенные задачи.

## Связанные темы

* [Обогащение принимаемых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.")