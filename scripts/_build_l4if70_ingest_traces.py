# -*- coding: utf-8 -*-
from _otel_canon import S, build_one, qa_one

REL = "ingest-from/opentelemetry/otlp-api"
FNAME = "ingest-traces.md"

TT_OTLP = "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."

TRANS = {
    # --- frontmatter title ---
    "title: Ingest OTLP traces": "title: Приём трассировок OTLP",
    # --- page headings (appear twice) ---
    "# Ingest OTLP traces": "# Приём трассировок OTLP",
    # --- metadata bullets ---
    "* Reference": "* Справочник",
    "* Updated on Jul 15, 2024": "* Обновлено 15 июля 2024 г.",
    # --- intro prose ---
    "The following limitations apply to OpenTelemetry trace ingest requests and ingested spans.": "К запросам на приём трассировок OpenTelemetry и принятым спанам применяются следующие ограничения.",
    # --- table header row ---
    "| Type | Limit | Description |": "| Тип | Предел | Описание |",
    # --- table data rows ---
    "| Span end time | 60 minutes in the past | The minimum value of the span end timestamp at time of ingestion |": "| Время окончания спана | 60 минут назад | Минимальное значение метки времени окончания спана на момент приёма |",
    "| Span end time | 10 minutes in the future | The maximum value of the span end timestamp at time of ingestion |": "| Время окончания спана | 10 минут в будущем | Максимальное значение метки времени окончания спана на момент приёма |",
    "| Number of span attributes | 128[1](#fn-1-1-def) | The maximum number of span attributes per span |": "| Количество атрибутов спана | 128[1](#fn-1-1-def) | Максимальное количество атрибутов спана на один спан |",
    "| Number of span events | 128[1](#fn-1-1-def) | The maximum number of events per span |": "| Количество событий спана | 128[1](#fn-1-1-def) | Максимальное количество событий на один спан |",
    "| Number of event attributes | 128[1](#fn-1-1-def) | The maximum number of attributes per span event |": "| Количество атрибутов события | 128[1](#fn-1-1-def) | Максимальное количество атрибутов на одно событие спана |",
    "| Number of span links | 128[1](#fn-1-1-def) | The maximum number of links per span |": "| Количество ссылок спана | 128[1](#fn-1-1-def) | Максимальное количество ссылок на один спан |",
    "| Number of link attributes | 128[1](#fn-1-1-def) | The maximum number of attributes per span link |": "| Количество атрибутов ссылки | 128[1](#fn-1-1-def) | Максимальное количество атрибутов на одну ссылку спана |",
    "| Request size | 8 MB | The maximum size of an OTLP request for trace ingest to an ActiveGate (uncompressed data) |": "| Размер запроса | 8 МБ | Максимальный размер запроса OTLP для приёма трассировок в ActiveGate (несжатые данные) |",
    "| Request size (gzip) | 8 MB | The maximum size of an OTLP request for trace ingest to an ActiveGate (compressed data) |": "| Размер запроса (gzip) | 8 МБ | Максимальный размер запроса OTLP для приёма трассировок в ActiveGate (сжатые данные) |",
    # --- footnote text ---
    "Typical limit of the OpenTelemetry SDK. Not limited by Dynatrace.": "Типичное ограничение OpenTelemetry SDK. Dynatrace не ограничивает.",
    **S,
}

# Lines kept verbatim (EN-only content with no Russian needed)
PASS = {
    "| --- | --- | --- |",  # table separator
    "1",  # bare footnote number
}

if __name__ == "__main__":
    build_one(REL, FNAME, TRANS, PASS)
    qa_one(REL, FNAME)
