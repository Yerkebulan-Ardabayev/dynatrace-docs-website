---
title: Приём данных syslog с помощью OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/syslog
---

# Приём данных syslog с помощью OTel Collector

# Приём данных syslog с помощью OTel Collector

* Практическое руководство
* Чтение 3 мин
* Опубликовано 26 янв. 2024 г.

Пример конфигурации ниже показывает, как настроить экземпляр Collector для приёма данных из syslog и отправки их на бэкенд Dynatrace.

## Предварительные условия

* Один из следующих дистрибутивов Collector с [attributes processor﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/attributesprocessor) и [Syslog receiver﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/syslogreceiver):

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + OpenTelemetry [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [Собственная версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* [URL конечной точки Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."), на которую нужно экспортировать данные
* [Токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate)

О том, как настроить Collector с приведённой ниже конфигурацией, см. [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.") и [Настройка Collector](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.").

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

[Проверьте настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

В этой конфигурации используются следующие компоненты.

### Receivers

В разделе `receivers` указаны два экземпляра receiver'а `syslog` в качестве активных компонентов-получателей для экземпляра Collector.

Syslog receiver поддерживает ряд [параметров конфигурации﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/receiver/syslogreceiver/README.md), которые позволяют настраивать его поведение. В этом примере используются следующие:

* `tcp`, задаёт TCP-listener для receiver'а и настраивает порты 54526 и 54527
* `protocol`, задаёт реализацию RFC 5424 для receiver'а (в качестве альтернативы также поддерживается RFC 3164)
* `operators`, настраивает операторы, применяемые к каждой записи лога. В этом примере используется оператор [add﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/pkg/stanza/docs/operators/add.md) для добавления дополнительной информации.

  + `field`, задаёт имя добавляемого значения
  + `value`, задаёт содержимое добавляемого значения

### Processors

В разделе `processors` настраивается processor `attributes`, который отбрасывает и корректирует указанные атрибуты в OTLP-запросе.

### Exporters

В разделе `exporters` указывается стандартный [`otlp_http` exporter﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter), который настраивается с URL API Dynatrace и необходимым токеном аутентификации.

Для этого задаются следующие две переменные окружения, на которые есть ссылки в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL конечной точки API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipelines

В разделе `service` в итоге собираются объекты receiver, processor и exporter в pipeline логов, который использует экземпляры receiver'ов для получения данных syslog и их приёма в Dynatrace с помощью OTLP.

## Ограничения

Логи принимаются с помощью протокола OpenTelemetry (OTLP) через [Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") и подчиняются ограничениям и лимитам API.
Подробнее см. [Приём логов OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.").

## Похожие темы

* [Обогащение принятых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")
* [Обогащение OTLP-запросов данными Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")
* [Приём логов из файлов с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/filelog "Configure the OpenTelemetry Collector to ingest log data into Dynatrace.")
* [Приём данных FluentD с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/fluentd "Configure the OpenTelemetry Collector to ingest FluentD data.")
* [Недоступно в Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.")