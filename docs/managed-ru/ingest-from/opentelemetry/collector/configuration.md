---
title: Настройка OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/configuration
---

# Настройка OTel Collector

# Настройка OTel Collector

* Практическое руководство
* Чтение займёт 4 мин
* Обновлено 16 апр. 2026 г.

Чтобы успешно настроить экземпляр OTel Collector, нужно настроить каждый компонент (receiver, опциональный processor и exporter) отдельно в файле конфигурации Collector YAML и включить их через дополнительные объекты pipeline.

Dynatrace OTel Collector

В рамках настройки Dynatrace OTel Collector учитывай, что можно настраивать только компоненты, поставляемые вместе с Dynatrace OTel Collector.

Полный список компонентов, поддерживаемых Dynatrace OTel Collector, см. в разделе [OTel Collector для приёма телеметрии в Dynatrace](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнай, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.").

## Пример конфигурации

Ниже приведён пример файла YAML для очень простой конфигурации Collector, которую можно использовать для экспорта трасс, метрик и логов OpenTelemetry в Dynatrace.

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

Рекомендация по процессору cumulativetodelta

Параметр `max_staleness` [процессора cumulativetodelta﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/cumulativetodeltaprocessor) рекомендуется устанавливать выше, чем частота, с которой Collector получает метрики (например, как часто поступают метрики через OTLP или какова длительность интервала сбора Prometheus). Это гарантирует, что ссылки на заброшенные потоки метрик не будут со временем накапливаться в памяти.

В этом файле YAML настраиваются следующие компоненты:

* OTLP receiver (`otlp`), который может принимать данные через gRPC и HTTP.
* Processor для преобразования любых метрик с кумулятивной темпоральностью в дельта-темпоральность (подробнее см. [Дельта-метрики](#delta-metrics)).
* OTLP HTTP exporter (`otlp_http`), настроенный со следующими параметрами:

  + Эндпоинт Dynatrace, см. [Базовые URL](/managed/ingest-from/opentelemetry/otlp-api#base-url "Узнай об эндпоинтах OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.")
  + Токен API, см. [Аутентификация](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнай об эндпоинтах OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.").

В рамках конфигурации экспортёра `otlp_http` можно также задать `logs_endpoint`, чтобы управлять тем, как Dynatrace обрабатывает структурированные данные логов: сохранять исходную вложенную структуру (raw) или разворачивать её в пути ключей (flattened).
Подробнее см. [Настройка обработки структурированных логов](#structured-logs).

В примере конфигурации выше токен Dynatrace должен иметь разрешения **Ingest OpenTelemetry traces** (`openTelemetryTrace.ingest`), **Ingest metrics** (`metrics.ingest`) и **Ingest logs** (`logs.ingest`).

В разделе service каждый компонент определяется отдельно.

* Extensions можно включать в своём собственном разделе, тогда как receivers, processors и exporters группируются в разделе pipeline.
* Pipeline могут быть типа traces, metrics или logs.
* Каждый receiver/processor/exporter можно использовать более чем в одном pipeline. Для processor'ов, на которые ссылаются несколько pipeline, каждый pipeline получает отдельный экземпляр processor'а. Это отличается от receiver'ов/exporter'ов, на которые ссылаются несколько pipeline: там для всех pipeline используется только один экземпляр receiver'а/exporter'а. Также учти, что порядок processor'ов определяет порядок, в котором обрабатываются данные.
* Одни и те же компоненты можно определять более одного раза. Например, можно иметь два разных receiver'а или даже две и более разных части pipeline.
* Даже если компонент правильно настроен в своём разделе, он не будет включён, пока не будет также определён в разделе service.

## Проверка конфигурации

Важно убедиться, что используемая конфигурация Collector синтаксически и семантически корректна. Например, YAML использует для отступов пробелы (не табуляцию), чтобы определить иерархию документа, и нужно использовать правильный уровень отступа для каждого раздела и компонента. Collector предоставляет встроенную команду `validate` для проверки того, что конфигурация и её компоненты и сервисы настроены правильно.

```
dynatrace-otel-collector validate --config=[PATH_TO_YOUR_CONFIGURATION_FILE]
```

Если используется контейнерный экземпляр Collector, можно также выполнить проверку напрямую из контейнера следующей командой Docker.

```
docker run -v $(pwd):$(pwd) -w $(pwd) ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.52.0 validate --config=[YOUR_CONFIGURATION_FILE]
```

## Дельта-метрики

Dynatrace требует, чтобы данные метрик [отправлялись с дельта-темпоральностью](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#aggregation-temporality "Узнай, как Dynatrace принимает метрики OpenTelemetry и какие ограничения при этом действуют."), а **не** с кумулятивной темпоральностью.

Если приложение не позволяет настроить дельта-темпоральность, можно использовать [процессор `cumulativetodelta`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/cumulativetodeltaprocessor), чтобы экземпляр Collector преобразовывал кумулятивные значения в дельта-значения. [Пример конфигурации](#configuration-example) выше показывает, как настроить процессор и сослаться на него в конфигурации Collector.

## Цепочки и балансировка нагрузки между Collector'ами

При использовании более одного экземпляра Collector важно поддерживать стабильное распространение значений во всех экземплярах.

Это особенно важно, когда запросы OTLP отправляются через разные экземпляры Collector (например, при балансировке нагрузки), поскольку каждый экземпляр Collector отслеживает собственное дельта-смещение, что может нарушить данные, передаваемые бэкенду Dynatrace.

В таких сценариях рекомендуется направлять запросы OTLP через единственный исходящий экземпляр Collector, который пересылает данные в бэкенд Dynatrace и берёт на себя дельта-преобразование. Остальные экземпляры Collector должны использовать кумулятивную агрегацию, чтобы обеспечить стабильное и согласованное распространение значений.

## Настройка обработки структурированных логов

При экспорте структурированных логов в Dynatrace, Dynatrace обрабатывает данные логов одним из двух способов.
Он либо:

* Сохраняет исходную вложенную структуру из источника логов ("raw").
* Разворачивает её так, чтобы все значения атрибутов лога были доступны через пути ключей ("flattened").

Чтобы настроить это поведение, используй параметр `logs_endpoint`, как показано в примере ниже:

```
exporters:



otlp_http:



endpoint: "${env:DT_ENDPOINT}"



logs_endpoint: "${env:DT_ENDPOINT}/v1/logs?structure=raw"



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"
```

Обязательно указывай полный путь эндпоинта API, включая `/v1/logs` (переменные окружения допустимы), после чего указывай нужное поведение.

* Чтобы сохранить исходную вложенную структуру, используй `structure=raw`.
* Чтобы развернуть данные логов, используй `structure=flattened`.

Подробнее см. [Обработка данных при приёме логов через API](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs#otlp-structured-logs "Узнай, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения при этом действуют.").

Если этот параметр конфигурации не указан, поведение по умолчанию зависит от того, когда было создано окружение.

* Для Dynatrace версии 1.331+ и окружений, созданных после 1 февраля 2026 г.: Raw.
* Для окружений, созданных до 1 февраля 2026 г.: Flattened.