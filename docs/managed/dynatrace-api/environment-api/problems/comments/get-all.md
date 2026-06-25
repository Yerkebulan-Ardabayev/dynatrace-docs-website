---
title: Problems API - GET all
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/problems/comments/get-all
scraped: 2026-05-12T12:08:10.021734
---

# Problems API - GET all

# Problems API - GET all

* Reference
* Updated on Jun 13, 2022
* Deprecated

This API is deprecated. Use the [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers.") instead.

Lists all comments on the specified problem.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/problem/details/{problemId}/comments` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/problem/details/{problemId}/comments` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| problemId | string | The ID of the problem where you want to read the comments. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ProblemCommentList](#openapi-definition-ProblemCommentList) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ProblemCommentList` object

The list of comments to the problem.

| Element | Type | Description |
| --- | --- | --- |
| comments | [ProblemComment[]](#openapi-definition-ProblemComment) | The list of comments to the problem. |

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



"comments": [



{



"content": "string",



"context": "string",



"createdAtTimestamp": 1,



"id": "string",



"userName": "string"



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

## Example

In this example, the request lists all comments on the problem with ID **2307087411653364173\_1538400720000V2**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/problem/details/2307087411653364173_1538400720000V2/comments \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/problem/details/2307087411653364173_1538400720000V2/comments
```

#### Response body

```
{



"comments": [



{



"id": "2216103859600298777_1538400720000",



"createdAtTimestamp": 1538568145285,



"content": "Checking [stack overflow](https://stackoverflow.com) for helpful answers",



"userName": "john.smith",



"context": null



}



]



}
```

#### Response code

200

## Related topics

* [DavisÂ® AI](/managed/dynatrace-intelligence "Get familiar with the capabilities of Davis AI.")