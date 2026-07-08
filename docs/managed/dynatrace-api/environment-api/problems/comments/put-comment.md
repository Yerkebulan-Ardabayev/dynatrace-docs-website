---
title: Problems API - PUT a comment
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/problems/comments/put-comment
---

# Problems API - PUT a comment

# Problems API - PUT a comment

* Reference
* Updated on Jun 13, 2022
* Deprecated

This API is deprecated. Use the [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers.") instead.

Updates an existing comment on the specified problem. A field omitted from the body remains unaffected.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/problem/details/{problemId}/comments/{commentId}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/problem/details/{problemId}/comments/{commentId}` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| problemId | string | The ID of the problem where you want to edit the comment. | path | Required |
| commentId | string | The ID of the comment you want to edit. | path | Required |
| body | [PushProblemComment](#openapi-definition-PushProblemComment) | JSON body of the request, containing the updated comment. | body | Optional |

### Request body objects

#### The `PushProblemComment` object

A comment of a problem

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| comment | string | A comment on the problem. | Required |
| context | string | The context of the comment. It can contain any additional information. | Optional |
| user | string | The author of the comment. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"comment": "This is a comment!",



"context": "Slack",



"user": "user1"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ProblemComment](#openapi-definition-ProblemComment) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

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



"content": "string",



"context": "string",



"createdAtTimestamp": 1,



"id": "string",



"userName": "string"



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

## Example

In this example, the request updates the comment with ID **-6026872125973307382\_1538400720000** on the problem with ID **2307087411653364173\_1538400720000V2**.

The update provides additional information for **context**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X PUT \



https://mySampleEnv.live.dynatrace.com/api/v1/problem/details/2307087411653364173_1538400720000V2/comments/-6026872125973307382_1538400720000 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"comment": "This one is probably caused by network",



"user": "john.smith",



"context": "Slack - by Tom Johnson"



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/problem/details/2307087411653364173_1538400720000V2/comments/-6026872125973307382_1538400720000
```

#### Request body

```
{



"comment": "This one is probably caused by network",



"context": "Slack - by Tom Johnson"



}
```

#### Response body

```
{



"id": "-6026872125973307382_1538400720000",



"createdAtTimestamp": 1538559856030,



"content": "This one is probably caused by network",



"userName": "john.smith",



"context": "Slack - by Tom Johnson"



}
```

#### Response code

200

## Related topics

* [Davis® AI](/managed/dynatrace-intelligence "Learn how Davis® AI detects performance anomalies, identifies root causes, and uses AI models for adaptive thresholds across your environment.")