---
title: Problems API v2 - GET a comment
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/problems-v2/comments/get-comment
scraped: 2026-05-12T11:57:29.372212
---

# Problems API v2 - GET a comment

# Problems API v2 - GET a comment

* Reference
* Published Oct 12, 2020

Gets the specified comment on a problem.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/problems/{problemId}/comments/{commentId}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/problems/{problemId}/comments/{commentId}` |

## Authentication

To execute this request, you need an access token with `problems.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| problemId | string | The ID of the required problem. | path | Required |
| commentId | string | The ID of the required comment. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [Comment](#openapi-definition-Comment) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `Comment` object

The comment to a problem.

| Element | Type | Description |
| --- | --- | --- |
| authorName | string | The user who wrote the comment. |
| content | string | The text of the comment. |
| context | string | The context of the comment. |
| createdAtTimestamp | integer | The timestamp of comment creation, in UTC milliseconds. |
| id | string | The ID of the comment. |

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



"authorName": "string",



"content": "string",



"context": "string",



"createdAtTimestamp": 1,



"id": "string"



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

* [DavisÂ® AI](/managed/dynatrace-intelligence "Get familiar with the capabilities of Davis AI.")