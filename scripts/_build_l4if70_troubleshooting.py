# -*- coding: utf-8 -*-
"""L4-IF.70 builder: ingest-from/opentelemetry/troubleshooting.md"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from _otel_canon import S, build_one, qa_one

REL = "ingest-from/opentelemetry"
FNAME = "troubleshooting.md"

TT_OTLP = "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."
RU_OTLP = "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."
TT_METAPI = (
    "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply."
)
RU_METAPI = "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются."
TT_LOGAPI = (
    "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply."
)
RU_LOGAPI = "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения применяются."
TT_TRACES = (
    "Learn how Dynatrace ingests OpenTelemetry traces and what limitations apply."
)
RU_TRACES = "Узнайте, как Dynatrace принимает трассировки OpenTelemetry и какие ограничения применяются."

TRANS = {
    # --- frontmatter / title ---
    "title: Ensure success with OpenTelemetry": "title: Успешная работа с OpenTelemetry",
    # --- H1 ---
    "# Ensure success with OpenTelemetry": "# Успешная работа с OpenTelemetry",
    # --- metadata ---
    "* Troubleshooting": "* Устранение неполадок",
    "* 1-min read": "* Чтение: 1 мин",
    "* Updated on Dec 03, 2025": "* Обновлено 03 декабря 2025 г.",
    # --- intro prose ---
    "Successfully implementing OpenTelemetry requires both reliable data export and proper visualization in Dynatrace.": "Для успешной реализации OpenTelemetry требуются как надёжный экспорт данных, так и их правильная визуализация в Dynatrace.",
    "This page offers guidance for properly configuring and troubleshooting your OpenTelemetry implementation with Dynatrace.": "На этой странице собраны рекомендации по правильной настройке и устранению неполадок в реализации OpenTelemetry с Dynatrace.",
    # --- section: Metrics for ingest monitoring ---
    "## Metrics for ingest monitoring": "## Метрики для мониторинга приёма",
    "Dynatrace provides the following built-in metrics for the ingestion of OpenTelemetry signals.": "Dynatrace предоставляет следующие встроенные метрики для приёма сигналов OpenTelemetry.",
    "In case of missing data, these can be useful in further analyzing possible ingestion issues.": "При отсутствии данных они могут быть полезны для дополнительного анализа возможных проблем с приёмом.",
    "In Dynatrace Classic, ingest monitoring metrics are prefixed with `dsfm:` instead of `dt.sfm.`": "В Dynatrace Classic метрики мониторинга приёма имеют префикс `dsfm:` вместо `dt.sfm.`",
    # --- subsection: logs ---
    "### Metrics for logs ingest": "### Метрики для приёма логов",
    "Latest Dynatrace": "Latest Dynatrace",
    "| Name | Description |": "| Название | Описание |",
    "| `dt.sfm.active_gate.event_ingest.event_incoming_count` | Number of ingested log records |": "| `dt.sfm.active_gate.event_ingest.event_incoming_count` | Количество принятых записей логов |",
    "| `dt.sfm.active_gate.event_ingest.drop_count` | Number of dropped log records |": "| `dt.sfm.active_gate.event_ingest.drop_count` | Количество отброшенных записей логов |",
    "| `dt.sfm.active_gate.event_ingest.event_otlp_size` | Payload size of received log requests |": "| `dt.sfm.active_gate.event_ingest.event_otlp_size` | Размер полезной нагрузки полученных запросов логов |",
    # --- subsection: metrics ---
    "### Metrics for metrics ingest": "### Метрики для приёма метрик",
    "| `dt.sfm.active_gate.metrics.ingest.otlp.datapoints.accepted` | Number of accepted data points |": "| `dt.sfm.active_gate.metrics.ingest.otlp.datapoints.accepted` | Количество принятых точек данных |",
    "| `dt.sfm.active_gate.metrics.ingest.otlp.datapoints.rejected` | Number of rejected data points |": "| `dt.sfm.active_gate.metrics.ingest.otlp.datapoints.rejected` | Количество отклонённых точек данных |",
    "Rejected metrics come with a `reason` dimension, which provides additional details on why a data point was rejected.": "Отклонённые метрики снабжены измерением `reason`, которое предоставляет дополнительные сведения о причине отклонения точки данных.",
    "In Dynatrace, you can filter, sort, and split by that dimension.": "В Dynatrace можно фильтровать, сортировать и разделять данные по этому измерению.",
    'A typical reason is when metrics are sent with cumulative aggregation temporality (Dynatrace [requires delta temporality](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#aggregation-temporality "%s")), in which case `reason` indicates `UNSUPPORTED_METRIC_TYPE_MONOTONIC_CUMULATIVE_SUM`.'
    % TT_METAPI: 'Типичная причина, когда метрики отправляются с кумулятивной агрегационной темпоральностью (Dynatrace [требует дельта-темпоральность](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#aggregation-temporality "%s")), при этом `reason` указывает `UNSUPPORTED_METRIC_TYPE_MONOTONIC_CUMULATIVE_SUM`.'
    % RU_METAPI,
    # --- subsection: traces ---
    "### Metrics for traces ingest": "### Метрики для приёма трассировок",
    # NOTE: The EN source says "OLTP trace endpoint" — this is a typo for "OTLP" in the source.
    # Per §3 (faithful to source), we reproduce "OLTP" verbatim in Russian.
    "| `dt.sfm.server.spans.received` | Number of OpenTelemetry spans ingested via the OLTP trace endpoint (ActiveGate or OneAgent) that were successfully received by Dynatrace |": "| `dt.sfm.server.spans.received` | Количество спанов OpenTelemetry, принятых через эндпоинт OLTP trace (ActiveGate или OneAgent), которые были успешно получены Dynatrace |",
    "| `dt.sfm.server.spans.persisted` | Number of OpenTelemetry spans preserved by Dynatrace; only preserved spans are available for distributed traces analysis |": "| `dt.sfm.server.spans.persisted` | Количество спанов OpenTelemetry, сохранённых Dynatrace; только сохранённые спаны доступны для анализа распределённых трассировок |",
    "| `dt.sfm.server.spans.dropped` | Number of OpenTelemetry spans that were not preserved by Dynatrace because of the indicated reason (for example, span end time out of range) |": "| `dt.sfm.server.spans.dropped` | Количество спанов OpenTelemetry, не сохранённых Dynatrace по указанной причине (например, время окончания спана вне допустимого диапазона) |",
    # --- section: Common issues and solutions ---
    "## Common issues and solutions": "## Распространённые проблемы и решения",
    "### Setup issues": "### Проблемы настройки",
    "* [I'm having setup issues with OpenTelemetry. What should I check?﻿](https://dt-url.net/dm038xt)": "* [Возникают проблемы с настройкой OpenTelemetry. Что следует проверить?](https://dt-url.net/dm038xt)",
    "* [Fixing SSL Errors in OpenTelemetry SDKs when exporting to Dynatrace ActiveGate﻿](https://community.dynatrace.com/t5/Troubleshooting/Fixing-SSL-Errors-in-OpenTelemetry-SDKs-when-exporting-to/ta-p/269404)": "* [Устранение ошибок SSL в SDK OpenTelemetry при экспорте в Dynatrace ActiveGate](https://community.dynatrace.com/t5/Troubleshooting/Fixing-SSL-Errors-in-OpenTelemetry-SDKs-when-exporting-to/ta-p/269404)",
    "### Connection issues": "### Проблемы соединения",
    "* [Why do I get a connection error when exporting with OTLP to ActiveGate?﻿](https://dt-url.net/x0238hc)": "* [Почему при экспорте по OTLP в ActiveGate возникает ошибка соединения?](https://dt-url.net/x0238hc)",
    "* [Why do I get a connection error when exporting OpenTelemetry traces to OneAgent?﻿](https://dt-url.net/tk4384x)": "* [Почему при экспорте трассировок OpenTelemetry в OneAgent возникает ошибка соединения?](https://dt-url.net/tk4384x)",
    "### Authentication issues": "### Проблемы аутентификации",
    "* Problem: HTTP 401/403 errors in ingestion metrics.": "* Проблема: ошибки HTTP 401/403 в метриках приёма.",
    "* Solution: Verify API permissions and endpoint configurations.": "* Решение: проверьте разрешения API и конфигурации эндпоинтов.",
    "See also:": "См. также:",
    "* [Why does ActiveGate return a 401 Unauthorized error?﻿](https://dt-url.net/lg638i3)": "* [Почему ActiveGate возвращает ошибку 401 Unauthorized?](https://dt-url.net/lg638i3)",
    "* [Why does ActiveGate return a 403 Forbidden error?﻿](https://dt-url.net/2n838im)": "* [Почему ActiveGate возвращает ошибку 403 Forbidden?](https://dt-url.net/2n838im)",
    "### Data format issues": "### Проблемы формата данных",
    "* Problem: High drop rates with format errors.": "* Проблема: высокий процент отбрасывания данных из-за ошибок формата.",
    "* Solution: Validate OpenTelemetry data format compliance and attribute limits.": "* Решение: проверьте соответствие формата данных OpenTelemetry требованиям и ограничениям атрибутов.",
    "### Configuration issues": "### Проблемы конфигурации",
    "* Problem: No data appears despite successful exports.": "* Проблема: данные не отображаются несмотря на успешный экспорт.",
    "* Solution: Verify endpoint URLs, headers, and protocol configuration.": "* Решение: проверьте URL эндпоинтов, заголовки и конфигурацию протокола.",
    "### Ingestion issues": "### Проблемы приёма данных",
    "* [Why does my OTLP export not work?﻿](https://dt-url.net/sb238k5)": "* [Почему не работает мой OTLP-экспорт?](https://dt-url.net/sb238k5)",
    '* [Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api "%s")'
    % TT_OTLP: '* [Эндпоинты Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "%s")'
    % RU_OTLP,
    "### Vertical topology": "### Вертикальная топология",
    "* [Why is my vertical topology missing?﻿](https://dt-url.net/48038un)": "* [Почему отсутствует вертикальная топология?](https://dt-url.net/48038un)",
    # --- section: Signal-specific questions ---
    "## Signal-specific questions": "## Вопросы по конкретным типам сигналов",
    "Specific information about ingesting each signal type is available at": "Конкретная информация о приёме каждого типа сигналов доступна по ссылкам:",
    '* [Ingest OTLP logs](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "%s")'
    % TT_LOGAPI: '* [Приём логов OTLP](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "%s")'
    % RU_LOGAPI,
    '* [About OTLP metrics ingest](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "%s")'
    % TT_METAPI: '* [О приёме метрик OTLP](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "%s")'
    % RU_METAPI,
    '* [Ingest OTLP traces](/managed/ingest-from/opentelemetry/otlp-api/ingest-traces "%s")'
    % TT_TRACES: '* [Приём трассировок OTLP](/managed/ingest-from/opentelemetry/otlp-api/ingest-traces "%s")'
    % RU_TRACES,
    "### Traces": "### Трассировки",
    "* [Why are my spans not linked? Why are my spans orphaned?﻿](https://dt-url.net/ae038vj)": "* [Почему спаны не связаны? Почему спаны осиротели?](https://dt-url.net/ae038vj)",
    "* [Why are my OpenTelemetry span attributes missing?﻿](https://dt-url.net/z402yxq)": "* [Почему отсутствуют атрибуты спанов OpenTelemetry?](https://dt-url.net/z402yxq)",
    "### Metrics": "### Метрики",
    "* [Why are my metrics not ingested?﻿](https://community.dynatrace.com/t5/Troubleshooting/Why-are-my-OpenTelemetry-metrics-not-ingested/ta-p/269428)": "* [Почему метрики не принимаются?](https://community.dynatrace.com/t5/Troubleshooting/Why-are-my-OpenTelemetry-metrics-not-ingested/ta-p/269428)",
    "* [Why are my cumulative metrics not ingested?﻿](https://dt-url.net/s60382e)": "* [Почему кумулятивные метрики не принимаются?](https://dt-url.net/s60382e)",
    '* [Why do I receive a "Partial Success" response?﻿](https://dt-url.net/0u238ec)': '* [Почему приходит ответ "Partial Success"?](https://dt-url.net/0u238ec)',
    "* [Why are my metric attributes missing?﻿](https://dt-url.net/jj03800)": "* [Почему отсутствуют атрибуты метрик?](https://dt-url.net/jj03800)",
    "* [How to set up OpenTelemetry metrics with delta temporality﻿](https://community.dynatrace.com/t5/Troubleshooting/How-to-set-up-OpenTelemetry-metrics-with-delta-temporality/ta-p/269292)": "* [Как настроить метрики OpenTelemetry с дельта-темпоральностью](https://community.dynatrace.com/t5/Troubleshooting/How-to-set-up-OpenTelemetry-metrics-with-delta-temporality/ta-p/269292)",
    "* [Delay in displaying OpenTelemetry metric dimensions in Dynatrace﻿](https://community.dynatrace.com/t5/Troubleshooting/Delay-in-displaying-OpenTelemetry-metric-dimensions-in-Dynatrace/ta-p/269732)": "* [Задержка отображения измерений метрик OpenTelemetry в Dynatrace](https://community.dynatrace.com/t5/Troubleshooting/Delay-in-displaying-OpenTelemetry-metric-dimensions-in-Dynatrace/ta-p/269732)",
    "* [Why are my OpenTelemetry metrics not ingested﻿](https://community.dynatrace.com/t5/Troubleshooting/Why-are-my-OpenTelemetry-metrics-not-ingested/ta-p/269428)": "* [Почему метрики OpenTelemetry не принимаются](https://community.dynatrace.com/t5/Troubleshooting/Why-are-my-OpenTelemetry-metrics-not-ingested/ta-p/269428)",
    # --- section: Best practices ---
    "## Best practices": "## Рекомендации",
    "### Use metric dimensions": "### Использование измерений метрик",
    "Dimensions are used in Dynatrace to help distinguish what is being measured in a specific data point.": "Измерения используются в Dynatrace для разграничения того, что именно измеряется в конкретной точке данных.",
    "In OpenTelemetry, dimensions are called attributes.": "В OpenTelemetry измерения называются атрибутами.",
    "For example, if you're measuring the number of requests an endpoint has received, you can use dimensions to split that metric into requests that went through (status code 200) and requests that failed (status code 500).": "Например, при измерении числа запросов, полученных эндпоинтом, с помощью измерений можно разбить метрику на успешные запросы (код статуса 200) и неуспешные (код статуса 500).",
    "Your dimensions should be well-annotated (recognizable, readable, understandable), have descriptive names, and provide good information.": "Измерения должны быть хорошо аннотированы (узнаваемы, читаемы, понятны), иметь описательные имена и нести полезную информацию.",
    "### Compression": "### Сжатие",
    "Dynatrace recommends that you enable `gzip` compression on your OTLP exporters.": "Dynatrace рекомендует включить сжатие `gzip` на экспортерах OTLP.",
    "The default compression on the OTLP exporter [is not set﻿](https://opentelemetry.io/docs/specs/otel/protocol/exporter/), but it can be configured through the following environment variables:": "Сжатие по умолчанию в экспортере OTLP [не задано](https://opentelemetry.io/docs/specs/otel/protocol/exporter/), однако его можно настроить с помощью следующих переменных окружения:",
    "* `OTEL_EXPORTER_OTLP_COMPRESSION`": "* `OTEL_EXPORTER_OTLP_COMPRESSION`",
    "* `OTEL_EXPORTER_OTLP_TRACES_COMPRESSION`": "* `OTEL_EXPORTER_OTLP_TRACES_COMPRESSION`",
    "* `OTEL_EXPORTER_OTLP_METRICS_COMPRESSION`": "* `OTEL_EXPORTER_OTLP_METRICS_COMPRESSION`",
    "* `OTEL_EXPORTER_OTLP_LOGS_COMPRESSION`": "* `OTEL_EXPORTER_OTLP_LOGS_COMPRESSION`",
    "Acceptable values are `none` or `gzip`.": "Допустимые значения: `none` или `gzip`.",
    "### Batching": "### Группирование",
    "If you use the OTel Collector, we highly recommend that you use a [batch processor﻿](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.151.0/processor/batchprocessor/README.md).": "При использовании OTel Collector настоятельно рекомендуется применять [batch processor](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.151.0/processor/batchprocessor/README.md).",
    "Batching helps better compress the data and reduce the number of outgoing connections required to transmit data to Dynatrace.": "Группирование позволяет эффективнее сжимать данные и сокращать количество исходящих соединений, необходимых для передачи данных в Dynatrace.",
    "See this [GitHub readme﻿](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.151.0/processor/batchprocessor/README.md) for more information.": "Дополнительные сведения см. в [README на GitHub](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.151.0/processor/batchprocessor/README.md).",
    **S,
}

# EN-kept lines with no Russian equivalent:
# - table separators
# - "Latest Dynatrace" tag (kept EN per corpus norm — it's a product-version badge)
# - env var bullet lines that are pure code (kept verbatim — only backtick content)
PASS = {
    "| --- | --- |",
}


if __name__ == "__main__":
    build_one(REL, FNAME, TRANS, PASS)
    qa_one(REL, FNAME)
