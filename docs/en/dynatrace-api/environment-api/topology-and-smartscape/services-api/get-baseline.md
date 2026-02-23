---
title: Services API - GET baseline
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-baseline
scraped: 2026-02-23T21:21:49.954711
---

# Services API - GET baseline

# Services API - GET baseline

* Reference
* Updated on Mar 22, 2023
* Deprecated

Gets the baseline data of the specified service.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/services/{meIdentifier}/baseline` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/services/{meIdentifier}/baseline` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| meIdentifier | string | The Dynatrace entity ID of the required service. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ServiceBaselineValues](#openapi-definition-ServiceBaselineValues) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ServiceBaselineValues` object

The baseline data for a service and its children for the **Response time** duration metric.

| Element | Type | Description |
| --- | --- | --- |
| displayName | string | The display name of the service. |
| entityId | string | The ID of the service. |
| serviceResponseTimeBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for the **Response time** duration metric. |

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



"displayName": "string",



"entityId": "string",



"serviceResponseTimeBaselines": [



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



]



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

* [Services](/docs/observe/application-observability/services "Learn how to monitor and analyze your services, define and use request attributes, and more.")