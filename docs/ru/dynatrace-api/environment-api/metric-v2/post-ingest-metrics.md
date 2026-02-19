---
title: Metrics API - POST ingest data points
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics
scraped: 2026-02-19T21:34:51.934398
---

# Metrics API - POST ingest data points

# Metrics API - POST ingest data points

* Reference
* Published Aug 21, 2020

Pushes custom data points to Dynatrace.

You can access the ingested datapoints via:

* [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.")
* [GET metric data points](/docs/dynatrace-api/environment-api/metric-v2/get-data-points "Read data points of one or multiple metrics via Metrics v2 API.") request of the Metric v2 API.

Provided data points must follow the [Metrics ingestion protocol](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Learn how the data ingestion protocol for Dynatrace Metrics API works."). You don't have to register the metric first. After Dynatrace has ingested and processed the data, you can use it just like any other metrics in Dynatrace, such as in [charts](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") or [metric events](/docs/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace"). You can also provide [metadata](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/custom-metric-metadata "Provide metadata for your custom metric.") for the ingested metric via the Settings API.

Prefer to ingest metrics right on the host?

You can also push the data points directly from a OneAgent-monitored host to the Extensions Execution Controller (EEC) OneAgent module over a secure channel using the local `http://localhost:<port>/metrics/ingest` endpoint, which doesn't require token authentication. The default port is `14499`. Using this method, the Dynatrace reserved `dt.entity.host=<host-ID>` dimension is added to each metric.

You can use the dimension `dt.process.id=<PID>` to add a process group identifier dimension. When the process group identifier is provided, `dt.entity.process_group_instance` dimension will be added to a given metric. It works on OneAgent metrics ingest only via [`dynatrace_ingest`](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-pipe "Learn how to ingest metrics using local scripting integration.") API.

For more information, see [OneAgent metric API](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Use the Dynatrace API to retrieve the metrics of monitored entities.").

You can't ingest metrics with key prefix of `dt.`âthese are reserved for usage by Dynatrace.

The request consumes a `text/plain` payload. The payload is limited to 1 MB.

There's no limit on the number of metrics.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/metrics/ingest` |
| POST | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/metrics/ingest` |

## Authentication

To execute this request, you need an access token with `metrics.ingest` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | string | Data points, provided in the [line protocolï»¿](https://dt-url.net/5d63ic1). Each line represents a single data point. | body | Required |

### Request body objects

#### The `RequestBody` object

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **202** | [ValidationResponse](#openapi-definition-ValidationResponse) | The provided metric data points are accepted and will be processed in the background. |
| **400** | [ValidationResponse](#openapi-definition-ValidationResponse) | Some data points are invalid. Valid data points are accepted and will be processed in the background. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ValidationResponse` object

| Element | Type | Description |
| --- | --- | --- |
| error | [MetricIngestError](#openapi-definition-MetricIngestError) | - |
| linesInvalid | integer | - |
| linesOk | integer | - |
| warnings | [Warnings](#openapi-definition-Warnings) | - |

#### The `MetricIngestError` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | - |
| invalidLines | [InvalidLine[]](#openapi-definition-InvalidLine) | - |
| message | string | - |

#### The `InvalidLine` object

| Element | Type | Description |
| --- | --- | --- |
| error | string | - |
| line | integer | - |

#### The `Warnings` object

| Element | Type | Description |
| --- | --- | --- |
| changedMetricKeys | [WarningLine[]](#openapi-definition-WarningLine) | - |
| message | string | - |

#### The `WarningLine` object

| Element | Type | Description |
| --- | --- | --- |
| line | integer | - |
| warning | string | - |

### Response body JSON models

```
{



"error": {



"code": 1,



"invalidLines": [



{



"error": "string",



"line": 1



}



],



"message": "string"



},



"linesInvalid": 1,



"linesOk": 1,



"warnings": {



"changedMetricKeys": [



{



"line": 1,



"warning": "string"



}



],



"message": "string"



}



}
```

## Example

With this `curl` command, you'll ingest the `cpu.temperature` metric assigned to the `HOST-06F288EE2A930951` dimension.

```
curl -L -X POST 'https://mySampleEnv.live.dynatrace.com/api/v2/metrics/ingest' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: text/plain' \



--data-raw 'cpu.temperature,dt.entity.host=HOST-06F288EE2A930951,cpu=1 55'
```

## Related topics

* [Metric ingestion protocol](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Learn how the data ingestion protocol for Dynatrace Metrics API works.")
* [Custom metric metadata](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/custom-metric-metadata "Provide metadata for your custom metric.")