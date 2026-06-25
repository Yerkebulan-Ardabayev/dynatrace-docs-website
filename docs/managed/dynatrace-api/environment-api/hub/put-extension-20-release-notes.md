---
title: Hub capabilities API - PUT an extension 2.0 release notes
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/hub/put-extension-20-release-notes
scraped: 2026-05-12T11:54:57.120943
---

# Hub capabilities API - PUT an extension 2.0 release notes

# Hub capabilities API - PUT an extension 2.0 release notes

* Reference
* Published Feb 07, 2023

Sets the release notes of an extension 2.0 release. Any notes are overwritten.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/hub/extensions2/{extensionName}/releases/{version}/releaseNotes` |
| PUT | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/hub/extensions2/{extensionName}/releases/{version}/releaseNotes` |

## Authentication

To execute this request, you need an access token with `hub.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| extensionName | string | Fully qualified name of the extension | path | Required |
| version | string | Version of the extension release | path | Required |
| body | [ExtensionReleaseNotes](#openapi-definition-ExtensionReleaseNotes) | The JSON body of the request. Contains the markdown for release notes | body | Optional |

### Request body objects

#### The `ExtensionReleaseNotes` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| markdown | string | Release notes in markdown format | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"markdown": "string"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Extension release notes updated |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Bad request |
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