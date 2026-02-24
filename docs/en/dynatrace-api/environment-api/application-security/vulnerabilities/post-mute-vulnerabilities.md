---
title: Vulnerabilities API - POST mute vulnerabilities
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/application-security/vulnerabilities/post-mute-vulnerabilities
scraped: 2026-02-24T21:31:38.272104
---

# Vulnerabilities API - POST mute vulnerabilities

# Vulnerabilities API - POST mute vulnerabilities

* Reference
* Updated on Sep 25, 2024

Mutes multiple vulnerabilities. Muted vulnerabilities are hidden from the vulnerability list in Dynatrace.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/securityProblems/mute` |
| POST | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/mute` |

## Authentication

To execute this request, you need an access token with `securityProblems.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [SecurityProblemsBulkMute](#openapi-definition-SecurityProblemsBulkMute) | The JSON body of the request. Contains the muting information. | body | Optional |

### Request body objects

#### The `SecurityProblemsBulkMute` object

Information on muting several security problems.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| comment | string | A comment about the muting reason. | Optional |
| reason | string | The reason for muting the security problems. The element can hold these values * `CONFIGURATION_NOT_AFFECTED` * `FALSE_POSITIVE` * `IGNORE` * `OTHER` * `VULNERABLE_CODE_NOT_IN_USE` | Required |
| securityProblemIds | string[] | The ids of the security problems to be muted. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"comment": "string",



"reason": "CONFIGURATION_NOT_AFFECTED",



"securityProblemIds": [



"string"



]



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SecurityProblemsBulkMuteResponse](#openapi-definition-SecurityProblemsBulkMuteResponse) | Success. The security problem(s) have been muted. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `SecurityProblemsBulkMuteResponse` object

Response of muting several security problems.

| Element | Type | Description |
| --- | --- | --- |
| summary | [SecurityProblemBulkMutingSummary[]](#openapi-definition-SecurityProblemBulkMutingSummary) | The summary of which security problems were muted and which already were muted previously. |

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

Mute two vulnerabilities, `2919200225913269102` and `4537041069803077238`, as the configuration isn't affected.

#### Curl

```
curl -X 'POST' 'https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/mute' \



-H 'accept: application/json; charset=utf-8' \



-H 'Authorization: Api-Token [your_token]' \



-H 'Content-Type: application/json; charset=utf-8' \



-d '{



"comment": "Example mute batch",



"reason": "CONFIGURATION_NOT_AFFECTED",



"securityProblemIds": [



"2919200225913269102", "4537041069803077238"



]



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/mute
```

#### Request body

```
{



"comment": "Example mute batch",



"reason": "CONFIGURATION_NOT_AFFECTED",



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

## Related topics

* [Application Security](/docs/secure/application-security "Access the Dynatrace Application Security functionalities.")
* [Davis Security Advisor API](/docs/dynatrace-api/environment-api/application-security/davis-security-advice "View the Davis Security Advisor recommendations via Dynatrace API.")