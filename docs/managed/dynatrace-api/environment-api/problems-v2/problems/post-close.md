---
title: Problems API v2 - POST close a problem
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/problems-v2/problems/post-close
scraped: 2026-05-12T11:57:25.245245
---

# Problems API v2 - POST close a problem

# Problems API v2 - POST close a problem

* Reference
* Published Oct 12, 2020

Closes the specified problem and adds the closing comment.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/problems/{problemId}/close` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/problems/{problemId}/close` |

## Authentication

To execute this request, you need an access token with `problems.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| problemId | string | The ID of the required problem. | path | Required |
| body | [ProblemCloseRequestDtoImpl](#openapi-definition-ProblemCloseRequestDtoImpl) | The JSON body of the request. Contains the closing comment on the problem. | body | Optional |

### Request body objects

#### The `ProblemCloseRequestDtoImpl` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| message | string | The text of the closing comment. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"message": "string"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ProblemCloseResult](#openapi-definition-ProblemCloseResult) | Success |
| **204** | - | The problem is closed already the request hasn't been executed. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ProblemCloseResult` object

The result of closing a problem.

| Element | Type | Description |
| --- | --- | --- |
| closeTimestamp | integer | The timestamp when the user triggered the closing. |
| closing | boolean | True, if the problem is being closed. |
| comment | [Comment](#openapi-definition-Comment) | The comment to a problem. |
| problemId | string | The ID of the problem. |

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



"closeTimestamp": 1,



"closing": true,



"comment": {



"authorName": "string",



"content": "string",



"context": "string",



"createdAtTimestamp": 1,



"id": "string"



},



"problemId": "string"



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