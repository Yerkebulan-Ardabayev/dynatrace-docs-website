---
title: Third-party synthetic API - POST modify state of third-party monitors
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/third-party-synthetic/post-modify-state
scraped: 2026-05-12T11:54:38.789186
---

# Third-party synthetic API - POST modify state of third-party monitors

# Third-party synthetic API - POST modify state of third-party monitors

* Reference
* Published May 15, 2020

Modifies the operation state of all third-party monitors.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/synthetic/ext/stateModifications` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/synthetic/ext/stateModifications` |

## Authentication

To execute this request, you need an access token with `ExternalSyntheticIntegration` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [StateModification](#openapi-definition-StateModification) | The JSON body of the request. Contains new operational status of third-party synthetic monitors. | body | Required |

### Request body objects

#### The `StateModification` object

Operation state to be set for all third-party Synthetic monitors

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| state | string | The new operation state for all third-party Synthetic monitors. The element can hold these values * `ACTIVE` * `HIDDEN` * `INACTIVE` | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"state": "ACTIVE"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The state of third-party monitors has been changed. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

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

In this example, the request sets the state of third-party monitors to **active**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/ext/stateModifications \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"state": "ACTIVE"



}



'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/ext/stateModifications
```

#### Request body

```
{



"state": "ACTIVE"



}
```

#### Response code

204