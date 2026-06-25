---
title: Настройка OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/configuration
scraped: 2026-05-12T11:37:06.786803
---

# Настройка OTel Collector

# Настройка OTel Collector

* Практическое руководство
* Чтение: 4 мин
* Обновлено 16 апреля 2026 г.

Для успешной настройки экземпляра OTel Collector нужно настроить каждый компонент (receiver, необязательный processor и exporter) по отдельности в файле конфигурации YAML Collector и включить их с помощью дополнительных объектов конвейера.

Dynatrace OTel Collector

При использовании дистрибутива Dynatrace OTel Collector следует учитывать, что настраивать можно только компоненты, входящие в его состав.

Полный список компонентов, поддерживаемых Dynatrace OTel Collector, см. в разделе [OTel Collector для приёма телеметрии в Dynatrace](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.").

## Пример конфигурации

Ниже приведён пример файла YAML с минимальной конфигурацией Collector, которую можно использовать для экспорта трассировок, метрик и логов OpenTelemetry в Dynatrace.

```
receivers:



otlp:



protocols:



grpc:



endpoint: 0.0.0.0:4317



http:



endpoint: 0.0.0.0:4318



processors:



cumulativetodelta:



max_staleness: 25h



exporters:



otlp_http:



endpoint: "${env:DT_ENDPOINT}"



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



traces:



receivers: [otlp]



processors: []



exporters: [otlp_http]



metrics:



receivers: [otlp]



processors: [cumulativetodelta]



exporters: [otlp_http]



logs:



receivers: [otlp]



processors: []



exporters: [otlp_http]
```

Рекомендации по processor cumulativetodelta

Параметру `max_staleness` [processor cumulativetodelta](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/cumulativetodeltaprocessor) рекомендуется задавать значение, превышающее интервал поступления метрик в Collector (например, интервал поступления метрик по OTLP или интервал сбора Prometheus). Это гарантирует, что ссылки на заброшенные потоки метрик не будут накапливаться в памяти с течением времени.

В этом файле YAML мы настраиваем следующие компоненты:

* Receiver OTLP (`otlp`), способный принимать данные по gRPC и HTTP.
* Processor для преобразования метрик с кумулятивной темпоральностью в дельта-темпоральность (подробнее см. в разделе [Дельта-метрики](#delta-metrics)).
* Exporter OTLP HTTP (`otlp_http`), настроенный с указанием:

  + эндпоинта Dynatrace, см. раздел [Базовые URL](/managed/ingest-from/opentelemetry/otlp-api#base-url "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")
  + API-токена, см. раздел [Аутентификация](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.").

В рамках конфигурации exporter `otlp_http` также можно задать `logs_endpoint`, чтобы управлять обработкой структурированных данных логов в Dynatrace: сохранять исходную вложенную структуру (`raw`) или выравнивать её в виде путей к ключам (`flattened`).
Дополнительные сведения см. в разделе [Настройка обработки структурированных логов](#structured-logs).

В приведённом выше примере конфигурации токен Dynatrace должен иметь разрешения **Ingest OpenTelemetry traces** (`openTelemetryTrace.ingest`), **Ingest metrics** (`metrics.ingest`) и **Ingest logs** (`logs.ingest`).

В разделе `service` каждый компонент определяется по отдельности.

* Extensions включаются в собственном разделе, тогда как receivers, processors и exporters группируются в разделе конвейера.
* Конвейеры могут быть типа traces, metrics или logs.
* Каждый receiver/processor/exporter можно использовать в нескольких конвейерах. Для processors, задействованных в нескольких конвейерах, каждый конвейер получает отдельный экземпляр processor. В отличие от них, receivers/exporters, задействованные в нескольких конвейерах, используют единственный экземпляр receiver/exporter для всех конвейеров. Следует также учитывать, что порядок processors определяет порядок обработки данных.
* Одни и те же компоненты можно определять более одного раза. Например, можно задать два разных receiver или даже два и более отдельных участка конвейера.
* Даже если компонент правильно настроен в своём разделе, он не будет активирован, пока не будет также определён в разделе `service`.

## Проверка конфигурации

Важно убедиться, что используемая конфигурация Collector синтаксически и семантически корректна. Например, в YAML для определения иерархии документа используются пробелы (не символы табуляции), и для каждого раздела и компонента необходим правильный уровень отступа. Collector предоставляет встроенную команду `validate` для проверки корректности конфигурации, её компонентов и сервисов.

```
dynatrace-otel-collector validate --config=[PATH_TO_YOUR_CONFIGURATION_FILE]
```

Если экземпляр Collector запущен в контейнере, для выполнения проверки непосредственно из контейнера также можно использовать следующую команду Docker.

```
docker run -v $(pwd):$(pwd) -w $(pwd) ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.48.0 validate --config=[YOUR_CONFIGURATION_FILE]
```

## Дельта-метрики

Dynatrace требует, чтобы данные метрик [передавались с дельта-темпоральностью](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#aggregation-temporality "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются."), а **не** с кумулятивной темпоральностью.

Если в приложении нет возможности настроить дельта-темпоральность, можно использовать [processor `cumulativetodelta`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/cumulativetodeltaprocessor), чтобы экземпляр Collector преобразовывал кумулятивные значения в значения с дельта-темпоральностью. В [примере конфигурации](#configuration-example) выше показано, как настроить processor и указать его в конфигурации Collector.

## Цепочечные Collector и балансировка нагрузки

При использовании нескольких экземпляров Collector важно обеспечить стабильное распространение значений между всеми экземплярами.

Это особенно важно при отправке запросов OTLP через разные экземпляры Collector (например, при балансировке нагрузки), поскольку каждый экземпляр Collector отслеживает собственное дельта-смещение, что может нарушить корректность данных, передаваемых в бэкенд Dynatrace.

В таких сценариях мы рекомендуем направлять запросы OTLP через единственный исходящий экземпляр Collector, который пересылает данные в бэкенд Dynatrace и выполняет преобразование дельта-значений. Остальные экземпляры Collector должны использовать кумулятивную агрегацию для обеспечения стабильного и согласованного распространения значений.

## Настройка обработки структурированных логов

При экспорте структурированных логов в Dynatrace обработка данных логов выполняется одним из двух способов.
Варианты:

* Сохранить исходную вложенную структуру из источника логов (`"raw"`).
* Выровнять её так, чтобы все значения атрибутов логов были доступны через пути к ключам (`"flattened"`).

Для настройки этого поведения используйте параметр `logs_endpoint`, как показано в примере ниже:

```
exporters:



otlp_http:



endpoint: "${env:DT_ENDPOINT}"



logs_endpoint: "${env:DT_ENDPOINT}/v1/logs?structure=raw"



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"
```

Нужно указать полный путь к эндпоинту API, включая `/v1/logs` (допускаются переменные окружения), а затем желаемое поведение.

* Чтобы сохранить исходную вложенную структуру, используйте `structure=raw`.
* Чтобы выровнять данные логов, используйте `structure=flattened`.

Дополнительные сведения см. в разделе [Обработка API приёма логов](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs#otlp-structured-logs "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения применяются.").

Если этот параметр конфигурации не задан, поведение по умолчанию зависит от даты создания среды.

* Для Dynatrace версии 1.331+ и сред, созданных после 1 февраля 2026 г.: Raw.
* Для сред, созданных до 1 февраля 2026 г.: Flattened.