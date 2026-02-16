---
title: Vulnarabilities API - POST mute remediation items
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/application-security/vulnerabilities/post-remediation-items-mute
scraped: 2026-02-16T21:26:48.028446
---

# Vulnarabilities API - POST mute remediation items

# Vulnarabilities API - POST mute remediation items

* Reference
* Updated on Sep 25, 2024

Mutes multiple [remediation tracking](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Track the remediation progress of vulnerabilities.") process groups or, in the case of Kubernetes vulnerabilities, multiple remediation tracking Kubernetes nodes.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/securityProblems/{id}/remediationItems/mute` |
| POST | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems/mute` |

## Authentication

To execute this request, you need an access token with `securityProblems.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the requested third-party security problem. | path | Required |
| body | [RemediationItemsBulkMute](#openapi-definition-RemediationItemsBulkMute) | The JSON body of the request. Contains the muting information. | body | Optional |

### Request body objects

#### The `RemediationItemsBulkMute` object

Information on muting several remediation items.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| comment | string | A comment about the muting reason. | Optional |
| reason | string | The reason for muting the remediation items. The element can hold these values * `CONFIGURATION_NOT_AFFECTED` * `FALSE_POSITIVE` * `IGNORE` * `OTHER` * `VULNERABLE_CODE_NOT_IN_USE` | Required |
| remediationItemIds | string[] | The ids of the remediation items to be muted. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"comment": "string",



"reason": "CONFIGURATION_NOT_AFFECTED",



"remediationItemIds": [



"string"



]



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [RemediationItemsBulkMuteResponse](#openapi-definition-RemediationItemsBulkMuteResponse) | Success. The remediation item(s) have been muted. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `RemediationItemsBulkMuteResponse` object

Response of muting several remediation items.

| Element | Type | Description |
| --- | --- | --- |
| summary | [RemediationItemMutingSummary[]](#openapi-definition-RemediationItemMutingSummary) | The summary of which remediation items were muted and which already were muted previously. |

#### The `RemediationItemMutingSummary` object

Summary of (un-)muting a remediation item.

| Element | Type | Description |
| --- | --- | --- |
| muteStateChangeTriggered | boolean | Whether a mute state change for the given remediation item was triggered by this request. |
| reason | string | Contains a reason, in case the requested operation was not executed. The element can hold these values * `ALREADY_MUTED` * `ALREADY_UNMUTED` * `REMEDIATION_ITEM_NOT_AFFECTED_BY_GIVEN_SECURITY_PROBLEM` |
| remediationItemId | string | The id of the remediation item that will be (un-)muted. |

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



"remediationItemId": "string"



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

Mute two remediation items, `PROCESS_GROUP-46C0E12D9B0EF2D9` and `PROCESS_GROUP-549E6AD75BD598EC` as the configuration isn't affected.

#### Curl

```
curl -X 'POST' 'https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/remediationItems/mute' \



-H 'accept: application/json; charset=utf-8' \



-H 'Authorization: Api-Token [your_token]' \



-H 'Content-Type: application/json; charset=utf-8' \



-d '{



"comment": "Example muting multiple entities",



"reason": "CONFIGURATION_NOT_AFFECTED",



"remediationItemIds": ["PROCESS_GROUP-46C0E12D9B0EF2D9", "PROCESS_GROUP-549E6AD75BD598EC"]



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/remediationItems/mute
```

#### Request body

```
{



"comment": "Example muting multiple entities",



"reason": "CONFIGURATION_NOT_AFFECTED",



"remediationItemIds": ["PROCESS_GROUP-46C0E12D9B0EF2D9", "PROCESS_GROUP-549E6AD75BD598EC"]



}
```

#### Response body

```
{



"summary": [



{



"remediationItemId": "PROCESS_GROUP-549E6AD75BD598EC",



"muteStateChangeTriggered": true



},



{



"remediationItemId": "PROCESS_GROUP-46C0E12D9B0EF2D9",



"muteStateChangeTriggered": true



}



]



}
```

If the request was successful, you'll see `muteStateChangeTriggered` per entity.

## Related topics

* [Application Security](/docs/secure/application-security "Access the Dynatrace Application Security functionalities.")
* [Davis Security Advisor API](/docs/dynatrace-api/environment-api/application-security/davis-security-advice "View the Davis Security Advisor recommendations via Dynatrace API.")
* [Remediation tracking](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Track the remediation progress of vulnerabilities.")