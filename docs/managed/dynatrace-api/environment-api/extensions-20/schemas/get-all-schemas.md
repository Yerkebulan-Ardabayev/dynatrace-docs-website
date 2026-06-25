---
title: Extensions 2.0 API - GET all schemas
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/extensions-20/schemas/get-all-schemas
scraped: 2026-05-12T11:56:25.161025
---

# Extensions 2.0 API - GET all schemas

# Extensions 2.0 API - GET all schemas

* Reference
* Published Jan 22, 2021

Lists all available Extensions 2.0 schema versions.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/extensions/schemas` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/extensions/schemas` |

## Authentication

To execute this request, you need an access token with `extensions.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SchemasList](#openapi-definition-SchemasList) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `SchemasList` object

| Element | Type | Description |
| --- | --- | --- |
| versions | string[] | A list of schema versions. |

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



"versions": [



"1.2.3"



]



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

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.")