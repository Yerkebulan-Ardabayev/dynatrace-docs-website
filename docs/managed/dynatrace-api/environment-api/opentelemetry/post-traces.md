---
title: OpenTelemetry trace ingest API
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/opentelemetry/post-traces
scraped: 2026-05-12T12:10:38.334723
---

# OpenTelemetry trace ingest API

# OpenTelemetry trace ingest API

* Reference
* Published Feb 14, 2022

Ingests OpenTelemetry traces to Dynatrace. Use this endpoint as a target for OpenTelemetry exporters. For more information, see [Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

The request consumes an `application/x-protobuf` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/otlp/v1/traces` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/traces` |

## Authentication

To execute this request, you need an access token with `openTelemetryTrace.ingest` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | byte[] | An [ExportTraceServiceRequestï»¿](https://github.com/open-telemetry/opentelemetry-proto/blob/v1.2.0/opentelemetry/proto/collector/trace/v1/trace_service.proto) message in binary protobuf format. | body | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | - | The request has been received and will be processed. |
| **400** | - | The request could not be processed. This may happen if the message is malformed. |
| **413** | - | The OTLP message exceeded the payload size limit. |
| **415** | - | The request was sent with an unsupported content type. This API supports requests in binary protobuf format with content type application/x-protobuf. |
| **500** | - | The request could not be processed due to an internal server error. |
| **503** | - | The service is currently unavailable. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

## Limitations

* The search of traces/spans by OpenTelemetry resources attribute is limited to the **service.name**. Use the **Service name** filter on the **Distributed traces** page.
* The search of traces/spans by OpenTelemetry span attribute is limited to the span name. Use the **Request** filter on the **Distributed traces** page.

## OneAgent endpoint

In addition to the OpenTelemetry trace ingest API, OneAgent also provides a local-only OpenTelemetry endpoint for trace ingestion.

This endpoint address is `http://localhost:14499/otlp/v1/traces` at the default TCP port 14499 (configurable via [`oneagentctl`](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#set-a-custom-ingestion-port "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.")) and requires a `POST` request.

### Enable the endpoint

The endpoint is disabled by default.

Enable at the environment level

1. Go to **Settings** and select **Preferences** > **Extension Execution Controller**.
2. Turn on **Enable Extension Execution Controller**.
3. Turn on **Enable local HTTP Metric, Log and Event Ingest API**.

Enable for a host group

1. Go to **Deployment Status** > **OneAgents**.
2. On the **OneAgent deployment** page, turn off **Show new OneAgent deployments**.
3. In the **Filter by** field, enter **Host group**, and then select the host group you want to configure from the dropdown list.

   The host list is now filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name in any row.

   As you have filtered by host group, all displayed hosts go to the same host group.

5. In the host group settings, select **Extension Execution Controller**.
6. Turn on **Enable Extension Execution Controller**.

Enable for a single host

1. Go to **Hosts**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

4. In the host settings, select **Extension Execution Controller**.
5. Turn on **Enable Extension Execution Controller**.

## Comparison of ingestion API and OneAgent endpoint

| Ingestion API | OneAgent endpoint |
| --- | --- |
| * Supports all OpenTelemetry signals (traces, metrics, logs) * No automatic information enrichment * SSL and authentication | * Automatic information enrichment * No support for metrics and logs (only traces) * No authentication |

## Related topics

* [Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")