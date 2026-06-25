---
title: Synthetic metrics API - POST a metric
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics/post-metric
scraped: 2026-05-12T11:19:24.203234
---

# Synthetic metrics API - POST a metric

# Synthetic metrics API - POST a metric

* Reference
* Published Apr 16, 2020

Creates a new calculated synthetic metric.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/synthetic` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/synthetic` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [CalculatedSyntheticMetric](#openapi-definition-CalculatedSyntheticMetric) | The JSON body of the request. Contains definition of the new calculated synthetic metric. | body | Optional |

### Request body objects

#### The `CalculatedSyntheticMetric` object

Definition of the calculated synthetic metric.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| dimensions | [SyntheticMetricDimension[]](#openapi-definition-SyntheticMetricDimension) | A list of metric dimensions. | Optional |
| enabled | boolean | The metric is enabled (`true`) or disabled (`false`). | Required |
| filter | [SyntheticMetricFilter](#openapi-definition-SyntheticMetricFilter) | Filter of the calculated synthetic metric. | Optional |
| metric | string | The type of the synthetic metric. The element can hold these values * `ApplicationCache` * `Callback` * `CumulativeLayoutShift` * `DNSLookup` * `DOMComplete` * `DOMContentLoaded` * `DOMInteractive` * `FailedRequestsResources` * `FirstContentfulPaint` * `FirstInputDelay` * `FirstInputStart` * `FirstPaint` * `HTMLDownloaded` * `HttpErrors` * `JavaScriptErrors` * `LargestContentfulPaint` * `LoadEventEnd` * `LoadEventStart` * `LongTasks` * `NavigationStart` * `OnDOMContentLoaded` * `OnLoad` * `Processing` * `RedirectTime` * `Request` * `RequestStart` * `ResourceCount` * `Response` * `SecureConnect` * `SpeedIndex` * `TCPConnect` * `TimeToFirstByte` * `TotalDuration` * `TransferSize` * `UserActionDuration` * `VisuallyComplete` | Required |
| metricKey | string | The unique key of the metric.  The key must have the `calc:synthetic` prefix. | Required |
| monitorIdentifier | string | The Dynatrace entity ID of the synthetic monitor to which the metric belongs. | Required |
| name | string | The name of the metric, displayed in the UI. | Required |

#### The `SyntheticMetricDimension` object

Dimension of the calculated synthetic metric.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| dimension | string | The dimension of the metric. The element can hold these values * `Event` * `Location` * `ResourceOrigin` | Required |
| topX | integer | The number of top values to be calculated. | Optional |

#### The `SyntheticMetricFilter` object

Filter of the calculated synthetic metric.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| actionType | string | Only user actions of the specified type are included in the metric calculation. The element can hold these values * `Custom` * `Load` * `Xhr` | Optional |
| errorCode | integer | Only executions finished with the specified error code are included in the metric calculation. | Optional |
| event | string | Only the specified browser clickpath event is included in the metric calculation.  Specify the Dynatrace entity ID of the event here. You can fetch the list of clickpath events of the monitor with the [GET a synthetic monitorï»¿](https://dt-url.net/4oe3kka) request from the Environment API | Optional |
| hasError | boolean | The execution status of the monitors to be included in the metric calculation:  * `true`: Only failed executions are included. * `false`: All executions are included. | Optional |
| location | string | Only executions from the specified location are included in the metric calculation.  Specify the Dynatrace entity ID of the location here. You can fetch the list of locations the monitor is running from with the [GET a synthetic monitorï»¿](https://dt-url.net/4oe3kka) request from the Environment API. | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"dimensions": [



{



"dimension": "Location"



}



],



"enabled": true,



"filter": {



"event": "SYNTHETIC_TEST_STEP-1234",



"hasError": true



},



"metric": "UserActionDuration",



"metricKey": "calc:synthetic.browser.mymetric",



"monitorIdentifier": "SYNTHETIC_TEST-1234",



"name": "MyMetric"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Success. The calculated synthetic metric has been created. Response contains its key and name. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid |

### Response body objects

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | A list of constraint violations |
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



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



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

## Validate payload

We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/synthetic/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/synthetic/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The submitted calculated synthetic metric is valid. The response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

#### Response body objects

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | A list of constraint violations |
| message | string | The error message |

#### The `ConstraintViolation` object

A list of constraint violations

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -The element can hold these values * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### Response body JSON models

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

## Related topics

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")