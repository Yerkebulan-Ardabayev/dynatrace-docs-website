---
title: Ensure success with OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/troubleshooting
scraped: 2026-03-06T21:23:23.450010
---

# Обеспечение успешной работы с OpenTelemetry

# Обеспечение успешной работы с OpenTelemetry

* Latest Dynatrace
* Устранение неполадок
* Чтение: 1 мин
* Обновлено 3 декабря 2025 г.

Успешное внедрение OpenTelemetry требует как надежного экспорта данных, так и правильной визуализации в Dynatrace.
На этой странице представлены рекомендации по правильной настройке и устранению неполадок вашей реализации OpenTelemetry с Dynatrace.

## Метрики для мониторинга загрузки

Dynatrace предоставляет следующие встроенные метрики для загрузки сигналов OpenTelemetry.
В случае отсутствия данных они могут быть полезны для дальнейшего анализа возможных проблем с загрузкой.

В Dynatrace Classic метрики мониторинга загрузки имеют префикс `dsfm:` вместо `dt.sfm.`

### Метрики для загрузки логов

Latest Dynatrace

| Название | Описание |
| --- | --- |
| `dt.sfm.active_gate.event_ingest.event_incoming_count` | Количество загруженных записей логов |
| `dt.sfm.active_gate.event_ingest.drop_count` | Количество отброшенных записей логов |
| `dt.sfm.active_gate.event_ingest.event_otlp_size` | Размер полезной нагрузки полученных запросов логов |

### Метрики для загрузки метрик

Latest Dynatrace

| Название | Описание |
| --- | --- |
| `dt.sfm.active_gate.metrics.ingest.otlp.datapoints.accepted` | Количество принятых точек данных |
| `dt.sfm.active_gate.metrics.ingest.otlp.datapoints.rejected` | Количество отклоненных точек данных |

Отклоненные метрики содержат измерение `reason`, которое предоставляет дополнительные сведения о причине отклонения точки данных.
В Dynatrace вы можете фильтровать, сортировать и разделять по этому измерению.

