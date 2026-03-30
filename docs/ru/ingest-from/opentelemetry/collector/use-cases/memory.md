---
title: Применение ограничений памяти к OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/memory
scraped: 2026-03-02T21:22:50.574157
---

Следующий пример конфигурации показывает, как настроить экземпляр Collector и его встроенный процессор ограничения памяти (memory limiter processor), чтобы гарантировать, что выделение памяти остаётся в заданных параметрах.

Рекомендуемая конфигурация

Для оптимального использования памяти вашим экземпляром Collector мы рекомендуем
применять эту конфигурацию в большинстве контейнерных развёртываний. Подробнее
см. раздел [Особенности развёртывания](#deployment-considerations).

## Предварительные требования

* Один из следующих дистрибутивов Collector с [процессором ограничения памяти (memory limiter processor)](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/processor/memorylimiterprocessor):

  + [Dynatrace Collector](../../collector.md#dt-collector-dist "Узнайте о Dynatrace OTel Collector.")
  + OpenTelemetry [Core](../../collector.md#collector-core "Узнайте о Dynatrace OTel Collector.") или [Contrib](../../collector.md#collector-contrib "Узнайте о Dynatrace OTel Collector.")
  + [Пользовательская версия Builder](../../collector.md#collector-builder "Узнайте о Dynatrace OTel Collector.")
* URL конечной точки API Dynatrace, куда должны экспортироваться данные
* [API-токен](../../otlp-api.md#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа (требуется для ActiveGate)

Подробнее о настройке Collector с приведённой ниже конфигурацией см. Развёртывание Collector и Конфигурация Collector.

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

Валидация конфигурации

[Проверьте ваши настройки](../configuration.md#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

Для нашей конфигурации мы настраиваем следующие компоненты.

### Приёмники (Receivers)

В разделе `receivers` мы указываем стандартный приёмник `otlp` в качестве активного компонента приёма для нашего экземпляра Collector.

Это сделано в основном для демонстрации. Здесь можно указать любой другой допустимый приёмник (например, `zipkin`).

### Процессоры (Processors)

В разделе `processors` мы указываем [процессор `memory_limiter`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/processor/memorylimiterprocessor) со следующими параметрами:

* `check_interval` настроен на проверку состояния памяти каждую секунду
* `limit_percentage` настроен на максимально допустимое выделение памяти 90 процентов
* `spike_limit_percentage` настроен на максимально допустимый пиковый расход памяти 20 процентов

С этой конфигурацией Collector проверяет выделение памяти каждую секунду
и начинает применять ограничения с помощью отдельных механизмов после достижения следующих
лимитов:

* Мягкий лимит (`limit_percentage - spike_limit_percentage`): после достижения этого лимита
  процессор отклоняет полезные нагрузки до тех пор, пока использование памяти не опустится ниже лимита.
  Вышестоящий приёмник отвечает за отправку соответствующих
  сообщений об отклонении.
* Жёсткий лимит (`limit_percentage`): после достижения этого лимита процессор
  принудительно запускает сборку мусора до тех пор, пока использование памяти не опустится ниже лимита. Данные
  будут продолжать отклоняться до тех пор, пока использование не опустится ниже мягкого лимита.

Помимо процессора ограничения памяти, мы настоятельно рекомендуем установить
переменную окружения `GOMEMLIMIT` на значение, равное 80% от жёсткого лимита. Обратите внимание, что
для `GOMEMLIMIT` необходимо задать абсолютное значение в байтах. Например, вы
можете установить `GOMEMLIMIT=1024MiB`, чтобы увеличить частоту циклов сборки
мусора, когда Collector достигнет 1024 МиБ используемой памяти в куче Go
VM. Подробнее см. [документацию пакета
Go](https://pkg.go.dev/runtime#hdr-Environment_Variables), описывающую
работу этой переменной окружения.

#### Особенности развёртывания

В контейнерных средах или других местах, где среда хоста устанавливает
максимально допустимый объём памяти для Collector, мы рекомендуем использовать
параметры `limit_percentage` и `spike_limit_percentage`.

Для развёртываний на виртуальных машинах или «голом железе», где Collector не
имеет явной квоты памяти, мы рекомендуем вместо этого использовать параметры `limit_mib` и
`spike_limit_mib`.

### Экспортёры (Exporters)

В разделе `exporters` мы указываем стандартный [экспортёр `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) и настраиваем его с URL API Dynatrace и необходимым токеном аутентификации.

Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации для `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL конечной точки API Dynatrace](../../otlp-api.md#export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [API-токен](../../otlp-api.md#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Пайплайны сервиса (Service pipelines)

В разделе `service` мы собираем наши объекты приёмника и экспортёра в пайплайны для трейсов, метрик и логов и включаем наш процессор ограничения памяти, ссылаясь на него в разделе `processors` для каждого соответствующего пайплайна.

## Ограничения и лимиты

Данные принимаются по протоколу OpenTelemetry (OTLP) через API Dynatrace OTLP и подчиняются ограничениям и лимитам API.
Подробнее см.:

* Ограничения метрик OpenTelemetry
* [Маппинг метрик Dynatrace](../../otlp-api/ingest-otlp-metrics/about-metrics-ingest.md#dynatrace-mapping "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")
* Приём логов OpenTelemetry

## Связанные темы

* Обогащение принятых данных полями, специфичными для Dynatrace
* Обогащение запросов OTLP данными Kubernetes
