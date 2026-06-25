---
title: Hub capabilities API - POST update an extension 2.0
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/hub/post-update-extension-20
scraped: 2026-05-12T11:54:51.159299
---

# Hub capabilities API - POST update an extension 2.0

# Hub capabilities API - POST update an extension 2.0

* Reference
* Published Feb 07, 2023

Updates an extension 2.0 to the specified version. If no version is specified, the recommended version is used.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/hub/extensions2/{extensionName}/actions/update` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/hub/extensions2/{extensionName}/actions/update` |

## Authentication

To execute this request, you need an access token with `hub.install` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| extensionName | string | Fully qualified name of the extension | path | Required |
| extensionVersion | string | Version of the extension. Fallback to the evaluated recommended version when the version is not provided | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [RegisteredExtensionResultDto](#openapi-definition-RegisteredExtensionResultDto) | OK |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Bad request |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Not found |
| **503** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Unavailable |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `RegisteredExtensionResultDto` object

| Element | Type | Description |
| --- | --- | --- |
| extensionName | string | FQN of the extension registered in the tenant. |
| extensionVersion | string | Version number of the extension. |

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



"extensionName": "string",



"extensionVersion": "string"



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