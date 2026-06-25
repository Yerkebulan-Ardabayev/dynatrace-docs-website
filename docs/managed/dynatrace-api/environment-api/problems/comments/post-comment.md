---
title: Problems API - POST a comment
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/problems/comments/post-comment
scraped: 2026-05-12T12:08:00.981989
---

# Problems API - POST a comment

# Problems API - POST a comment

* Reference
* Updated on Jun 13, 2022
* Deprecated

This API is deprecated. Use the [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers.") instead.

Adds a comments to the specified problem.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/problem/details/{problemId}/comments` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/problem/details/{problemId}/comments` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| problemId | string | The ID of the problem where you want to add the comment. | path | Required |
| body | [PushProblemComment](#openapi-definition-PushProblemComment) | JSON body of the request, containing the comment. | body | Optional |

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

In this example, the request adds a new comment on the problem with ID **2307087411653364173\_1538400720000V2**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/problem/details/2307087411653364173_1538400720000V2/comments \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"comment": "This one is probably caused by network",



"user": "john.smith",



"context": "Slack"



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/problem/details/2307087411653364173_1538400720000V2/comments
```

#### Request body

```
{



"comment": "This one is probably caused by network",



"user": "john.smith",



"context": "Slack"



}
```

#### Response body

```
{



"id": "-6026872125973307382_1538400720000",



"createdAtTimestamp": 1538559856030,



"content": "This one is probably caused by network",



"userName": "john.smith",



"context": "Slack"



}
```

#### Response code

200

## Related topics

* [DavisÂ® AI](/managed/dynatrace-intelligence "Get familiar with the capabilities of Davis AI.")