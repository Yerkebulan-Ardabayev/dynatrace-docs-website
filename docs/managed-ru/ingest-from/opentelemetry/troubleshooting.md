---
title: Успешная работа с OpenTelemetry
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/troubleshooting
scraped: 2026-05-12T12:11:27.888076
---

# Успешная работа с OpenTelemetry

# Успешная работа с OpenTelemetry

* Устранение неполадок
* Чтение: 1 мин
* Обновлено 03 декабря 2025 г.

Для успешной реализации OpenTelemetry требуются как надёжный экспорт данных, так и их правильная визуализация в Dynatrace.
На этой странице собраны рекомендации по правильной настройке и устранению неполадок в реализации OpenTelemetry с Dynatrace.

## Метрики для мониторинга приёма

Dynatrace предоставляет следующие встроенные метрики для приёма сигналов OpenTelemetry.
При отсутствии данных они могут быть полезны для дополнительного анализа возможных проблем с приёмом.

В Dynatrace Classic метрики мониторинга приёма имеют префикс `dsfm:` вместо `dt.sfm.`

### Метрики для приёма логов

Latest Dynatrace

| Название | Описание |
| --- | --- |
| `dt.sfm.active_gate.event_ingest.event_incoming_count` | Количество принятых записей логов |
| `dt.sfm.active_gate.event_ingest.drop_count` | Количество отброшенных записей логов |
| `dt.sfm.active_gate.event_ingest.event_otlp_size` | Размер полезной нагрузки полученных запросов логов |

### Метрики для приёма метрик

Latest Dynatrace

| Название | Описание |
| --- | --- |
| `dt.sfm.active_gate.metrics.ingest.otlp.datapoints.accepted` | Количество принятых точек данных |
| `dt.sfm.active_gate.metrics.ingest.otlp.datapoints.rejected` | Количество отклонённых точек данных |

Отклонённые метрики снабжены измерением `reason`, которое предоставляет дополнительные сведения о причине отклонения точки данных.
В Dynatrace можно фильтровать, сортировать и разделять данные по этому измерению.

