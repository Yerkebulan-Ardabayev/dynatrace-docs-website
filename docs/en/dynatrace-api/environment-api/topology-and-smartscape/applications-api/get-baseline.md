---
title: Applications API - GET baseline
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-baseline
scraped: 2026-02-17T04:50:37.855623
---

# Applications API - GET baseline

# Applications API - GET baseline

* Reference
* Updated on Mar 22, 2023
* Deprecated

Gets the baseline data of the specified application.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/applications/{meIdentifier}/baseline` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/applications/{meIdentifier}/baseline` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| meIdentifier | string | The Dynatrace entity ID of the required application. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ApplicationBaselineValues](#openapi-definition-ApplicationBaselineValues) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ApplicationBaselineValues` object

The baseline data for an application and its children for each available duration metric.

A duration metric is one of the following:

* **DOM interactive**
* **HTML downloaded**
* **Load event end**
* **Load event start**
* **Response time**
* **Speed index**
* **Time to first byte**
* **Visually complete**

| Element | Type | Description |
| --- | --- | --- |
| applicationDomInteractiveBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for the **DOM interactive** duration metric. |
| applicationHtmlDownloadedBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for the **HTML downloaded** duration metric. |
| applicationLoadEventEndBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for the **Load event end** duration metric. |
| applicationLoadEventStartBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for the **Load event start** duration metric. |
| applicationResponseTimeBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for the **Response time** duration metric. |
| applicationSpeedIndexBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for the **Speed index** duration metric. |
| applicationTimeToFirstByteBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for the **Time to first byte** duration metric. |
| applicationVisualCompleteBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for the **Visually complete** duration metric. |
| displayName | string | The name of the application as displayed in the UI. |
| entityId | string | The Dynatrace entity ID of the application. |

#### The `EntityBaselineData` object

The baseline data for a Dynatrace entity for a specific duration metric.

| Element | Type | Description |
| --- | --- | --- |
| childBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for child entities of this entity, for example a `SERVICE_METHOD` of a `SERVICE_METHOD_GROUP`. |
| displayName | string | The display name of the entity. |
| entityId | string | The ID of the Dynatrace entity. |
| errorRate | number | The error rate baseline. |
| hasLoadBaseline | boolean | The entity has a load baseline (`true`) or doesn't (`false`). |
| micros90thPercentile | number | The 90th percentile baseline, in microseconds. |
| microsMedian | number | The median baseline, in microseconds. |

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



"applicationDomInteractiveBaselines": [



{



"childBaselines": [



{}



],



"displayName": "string",



"entityId": "string",



"errorRate": 1,



"hasLoadBaseline": true,



"micros90thPercentile": 1,



"microsMedian": 1



}



],



"applicationHtmlDownloadedBaselines": [



{}



],



"applicationLoadEventEndBaselines": [



{}



],



"applicationLoadEventStartBaselines": [



{}



],



"applicationResponseTimeBaselines": [



{}



],



"applicationSpeedIndexBaselines": [



{}



],



"applicationTimeToFirstByteBaselines": [



{}



],



"applicationVisualCompleteBaselines": [



{}



],



"displayName": "string",



"entityId": "string"



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

## Related topics

* [Real User Monitoring](/docs/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.")