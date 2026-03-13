---
title: Ingest NetFlow with the OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/netflow
scraped: 2026-03-06T21:27:28.297927
---

# Приём данных NetFlow с помощью OpenTelemetry Collector

# Приём данных NetFlow с помощью OpenTelemetry Collector

* Последняя версия Dynatrace
* Практическое руководство
* Чтение: 1 мин
* Обновлено 27 янв. 2026

Следующий пример конфигурации показывает, как настроить экземпляр Collector для приёма пакетов NetFlow и их передачи в Dynatrace в виде запросов OTLP.

## Предварительные требования

* Один из следующих дистрибутивов Collector с [приёмником NetFlow](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/receiver/netflowreceiver):

  + [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте о Dynatrace OTel Collector.")
  + [OpenTelemetry Contrib](/docs/ingest-from/opentelemetry/collector#collector-contrib "Узнайте о Dynatrace OTel Collector.")
  + [Пользовательская сборка с помощью Builder](/docs/ingest-from/opentelemetry/collector#collector-builder "Узнайте о Dynatrace OTel Collector.")
* [URL конечной точки Dynatrace API](/docs/ingest-from/opentelemetry/otlp-api "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."), на которую должны экспортироваться данные.
* [API-токен](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с областью действия Ingest logs (`logs.ingest`).
* Устройство с поддержкой NetFlow или sFlow, способное отправлять пакеты NetFlow на экземпляр Collector.

См. [Развёртывание Collector](/docs/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OTel Collector.") и [Конфигурация Collector](/docs/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector.") для получения информации о настройке вашего Collector с приведённой ниже конфигурацией.

## Конфигурация Collector

```
receivers:



netflow:



hostname: "0.0.0.0"



scheme: netflow



port: 2055



sockets: 2



workers: 4



processors:



batch:



send_batch_size: 30



timeout: 30s



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



logs:



receivers: [netflow]



processors: [batch]



exporters: [otlp_http]
```

Ознакомьтесь с документацией [приёмника NetFlow](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/receiver/netflowreceiver#netflow-receiver) для получения информации о доступных параметрах конфигурации.

Мы рекомендуем устанавливать параметр `sockets` равным количеству ядер CPU, доступных на экземпляре Collector, а параметр `workers` — удвоенному количеству сокетов. Такая конфигурация позволяет Collector обрабатывать несколько входящих пакетов NetFlow параллельно, что повышает производительность.

Для очень больших объёмов данных следует распараллелить конфигурацию между несколькими экземплярами Collector.

Проверка конфигурации

[Проверьте ваши настройки](/docs/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

Для нашей конфигурации мы настраиваем следующие компоненты.

### Приёмники

В разделе `receivers` мы указываем приёмник `netflow` как активный компонент-приёмник для нашего экземпляра Collector и настраиваем его для прослушивания на указанных портах.

### Процессоры

В разделе `processors` мы указываем процессор `batch`, который объединяет входящие пакеты NetFlow в пакеты перед отправкой в Dynatrace. Это полезно для оптимизации производительности и уменьшения количества отправляемых запросов.

### Экспортёры

В разделе `exporters` мы указываем стандартный [экспортёр `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) и настраиваем его с URL нашего Dynatrace API и необходимым токеном аутентификации.

Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации для `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL конечной точки Dynatrace API](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [API-токен](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Конвейеры сервиса

В разделе `service` мы собираем наши объекты приёмника и экспортёра в конвейер логов, который будет слушать на настроенном адресе входящие пакеты NetFlow и пересылать их в Dynatrace с помощью экспортёра.

## Визуализация данных

Записи логов будут доступны в Dynatrace с полями, описанными в [документации приёмника](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/receiver/netflowreceiver#data-format).

### Примеры запросов DQL

* Получение всех логов NetFlow и суммирование байтов и пакетов по адресам источника и назначения:

  ```
  fetch logs



  | filter otel.scope.name == "otelcol/netflowreceiver"



  | summarize {bytes=sum(toDouble(flow.io.bytes)), packets=sum(toDouble(flow.io.packets))}, by: {source = source.address, destination = destination.address}



  | fieldsAdd bytes_relative=bytes



  | fieldsAdd packets_relative=packets



  | sort bytes desc
  ```

  ![Примеры графиков NetFlow, показывающие основные источники, назначения и соединения](https://dt-cdn.net/images/screenshot-2025-06-16-at-12-55-07-pm-1956-d01b596006.png)
* Получение наиболее используемых портов:

  ```
  fetch logs



  | filter otel.scope.name == "otelcol/netflowreceiver"



  | summarize {bytes=sum(toDouble(flow.io.bytes))}, by: {port = destination.port}



  | sort bytes desc



  | limit 10
  ```

  ![График NetFlow, показывающий наиболее используемые порты по объёму байтов](https://dt-cdn.net/images/screenshot-2025-06-16-at-1-04-11-pm-734-9a3a884a16.png)

## Ограничения и лимиты

Логи передаются с использованием протокола OpenTelemetry (OTLP) через [Dynatrace OTLP API](/docs/ingest-from/opentelemetry/otlp-api "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") и подчиняются ограничениям и лимитам API.
Дополнительная информация:

* [Приём логов OpenTelemetry](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения действуют.")

## Связанные темы

* [Приём логов из файлов с помощью OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/use-cases/filelog "Настройка OpenTelemetry Collector для приёма данных логов в Dynatrace.")
