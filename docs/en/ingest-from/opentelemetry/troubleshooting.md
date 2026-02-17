---
title: Ensure success with OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/troubleshooting
scraped: 2026-02-17T21:24:28.367468
---

# Ensure success with OpenTelemetry

# Ensure success with OpenTelemetry

* Latest Dynatrace
* Troubleshooting
* 1-min read
* Updated on Dec 03, 2025

Successfully implementing OpenTelemetry requires both reliable data export and proper visualization in Dynatrace.
This page offers guidance for properly configuring and troubleshooting your OpenTelemetry implementation with Dynatrace.

## Metrics for ingest monitoring

Dynatrace provides the following built-in metrics for the ingestion of OpenTelemetry signals.
In case of missing data, these can be useful in further analyzing possible ingestion issues.

In Dynatrace Classic, ingest monitoring metrics are prefixed with `dsfm:` instead of `dt.sfm.`

### Metrics for logs ingest

Latest Dynatrace

| Name | Description |
| --- | --- |
| `dt.sfm.active_gate.event_ingest.event_incoming_count` | Number of ingested log records |
| `dt.sfm.active_gate.event_ingest.drop_count` | Number of dropped log records |
| `dt.sfm.active_gate.event_ingest.event_otlp_size` | Payload size of received log requests |

### Metrics for metrics ingest

Latest Dynatrace

| Name | Description |
| --- | --- |
| `dt.sfm.active_gate.metrics.ingest.otlp.datapoints.accepted` | Number of accepted data points |
| `dt.sfm.active_gate.metrics.ingest.otlp.datapoints.rejected` | Number of rejected data points |

Rejected metrics come with a `reason` dimension, which provides additional details on why a data point was rejected.
In Dynatrace, you can filter, sort, and split by that dimension.

A typical reason is when metrics are sent with cumulative aggregation temporality (Dynatrace [requires delta temporality](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#aggregation-temporality "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")), in which case `reason` indicates `UNSUPPORTED_METRIC_TYPE_MONOTONIC_CUMULATIVE_SUM`.

### Metrics for traces ingest

Latest Dynatrace

| Name | Description |
| --- | --- |
| `dt.sfm.server.spans.received` | Number of OpenTelemetry spans ingested via the OLTP trace endpoint (ActiveGate or OneAgent) that were successfully received by Dynatrace |
| `dt.sfm.server.spans.persisted` | Number of OpenTelemetry spans preserved by Dynatrace; only preserved spans are available for distributed traces analysis |
| `dt.sfm.server.spans.dropped` | Number of OpenTelemetry spans that were not preserved by Dynatrace because of the indicated reason (for example, span end time out of range) |

## Common issues and solutions

### Setup issues

* [I'm having setup issues with OpenTelemetry. What should I check?ï»¿](https://dt-url.net/dm038xt)
* [Fixing SSL Errors in OpenTelemetry SDKs when exporting to Dynatrace ActiveGateï»¿](https://community.dynatrace.com/t5/Troubleshooting/Fixing-SSL-Errors-in-OpenTelemetry-SDKs-when-exporting-to/ta-p/269404)

### Connection issues

* [Why do I get a connection error when exporting with OTLP to ActiveGate?ï»¿](https://dt-url.net/x0238hc)
* [Why do I get a connection error when exporting OpenTelemetry traces to OneAgent?ï»¿](https://dt-url.net/tk4384x)

### Authentication issues

* Problem: HTTP 401/403 errors in ingestion metrics.
* Solution: Verify API permissions and endpoint configurations.

See also:

* [Why does ActiveGate return a 401 Unauthorized error?ï»¿](https://dt-url.net/lg638i3)
* [Why does ActiveGate return a 403 Forbidden error?ï»¿](https://dt-url.net/2n838im)

### Data format issues

* Problem: High drop rates with format errors.
* Solution: Validate OpenTelemetry data format compliance and attribute limits.

### Configuration issues

* Problem: No data appears despite successful exports.
* Solution: Verify endpoint URLs, headers, and protocol configuration.

### Ingestion issues

* [Why does my OTLP export not work?ï»¿](https://dt-url.net/sb238k5)
* [Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Vertical topology

* [Why is my vertical topology missing?ï»¿](https://dt-url.net/48038un)

## Signal-specific questions

Specific information about ingesting each signal type is available at

* [Ingest OTLP logs](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")
* [About OTLP metrics ingest](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Ingest OTLP traces](/docs/ingest-from/opentelemetry/otlp-api/ingest-traces "Learn how Dynatrace ingests OpenTelemetry traces and what limitations apply.")

### Traces

* [Why are my spans not linked? Why are my spans orphaned?ï»¿](https://dt-url.net/ae038vj)
* [Why are my OpenTelemetry span attributes missing?ï»¿](https://dt-url.net/z402yxq)

### Metrics

* [Why are my metrics not ingested?ï»¿](https://community.dynatrace.com/t5/Troubleshooting/Why-are-my-OpenTelemetry-metrics-not-ingested/ta-p/269428)
* [Why are my cumulative metrics not ingested?ï»¿](https://dt-url.net/s60382e)
* [Why do I receive a "Partial Success" response?ï»¿](https://dt-url.net/0u238ec)
* [Why are my metric attributes missing?ï»¿](https://dt-url.net/jj03800)
* [How to set up OpenTelemetry metrics with delta temporalityï»¿](https://community.dynatrace.com/t5/Troubleshooting/How-to-set-up-OpenTelemetry-metrics-with-delta-temporality/ta-p/269292)
* [Delay in displaying OpenTelemetry metric dimensions in Dynatraceï»¿](https://community.dynatrace.com/t5/Troubleshooting/Delay-in-displaying-OpenTelemetry-metric-dimensions-in-Dynatrace/ta-p/269732)
* [Why are my OpenTelemetry metrics not ingestedï»¿](https://community.dynatrace.com/t5/Troubleshooting/Why-are-my-OpenTelemetry-metrics-not-ingested/ta-p/269428)

## Best practices

### Use metric dimensions

Dimensions are used in Dynatrace to help distinguish what is being measured in a specific data point.

In OpenTelemetry, dimensions are called attributes.

For example, if you're measuring the number of requests an endpoint has received, you can use dimensions to split that metric into requests that went through (status code 200) and requests that failed (status code 500).

Your dimensions should be well-annotated (recognizable, readable, understandable), have descriptive names, and provide good information.

### Compression

Dynatrace recommends that you enable `gzip` compression on your OTLP exporters.

The default compression on the OTLP exporter [is not setï»¿](https://opentelemetry.io/docs/specs/otel/protocol/exporter/), but it can be configured through the following environment variables:

* `OTEL_EXPORTER_OTLP_COMPRESSION`
* `OTEL_EXPORTER_OTLP_TRACES_COMPRESSION`
* `OTEL_EXPORTER_OTLP_METRICS_COMPRESSION`
* `OTEL_EXPORTER_OTLP_LOGS_COMPRESSION`

Acceptable values are `none` or `gzip`.

### Batching

If you use the OpenTelemetry Collector, we highly recommend that you use a [batch processorï»¿](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.145.0/processor/batchprocessor/README.md).

Batching helps better compress the data and reduce the number of outgoing connections required to transmit data to Dynatrace.

See this [GitHub readmeï»¿](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.145.0/processor/batchprocessor/README.md) for more information.