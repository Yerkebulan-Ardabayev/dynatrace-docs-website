---
title: Семплирование с OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/sampling
scraped: 2026-03-04T21:37:07.307900
---

# Сэмплирование с OpenTelemetry Collector


* Latest Dynatrace
* How-to guide
* 5 мин. чтения
* Опубликовано 28 мая 2024

Распределённое приложение под высокой нагрузкой может генерировать огромный объём данных наблюдаемости. Эти данные влекут за собой затраты на генерацию, обработку, передачу и хранение. Однако часто можно использовать сэмплирование — когда вы используете лишь относительно небольшую часть данных наблюдаемости, а остальные отбрасываете — для снижения затрат при сохранении эффективного мониторинга вашего приложения.

В OpenTelemetry существует два основных метода сэмплирования:

* **Сэмплирование на входе (Head sampling)** выполняется внутри вашего приложения с помощью OpenTelemetry SDK и обычно включает сохранение случайной выборки транзакций.

  Сэмплирование на входе простое и эффективное, но имеет важные ограничения. Например, поскольку решение о сэмплировании должно быть принято в начале транзакции, оно не может учитывать ничего, что произойдёт после этого момента.
* **Сэмплирование на выходе (Tail sampling)** используется для принятия решений о сэмплировании на основе информации, неизвестной в начале транзакции.

  В OpenTelemetry сэмплирование на выходе обычно выполняется с помощью Collector путём временного хранения полного набора данных мониторинга до завершения транзакции. Затем Collector решает, сохранить или отбросить данные транзакции на основе набора политик сэмплирования.

  Поскольку сэмплирование на выходе обычно не является случайным, важно убедиться, что любые вычисляемые метрики не искажены. Это можно сделать, вычисляя метрики из полного набора транзакций, как показано ниже, или из отдельного, случайно сэмплированного потока.

Следующий пример конфигурации показывает, как настроить экземпляр Collector для сэмплирования данных трассировки и их импорта в Dynatrace в качестве OTLP-запроса. Он использует [коннектор `spanmetrics`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/connector/spanmetricsconnector) для вычисления метрик сервисов из трассировок перед сэмплированием, чтобы обеспечить их точность.

## Предварительные требования

