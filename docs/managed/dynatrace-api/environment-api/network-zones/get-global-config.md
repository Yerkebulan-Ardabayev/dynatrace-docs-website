---
title: Network zones API - GET global configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/network-zones/get-global-config
---

# Network zones API - GET global configuration

# Network zones API - GET global configuration

* Reference
* Published Mar 05, 2020

Gets the global configuration of network zones in your environment.

The request produces an `application/json` payload.

|  |  |
| --- | --- |
| GET | * SaaS https://{your-environment-id}.live.dynatrace.com/api/v2/networkZoneSettings |

## Authentication

To execute this request, you need the **Read network zones** (`networkZones.read`) permission assigned to your API token. To learn how to obtain and use it, see [Authentication](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [NetworkZoneSettings](#openapi-definition-NetworkZoneSettings) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `NetworkZoneSettings` object

Global network zone configuration.

| Element | Type | Description |
| --- | --- | --- |
| networkZonesEnabled | boolean | Network zones feature is enabled (`true`) or disabled (`false`). |

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



"networkZonesEnabled": true



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

* [Network zones](/managed/manage/network-zones "Find out how network zones work in Dynatrace.")