---
title: Vulnerabilities API - PUT mute or unmute a remediation item
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/application-security/vulnerabilities/put-remediation-items
scraped: 2026-02-18T05:43:41.247083
---

# Vulnerabilities API - PUT mute or unmute a remediation item

# Vulnerabilities API - PUT mute or unmute a remediation item

* Reference
* Updated on May 03, 2022

Set the mute status of a [remediation tracking](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Track the remediation progress of vulnerabilities.") process group or, in the case of Kubernetes vulnerabilities, of a remediation tracking Kubernetes node, to `mute` or `unmute`.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/securityProblems/{id}/remediationItems/{remediationItemId}/muteState` |
| PUT | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems/{remediationItemId}/muteState` |

## Authentication

To execute this request, you need an access token with `securityProblems.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the requested third-party security problem. | path | Required |
| remediationItemId | string | The ID of the remediation item. | path | Required |
| body | [RemediationItemMuteStateChange](#openapi-definition-RemediationItemMuteStateChange) | The JSON body of the request. Contains the mute state information to be applied. | body | Optional |

### Request body objects

#### The `RemediationItemMuteStateChange` object

An updated configuration of the remediation item's mute state.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| comment | string | A comment about the mute state change reason. | Required |
| muted | boolean | The desired mute state of the remediation item. | Required |
| reason | string | The reason for the mute state change. The element can hold these values * `AFFECTED` * `CONFIGURATION_NOT_AFFECTED` * `FALSE_POSITIVE` * `IGNORE` * `INITIAL_STATE` * `OTHER` * `VULNERABLE_CODE_NOT_IN_USE` | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"comment": "string",



"muted": true,



"reason": "IGNORE"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | - | Success. The requested mute state has been applied to the remediation item. |
| **204** | - | Not executed. The remediation item was previously put into the requested mute state by the same user with the same reason and comment. |
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

## Example

Mute the `PROCESS_GROUP-70DF2C1374244F5A` remediation item of the `8788643471842202915` vulnerability from the [GET request example](/docs/dynatrace-api/environment-api/application-security/vulnerabilities/get-remediation-items#example "View the list of remediation items of a vulnerability via Dynatrace API."). The response code of **200** indicates a successful request.

#### Curl

```
curl --request PUT \



--url https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/8788643471842202915/remediationItems/PROCESS_GROUP-70DF2C1374244F5A/muteState \



--header 'Authorization: Api-Token [your_token]' \



--header 'Content-Type: application/json' \



--data '{



"muted": true,



"reason": "OTHER",



"comment": "API test"



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/8788643471842202915/remediationItems/PROCESS_GROUP-70DF2C1374244F5A/muteState
```

#### Request body

```
{



"muted": true,



"reason": "OTHER",



"comment": "API test"



}
```

#### Response code

200

## Related topics

* [Application Security](/docs/secure/application-security "Access the Dynatrace Application Security functionalities.")
* [Davis Security Advisor API](/docs/dynatrace-api/environment-api/application-security/davis-security-advice "View the Davis Security Advisor recommendations via Dynatrace API.")
* [Remediation tracking](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Track the remediation progress of vulnerabilities.")