---
title: Problems API - POST close
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/problems/problems/post-close
---

# Problems API - POST close

# Problems API - POST close

* Reference
* Updated on Jun 13, 2022
* Deprecated

This API is deprecated. Use the [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers.") instead.

Closes the specified problem and adds the closing comment.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/problem/details/{problemId}/close` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/problem/details/{problemId}/close` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| problemId | string | The ID of the problem to be closed. | path | Required |
| content | string | The closing comment. | query | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ProblemCloseResult](#openapi-definition-ProblemCloseResult) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ProblemCloseResult` object

The result of closing a problem.

| Element | Type | Description |
| --- | --- | --- |
| closeTimestamp | integer | The timestamp when the closure was triggered. |
| closing | boolean | The problem is in process of closing (`true`) or closed (`false`). |
| comment | [ProblemComment](#openapi-definition-ProblemComment) | The comment to the problem. |
| problemId | string | The ID of the problem. |

#### The `ProblemComment` object

The comment to the problem.

| Element | Type | Description |
| --- | --- | --- |
| content | string | The text of the comment. |
| context | string | The context of the comment.  Could be any textual comment. You can only set it via REST API. |
| createdAtTimestamp | integer | The timestamp of the comment creation, in UTC milliseconds. |
| id | string | The ID of the comment. |
| userName | string | The author of the comment. |

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



"closeTimestamp": 1,



"closing": true,



"comment": {



"content": "string",



"context": "string",



"createdAtTimestamp": 1,



"id": "string",



"userName": "string"



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

* [Davis® AI](/managed/dynatrace-intelligence "Learn how Davis® AI detects performance anomalies, identifies root causes, and uses AI models for adaptive thresholds across your environment.")