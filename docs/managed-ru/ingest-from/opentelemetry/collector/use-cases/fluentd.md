---
title: Приём данных FluentD с помощью OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/fluentd
---

# Приём данных FluentD с помощью OTel Collector

# Приём данных FluentD с помощью OTel Collector

* Практическое руководство
* Чтение: 1 мин
* Опубликовано 26 января 2024 г.

Пример конфигурации ниже показывает, как настроить экземпляр Collector на приём событий FluentD по [протоколу Fluent Forward﻿](https://github.com/fluent/fluentd/wiki/Forward-Protocol-Specification-v1) и передачу их в виде OTLP-запросов в Dynatrace.

## Предварительные требования

* Один из следующих дистрибутивов Collector с [приёмником Fluent Forward﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/fluentforwardreceiver):

  + [OTel Collector Dynatrace](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая OTel Collector Dynatrace, для приёма телеметрии из OpenTelemetry.")
  + [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая OTel Collector Dynatrace, для приёма телеметрии из OpenTelemetry.")
  + [Пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая OTel Collector Dynatrace, для приёма телеметрии из OpenTelemetry.")
* [URL конечной точки Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте о конечных точках OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace."), на которую нужно экспортировать данные
* [Токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с нужной областью доступа (требуется только для SaaS и ActiveGate)

О том, как настроить Collector с приведённой ниже конфигурацией, см. в разделах [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть OpenTelemetry Collector Dynatrace.") и [Настройка Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector.").

## Демонстрационная конфигурация

```
receivers:



fluentforward:



endpoint: 0.0.0.0:8006



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



logs:



receivers: [fluentforward]



processors: []



exporters: [otlp_http]
```

Проверка конфигурации

[Проверьте настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

В нашей конфигурации настроены следующие компоненты.

### Приёмники (Receivers)

В разделе `receivers` указывается приёмник `fluentforward` в качестве активного компонента-приёмника для экземпляра Collector и настраивается его прослушивание на указанных портах.

### Экспортёры (Exporters)

В разделе `exporters` указывается стандартный [экспортёр `otlp_http`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter) и настраивается с URL API Dynatrace и требуемым токеном аутентификации.

Для этого задаются следующие две переменные среды, на которые даётся ссылка в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL конечной точки API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте о конечных точках OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Конвейеры службы (Service pipelines)

В разделе `service` объекты приёмника и экспортёра собираются в конвейер логов, который будет прослушивать настроенный адрес на предмет логов FluentD и передавать данные в Dynatrace.

## Ограничения

Логи принимаются с использованием протокола OpenTelemetry (OTLP) через [OTLP API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api "Узнайте о конечных точках OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.") и подчиняются ограничениям и лимитам API.
Подробнее см. в разделе [Приём логов OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения при этом действуют.").

## Похожие темы

* [Обогащение принимаемых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать телеметрические данные полями, специфичными для Dynatrace.")
* [Обогащение OTLP-запросов данными Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Настройте OpenTelemetry Collector для обогащения OTLP-запросов данными Kubernetes.")
* [Приём логов из файлов с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/filelog "Настройте OpenTelemetry Collector для приёма данных логов в Dynatrace.")
* [Приём данных syslog с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/syslog "Настройте OpenTelemetry Collector для приёма данных syslog в Dynatrace.")