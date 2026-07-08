---
title: Service-level objectives API - POST an SLO alert
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/service-level-objectives-classic/post-slo-alert
---

# Service-level objectives API - POST an SLO alert

# Service-level objectives API - POST an SLO alert

* Reference
* Updated on Jan 07, 2025

Creates a new service-level objective (SLO) alert.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/slo/{id}/alert` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/slo/{id}/alert` |

## Authentication

To execute this request, you need an access token with `slo.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| from | string | The start of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the relative timeframe of two weeks is used (`now-2w`). | query | Optional |
| to | string | The end of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the current timestamp is used. | query | Optional |
| timeFrame | string | The timeframe to calculate the SLO values:  * `CURRENT`: SLO's own timeframe. * `GTF`: timeframe specified by **from** and **to** parameters.  If not set, the `CURRENT` value is used. The element can hold these values * `CURRENT` * `GTF` | query | Optional |
| id | string | The ID of the required SLO. | path | Required |
| body | [AbstractSloAlertDto](#openapi-definition-AbstractSloAlertDto) | The JSON body of the request. Contains the parameters of the new SLO alert. | body | Required |

### Request body objects

#### The `AbstractSloAlertDto` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| alertName | string | Name of the alert. | Required |
| alertThreshold | number | Threshold of the alert. Status alerts trigger if they fall below this value, burn rate alerts trigger if they exceed the value. | Required |
| alertType | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `BURN_RATE` -> BurnRateAlert * `STATUS` -> StatusAlert The element can hold these values * `BURN_RATE` * `STATUS` | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"alertName": "Payment service availability burn rate alert",



"alertThreshold": 10,



"alertType": "BURN_RATE"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Success. The new alert has been created. The response contains the parameters of the new alert. The **location** response header contains the ID of the new alert. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The requested resource doesn't exist. |
| **412** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Precondition for creating an SLO alert not fulfilled. The SLO func metric cannot be created or is not created by the SLO. |
| **500** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Internal server error. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

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

## Related topics

* [Service-Level Objectives](/managed/deliver/service-level-objectives-classic "Monitor and alert on service-level objectives with Dynatrace in Service-Level Objectives Classic.")