Типичная причина, когда метрики отправляются с кумулятивной агрегационной темпоральностью (Dynatrace [требует дельта-темпоральность](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#aggregation-temporality "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")), при этом `reason` указывает `UNSUPPORTED_METRIC_TYPE_MONOTONIC_CUMULATIVE_SUM`.

### Метрики для приёма трассировок

Latest Dynatrace

| Название | Описание |
| --- | --- |
| `dt.sfm.server.spans.received` | Количество спанов OpenTelemetry, принятых через эндпоинт OLTP trace (ActiveGate или OneAgent), которые были успешно получены Dynatrace |
| `dt.sfm.server.spans.persisted` | Количество спанов OpenTelemetry, сохранённых Dynatrace; только сохранённые спаны доступны для анализа распределённых трассировок |
| `dt.sfm.server.spans.dropped` | Количество спанов OpenTelemetry, не сохранённых Dynatrace по указанной причине (например, время окончания спана вне допустимого диапазона) |

## Распространённые проблемы и решения

### Проблемы настройки

* [Возникают проблемы с настройкой OpenTelemetry. Что следует проверить?](https://dt-url.net/dm038xt)
* [Устранение ошибок SSL в SDK OpenTelemetry при экспорте в Dynatrace ActiveGate](https://community.dynatrace.com/t5/Troubleshooting/Fixing-SSL-Errors-in-OpenTelemetry-SDKs-when-exporting-to/ta-p/269404)

### Проблемы соединения

* [Почему при экспорте по OTLP в ActiveGate возникает ошибка соединения?](https://dt-url.net/x0238hc)
* [Почему при экспорте трассировок OpenTelemetry в OneAgent возникает ошибка соединения?](https://dt-url.net/tk4384x)

### Проблемы аутентификации

* Проблема: ошибки HTTP 401/403 в метриках приёма.
* Решение: проверьте разрешения API и конфигурации эндпоинтов.

См. также:

* [Почему ActiveGate возвращает ошибку 401 Unauthorized?](https://dt-url.net/lg638i3)
* [Почему ActiveGate возвращает ошибку 403 Forbidden?](https://dt-url.net/2n838im)

### Проблемы формата данных

* Проблема: высокий процент отбрасывания данных из-за ошибок формата.
* Решение: проверьте соответствие формата данных OpenTelemetry требованиям и ограничениям атрибутов.

### Проблемы конфигурации

* Проблема: данные не отображаются несмотря на успешный экспорт.
* Решение: проверьте URL эндпоинтов, заголовки и конфигурацию протокола.

### Проблемы приёма данных

* [Почему не работает мой OTLP-экспорт?](https://dt-url.net/sb238k5)
* [Эндпоинты Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Вертикальная топология

* [Почему отсутствует вертикальная топология?](https://dt-url.net/48038un)

## Вопросы по конкретным типам сигналов

Конкретная информация о приёме каждого типа сигналов доступна по ссылкам:

* [Приём логов OTLP](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения применяются.")
* [О приёме метрик OTLP](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")
* [Приём трассировок OTLP](/managed/ingest-from/opentelemetry/otlp-api/ingest-traces "Узнайте, как Dynatrace принимает трассировки OpenTelemetry и какие ограничения применяются.")

### Трассировки

* [Почему спаны не связаны? Почему спаны осиротели?](https://dt-url.net/ae038vj)
* [Почему отсутствуют атрибуты спанов OpenTelemetry?](https://dt-url.net/z402yxq)

### Метрики

* [Почему метрики не принимаются?](https://community.dynatrace.com/t5/Troubleshooting/Why-are-my-OpenTelemetry-metrics-not-ingested/ta-p/269428)
* [Почему кумулятивные метрики не принимаются?](https://dt-url.net/s60382e)
* [Почему приходит ответ "Partial Success"?](https://dt-url.net/0u238ec)
* [Почему отсутствуют атрибуты метрик?](https://dt-url.net/jj03800)
* [Как настроить метрики OpenTelemetry с дельта-темпоральностью](https://community.dynatrace.com/t5/Troubleshooting/How-to-set-up-OpenTelemetry-metrics-with-delta-temporality/ta-p/269292)
* [Задержка отображения измерений метрик OpenTelemetry в Dynatrace](https://community.dynatrace.com/t5/Troubleshooting/Delay-in-displaying-OpenTelemetry-metric-dimensions-in-Dynatrace/ta-p/269732)
* [Почему метрики OpenTelemetry не принимаются](https://community.dynatrace.com/t5/Troubleshooting/Why-are-my-OpenTelemetry-metrics-not-ingested/ta-p/269428)

## Рекомендации

### Использование измерений метрик

Измерения используются в Dynatrace для разграничения того, что именно измеряется в конкретной точке данных.

В OpenTelemetry измерения называются атрибутами.

Например, при измерении числа запросов, полученных эндпоинтом, с помощью измерений можно разбить метрику на успешные запросы (код статуса 200) и неуспешные (код статуса 500).

Измерения должны быть хорошо аннотированы (узнаваемы, читаемы, понятны), иметь описательные имена и нести полезную информацию.

### Сжатие

Dynatrace рекомендует включить сжатие `gzip` на экспортерах OTLP.

Сжатие по умолчанию в экспортере OTLP [не задано](https://opentelemetry.io/docs/specs/otel/protocol/exporter/), однако его можно настроить с помощью следующих переменных окружения:

* `OTEL_EXPORTER_OTLP_COMPRESSION`
* `OTEL_EXPORTER_OTLP_TRACES_COMPRESSION`
* `OTEL_EXPORTER_OTLP_METRICS_COMPRESSION`
* `OTEL_EXPORTER_OTLP_LOGS_COMPRESSION`

Допустимые значения: `none` или `gzip`.

### Группирование

При использовании OTel Collector настоятельно рекомендуется применять [batch processor](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.151.0/processor/batchprocessor/README.md).

Группирование позволяет эффективнее сжимать данные и сокращать количество исходящих соединений, необходимых для передачи данных в Dynatrace.

Дополнительные сведения см. в [README на GitHub](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.151.0/processor/batchprocessor/README.md).