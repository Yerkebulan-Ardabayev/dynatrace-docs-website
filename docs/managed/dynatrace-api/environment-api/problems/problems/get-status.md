---
title: Problems API - GET count
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/problems/problems/get-status
---

# Problems API - GET count

# Problems API - GET count

* Reference
* Updated on Jun 13, 2022
* Deprecated

This API is deprecated. Use the [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers.") instead.

Gets the count of problems in your environment and their distribution by impact level.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/problem/status` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/problem/status` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ProblemStatusResultWrapper](#openapi-definition-ProblemStatusResultWrapper) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ProblemStatusResultWrapper` object

| Element | Type | Description |
| --- | --- | --- |
| result | [GlobalProblemStatus](#openapi-definition-GlobalProblemStatus) | The count of open problems in your environment. |

#### The `GlobalProblemStatus` object

The count of open problems in your environment.

| Element | Type | Description |
| --- | --- | --- |
| openProblemCounts | object | Numbers of open problems per impact level. |
| totalOpenProblemsCount | integer | The total number of open problems in your environment. |

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



"result": {



"openProblemCounts": {



"APPLICATION": 1,



"ENVIRONMENT": 1,



"INFRASTRUCTURE": 1,



"SERVICE": 1



},



"totalOpenProblemsCount": 1



}



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

In this example, the request gets the number of problems in an environment.

The API token is passed in the **Authorization** header.

The response shows there are 34 problems detected:

* 4 affect the **infrastructure**.
* 30 affect **applications**.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/problem/status \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/problem/status
```

#### Response content

```
{



"result": {



"totalOpenProblemsCount": 34,



"openProblemCounts": {



"INFRASTRUCTURE": 4,



"SERVICE": 0,



"APPLICATION": 30,



"ENVIRONMENT": 0



}



}



}
```

#### Response code

200

## Related topics

* [Davis® AI](/managed/dynatrace-intelligence "Learn how Davis® AI detects performance anomalies, identifies root causes, and uses AI models for adaptive thresholds across your environment.")