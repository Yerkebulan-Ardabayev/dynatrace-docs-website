---
title: Сэмплирование с помощью OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/sampling
scraped: 2026-05-12T12:10:56.212832
---

# Сэмплирование с помощью OTel Collector

# Сэмплирование с помощью OTel Collector

* Практическое руководство
* Чтение: 5 мин
* Опубликовано 28 мая 2024 г.

Распределённое приложение под высокой нагрузкой может генерировать огромный объём данных наблюдаемости. Эти данные влекут затраты на генерацию, обработку, передачу и хранение. Однако зачастую можно использовать сэмплирование, при котором используется лишь относительно небольшая часть данных наблюдаемости, а остальные отбрасываются, чтобы сократить затраты и при этом эффективно отслеживать ваше приложение.

В OpenTelemetry есть два основных метода сэмплирования:

* **Сэмплирование на входе (head sampling)** выполняется внутри вашего приложения с помощью OpenTelemetry SDK и обычно заключается в сохранении случайной выборки транзакций.

  Сэмплирование на входе простое и эффективное, но у него есть важные ограничения. Например, поскольку решение о сэмплировании нужно принимать в начале транзакции, на него не может повлиять ничего из того, что происходит после этого момента.
* **Сэмплирование на выходе (tail sampling)** используется для принятия решений о сэмплировании на основе информации, неизвестной в начале транзакции.

  В OpenTelemetry сэмплирование на выходе обычно выполняется с помощью OTel Collector путём временного хранения полного набора данных мониторинга до завершения транзакции. Затем Collector решает, сохранить или отбросить данные транзакции, на основе набора политик сэмплирования.

  Поскольку сэмплирование на выходе обычно не случайно, важно убедиться, что любые вычисляемые метрики несмещённые. Этого можно добиться, вычисляя метрики из полного набора транзакций, как показано ниже, или из отдельного, случайно сэмплированного потока.

В следующем примере конфигурации показано, как настроить экземпляр Collector для сэмплирования данных трассировок и их импорта в виде запроса OTLP в Dynatrace. В нём используется [connector `spanmetrics`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/connector/spanmetricsconnector) для вычисления метрик сервисов из трассировок до сэмплирования, чтобы обеспечить их точность.

## Предварительные требования

* Один из следующих дистрибутивов Collector с processor `transform` ([`transform`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor)), `filter` ([`filter`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/filterprocessor)) и `tail_sampling` ([`tail_sampling`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/tailsamplingprocessor)), а также connector `spanmetrics` ([`spanmetrics`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/connector/spanmetricsconnector)):

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + Дистрибутив OpenTelemetry [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* [URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."), на который должны экспортироваться данные
* [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate)

См. [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.") и [Настройку Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector."), чтобы узнать, как настроить ваш Collector с приведённой ниже конфигурацией.

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

Проверка конфигурации

[Проверьте ваши настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

Для нашей конфигурации мы настраиваем следующие компоненты.

### Receivers

В разделе `receivers` мы указываем стандартный receiver `otlp` в качестве активного компонента receiver для нашего экземпляра Collector и настраиваем его на приём запросов OTLP по gRPC и HTTP.

### Processors

* [`tail_sampling`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/tailsamplingprocessor) для сэмплирования распределённых трассировок на основе свойств трассировки.

### Connectors

В разделе `connectors` мы указываем [connector `spanmetrics`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/connector/spanmetricsconnector) для вычисления метрик сервисов из спанов.

### Exporters

В разделе `exporters` мы указываем стандартный [exporter `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) и настраиваем его с помощью URL нашего Dynatrace API и необходимого токена аутентификации.

Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Сервисные конвейеры

В разделе `service` мы собираем три конвейера:

* `traces` собирает receiver OTLP, processor сэмплирования на выходе и exporter `otlp_http` для отправки сэмплированных спанов в Dynatrace.
* `traces/spanmetrics` использует тот же receiver OTLP и connector `spanmetrics` для вычисления метрик сервисов из полученных спанов без сэмплирования и пересылает вычисленные метрики в `metrics`.
* `metrics` использует processor `transform`, `filter` и `transform/spanmetrics` для форматирования метрик под приём метрик Dynatrace перед отправкой метрик в Dynatrace с помощью exporter `otlp_http`.

## Особенности сэмплирования OpenTelemetry

### Смешанный режим сэмплирования

OpenTelemetry и OneAgent используют несовместимые подходы к сэмплированию, которые не следует смешивать. Если распределённая трассировка, которая может включать несколько приложений и сервисов, лишь частично использует тот или иной метод, это, скорее всего, приведёт к несогласованным результатам и неполным распределённым трассировкам. Каждая распределённая трассировка должна сэмплироваться только одним из методов, чтобы гарантировать её захват целиком.

### Метрики сервисов, производные от трассировок

Производные от трассировок метрики Dynatrace вычисляются из данных трассировок после их приёма в Dynatrace.

Если трассировки OpenTelemetry сэмплируются, производные от трассировок метрики вычисляются только из сэмплированного подмножества данных трассировок. Это означает, что некоторые производные от трассировок метрики могут быть смещёнными или неверными.

Например, вероятностный сэмплер, сохраняющий 5% трафика, даст метрику пропускной способности, показывающую 5% фактической пропускной способности. Если использовать сэмплирование OpenTelemetry на выходе, чтобы дополнительно захватывать 100% медленных или ошибочных трассировок, метрики сервисов не только покажут неверную пропускную способность, но и внесут некорректное смещение в доли ошибок и время отклика.

Чтобы смягчить это, при сэмплировании трассировок OpenTelemetry следует вычислять метрики сервисов до сэмплирования и использовать эти метрики вместо производных от трассировок метрик, вычисляемых Dynatrace. Если для сэмплирования используется Collector, производные от трассировок метрики должны вычисляться Collector до применения сэмплирования или с помощью SDK. Этого можно добиться с помощью [connector `spanmetrics`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/connector/spanmetricsconnector), как показано в примере выше.

## Пределы и ограничения

Данные принимаются с помощью протокола OpenTelemetry (OTLP) через [Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") и подчиняются ограничениям и лимитам этого API.
Дополнительные сведения см.:

* [Ограничения метрик OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")
* [Сопоставление метрик Dynatrace](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")
* [Приём логов OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения применяются.")

## Связанные темы

* [Группирование запросов OTLP с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/batch "Настройте OpenTelemetry Collector для отправки данных группами в бэкенд Dynatrace.")
* [Вычисление сводок гистограмм с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/histograms "Настройте OpenTelemetry Collector для вычисления сводок гистограмм.")
* [Применение ограничений памяти к OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/memory "Настройте OpenTelemetry Collector для соблюдения ограничений памяти и предотвращения чрезмерного использования системных ресурсов.")
* [Отправка данных OpenTelemetry в несколько бэкендов](/managed/ingest-from/opentelemetry/collector/use-cases/multi-export "Настройте OpenTelemetry Collector для отправки данных более чем в один бэкенд.")