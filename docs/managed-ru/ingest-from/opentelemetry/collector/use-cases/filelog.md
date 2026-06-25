---
title: Приём логов из файлов с помощью OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/filelog
scraped: 2026-05-12T12:06:11.003036
---

# Приём логов из файлов с помощью OTel Collector

# Приём логов из файлов с помощью OTel Collector

* Практическое руководство
* Чтение: 3 мин
* Обновлено 09 апреля 2026 г.

В следующем примере конфигурации показано, как настроить экземпляр Collector для мониторинга файлов логов и отправки их записей логов в бэкенд Dynatrace.

## Предварительные требования

* Один из следующих дистрибутивов Collector с [receiver Filelog](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/filelogreceiver):

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* [URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."), на который должны экспортироваться данные
* [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate)

См. [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.") и [Настройку Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector."), чтобы узнать, как настроить ваш Collector с приведённой ниже конфигурацией.

## Демонстрационная конфигурация

```
receivers:



file_log:



include: [ /path/to/file.log ]



start_at: beginning



operators:



- type: regex_parser



regex: '^(?P<time>\d{4}-\d{2}-\d{2}) (?P<sev>[A-Z]*) (?P<msg>.*)$'



timestamp:



parse_from: attributes.time



layout: '%Y-%m-%d'



severity:



parse_from: attributes.sev



exporters:



otlp_http/dynatrace:



endpoint: ${env:DT_ENDPOINT}



headers:



"Authorization": "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



logs:



receivers: [file_log]



processors: []



exporters: [otlp_http/dynatrace]
```

Проверка конфигурации

[Проверьте ваши настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Пример файла логов

Для приведённой выше демонстрационной конфигурации мы разбираем файл `file.log` следующего формата:

```
1970-01-01 INFO Something routine



1970-01-01 ERROR Some error occurred!



1970-01-01 DEBUG Some details...
```

Каждая строка начинается с метки времени в формате ISO 8601, за которой следует уровень серьёзности записи, и заканчивается сообщением лога.

Мы разбираем каждую строку на отдельные части с помощью следующего регулярного выражения:

```
^(?P<time>\d{4}-\d{2}-\d{2}) (?P<sev>[A-Z]*) (?P<msg>.*)$
```

Помимо двух утверждений начала (`^`) и конца (`$`) строки, у нас есть следующие именованные группы захвата:

* `(?P<time>\d{4}-\d{2}-\d{2})`: называет свою группу захвата `time` и сопоставляется с типичной меткой времени ISO 8601.
* `(?P<sev>[A-Z]*)`: называет свою группу захвата `sev` и сопоставляется с произвольным числом латинских символов в верхнем регистре.
* `(?P<msg>.*)`: называет свою группу захвата `msg` и сопоставляется с произвольным числом символов.

## Компоненты

Для нашей конфигурации мы используем следующие компоненты.

### Receivers

В разделе `receivers` мы указываем receiver `filelog` в качестве активного компонента receiver для нашего экземпляра Collector.

Receiver Filelog поддерживает ряд [параметров конфигурации](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/receiver/filelogreceiver/README.md), позволяющих настроить его поведение. В нашем примере мы используем следующие:

* `include`: задаёт шаблон пути к файлам, которые мы хотим принимать.
* `start_at`: задаёт, должен ли receiver читать с начала файла или, только для самых последних записей, с конца.
* `operators`: настраивает операторы, применяемые к каждой записи лога. В нашем примере мы используем оператор [regex\_parser](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/stanza/docs/operators/regex_parser.md) для извлечения информации с помощью регулярного выражения.

  + `regex`: задаёт само регулярное выражение. Используя именованные группы захвата (`(?P<name>)`), receiver делает захваченные данные доступными в `attributes` под соответствующим именем.
  + `timestamp`: задаёт, откуда брать метку времени записи (поле `time` регулярного выражения) и формат даты.
  + `severity`: задаёт, откуда брать уровень серьёзности записи (поле `sev` регулярного выражения).

### Exporters

В разделе `exporters` мы указываем стандартный [exporter `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) и настраиваем его с помощью URL нашего Dynatrace API и необходимого токена аутентификации.

Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Сервисные конвейеры

В разделе `service` мы в итоге собираем наши объекты receiver и exporter в конвейер трассировок, который непрерывно отслеживает настроенные файлы и принимает их записи в Dynatrace с помощью OTLP.

## Пределы и ограничения

Логи принимаются с помощью протокола OpenTelemetry (OTLP) через [Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") и подчиняются ограничениям и лимитам этого API.
Дополнительные сведения см. в разделе [Приём логов OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения применяются.").

## Связанные темы

* [Обогащение принимаемых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.")
* [Обогащение запросов OTLP данными Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Настройте OpenTelemetry Collector для обогащения запросов OTLP данными Kubernetes.")
* [Приём данных FluentD с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/fluentd "Настройте OpenTelemetry Collector для приёма данных FluentD.")
* [Приём данных syslog с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/syslog "Настройте OpenTelemetry Collector для приёма данных syslog в Dynatrace.")