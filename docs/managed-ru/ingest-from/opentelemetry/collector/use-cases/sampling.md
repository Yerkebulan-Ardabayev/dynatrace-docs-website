---
title: Сэмплирование с OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/sampling
---

# Сэмплирование с OTel Collector

# Сэмплирование с OTel Collector

* Практическое руководство
* Чтение 5 мин
* Опубликовано 28 мая 2024

Распределённое приложение под высокой нагрузкой может генерировать огромный объём данных наблюдаемости. Эти данные влекут расходы на генерацию, обработку, передачу и хранение. Однако часто можно использовать сэмплирование (когда используется лишь относительно небольшая часть данных наблюдаемости, а остальное отбрасывается), чтобы снизить расходы и при этом эффективно мониторить приложение.

В OpenTelemetry есть два основных метода сэмплирования:

* **Head sampling** выполняется внутри приложения SDK OpenTelemetry и обычно заключается в сохранении случайной выборки транзакций.

  Head sampling прост и эффективен, но имеет важные ограничения. Например, поскольку решение о сэмплировании нужно принять в начале транзакции, на него не может повлиять ничего из того, что происходит позже.
* **Tail sampling** используется для принятия решений о сэмплировании на основе информации, неизвестной в начале транзакции.

  В OpenTelemetry tail sampling обычно выполняется с помощью OTel Collector: он временно хранит полный набор данных мониторинга до завершения транзакции. Затем Collector решает, сохранить данные транзакции или отбросить их, на основе набора политик сэмплирования.

  Поскольку tail sampling обычно не случаен, важно убедиться, что любые вычисляемые метрики не смещены. Этого можно добиться, вычисляя метрики из полного набора транзакций (как показано ниже) или из отдельного, случайно сэмплированного потока.

Следующий пример конфигурации показывает, как настроить экземпляр Collector для сэмплирования данных трассировки и импорта их как OTLP-запроса в Dynatrace. Он использует [коннектор `spanmetrics`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/connector/spanmetricsconnector) для вычисления метрик сервисов из трассировок до сэмплирования, чтобы обеспечить их точность.

## Предварительные условия

