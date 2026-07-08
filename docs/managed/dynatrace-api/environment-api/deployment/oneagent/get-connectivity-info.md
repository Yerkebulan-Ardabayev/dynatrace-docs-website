---
title: Deployment API - View connectivity information for OneAgent
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/deployment/oneagent/get-connectivity-info
---

# Deployment API - View connectivity information for OneAgent

# Deployment API - View connectivity information for OneAgent

* Reference
* Published Aug 28, 2019

Gets the connectivity information for OneAgent.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/connectioninfo` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/connectioninfo` |

## Authentication

To execute this request, you need an access token with `InstallerDownload` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| networkZone | string | The network zone you want the result to be configured with. | query | Optional |
| defaultZoneFallback | boolean | Set `true` to perform a fallback to the default network zone if the provided network zone does not exist. | query | Optional |
| version | string | The version of the OneAgent for which you're requesting connectivity information, in the `1.221` format.  Set this parameter to get the best format of endpoint list for optimal performance. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ConnectionInfo](#openapi-definition-ConnectionInfo) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ConnectionInfo` object

OneAgent connectivity information.

| Element | Type | Description |
| --- | --- | --- |
| communicationEndpoints | string[] | The list of endpoints to connect to the Dynatrace environment. The list is sorted by endpoint priority, descending. |
| formattedCommunicationEndpoints | string | The formatted list of endpoints to connect to the Dynatrace environment. |
| tenantToken | string | The internal token that is used for authentication when OneAgent connects to the Dynatrace cluster to send data. |
| tenantUUID | string | The ID of your Dynatrace environment. |

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



"communicationEndpoints": [



"string"



],



"formattedCommunicationEndpoints": "string",



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