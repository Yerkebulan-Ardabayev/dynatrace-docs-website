---
title: Приём данных syslog с помощью OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/syslog
scraped: 2026-05-12T11:36:20.177711
---

# Приём данных syslog с помощью OTel Collector

# Приём данных syslog с помощью OTel Collector

* Практическое руководство
* Чтение: 3 мин
* Опубликовано 26 января 2024 г.

В следующем примере конфигурации показано, как настроить экземпляр Collector для приёма данных из syslog и их отправки в бэкенд Dynatrace.

## Предварительные требования

* Один из следующих дистрибутивов Collector с [processor attributes](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/attributesprocessor) и [receiver Syslog](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/syslogreceiver):

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + OpenTelemetry [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* [URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."), на который должны экспортироваться данные
* [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate)

См. [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.") и [Настройку Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector."), чтобы узнать, как настроить ваш Collector с приведённой ниже конфигурацией.

## Демонстрационная конфигурация

```
receivers:



syslog/f5:



tcp:



listen_address: "0.0.0.0:54526"



protocol: rfc5424



operators:



- type: add



field: attributes.log.source



value: syslog



- type: add



field: attributes.dt.ip_addresses



value: "1xx.xx.xx.xx1"



- type: add



field: attributes.instance.name



value: "ip-1xx-xx-x-xx9.ec2.internal"



- type: add



field: attributes.device.type



value: "f5bigip"



syslog/host:



tcp:



listen_address: "0.0.0.0:54527"



protocol: rfc5424



operators:



- type: add



field: attributes.log.source



value: syslog



- type: add



field: attributes.device.type



value: "ubuntu-syslog"



processors:



attributes:



actions:



- key: net.host.name



action: delete



- key: net.peer.name



action: delete



- key: net.peer.port



action: delete



- key: net.transport



action: delete



- key: net.host.ip



action: delete



- key: dt.ingest.port



from_attribute: net.host.port



action: upsert



- key: dt.ingest.source.ip



from_attribute: net.peer.ip



action: upsert



- key: net.peer.ip



action: delete



- key: net.host.port



action: delete



- key: syslog.hostname



from_attribute: hostname



action: upsert



- key: hostname



action: delete



- key: syslog.facility



from_attribute: facility



action: upsert



- key: facility



action: delete



- key: syslog.priority



from_attribute: priority



action: upsert



- key: priority



action: delete



- key: syslog.proc_id



from_attribute: proc_id



action: upsert



- key: proc_id



action: delete



- key: syslog.version



from_attribute: version



action: upsert



- key: version



action: delete



- key: syslog.appname



from_attribute: appname



action: upsert



- key: appname



action: delete



- key: message



action: delete



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



logs:



receivers: [syslog/f5, syslog/host]



processors: [attributes]



exporters: [otlp_http]
```

Проверка конфигурации

[Проверьте ваши настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

Для нашей конфигурации мы используем следующие компоненты.

### Receivers

В разделе `receivers` мы указываем два экземпляра receiver `syslog` в качестве активных компонентов receiver для нашего экземпляра Collector.

Receiver Syslog поддерживает ряд [параметров конфигурации](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/receiver/syslogreceiver/README.md), позволяющих настроить его поведение. В нашем примере мы используем следующие:

* `tcp`: задаёт TCP-приёмник для receiver и настраивает порты 54526 и 54527
* `protocol`: задаёт реализацию RFC 5424 для нашего receiver (в качестве альтернативы также поддерживается RFC 3164)
* `operators`: настраивает операторы, применяемые к каждой записи лога. В нашем примере мы используем оператор [add](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/stanza/docs/operators/add.md) для добавления дополнительной информации.

  + `field`: задаёт имя добавляемого значения
  + `value`: задаёт содержимое добавляемого значения

### Processors

В разделе `processors` мы настраиваем processor `attributes` для удаления и корректировки указанных атрибутов в нашем запросе OTLP.

### Exporters

В разделе `exporters` мы указываем стандартный [exporter `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) и настраиваем его с помощью URL нашего Dynatrace API и необходимого токена аутентификации.

Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Сервисные конвейеры

В разделе `service` мы в итоге собираем наши объекты receiver, processor и exporter в конвейер логов, который использует экземпляры receiver для получения данных syslog и их приёма в Dynatrace с помощью OTLP.

## Пределы и ограничения

Логи принимаются с помощью протокола OpenTelemetry (OTLP) через [Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") и подчиняются ограничениям и лимитам этого API.
Дополнительные сведения см. в разделе [Приём логов OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения применяются.").

## Связанные темы

* [Обогащение принимаемых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.")
* [Обогащение запросов OTLP данными Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Настройте OpenTelemetry Collector для обогащения запросов OTLP данными Kubernetes.")
* [Приём логов из файлов с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/filelog "Настройте OpenTelemetry Collector для приёма данных логов в Dynatrace.")
* [Приём данных FluentD с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/fluentd "Настройте OpenTelemetry Collector для приёма данных FluentD.")
* [Недоступно в Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.")