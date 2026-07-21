---
title: Пакетная отправка запросов OTLP с помощью OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/batch
---

# Пакетная отправка запросов OTLP с помощью OTel Collector

# Пакетная отправка запросов OTLP с помощью OTel Collector

* Практическое руководство
* Чтение 3 мин
* Обновлено 11 мая 2026 г.

Пример конфигурации ниже показывает, как настроить экземпляр Collector и экспортёр `otlp_http` для постановки запросов OTLP в очередь и их пакетной отправки, чтобы повысить производительность пропускной способности.

Рекомендуемая конфигурация

Для оптимальной производительности экземпляра Collector рекомендуется настраивать
пакетирование во всех развёртываниях примерно так, как показано ниже. Значения в
приведённом примере конфигурации хорошо подходят для большинства данных, но
рекомендуется определить оптимальные настройки для конкретной ситуации.

## Предварительные требования

* Дистрибутив Collector:

  + [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + Дистрибутив OpenTelemetry [Core](/managed/ingest-from/opentelemetry/collector#collector-core "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.") или [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [Пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* [URL конечной точки Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте про конечные точки OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.") для экспорта данных
* [Токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте про конечные точки OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate)

О настройке Collector с конфигурацией ниже см. [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.") и [Конфигурация Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector.").

## Демонстрационная конфигурация

```
receivers:



otlp:



protocols:



grpc:



endpoint: 0.0.0.0:4317



http:



endpoint: 0.0.0.0:4318



exporters:



otlp_http/traces:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



sending_queue:



batch:



min_size: 5000



max_size: 5000



flush_timeout: 60s



otlp_http/metrics:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



sending_queue:



batch:



min_size: 3000



max_size: 3000



flush_timeout: 60s



otlp_http/logs:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



sending_queue:



batch:



min_size: 1800



max_size: 2000



flush_timeout: 60s



service:



pipelines:



traces:



receivers: [otlp]



exporters: [otlp_http/traces]



metrics:



receivers: [otlp]



exporters: [otlp_http/metrics]



logs:



receivers: [otlp]



exporters: [otlp_http/logs]
```

Проверка конфигурации

[Проверьте настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector.") во избежание проблем с конфигурацией.

## Компоненты

В этой конфигурации настроены следующие компоненты.

### Receivers (приёмники)

В разделе `receivers` указан стандартный приёмник `otlp` как активный компонент-приёмник для экземпляра Collector.

Это сделано в демонстрационных целях. Здесь можно указать любой другой допустимый приёмник (например, `zipkin`).

### Exporters (экспортёры)

В разделе `exporters` указан [экспортёр `otlp_http`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter) для каждого сигнала, настроенный с соответствующими параметрами пакетирования, а также URL Dynatrace API и требуемым токеном аутентификации.

Для этого задаются следующие две переменные окружения, на которые есть ссылки в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL конечной точки Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте про конечные точки OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте про конечные точки OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

В разделе `sending_queue` конфигурации экспортёра указан отдельный [раздел `batch`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/exporterhelper#sending-queue-batch-settings)
для каждого сигнала телеметрии со следующими параметрами:

* `min_size`: задаёт минимальное количество записей, которое процессор поставит в очередь перед отправкой всего пакета.
* `max_size`: задаёт максимальное количество записей, которое может содержать пакет. Большее количество записей разобьёт крупный пакет на более мелкие.
* `timeout`: определяет промежуток времени, по истечении которого пакет будет отправлен. Пакет отправляется по истечении `timeout` только в том случае, если условие `send_batch_size` не выполнено.

При такой конфигурации OTel Collector ставит записи телеметрии в очередь пакетами, обеспечивая хороший баланс между размером и количеством запросов экспорта
к API Dynatrace.

Значения размера пакета

На итоговый размер пакета влияет не только количество отдельных записей телеметрии,
но и количество связанных с ними атрибутов и их размер.

Например, атрибуты span'ов/метрик/логов могут сделать пакет с тем же количеством записей больше,
в зависимости от того, сколько атрибутов и насколько они велики.

Используйте приведённые выше значения конфигурации как отправную точку, но обязательно адаптируйте их под свой объём данных
и соблюдайте ограничения API Dynatrace для каждого типа сигнала ([трейсы](/managed/ingest-from/opentelemetry/otlp-api/ingest-traces#ingestion-limits "Узнайте, как Dynatrace принимает трейсы OpenTelemetry и какие ограничения применяются."),
[метрики](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#limits "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются."), [логи](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs#ingestion-limits "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения применяются.")), чтобы избежать отклонения запросов.

Для устранения проблем с отклонёнными запросами можно использовать [метрики самомониторинга ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-sfm-metrics#rest "Изучите метрики самомониторинга ActiveGate.").
Например, можно использовать `dsfm:active_gate.rest.request_count` с фильтрацией по измерению `operation`
(`POST /otlp/v1/<...>` для приёма OTLP) и разбивкой по `response_code`. Крупные запросы отклоняются с кодом состояния HTTP `413`.

Другой вариант, это проверка логов Collector на предмет сообщений об ошибках вида: `HTTP Status Code 413, Message=Max Payload size of`.

### Конвейеры служб

В разделе `service` объекты приёмника и экспортёра собираются в конвейеры для трейсов, метрик и логов.

## Ограничения

Данные принимаются с использованием протокола OpenTelemetry (OTLP) через [APIы OTLP Dynatrace](/managed/ingest-from/opentelemetry/otlp-api "Узнайте про конечные точки OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.") и подчиняются ограничениям и правилам API.
Подробнее см.:

* [Ограничения метрик OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")
* [Сопоставление метрик Dynatrace](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")
* [Приём логов OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения применяются.")

## Похожие темы

* [Обогащение принятых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.")
* [Обогащение запросов OTLP данными Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Настройте OpenTelemetry Collector для обогащения запросов OTLP данными Kubernetes.")