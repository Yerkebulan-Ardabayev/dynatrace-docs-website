---
title: About OTLP metrics ingest
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest
scraped: 2026-02-27T21:28:28.588007
---

# About OTLP metrics ingest

# About OTLP metrics ingest

* Latest Dynatrace
* Explanation
* 2-min read
* Updated on Feb 18, 2026

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

When ingesting OpenTelemetry metrics, limits and validations apply as described in the tables below.

* When [Metrics powered by Grail overview (DPS)](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.") is on your rate card:

  + Latest Dynatrace If **Advanced OTLP metric dimensions** is configured, the limits in **Advanced OTLP Metric dimensions limits** apply.
  + If **Advanced OTLP metric dimensions** is not configured, the limits in **Default limits** apply.
* When [Custom Metrics Classic (DPS)](/docs/license/capabilities/platform-extensions/custom-metrics-classic "Learn how your consumption of the Dynatrace Custom Metrics Classic DPS capability is billed and charged.") is on your rate card, the limits in **Default limits** apply

For more information about advanced OTLP metric dimensions, see [Important: OTLP Metric Dimensions Changesï»¿](https://community.dynatrace.com/t5/Product-news/Important-OTLP-Metric-Dimensions-Changes/ba-p/293109) in the Dynatrace Community.

Default limits

Advanced OTLP metric dimensions limits

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