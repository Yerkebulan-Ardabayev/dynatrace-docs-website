# -*- coding: utf-8 -*-
"""L4-IF.70 builder: ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest.md"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from _otel_canon import S, build_one, qa_one

REL = "ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics"
FNAME = "about-metrics-ingest.md"

# Tooltip reused from siblings:
TT_WALK = "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace."
RU_WALK = "Узнайте, как интегрировать и принимать данные OpenTelemetry (трассировки, метрики и логи) в Dynatrace."

TRANS = {
    # ---- frontmatter ----
    "title: About OTLP metrics ingest": "title: О приёме метрик OTLP",
    # ---- page title (appears twice per source) ----
    "# About OTLP metrics ingest": "# О приёме метрик OTLP",
    # ---- doc-type metadata ----
    "* Explanation": "* Пояснение",
    "* 2-min read": "* Чтение: 2 мин",
    "* Updated on Mar 11, 2026": "* Обновлено 11 марта 2026 г.",
    # ---- intro ----
    "This page provides information about how Dynatrace ingests and enriches OpenTelemetry metrics.": "На этой странице представлена информация о том, как Dynatrace принимает и обогащает метрики OpenTelemetry.",
    # ---- callout heading (not a markdown heading, bare text) ----
    "Migrate from the Dynatrace OpenTelemetry metrics exporter": "Миграция с Dynatrace OpenTelemetry metrics exporter",
    "If you're still using the Dynatrace OpenTelemetry metrics exporter, we recommend that you migrate to the OTLP metrics exporter.": "Если вы ещё используете Dynatrace OpenTelemetry metrics exporter, рекомендуется перейти на OTLP metrics exporter.",
    # norm() strips the ï»¿ BOM-class char before the closing ] in the raw source:
    "For more information, see [Migrating from the Dynatrace OTel metrics exporter to standard OTLP metrics exporter](https://community.dynatrace.com/t5/Open-Q-A/Migrating-from-the-Dynatrace-OTel-metrics-exporter-to-standard/m-p/286986/thread-id/37689#M37690).": "Дополнительные сведения см. в разделе [Migrating from the Dynatrace OTel metrics exporter to standard OTLP metrics exporter](https://community.dynatrace.com/t5/Open-Q-A/Migrating-from-the-Dynatrace-OTel-metrics-exporter-to-standard/m-p/286986/thread-id/37689#M37690).",
    # ---- section headings ----
    # Translated: the EN slug would be #dynatrace-specific-mapping anyway (not #dynatrace-mapping),
    # so there is no anchor stability benefit to keeping it EN.
    # Cross-links in S that reference #dynatrace-mapping are pre-existing and platform-resolved.
    "## Dynatrace-specific mapping": "## Сопоставление с типами метрик Dynatrace",
    "## API limits and validations": "## Пределы и проверки API",
    "### Attribute ingestion": "### Приём атрибутов",
    # Kept EN: "### Aggregation temporality" -> anchor #aggregation-temporality (cross-linked)
    "### Aggregation temporality": "### Aggregation temporality",
    "### Metric keys": "### Ключи метрик",
    "### Dimension keys": "### Ключи измерений",
    "### Histograms": "### Гистограммы",
    "### Summaries": "### Сводки (Summary)",
    # ---- intro para below mapping heading ----
    "Dynatrace maps the individual OpenTelemetry instruments to the following Dynatrace metric types:": "Dynatrace сопоставляет отдельные инструменты OpenTelemetry со следующими типами метрик Dynatrace:",
    # ---- table header row ----
    "| Instrument | with temporality | maps to Dynatrace |": "| Инструмент | с темпоральностью | сопоставляется с типом Dynatrace |",
    # ---- table data rows ----
    "| Counter | Delta | Counter |": "| Counter | Дельта | Counter |",
    "| Counter | Cumulative | N/A |": "| Counter | Кумулятивная | N/A |",
    "| Gauge | N/A | Gauge |": "| Gauge | N/A | Gauge |",
    "| Explicit bucket histogram [1](#fn-1-1-def) | Delta | Histogram |": "| Explicit bucket histogram [1](#fn-1-1-def) | Дельта | Histogram |",
    "| Exponential histogram [2](#fn-1-2-def) | Delta | Exponential histogram |": "| Exponential histogram [2](#fn-1-2-def) | Дельта | Exponential histogram |",
    "| UpDownCounter | Delta | Counter |": "| UpDownCounter | Дельта | Counter |",
    "| UpDownCounter | Cumulative | Gauge |": "| UpDownCounter | Кумулятивная | Gauge |",
    "| Summary | N/A | N/A |": "| Summary | N/A | N/A |",
    # ---- footnote numbers (bare digit lines) ----
    "1": "1",
    "2": "2",
    # ---- footnote bodies ----
    "Explicit bucket histograms are supported with Dynatrace Managed version 1.324+ and ActiveGate version 1.321+.": "Explicit bucket histograms поддерживаются в Dynatrace Managed версии 1.324+ и ActiveGate версии 1.321+.",
    "For exponential histograms, Dynatrace ingests the histogram's `min|max|sum|count` but doesn't ingest the buckets.": "Для экспоненциальных гистограмм Dynatrace принимает `min|max|sum|count` гистограммы, но не принимает интервалы.",
    # ---- API limits section ----
    "When ingesting OpenTelemetry metrics, limits and validations apply as described in the tables below.": "При приёме метрик OpenTelemetry применяются пределы и проверки, описанные в таблицах ниже.",
    # limits table header
    "| Entity | Limit | Description |": "| Сущность | Предел | Описание |",
    # limits table rows
    "| Metric key length, characters | Min: 2, Max: 255 | The length of a metric key. |": "| Длина ключа метрики, символы | Мин: 2, Макс: 255 | Длина ключа метрики. |",
    "| Dimension key length, characters | Min: 1, Max: 100 | The length of a dimension key. If the maximum length is exceeded, the key is truncated at the upper limit. |": "| Длина ключа измерения, символы | Мин: 1, Макс: 100 | Длина ключа измерения. Если превышена максимальная длина, ключ усекается до верхнего предела. |",
    "| Dimension value length, characters | Min: 1, Max: 255 | The length of a dimension value. If the maximum length is exceeded, the dimension value is truncated at the upper limit. |": "| Длина значения измерения, символы | Мин: 1, Макс: 255 | Длина значения измерения. Если превышена максимальная длина, значение измерения усекается до верхнего предела. |",
    "| Number of dimensions per metric data point | 50 | The maximum total number of dimensions in a single metric data point. If the number of dimensions is exceeded, the whole data point is dropped. |": "| Количество измерений на точку данных метрики | 50 | Максимальное общее количество измерений в одной точке данных метрики. Если число измерений превышено, вся точка данных отбрасывается. |",
    "| Total number of possible metric keys per environment | 100,000 | The maximum number of metric keys that can be active at the same time. |": "| Общее количество возможных ключей метрик на среду | 100 000 | Максимальное количество ключей метрик, которые могут быть активны одновременно. |",
    "| Number of tuples per month per metric | 1,000,000 | The maximum number of tuples (unique metric-dimension key-value type combinations) for each metric key for the last 30 days. |": "| Количество кортежей в месяц на метрику | 1 000 000 | Максимальное количество кортежей (уникальных комбинаций ключ-значение измерение-метрика) для каждого ключа метрики за последние 30 дней. |",
    "| Number of tuples per month for all custom metrics | 50,000,000 | The maximum number of tuples (unique metric-dimension key-value type combinations) for all custom metrics for the last 30 days. |": "| Количество кортежей в месяц для всех пользовательских метрик | 50 000 000 | Максимальное количество кортежей (уникальных комбинаций ключ-значение измерение-метрика) для всех пользовательских метрик за последние 30 дней. |",
    "| Instrument unit, characters | 63 | The maximum total length of the instrument unit. If the maximum length is exceeded, the unit is dropped. |": "| Единица инструмента, символы | 63 | Максимальная общая длина единицы измерения инструмента. Если превышена максимальная длина, единица измерения отбрасывается. |",
    "| Instrument description, characters | 1,023 | The maximum total length of the instrument description. If the maximum length is exceeded, the instrument description is truncated at the character limit. |": "| Описание инструмента, символы | 1 023 | Максимальная общая длина описания инструмента. Если превышена максимальная длина, описание инструмента усекается до лимита символов. |",
    "| Request size | 4 MB | The maximum uncompressed size of an OTLP request with a metrics payload. If the limit is exceeded, the entire request is dropped. |": "| Размер запроса | 4 МБ | Максимальный несжатый размер OTLP-запроса с полезной нагрузкой метрик. Если лимит превышен, весь запрос отбрасывается. |",
    "| Metric data points | 15,000 | The maximum number of metric data points in an OTLP request with a metrics payload. If the limit is exceeded, the entire request is dropped. |": "| Точки данных метрик | 15 000 | Максимальное количество точек данных метрик в OTLP-запросе с полезной нагрузкой метрик. Если лимит превышен, весь запрос отбрасывается. |",
    # ---- attribute ingestion subsection ----
    "OpenTelemetry supports attributes on different levels in an OpenTelemetry metric request (that is, data points, scopes, and resources).": "OpenTelemetry поддерживает атрибуты на разных уровнях в запросе метрик OpenTelemetry: точки данных, области видимости и ресурсы.",
    "Because attributes are saved in a flattened fashion on the Dynatrace side, there may be name collisions if attributes on different levels share the same name.": "Так как атрибуты сохраняются на стороне Dynatrace в плоском виде, при совпадении имён атрибутов на разных уровнях могут возникать коллизии имён.",
    "To handle such name conflicts, Dynatrace applies the following order of priority to choose which attribute will be ingested:": "Для разрешения таких конфликтов имён Dynatrace применяет следующий приоритетный порядок выбора принимаемого атрибута:",
    "1. Data point attributes": "1. Атрибуты точки данных",
    "2. Scope attributes": "2. Атрибуты области видимости",
    "3. Resource attributes": "3. Атрибуты ресурса",
    "For example, if there is a data point and a scope attribute have the same name, the value of the data point will take precedence.": "Например, если точка данных и атрибут области видимости имеют одинаковое имя, приоритет отдаётся значению точки данных.",
    "Similarly, if a scope and resource attribute share the same name, Dynatrace will ingest the value of the scope attribute.": "Аналогично, если атрибут области видимости и атрибут ресурса имеют одинаковое имя, Dynatrace примет значение атрибута области видимости.",
    # ---- aggregation temporality subsection ----
    "The Dynatrace backend exclusively works with delta values and requires the respective aggregation temporality.": "Бэкенд Dynatrace работает исключительно с дельта-значениями и требует соответствующей темпоральности агрегации.",
    # norm() strips ï»¿ from the raw source before the URL:
    "Please ensure your metrics exporter is accordingly configured or set the [`OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE`](https://opentelemetry.io/docs/specs/otel/metrics/sdk_exporters/otlp/) environment variable to `DELTA`.": "Убедитесь, что ваш exporter метрик настроен соответствующим образом, или задайте переменной окружения [`OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE`](https://opentelemetry.io/docs/specs/otel/metrics/sdk_exporters/otlp/) значение `DELTA`.",
    'For examples on how to set the temporality under each individual language, see the [integration walkthroughs](/managed/ingest-from/opentelemetry/walkthroughs "%s").'
    % TT_WALK: 'Примеры установки темпоральности для конкретных языков программирования см. в разделе [пошаговые руководства по интеграции](/managed/ingest-from/opentelemetry/walkthroughs "%s").'
    % RU_WALK,
    # ---- metric keys subsection ----
    "* A metric key consists of sections separated by dots (for example, `dt.metrics`).": "* Ключ метрики состоит из секций, разделённых точками (например, `dt.metrics`).",
    "* A metric key can contain lowercase and uppercase letters, numbers, hyphens (`-`), and underscores (`_`).": "* Ключ метрики может содержать строчные и прописные буквы, цифры, дефисы (`-`) и символы подчёркивания (`_`).",
    "* A metric key must start with a letter character.": "* Ключ метрики должен начинаться с буквенного символа.",
    # Ã¤ Ã¶ Ã¼ are raw mojibaked chars in EN source (= ä ö ü); norm() does NOT strip them,
    # so keys must match them verbatim. RU output uses the clean Unicode chars (ä ö ü):
    "* A metric key must not contain non-Latin characters (such as `Ã¤`, `Ã¶`, and `Ã¼`).": "* Ключ метрики не должен содержать не-латинские символы (например, `ä`, `ö` и `ü`).",
    "* A metric key may be suffixed automatically depending on the payload (for example, `.count` for counters and `.gauge` for gauges).": "* К ключу метрики может автоматически добавляться суффикс в зависимости от полезной нагрузки (например, `.count` для счётчиков и `.gauge` для gauge).",
    "If you use characters that are invalid according to the rules above, they will be replaced with underscores.": "Если используются символы, недопустимые согласно приведённым правилам, они будут заменены символами подчёркивания.",
    "If your metric key does not have at least one valid character, the data point will be dropped.": "Если ключ метрики не содержит ни одного допустимого символа, точка данных будет отброшена.",
    # ---- dimension keys subsection ----
    "* Dimensions are comparable to span or resources attributes.": "* Измерения сопоставимы с атрибутами спана или ресурса.",
    "* A dimension key can contain only lowercase letters (not uppercase letters), numbers, hyphens (`-`), periods (`.`), and underscores (`_`).": "* Ключ измерения может содержать только строчные буквы (не прописные), цифры, дефисы (`-`), точки (`.`) и символы подчёркивания (`_`).",
    "* A dimension key must start with a letter character.": "* Ключ измерения должен начинаться с буквенного символа.",
    "* A dimension key must not contain non-Latin characters (such as `Ã¤`, `Ã¶`, and `Ã¼`).": "* Ключ измерения не должен содержать не-латинские символы (например, `ä`, `ö` и `ü`).",
    "* A dimension key can be in the `key.key-section` format.": "* Ключ измерения может иметь формат `key.key-section`.",
    "* You can specify up to 50 dimensions.": "* Можно задать до 50 измерений.",
    "* If the same dimension key is specified multiple times in a single payload, only the value that occurs first is accepted.": "* Если один и тот же ключ измерения указан несколько раз в одной полезной нагрузке, принимается только первое значение.",
    "If your dimension key does not have at least one valid character, the key will be dropped.": "Если ключ измерения не содержит ни одного допустимого символа, ключ будет отброшен.",
    "Dimension values must be passed as a string, Boolean, or integer.": "Значения измерений должны передаваться как строка, булево значение или целое число.",
    "Dynatrace does not support non-string dimensions and will convert Booleans and integers to strings upon ingest.": "Dynatrace не поддерживает измерения нестрокового типа и при приёме преобразует булевы значения и целые числа в строки.",
    "If any other type is used, the entire dimension will be dropped.": "Если используется любой другой тип, всё измерение будет отброшено.",
    # ---- histograms subsection ----
    "For explicit bucket histograms, there are a few things to consider:": "Для explicit bucket histogram следует учитывать несколько аспектов:",
    "* Dynatrace adds to the metric key of a histogram metric the suffix `.histogram`.": "* Dynatrace добавляет к ключу метрики гистограммы суффикс `.histogram`.",
    "* A histogram metric is billed like a count or gauge metric; the individual buckets are not billed separately.": "* Метрика гистограммы тарифицируется как метрика count или gauge; отдельные интервалы не тарифицируются отдельно.",
    "* Only 12 buckets per histogram datapoint are stored.": "* Хранится не более 12 интервалов на точку данных гистограммы.",
    "* Negative bucket boundaries are not supported.": "* Отрицательные границы интервалов не поддерживаются.",
    "If any of below happens, the OpenTelemetry ingest API returns the `400` or `200 with partial success` responses.": "Если происходит любое из нижеперечисленного, OTLP ingest API возвращает ответ `400` или `200 with partial success`.",
    "* Cumulative histograms aren't ingested (similarly to cumulative counters).": "* Кумулятивные гистограммы не принимаются (аналогично кумулятивным счётчикам).",
    "* Histogram data points without sum aren't ingested. This happens when negative values are recorded.": "* Точки данных гистограммы без суммы не принимаются. Это происходит при записи отрицательных значений.",
    "* Histogram buckets are not sorted.": "* Интервалы гистограммы не отсортированы.",
    "* Histogram bucket boundary values of `NaN` or `Infinite` are invalid.": "* Граничные значения интервалов гистограммы `NaN` или `Infinite` недопустимы.",
    "The Dynatrace OpenTelemetry ingest API only returns an HTTP `400` when all metrics in the OTLP request are invalid.": "Dynatrace OpenTelemetry ingest API возвращает HTTP `400` только в том случае, если все метрики в OTLP-запросе недопустимы.",
    # ---- summaries subsection ----
    "Dynatrace does not support summary metrics.": "Dynatrace не поддерживает метрики типа Summary.",
    "Summary metrics only exist in the OpenTelemetry protocol (OTLP) for compatibility with other formats.": "Метрики Summary существуют в протоколе OpenTelemetry (OTLP) только для совместимости с другими форматами.",
    "Applications using official OpenTelemetry SDKs cannot produce summary metrics.": "Приложения, использующие официальные SDK OpenTelemetry, не могут создавать метрики Summary.",
    **S,
}

# Table separator rows and EN-kept headings (no Russian content):
PASS = {
    "| --- | --- | --- |",
}

if __name__ == "__main__":
    build_one(REL, FNAME, TRANS, PASS)
    qa_one(REL, FNAME)
