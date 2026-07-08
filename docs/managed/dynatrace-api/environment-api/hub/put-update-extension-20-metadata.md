---
title: Hub capabilities API - PUT an extension 2.0 metadata
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/hub/put-update-extension-20-metadata
---

# Hub capabilities API - PUT an extension 2.0 metadata

# Hub capabilities API - PUT an extension 2.0 metadata

* Reference
* Published Feb 07, 2023

Updates the metadata of an extension 2.0 that doesn't have Dynatrace-defined metadata. Any existing metadata is overwritten.

The request consumes a `multipart/form-data` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/hub/extensions2/{extensionName}/metadata` |
| PUT | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/hub/extensions2/{extensionName}/metadata` |

## Authentication

To execute this request, you need an access token with `hub.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| extensionName | string | Fully qualified name of the extension | path | Required |
| body | object | - | body | Optional |

### Request body objects

#### The `RequestBody` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| description | string | - | Optional |
| logo | string | Logo of the extension | Optional |
| name | string | If left empty or blank, the extension name will be used as name | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"description": "string",



"logo": "string",



"name": "string"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Extension metadata uploaded |
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