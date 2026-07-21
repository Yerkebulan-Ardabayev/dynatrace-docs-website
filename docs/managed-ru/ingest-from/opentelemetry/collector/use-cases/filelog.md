---
title: Приём логов из файлов с помощью OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/filelog
---

# Приём логов из файлов с помощью OTel Collector

# Приём логов из файлов с помощью OTel Collector

* Практическое руководство
* Чтение: 3 мин
* Обновлено 09 апреля 2026

Приведённый ниже пример конфигурации показывает, как настроить экземпляр Collector для мониторинга файлов логов и отправки их записей в бэкенд Dynatrace.

## Предварительные требования

* Один из следующих дистрибутивов Collector с [Filelog receiver﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/filelogreceiver):

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [Пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* [URL конечной точки Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."), на который нужно экспортировать данные
* [Токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate)

Информацию о том, как настроить Collector с приведённой ниже конфигурацией, см. в разделах [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.") и [Настройка Collector](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.").

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

[Проверьте свои настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Пример файла логов

Для приведённой выше демонстрационной конфигурации разбирается файл `file.log` со следующим форматом:

```
1970-01-01 INFO Something routine



1970-01-01 ERROR Some error occurred!



1970-01-01 DEBUG Some details...
```

Каждая строка начинается с временной метки ISO 8601, за ней следует уровень серьёзности записи, а завершается строка сообщением лога.

Каждая строка разбирается на отдельные части с помощью следующего регулярного выражения:

```
^(?P<time>\d{4}-\d{2}-\d{2}) (?P<sev>[A-Z]*) (?P<msg>.*)$
```

Помимо утверждений о начале (`^`) и конце (`$`) строки, здесь используются следующие именованные группы захвата:

* `(?P<time>\d{4}-\d{2}-\d{2})`, называет группу захвата `time` и находит соответствие типичной временной метке ISO 8601.
* `(?P<sev>[A-Z]*)`, называет группу захвата `sev` и находит соответствие произвольному числу латинских заглавных символов.
* `(?P<msg>.*)`, называет группу захвата `msg` и находит соответствие произвольному числу символов.

## Компоненты

В нашей конфигурации используются следующие компоненты.

### Receivers (приёмники)

В разделе `receivers` указывается приёмник `filelog` в качестве активного компонента-приёмника для экземпляра Collector.

Filelog receiver поддерживает ряд [параметров конфигурации﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/receiver/filelogreceiver/README.md), которые позволяют настраивать его поведение под свои нужды. В нашем примере используются следующие:

* `include`, задаёт шаблон пути к файлам, которые нужно принимать.
* `start_at`, определяет, должен ли приёмник читать файл с начала или, для получения только самых последних записей, с конца.
* `operators`, настраивает операторы, применяемые к каждой записи лога. В нашем примере используется оператор [regex\_parser﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/pkg/stanza/docs/operators/regex_parser.md) для извлечения информации с помощью регулярного выражения.

  + `regex`, задаёт само регулярное выражение. Используя именованные группы захвата (`(?P<name>)`), приёмник делает захваченные данные доступными в `attributes` под соответствующим именем.
  + `timestamp`, указывает, откуда брать временную метку записи (поле `time` регулярного выражения) и формат даты.
  + `severity`, указывает, откуда брать уровень серьёзности записи (поле `sev` регулярного выражения).

### Exporters (экспортёры)

В разделе `exporters` указывается экспортёр по умолчанию [`otlp_http`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter) и настраивается с URL Dynatrace API и необходимым токеном аутентификации.

Для этого задаются следующие две переменные окружения, на которые есть ссылка в значениях конфигурации для `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL конечной точки Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipelines (конвейеры службы)

В разделе `service` в итоге собираются объекты приёмника и экспортёра в конвейер трейсов, который будет непрерывно отслеживать настроенные файлы и принимать их записи в Dynatrace с помощью OTLP.

## Ограничения

Логи принимаются с помощью протокола OpenTelemetry (OTLP) через [OTLP API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") и подчиняются ограничениям и лимитам API.
Подробнее см. в разделе [Приём логов OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.").

## Связанные темы

* [Обогащение принимаемых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")
* [Обогащение запросов OTLP данными Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")
* [Приём данных FluentD с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/fluentd "Configure the OpenTelemetry Collector to ingest FluentD data.")
* [Приём данных syslog с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/syslog "Configure the OpenTelemetry Collector to ingest syslog data into Dynatrace.")