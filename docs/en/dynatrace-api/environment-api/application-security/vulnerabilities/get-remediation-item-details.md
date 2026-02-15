---
title: Vulnerabilities API - GET remediation item details
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/application-security/vulnerabilities/get-remediation-item-details
scraped: 2026-02-15T09:06:43.930881
---

# Vulnerabilities API - GET remediation item details

# Vulnerabilities API - GET remediation item details

* Reference
* Updated on Sep 25, 2024

Lists the details of a [remediation tracking](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Track the remediation progress of vulnerabilities.") process group of a third-party vulnerability (or, in the case of Kubernetes vulnerabilities, the parameters of a remediation tracking Kubernetes node).

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/securityProblems/{id}/remediationItems/{remediationItemId}` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems/{remediationItemId}` |

## Authentication

To execute this request, you need an access token with `securityProblems.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the requested third-party security problem. | path | Required |
| remediationItemId | string | The ID of the remediation item. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [RemediationDetailsItem](#openapi-definition-RemediationDetailsItem) | Success. The response contains details of a single remediation item of a security problem. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `RemediationDetailsItem` object

Detailed information of a remediation item for a security problem.

| Element | Type | Description |
| --- | --- | --- |
| assessment | [RemediationAssessment](#openapi-definition-RemediationAssessment) | Assessment of the remediation item. |
| entityIds | string[] | - |
| firstAffectedTimestamp | integer | - |
| id | string | - |
| muteState | [RemediationItemMuteState](#openapi-definition-RemediationItemMuteState) | The mute state of a remediation item of a security problem. |
| name | string | - |
| remediationProgress | [RemediationProgress](#openapi-definition-RemediationProgress) | The progress of this remediation item. It contains affected and unaffected entities. |
| resolvedTimestamp | integer | - |
| trackingLink | [TrackingLink](#openapi-definition-TrackingLink) | External tracking link URL associated with the remediable entity of the security problem. |
| vulnerabilityState | string | -The element can hold these values * `RESOLVED` * `VULNERABLE` |
| vulnerableComponents | [RemediationItemDetailsVulnerableComponent[]](#openapi-definition-RemediationItemDetailsVulnerableComponent) | A list of vulnerable components of the remediation item.  A vulnerable component is what causes the security problem. |

#### The `RemediationAssessment` object

Assessment of the remediation item.

| Element | Type | Description |
| --- | --- | --- |
| assessmentAccuracy | string | The accuracy of the assessment. The element can hold these values * `FULL` * `NOT_AVAILABLE` * `REDUCED` |
| assessmentAccuracyDetails | [AssessmentAccuracyDetails](#openapi-definition-AssessmentAccuracyDetails) | The assessment accuracy details. |
| dataAssets | string | The reachability of related data assets by affected entities. The element can hold these values * `NOT_AVAILABLE` * `NOT_DETECTED` * `REACHABLE` |
| exposure | string | The level of exposure of affected entities. The element can hold these values * `NOT_AVAILABLE` * `NOT_DETECTED` * `PUBLIC_NETWORK` |
| numberOfDataAssets | integer | The number of related data assets. |
| vulnerableFunctionRestartRequired | boolean | Whether a restart is required for the latest vulnerable function data. |
| vulnerableFunctionUsage | string | The usage of vulnerable functions The element can hold these values * `IN_USE` * `NOT_AVAILABLE` * `NOT_IN_USE` |
| vulnerableFunctionsInUse | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | A list of vulnerable functions that are in use. |
| vulnerableFunctionsNotAvailable | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | A list of vulnerable functions that are not available. |
| vulnerableFunctionsNotInUse | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | A list of vulnerable functions that are not in use. |

#### The `AssessmentAccuracyDetails` object

The assessment accuracy details.

| Element | Type | Description |
| --- | --- | --- |
| reducedReasons | string[] | The reason for a reduced accuracy of the assessment. The element can hold these values * `LIMITED_AGENT_SUPPORT` * `LIMITED_BY_CONFIGURATION` |

#### The `VulnerableFunction` object

Defines an vulnerable function.

| Element | Type | Description |
| --- | --- | --- |
| className | string | The class name of the vulnerable function. |
| filePath | string | The file path of the vulnerable function. |
| functionName | string | The function name of the vulnerable function. |

#### The `RemediationItemMuteState` object

The mute state of a remediation item of a security problem.

| Element | Type | Description |
| --- | --- | --- |
| comment | string | A short comment about the most recent mute state change. |
| lastUpdatedTimestamp | integer | The timestamp (UTC milliseconds) of the last update of the mute state. |
| muted | boolean | The remediation is (`true`) or is not (`false`) muted. |
| reason | string | The reason for the most recent mute state change. The element can hold these values * `AFFECTED` * `CONFIGURATION_NOT_AFFECTED` * `FALSE_POSITIVE` * `IGNORE` * `INITIAL_STATE` * `OTHER` * `VULNERABLE_CODE_NOT_IN_USE` |
| user | string | The user who last changed the mute state. |

#### The `RemediationProgress` object

The progress of this remediation item. It contains affected and unaffected entities.

| Element | Type | Description |
| --- | --- | --- |
| affectedEntities | string[] | A list of related entities that are affected by the security problem. |
| unaffectedEntities | string[] | A list of related entities that are affected by the security problem. |

#### The `TrackingLink` object

External tracking link URL associated with the remediable entity of the security problem.

| Element | Type | Description |
| --- | --- | --- |
| displayName | string | Display name (title) set for the tracking link, e.g. 'ISSUE-123'. |
| lastUpdatedTimestamp | integer | The timestamp (UTC milliseconds) of the last update of the tracking link. |
| url | string | URL set for the tracking link, e.g. https://example.com/ISSUE-123 |
| user | string | The user who last changed the tracking link. |

#### The `RemediationItemDetailsVulnerableComponent` object

A vulnerable component with details for a remediation item (PG).

| Element | Type | Description |
| --- | --- | --- |
| affectedEntities | string[] | A list of affected entities. |
| displayName | string | The display name of the vulnerable component. |
| fileName | string | The file name of the vulnerable component. |
| id | string | The Dynatrace entity ID of the vulnerable component. |
| loadOrigins | string[] | The load origins of the vulnerable components. |
| numberOfAffectedEntities | integer | The number of affected entities. |
| shortName | string | The short, component-only name of the vulnerable component. |

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



"assessment": {



"assessmentAccuracy": "FULL",



"assessmentAccuracyDetails": {



"reducedReasons": [



"LIMITED_AGENT_SUPPORT"



]



},



"dataAssets": "NOT_AVAILABLE",



"exposure": "NOT_AVAILABLE",



"numberOfDataAssets": 1,



"vulnerableFunctionRestartRequired": true,



"vulnerableFunctionUsage": "IN_USE",



"vulnerableFunctionsInUse": [



{



"className": "string",



"filePath": "string",



"functionName": "string"



}



],



"vulnerableFunctionsNotAvailable": [



{}



],



"vulnerableFunctionsNotInUse": [



{}



]



},



"entityIds": [



"string"



],



"firstAffectedTimestamp": 1,



"id": "string",



"muteState": {



"comment": "string",



"lastUpdatedTimestamp": 1,



"muted": true,



"reason": "AFFECTED",



"user": "string"



},



"name": "string",



"remediationProgress": {



"affectedEntities": [



"string"



],



"unaffectedEntities": [



"string"



]



},



"resolvedTimestamp": 1,



"trackingLink": {



"displayName": "string",



"lastUpdatedTimestamp": 1,



"url": "string",



"user": "string"



},



"vulnerabilityState": "RESOLVED",



"vulnerableComponents": [



{



"affectedEntities": [



"string"



],



"displayName": "string",



"fileName": "string",



"id": "string",



"loadOrigins": [



"string"



],



"numberOfAffectedEntities": 1,



"shortName": "string"



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

Query a remediable entity.

Required filters:

* `securityProblemid`
* `remediationItemId`

#### Curl

```
curl -X 'GET' 'https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/7412525767433554374/remediationItems/PROCESS_GROUP-F32C09AEDCB7A450' \



-H 'accept: application/json; charset=utf-8' \



-H 'Authorization: Api-Token [your_token]'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/7412525767433554374/remediationItems/PROCESS_GROUP-F32C09AEDCB7A4
```

#### Response body

```
{



"id": "PROCESS_GROUP-F32C09AEDCB7A450",



"entityIds": [



"PROCESS_GROUP-F32C09AEDCB7A450"



],



"name": "app.js (frontend) unguard-frontend-*",



"firstAffectedTimestamp": 1725894871213,



"assessment": {



"exposure": "PUBLIC_NETWORK",



"dataAssets": "NOT_DETECTED",



"numberOfDataAssets": 0,



"vulnerableFunctionRestartRequired": false,



"vulnerableFunctionUsage": "NOT_AVAILABLE",



"vulnerableFunctionsInUse": [],



"vulnerableFunctionsNotInUse": [],



"vulnerableFunctionsNotAvailable": [],



"assessmentAccuracy": "FULL",



"assessmentAccuracyDetails": {



"reducedReasons": []



}



},



"vulnerabilityState": "VULNERABLE",



"muteState": {



"muted": false,



"user": "unknown",



"reason": "INITIAL_STATE"



},



"vulnerableComponents": [



{



"id": "SOFTWARE_COMPONENT-30CF12729DF87E61",



"displayName": "minimatch:3.0.4",



"shortName": "minimatch",



"numberOfAffectedEntities": 1,



"affectedEntities": [



"PROCESS_GROUP_INSTANCE-66B8C7F0FA77E541"



]



}



],



"remediationProgress": {



"affectedEntities": [



"PROCESS_GROUP_INSTANCE-66B8C7F0FA77E541"



],



"unaffectedEntities": []



}



}
```

## Related topics

* [Application Security](/docs/secure/application-security "Access the Dynatrace Application Security functionalities.")
* [Davis Security Advisor API](/docs/dynatrace-api/environment-api/application-security/davis-security-advice "View the Davis Security Advisor recommendations via Dynatrace API.")
* [Remediation tracking](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Track the remediation progress of vulnerabilities.")