---
title: OpenTelemetry logs ingest API
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/opentelemetry/post-logs
---

# OpenTelemetry logs ingest API

# OpenTelemetry logs ingest API

* Reference
* Published Nov 09, 2023

Ingests OpenTelemetry logs into Dynatrace. Use this endpoint as a target for OpenTelemetry exporters. For more information, see [Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

The request consumes an `application/x-protobuf` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/otlp/v1/logs` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/logs` |

## Authentication

To execute this request, you need an access token with `logs.ingest` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

When using log processing with the custom processing pipeline (OpenPipeline), ingest supports all JSON data types for attribute values. This requires SaaS version 1.295+ when using the SaaS API endpoint or ActiveGate version 1.295+ when using the ActiveGate API endpoint. In all other cases, all ingested values are converted to the string type.

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| structure | string | (Optional) Data model used for structuring the input into log records. Allowed values: `raw`, `flattened`. For more details, refer to the [documentation﻿](https://dt-url.net/6y235qc). The element can hold these values * `raw` * `flattened` | query | Optional |
| X-Dynatrace-Attr | string | (Optional) Contains ampersand‑separated key–value pairs representing additional log attributes to be added to each ingested log record. If the same key appears multiple times, all values are captured as a multi‑value attribute. Query parameters take precedence over values provided in this header. For more details, refer to the [documentation﻿](https://dt-url.net/vj639p4). | header | Optional |
| X-Dynatrace-Options | string | (Optional) Contains ampersand-separated Dynatrace-specific parameters. Supported options: (SaaS only) `structure` (values: `raw`, `flattened`) defines how input data is structured into log records. Query parameters take precedence over header values. For more details, refer to the [documentation﻿](https://dt-url.net/6y235qc). | header | Optional |
| body | [ExportLogsServiceRequest](#openapi-definition-ExportLogsServiceRequest) | An ExportLogsServiceRequest message in binary protobuf format. | body | Required |

### Request body objects

#### The `ExportLogsServiceRequest` object

The [ExportLogsServiceRequest﻿](https://github.com/open-telemetry/opentelemetry-proto/blob/v1.2.0/opentelemetry/proto/collector/logs/v1/logs_service.proto)
protobuf request, as defined in the official OpenTelemetry specification, serves as the input type for the LogsService/Export RPC.

While the protocol defines the wire format, the following properties are part of the Log Data Model, which represents the structure of log records as processed within Dynatrace:

* Timestamp: Time when the event occurred.
* ObservedTimestamp: Time when the event was observed.
* TraceId: Request trace ID.
* SpanId: Request span ID.
* TraceFlags: W3C trace flag.
* SeverityText: The severity text (also known as log level).
* SeverityNumber: Numerical value of the severity.
* Body: The body of the log record.
* Resource: Describes the source of the log.
* InstrumentationScope: Describes the scope that emitted the log.
* Attributes: Additional information about the event.
* EventName: Name that identifies the class/type of event.

Log records are mapped to Dynatrace log records containing three special attributes: timestamp, loglevel, and content, as well as a map of other attributes. For more details, refer to the [documentation﻿](https://dt-url.net/6y235qc).

(SaaS only) Attribute processing depends on the data model used for input processing. The effective data model for a specific request depends on the `structure` parameter or the default tenant data model, which is determined by tenant configuration. More details can be found in the [documentation﻿](https://dt-url.net/6y235qc).

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | - | The request has been successfully accepted or partially accepted (i.e. when the server accepts only parts of the data and rejects the rest). |
| **400** | - | The request could not be processed. This may happen if the message is malformed. |
| **413** | - | The OTLP message exceeded the payload size limit. Retryable with exponential backoff strategy. |
| **500** | - | The request could not be processed due to an internal server error. |
| **502** | - | Failed. Bad Gateway. This may happen if an intermediate system (e.g., ActiveGate or a proxy) encounters an issue while forwarding the request. Retryable with exponential backoff strategy. |
| **503** | - | The service is currently unavailable. Retryable with exponential backoff strategy. |
| **504** | - | Failed. Gateway Timeout. This may occur due to an issue in the underlying infrastructure causing a delay in processing the request. Retryable with exponential backoff strategy. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

## Related topics

* [Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")