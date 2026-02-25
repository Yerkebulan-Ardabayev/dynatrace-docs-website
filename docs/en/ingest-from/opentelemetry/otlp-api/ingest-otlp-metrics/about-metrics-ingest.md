---
title: About OTLP metrics ingest
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest
scraped: 2026-02-25T21:33:43.375725
---

# About OTLP metrics ingest

# About OTLP metrics ingest

* Latest Dynatrace
* Explanation
* 2-min read
* Updated on Nov 04, 2025

Dynatrace version 1.254+

This page provides information about how Dynatrace ingests and enriches OpenTelemetry metrics.

Migrate from the Dynatrace OpenTelemetry metrics exporter

If you're still using the Dynatrace OpenTelemetry metrics exporter, we recommend that you migrate to the OTLP metrics exporter.
For more information, see [Migrating from the Dynatrace OTel metrics exporter to standard OTLP metrics exporterï»¿](https://community.dynatrace.com/t5/Open-Q-A/Migrating-from-the-Dynatrace-OTel-metrics-exporter-to-standard/m-p/286986/thread-id/37689#M37690).

## Dynatrace-specific mapping

Dynatrace maps the individual OpenTelemetry instruments to the following Dynatrace metric types:

| Instrument | with temporality | maps to Dynatrace |
| --- | --- | --- |
| Counter | Delta | Counter |
| Counter | Cumulative | N/A |
| Gauge | N/A | Gauge |
| Explicit bucket histogram [1](#fn-1-1-def) | Delta | Histogram |
| Exponential histogram [2](#fn-1-2-def) | Delta | Exponential histogram |
| UpDownCounter | Delta | Counter |
| UpDownCounter | Cumulative | Gauge |
| Summary | N/A | N/A |

1

Explicit bucket histograms are supported starting with Dynatrace version 1.300.

2

For exponential histograms, Dynatrace ingests the histogram's `min|max|sum|count` but doesn't ingest the buckets.

## API limits and validations

When ingesting OpenTelemetry metrics, the following limits and validations apply.

| Entity | Limit | Description |
| --- | --- | --- |
| Metric key length, characters | Min: 2, Max: 255 | The length of a metric key. |
| Dimension key length, characters | Min: 1, Max: 100 | The length of a dimension key. If the maximum length is exceeded, the key is truncated to 100 characters. |
| Dimension value length, characters | Min: 1, Max: 255 | The length of a dimension value. If the maximum length is exceeded, the dimension value is truncated to 255 characters. |
| Number of dimensions per metric data point | 50 | The maximum total number of dimensions in a single metric data point. If the number of dimensions is exceeded, the whole data point is dropped. |
| Total number of possible metric keys per environment | 100,000 | The maximum number of metric keys that can be active at the same time. |
| Number of tuples per month per metric | 1,000,000 | The maximum number of tuples (unique metric-dimension key-value type combinations) for each metric key for the last 30 days. |
| Number of tuples per month for all custom metrics | 50,000,000 | The maximum number of tuples (unique metric-dimension key-value type combinations) for all custom metrics for the last 30 days. |
| Instrument unit, characters | 63 | The maximum total length of the instrument unit. If the maximum length is exceeded, the unit is dropped. |
| Instrument description, characters | 1,023 | The maximum total length of the instrument description. If the maximum length is exceeded, the instrument description is truncated to 1,023 characters. |
| Request size | 4 MB | The maximum uncompressed size of an OTLP request with a metrics payload. If the limit is exceeded, the entire request is dropped. |
| Metric data points | 15,000 | The maximum number of metric data points in an OTLP request with a metrics payload. If the limit is exceeded, the entire request is dropped. |

### Attribute ingestion

OpenTelemetry supports attributes on different levels in an OpenTelemetry metric request (that is, data points, scopes, and resources).
Because attributes are saved in a flattened fashion on the Dynatrace side, there may be name collisions if attributes on different levels share the same name.

To handle such name conflicts, Dynatrace applies the following order of priority to choose which attribute will be ingested:

1. Data point attributes
2. Scope attributes
3. Resource attributes

For example, if there is a data point and a scope attribute have the same name, the value of the data point will take precedence.
Similarly, if a scope and resource attribute share the same name, Dynatrace will ingest the value of the scope attribute.

### Aggregation temporality

The Dynatrace backend exclusively works with delta values and requires the respective aggregation temporality.
Please ensure your metrics exporter is accordingly configured or set the [`OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE`ï»¿](https://opentelemetry.io/docs/specs/otel/metrics/sdk_exporters/otlp/) environment variable to `DELTA`.

For examples on how to set the temporality under each individual language, see the [integration walkthroughs](/docs/ingest-from/opentelemetry/walkthroughs "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.").

### Metric keys

* A metric key consists of sections separated by dots (for example, `dt.metrics`).
* A metric key can contain lowercase and uppercase letters, numbers, hyphens (`-`), and underscores (`_`).
* A metric key must start with a letter character.
* A metric key must not contain non-Latin characters (such as `Ã¤`, `Ã¶`, and `Ã¼`).
* A metric key may be suffixed automatically depending on the payload (for example, `.count` for counters and `.gauge` for gauges).

If you use characters that are invalid according to the rules above, they will be replaced with underscores.
If your metric key does not have at least one valid character, the data point will be dropped.

### Dimension keys

* Dimensions are comparable to span or resources attributes.
* A dimension key can contain only lowercase letters (not uppercase letters), numbers, hyphens (`-`), periods (`.`), and underscores (`_`).
* A dimension key must start with a letter character.
* A dimension key must not contain non-Latin characters (such as `Ã¤`, `Ã¶`, and `Ã¼`).
* A dimension key can be in the `key.key-section` format.
* You can specify up to 50 dimensions.
* If the same dimension key is specified multiple times in a single payload, only the value that occurs first is accepted.

If you use characters that are invalid according to the rules above, they will be replaced with underscores.
If your dimension key does not have at least one valid character, the key will be dropped.

Dimension values must be passed as a string, Boolean, or integer.

Dynatrace does not support non-string dimensions and will convert Booleans and integers to strings upon ingest.

If any other type is used, the entire dimension will be dropped.

### Histograms

For exponential histograms, Dynatrace ingests the histogram's `min|max|sum|count` but doesn't ingest the buckets.

If any of below happens, the OpenTelemetry ingest API returns the `400` or `200 with partial success` responses.

* Cumulative histograms aren't ingested (similarly to cumulative counters).
* Histogram data points without sum aren't ingested. This happens when negative values are recorded.
* Histogram buckets are not sorted.
* Histogram bucket boundary values of `NaN` or `Infinite` are invalid.

The Dynatrace OpenTelemetry ingest API only returns an HTTP `400` when all metrics in the OTLP request are invalid.

### Summaries

Dynatrace does not support summary metrics.

Summary metrics only exist in the OpenTelemetry protocol (OTLP) for compatibility with other formats.
Applications using official OpenTelemetry SDKs cannot produce summary metrics.