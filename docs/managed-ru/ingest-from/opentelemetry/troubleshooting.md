---
title: Обеспечение успешного внедрения OpenTelemetry
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/troubleshooting
---

# Обеспечение успешного внедрения OpenTelemetry

# Обеспечение успешного внедрения OpenTelemetry

* Устранение неполадок
* Чтение 1 мин
* Обновлено 03 дек. 2025 г.

Успешное внедрение OpenTelemetry требует одновременно надёжного экспорта данных и корректной визуализации в Dynatrace.
Эта страница содержит рекомендации по правильной настройке и устранению неполадок в реализации OpenTelemetry с Dynatrace.

## Метрики для мониторинга приёма данных

Dynatrace предоставляет следующие встроенные метрики для приёма сигналов OpenTelemetry.
В случае отсутствия данных они полезны для дальнейшего анализа возможных проблем приёма.

В Dynatrace Classic метрики мониторинга приёма данных имеют префикс `dsfm:` вместо `dt.sfm.`

### Метрики для приёма логов

Последняя версия Dynatrace

| Название | Описание |
| --- | --- |
| `dt.sfm.active_gate.event_ingest.event_incoming_count` | Количество принятых записей логов |
| `dt.sfm.active_gate.event_ingest.drop_count` | Количество отброшенных записей логов |
| `dt.sfm.active_gate.event_ingest.event_otlp_size` | Размер полезной нагрузки полученных запросов логов |

### Метрики для приёма метрик

Последняя версия Dynatrace

| Название | Описание |
| --- | --- |
| `dt.sfm.active_gate.metrics.ingest.otlp.datapoints.accepted` | Количество принятых точек данных |
| `dt.sfm.active_gate.metrics.ingest.otlp.datapoints.rejected` | Количество отклонённых точек данных |

Отклонённые метрики сопровождаются измерением `reason`, которое даёт дополнительные сведения о причине отклонения точки данных.
В Dynatrace можно фильтровать, сортировать и разбивать по этому измерению.

