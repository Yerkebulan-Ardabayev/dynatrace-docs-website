---
title: Problems API v2 - POST a comment
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/problems-v2/comments/post-comment
scraped: 2026-05-12T11:57:27.343705
---

# Problems API v2 - POST a comment

# Problems API v2 - POST a comment

* Reference
* Published Oct 12, 2020

Posts a comment on the specified problem.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/problems/{problemId}/comments` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/problems/{problemId}/comments` |

## Authentication

To execute this request, you need an access token with `problems.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| problemId | string | The ID of the required problem. | path | Required |
| body | [CommentRequestDtoImpl](#openapi-definition-CommentRequestDtoImpl) | The JSON body of the request. Contains the comment to be added. | body | Optional |

### Request body objects

#### The `CommentRequestDtoImpl` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| context | string | The context of the comment. | Optional |
| message | string | The text of the comment. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"context": "string",



"message": "string"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | - | Success. The comment has been added. |
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

## Related topics

* [DavisÂ® AI](/managed/dynatrace-intelligence "Get familiar with the capabilities of Davis AI.")