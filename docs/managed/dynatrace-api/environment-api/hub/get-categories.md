---
title: Hub capabilities API - GET categories
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/hub/get-categories
scraped: 2026-05-12T11:54:40.791115
---

# Hub capabilities API - GET categories

# Hub capabilities API - GET categories

* Reference
* Published Feb 07, 2023

Lists all available categories of Hub items.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/hub/categories` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/hub/categories` |

## Authentication

To execute this request, you need an access token with `hub.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [CategoryList](#openapi-definition-CategoryList) | OK |
| **503** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Unavailable |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `CategoryList` object

| Element | Type | Description |
| --- | --- | --- |
| items | [Category[]](#openapi-definition-Category) | A list of available categories. |

#### The `Category` object

A list of available categories.

| Element | Type | Description |
| --- | --- | --- |
| description | string | Description of the category |
| id | string | Id of the category |
| name | string | Name of the category |

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



"items": [



{



"description": "string",



"id": "string",



"name": "string"



}



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