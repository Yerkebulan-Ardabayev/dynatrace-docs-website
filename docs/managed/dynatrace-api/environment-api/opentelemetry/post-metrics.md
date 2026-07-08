---
title: OpenTelemetry metrics ingest API
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/opentelemetry/post-metrics
---

# OpenTelemetry metrics ingest API

# OpenTelemetry metrics ingest API

* Reference
* Published Sep 12, 2022

Ingests OpenTelemetry metrics into Dynatrace. Use this endpoint as a target for OpenTelemetry exporters. For more information, see [Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

The request consumes an `application/x-protobuf` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/otlp/v1/metrics` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/metrics` |

## Authentication

To execute this request, you need an access token with `metrics.ingest` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | byte[] | An [ExportMetricsServiceRequest﻿](https://github.com/open-telemetry/opentelemetry-proto/blob/v1.2.0/opentelemetry/proto/collector/metrics/v1/metrics_service.proto) message in binary protobuf format. | body | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | - | The request has been received and will be processed. |
| **400** | - | The request could not be processed. This may happen if the message is malformed. |
| **413** | - | The OTLP message exceeded the payload size limit. |
| **415** | - | The request was sent with an unsupported content type. This API supports requests in binary protobuf format with content type application/x-protobuf. |
| **500** | - | The request could not be processed due to an internal server error. |
| **503** | - | The service is currently unavailable. This may happen if the module is paused. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

## Related topics

* [Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")