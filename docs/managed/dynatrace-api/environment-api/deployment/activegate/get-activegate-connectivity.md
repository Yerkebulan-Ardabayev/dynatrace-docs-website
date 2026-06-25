---
title: Deployment API - GET connectivity information for ActiveGate
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/deployment/activegate/get-activegate-connectivity
scraped: 2026-05-12T11:36:33.286160
---

# Deployment API - GET connectivity information for ActiveGate

# Deployment API - GET connectivity information for ActiveGate

* Reference
* Published Jul 02, 2020

Gets the connectivity information for ActiveGate.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/installer/gateway/connectioninfo` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/deployment/installer/gateway/connectioninfo` |

## Authentication

To execute this request, you need an access token with `InstallerDownload` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| networkZone | string | The network zone you want the result to be configured with. | query | Optional |
| defaultZoneFallback | boolean | Set `true` to perform a fallback to the default network zone if the provided network zone does not exist. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ActiveGateConnectionInfo](#openapi-definition-ActiveGateConnectionInfo) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ActiveGateConnectionInfo` object

Connectivity information for an Environment ActiveGate (except ActiveGate tokens)

| Element | Type | Description |
| --- | --- | --- |
| communicationEndpoints | string | - |
| tenantToken | string | - |
| tenantUUID | string | - |

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



"communicationEndpoints": "string",



"tenantToken": "string",



"tenantUUID": "string"



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