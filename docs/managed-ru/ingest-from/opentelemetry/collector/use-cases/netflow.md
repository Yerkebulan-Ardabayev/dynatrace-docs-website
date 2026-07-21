---
title: Приём NetFlow с помощью OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/netflow
---

# Приём NetFlow с помощью OTel Collector

# Приём NetFlow с помощью OTel Collector

* Практическое руководство
* Чтение: 1 мин
* Обновлено 11 мая 2026 г.

Приведённый ниже пример конфигурации показывает, как настроить экземпляр Collector для приёма пакетов NetFlow и передачи их в виде запросов OTLP в Dynatrace.

## Предварительные требования

* Один из следующих дистрибутивов Collector с [NetFlow receiver﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/netflowreceiver):

  + [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [Пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* [URL конечной точки Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."), в которую нужно экспортировать данные.
* [Токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") с областью действия Ingest logs (`logs.ingest`).
* Устройство с поддержкой NetFlow или sFlow, способное отправлять пакеты NetFlow на экземпляр OTel Collector.

О том, как настроить Collector с приведённой ниже конфигурацией, см. в разделах [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.") и [Настройка Collector](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.").

## Конфигурация Collector

```
receivers:



netflow:



hostname: "0.0.0.0"



scheme: netflow



port: 2055



sockets: 2



workers: 4



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



sending_queue:



batch:



# Use default batching settings for logs.



min_size: 1800



max_size: 2000



flush_timeout: 60s



service:



pipelines:



logs:



receivers: [netflow]



processors: [batch]



exporters: [otlp_http]
```

Доступные варианты конфигурации см. в документации [NetFlow receiver﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/netflowreceiver#netflow-receiver).

Рекомендуется устанавливать параметр `sockets` равным числу ядер CPU, доступных на экземпляре Collector, а параметр `workers`, вдвое больше числа сокетов. Такая конфигурация позволяет Collector обрабатывать несколько входящих пакетов NetFlow одновременно, что повышает производительность.

Для чрезвычайно больших объёмов данных конфигурацию следует распараллелить между несколькими экземплярами Collector.

Проверка конфигурации

[Проверьте настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

В нашей конфигурации настроены следующие компоненты.

### Receivers

В разделе `receivers` указан receiver `netflow` в качестве активного компонента-приёмника для экземпляра Collector, настроенный на прослушивание указанных портов.

### Processors

В разделе `processors` указан процессор `batch`, который группирует входящие пакеты NetFlow перед отправкой в Dynatrace. Это полезно для оптимизации производительности и сокращения числа отправляемых запросов.

### Exporters

В разделе `exporters` указан стандартный [экспортёр `otlp_http`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter), настроенный с URL API Dynatrace и необходимым токеном авторизации.

Для этого задаются следующие две переменные окружения, на которые даются ссылки в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL конечной точки Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Конвейеры служб

В разделе `service` объекты receiver и exporter объединяются в конвейер логов, который будет прослушивать настроенный адрес на предмет входящих пакетов NetFlow и передавать их в Dynatrace с помощью экспортёра.

## Лимиты и ограничения

Логи принимаются с использованием протокола OpenTelemetry (OTLP) через [API OTLP Dynatrace](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") и подчиняются лимитам и ограничениям API.
Подробнее см. в разделе [Приём логов OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.").

## Связанные темы

* [Приём логов из файлов с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/filelog "Configure the OpenTelemetry Collector to ingest log data into Dynatrace.")