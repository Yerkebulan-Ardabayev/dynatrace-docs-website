---
title: Log Monitoring API v2 - POST ingest logs
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs
---

# Log Monitoring API v2 - POST ingest logs

# Log Monitoring API v2 - POST ingest logs

* Reference
* Updated on Sep 28, 2026

Pushes custom logs to Dynatrace.

This endpoint is available in your SaaS environment, or as an alternative, you can expose it on an Environmental ActiveGate with the **Log analytics collector** module enabled. This module is enabled by default on all of your ActiveGates.

The request consumes one of the following payload types:

* `text/plain`—limited to a single log event.
* `application/json`, `application/jsonl`, `application/jsonlines`, `application/jsonlines+json`, `application/x-ndjson`, `application/x-jsonlines`—support multiple log events in a single payload.

Be sure to set the correct **Content-Type** header and encode payload with **UTF-8**, for example: `application/json; charset=utf-8`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/logs/ingest` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/logs/ingest` |

## Authentication

### Api-Token:

To execute this request, you need an access token with `logs.ingest` scope.

To learn how to obtain and use it, see [Personal access tokens](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Platform Token / OAuth:

Required scope: `storage:logs:write` (legacy)

To learn how to obtain and use it, see [Platform tokens﻿](https://docs.dynatrace.com/docs/shortlink/platform-tokens) or [OAuth clients﻿](https://docs.dynatrace.com/docs/shortlink/oauth).

## Parameters

When using log processing with the custom processing pipeline (OpenPipeline), ingest supports all JSON data types for attribute values. This requires SaaS version 1.295+ when using the SaaS API endpoint or ActiveGate version 1.295+ when using the ActiveGate API endpoint. In all other cases, all ingested values are converted to the string type.

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| content-type | string | (Optional) Allows to provide content type with query parameter. Has priority over value provided in Content-Type header. | query | Optional |
| structure | string | (Optional) Data model used for structuring the input into log records. Allowed values: `raw`, `flattened`. For more details, refer to the [documentation﻿](https://dt-url.net/lyi2yte?dt=m). The element can hold these values * `raw` * `flattened` | query | Optional |
| X-Dynatrace-Attr | string | (Optional) Contains ampersand‑separated key–value pairs representing additional log attributes to be added to each ingested log record. If the same key appears multiple times, all values are captured as a multi‑value attribute. Query parameters take precedence over values provided in this header. For more details, refer to the [documentation﻿](https://dt-url.net/2f4394a?dt=m). | header | Optional |
| X-Dynatrace-Options | string | (Optional) Contains ampersand-separated Dynatrace-specific parameters. Supported options: (SaaS only) `structure` (values: `raw`, `flattened`) defines how input data is structured into log records. Query parameters take precedence over header values. For more details, refer to the [documentation﻿](https://dt-url.net/lyi2yte?dt=m). | header | Optional |
| body | [LogMessageJson](#openapi-definition-LogMessageJson) | The body of the request. Contains one or more log events to be ingested.  The endpoint accepts one of the following payload types, defined by the **Accept** header:  * `text/plain`: supports only one log event. * `application/json`: supports multiple log events in a single JSON array payload. * `application/jsonl`, `application/jsonlines`, `application/x-ndjson`, `application/jsonlines+json`, or `application/x-jsonlines`: supports multiple log events as JSON-lines payload (one JSON object per line). | body | Optional |

### Request body objects

#### The `LogMessageJson` object

A set of one or more log events:

* in JSON format:

  + an array of log events JSON objects, e.g.:

    `[ { "message": "1" }, { "message": "2" } ]`
  + a single log event JSON object, e.g.:

    `{ "message": "1" }`
* in JSON lines format: a sequence of log event JSON objects separated by new lines, e.g.:

  ```
  { "message": "1" }



  { "message": "2" }
  ```

Log events from the input are mapped to Dynatrace log records containing three special attributes: timestamp, loglevel, and content, as well as a map of other attributes. These four properties are set based on keys present in the input JSON object. For more details, refer to the [documentation﻿](https://dt-url.net/lyi2yte?dt=m).

(SaaS only) Attribute processing depends on the data model used for input processing. The effective data model for a specific request depends on the `structure` parameter or the default tenant data model, which is determined by tenant configuration. More details can be found in the [documentation﻿](https://dt-url.net/lyi2yte?dt=m).

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
[



{



"content": "Exception: Custom error log sent via Generic Log Ingest",



"log.source": "/var/log/syslog",



"timestamp": "2025-12-17T22:12:31.0000",



"severity": "error",



"custom.attribute": "attribute value",



"complex": {



"key-1": "attribute value-1",



"key-2": 234.2



},



"array.attr": [



"value-1",



1,



null,



true,



[



1,



2,



3



],



{



"key": "value"



}



]



},



{



"message": "User1 logged in successfully",



"log.source": "/var/log/syslog",



"@timestamp": "1765281600"



},



{



"payload": "Exception: Custom error log sent via Generic Log Ingest",



"log.source": "/var/log/syslog"



},



{



"log": "My log message without additional attributes"



}



]
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SuccessEnvelope](#openapi-definition-SuccessEnvelope) | Only a part of input events were ingested due to event invalidity. For details, check the response body. |
| **204** | - | Success. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **402** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. This is due either to the status of your licensing agreement or because you've exhausted your [DPS license﻿](https://www.dynatrace.com/support/help/shortlink/dynatrace-platform-subscription). |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The requested resource doesn't exist. This may happen when no ActiveGate is available with the Log Analytics Collector module enabled. |
| **413** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. Request payload size is too big. This may happen when the payload byte size exceeds the limit or when the ingested payload is a JSON array with the size exceeding the limit. |
| **429** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. Too Many Requests. This may happen when ActiveGate is unable to process more requests at the moment or when log ingest is disabled. Retryable with exponential backoff strategy. |
| **501** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The server either does not recognize the request method, or it lacks the ability to fulfil the request. In Log Monitoring Classic, this may happen when indexed log storage is not enabled. |
| **502** | - | Failed. Bad Gateway. This may happen if an intermediate system (e.g., ActiveGate or a proxy) encounters an issue while forwarding the request. Retryable with exponential backoff strategy. |
| **503** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The server is currently unable to handle the request. This may happen when ActiveGate is overloaded. Retryable with exponential backoff strategy. |
| **504** | - | Failed. Gateway Timeout. This may occur due to an issue in the underlying infrastructure causing a delay in processing the request. Retryable with exponential backoff strategy. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `SuccessEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| details | [Success](#openapi-definition-Success) | - |

#### The `Success` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| message | string | Detailed message |

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | A list of constraint violations |
| message | string | The error message |

#### The `ConstraintViolation` object

A list of constraint violations

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -The element can hold these values * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Response body JSON models

```
{



"details": {



"code": 1,



"message": "string"



}



}
```

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Example

This example ingests a JSON log event with the `content`, `status`, `service.name`, and `service.namespace` attributes. The API token is passed in the `Authorization` header. A successful request returns response code `204`.

### Curl

Platform token

Classic access token

```
curl -X POST \



https://{your-environment-id}.live.dynatrace.com/api/v2/logs/ingest \



-H 'Content-Type: application/json; charset=utf-8' \



-H 'Authorization: Bearer <your-platform-token>' \



-d '[



{



"content": "Exception: Custom error log sent via Log ingestion API",



"status": "error",



"service.name": "log-monitoring-tenant",



"service.namespace": "dev-stage-cluster"



}



]'
```

Required scope: `openpipeline:logs:ingest`

```
curl -X POST \



https://environment.activegate.domain.com:9999/e/abc123a/api/v2/logs/ingest \



-H 'Content-Type: application/json; charset=utf-8' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-d '[



{



"content": "Exception: Custom error log sent via Log ingestion API",



"status": "error",



"service.name": "log-monitoring-tenant",



"service.namespace": "dev-stage-cluster"



}



]'
```

### Response code

`204`

## Retry failed requests

API clients must retry log ingestion requests that fail on retryable errors. Each API endpoint's documentation specifies which response codes are retryable. When retrying, implement an exponential backoff strategy.

## Log data queue

You can customize the log data queue properties by editing the `custom.properties` file (see [Configuration properties and parameters of ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#generic-ingest "Learn which ActiveGate properties you can configure based on your needs and requirements.")) on your ActiveGate:

```
[generic_ingest]



#disk_queue_path=<custom_path> # defaults to temp folder



#disk_queue_max_size_mb=<limit> # defaults to 300 MB
```

503 Usable space limit reached

The log data ingestion API returns a `503 Usable space limit reached` error when the ingested log data exceeds the configured queue size. Typically, this is a temporary situation that occurs only during spikes. If this error persists, increase the value of `disk_queue_max_size_mb` in `custom.properties` to allow log ingestion spikes to be queued.

## Troubleshooting

Visit Dynatrace Community for troubleshooting guides.

* [Troubleshooting log Ingestion via API - POST ingest logs﻿](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-log-Ingestion-via-API-POST-ingest-logs/ta-p/286608)

## Related sizing guides

For detailed ActiveGate sizing recommendations based on workload profiles, see:

* [Linux ActiveGate sizing guide](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements#sizing-guide "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.")
* [Windows ActiveGate sizing guide](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-activegate-hardware-and-system-requirements#sizing-guide "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Windows for routing and monitoring.")
* [Kubernetes ActiveGate sizing guide](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits "Find CPU and memory resource recommendations for Dynatrace ActiveGates deployed in Kubernetes, sized by cluster scale and workload type.")

## Related topics

* [Unavailable in Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.")
* [Log Monitoring](/managed/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.")