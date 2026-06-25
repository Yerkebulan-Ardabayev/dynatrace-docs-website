---
title: Приём NetFlow с помощью OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/netflow
scraped: 2026-05-12T12:11:00.045039
---

# Приём NetFlow с помощью OTel Collector

# Приём NetFlow с помощью OTel Collector

* Практическое руководство
* Чтение: 1 мин
* Обновлено 27 января 2026 г.

В следующем примере конфигурации показано, как настроить экземпляр Collector для приёма пакетов NetFlow и их передачи в виде запросов OTLP в Dynatrace.

## Предварительные требования

* Один из следующих дистрибутивов Collector с [receiver NetFlow](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/netflowreceiver):

  + [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* [URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."), на который должны экспортироваться данные.
* [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с областью доступа Ingest logs (`logs.ingest`).
* Устройство с поддержкой NetFlow или sFlow, способное отправлять пакеты NetFlow в экземпляр OTel Collector.

См. [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.") и [Настройку Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector."), чтобы узнать, как настроить ваш Collector с приведённой ниже конфигурацией.

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

Доступные параметры конфигурации см. в документации по [receiver NetFlow](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/netflowreceiver#netflow-receiver).

Мы рекомендуем задавать параметру `sockets` значение, равное числу доступных на экземпляре Collector ядер CPU, а параметру `workers` задавать удвоенное число сокетов. Такая конфигурация позволяет Collector обрабатывать несколько входящих пакетов NetFlow одновременно, что повышает производительность.

Для очень больших объёмов данных следует распараллелить конфигурацию между несколькими экземплярами Collector.

Проверка конфигурации

[Проверьте ваши настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

Для нашей конфигурации мы настраиваем следующие компоненты.

### Receivers

В разделе `receivers` мы указываем receiver `netflow` в качестве активного компонента receiver для нашего экземпляра Collector и настраиваем его на прослушивание указанных портов.

### Processors

В разделе `processors` мы указываем processor `batch`, который группирует входящие пакеты NetFlow перед их отправкой в Dynatrace. Это полезно для оптимизации производительности и сокращения числа отправляемых запросов.

### Exporters

В разделе `exporters` мы указываем стандартный [exporter `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) и настраиваем его с помощью URL нашего Dynatrace API и необходимого токена аутентификации.

Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Сервисные конвейеры

В разделе `service` мы собираем наши объекты receiver и exporter в конвейер логов, который прослушивает настроенный адрес на наличие входящих пакетов NetFlow и пересылает их в Dynatrace с помощью exporter.

## Пределы и ограничения

Логи принимаются с помощью протокола OpenTelemetry (OTLP) через [Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") и подчиняются ограничениям и лимитам этого API.
Дополнительные сведения см. в разделе [Приём логов OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения применяются.").

## Связанные темы

* [Приём логов из файлов с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/filelog "Настройте OpenTelemetry Collector для приёма данных логов в Dynatrace.")