Типичная причина -- отправка метрик с кумулятивной временной агрегацией (Dynatrace [требует дельта-временную агрегацию](otlp-api/ingest-otlp-metrics/about-metrics-ingest.md#aggregation-temporality "Узнайте, как Dynatrace загружает метрики OpenTelemetry и какие ограничения применяются.")), в этом случае `reason` указывает `UNSUPPORTED_METRIC_TYPE_MONOTONIC_CUMULATIVE_SUM`.

### Метрики для загрузки трассировок

Latest Dynatrace

| Название | Описание |
| --- | --- |
| `dt.sfm.server.spans.received` | Количество спанов OpenTelemetry, загруженных через эндпоинт OLTP для трассировок (ActiveGate или OneAgent), которые были успешно получены Dynatrace |
| `dt.sfm.server.spans.persisted` | Количество спанов OpenTelemetry, сохраненных Dynatrace; только сохраненные спаны доступны для анализа распределенных трассировок |
| `dt.sfm.server.spans.dropped` | Количество спанов OpenTelemetry, которые не были сохранены Dynatrace по указанной причине (например, время окончания спана вне допустимого диапазона) |

## Распространенные проблемы и решения

### Проблемы с настройкой

* [У меня проблемы с настройкой OpenTelemetry. Что нужно проверить?](https://dt-url.net/dm038xt)
* [Исправление ошибок SSL в OpenTelemetry SDK при экспорте в Dynatrace ActiveGate](https://community.dynatrace.com/t5/Troubleshooting/Fixing-SSL-Errors-in-OpenTelemetry-SDKs-when-exporting-to/ta-p/269404)

### Проблемы с подключением

* [Почему я получаю ошибку соединения при экспорте через OTLP в ActiveGate?](https://dt-url.net/x0238hc)
* [Почему я получаю ошибку соединения при экспорте трассировок OpenTelemetry в OneAgent?](https://dt-url.net/tk4384x)

### Проблемы с аутентификацией

* Проблема: ошибки HTTP 401/403 в метриках загрузки.
* Решение: проверьте разрешения API и конфигурации эндпоинтов.

См. также:

* [Почему ActiveGate возвращает ошибку 401 Unauthorized?](https://dt-url.net/lg638i3)
* [Почему ActiveGate возвращает ошибку 403 Forbidden?](https://dt-url.net/2n838im)

### Проблемы с форматом данных

* Проблема: высокий уровень отбрасывания с ошибками формата.
* Решение: проверьте соответствие формата данных OpenTelemetry и ограничения атрибутов.

### Проблемы с конфигурацией

* Проблема: данные не отображаются, несмотря на успешный экспорт.
* Решение: проверьте URL эндпоинтов, заголовки и конфигурацию протокола.

### Проблемы с загрузкой

* [Почему мой OTLP-экспорт не работает?](https://dt-url.net/sb238k5)
* [Эндпоинты Dynatrace OTLP API](otlp-api.md "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Вертикальная топология

* [Почему отсутствует моя вертикальная топология?](https://dt-url.net/48038un)

## Вопросы по конкретным сигналам

Информация о загрузке каждого типа сигнала доступна по ссылкам:

* [Загрузка логов OTLP](otlp-api/ingest-logs.md "Узнайте, как Dynatrace загружает записи логов OpenTelemetry и какие ограничения применяются.")
* [О загрузке метрик OTLP](otlp-api/ingest-otlp-metrics/about-metrics-ingest.md "Узнайте, как Dynatrace загружает метрики OpenTelemetry и какие ограничения применяются.")
* [Загрузка трассировок OTLP](otlp-api/ingest-traces.md "Узнайте, как Dynatrace загружает трассировки OpenTelemetry и какие ограничения применяются.")

### Трассировки

* [Почему мои спаны не связаны? Почему мои спаны являются сиротами?](https://dt-url.net/ae038vj)
* [Почему отсутствуют атрибуты моих спанов OpenTelemetry?](https://dt-url.net/z402yxq)

### Метрики

* [Почему мои метрики не загружаются?](https://community.dynatrace.com/t5/Troubleshooting/Why-are-my-OpenTelemetry-metrics-not-ingested/ta-p/269428)
* [Почему мои кумулятивные метрики не загружаются?](https://dt-url.net/s60382e)
* [Почему я получаю ответ "Partial Success"?](https://dt-url.net/0u238ec)
* [Почему отсутствуют атрибуты моих метрик?](https://dt-url.net/jj03800)
* [Как настроить метрики OpenTelemetry с дельта-временной агрегацией](https://community.dynatrace.com/t5/Troubleshooting/How-to-set-up-OpenTelemetry-metrics-with-delta-temporality/ta-p/269292)
* [Задержка отображения измерений метрик OpenTelemetry в Dynatrace](https://community.dynatrace.com/t5/Troubleshooting/Delay-in-displaying-OpenTelemetry-metric-dimensions-in-Dynatrace/ta-p/269732)
* [Почему мои метрики OpenTelemetry не загружаются](https://community.dynatrace.com/t5/Troubleshooting/Why-are-my-OpenTelemetry-metrics-not-ingested/ta-p/269428)

## Лучшие практики

### Используйте измерения метрик

Измерения используются в Dynatrace для различения того, что именно измеряется в конкретной точке данных.

В OpenTelemetry измерения называются атрибутами.

Например, если вы измеряете количество запросов, полученных эндпоинтом, вы можете использовать измерения для разделения этой метрики на запросы, прошедшие успешно (код статуса 200), и запросы, завершившиеся ошибкой (код статуса 500).

Ваши измерения должны быть хорошо аннотированы (узнаваемы, читаемы, понятны), иметь описательные названия и предоставлять полезную информацию.

### Сжатие

Dynatrace рекомендует включить сжатие `gzip` в ваших OTLP-экспортерах.

Сжатие по умолчанию в OTLP-экспортере [не задано](https://opentelemetry.io/docs/specs/otel/protocol/exporter/), но его можно настроить через следующие переменные окружения:

* `OTEL_EXPORTER_OTLP_COMPRESSION`
* `OTEL_EXPORTER_OTLP_TRACES_COMPRESSION`
* `OTEL_EXPORTER_OTLP_METRICS_COMPRESSION`
* `OTEL_EXPORTER_OTLP_LOGS_COMPRESSION`

Допустимые значения: `none` или `gzip`.

### Пакетная обработка

Если вы используете OpenTelemetry Collector, настоятельно рекомендуется использовать [batch-процессор](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.145.0/processor/batchprocessor/README.md).

Пакетная обработка помогает лучше сжимать данные и уменьшить количество исходящих соединений, необходимых для передачи данных в Dynatrace.

Подробнее см. в [README на GitHub](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.145.0/processor/batchprocessor/README.md).