* Один из следующих дистрибутивов Collector с процессорами [`transform`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/transformprocessor), [`filter`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/filterprocessor) и [`tail_sampling`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/tailsamplingprocessor), а также коннектором [`spanmetrics`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/connector/spanmetricsconnector):

  + [OTel Collector от Dynatrace](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая OTel Collector от Dynatrace, для приёма телеметрии из OpenTelemetry.")
  + Дистрибутив OpenTelemetry [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая OTel Collector от Dynatrace, для приёма телеметрии из OpenTelemetry.")
  + [Кастомная версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая OTel Collector от Dynatrace, для приёма телеметрии из OpenTelemetry.")
* [URL конечной точки Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте про конечные точки OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace."), в которую нужно экспортировать данные
* [Токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте про конечные точки OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate)

О том, как настроить Collector с указанной ниже конфигурацией, читайте в разделах [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть OpenTelemetry Collector от Dynatrace.") и [Конфигурация Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector.").

## Демонстрационная конфигурация

```
receivers:



otlp:



protocols:



grpc:



endpoint: 0.0.0.0:4317



http:



endpoint: 0.0.0.0:4318



processors:



tail_sampling:



# This configuration keeps errors, traces longer than 500ms, and 20% of all remaining traces.



# Adjust with policies of your choice.



policies:



- name: policy1-keep-errors



type: status_code



status_code: {status_codes: [ERROR, UNSET]}



- name: policy2-keep-slow-traces



type: latency



latency: {threshold_ms: 500}



- name: policy3-keep-random-sample



type: probabilistic



probabilistic: {sampling_percentage: 20}



decision_wait: 30s



connectors:



spanmetrics:



aggregation_temporality: "AGGREGATION_TEMPORALITY_DELTA"



namespace: "requests"



metrics_flush_interval: 15s



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: Api-Token ${env:DT_API_TOKEN}



service:



pipelines:



traces:



receivers: [otlp]



processors: [tail_sampling]



exporters: [otlp_http]



traces/spanmetrics:



receivers: [otlp]



processors: []



exporters: [spanmetrics]



metrics:



receivers: [spanmetrics]



processors: []



exporters: [otlp_http]
```

Валидация конфигурации

[Проверьте настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

В нашей конфигурации настроены следующие компоненты.

### Receivers (приёмники)

В разделе `receivers` указан стандартный приёмник `otlp` в качестве активного компонента-приёмника для экземпляра Collector, настроенный на приём OTLP-запросов по gRPC и HTTP.

### Processors (процессоры)

* [`tail_sampling`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/tailsamplingprocessor) для сэмплирования распределённых трассировок на основе свойств трассировки.

### Connectors (коннекторы)

В разделе `connectors` указан [коннектор `spanmetrics`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/connector/spanmetricsconnector) для вычисления метрик сервисов из спанов.

### Exporters (экспортёры)

В разделе `exporters` указан стандартный [экспортёр `otlp_http`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter), настроенный с URL API Dynatrace и требуемым токеном аутентификации.

Для этого заданы следующие две переменные окружения, на которые есть ссылки в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL конечной точки API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте про конечные точки OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте про конечные точки OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Пайплайны сервиса

В разделе `service` собраны три пайплайна:

* `traces` объединяет приёмник OTLP, процессор tail sampling и экспортёр `otlp_http`, чтобы отправлять сэмплированные спаны в Dynatrace.
* `traces/spanmetrics` использует тот же приёмник OTLP и коннектор `spanmetrics` для вычисления метрик сервисов из полученных спанов без сэмплирования и передаёт вычисленные метрики в `metrics`.
* `metrics` использует процессоры `transform`, `filter` и `transform/spanmetrics` для форматирования метрик под приём метрик Dynatrace перед отправкой метрик в Dynatrace с помощью экспортёра `otlp_http`.

## Особенности сэмплирования OpenTelemetry

### Смешанный режим сэмплирования

OpenTelemetry и OneAgent используют несовместимые подходы к сэмплированию, которые не следует смешивать. Если распределённая трассировка, которая может включать несколько приложений и сервисов, лишь частично использует один из методов, это, вероятно, приведёт к противоречивым результатам и неполным распределённым трассировкам. Каждую распределённую трассировку следует сэмплировать только одним из методов, чтобы гарантировать её захват целиком.

### Метрики сервисов, производные от трассировок

Производные от трассировок метрики Dynatrace вычисляются из данных трассировки после их приёма в Dynatrace.

Если трассировки OpenTelemetry сэмплируются, производные от трассировок метрики вычисляются только из сэмплированного подмножества данных трассировки. Это значит, что некоторые производные от трассировок метрики могут быть смещены или некорректны.

Например, вероятностный сэмплер, сохраняющий 5% трафика, приведёт к тому, что метрика пропускной способности покажет 5% от фактической пропускной способности. Если также использовать tail-based сэмплирование OpenTelemetry для захвата 100% медленных трассировок или трассировок с ошибками, метрики сервиса не только покажут некорректную пропускную способность, но и некорректно сместят частоту ошибок и время отклика.

Чтобы это смягчить, при сэмплировании трассировок OpenTelemetry метрики сервисов следует вычислять до сэмплирования и использовать эти метрики вместо производных от трассировок метрик, вычисляемых Dynatrace. При использовании Collector для сэмплирования производные от трассировок метрики должны вычисляться Collector'ом до применения сэмплирования, либо SDK. Это можно сделать с помощью [коннектора `spanmetrics`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/connector/spanmetricsconnector), как показано в примере выше.

## Ограничения и лимиты

Данные принимаются с использованием протокола OpenTelemetry (OTLP) через [Dynatrace OTLP APIs](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") и подчиняются лимитам и ограничениям API.
Подробнее см.:

* [Ограничения метрик OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Сопоставление метрик Dynatrace](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Приём логов OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")

## Похожие темы

* [Пакетная отправка запросов OTLP через OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/batch "Configure the OpenTelemetry Collector to send data in batches to the Dynatrace backend.")
* [Вычисление сводок гистограмм с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/histograms "Configure the OpenTelemetry Collector to compute histogram summaries.")
* [Применение ограничений памяти к OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/memory "Configure the OpenTelemetry Collector to respect memory limits and not use excessive system resources.")
* [Отправка данных OpenTelemetry в несколько бэкендов](/managed/ingest-from/opentelemetry/collector/use-cases/multi-export "Configure the OpenTelemetry Collector to send data to more than one backend.")