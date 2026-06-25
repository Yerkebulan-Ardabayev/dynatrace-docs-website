---
title: Применение ограничений памяти к OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/memory
scraped: 2026-05-12T12:11:03.995208
---

# Применение ограничений памяти к OTel Collector

# Применение ограничений памяти к OTel Collector

* Практическое руководство
* Чтение: 2 мин
* Обновлено 08 января 2026 г.

В следующем примере конфигурации показано, как настроить экземпляр Collector и его встроенный processor memory_limiter, чтобы гарантировать, что выделение памяти остаётся в пределах указанных параметров.

Рекомендуемая конфигурация

Для оптимального использования памяти вашим экземпляром Collector мы рекомендуем
применять эту конфигурацию в большинстве контейнеризированных установок. Дополнительные сведения см. в разделе о
[вопросах развёртывания](#deployment-considerations).

## Предварительные требования

* Один из следующих дистрибутивов Collector с [processor memory limiter](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/processor/memorylimiterprocessor):

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + OpenTelemetry [Core](/managed/ingest-from/opentelemetry/collector#collector-core "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.") или [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
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



memory_limiter:



check_interval: 1s



limit_percentage: 90



spike_limit_percentage: 20



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



traces:



receivers: [otlp]



processors: [memory_limiter]



exporters: [otlp_http]



metrics:



receivers: [otlp]



processors: [memory_limiter]



exporters: [otlp_http]



logs:



receivers: [otlp]



processors: [memory_limiter]



exporters: [otlp_http]
```

Проверка конфигурации

[Проверьте ваши настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

Для нашей конфигурации мы настраиваем следующие компоненты.

### Receivers

В разделе `receivers` мы указываем стандартный receiver `otlp` в качестве активного компонента receiver для нашего экземпляра Collector.

Это сделано в основном в демонстрационных целях. Здесь можно указать любой другой допустимый receiver (например, `zipkin`).

### Processors

В разделе `processors` мы указываем [processor `memory_limiter`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/processor/memorylimiterprocessor) со следующими параметрами:

* `check_interval` настроен на проверку состояния памяти каждую секунду
* `limit_percentage` настроен на разрешение максимального выделения памяти в 90 процентов
* `spike_limit_percentage` настроен на разрешение максимального пикового использования памяти в 20 процентов

При такой конфигурации OTel Collector проверяет выделение памяти каждую секунду
и начинает применять давление с помощью отдельных механизмов после достижения следующих
пределов:

* Мягкий предел (`limit_percentage - spike_limit_percentage`): после достижения этого предела
  processor отклоняет полезные нагрузки, пока использование памяти не опустится ниже предела.
  Отправка надлежащих сообщений об отклонении возлагается на receiver, расположенный выше processor
  по конвейеру.
* Жёсткий предел: (`limit_percentage`): после достижения этого предела processor
  принудительно запускает сборку мусора, пока использование памяти не опустится ниже предела. Данные
  продолжают отклоняться, пока использование не опустится ниже мягкого предела.

В дополнение к processor memory limiter мы настоятельно рекомендуем задать
переменной окружения `GOMEMLIMIT` значение, равное 80% от жёсткого предела. Обратите внимание, что
для `GOMEMLIMIT` требуется задавать абсолютное значение в байтах. Например, можно
задать `GOMEMLIMIT=1024MiB`, чтобы начать увеличивать частоту циклов сборки
мусора, когда Collector достигает 1024 МиБ памяти, используемой в куче Go
VM. Дополнительные сведения см. в [документации пакета Go
](https://pkg.go.dev/runtime#hdr-Environment_Variables), описывающей
работу этой переменной окружения.

#### Вопросы развёртывания

В контейнеризированных средах или других случаях, когда хост-среда задаёт
максимально допустимый объём памяти Collector, мы рекомендуем использовать параметры
`limit_percentage` и `spike_limit_percentage`.

Для развёртываний на виртуальных машинах или физических серверах, где Collector не
получает явную квоту памяти, мы вместо этого рекомендуем использовать параметры `limit_mib` и
`spike_limit_mib`.

### Exporters

В разделе `exporters` мы указываем стандартный [exporter `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) и настраиваем его с помощью URL нашего Dynatrace API и необходимого токена аутентификации.

Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Сервисные конвейеры

В разделе `service` мы собираем наши объекты receiver и exporter в конвейеры для трассировок, метрик и логов и включаем наш processor memory limiter, ссылаясь на него в разделе `processors` для каждого соответствующего конвейера.

## Пределы и ограничения

Данные принимаются с помощью протокола OpenTelemetry (OTLP) через [Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") и подчиняются ограничениям и лимитам этого API.
Дополнительные сведения см.:

* [Ограничения метрик OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")
* [Сопоставление метрик Dynatrace](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")
* [Приём логов OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения применяются.")

## Связанные темы

* [Обогащение принимаемых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.")
* [Обогащение запросов OTLP данными Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Настройте OpenTelemetry Collector для обогащения запросов OTLP данными Kubernetes.")