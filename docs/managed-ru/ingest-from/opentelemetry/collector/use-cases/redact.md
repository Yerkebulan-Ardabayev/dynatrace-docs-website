---
title: Маскирование чувствительных данных с помощью OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/redact
---

# Маскирование чувствительных данных с помощью OTel Collector

# Маскирование чувствительных данных с помощью OTel Collector

* Практическое руководство
* Чтение 5 минут
* Обновлено 12 января 2026 г.

Телеметрические данные часто содержат чувствительные данные (например, [PII﻿](https://en.wikipedia.org/wiki/Personal_data)), которые нужно маскировать по соображениям безопасности и регуляторным требованиям. Это можно реализовать на стороне приложения, но обычно лучше обрабатывать это централизованно с помощью шлюзов, таких как OTel Collector. Это даёт возможность управлять правилами маскирования из одной точки для всех приложений и сервисов, без необходимости обновлять код каждый раз, когда требуется новое правило маскирования.

На этой странице приведены примеры конфигураций Collector для маскирования конкретных чувствительных данных (например, номеров кредитных карт или email-адресов), которые могут появляться в телеметрических данных и которые нужно замаскировать до того, как они покинут сеть.

## Предварительные требования

* Один из следующих дистрибутивов Collector с процессорами [transform﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/transformprocessor) и/или [redaction﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/redactionprocessor):

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [Пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* [URL конечной точки Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте о конечных точках OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.") для экспорта данных
* [Токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с необходимой областью доступа (требуется только для SaaS и ActiveGate)

О том, как настроить Collector с приведённой ниже конфигурацией, см. в разделах [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.") и [Конфигурация Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector.").

## Процессор redaction против процессора transform

В следующих примерах используются эти два процессора Collector [﻿](https://opentelemetry.io/docs/collector/architecture/#processors):

* [процессор transform﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/processor/transformprocessor/README.md)
* [процессор redaction﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/processor/redactionprocessor/README.md)

В следующих примерах оба процессора используются для маскирования данных, но у каждого своё назначение. Процессор redaction прост в использовании и принимает список значений, на основе которого совпадающие данные полностью маскируются. Процессор transform, в свою очередь, более универсален и предназначен не только для маскирования данных.

Для маскирования данных обычно можно использовать любой из процессоров, и стоит выбрать тот, который лучше подходит под конкретный случай. Например, для полного маскирования данных проще использовать процессор redaction. С другой стороны, частичное маскирование данных можно реализовать только с помощью процессора transform. Кроме того, процессор transform может фильтровать по данным в теле логов, тогда как процессор redaction имеет доступ только к атрибутам.

## Ограничения и особенности

Примеры, приведённые на этой странице, демонстрируют типичные сценарии маскирования. Обратите внимание на следующее:

* Примеры могут не охватывать все случаи использования. Их может потребоваться адаптировать под конкретные требования.
* Регулярные выражения и сопоставление атрибутов работают только тогда, когда значение атрибута целиком совпадает с маскируемым шаблоном. Частичные совпадения внутри более длинных строк могут потребовать более сложных шаблонов или дополнительной обработки.
* Имя спана хранится как отдельное поле в структуре сообщения OTLP, а не как атрибут. Поэтому процессоры redaction, нацеленные на атрибуты, по умолчанию не влияют на имена спанов. Как это обработать, см. в примере [Имена спанов](#span-names).
* Порядок процессоров в пайплайнах имеет значение. Применяйте transform/redaction до маршрутизации или экспорта и держите связанные процессоры рядом, чтобы последующие шаги видели уже очищенные данные.

## Демонстрационная конфигурация

Этот документ YAML представляет собой базовый скелет конфигурации Collector, содержащий базовые общие компоненты (то есть receivers, exporters и определение пайплайна).

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

* `PLACEHOLDER-FOR-PROCESSOR-CONFIGURATIONS`: соответствующая конфигурация процессора
* `PLACEHOLDER-FOR-PROCESSOR-REFERENCES`: ссылка на применимые объекты процессоров для отдельных типов сигналов

### IP-адреса

С помощью процессора transform маскируем атрибут `client.address` с помощью [оператора `set`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/pkg/ottl/ottlfuncs/README.md#set).

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

### Email-адреса

С помощью процессора transform маскируем атрибут `user.email` с помощью [оператора `set`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/pkg/ottl/ottlfuncs/README.md#set).

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

### Токены Dynatrace API

С помощью процессора redaction используем регулярное выражение `dt0[a-z]0[1-9]\.[A-Za-z0-9]{24}\.([A-Za-z0-9]{64})` для маскирования всех вхождений [токенов Dynatrace API](/managed/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как пройти аутентификацию для использования Dynatrace API.") в наших телеметрических данных.

```
redaction:



allow_all_keys: true



blocked_values:



- dt0[a-z]0[1-9]\.[A-Za-z0-9]{24}\.([A-Za-z0-9]{64})



summary: info
```

### Имена пользователей

С помощью процессора transform маскируем атрибуты `user.id`, `user.name` и `user.full_name` с помощью [оператора `set`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/pkg/ottl/ottlfuncs/README.md#set).

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

### Номера банковских карт

С помощью transform processor настраиваем три инструкции [`replace_all_patterns`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/pkg/ottl/ottlfuncs/README.md#replace_all_patterns), которые маскируют номера банковских карт, оставляя видимыми только последние четыре цифры.

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

Для номеров банковских карт можно также использовать встроенную стандартную функцию OTTL [`IsValidLuhn()`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/pkg/ottl/ottlfuncs#isvalidluhn) вместо регулярных выражений, если нужно полностью блокировать значения, а не просто маскировать их.

### Номера IBAN

С помощью redaction processor используем регулярное выражение `^[A-Z]{2}[0-9]{2}(\\s*[A-Z0-9]){8,30}$`, чтобы замаскировать все вхождения IBAN в данных телеметрии.

```
redaction:



allow_all_keys: true



blocked_values:



- "^[A-Z]{2}[0-9]{2}(\\s*[A-Z0-9]){8,30}$"



summary: info
```

### Имена спанов

Имена спанов не хранятся как атрибуты в структуре сообщения OTLP, поэтому редактирование на основе атрибутов к ним неприменимо.
Есть несколько способов редактирования и упрощения имён спанов:

#### Сгенерировать новое имя спана

Рекомендуется

`set_semconv_span_name` доступна начиная с версии Collector Contrib 0.142.0 и Collector версии Dynatrace 0.42.0.

Используйте функцию transform processor [`set_semconv_span_name`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/transformprocessor#set_semconv_span_name), чтобы получить имя с низкой кардинальностью, соответствующее семантическим соглашениям OpenTelemetry. Оно использует (с низкой кардинальностью) `http.request.method` и `http.route` для формирования нового имени спана. Это сохраняет согласованность имени с соглашениями HTTP/RPC/messaging/database и не допускает утечки идентификаторов.

```
transform:



error_mode: ignore



trace_statements:



- context: span



statements:



- set_semconv_span_name("1.37.0")
```

#### Явное редактирование имени спана

```
transform:



error_mode: ignore



trace_statements:



- context: span



statements:



- replace_pattern(name, "(GET /api/v1/users/)\\d+", "$$1{id}")
```

Проверка конфигурации

[Проверьте свои настройки](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

В нашей конфигурации используются следующие компоненты.

### Receivers

В разделе `receivers` указывается стандартный receiver `otlp` как активный компонент-приёмник для нашего экземпляра Collector.

### Processors

В разделе `processors` размещается конфигурация нужных экземпляров процессоров.

### Exporters

В разделе `exporters` указывается стандартный [экспортёр `otlp_http`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter) и настраивается с URL нашего Dynatrace API и требуемым токеном аутентификации.

Для этого задаются следующие две переменные окружения, на которые даются ссылки в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Пайплайны сервиса

В разделе `service` в итоге собираются все настроенные объекты в пайплайны для отдельных сигналов телеметрии (трейсы и т. д.), и экземпляр Collector выполняет настроенные задачи.

## Похожие темы

* [Обогащение поступающих данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")