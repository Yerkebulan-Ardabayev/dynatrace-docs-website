---
title: Extensions 2.0 API - GET all files
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/extensions-20/schemas/get-all-files
---

# Extensions 2.0 API - GET all files

# Extensions 2.0 API - GET all files

* Reference
* Published Jan 22, 2021

Lists all files in the specified version of the Extensions 2.0 extension schema.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/extensions/schemas/{schemaVersion}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/extensions/schemas/{schemaVersion}` |

## Authentication

To execute this request, you need an access token with `extensions.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| schemaVersion | string | The version of the schema. | path | Required |
| Accept | string | Accept header. Specifies part of the extension 2.0 that will be returned:  * application/json; charset=utf-8 - returns extension 2.0 metadata in JSON * application/octet-stream - returns extension 2.0 zip package stored on the server. | header | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SchemaFiles](#openapi-definition-SchemaFiles) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `SchemaFiles` object

| Element | Type | Description |
| --- | --- | --- |
| files | string[] | A list of schema files. |

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



"files": [



"string"



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