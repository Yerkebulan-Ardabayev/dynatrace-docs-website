---
title: Ingest OTLP traces
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/otlp-api/ingest-traces
---

# Ingest OTLP traces

# Ingest OTLP traces

* Reference
* 1-min read
* Updated on Sep 29, 2026

The following reference covers the ingestion limits and supported attribute types for OTLP trace ingest in Dynatrace.

## Ingestion limits

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

## Supported attribute types

Dynatrace supports all OTLP attribute value types in trace ingest, including all primitive types and the complex types introduced in [OTEP 4485﻿](https://opentelemetry.io/blog/2025/complex-attribute-types/): maps, heterogeneous arrays, byte arrays, and null values.

| Type | Description |
| --- | --- |
| `string` | UTF-8 string value. |
| `bool` | Boolean value (`true` or `false`). |
| `int` | 64-bit signed integer. |
| `double` | 64-bit double-precision floating-point number. |
| `bytes` | Byte array. |
| `array` | Array whose elements can be any attribute value type, including heterogeneous values. |
| `kvlist` | Key-value list (map), where each key is a string and each value can be any attribute value type, including nested `kvlist` values. |
| `null` | Empty (null) value. |

Once ingested, all attribute value types, including complex ones, are preserved and available for querying with [Dynatrace Query Language (DQL)](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").

Complex attributes are only supported in Latest Dynatrace.