* Один из следующих дистрибутивов Collector с процессорами [`transform`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/transformprocessor), [`filter`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/filterprocessor) и [`tail_sampling`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/tailsamplingprocessor), а также коннектором [`spanmetrics`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/connector/spanmetricsconnector):

  + [Dynatrace Collector](../../collector.md#dt-collector-dist "Узнайте о Dynatrace OTel Collector.")
  + Дистрибутив OpenTelemetry [Contrib](../../collector.md#collector-contrib "Узнайте о Dynatrace OTel Collector.")
  + [Пользовательская сборка через Builder](../../collector.md#collector-builder "Узнайте о Dynatrace OTel Collector.")
* [URL конечной точки Dynatrace API](../../otlp-api.md "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."), куда должны экспортироваться данные
* [API-токен](../../otlp-api.md#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate)

См. [Развёртывание Collector](../deployment.md "Как развернуть Dynatrace OTel Collector.") и [Конфигурация Collector](../configuration.md "Как настроить OpenTelemetry Collector.") для настройки вашего Collector с приведённой ниже конфигурацией.

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

[Проверьте ваши настройки](../configuration.md#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

Для нашей конфигурации мы настраиваем следующие компоненты.

### Приёмники (Receivers)

В разделе `receivers` мы указываем стандартный приёмник `otlp` как активный компонент приёмника для нашего экземпляра Collector и настраиваем его для приёма OTLP-запросов по gRPC и HTTP.

### Процессоры (Processors)

* [`tail_sampling`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/tailsamplingprocessor) для сэмплирования распределённых трассировок на основе свойств трассировки.

### Коннекторы (Connectors)

В разделе `connectors` мы указываем [коннектор `spanmetrics`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/connector/spanmetricsconnector) для вычисления метрик сервисов из спанов.

### Экспортёры (Exporters)

В разделе `exporters` мы указываем стандартный [экспортёр `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) и настраиваем его с нашим URL Dynatrace API и необходимым токеном аутентификации.

Для этого мы устанавливаем следующие две переменные среды и ссылаемся на них в значениях конфигурации для `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL конечной точки Dynatrace API](../../otlp-api.md#export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [API-токен](../../otlp-api.md#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Конвейеры сервисов (Service pipelines)

В разделе `service` мы собираем три конвейера:

* `traces` объединяет приёмник OTLP, процессор сэмплирования на выходе и экспортёр `otlp_http` для отправки сэмплированных спанов в Dynatrace.
* `traces/spanmetrics` использует тот же приёмник OTLP и коннектор `spanmetrics` для вычисления метрик сервисов из полученных спанов без сэмплирования и пересылает вычисленные метрики в `metrics`.
* `metrics` использует процессоры `transform`, `filter` и `transform/spanmetrics` для форматирования метрик для загрузки метрик Dynatrace перед отправкой метрик в Dynatrace с помощью экспортёра `otlp_http`.

## Особенности сэмплирования OpenTelemetry

### Смешанный режим сэмплирования

OpenTelemetry и OneAgent используют несовместимые подходы к сэмплированию, которые не следует смешивать. Если распределённая трассировка, которая может включать несколько приложений и сервисов, лишь частично использует один из методов, это, вероятно, приведёт к несогласованным результатам и неполным распределённым трассировкам. Каждая распределённая трассировка должна сэмплироваться только одним из методов, чтобы обеспечить её полный захват.

### Метрики сервисов, производные от трассировок

Метрики Dynatrace, производные от трассировок, вычисляются из данных трассировок после их загрузки в Dynatrace.

Если трассировки OpenTelemetry сэмплируются, метрики, производные от трассировок, вычисляются только из сэмплированного подмножества данных трассировок. Это означает, что некоторые метрики, производные от трассировок, могут быть искажены или некорректны.

Например, вероятностный сэмплер, сохраняющий 5% трафика, приведёт к метрике пропускной способности, показывающей 5% от фактической пропускной способности. Если вы используете сэмплирование OpenTelemetry на выходе для дополнительного захвата 100% медленных или ошибочных трассировок, метрики ваших сервисов будут не только показывать некорректную пропускную способность, но и некорректно искажать показатели ошибок и времени отклика.

Для смягчения этой проблемы, если вы хотите сэмплировать трассировки OpenTelemetry, вам следует вычислять метрики сервисов до сэмплирования и использовать эти метрики вместо метрик, производных от трассировок, вычисляемых Dynatrace. Если вы используете Collector для сэмплирования, метрики, производные от трассировок, должны вычисляться Collector до применения сэмплирования или SDK. Это можно сделать с помощью [коннектора `spanmetrics`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/connector/spanmetricsconnector), как показано в примере выше.

## Лимиты и ограничения

Данные загружаются с использованием протокола OpenTelemetry (OTLP) через [Dynatrace OTLP API](../../otlp-api.md "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") и подчиняются лимитам и ограничениям API.
Подробнее см.:

* [Ограничения метрик OpenTelemetry](../../otlp-api/ingest-otlp-metrics/about-metrics-ingest.md "Узнайте, как Dynatrace загружает метрики OpenTelemetry и какие ограничения применяются.")
* [Сопоставление метрик Dynatrace](../../otlp-api/ingest-otlp-metrics/about-metrics-ingest.md#dynatrace-mapping "Узнайте, как Dynatrace загружает метрики OpenTelemetry и какие ограничения применяются.")
* [Загрузка логов OpenTelemetry](../../otlp-api/ingest-logs.md "Узнайте, как Dynatrace загружает записи логов OpenTelemetry и какие ограничения применяются.")

## Связанные темы

* [Пакетная обработка OTLP-запросов с OpenTelemetry Collector](batch.md "Настройте OpenTelemetry Collector для отправки данных пакетами на бэкенд Dynatrace.")
* [Вычисление сводок гистограмм с OpenTelemetry Collector](histograms.md "Настройте OpenTelemetry Collector для вычисления сводок гистограмм.")
* [Применение лимитов памяти к OpenTelemetry Collector](memory.md "Настройте OpenTelemetry Collector для соблюдения лимитов памяти и предотвращения чрезмерного использования системных ресурсов.")
* [Отправка данных OpenTelemetry на несколько бэкендов](multi-export.md "Настройте OpenTelemetry Collector для отправки данных на более чем один бэкенд.")