Типичная причина, это отправка метрик с кумулятивной временной агрегацией (Dynatrace [требует дельта-агрегацию](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#aggregation-temporality "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения при этом действуют."), в этом случае `reason` указывает `UNSUPPORTED_METRIC_TYPE_MONOTONIC_CUMULATIVE_SUM`.

### Метрики для приёма трасс

Последняя версия Dynatrace

| Название | Описание |
| --- | --- |
| `dt.sfm.server.spans.received` | Количество спанов OpenTelemetry, принятых через конечную точку трасс OLTP (ActiveGate или OneAgent), которые были успешно получены Dynatrace |
| `dt.sfm.server.spans.persisted` | Количество спанов OpenTelemetry, сохранённых Dynatrace; только сохранённые спаны доступны для анализа распределённых трасс |
| `dt.sfm.server.spans.dropped` | Количество спанов OpenTelemetry, которые не были сохранены Dynatrace по указанной причине (например, время окончания спана вне допустимого диапазона) |

## Распространённые проблемы и решения

### Проблемы с настройкой

* [У меня проблемы с настройкой OpenTelemetry. Что нужно проверить?﻿](https://dt-url.net/dm038xt)
* [Исправление ошибок SSL в SDKах OpenTelemetry при экспорте в Dynatrace ActiveGate﻿](https://community.dynatrace.com/t5/Troubleshooting/Fixing-SSL-Errors-in-OpenTelemetry-SDKs-when-exporting-to/ta-p/269404)

### Проблемы с подключением

* [Почему я получаю ошибку подключения при экспорте с OTLP в ActiveGate?﻿](https://dt-url.net/x0238hc)
* [Почему я получаю ошибку подключения при экспорте трасс OpenTelemetry в OneAgent?﻿](https://dt-url.net/tk4384x)

### Проблемы аутентификации

* Проблема: ошибки HTTP 401/403 в метриках приёма данных.
* Решение: проверить права API и настройки конечных точек.

См. также:

* [Почему ActiveGate возвращает ошибку 401 Unauthorized?﻿](https://dt-url.net/lg638i3)
* [Почему ActiveGate возвращает ошибку 403 Forbidden?﻿](https://dt-url.net/2n838im)

### Проблемы формата данных

* Проблема: высокий процент отбрасывания с ошибками формата.
* Решение: проверить соответствие формата данных OpenTelemetry и ограничения атрибутов.

### Проблемы конфигурации

* Проблема: данные не появляются, несмотря на успешный экспорт.
* Решение: проверить URL конечных точек, заголовки и настройку протокола.

### Проблемы приёма данных

* [Почему мой экспорт OTLP не работает?﻿](https://dt-url.net/sb238k5)
* [Конечные точки OTLP API в Dynatrace](/managed/ingest-from/opentelemetry/otlp-api "Узнайте о конечных точках OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Вертикальная топология

* [Почему отсутствует моя вертикальная топология?﻿](https://dt-url.net/48038un)

## Вопросы по конкретным сигналам

Подробные сведения о приёме каждого типа сигналов доступны здесь:

* [Приём логов OTLP](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения при этом действуют.")
* [О приёме метрик OTLP](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения при этом действуют.")
* [Приём трасс OTLP](/managed/ingest-from/opentelemetry/otlp-api/ingest-traces "Узнайте, как Dynatrace принимает трассы OpenTelemetry и какие ограничения при этом действуют.")

### Трассы

* [Почему мои спаны не связаны? Почему мои спаны становятся сиротами?﻿](https://dt-url.net/ae038vj)
* [Почему отсутствуют атрибуты моих спанов OpenTelemetry?﻿](https://dt-url.net/z402yxq)

### Метрики

* [Почему мои метрики не принимаются?﻿](https://community.dynatrace.com/t5/Troubleshooting/Why-are-my-OpenTelemetry-metrics-not-ingested/ta-p/269428)
* [Почему мои кумулятивные метрики не принимаются?﻿](https://dt-url.net/s60382e)
* [Почему я получаю ответ «Partial Success»?﻿](https://dt-url.net/0u238ec)
* [Почему отсутствуют мои атрибуты метрик?﻿](https://dt-url.net/jj03800)
* [Как настроить метрики OpenTelemetry с дельта-агрегацией﻿](https://community.dynatrace.com/t5/Troubleshooting/How-to-set-up-OpenTelemetry-metrics-with-delta-temporality/ta-p/269292)
* [Задержка отображения измерений метрик OpenTelemetry в Dynatrace﻿](https://community.dynatrace.com/t5/Troubleshooting/Delay-in-displaying-OpenTelemetry-metric-dimensions-in-Dynatrace/ta-p/269732)
* [Почему мои метрики OpenTelemetry не принимаются﻿](https://community.dynatrace.com/t5/Troubleshooting/Why-are-my-OpenTelemetry-metrics-not-ingested/ta-p/269428)

## Рекомендации

### Используйте измерения метрик

Измерения используются в Dynatrace, чтобы помочь определить, что именно измеряется в конкретной точке данных.

В OpenTelemetry измерения называются атрибутами.

Например, если измеряется количество запросов, полученных конечной точкой, измерения можно использовать для разбивки этой метрики на запросы, выполненные успешно (код состояния 200), и запросы с ошибкой (код состояния 500).

Измерения должны быть хорошо аннотированы (узнаваемы, читаемы, понятны), иметь описательные названия и предоставлять полезную информацию.

### Сжатие

Dynatrace рекомендует включить сжатие `gzip` в экспортёрах OTLP.

Сжатие по умолчанию в экспортёре OTLP [не задано﻿](https://opentelemetry.io/docs/specs/otel/protocol/exporter/), но его можно настроить с помощью следующих переменных окружения:

* `OTEL_EXPORTER_OTLP_COMPRESSION`
* `OTEL_EXPORTER_OTLP_TRACES_COMPRESSION`
* `OTEL_EXPORTER_OTLP_METRICS_COMPRESSION`
* `OTEL_EXPORTER_OTLP_LOGS_COMPRESSION`

Допустимые значения: `none` или `gzip`.

### Пакетная обработка

При использовании OpenTelemetry Collector настоятельно рекомендуется использовать [пакетную обработку﻿](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.156.0/exporter/exporterhelper#sending-queue-batch-settings) в экспортёре `otlp_http`.

Пакетная обработка помогает лучше сжимать данные и снижает количество исходящих соединений, необходимых для передачи данных в Dynatrace.

Дополнительные сведения приведены в этом [readme на GitHub﻿](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.156.0/processor/batchprocessor/README.md).