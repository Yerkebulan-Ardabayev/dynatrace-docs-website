---
title: Vulnerabilities API - POST unmute vulnerabilities
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/application-security/vulnerabilities/post-problems-unmute
scraped: 2026-02-16T09:30:15.778545
---

# Vulnerabilities API - POST unmute vulnerabilities

# Vulnerabilities API - POST unmute vulnerabilities

* Reference
* Updated on Sep 25, 2024

Unmutes multiple vulnerabilities. Unmuted vulnerabilities are displayed on the vulnerability list in Dynatrace.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/securityProblems/unmute` |
| POST | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/unmute` |

## Authentication

To execute this request, you need an access token with `securityProblems.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [SecurityProblemsBulkUnmute](#openapi-definition-SecurityProblemsBulkUnmute) | The JSON body of the request. Contains the un-muting information. | body | Optional |

### Request body objects

#### The `SecurityProblemsBulkUnmute` object

Information on un-muting several security problems.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| comment | string | A comment about the un-muting reason. | Optional |
| reason | string | The reason for un-muting the security problems. The element can hold these values * `AFFECTED` | Required |
| securityProblemIds | string[] | The ids of the security problems to be un-muted. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"comment": "string",



"reason": "AFFECTED",



"securityProblemIds": [



"string"



]



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SecurityProblemsBulkUnmuteResponse](#openapi-definition-SecurityProblemsBulkUnmuteResponse) | Success. The security problem(s) have been un-muted. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `SecurityProblemsBulkUnmuteResponse` object

Response of un-muting several security problems.

| Element | Type | Description |
| --- | --- | --- |
| summary | [SecurityProblemBulkMutingSummary[]](#openapi-definition-SecurityProblemBulkMutingSummary) | The summary of which security problems were un-muted and which already were un-muted previously. |

#### The `SecurityProblemBulkMutingSummary` object

Summary of (un-)muting a security problem.

| Element | Type | Description |
| --- | --- | --- |
| muteStateChangeTriggered | boolean | Whether a mute state change for the given security problem was triggered by this request. |
| reason | string | Contains a reason, in case the requested operation was not executed. The element can hold these values * `ALREADY_MUTED` * `ALREADY_UNMUTED` |
| securityProblemId | string | The id of the security problem that was (un-)muted. |

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



"summary": [



{



"muteStateChangeTriggered": true,



"reason": "ALREADY_MUTED",



"securityProblemId": "string"



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

Unmute two vulnerabilities, `2919200225913269102` and `4537041069803077238`.

#### Curl

```
curl -X 'POST' 'https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/unmute' \



-H 'accept: application/json; charset=utf-8' \



-H 'Authorization: Api-Token [your_token]' \



-H 'Content-Type: application/json; charset=utf-8' \



-d '{



"comment": "Example unmute bulk",



"reason": "AFFECTED",



"securityProblemIds": [



"2919200225913269102", "4537041069803077238"



]



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/unmute
```

#### Request body

```
{



"comment": "Example unmute bulk",



"reason": "AFFECTED",



"securityProblemIds": [



"2919200225913269102", "4537041069803077238"



]



}
```

#### Response body

```
{



"summary": [



{



"securityProblemId": "2919200225913269102",



"muteStateChangeTriggered": true



},



{



"securityProblemId": "4537041069803077238",



"muteStateChangeTriggered": true



}



]



}
```

Here, `muteStateChangeTriggered` indicates the success of the operation.

Note that unmuting a vulnerability can take up to one minute.

## Related topics

* [Application Security](/docs/secure/application-security "Access the Dynatrace Application Security functionalities.")
* [Davis Security Advisor API](/docs/dynatrace-api/environment-api/application-security/davis-security-advice "View the Davis Security Advisor recommendations via Dynatrace API.")