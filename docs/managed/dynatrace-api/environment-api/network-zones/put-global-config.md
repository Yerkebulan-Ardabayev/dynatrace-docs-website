---
title: Network zones API - PUT global configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/network-zones/put-global-config
---

# Network zones API - PUT global configuration

# Network zones API - PUT global configuration

* Reference
* Published Apr 20, 2020

Updates the global configuration of network zones in your environment.

The request consumes an `application/json` payload.

|  |  |
| --- | --- |
| PUT | * SaaS https://{your-environment-id}.live.dynatrace.com/api/v2/networkZoneSettings |

## Authentication

To execute this request, you need the **Write network zones** (`networkZones.write`) permission assigned to your API token. To learn how to obtain and use it, see [Authentication](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [NetworkZoneSettings](#openapi-definition-NetworkZoneSettings) | The JSON body of the request. Contains global configuration of network zones. | body | Required |

### Request body objects

#### The `NetworkZoneSettings` object

Global network zone configuration.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| networkZonesEnabled | boolean | Network zones feature is enabled (`true`) or disabled (`false`). | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"networkZonesEnabled": true



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The global network zones configuration has been updated. Response doesn't have a body. |
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

* [Network zones](/managed/manage/network-zones "Find out how network zones work in Dynatrace.")