---
title: Ingest OTLP traces
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/otlp-api/ingest-traces
scraped: 2026-02-24T21:29:56.182627
---

# Ingest OTLP traces

# Ingest OTLP traces

* Latest Dynatrace
* Reference
* 1-min read
* Updated on Jul 15, 2024

The following limitations apply to OpenTelemetry trace ingest requests and ingested spans.

| Type | Limit | Description |
| --- | --- | --- |
| Span end time | 60 minutes in the past | The minimum value of the span end timestamp at time of ingestion |
| Span end time | 10 minutes in the future | The maximum value of the span end timestamp at time of ingestion |
| Number of span attributes | 128[1](#fn-1-1-def) | The maximum number of span attributes per span |
| Number of span events | 128[1](#fn-1-1-def) | The maximum number of events per span |
| Number of event attributes | 128[1](#fn-1-1-def) | The maximum number of attributes per span event |
| Number of span links | 128[1](#fn-1-1-def) | The maximum number of links per span |
| Number of link attributes | 128[1](#fn-1-1-def) | The maximum number of attributes per span link |
| Request size | 8 MB | The maximum size of an OTLP request for trace ingest to an ActiveGate (uncompressed data) |
| Request size (gzip) | 8 MB | The maximum size of an OTLP request for trace ingest to an ActiveGate (compressed data) |

1

Typical limit of the OpenTelemetry SDK. Not limited by Dynatrace.