---
title: Mask sensitive data with the OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/redact
scraped: 2026-03-06T21:32:24.265515
---

# Маскирование конфиденциальных данных с помощью OpenTelemetry Collector

# Маскирование конфиденциальных данных с помощью OpenTelemetry Collector

* Latest Dynatrace
* Практическое руководство
* 5 мин. чтения
* Обновлено 12 января 2026

Телеметрические данные часто могут содержать конфиденциальную информацию (например, [персональные данные (PII)](https://en.wikipedia.org/wiki/Personal_data)), которую может потребоваться редактировать по соображениям безопасности и нормативного соответствия. Хотя это можно реализовать на стороне приложения, обычно лучше обрабатывать это централизованно с помощью шлюзов, таких как Collector. Это позволяет управлять правилами редактирования в одной точке для всех ваших приложений и сервисов, без необходимости обновлять код каждый раз, когда требуется новое правило редактирования.

На этой странице приведены примеры конфигураций Collector для редактирования определённых конфиденциальных данных (например, номеров кредитных карт или адресов электронной почты), которые могут появляться в телеметрических данных и которые должны быть замаскированы/отредактированы перед выходом из вашей сети.

## Предварительные требования

* Одна из следующих дистрибуций Collector с процессорами [transform](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/transformprocessor) и/или [redaction](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/redactionprocessor):

  + [Dynatrace Collector](../../collector.md#dt-collector-dist "Узнайте о Dynatrace OTel Collector.")
  + [OpenTelemetry Contrib](../../collector.md#collector-contrib "Узнайте о Dynatrace OTel Collector.")
  + [Пользовательская версия через Builder](../../collector.md#collector-builder "Узнайте о Dynatrace OTel Collector.")
* [URL конечной точки Dynatrace API](../../otlp-api.md "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."), на который должны экспортироваться данные
* [Токен API](../../otlp-api.md#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate)

Информацию о том, как настроить Collector с приведённой ниже конфигурацией, см. в разделах [Развёртывание Collector](../deployment.md "Как развернуть Dynatrace OTel Collector.") и [Конфигурация Collector](../configuration.md "Как настроить OpenTelemetry Collector.").

## Процессор redaction и процессор transform

В следующих примерах используются два [процессора](https://opentelemetry.io/docs/collector/architecture/#processors) Collector:

* [процессор transform](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/transformprocessor/README.md)
* [процессор redaction](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/redactionprocessor/README.md)

Хотя в следующих примерах оба процессора используются для маскирования данных, каждый процессор имеет своё собственное назначение. Процессор redaction прост и принимает список значений, на основе которых совпадающие данные будут полностью редактированы. С другой стороны, процессор transform более универсален и выходит за рамки простого редактирования данных.

Для редактирования данных, как правило, может использоваться любой из процессоров, и вы можете выбрать тот, который лучше подходит для вашего случая. Например, для полного редактирования данных процессор redaction может быть проще в использовании. С другой стороны, частичное редактирование данных может быть достигнуто только с помощью процессора transform. Кроме того, процессор transform также может фильтровать по данным в теле логов, тогда как процессор redaction имеет доступ только к атрибутам.

## Ограничения и замечания

Примеры, приведённые на этой странице, являются демонстрацией типичных сценариев редактирования. Обратите внимание на следующее:

* Примеры могут быть не исчерпывающими для всех случаев использования. Возможно, вам потребуется адаптировать их под ваши конкретные требования.
* Шаблоны регулярных выражений и сопоставление атрибутов работают только тогда, когда всё значение атрибута соответствует редактируемому шаблону. Частичные совпадения в более длинных строках могут потребовать более сложных шаблонов или дополнительной обработки.
* Имя span хранится как отдельное поле в структуре сообщения OTLP, а не как атрибут. Поэтому процессоры редактирования, нацеленные на атрибуты, по умолчанию не влияют на имена span. См. пример [Имена span](#span-names) для обработки этого случая.
* Порядок процессоров в конвейерах имеет значение. Применяйте transform/redaction перед маршрутизацией или экспортом, и размещайте связанные процессоры рядом, чтобы последующие шаги видели уже очищенные данные.

## Демонстрационная конфигурация

Этот YAML-документ представляет собой базовый каркас конфигурации Collector, содержащий основные общие компоненты (то есть receivers, exporters и определение конвейера).

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
* `PLACEHOLDER-FOR-PROCESSOR-REFERENCES`: ссылки на применимые объекты процессоров для отдельных типов сигналов

### IP-адреса

С помощью процессора transform мы маскируем атрибут `client.address` с помощью [оператора `set`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/pkg/ottl/ottlfuncs/README.md#set).

```
transform:



error_mode: ignore



trace_statements:



- context: span



statements: &filter-statements



# это замаскирует не только IP-адреса клиентов конечных пользователей,



# но и адрес сервера, выступающего в роли клиента при установлении соединения с другим сервером



- set(attributes["client.address"], "<masked-clientip-ot>")



metric_statements:



- context: datapoint



statements: *filter-statements



log_statements:



- context: log



statements: *filter-statements
```

### Адреса электронной почты

С помощью процессора transform мы маскируем атрибут `user.email` с помощью [оператора `set`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/pkg/ottl/ottlfuncs/README.md#set).

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

С помощью процессора redaction мы используем регулярное выражение `dt0[a-z]0[1-9]\.[A-Za-z0-9]{24}\.([A-Za-z0-9]{64})` для маскирования всех вхождений [токенов Dynatrace API](../../../../dynatrace-api/basics/dynatrace-api-authentication.md "Узнайте, как пройти аутентификацию для использования Dynatrace API.") в наших телеметрических данных.

```
redaction:



allow_all_keys: true



blocked_values:



- dt0[a-z]0[1-9]\.[A-Za-z0-9]{24}\.([A-Za-z0-9]{64})



summary: info
```

### Имена пользователей

С помощью процессора transform мы маскируем атрибуты `user.id`, `user.name` и `user.full_name` с помощью [оператора `set`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/pkg/ottl/ottlfuncs/README.md#set).

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

С помощью процессора transform мы настраиваем три [оператора `replace_all_patterns`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/pkg/ottl/ottlfuncs/README.md#replace_all_patterns) для маскирования любых вхождений номеров кредитных карт, сохраняя только последние четыре цифры.

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

Для номеров кредитных карт также можно использовать встроенную [стандартную функцию OTTL `IsValidLuhn()`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/pkg/ottl/ottlfuncs#isvalidluhn) вместо регулярных выражений, если вы предпочитаете полностью блокировать значения, а не просто маскировать их.

### Номера IBAN

С помощью процессора redaction мы используем регулярное выражение `^[A-Z]{2}[0-9]{2}(\\s*[A-Z0-9]){8,30}$` для маскирования всех вхождений IBAN в наших телеметрических данных.

```
redaction:



allow_all_keys: true



blocked_values:



- "^[A-Z]{2}[0-9]{2}(\\s*[A-Z0-9]){8,30}$"



summary: info
```

### Имена span

Имена span не хранятся как атрибуты в структуре сообщения OTLP, поэтому редактирование на основе атрибутов к ним не применяется.
Существует несколько способов редактирования и упрощения имён span:

#### Генерация нового имени span

Рекомендуется

`set_semconv_span_name` доступен начиная с Collector Contrib версии 0.142.0 и Dynatrace Collector версии 0.42.0.

Используйте [`set_semconv_span_name`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/transformprocessor#set_semconv_span_name) процессора transform для формирования имени с низкой кардинальностью, соответствующего семантическим конвенциям OpenTelemetry. При этом используются (низкокардинальные) `http.request.method` и `http.route` для генерации нового имени span. Это обеспечивает согласованность имени с конвенциями HTTP/RPC/messaging/database и предотвращает утечку идентификаторов.

```
transform:



error_mode: ignore



trace_statements:



- context: span



statements:



- set_semconv_span_name("1.37.0")
```

#### Явное редактирование имени span

```
transform:



error_mode: ignore



trace_statements:



- context: span



statements:



- replace_pattern(name, "(GET /api/v1/users/)\\d+", "$$1{id}")
```

Валидация конфигурации

[Проверьте ваши настройки](../configuration.md#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

Для нашей конфигурации мы используем следующие компоненты.

### Receivers

В разделе `receivers` мы указываем стандартный приёмник `otlp` в качестве активного компонента для нашего экземпляра Collector.

### Processors

В разделе `processors` мы размещаем конфигурацию для соответствующих экземпляров процессоров.

### Exporters

В разделе `exporters` мы указываем стандартный [экспортёр `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) и настраиваем его с нашим URL Dynatrace API и необходимым токеном аутентификации.

Для этого мы устанавливаем следующие две переменные окружения и ссылаемся на них в значениях конфигурации для `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL конечной точки Dynatrace API](../../otlp-api.md#export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [токен API](../../otlp-api.md#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Конвейеры сервисов

В разделе `service` мы собираем все настроенные объекты в конвейеры для отдельных телеметрических сигналов (трассировки и т. д.) и запускаем настроенные задачи на экземпляре Collector.

## Связанные темы

* [Обогащение полученных данных полями, специфичными для Dynatrace](../../../extend-dynatrace/extend-data.md "Узнайте, как автоматически обогащать ваши телеметрические данные полями, специфичными для Dynatrace.")