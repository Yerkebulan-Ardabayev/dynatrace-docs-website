---
title: Hub capabilities API - GET an extension v1 artifact
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/hub/get-extension-v1-artifact
---

# Hub capabilities API - GET an extension v1 artifact

# Hub capabilities API - GET an extension v1 artifact

* Reference
* Published Feb 07, 2023

Downloads the ZIP file of a version 1 extension.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/hub/extensions1/{extension1FQN}/releases/{version}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/hub/extensions1/{extension1FQN}/releases/{version}` |

## Authentication

To execute this request, you need an access token with `hub.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| extension1FQN | string | Fully qualified name of the extension1/plugin | path | Required |
| version | string | Version of the release of the extension1/plugin | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | - | Ok - download file |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Not found |
| **503** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Unavailable |
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