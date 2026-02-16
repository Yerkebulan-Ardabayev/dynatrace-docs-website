# Dynatrace Documentation: dynatrace-api/environment-api

Generated: 2026-02-16

Files combined: 70

---


## Source: attacks.md


---
title: Attacks API
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/application-security/attacks
scraped: 2026-02-16T21:25:45.541425
---

# Attacks API

# Attacks API

* Reference
* Published Aug 30, 2023

[### List attacks](/docs/dynatrace-api/environment-api/application-security/attacks/get-attacks "View the list of attacks via Dynatrace API.")[### View attack details](/docs/dynatrace-api/environment-api/application-security/attacks/get-attack-details "View details of an attack via Dynatrace API.")

## Related topics

* [Application Security](/docs/secure/application-security "Access the Dynatrace Application Security functionalities.")
* [Davis Security Advisor API](/docs/dynatrace-api/environment-api/application-security/davis-security-advice "View the Davis Security Advisor recommendations via Dynatrace API.")
* [Threats & Exploits](/docs/secure/threats-and-exploits "Understand, triage, and investigate detection findings and alerts.")


---


## Source: get-remediation-item-details.md


---
title: Vulnerabilities API - GET remediation item details
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/application-security/vulnerabilities/get-remediation-item-details
scraped: 2026-02-16T21:30:05.164975
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


---


## Source: get-remediation-item-entities.md


---
title: Vulnerabilities API - GET remediation item entities
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/application-security/vulnerabilities/get-remediation-item-entities
scraped: 2026-02-16T21:31:56.790806
---

# Vulnerabilities API - GET remediation item entities

# Vulnerabilities API - GET remediation item entities

* Reference
* Updated on Sep 25, 2024

Lists the [remediation tracking](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Track the remediation progress of vulnerabilities.") processes of a third-party vulnerability.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/securityProblems/{id}/remediationItems/{remediationItemId}/remediationProgressEntities` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems/{remediationItemId}/remediationProgressEntities` |

## Authentication

To execute this request, you need an access token with `securityProblems.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the requested third-party security problem. | path | Required |
| remediationItemId | string | The ID of the remediation item. | path | Required |
| remediationProgressEntitySelector | string | Defines the scope of the query. Only remediation progress entities matching the specified criteria are included in the response.  You can add one or more of the following criteria. Values are *not* case-sensitive and the `EQUALS` operator is used unless otherwise specified.  * State: `state("value")`. Possible values the **state** field are `AFFECTED` and `UNAFFECTED`. If not set, all entities are returned. * Vulnerable function usage assessment: `assessment.vulnerableFunctionUsage("value")` Possible values are `IN_USE`, and `NOT_IN_USE`. * Vulnerable function restart required: `assessment.vulnerableFunctionRestartRequired("value")` Possible values are `TRUE` or `FALSE`. * Vulnerable function in use contains: `assessment.vulnerableFunctionInUseContains("value")`. Possible values are `class::function`, `class::` and `function`. The `CONTAINS` operator is used. Only vulnerable functions in use are considered. * Entity name contains: `entityNameContains("value-1")`. The `CONTAINS` operator is used.  To set several criteria, separate them with a comma (`,`). Only results matching **all** criteria are included in the response.  Specify the value of a criterion as a quoted string. The following special characters must be escaped with a tilde (`~`) inside quotes:  * Tilde `~` * Quote `"` | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [RemediationProgressEntityList](#openapi-definition-RemediationProgressEntityList) | Success. The response contains a list of remediation progress entities of a remediation item of a security problem. The number of entities returned is limited. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `RemediationProgressEntityList` object

A list of remediation progress entities.

| Element | Type | Description |
| --- | --- | --- |
| remediationProgressEntities | [RemediationProgressEntity[]](#openapi-definition-RemediationProgressEntity) | A list of remediation progress entities. |

#### The `RemediationProgressEntity` object

An affected or unaffected entity of a remediation for a security problem.

| Element | Type | Description |
| --- | --- | --- |
| assessment | [RemediationProgressEntityAssessment](#openapi-definition-RemediationProgressEntityAssessment) | Assessment of the remediation progress entity. |
| firstAffectedTimestamp | integer | The timestamp when the remediation progress entity has first been related to the vulnerability. |
| id | string | The ID of the remediation progress entity. |
| name | string | The name of the remediation progress entity. |
| state | string | The current state of the remediation progress entity. The element can hold these values * `AFFECTED` * `UNAFFECTED` |
| vulnerableComponents | [RemediationProgressVulnerableComponent[]](#openapi-definition-RemediationProgressVulnerableComponent) | A list of vulnerable components of the remediation item.  A vulnerable component is what causes the security problem. |

#### The `RemediationProgressEntityAssessment` object

Assessment of the remediation progress entity.

| Element | Type | Description |
| --- | --- | --- |
| vulnerableFunctionRestartRequired | boolean | Whether a restart is required for the latest vulnerable function data. |
| vulnerableFunctionUsage | string | The usage of vulnerable functions The element can hold these values * `IN_USE` * `NOT_AVAILABLE` * `NOT_IN_USE` |
| vulnerableFunctionsInUse | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | A list of vulnerable functions that are in use. |
| vulnerableFunctionsNotAvailable | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | A list of vulnerable functions that are not available. |
| vulnerableFunctionsNotInUse | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | A list of vulnerable functions that are not in use. |

#### The `VulnerableFunction` object

Defines an vulnerable function.

| Element | Type | Description |
| --- | --- | --- |
| className | string | The class name of the vulnerable function. |
| filePath | string | The file path of the vulnerable function. |
| functionName | string | The function name of the vulnerable function. |

#### The `RemediationProgressVulnerableComponent` object

A vulnerable component with details for a remediation progress entity (PGI).

| Element | Type | Description |
| --- | --- | --- |
| displayName | string | The display name of the vulnerable component. |
| fileName | string | The file name of the vulnerable component. |
| id | string | The Dynatrace entity ID of the vulnerable component. |
| loadOrigins | string[] | The load origins of the vulnerable components. |
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



"remediationProgressEntities": [



{



"assessment": {



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



"firstAffectedTimestamp": 1,



"id": "string",



"name": "string",



"state": "AFFECTED",



"vulnerableComponents": [



{



"displayName": "string",



"fileName": "string",



"id": "string",



"loadOrigins": [



"string"



],



"shortName": "string"



}



]



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

Examine the currently affected processes of a remediation item.

Required filter: `remediationProgressEntitySelector=state("AFFECTED")`.

#### Curl

```
curl -X 'GET' 'https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/7412525767433554374/remediationItems/PROCESS_GROUP-F32C09AEDCB7A450/remediationProgressEntities?remediationProgressEntitySelector=state%28%22AFFECTED%22%29' \



-H 'accept: application/json; charset=utf-8' \



-H 'Authorization: Api-Token [your_token]'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/7412525767433554374/remediationItems/PROCESS_GROUP-F32C09AEDCB7A450/remediationProgressEntities?remediationProgressEntitySelector=state%28%22AFFECTED%22%29
```

#### Response body

```
{



"remediationProgressEntities": [



{



"id": "PROCESS_GROUP_INSTANCE-66B8C7F0FA77E541",



"name": "app.js (frontend) unguard-frontend-* (unguard-frontend-696558fd77-cdkxp)",



"firstAffectedTimestamp": 1725894871213,



"state": "AFFECTED",



"vulnerableComponents": [



{



"id": "SOFTWARE_COMPONENT-30CF12729DF87E61",



"displayName": "minimatch:3.0.4",



"shortName": "minimatch"



}



],



"assessment": {



"vulnerableFunctionUsage": "NOT_AVAILABLE",



"vulnerableFunctionRestartRequired": false,



"vulnerableFunctionsInUse": [],



"vulnerableFunctionsNotInUse": [],



"vulnerableFunctionsNotAvailable": []



}



}



]



}
```

## Related topics

* [Application Security](/docs/secure/application-security "Access the Dynatrace Application Security functionalities.")
* [Davis Security Advisor API](/docs/dynatrace-api/environment-api/application-security/davis-security-advice "View the Davis Security Advisor recommendations via Dynatrace API.")
* [Remediation tracking](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Track the remediation progress of vulnerabilities.")


---


## Source: get-remediation-items.md


---
title: Vulnerabilities API - GET remediation items
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/application-security/vulnerabilities/get-remediation-items
scraped: 2026-02-15T21:26:58.258683
---

# Vulnerabilities API - GET remediation items

# Vulnerabilities API - GET remediation items

* Reference
* Updated on May 03, 2022

Lists the [remediation tracking](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Track the remediation progress of vulnerabilities.") process groups of a third-party vulnerability (or, in the case of Kubernetes vulnerabilities, the remediation tracking Kubernetes nodes).

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/securityProblems/{id}/remediationItems` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems` |

## Authentication

To execute this request, you need an access token with `securityProblems.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the requested third-party security problem. | path | Required |
| remediationItemSelector | string | Defines the scope of the query. Only remediable entities matching the specified criteria are included in the response.  You can add one or more of the following criteria. Values are *not* case-sensitive and the `EQUALS` operator is used unless otherwise specified.  * Vulnerability state: `vulnerabilityState("value")`. Possible values are `VULNERABLE`, and `RESOLVED`. If not set, all entities are returned. * Muted: `muted("value")`. Possible values are `TRUE` or `FALSE`. * Reachable data asset assessment: `assessment.dataAssets("value")` Possible values are `REACHABLE`, and `NOT_DETECTED`. * Network exposure assessment: `assessment.exposure("value")` Possible values are `PUBLIC_NETWORK`, and `NOT_DETECTED`. * Vulnerable function usage assessment: `assessment.vulnerableFunctionUsage("value")` Possible values are `IN_USE`, and `NOT_IN_USE`. * Vulnerable function restart required: `assessment.vulnerableFunctionRestartRequired("value")` Possible values are `TRUE` or `FALSE`. * Vulnerable function in use contains: `assessment.vulnerableFunctionInUseContains("value")`. Possible values are `class::function`, `class::` and `function`. The `CONTAINS` operator is used. Only vulnerable functions in use are considered. * Assessment accuracy: `assessment.accuracy("value")` Possible values are `FULL` and `REDUCED`. * Entity name contains: `entityNameContains("value-1")`. The `CONTAINS` operator is used. * Tracking link display name: `trackingLink.displayNameContains("value")`. The `CONTAINS` operator is used.  To set several criteria, separate them with a comma (`,`). Only results matching **all** criteria are included in the response.  Specify the value of a criterion as a quoted string. The following special characters must be escaped with a tilde (`~`) inside quotes:  * Tilde `~` * Quote `"` | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [RemediationItemList](#openapi-definition-RemediationItemList) | Success. The response contains the list of remediation items of a problem. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `RemediationItemList` object

A list of remediation items.

| Element | Type | Description |
| --- | --- | --- |
| remediationItems | [RemediationItem[]](#openapi-definition-RemediationItem) | A list of remediation items. |

#### The `RemediationItem` object

A possible remediation for a security problem.

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
| vulnerableComponents | [VulnerableComponent[]](#openapi-definition-VulnerableComponent) | A list of vulnerable components of the remediation item.  A vulnerable component is what causes the security problem. |

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

#### The `VulnerableComponent` object

Vulnerable component of a security problem.

| Element | Type | Description |
| --- | --- | --- |
| affectedEntities | string[] | A list of affected entities. |
| displayName | string | The display name of the vulnerable component. |
| fileName | string | The file name of the vulnerable component. |
| id | string | The Dynatrace entity ID of the vulnerable component. |
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



"remediationItems": [



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



"numberOfAffectedEntities": 1,



"shortName": "string"



}



]



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

List the remediation items of the `8788643471842202915` vulnerability. The response is truncated to two entries.

#### Curl

```
curl --request GET \



--url https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/8788643471842202915/remediationItems \



--header 'Authorization: Api-Token [your_token]'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/8788643471842202915/remediationItems
```

#### Response body

```
{



"remediationItems": [



{



"id": "PROCESS_GROUP-70DF2C1374244F5A",



"entityIds": [



"PROCESS_GROUP-70DF2C1374244F5A"



],



"name": "KpiTomcatBackEnd-CWS-1-IG-144-HG",



"firstAffectedTimestamp": 1633531037359,



"assessment": {



"exposure": "NOT_DETECTED",



"dataAssets": "REACHABLE"



},



"vulnerabilityState": "VULNERABLE",



"muteState": {



"muted": false,



"user": "unknown",



"reason": "INITIAL_STATE"



},



"vulnerableComponents": [



{



"id": "SOFTWARE_COMPONENT-2559CD116033C217",



"displayName": "io.software.component.1.1",



"fileName": "io.software.component.1.1.jar",



"numberOfAffectedEntities": 2,



"affectedEntities": [



"PROCESS_GROUP_INSTANCE-3684888745E180D5",



"PROCESS_GROUP_INSTANCE-8F100796B9296962"



]



},



{



"id": "SOFTWARE_COMPONENT-0A679AA673B2B525",



"displayName": "io.software.component.loader.2.0.Final",



"fileName": "io.software.component.loader.2.0.jar",



"numberOfAffectedEntities": 4,



"affectedEntities": [



"PROCESS_GROUP_INSTANCE-0D133F13A28B477A",



"PROCESS_GROUP_INSTANCE-258962DC804FEDBC",



"PROCESS_GROUP_INSTANCE-3684888745E180D5",



"PROCESS_GROUP_INSTANCE-B79C2594071FBF6C"



]



}



],



"remediationProgress": {



"affectedEntities": [



"PROCESS_GROUP_INSTANCE-0D133F13A28B477A",



"PROCESS_GROUP_INSTANCE-258962DC804FEDBC",



"PROCESS_GROUP_INSTANCE-3684888745E180D5",



"PROCESS_GROUP_INSTANCE-8F100796B9296962",



"PROCESS_GROUP_INSTANCE-B79C2594071FBF6C"



],



"unaffectedEntities": [



"PROCESS_GROUP_INSTANCE-63AD33941D667CAC",



"PROCESS_GROUP_INSTANCE-E20A5DDF167AF3B8",



"PROCESS_GROUP_INSTANCE-F1166B3AB1F4312D",



"PROCESS_GROUP_INSTANCE-F9D0250A7432521D",



"PROCESS_GROUP_INSTANCE-FF1B355E4E252FA1"



]



}



},



{



"id": "PROCESS_GROUP-18407614632D87A6",



"entityIds": [



"PROCESS_GROUP-18407614632D87A6"



],



"name": "KpiTomcatFrontEnd-CWS-1-IG-67-HG",



"firstAffectedTimestamp": 1633531037359,



"assessment": {



"exposure": "PUBLIC_NETWORK",



"dataAssets": "NOT_DETECTED"



},



"resolvedTimestamp": 1636096094323,



"vulnerabilityState": "RESOLVED",



"muteState": {



"muted": false,



"user": "unknown",



"reason": "INITIAL_STATE"



},



"vulnerableComponents": [



{



"id": "SOFTWARE_COMPONENT-2559CD116033C217",



"displayName": "io.software.component.1.1.Final",



"fileName": "io.software.component.1.1.jar",



"numberOfAffectedEntities": 1,



"affectedEntities": [



"PROCESS_GROUP_INSTANCE-41115D4B6F8BFEEC"



]



}



],



"remediationProgress": {



"affectedEntities": [



"PROCESS_GROUP_INSTANCE-41115D4B6F8BFEEC"



],



"unaffectedEntities": [



"PROCESS_GROUP_INSTANCE-0189CF4780B4B872",



"PROCESS_GROUP_INSTANCE-2D54D85C45C0BA57",



"PROCESS_GROUP_INSTANCE-3E6373ACEA9DE722",



"PROCESS_GROUP_INSTANCE-47BCF72F93FF9528",



"PROCESS_GROUP_INSTANCE-6B5EF5C1A5ED42D0",



"PROCESS_GROUP_INSTANCE-BA18DB16A7A28A04",



"PROCESS_GROUP_INSTANCE-BCAECCB29AB12462",



"PROCESS_GROUP_INSTANCE-DD3CD2024A06BB5B",



"PROCESS_GROUP_INSTANCE-DE5B280889AC6569"



]



}



}



]



}
```

#### Response code

200

## Related topics

* [Application Security](/docs/secure/application-security "Access the Dynatrace Application Security functionalities.")
* [Davis Security Advisor API](/docs/dynatrace-api/environment-api/application-security/davis-security-advice "View the Davis Security Advisor recommendations via Dynatrace API.")
* [Remediation tracking](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Track the remediation progress of vulnerabilities.")


---


## Source: get-vulnerability-events.md


---
title: Vulnerabilities API - GET vulnerability events
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/application-security/vulnerabilities/get-vulnerability-events
scraped: 2026-02-15T21:29:33.231361
---

# Vulnerabilities API - GET vulnerability events

# Vulnerabilities API - GET vulnerability events

* Reference
* Updated on Sep 25, 2024

Lists the events of a specific vulnerability.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/securityProblems/{id}/events` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/{id}/events` |

## Authentication

To execute this request, you need an access token with `securityProblems.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the requested security problem. | path | Required |
| from | string | The start of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the relative timeframe of thirty days is used (`now-30d`). | query | Optional |
| to | string | The end of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the current timestamp is used. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SecurityProblemEventsList](#openapi-definition-SecurityProblemEventsList) | Success. The response contains the list of security problem events. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `SecurityProblemEventsList` object

A list of events for a security problem.

| Element | Type | Description |
| --- | --- | --- |
| events | [SecurityProblemEvent[]](#openapi-definition-SecurityProblemEvent) | A list of events for a security problem. |
| nextPageKey | string | The cursor for the next page of results. Has the value of `null` on the last page.  Use it in the **nextPageKey** query parameter to obtain subsequent pages of the result. |
| pageSize | integer | The number of entries per page. |
| totalCount | integer | The total number of entries in the result. |

#### The `SecurityProblemEvent` object

The event of a security problem.

| Element | Type | Description |
| --- | --- | --- |
| muteState | [MuteState](#openapi-definition-MuteState) | Metadata of the muted state of a security problem in relation to an event. |
| reason | string | The reason of the event creation. The element can hold these values * `ASSESSMENT_CHANGED` * `SECURITY_PROBLEM_CREATED` * `SECURITY_PROBLEM_MUTED` * `SECURITY_PROBLEM_REOPENED` * `SECURITY_PROBLEM_RESOLVED` * `SECURITY_PROBLEM_UNMUTED` * `VULNERABILITY_DEPRECATED` * `VULNERABILITY_ID_CHANGED` |
| riskAssessmentSnapshot | [RiskAssessmentSnapshot](#openapi-definition-RiskAssessmentSnapshot) | A snapshot of the risk assessment of a security problem. |
| timestamp | integer | The timestamp when the event occurred. |

#### The `MuteState` object

Metadata of the muted state of a security problem in relation to an event.

| Element | Type | Description |
| --- | --- | --- |
| comment | string | A user's comment. |
| reason | string | The reason for the mute state change. The element can hold these values * `AFFECTED` * `CONFIGURATION_NOT_AFFECTED` * `FALSE_POSITIVE` * `IGNORE` * `INITIAL_STATE` * `OTHER` * `VULNERABLE_CODE_NOT_IN_USE` |
| user | string | The user who has muted or unmuted the problem. |

#### The `RiskAssessmentSnapshot` object

A snapshot of the risk assessment of a security problem.

| Element | Type | Description |
| --- | --- | --- |
| baseRiskScore | number | The risk score (1-10) from the CVSS score. |
| changes | [RiskAssessmentChanges](#openapi-definition-RiskAssessmentChanges) | All changes of the risk assessment. |
| exposure | string | The level of exposure of affected entities. The element can hold these values * `NOT_AVAILABLE` * `NOT_DETECTED` * `PUBLIC_NETWORK` |
| numberOfAffectedEntities | integer | The number of currently affected entities. |
| numberOfAffectedNodes | integer | The number of currently affected nodes. |
| numberOfAffectedProcessGroups | integer | The number of currently affected process groups. |
| numberOfReachableDataAssets | integer | The number of data assets that are currently reachable by affected entities. |
| numberOfRelatedAttacks | integer | The number of related attacks. |
| publicExploit | string | The availability status of public exploits. The element can hold these values * `AVAILABLE` * `NOT_AVAILABLE` |
| riskLevel | string | The Davis risk level.  It is calculated by Dynatrace on the basis of CVSS score. The element can hold these values * `CRITICAL` * `HIGH` * `LOW` * `MEDIUM` * `NONE` |
| riskScore | number | The Davis risk score (1-10).  It is calculated by Dynatrace on the basis of CVSS score. |
| vulnerableFunctionUsage | string | The state of vulnerable code execution. The element can hold these values * `IN_USE` * `NOT_AVAILABLE` * `NOT_IN_USE` |

#### The `RiskAssessmentChanges` object

All changes of the risk assessment.

| Element | Type | Description |
| --- | --- | --- |
| deltaBaseRiskScore | number | The delta of the risk score. |
| deltaNumberOfAffectedNodes | integer | The delta of the number of currently affected nodes. |
| deltaNumberOfAffectedProcessGroups | integer | The delta of the number of currently affected process groups. |
| deltaNumberOfReachableDataAssets | integer | The delta of the number of data assets that are currently reachable by affected entities. |
| deltaNumberOfRelatedAttacks | integer | The delta of the number of related attacks. |
| deltaRiskScore | number | The delta of the Davis risk score. |
| previousExposure | string | The previous level of exposure of affected entities. The element can hold these values * `NOT_AVAILABLE` * `NOT_DETECTED` * `PUBLIC_NETWORK` |
| previousPublicExploit | string | The previous availability status of public exploits. The element can hold these values * `AVAILABLE` * `NOT_AVAILABLE` |
| previousVulnerableFunctionUsage | string | The previous state of vulnerable code execution. The element can hold these values * `IN_USE` * `NOT_AVAILABLE` * `NOT_IN_USE` |

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



"events": [



{



"muteState": {



"comment": "string",



"reason": "AFFECTED",



"user": "string"



},



"reason": "ASSESSMENT_CHANGED",



"riskAssessmentSnapshot": {



"baseRiskScore": 1,



"changes": {



"deltaBaseRiskScore": 1,



"deltaNumberOfAffectedNodes": 1,



"deltaNumberOfAffectedProcessGroups": 1,



"deltaNumberOfReachableDataAssets": 1,



"deltaNumberOfRelatedAttacks": 1,



"deltaRiskScore": 1,



"previousExposure": "NOT_AVAILABLE",



"previousPublicExploit": "AVAILABLE",



"previousVulnerableFunctionUsage": "IN_USE"



},



"exposure": "NOT_AVAILABLE",



"numberOfAffectedEntities": 1,



"numberOfAffectedNodes": 1,



"numberOfAffectedProcessGroups": 1,



"numberOfReachableDataAssets": 1,



"numberOfRelatedAttacks": 1,



"publicExploit": "AVAILABLE",



"riskLevel": "CRITICAL",



"riskScore": 1,



"vulnerableFunctionUsage": "IN_USE"



},



"timestamp": 1



}



],



"nextPageKey": "AQAAABQBAAAABQ==",



"pageSize": 1,



"totalCount": 1



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

Query global vulnerability events.

Required filter: `securityProblemId`.

#### Curl

```
curl -X 'GET' 'https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/7412525767433554374/events' \



-H 'accept: application/json; charset=utf-8' \



-H 'Authorization: Api-Token [your_token]'
```

#### Request URL

```
https://mySampleEnv.live.dynatracelabs.com/api/v2/securityProblems/7412525767433554374/events
```

#### Response body

```
{



"events": [



{



"timestamp": 1726497793191,



"reason": "SECURITY_PROBLEM_REOPENED",



"riskAssessmentSnapshot": {



"baseRiskScore": 5.3,



"exposure": "PUBLIC_NETWORK",



"numberOfAffectedEntities": 2,



"numberOfAffectedNodes": 0,



"numberOfAffectedProcessGroups": 2,



"numberOfReachableDataAssets": 1,



"numberOfRelatedAttacks": 0,



"publicExploit": "NOT_AVAILABLE",



"riskLevel": "MEDIUM",



"riskScore": 5.3,



"vulnerableFunctionUsage": "NOT_AVAILABLE"



}



},



{



"timestamp": 1726496886335,



"reason": "SECURITY_PROBLEM_RESOLVED",



"riskAssessmentSnapshot": {



"baseRiskScore": 5.3,



"exposure": "NOT_DETECTED",



"numberOfAffectedEntities": 0,



"numberOfAffectedNodes": 0,



"numberOfAffectedProcessGroups": 0,



"numberOfReachableDataAssets": 0,



"numberOfRelatedAttacks": 0,



"publicExploit": "NOT_AVAILABLE",



"riskLevel": "MEDIUM",



"riskScore": 5.3,



"vulnerableFunctionUsage": "NOT_AVAILABLE"



}



},



{



"timestamp": 1726495992217,



"reason": "SECURITY_PROBLEM_REOPENED",



"riskAssessmentSnapshot": {



"baseRiskScore": 5.3,



"exposure": "PUBLIC_NETWORK",



"numberOfAffectedEntities": 2,



"numberOfAffectedNodes": 0,



"numberOfAffectedProcessGroups": 2,



"numberOfReachableDataAssets": 1,



"numberOfRelatedAttacks": 0,



"publicExploit": "NOT_AVAILABLE",



"riskLevel": "MEDIUM",



"riskScore": 5.3,



"vulnerableFunctionUsage": "NOT_AVAILABLE"



}



},



{



"timestamp": 1726495086473,



"reason": "SECURITY_PROBLEM_RESOLVED",



"riskAssessmentSnapshot": {



"baseRiskScore": 5.3,



"exposure": "NOT_DETECTED",



"numberOfAffectedEntities": 0,



"numberOfAffectedNodes": 0,



"numberOfAffectedProcessGroups": 0,



"numberOfReachableDataAssets": 0,



"numberOfRelatedAttacks": 0,



"publicExploit": "NOT_AVAILABLE",



"riskLevel": "MEDIUM",



"riskScore": 5.3,



"vulnerableFunctionUsage": "NOT_AVAILABLE"



}



},



{



"timestamp": 1726121661376,



"reason": "ASSESSMENT_CHANGED",



"riskAssessmentSnapshot": {



"baseRiskScore": 5.3,



"changes": {



"deltaRiskScore": 1,



"previousExposure": "NOT_DETECTED"



},



"exposure": "PUBLIC_NETWORK",



"numberOfAffectedEntities": 2,



"numberOfAffectedNodes": 0,



"numberOfAffectedProcessGroups": 2,



"numberOfReachableDataAssets": 1,



"numberOfRelatedAttacks": 0,



"publicExploit": "NOT_AVAILABLE",



"riskLevel": "MEDIUM",



"riskScore": 5.3,



"vulnerableFunctionUsage": "NOT_AVAILABLE"



}



},



{



"timestamp": 1725894871382,



"reason": "ASSESSMENT_CHANGED",



"riskAssessmentSnapshot": {



"baseRiskScore": 5.3,



"changes": {



"deltaNumberOfAffectedProcessGroups": 1



},



"exposure": "NOT_DETECTED",



"numberOfAffectedEntities": 2,



"numberOfAffectedNodes": 0,



"numberOfAffectedProcessGroups": 2,



"numberOfReachableDataAssets": 1,



"numberOfRelatedAttacks": 0,



"publicExploit": "NOT_AVAILABLE",



"riskLevel": "MEDIUM",



"riskScore": 4.3,



"vulnerableFunctionUsage": "NOT_AVAILABLE"



}



}



],



"pageSize": 1,



"totalCount": 6



}
```

## Related topics

* [Application Security](/docs/secure/application-security "Access the Dynatrace Application Security functionalities.")
* [Davis Security Advisor API](/docs/dynatrace-api/environment-api/application-security/davis-security-advice "View the Davis Security Advisor recommendations via Dynatrace API.")


---


## Source: get-vulnerable-functions.md


---
title: Vulnerabilities API - GET vulnerable functions
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/application-security/vulnerabilities/get-vulnerable-functions
scraped: 2026-02-16T09:27:44.664793
---

# Vulnerabilities API - GET vulnerable functions

# Vulnerabilities API - GET vulnerable functions

* Reference
* Updated on Sep 25, 2024

Lists the vulnerable functions and their usage.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/securityProblems/{id}/vulnerableFunctions` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/{id}/vulnerableFunctions` |

## Authentication

To execute this request, you need an access token with `securityProblems.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the requested third-party security problem. | path | Required |
| vulnerableFunctionsSelector | string | Defines the scope of the query. Only vulnerable functions matching the specified criteria are included in the response.  You can add the following criteria. Values are *not* case sensitive and the `EQUALS` operator is used unless otherwise specified.  * Management zone ID: `managementZoneIds("mzId-1", "mzId-2")`. * Management zone name: `managementZones("name-1", "name-2")`. Values are case sensitive. * Process group ID: `processGroupIds("pgId-1", "pgId-2")`. Specify Dynatrace entity IDs here. * Process group name: `processGroupNames("name-1", "name-2")`. Values are case sensitive. * Process group name contains: `processGroupNameContains("name-1")`. The `CONTAINS` operator is used.  Specify the value of a criterion as a quoted string. The following special characters must be escaped with a tilde (`~`) inside quotes:  * Tilde `~` * Quote `"` | query | Optional |
| groupBy | string | Defines additional grouping types in which vulnerable functions should be displayed.  You can add one of the following grouping types.  * Process group: `PROCESS_GROUP` | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [VulnerableFunctionsContainer](#openapi-definition-VulnerableFunctionsContainer) | Success. The response contains the list of vulnerable functions. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `VulnerableFunctionsContainer` object

A list of vulnerable functions, their security problem wide usages and their usages per process group.
Optional: A list of vulnerable function usages per process group for a security problem.

| Element | Type | Description |
| --- | --- | --- |
| vulnerableFunctions | [VulnerableFunctionProcessGroups[]](#openapi-definition-VulnerableFunctionProcessGroups) | A list of vulnerable functions, their security problem wide usages and their usages per process group. |
| vulnerableFunctionsByProcessGroup | [ProcessGroupVulnerableFunctions[]](#openapi-definition-ProcessGroupVulnerableFunctions) | A list of vulnerable function usages per process group for a security problem. The result is sorted based on the following criteria:  * the number of vulnerable functions in use (descending). * the number of vulnerable functions not in use (descending). * the number of vulnerable functions not available (descending). * the process group identifier (ascending) |

#### The `VulnerableFunctionProcessGroups` object

A vulnerable function including its usage by specific process groups in context of the security problem.

| Element | Type | Description |
| --- | --- | --- |
| function | [VulnerableFunction](#openapi-definition-VulnerableFunction) | Defines an vulnerable function. |
| processGroupsInUse | string[] | The process group identifiers, where this vulnerable function is in use. |
| processGroupsNotAvailable | string[] | The process group identifiers, where information about the usage of this function not available. |
| processGroupsNotInUse | string[] | The process group identifiers, where this vulnerable function is not in use. |
| usage | string | The vulnerable function usage based on the given process groups:  * IN\_USE if at least one process group calls this vulnerable function. * NOT\_IN\_USE if all process groups do not call this vulnerable function. * NOT\_AVAILABLE if vulnerable function usage could not be calculated for at least one process group and no process group calls this vulnerable function. The element can hold these values * `IN_USE` * `NOT_AVAILABLE` * `NOT_IN_USE` |

#### The `VulnerableFunction` object

Defines an vulnerable function.

| Element | Type | Description |
| --- | --- | --- |
| className | string | The class name of the vulnerable function. |
| filePath | string | The file path of the vulnerable function. |
| functionName | string | The function name of the vulnerable function. |

#### The `ProcessGroupVulnerableFunctions` object

The vulnerable functions of a process group including their usage.

| Element | Type | Description |
| --- | --- | --- |
| functionsInUse | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | A list of vulnerable functions in use. |
| functionsNotAvailable | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | A list of vulnerable functions with unknown state. |
| functionsNotInUse | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | A list of vulnerable functions not in use. |
| processGroup | string | The process group identifier. |

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



"vulnerableFunctions": [



{



"function": {



"className": "string",



"filePath": "string",



"functionName": "string"



},



"processGroupsInUse": [



"string"



],



"processGroupsNotAvailable": [



"string"



],



"processGroupsNotInUse": [



"string"



],



"usage": "IN_USE"



}



],



"vulnerableFunctionsByProcessGroup": [



{



"functionsInUse": [



{}



],



"functionsNotAvailable": [



{}



],



"functionsNotInUse": [



{}



],



"processGroup": "string"



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

Given a vulnerability with ID `2919200225913269102` that has vulnerable functions in use, query both views on the vulnerable functions (vulnerable function to `PROCESS_GROUP` and `PROCESS_GROUP` to vulnerable function).

Required filter: `groupBy=PROCESS_GROUP`.

#### Curl

```
curl -X 'GET' 'https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/vulnerableFunctions?groupBy=PROCESS_GROUP' \



-H 'accept: application/json; charset=utf-8' \



-H 'Authorization: Api-Token [your_token]'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/vulnerableFunctions?groupBy=PROCESS_GROUP
```

#### Response body

```
{



"vulnerableFunctions": [



{



"function": {



"className": "org.apache.coyote.http11.Http11InputBuffer",



"filePath": null,



"functionName": "parseHeader"



},



"usage": "IN_USE",



"processGroupsInUse": [



"PROCESS_GROUP-285FF9C91448BC8B"



],



"processGroupsNotInUse": [],



"processGroupsNotAvailable": []



}



],



"vulnerableFunctionsByProcessGroup": [



{



"processGroup": "PROCESS_GROUP-285FF9C91448BC8B",



"functionsInUse": [



{



"className": "org.apache.coyote.http11.Http11InputBuffer",



"filePath": null,



"functionName": "parseHeader"



}



],



"functionsNotInUse": [],



"functionsNotAvailable": []



}



]



}
```

## Related topics

* [Application Security](/docs/secure/application-security "Access the Dynatrace Application Security functionalities.")
* [Davis Security Advisor API](/docs/dynatrace-api/environment-api/application-security/davis-security-advice "View the Davis Security Advisor recommendations via Dynatrace API.")


---


## Source: post-mute-vulnerabilities.md


---
title: Vulnerabilities API - POST mute vulnerabilities
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/application-security/vulnerabilities/post-mute-vulnerabilities
scraped: 2026-02-16T21:24:57.428230
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


---


## Source: post-problems-unmute.md


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


---


## Source: post-remediation-item-tracking-link.md


---
title: Vulnerabilities API - POST remediation item tracking links
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/application-security/vulnerabilities/post-remediation-item-tracking-link
scraped: 2026-02-16T09:36:37.678022
---

# Vulnerabilities API - POST remediation item tracking links

# Vulnerabilities API - POST remediation item tracking links

* Reference
* Updated on Sep 25, 2024

Adds, edits, or deletes the tracking links of [remediation tracking](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Track the remediation progress of vulnerabilities.") process groups of a third-party vulnerability (or, in the case of Kubernetes vulnerabilities, of remediation tracking Kubernetes nodes).

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/securityProblems/{id}/remediationItems/trackingLinks` |
| POST | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems/trackingLinks` |

## Authentication

To execute this request, you need an access token with `securityProblems.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the requested third-party security problem. | path | Required |
| body | [RemediationItemsBulkUpdateDeleteDto](#openapi-definition-RemediationItemsBulkUpdateDeleteDto) | Contains the external tracking link associations to be set or deleted on the remediation items of the security problem.  * Links to be set should be submitted in the `updates` object. * Links to be deleted should be submitted in the `deletes` array.  The request must contain at least one entry to set or delete to be valid.  Conflicting changes for the same remediation item (ID appears both in the `deletes` and `updates` field) cannot be submitted.  Note that all tracking link updates for the security problem should be submitted in one request. | body | Optional |

### Request body objects

#### The `RemediationItemsBulkUpdateDeleteDto` object

Contains the external tracking link associations to be applied to the remediation items of the security problem.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| deletes | string[] | Tracking links to remove from the security problem.  List of remediation item IDs of the security problem for which to remove the tracking links. | Optional |
| updates | object | Tracking links to set for the security problem.  Map of remediation item ID to tracking link objects.  Keys must be valid remediation item IDs of the security problem, the associated value must contain the link to set for the item. | Optional |

#### The `TrackingLinkUpdate` object

External tracking link URL association to be set for the remediable entity of the security problem.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| displayName | string | The desired tracking link display name (title) set for the remediation item, e.g. 'ISSUE-123'. | Required |
| url | string | The desired tracking link url set for the remediation item, e.g. https://example.com/ISSUE-123  Note that only valid URLs with 'http' or 'https' protocols are supported. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"deletes": [



"string"



],



"updates": {}



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The requested tracking links have been updated. |
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

## Examples

### Set tracking links

Setup: There's an automation in place that creates a ticket for each remediable entity automatically.

Goal: Make the endpoint link the ticket with the remediation item. The following tracking links will be set:

* `https://example.com/TICKET-46C0E12D9B0EF2D9` for `"PROCESS_GROUP-46C0E12D9B0EF2D9"`
* `https://example.com/TICKET-549E6AD75BD598EC` for `"PROCESS_GROUP-549E6AD75BD598EC"`

#### Curl

```
curl -X 'POST' 'https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/remediationItems/trackingLinks' \



-H 'accept: */*' \



-H 'Authorization: Api-Token [your_token]' \



-H 'Content-Type: application/json; charset=utf-8' \



-d '{



"updates": {



"PROCESS_GROUP-46C0E12D9B0EF2D9": {



"displayName": "TICKET-46C0E12D9B0EF2D9",



"url": "https://example.com/TICKET-46C0E12D9B0EF2D9"



},



"PROCESS_GROUP-549E6AD75BD598EC": {



"displayName": "TICKET-549E6AD75BD598EC",



"url": "https://example.com/TICKET-549E6AD75BD598EC"



}



}



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/remediationItems/trackingLinks
```

#### Request body

```
{



"updates": {



"PROCESS_GROUP-46C0E12D9B0EF2D9": {



"displayName": "TICKET-46C0E12D9B0EF2D9",



"url": "https://example.com/TICKET-46C0E12D9B0EF2D9"



},



"PROCESS_GROUP-549E6AD75BD598EC": {



"displayName": "TICKET-549E6AD75BD598EC",



"url": "https://example.com/TICKET-549E6AD75BD598EC"



}



}



}
```

#### Response code

200

### Delete tracking links

Remove tracking links from `"PROCESS_GROUP-46C0E12D9B0EF2D9"` and `"PROCESS_GROUP-549E6AD75BD598EC"`.

#### Curl

```
curl -X 'POST' 'https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/remediationItems/trackingLinks' \



-H 'accept: */*' \



-H 'Authorization: Api-Token [your_token]' \



-H 'Content-Type: application/json; charset=utf-8' \



-d '{



"deletes": ["PROCESS_GROUP-46C0E12D9B0EF2D9", "PROCESS_GROUP-549E6AD75BD598EC"]



}



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/remediationItems/trackingLinks
```

#### Request body

```
{



"deletes": ["PROCESS_GROUP-46C0E12D9B0EF2D9", "PROCESS_GROUP-549E6AD75BD598EC"]



}
```

#### Response code

200

## Related topics

* [Application Security](/docs/secure/application-security "Access the Dynatrace Application Security functionalities.")
* [Remediation tracking](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Track the remediation progress of vulnerabilities.")


---


## Source: post-remediation-items-mute.md


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


---


## Source: post-remediation-items-unmute.md


---
title: Vulnerabilities API - POST unmute remediation items
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/application-security/vulnerabilities/post-remediation-items-unmute
scraped: 2026-02-16T21:26:09.638354
---

# Vulnerabilities API - POST unmute remediation items

# Vulnerabilities API - POST unmute remediation items

* Reference
* Updated on Sep 25, 2024

Unmutes multiple [remediation tracking](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Track the remediation progress of vulnerabilities.") process groups or, in the case of Kubernetes vulnerabilities, multiple remediation tracking Kubernetes nodes.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/securityProblems/{id}/remediationItems/unmute` |
| POST | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems/unmute` |

## Authentication

To execute this request, you need an access token with `securityProblems.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the requested third-party security problem. | path | Required |
| body | [RemediationItemsBulkUnmute](#openapi-definition-RemediationItemsBulkUnmute) | The JSON body of the request. Contains the un-muting information. | body | Optional |

### Request body objects

#### The `RemediationItemsBulkUnmute` object

Information on un-muting several remediation items.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| comment | string | A comment about the un-muting reason. | Optional |
| reason | string | The reason for un-muting the remediation items. The element can hold these values * `AFFECTED` | Required |
| remediationItemIds | string[] | The ids of the remediation items to be un-muted. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"comment": "string",



"reason": "AFFECTED",



"remediationItemIds": [



"string"



]



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [RemediationItemsBulkUnmuteResponse](#openapi-definition-RemediationItemsBulkUnmuteResponse) | Success. The remediation item(s) have been un-muted. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `RemediationItemsBulkUnmuteResponse` object

Response of un-muting several remediation items.

| Element | Type | Description |
| --- | --- | --- |
| summary | [RemediationItemMutingSummary[]](#openapi-definition-RemediationItemMutingSummary) | The summary of which remediation items were un-muted and which already were un-muted previously. |

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

Unmute two entities, `PROCESS_GROUP-46C0E12D9B0EF2D9` and `PROCESS_GROUP-549E6AD75BD598EC`.

#### Curl

```
curl -X 'POST' 'https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/remediationItems/unmute' \



-H 'accept: application/json; charset=utf-8' \



-H 'Authorization: Api-Token [your_token]' \



-H 'Content-Type: application/json; charset=utf-8' \



-d '{



"comment": "Example unmute multiple",



"reason": "AFFECTED",



"remediationItemIds": ["PROCESS_GROUP-46C0E12D9B0EF2D9", "PROCESS_GROUP-549E6AD75BD598EC"]



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/remediationItems/unmute
```

#### Request body

```
{



"comment": "Example unmute multiple",



"reason": "AFFECTED",



"remediationItemIds": ["PROCESS_GROUP-46C0E12D9B0EF2D9", "PROCESS_GROUP-549E6AD75BD598EC"]



}
```

#### Response body

```
{



"summary": [



{



"remediationItemId": "PROCESS_GROUP-46C0E12D9B0EF2D9",



"muteStateChangeTriggered": true



},



{



"remediationItemId": "PROCESS_GROUP-549E6AD75BD598EC",



"muteStateChangeTriggered": true



}



]



}
```

## Related topics

* [Application Security](/docs/secure/application-security "Access the Dynatrace Application Security functionalities.")
* [Davis Security Advisor API](/docs/dynatrace-api/environment-api/application-security/davis-security-advice "View the Davis Security Advisor recommendations via Dynatrace API.")
* [Remediation tracking](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Track the remediation progress of vulnerabilities.")


---


## Source: put-remediation-items.md


---
title: Vulnerabilities API - PUT mute or unmute a remediation item
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/application-security/vulnerabilities/put-remediation-items
scraped: 2026-02-16T21:31:00.874783
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


---


## Source: credential-vault.md


---
title: Credential vault API
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/credential-vault
scraped: 2026-02-16T21:28:14.112192
---

# Credential vault API

# Credential vault API

* Reference
* Published Oct 14, 2019

The **Credential vault API** empowers you to manage credentials for synthetic [browser](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Learn about configuring browser monitors and clickpaths.") and [HTTP](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Learn about configuring HTTP monitors.") monitors.

[### List all credentials

Get an overview of all credentials configured in your Dynatrace environment.](/docs/dynatrace-api/environment-api/credential-vault/get-all "Fetch the list of stored credentials via the Dynatrace API.")[### View credentials metadata

Get credentials parameters by configuration ID.](/docs/dynatrace-api/environment-api/credential-vault/get-credentials "View a stored credentials configuration via the Dynatrace API.")

[### Create credentials

Create a new credentials configuration with the exact parameters you need.](/docs/dynatrace-api/environment-api/credential-vault/post-credentials "Create a credentials configuration via Dynatrace API.")[### Edit credentials

Update the existing configuration of credentials.](/docs/dynatrace-api/environment-api/credential-vault/put-credentials "Update a stored credentials configuration via the Dynatrace API.")[### Delete credentials

Delete the configuration of credentials you no longer need.](/docs/dynatrace-api/environment-api/credential-vault/del-credentials "Delete a stored credentials configuration via the Dynatrace API.")

## Related topics

* [Configure browser monitors](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Learn about configuring browser monitors and clickpaths.")
* [Configure HTTP monitors](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Learn about configuring HTTP monitors.")


---


## Source: get-latest-image.md


---
title: Deployment API - GET the latest available ActiveGate image version
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/deployment/activegate/get-latest-image
scraped: 2026-02-16T09:29:19.743752
---

# Deployment API - GET the latest available ActiveGate image version

# Deployment API - GET the latest available ActiveGate image version

* Reference
* Published Nov 22, 2023

Get the latest available ActiveGate image version.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/deployment/image/gateway/latest` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/deployment/image/gateway/latest` |

## Authentication

To execute this request, you need an access token with `InstallerDownload` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ImageDto](#openapi-definition-ImageDto) | Success |
| **404** | - | No ActiveGate image found |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ImageDto` object

| Element | Type | Description |
| --- | --- | --- |
| source | string | Image location |
| tag | string | Image tag |

### Response body JSON models

```
{



"source": "string",



"tag": "string"



}
```


---


## Source: get-arns-for-lambda-layers.md


---
title: Deployment API - View ARNs for AWS Lambda layers
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/deployment/oneagent/get-arns-for-lambda-layers
scraped: 2026-02-16T09:34:06.327232
---

# Deployment API - View ARNs for AWS Lambda layers

# Deployment API - View ARNs for AWS Lambda layers

* Reference
* Published Jul 29, 2022

This API is intended for use with the latest AWS Lambda implementation. For details, see [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

Get the Amazon Resource Names (ARNs) of the latest version of OneAgent for AWS Lambda layers for supported AWS Lambda runtimes.

Note that passing architecture, technology type, or region as a parameter returns only the relevant layers.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/deployment/lambda/layer` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/deployment/lambda/layer` |

## Authentication

To execute this request, you need an access token with `InstallerDownload` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| arch | string | The architecture of your OS:  * If omitted, shows available layers for all architectures. * `x86`: x86 architecture. * `arm`: ARM architecture. The element can hold these values * `x86` * `arm` | query | Optional |
| techtype | string | Technology type of the lambda runtime. The element can hold these values * `java` * `nodejs` * `python` | query | Optional |
| withCollector | string | Specify if you want the log collector contained or log collector only. ONLY cannot be combined with techtype The element can hold these values * `included` * `excluded` * `only` | query | Optional |
| region | string | The region of the layer. It must match the region of the AWS Lambda function | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [LatestLambdaLayersMetainfo](#openapi-definition-LatestLambdaLayersMetainfo) | Success. The payload contains the ARNs of the latest available layers. |
| **404** | - | Not found. See the response body for details. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `LatestLambdaLayersMetainfo` object

Latest information about available AWS lambda layers

| Element | Type | Description |
| --- | --- | --- |
| arns | [LambdaDto[]](#openapi-definition-LambdaDto) | - |

#### The `LambdaDto` object

| Element | Type | Description |
| --- | --- | --- |
| arch | string | - |
| arn | string | - |
| region | string | - |
| techType | string | - |
| withCollector | string | - |

### Response body JSON models

```
{



"arns": [



{



"arch": "string",



"arn": "string",



"region": "string",



"techType": "string",



"withCollector": "string"



}



]



}
```


---


## Source: get-latest-version-lambda-classic.md


---
title: Deployment API - View the latest OneAgent version for AWS Lambda Classic
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/deployment/oneagent/get-latest-version-lambda-classic
scraped: 2026-02-16T09:38:05.836620
---

# Deployment API - View the latest OneAgent version for AWS Lambda Classic

# Deployment API - View the latest OneAgent version for AWS Lambda Classic

* Reference
* Updated on Aug 20, 2025

This API is intended for use with the AWS Lambda Classic implementation. For details, see [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

Get the latest version names of OneAgent code modules for the Java, Node.js, and Python AWS Lambda runtimes, also including names for layers that are combined with the log collector, as well as for the standalone log collector layer.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/deployment/lambda/agent/latest` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/deployment/lambda/agent/latest` |

## Authentication

To execute this request, you need an access token with `InstallerDownload` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [LatestLambdaLayerNames](#openapi-definition-LatestLambdaLayerNames) | Success. The payload contains the available versions. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `LatestLambdaLayerNames` object

Latest OneAgent lambda version names available

| Element | Type | Description |
| --- | --- | --- |
| collector | string | - |
| java | string | - |
| java\_with\_collector | string | - |
| nodejs | string | - |
| nodejs\_with\_collector | string | - |
| python | string | - |
| python\_with\_collector | string | - |

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



"collector": "string",



"java": "string",



"java_with_collector": "string",



"nodejs": "string",



"nodejs_with_collector": "string",



"python": "string",



"python_with_collector": "string"



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


---


## Source: get-processmodule-config.md


---
title: Deployment API - View process module configuration for OneAgent
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/deployment/oneagent/get-processmodule-config
scraped: 2026-02-15T21:29:09.747925
---

# Deployment API - View process module configuration for OneAgent

# Deployment API - View process module configuration for OneAgent

* Reference
* Published Mar 25, 2022

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/deployment/installer/agent/processmoduleconfig` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/deployment/installer/agent/processmoduleconfig` |

## Authentication

To execute this request, you need an access token with `InstallerDownload` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| revision | integer | The previously received revision to compare against. | query | Optional |
| sections | string | A list of comma-separated section identifiers to retrieve values for. Supported sections are 'general' and 'agentType'. Defaults to 'general'. | query | Optional |
| hostgroup | string | The name of the host group the process is part of. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [AgentProcessModuleConfigResponse](#openapi-definition-AgentProcessModuleConfigResponse) | Success |
| **304** | - | Not modified. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `AgentProcessModuleConfigResponse` object

The response to a process module config request.

| Element | Type | Description |
| --- | --- | --- |
| properties | [SectionProperty[]](#openapi-definition-SectionProperty) | The properties and their sections in this response. |
| revision | integer | The new revision associated with the config. |

#### The `SectionProperty` object

A single agent property with it's associated section.

| Element | Type | Description |
| --- | --- | --- |
| key | string | The property key. |
| section | string | The section this property belongs to. |
| value | string | The property value. |

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



"properties": [



{



"key": "dockerInjection",



"section": "general",



"value": "on"



}



],



"revision": 64459404400310540



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


---


## Source: entity-selector.md


---
title: Environment API v2 - Entity selector
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/entity-v2/entity-selector
scraped: 2026-02-15T21:26:28.445104
---

# Environment API v2 - Entity selector

# Environment API v2 - Entity selector

* Reference
* Published Nov 20, 2020

The entity selector is a powerful instrument for specifying which entities you want to include to the scope of your Environment v2 API calls. It is used in several APIs, so you only have to learn the syntax once and then reuse it for multiple use cases.

You must specify one of following criteria:

* [Entity type](#type)
* [Entity ID](#id)

Additionally you can provide the following criteria in any combination:

* [Entity name](#name)
* [Entity attribute](#attribute)
* [Tag](#tag)
* [Management zone ID](#mzid)
* [Management zone name](#mzname)
* [Health state](#health)

If you provide several criteria, only results matching **all** criteria are included in the response.

* For example: `type(HOST),entityName.equals(Server)`

If the text input in the criteria contains certain symbols, such as parentheses or a comma, the text must be enclosed in quotation marks.

* For example: `type(HOST),entityName.equals("Server(prod),1")`

## Limitations

The total length of the **entitySelector** string is limited to 2,000 characters.

You can select only one type of entity per query.

## Entity type

The type of the entity you want to query.

You can fetch the list of available entity types with the [GET all entity types](/docs/dynatrace-api/environment-api/entity-v2/get-all-entity-types "View all types of monitored entities in your environment via Dynatrace API.") call.

|  |  |
| --- | --- |
| Syntax | `type("value")` |
| Multiple values | Not applicable |
| Value operator | `EQUALS` |
| Case-sensitive value | Not applicable |

## Dynatrace entity ID

The Dynatrace entity ID of the requested entity.

To specify several IDs, separate them by a comma (`,`). All requested entities must be of the same type.

You can fetch the list of available entities with the [GET entities list](/docs/dynatrace-api/environment-api/entity-v2/get-entities-list "View a list of monitored entities via Dynatrace API.") call.

|  |  |
| --- | --- |
| Syntax | `entityId("id-1","id-2")` |
| Multiple values | Applicable |
| Value operator | `EQUALS` |
| Case-sensitive value | Not applicable |

## Entity name

The name of the requested entity.

You can fetch the list of available entities with the [GET entities list](/docs/dynatrace-api/environment-api/entity-v2/get-entities-list "View a list of monitored entities via Dynatrace API.") call.

|  |  |
| --- | --- |
| Syntax | `entityName("name")` |
| Multiple values | Not applicable |
| Value operator | `CONTAINS` |
| Case-sensitive value | Not applicable |

### Starts with modification

Changes the value operator of the entity name criterion to `BEGINS WITH`.

|  |  |
| --- | --- |
| Syntax | `entityName.startsWith("name")` |
| Multiple values | Not applicable |
| Value operator | `BEGINS WITH` |
| Case-sensitive value | Not applicable |

### Equals modification

Changes the value operator of the entity name criterion to `EQUALS`.

|  |  |
| --- | --- |
| Syntax | `entityName.equals("name")` |
| Multiple values | Not applicable |
| Value operator | `EQUALS` |
| Case-sensitive value | Not applicable |

### One of values modification

Enables you to provide multiple values for the entity name criterion.

|  |  |
| --- | --- |
| Syntax | `entityName.in("name1","name2")` |
| Multiple values | Applicable |
| Value operator | `EQUALS` |
| Case-sensitive value | Not applicable |

### Case sensitive modification

By default entity names evaluation disregards the case. You can make the criterion stricter by using the `caseSensitive` modification. It takes any entity name criterion as an argument (including those already modified with `.startsWith` or `.equals` modifiers) and evaluates values as case-sensitive.

|  |  |
| --- | --- |
| Syntax | `caseSensitive(<entity name criterion>)` |
| Multiple arguments | Not applicable |

## Entity attribute

The attribute nameâattribute value pair that the requested entity should have.

To fetch the list of available attributes, execute the [GET entity type](/docs/dynatrace-api/environment-api/entity-v2/get-entity-type "View the details of a monitored entity type via Dynatrace API.") call and check the **properties** field. You can use attributes with values that can be represented by a string.

|  |  |
| --- | --- |
| Syntax | `<attribute name>("attribute value")` |
| Multiple values | Applicable |
| Value operator | `EQUALS` |
| Case-sensitive attribute name | Not applicable |
| Case-sensitive attribute value | Applicable |

### Exists modification

Changes the operator of the entity attribute criterion to `EXISTS`. In this case, the condition selects the entities that have the attribute, regardless of the attribute's value.

|  |  |
| --- | --- |
| Syntax | `<attribute name>.exists()` |
| Operator | `EXISTS` |

## Tag

The tag of the requested entities. Tags in `[context]key:value`, `key:value`, and `value` formats are detected and parsed automatically. If a value-only tag has a colon (`:`) in it, you must escape the colon with a backslash(`\`). Otherwise, the tag will be parsed as a `key:value` tag.

To specify several tags, separate them by a comma (`,`). An entity with **any** of the specified tags is included to the response.

You can fetch the list of available tags with the [GET custom tags](/docs/dynatrace-api/environment-api/custom-tags/get-tags "View custom tags of monitored entities via Dynatrace API.") and the [GET auto-tags](/docs/dynatrace-api/configuration-api/automatically-applied-tags-api/get-all "View all automatically applied tags of your environment via the Dynatrace API.") calls.

|  |  |
| --- | --- |
| Syntax | `tag("[context]key1:value-1","key2:value-2","value-3")` |
| Multiple values | Applicable |
| Value operator | `EQUALS` |
| Case-sensitive value | Applicable |

## Management zone ID

The ID of the management zone to which the requested entities belong.

To specify several IDs, separate them by a comma (`,`).

You can fetch the list of available management zones with the [GET all management zones](/docs/dynatrace-api/configuration-api/management-zones-api/get-all "View all management zones of your environment via the Dynatrace API.") call.

|  |  |
| --- | --- |
| Syntax | `mzId("123456789","987654321")` |
| Multiple values | Applicable |
| Value operator | `EQUALS` |
| Case-sensitive value | n/a |

## Management zone name

The name of the management zone to which the requested entities belong.

To specify several names, separate them by a comma (`,`).

You can fetch the list of available management zones with the [GET all management zones](/docs/dynatrace-api/configuration-api/management-zones-api/get-all "View all management zones of your environment via the Dynatrace API.") call.

|  |  |
| --- | --- |
| Syntax | `mzName("name-1","name-2")` |
| Multiple values | Applicable |
| Value operator | `EQUALS` |
| Case-sensitive value | Applicable |

## Health state

The health state of the requested entities. Possible values are `HEALTHY` and `UNHEALTHY`.

|  |  |
| --- | --- |
| Syntax | `healthState("HEALTHY")` |
| Multiple values | Not applicable |
| Value operator | `EQUALS` |
| Case-sensitive value | Applicable |

## First seen

The timestamp (UTC milliseconds) when the entity was seen for the first time.

Syntax

`firstSeenTms.<operator>(timestamp)`

Multiple values

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

Value operator

* `lte`: earlier than or at the specified time
* `lt`: earlier than the specified time
* `gte`: later than or at the specified time
* `gt`: later than the specified time

Case-sensitive value

n/a

## Relationships

Relationships that the requested entity should have.

To fetch the list of available relationships, issue the [GET entity type](/docs/dynatrace-api/environment-api/entity-v2/get-entity-type "View the details of a monitored entity type via Dynatrace API.") call and check the **fromRelationships** and **toRelationships** fields.

Syntax

* `fromRelationships.<relationship>(<entitySelector>)`
* `toRelationships.<relationship>(<entitySelector>)`

Multiple arguments

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

Note

Takes an entity selector as an attribute.

## Negate criterion

You can use the `not` modification to invert any criterion except for **type**. It takes a criterion as an argument and inverts the condition. For example, the `not(tag("Infrastructure:Linux"))` criterion selects entities that do *not* have the **Infrastructure:Linux** tag.

You can use the negated criteria as part of complicated selectors, just like any other criteria.

|  |  |
| --- | --- |
| Syntax | `not (<criterion>)` |
| Multiple arguments | Not applicable |
| Note | Doesn't support [**type** criteria](#type). |

## Related topics

* [Custom tags API](/docs/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.")
* [Metrics API v2](/docs/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.")
* [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.")
* [Problems API v2](/docs/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers.")


---


## Source: security-context.md


---
title: Monitored entities API - security context
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/entity-v2/security-context
scraped: 2026-02-16T09:33:25.800014
---

# Monitored entities API - security context

# Monitored entities API - security context

* Reference
* Updated on Jun 06, 2025
* Deprecated

This API is deprecated. Use the [Management zones](/docs/dynatrace-api/environment-api/settings/schemas/builtin-management-zones "View builtin:management-zones settings schema table of your monitoring environment via the Dynatrace API.") schema (`builtin:management-zones`) of the Settings API instead.

Create or delete security context for monitored entities.

Matching entities will have a management zone assigned if the given security context matches the name of an already existing management zone. This endpoint does not create a new management zone if there is no management zone with the provided name.

Management zone rules will not apply to entities with a set security context. To be able to apply them again, you need to delete the security context.

For more information on security context, see [Grant access to entities with security context](/docs/manage/identity-access-management/use-cases/access-security-context "Grant access to entities with security context").

## Create the security context

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/entities/securityContext` |
| POST | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/entities/securityContext` |

## Authentication

To execute this request, you need an access token with `settings.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| entitySelector | string | Defines the scope of the entities to set the security context for. Only entities that can have management zones are considered for this operation  You must set one of these criteria:  * Entity type: `type("TYPE")` * Dynatrace entity ID: `entityId("id")`. You can specify several IDs, separated by a comma (`entityId("id-1","id-2")`). All requested entities must be of the same type.  You can add one or more of the following criteria. Values are case-sensitive and the `EQUALS` operator is used unless otherwise specified.  * Tag: `tag("value")`. Tags in `[context]key:value`, `key:value`, and `value` formats are detected and parsed automatically. Any colons (`:`) that are part of the key or value must be escaped with a backslash(`\`). Otherwise, it will be interpreted as the separator between the key and the value. All tag values are case-sensitive. * Management zone ID: `mzId(123)` * Management zone name: `mzName("value")` * Entity name: + `entityName.equals`: performs a non-casesensitive `EQUALS` query.   + `entityName.startsWith`: changes the operator to `BEGINS WITH`.   + `entityName.in`: enables you to provide multiple values. The `EQUALS` operator applies.   + `caseSensitive(entityName.equals("value"))`: takes any entity name criterion as an argument and makes the value case-sensitive. * Health state (HEALTHY,UNHEALTHY): `healthState("HEALTHY")` * First seen timestamp: `firstSeenTms.<operator>(now-3h)`. Use any timestamp format from the **from**/**to** parameters.   The following operators are available: + `lte`: earlier than or at the specified time   + `lt`: earlier than the specified time   + `gte`: later than or at the specified time   + `gt`: later than the specified time * Entity attribute: `<attribute>("value1","value2")` and `<attribute>.exists()`. To fetch the list of available attributes, execute the [GET entity typeï»¿](https://dt-url.net/2ka3ivt) request and check the **properties** field of the response. * Relationships: `fromRelationships.<relationshipName>()` and `toRelationships.<relationshipName>()`. This criterion takes an entity selector as an attribute. To fetch the list of available relationships, execute the [GET entity typeï»¿](https://dt-url.net/2ka3ivt) request and check the **fromRelationships** and **toRelationships** fields. * Negation: `not(<criterion>)`. Inverts any criterion except for **type**.  For more information, see [Entity selectorï»¿](https://dt-url.net/apientityselector) in Dynatrace Documentation.  To set several criteria, separate them with a comma (`,`). For example, `type("HOST"),healthState("HEALTHY")`. Only results matching **all** criteria are included in the response.  The maximum string length is 2,000 characters. | query | Required |
| from | string | The start of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the relative timeframe of three days is used (`now-3d`). | query | Optional |
| to | string | The end of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the current timestamp is used. | query | Optional |
| body | [SecurityContextDtoImpl](#openapi-definition-SecurityContextDtoImpl) | The JSON body of the request. Contains security context to be set for the matching entities. | body | Optional |

### Request body objects

#### The `SecurityContextDtoImpl` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| securityContext | string[] | The security context, that will be set for matching entities. If there exists a management zone with this name, it will be set for all matching entities, overriding all automatic management zone rules. | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"securityContext": [



"string"



]



}
```

### Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SecurityContextResultDto](#openapi-definition-SecurityContextResultDto) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `SecurityContextResultDto` object

The response payload holding the result of the security context application.

| Element | Type | Description |
| --- | --- | --- |
| entityIds | string[] | The entity ids that matched the entity selector and now have the supplied security context set. |
| managementZoneIds | integer[] | The management zone ids that is applied to the entity ids, if the security context matched an existing management zone's name, otherwise null. |

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



"entityIds": [



"string"



],



"managementZoneIds": [



1



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

## Delete the security context

|  |  |  |
| --- | --- | --- |
| DELETE | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/entities/securityContext` |
| DELETE | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/entities/securityContext` |

## Authentication

To execute this request, you need an access token with `settings.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| entitySelector | string | Defines the scope of the entities to set the security context for. Only entities that can have management zones are considered for this operation  You must set one of these criteria:  * Entity type: `type("TYPE")` * Dynatrace entity ID: `entityId("id")`. You can specify several IDs, separated by a comma (`entityId("id-1","id-2")`). All requested entities must be of the same type.  You can add one or more of the following criteria. Values are case-sensitive and the `EQUALS` operator is used unless otherwise specified.  * Tag: `tag("value")`. Tags in `[context]key:value`, `key:value`, and `value` formats are detected and parsed automatically. Any colons (`:`) that are part of the key or value must be escaped with a backslash(`\`). Otherwise, it will be interpreted as the separator between the key and the value. All tag values are case-sensitive. * Management zone ID: `mzId(123)` * Management zone name: `mzName("value")` * Entity name: + `entityName.equals`: performs a non-casesensitive `EQUALS` query.   + `entityName.startsWith`: changes the operator to `BEGINS WITH`.   + `entityName.in`: enables you to provide multiple values. The `EQUALS` operator applies.   + `caseSensitive(entityName.equals("value"))`: takes any entity name criterion as an argument and makes the value case-sensitive. * Health state (HEALTHY,UNHEALTHY): `healthState("HEALTHY")` * First seen timestamp: `firstSeenTms.<operator>(now-3h)`. Use any timestamp format from the **from**/**to** parameters.   The following operators are available: + `lte`: earlier than or at the specified time   + `lt`: earlier than the specified time   + `gte`: later than or at the specified time   + `gt`: later than the specified time * Entity attribute: `<attribute>("value1","value2")` and `<attribute>.exists()`. To fetch the list of available attributes, execute the [GET entity typeï»¿](https://dt-url.net/2ka3ivt) request and check the **properties** field of the response. * Relationships: `fromRelationships.<relationshipName>()` and `toRelationships.<relationshipName>()`. This criterion takes an entity selector as an attribute. To fetch the list of available relationships, execute the [GET entity typeï»¿](https://dt-url.net/2ka3ivt) request and check the **fromRelationships** and **toRelationships** fields. * Negation: `not(<criterion>)`. Inverts any criterion except for **type**.  For more information, see [Entity selectorï»¿](https://dt-url.net/apientityselector) in Dynatrace Documentation.  To set several criteria, separate them with a comma (`,`). For example, `type("HOST"),healthState("HEALTHY")`. Only results matching **all** criteria are included in the response.  The maximum string length is 2,000 characters. | query | Required |
| from | string | The start of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the relative timeframe of three days is used (`now-3d`). | query | Optional |
| to | string | The end of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the current timestamp is used. | query | Optional |

### Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SecurityContextResultDto](#openapi-definition-SecurityContextResultDto) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `SecurityContextResultDto` object

The response payload holding the result of the security context application.

| Element | Type | Description |
| --- | --- | --- |
| entityIds | string[] | The entity ids that matched the entity selector and now have the supplied security context set. |
| managementZoneIds | integer[] | The management zone ids that is applied to the entity ids, if the security context matched an existing management zone's name, otherwise null. |

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



"entityIds": [



"string"



],



"managementZoneIds": [



1



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


---


## Source: entity-v2.md


---
title: Monitored entities API
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/entity-v2
scraped: 2026-02-16T21:19:20.918698
---

# Monitored entities API

# Monitored entities API

* Reference
* Published May 28, 2020

[### List entities

Get an overview of entities you're monitoring with Dynatrace.](/docs/dynatrace-api/environment-api/entity-v2/get-entities-list "View a list of monitored entities via Dynatrace API.")[### View an entity

Get the properties of a particular entity.](/docs/dynatrace-api/environment-api/entity-v2/get-entity "View parameters of a monitored entity via Dynatrace API.")[### Select the data you need

Learn how to use entity selector to fine-tune the entity scope of your query.](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.")[### List entity types

Get an overview of entity types you're monitoring with Dynatrace.](/docs/dynatrace-api/environment-api/entity-v2/get-all-entity-types "View all types of monitored entities in your environment via Dynatrace API.")[### View an entity type

Get the properties of a particular entity type.](/docs/dynatrace-api/environment-api/entity-v2/get-entity-type "View the details of a monitored entity type via Dynatrace API.")[### Create custom device

Create or update a custom device with the exact parameters you need.](/docs/dynatrace-api/environment-api/entity-v2/post-custom-device "Create or update a custom device via Dynatrace API.")

## Related topics

* [Custom tags API](/docs/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.")


---


## Source: post-event.md


---
title: Events API v2 - POST an event
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/events-v2/post-event
scraped: 2026-02-15T21:24:54.169784
---

# Events API v2 - POST an event

# Events API v2 - POST an event

* Reference
* Published Nov 05, 2021

Ingests a custom event to Dynatrace.

The request consumes an `application/json` payload.

The ingestion of custom events consumes [Davis Data Units (DDUs)](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).") from the events pool.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/events/ingest` |
| POST | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/events/ingest` |

## Authentication

To execute this request, you need an access token with `events.ingest` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [EventIngest](#openapi-definition-EventIngest) | The JSON body of the request. Contains properties of the new event. | body | Optional |

### Request body objects

#### The `EventIngest` object

The configuration of an event to be ingested.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| endTime | integer | The end time of the event, in UTC milliseconds.  If not set, the start time plus timeout is used. | Optional |
| entitySelector | string | The [entity selectorï»¿](https://dt-url.net/apientityselector), defining a set of Dynatrace entities to be associated with the event.  Only entities that have been active within the last 24 hours can be selected. Note that the `entityId` filter bypasses this time constraint, allowing events to be ingested for entities that have been inactive for more than 24 hours.  If not set, the event is associated with the environment (`dt.entity.environment`) entity. | Optional |
| eventType | string | The type of the event. The element can hold these values * `AVAILABILITY_EVENT` * `CUSTOM_ALERT` * `CUSTOM_ANNOTATION` * `CUSTOM_CONFIGURATION` * `CUSTOM_DEPLOYMENT` * `CUSTOM_INFO` * `ERROR_EVENT` * `MARKED_FOR_TERMINATION` * `PERFORMANCE_EVENT` * `RESOURCE_CONTENTION_EVENT` * `WARNING` | Required |
| properties | object | A map of event properties.  * To set event properties with predefined behavior, use classic `dt.event.*` and `dt.davis.*` properties. To check which properties belong to classic API, see [Events API v2 - GET all event propertiesï»¿](https://dt-url.net/9622g1w). * To attach entity information to an event, use `dt.entity.*` keys. * To provide additional info, you can use any key outside of the `dt.*` namespace.  Values of event properties with predefined behavior must fulfill the requirements of the respective property.  A maximum of 100 properties can be specified. A property key is allowed to contain up to 100 characters. A property value is allowed to contain up to 4096 characters. | Optional |
| startTime | integer | The start time of the event, in UTC milliseconds.  If not set, the current timestamp is used.  Depending on the event type, the start time must not lie in the past more than 6 hours for problem-opening events and 30 days for info events.  Depending on the event type, the start time must not lie in the future more than 5 minutes for problem-opening events and 7 days for info events.  Events that can be sent up to 7 days in the future:  * `CUSTOM_ANNOTATION` * `CUSTOM_CONFIGURATION` * `CUSTOM_DEPLOYMENT` * `CUSTOM_INFO` * `MARKED_FOR_TERMINATION` | Optional |
| timeout | integer | The timeout of the event, in minutes.  If not set, 15 is used.  The timeout will automatically be capped to a maximum of 360 minutes (6 hours).  Problem-opening events can be refreshed and therefore kept open by sending the same payload again. | Optional |
| title | string | The title of the event. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"endTime": 1,



"entitySelector": "string",



"eventType": "AVAILABILITY_EVENT",



"properties": {},



"startTime": 1,



"timeout": 1,



"title": "string"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [EventIngestResults](#openapi-definition-EventIngestResults) | The event ingest request was received by the server. The response body indicates for each event whether its creation was successful. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `EventIngestResults` object

The results of an event ingest.

| Element | Type | Description |
| --- | --- | --- |
| eventIngestResults | [EventIngestResult[]](#openapi-definition-EventIngestResult) | The result of each created event report. |
| reportCount | integer | The number of created event reports. |

#### The `EventIngestResult` object

The result of a created event report.

| Element | Type | Description |
| --- | --- | --- |
| correlationId | string | The correlation ID of the created event. |
| status | string | The status of the ingestion. The element can hold these values * `INVALID_ENTITY_TYPE` * `INVALID_METADATA` * `INVALID_TIMESTAMPS` * `OK` |

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



"eventIngestResults": [



{



"correlationId": "string",



"status": "INVALID_ENTITY_TYPE"



}



],



"reportCount": 1



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

## Examples

Example 1

Example 2

Example 3

Use case

An operations team wants to push a **Marked for termination** event to all the hosts that are planned to be removed. They also want to include the purpose for the deletion and a job identifier. The hosts to be removed are gathered in a designated host group.

In this example, the request sends a **Marked for termination** event to hosts that are planned to be removed. Such hosts are identified by the **cloud-burst-hosts** host group. The event automatically applies to all hosts that are part of the group. The purpose for termination and automation job number are provided as additional information.

The API token is passed in the **Authorization** header.

#### Curl

```
curl --request POST \



--url https://mySampleEnv.live.dynatrace.com/api/v2/events/ingest \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



--header 'Content-Type: application/json' \



--data '{



"eventType": "MARKED_FOR_TERMINATION",



"title": "Planned host downscale",



"entitySelector": "type(HOST),fromRelationship.isInstanceOf(type(HOST_GROUP),entityName(cloud-burst-hosts))",



"properties": {



"job.number": "21234346"



}



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/events/ingest
```

#### Request body

```
{



"eventType": "MARKED_FOR_TERMINATION",



"title": "Planned host downscale",



"entitySelector": "type(HOST),fromRelationship.isInstanceOf(type(HOST_GROUP),entityName(cloud-burst-hosts))",



"properties": {



"job.number": "21234346"



}



}
```

#### Response body

```
{



"reportCount": 2,



"eventIngestResults": [



{



"correlationId": "41f5d263011a6c9a",



"status": "OK"



},



{



"correlationId": "80eae4d163cc5760",



"status": "OK"



}



]



}
```

#### Response code

201

Use case

A DevOps team wants to connect their load test tool with Dynatrace to annotate a service that is currently undergoing a load test. Later, when Dynatrace raises a problem caused by the load test, the problem details will include this information, simplifying the triage process.

In this example, the request sends a **Custom info** event to the **BookingService** service, marking it as a target of a load test.

The API token is passed in the **Authorization** header.

#### Curl

```
curl --request POST \



--url https://mySampleEnv.live.dynatrace.com/api/v2/events/ingest \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



--header 'Content-Type: application/json' \



--data '{



"eventType": "CUSTOM_INFO",



"title": "Loadtest start",



"timeout": 30,



"entitySelector": "type(SERVICE),entityName.equals(BookingService)",



"properties": {



"Tool": "MyLoadTool",



"Load per minute": "100",



"Load pattern": "production"



}



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/events/ingest
```

#### Request body

```
{



"eventType": "CUSTOM_INFO",



"title": "Loadtest start",



"timeout": 30,



"entitySelector": "type(SERVICE),entityName.equals(BookingService)",



"properties": {



"Tool": "MyLoadTool",



"Load per minute": "100",



"Load pattern": "production"



}



}
```

#### Response body

```
{



"reportCount": 1,



"eventIngestResults": [



{



"correlationId": "eba82f647696e485",



"status": "OK"



}



]



}
```

#### Response code

201

Use case

The operations team of a large retailer wants to trigger an alert in Dynatrace whenever their catalog update batch process fails. They want to create an event and alert in Dynatrace, but they donât want Dynatrace Intelligence to merge this externally created event with any larger incident.

In this example, the request sends an **Error** event to the **BookingService** service, indicating a failed update. The **dt.event.allow\_davis\_merge** property is set to `false`, preventing Dynatrace Intelligence from merging this event with any other event.

The API token is passed in the **Authorization** header.

#### Curl

```
curl --request POST \



--url https://mySampleEnv.live.dynatrace.com/api/v2/events/ingest \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



--header 'Content-Type: application/json' \



--data '{



"eventType": "ERROR_EVENT",



"title": "Product catalog update failed",



"timeout": 30,



"entitySelector": "type(SERVICE),entityName.equals(BookingService)",



"properties": {



"dt.event.allow_davis_merge": "false",



"Catalog": "APAC travels",



"Batch processor": "travel-catalog"



}



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/events/ingest
```

#### Request body

```
{



"eventType": "ERROR_EVENT",



"title": "Product catalog update failed",



"timeout": 30,



"entitySelector": "type(SERVICE),entityName.equals(BookingService)",



"properties": {



"dt.event.allow_davis_merge": "false",



"Catalog": "APAC travels",



"Batch processor": "travel-catalog"



}



}
```

#### Response body

```
{



"reportCount": 1,



"eventIngestResults": [



{



"correlationId": "cefb7ae03ac720b6",



"status": "OK"



}



]



}
```

#### Response code

201

## Related topics

* [Event categories](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Learn about different categories of events and supported event types, along with their severity levels, and the logic behind raising them.")
* [Event analysis and correlation](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Gain an understanding of the Events section on each host, process, and service overview page.")


---


## Source: events-v2.md


---
title: Events API v2
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/events-v2
scraped: 2026-02-16T21:28:52.730060
---

# Events API v2

# Events API v2

* Reference
* Published Aug 06, 2021

[### List events

Get an overview of events in your Dynatrace environment.](/docs/dynatrace-api/environment-api/events-v2/get-events "List events of your monitoring environment via the Dynatrace API.")[### View an event

Get the properties of an event.](/docs/dynatrace-api/environment-api/events-v2/get-event "View parameters of an event via the Events API v2.")[### Ingest an event

Push external events to your Dynatrace environment.](/docs/dynatrace-api/environment-api/events-v2/post-event "Ingests an event via the Dynatrace API.")

[### List event types

Get an overview of all event types that Dynatrace creates.](/docs/dynatrace-api/environment-api/events-v2/get-event-types "List event types via the Dynatrace API.")[### View an event type

Get the details of an event type.](/docs/dynatrace-api/environment-api/events-v2/get-event-type "View parameters of an event type via the Dynatrace API.")

[### List event properties

Get an overview of all event properties that Dynatrace provides.](/docs/dynatrace-api/environment-api/events-v2/get-event-properties "List all event properties via the Dynatrace API.")[### View an event property

Get the details of an event property.](/docs/dynatrace-api/environment-api/events-v2/get-event-property "View an event property via the Dynatrace API.")

## Related topics

* [Event categories](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Learn about different categories of events and supported event types, along with their severity levels, and the logic behind raising them.")
* [Event analysis and correlation](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Gain an understanding of the Events section on each host, process, and service overview page.")


---


## Source: hub.md


---
title: Hub items API
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/hub
scraped: 2026-02-16T21:32:55.388325
---

# Hub items API

# Hub items API

* Reference
* Published Feb 07, 2023

[### List categories

View categories of Hub items.](/docs/dynatrace-api/environment-api/hub/get-categories "View categories of Hub items via the Hub capabilities API.")[### List items

View Hub items.](/docs/dynatrace-api/environment-api/hub/get-items "View Hub items via the Hub capabilities API.")[### Get technology

View technology details.](/docs/dynatrace-api/environment-api/hub/get-technology "View technology details via the Hub capabilities API.")

## Extensions v1

[### View an extension v1

Get an overview of a version 1 extension.](/docs/dynatrace-api/environment-api/hub/get-extension-v1 "View details about a version 1 extension via the Hub capabilities API.")[### Download an extension v1

Download the artifact of a version 1 extension.](/docs/dynatrace-api/environment-api/hub/get-extension-v1-artifact "Download the artifact of a version 1 extension via the Hub capabilities API.")

## Extensions 2.0

[### View an extension 2.0

Get an overview of an extension 2.0.](/docs/dynatrace-api/environment-api/hub/get-extension-20 "View the details of an extension 2.0 via the Hub capabilities API.")[### Add an extension 2.0 to environment

Register an extension 2.0 in your environment.](/docs/dynatrace-api/environment-api/hub/post-extension-20-to-evironment "Add an extension 2.0 to your environment via the Hub capabilities API.")[### Update an extension 2.0

Update an extension 2.0 to the latest version.](/docs/dynatrace-api/environment-api/hub/post-update-extension-20 "Update an extension 2.0 via the Hub capabilities API.")[### Update an extension 2.0 metadata

Update the metadata of an extension 2.0.](/docs/dynatrace-api/environment-api/hub/put-update-extension-20-metadata "Update the metadata of an extension 2.0 via the Hub capabilities API.")[### Add release notes to an extension 2.0 release

Set the release notes of an extension 2.0 release.](/docs/dynatrace-api/environment-api/hub/put-extension-20-release-notes "Set the release notes of an extension 2.0 release via the Hub capabilities API.")


---


## Source: log-monitoring-v2.md


---
title: Log Monitoring API v2
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/log-monitoring-v2
scraped: 2026-02-16T09:31:00.836234
---

# Log Monitoring API v2

# Log Monitoring API v2

* Reference
* Updated on Nov 20, 2025

Log Monitoring API v2 deprecation

The `search`, `export`, and `aggregate` endpoints of this API are deprecated and will be removed by the end of 2027. Use the [Logs on Grail APIï»¿](https://dt-url.net/zb0381u) instead.

[### Search

Fetch a limited number of log records matching your criteria.

Deprecated](/docs/dynatrace-api/environment-api/log-monitoring-v2/get-search-logs "Fetch log records via the Log Monitoring API v2.")[### Export

Fetch an unlimited number of log records matching your criteria.

Deprecated](/docs/dynatrace-api/environment-api/log-monitoring-v2/get-export-logs "Fetch log records via the Log Monitoring API v2.")[### Aggregate

Fetch aggregated log records matching your criteria.

Deprecated](/docs/dynatrace-api/environment-api/log-monitoring-v2/get-aggregate-logs "Fetch the aggregated log records via the Log Monitoring API v2.")[### Ingest

Push custom log records to Dynatrace.](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.")

## Related topics

* [Log Monitoring Classic](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.")


---


## Source: metric-expressions.md


---
title: Metrics API - Metric expressions
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/metric-v2/metric-expressions
scraped: 2026-02-16T21:29:50.927774
---

# Metrics API - Metric expressions

# Metrics API - Metric expressions

* Reference
* Updated on Jul 29, 2022

Metric expressions enable you to use simple arithmetic operations right in the metric selector.

For example, this expression calculates the ratio (as a percentage) of two metrics:

```
metric1 / metric2 * 100
```

For the operands of the expression, you can use metrics or numbers.

* You need to use brackets to enforce order of operations.
* All metrics with more than 1 data point involved in a metric expression must be of the same resolution.
* You can use any metric as an operand, including metrics modified by any [transformation chain](/docs/dynatrace-api/environment-api/metric-v2/metric-selector "Configure the metric selector for the Metric v2 API."), and you can apply transformations to the result of the expression.

## Limitations

* The selector must contain at least one metric key.
* You can query data points of up to 10 metrics in one query.

For the purposes of this limit, one expression (for example, `metric2 + metric2`) counts as one metric.

## Precedence

Standard mathematical precedence rules applies:

1. Parentheses, metric transformations
2. Negation
3. Multiplication, division
4. Addition, subtraction

## Aggregation

If an aggregation has been applied in a transformation chain, this aggregation is used. If no transformation has been applied, the default aggregation is used. Your metric operands can be of different aggregations. For example, `metric:max - metric:min`.

## Resolving expressions

Metric expressions are resolved as follows:

1. [Form tuple pairs](#tuples) for each pair of metrics.
2. [Align data points](#data) in every tuple.
3. Apply arithmetic operation to aligned data points.

### Tuples

Arithmetic operations use the data points of tuples (unique combinations of metricâdimensionâdimension value) of metrics. Identical tuples of each metric are paired and then their data points are aligned.

If one metric is dimensionless (has just one tuple without dimensions and dimension values), then this single tuple is paired with every tuple of other metrics. The same applies to numbers.

Non-pairable tuples are ignored by the expression and are not presented in the result.

### Data points

Once tuple pairs are formed, the data points are aligned, and then the desired arithmetical operation is applied to the aligned data points.

* If any of the aligned data points is `null`, the expression resolves to `null`.
* If a number is involved in the operation, it is aligned with every data point of the metric operand.
* If one metric is a single data point and the other is a series, the single data point is aligned with every data point of the series.
* If both metrics are a single data point, the data points are aligned and the resulting time slot covers both data points.
* If both metrics are series, the data points are aligned by timestamps.

For any unaligned data points, the expression resolves to `null`.

## Best practices

### Use only when necessary

Use a metric expression only if you cannot accomplish your goal without it. Let's say you want to calculate the average CPU usage of two hosts, `HOST-001` and `HOST-002`. You could do it with a metric expression:

```
(



builtin:host.cpu.usage:filter(eq("dt.entity.host","HOST-001")):splitBy()



+



builtin:host.cpu.usage:filter(eq("dt.entity.host","HOST-002")):splitBy()



)



/2
```

There are two problems with this approach. First, the expression is hard to read and therefore prone to syntax errors. Second, if one of the hosts is offline, the result of the expression is empty. Even though the second problem could be solved by a **default** transformation, usage of the [average aggregation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#aggregation "Configure the metric selector for the Metric v2 API.") is more effective:

```
builtin:host.cpu.usage



:filter(



or(



eq("dt.entity.host","HOST-001"),



eq("dt.entity.host","HOST-002")



)



)



:splitBy()



:avg
```

### Do not convert units

Do not use a metric expression to convert the unit of the data. Use the [**toUnit** transformation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#to-unit "Configure the metric selector for the Metric v2 API.") instead. The only exception to this rule is for units that Dynatrace does not support. Use the [GET all units](/docs/dynatrace-api/environment-api/metrics-units/get-all-units "List all metrics that are available for your monitoring environment via the Dynatrace API.") request to fetch the list of supported units.

### Limit transformation usage

Always apply the [**limit** transformation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#limit-transformation "Configure the metric selector for the Metric v2 API.") to the result of a calculation, not to its operands.

Consider the following query, which attempts to add top-10 CPU usage times to top-10 CPU idle times.

```
builtin:host.cpu.usage:sort(value(avg,descending)):limit(10)



+



builtin:host.cpu.idle:sort(value(avg,descending)):limit(10)
```

If you have a large environment with hundreds of hosts, it is unlikely that the 10 hosts with the highest CPU usage are among the 10 hosts with the highest CPU idle time. The operands won't have matching tuples, therefore the result of the expression will be empty. The solution is to apply the limit to the result of the expression instead:

```
(



builtin:host.cpu.usage



+



builtin:host.cpu.idle



)



:sort(value(auto,descending))



:limit(10)
```

### Cover data gaps with the default transformation

The [**default** transformation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#default "Configure the metric selector for the Metric v2 API.") is particularly valuable for metric expressions. Even though normally the transformation doesn't fill up `null` data points if a metric doesn't have a single data point in the query timeframe, in the metric expression context its semantic is slightly different. As long as a metric on either side of the expression has at least one data point, the transformation will fill the gaps. However, if all metrics in the expression are missing data, the transformation will return empty results.

Consider this example of a ratio expression, where we calculate the error ratio for key user actions:

```
builtin:apps.other.keyUserActions.reportedErrorCount.os



/



builtin:apps.other.keyUserActions.requestCount.os
```

If there are many requests but not a single error in your timeframe, the result will be empty, though an error ratio of `0` would be more meaningful. You can achieve that with the `default(0)` transformation:

```
builtin:apps.other.keyUserActions.reportedErrorCount.os:default(0)



/



builtin:apps.other.keyUserActions.requestCount.os
```

## Examples

Example 1. Build a ratio metric

With a metric expression, you can build your own ratio metrics. Suppose we start with the following metrics:

* **builtin:service.errors.total.count** shows the number of errors of any type in a service
* **builtin:service.errors.server.successCount** shows the number of calls without server-side errors

From them, we can build an error ratio metric:

```
builtin:service.errors.total.count:value:default(0)



/



(



builtin:service.errors.total.successCount:value:default(0)



+



builtin:service.errors.total.count:value:default(0)



)
```

The [**default** transformation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#default "Configure the metric selector for the Metric v2 API.") is used to replace the values of the time slots that have the value `null` with 0.

Metric 1

Metric 2

Result

```
{



"totalCount": 3,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:service.errors.total.count",



"data": [



{



"dimensions": ["SERVICE-B82BFBCB4E264A98"],



"dimensionMap": {



"dt.entity.service": "SERVICE-B82BFBCB4E264A98"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [48763, 81283, 80798]



},



{



"dimensions": ["SERVICE-BE8B6928C46204B5"],



"dimensionMap": {



"dt.entity.service": "SERVICE-BE8B6928C46204B5"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [1096, 1124, 1095]



}



]



}



]



}
```

```
{



"totalCount": 3,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:service.errors.total.successCount",



"data": [



{



"dimensions": ["SERVICE-B82BFBCB4E264A98"],



"dimensionMap": {



"dt.entity.service": "SERVICE-B82BFBCB4E264A98"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [46182, 77110, 76736]



},



{



"dimensions": ["SERVICE-BE8B6928C46204B5"],



"dimensionMap": {



"dt.entity.service": "SERVICE-BE8B6928C46204B5"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [0, 0, 0]



}



]



}



]



}
```

```
{



"totalCount": 3,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:service.errors.total.count/(builtin:service.errors.total.count+builtin:service.errors.total.successCount)",



"data": [



{



"dimensions": ["SERVICE-B82BFBCB4E264A98"],



"dimensionMap": {



"dt.entity.service": "SERVICE-B82BFBCB4E264A98"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [0.513592079625046, 0.513172930621934, 0.5128924549621035]



},



{



"dimensions": ["SERVICE-BE8B6928C46204B5"],



"dimensionMap": {



"dt.entity.service": "SERVICE-BE8B6928C46204B5"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [1, 1, 1]



}



]



}



]



}
```

Example 2. Contribution of a single service to total error count

The **builtin:service.errors.total.count** metric shows the number of errors across your services. The list might be lengthy, and you might be interested in each service's contribution to the error count. A combination of metric transformations and metric expressions can provide this information.

You need these transformations:

* [filter transformation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#filter "Configure the metric selector for the Metric v2 API.") to obtain the error count for the service that you're checking.
* [split by transformation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#splitby "Configure the metric selector for the Metric v2 API.") to merge individual error counts of each service into one.

Then use this expression:

```
builtin:service.errors.total.count:filter(eq("dt.entity.service","SERVICE-B82BFBCB4E264A98")):value:default(0)



/



builtin:service.errors.total.count:splitBy():value:default(0) * 100
```

The [**default** transformation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#default "Configure the metric selector for the Metric v2 API.") is used to replace the values of the time slots that have the value `null` with 0.

Isolated service

Total count

Percentage

```
{



"totalCount": 1,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:service.errors.total.count:filter(eq(\"dt.entity.service\",SERVICE-B82BFBCB4E264A98))",



"data": [



{



"dimensions": ["SERVICE-B82BFBCB4E264A98"],



"dimensionMap": {



"dt.entity.service": "SERVICE-B82BFBCB4E264A98"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [48763, 81283, 80798]



}



]



}



]



}
```

```
{



"totalCount": 1,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:service.errors.total.count:splitBy()",



"data": [



{



"dimensions": [],



"dimensionMap": {},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [49882, 82425, 81911]



}



]



}



]



}
```

```
{



"totalCount": 1,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:service.errors.total.count:filter(eq(\"dt.entity.service\",SERVICE-B82BFBCB4E264A98))/builtin:service.errors.total.count:splitBy()*100",



"data": [



{



"dimensions": ["SERVICE-B82BFBCB4E264A98"],



"dimensionMap": {



"dt.entity.service": "SERVICE-B82BFBCB4E264A98"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [97.75670582574877, 98.61449802851077, 98.64120814054277]



}



]



}



]



}
```

Example 3. Average GC duration

The **builtin:tech.jvm.memory.gc.collectionTime** metric shows the total duration of all garbage collections in a time slot. Information about individual GC times is not available, but we can use the **builtin:tech.jvm.memory.pool.collectionCount** metric showing the number of GCs per time to obtain the average duration of a garbage collection.

Before we start the calculation, we need to align the dimensions of both metrics. To do that, we need to apply the **split by** transformation with the `dt.entity.process_group_instance` argument to the **builtin:tech.jvm.memory.pool.collectionCount** metric.

Additionally, we can sort the result in descending order by applying the [sort transformation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#sort "Configure the metric selector for the Metric v2 API."). The expression looks like this:

```
(



builtin:tech.jvm.memory.gc.collectionTime



/



builtin:tech.jvm.memory.pool.collectionCount:splitBy("dt.entity.process_group_instance")



):sort(value(max,descending))
```

Total GC time

Number of GCs

Average GC duration

```
{



"totalCount": 3,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:tech.jvm.memory.gc.collectionTime",



"data": [



{



"dimensions": ["PROCESS_GROUP_INSTANCE-18A5241823ABC769"],



"dimensionMap": {



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-18A5241823ABC769"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [164670, 171630, 163044]



},



{



"dimensions": ["PROCESS_GROUP_INSTANCE-92605BB8AE962F1C"],



"dimensionMap": {



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-92605BB8AE962F1C"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [6883411, 5977311, 6356225]



},



{



"dimensions": ["PROCESS_GROUP_INSTANCE-4285F2EF6B79E8A9"],



"dimensionMap": {



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-4285F2EF6B79E8A9"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [163368, 162924, 170502]



}



]



}



]



}
```

```
{



"totalCount": 3,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:tech.jvm.memory.pool.collectionCount:splitBy(\"dt.entity.process_group_instance\")",



"data": [



{



"dimensions": ["PROCESS_GROUP_INSTANCE-18A5241823ABC769"],



"dimensionMap": {



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-18A5241823ABC769"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [1727814, 1720686, 1691604]



},



{



"dimensions": ["PROCESS_GROUP_INSTANCE-92605BB8AE962F1C"],



"dimensionMap": {



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-92605BB8AE962F1C"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [31363, 30588, 31419.5]



},



{



"dimensions": ["PROCESS_GROUP_INSTANCE-4285F2EF6B79E8A9"],



"dimensionMap": {



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-4285F2EF6B79E8A9"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [1697262, 1703742, 1722612]



}



]



}



]



}
```

```
{



"totalCount": 3,



"nextPageKey": null,



"result": [



{



"metricId": "(builtin:tech.jvm.memory.gc.collectionTime/builtin:tech.jvm.memory.pool.collectionCount:splitBy(\"dt.entity.process_group_instance\")):sort(value(max,descending))",



"data": [



{



"dimensions": ["PROCESS_GROUP_INSTANCE-92605BB8AE962F1C"],



"dimensionMap": {



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-92605BB8AE962F1C"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [219.47552848898383, 195.41359356610437, 202.3019144162065]



},



{



"dimensions": ["PROCESS_GROUP_INSTANCE-18A5241823ABC769"],



"dimensionMap": {



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-18A5241823ABC769"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [0.09530539745597616, 0.09974510166294141, 0.09638426014599162]



},



{



"dimensions": ["PROCESS_GROUP_INSTANCE-4285F2EF6B79E8A9"],



"dimensionMap": {



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-4285F2EF6B79E8A9"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [0.09625384884596486, 0.09562715481569392, 0.09897876016189368]



}



]



}



]



}
```

For more examples, see the ['Metric Expressions by Example' Github pageï»¿](https://dt-url.net/metric-expressions-by-example).

## Introductory video

Note that the syntax used in this video is based on the old syntax, which required parentheses around each metric and number of an expression.

Metric Expressions


---


## Source: metric-faq.md


---
title: Metrics API - FAQ
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/metric-v2/metric-faq
scraped: 2026-02-16T09:32:08.907013
---

# Metrics API - FAQ

# Metrics API - FAQ

* Reference
* Updated on Nov 16, 2022

## Metric query

Why is the last timestamp of the result in the future?

In Dynatrace, metric data points are stored in time slots of different resolutions. The finest granularity of a time slot is one minute.
The timestamps returned by the metrics query endpoint are the *end times* of these time slots.

For example, if the current time is 09:24 a.m. and you query the last 6 hours at a 1-hour resolution, the timestamp of the last data point will be today at 10:00 a.m. For details, see [Timeframe note](/docs/dynatrace-api/environment-api/metric-v2/get-data-points#timeframe-note "Read data points of one or multiple metrics via Metrics v2 API.").

Why do the returned values grow larger for a larger timeframe?

The data points returned by the query endpoint are time-aggregated. Depending on the query timeframe, the resolution of the data points may be minutes, hours, days, or even years. If you query a larger timeframe, the resolution of your data is likely to be coarser, causing greater values for aggregations such as `sum` or `count`.

If you want to have comparable results for different resolutions, use the [**rate** transformation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#rate "Configure the metric selector for the Metric v2 API."). For example, `:rate(1m)` provides you with the value per minute.

Why is the value of a percentage metric greater than 100% when a fold is used?

For example, the following query might return values higher than 100% even though the metric's unit is `Percent`.

```
builtin:host.availability:splitBy():avg:fold
```

The root cause of this problem is that, when you apply an [**aggregation** transformation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#aggregation "Configure the metric selector for the Metric v2 API.") (by calling `:avg` in the example above), the semantics of the metric are lost and unavailable for transformations that occur later in the transformation chain. That is, when the [**fold** transformation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#fold "Configure the metric selector for the Metric v2 API.") is called, the information that the values should be averaged is no longer available, and the aggregation `sum` is applied instead.

To prevent this issue, do not perform an aggregation before a fold transformation.

```
builtin:host.availability:splitBy():fold
```

Why is the value of a dimension null?

If a [top x](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#remainder "Configure the metric selector for the Metric v2 API.") is applied to a dimension of a metric, only *x* dimension values are retained. All other dimension values are booked into the `remainder` dimension, which has the value `null`.

How can I get pretty names for monitored entities?

By default, the query response only contains the IDs of the monitored entities (for example, `HOST-E1784F5E3F9987CD`).

If you want to have the entity name in the response as well, you need to use the [**names** transformation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#names "Configure the metric selector for the Metric v2 API."). The pretty name is then available in the `dimensionMap` under the dimension key `dt.entity.<entityType>.name` for example, `dt.entity.host.name`).

Why is the result of my metric expression empty?

There are multiple reasons why a metric expression could yield an empty result:

* The dimension keys of the metrics used in the expression do not match.

  If you have metrics with different dimension keys, you need to align the dimensions of the metrics to make a calculation possible. You can use either the [**split by**](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#splitby "Configure the metric selector for the Metric v2 API.") or [**merge**](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#merge "Configure the metric selector for the Metric v2 API.") transformation for this purpose. Consider this query:

  ```
  builtin:host.cpu.iowait



  /



  builtin:host.disk.throughput.read
  ```

  It will produce the `Metric expression contains non-matching dimension-keys.` error, because the **builtin:host.cpu.iowait** metric has only one dimension (**dt.entity.host**), while **builtin:host.disk.throughput.read** has two (**dt.entity.host** and **dt.entity.disk**). To make the query work, you need to get rid of the disk dimension (for example, by using the **merge** transformation).

  ```
  builtin:host.cpu.iowait



  /



  builtin:host.disk.throughput.read:merge(dt.entity.disk)
  ```
* The dimension values do not match.

  For example, the following expression will deliver an empty result because different dimension values cannot be joined.

  ```
  builtin:host.cpu.iowait:filter(eq(dt.entity.host,HOST-001))



  /



  builtin:host.cpu.iowait:filter(eq(dt.entity.host,HOST-002))
  ```

  The solution in this case is to drop the dimensions completely using the [**splitBy** transformation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#splitby "Configure the metric selector for the Metric v2 API.").

  ```
  builtin:host.cpu.iowait:filter(eq(dt.entity.host,HOST-001)):splitBy()



  /



  builtin:host.cpu.iowait:filter(eq(dt.entity.host,HOST-002)):splitBy()
  ```

  One more reason why there are no matching tuples: applying a [**limit** transformation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#limit "Configure the metric selector for the Metric v2 API.") to an operand of the expression may cause matching dimensions to be filtered out. **Always** apply the **limit** transformation to the result of an expression and not to its operands.

  Consider the following query, which attempts to add top-10 CPU usage times to top-10 CPU idle times.

  ```
  builtin:host.cpu.usage:sort(value(avg,descending)):limit(10)



  +



  builtin:host.cpu.idle:sort(value(avg,descending)):limit(10)
  ```

  If you have a large environment with hundreds of hosts, it is unlikely that the 10 hosts with the highest CPU usage are among the 10 hosts with the highest CPU idle time. The operands won't have matching tuples, therefore the result of the expression will be empty. The solution is to apply the limit to the result of the expression instead:

  ```
  (



  builtin:host.cpu.usage



  +



  builtin:host.cpu.idle



  )



  :sort(value(auto,descending))



  :limit(10)
  ```
* There is no data for a metric.

  Consider this example of a ratio expression, where we calculate the error ratio for key user actions:

  ```
  builtin:apps.other.keyUserActions.reportedErrorCount.os



  /



  builtin:apps.other.keyUserActions.requestCount.os
  ```

  If there are many requests but not a single error in your timeframe, the result will be empty, though an error ratio of `0` would be more meaningful. You can achieve that with the `default(0)` transformation:

  ```
  builtin:apps.other.keyUserActions.reportedErrorCount.os:default(0)



  /



  builtin:apps.other.keyUserActions.requestCount.os
  ```

Why can I apply an aggregation that the metric does not support?

After performing a space aggregation using the [**split by**](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#splitby "Configure the metric selector for the Metric v2 API.") or [**merge**](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#merge "Configure the metric selector for the Metric v2 API.") transformation, you can apply arbitrary aggregations to the result.

For example, you can run the following query even though the metric does not natively support percentiles.

```
builtin:host.cpu.user:splitBy("dt.entity.host"):percentile(50)
```

However, because the metric has only one dimension (**dt.entity.host**), no values are in fact space-aggregated. Consequently, the `percentile(50)` aggregation will deliver the same result as `percentile(99)`, because the percentile estimation is based on only one data point in this case.

## Metric ingest

Why is my ingested data point unavailable?

There are multiple reasons why a data point could be unavailable. Try the following solutions.

* Make sure that you receive a response with the `202` HTTP status code for the ingest endpoint.
* It may take a couple of minutes until an ingested data point becomes available via the Metrics REST API and in [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."). The solution is to wait.
* Use the **Metric & Dimension Usage + Rejections** dashboard to check whether the data point was rejected at a later stage. A data point could be accepted by the ingestion endpoint, but later rejected because an invariant was broken.
* Check the filters you're using. The data point may be filtered out by a management zone or a timeframe filter.

Why are my metric keys suffixed with '.count' or '.gauge'?

Metrics with different [payload types](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#payload "Learn how the data ingestion protocol for Dynatrace Metrics API works.") cannot share the same key. Therefore:

* `count` metrics are automatically suffixed with `.count` unless their metric key already ends with `.count` or `_count`
* `gauge` metrics are automatically suffixed with `.gauge` if their key ends with `.count` or `_count`

Why is the metadata of my metric not updated?

You can write the metadata of a metric via the [ingestion protocol](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#metadata "Learn how the data ingestion protocol for Dynatrace Metrics API works.") only if *it has not been set before*. To update the metric metadata, you need to use the [metric browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser#metadata "Browse metrics with the Dynatrace metrics browser.").

Why is an ingested dimension missing?

If you ingest a dimension with an empty value, the whole dimension tuple is dropped at ingestion time. For instance, if you ingest `myMetric,dimEmpty="" 1`, the dimension `dimEmpty` is removed.


---


## Source: metric-selector.md


---
title: Metrics API - Metric selector
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/metric-v2/metric-selector
scraped: 2026-02-15T09:12:36.370935
---

# Metrics API - Metric selector

# Metrics API - Metric selector

* Reference
* Updated on Oct 31, 2025

The metric selector is a powerful instrument for specifying which metrics you want to read via the [GET metric data points](/docs/dynatrace-api/environment-api/metric-v2/get-data-points "Read data points of one or multiple metrics via Metrics v2 API.") request or in the [**Advanced mode** of Data Explorer](/docs/analyze-explore-automate/explorer/explorer-advanced-query-editor "Build advanced queries using the Data Explorer advanced mode.").

In addition, you can transform the resulting set of data points. These transformations modify the plain metric data.

Even if you are building a selector to use in an API call, we recommend that you create your query using the **Code** tab of Data Explorer, which offers built-in tools (for example, auto-completion) to help you construct the query.

## Limitations

* The selector must contain at least one metric key.
* You can query data points of up to 10 metrics in one query.

## Metric dimensions

Many Dynatrace metrics can be referenced with finer granularity using dimensions. For example, the **builtin:host.disk.avail** metric has two dimensions:

* The primary dimension is **Host**
* The secondary dimension is **Disk**

Query a metric with the [GET metric descriptor](/docs/dynatrace-api/environment-api/metric-v2/get-descriptor "View the descriptor of a metric via Metrics v2 API.") call to obtain information about available dimensionsâyou can find them in the **dimensionDefinitions** field of the metric descriptor.

Show descriptor example

```
{



"dimensionDefinitions": [



{



"key": "dt.entity.host",



"name": "Host",



"displayName": "Host",



"index": 0,



"type": "ENTITY"



},



{



"key": "dt.entity.disk",



"name": "Disk",



"displayName": "Disk",



"index": 1,



"type": "ENTITY"



}



]



}
```

Wherever you see the `<dimension>` placeholder in the example syntax, you can select a specific dimension of the metric. You can reference a dimension by its key. For example, for **builtin:host.disk.avail** these are **dt.entity.host** and **dt.entity.disk**.

Transform operations modify the list of dimensions by adding or removing them. Subsequent transformations operate on the modified list of dimensions. Query the metric descriptor with preceding transformations (for example, **builtin:host.disk.avail:names**) to view the new list of available dimensions.

### Remainder dimension

Dynatrace keeps only the top X dimension tuples (the exact number depends on the metric, aggregation, timeframe, and other factors). All other dimension tuples are aggregated into one, called the *remainder* dimension.

If the query result includes this dimension, the `dimensions` and `dimensionMap` value will be `null`. However, if the `dimensionMap` does not contain an entry at all, then this is not the remainder dimension, but rather a literal `null` value.

## Time aggregation

The amount of raw data available in Dynatrace makes it challenging to present the data in a meaningful way. To improve the readability, Dynatrace applies a time aggregation, aligning the data to time slots. You can define the aggregation method via the [**aggregation** transformation](#aggregation).

Even if you don't specify any aggregation transformation, some aggregation applies nevertheless, using the *default transformation* of the metric. Applying the `auto` transformation has the same effect.

Available aggregations vary for each metric. You can check the available aggregations (and the default aggregation) via the [GET metric descriptor](/docs/dynatrace-api/environment-api/metric-v2/get-descriptor "View the descriptor of a metric via Metrics v2 API.") callâlook for the **aggregationTypes** and **defaultAggregation** fields.

The resolution of the resulting time series depends on factors such as the query timeframe and the age of the data. You can, to an extent, control the resolution via the **resolution** query parameter of the [GET metric data points](/docs/dynatrace-api/environment-api/metric-v2/get-data-points "Read data points of one or multiple metrics via Metrics v2 API.") request. The finest available resolution is one minute. Additionally, you can aggregate all data points of a time series into a single data pointâuse the [**fold** transformation](#fold) for that.

#### Example

To illustrate the time aggregations, let's consider an example of the **CPU usage** (`builtin:host.cpu.usage`) metric.

Show metric descriptor

```
{



"metricId": "builtin:host.cpu.usage",



"displayName": "CPU usage %",



"description": "Percentage of CPU time currently utilized.",



"unit": "Percent",



"dduBillable": false,



"created": 0,



"lastWritten": 1668607995463,



"entityType": [



"HOST"



],



"aggregationTypes": [



"auto",



"avg",



"max",



"min"



],



"transformations": [



"filter",



"fold",



"limit",



"merge",



"names",



"parents",



"timeshift",



"sort",



"last",



"splitBy",



"lastReal",



"setUnit"



],



"defaultAggregation": {



"type": "avg"



},



"dimensionDefinitions": [



{



"key": "dt.entity.host",



"name": "Host",



"displayName": "Host",



"index": 0,



"type": "ENTITY"



}



],



"tags": [],



"metricValueType": {



"type": "unknown"



},



"scalar": false,



"resolutionInfSupported": true



}
```

Because its default transformation is `avg`, if you query data points without applying any aggregation, you will obtain the average CPU usage for each time slot of the resulting time series.

To obtain the maximum CPU usage per time slot, use the selector below.

```
builtin:host.cpu.usage:max
```

If you want the single highest usage of a timeframe, you can apply the fold transformation.

```
builtin:host.cpu.usage:fold(max)
```

## Space aggregation

Each metric might carry numerous time series for various dimensions. Space aggregation eases the access to dimensions you're interested in by merging everything else together.

#### Example

Let's consider an example of the **Session count - estimated** (`builtin:apps.other.sessionCount.osAndGeo`) metric.

Show metric descriptor

```
{



"metricId": "builtin:apps.other.sessionCount.osAndGeo:names",



"displayName": "Session count - estimated (by OS, geolocation) [mobile, custom]",



"description": "",



"unit": "Count",



"dduBillable": false,



"created": 0,



"lastWritten": 1668609851154,



"entityType": [



"CUSTOM_APPLICATION",



"MOBILE_APPLICATION"



],



"aggregationTypes": [



"auto",



"value"



],



"transformations": [



"filter",



"fold",



"limit",



"merge",



"names",



"parents",



"timeshift",



"sort",



"last",



"splitBy",



"lastReal",



"setUnit"



],



"defaultAggregation": {



"type": "value"



},



"dimensionDefinitions": [



{



"key": "dt.entity.device_application.name",



"name": "dt.entity.device_application.name",



"displayName": "dt.entity.device_application.name",



"index": 0,



"type": "STRING"



},



{



"key": "dt.entity.device_application",



"name": "Application",



"displayName": "Mobile or custom application",



"index": 1,



"type": "ENTITY"



},



{



"key": "dt.entity.os.name",



"name": "dt.entity.os.name",



"displayName": "dt.entity.os.name",



"index": 2,



"type": "STRING"



},



{



"key": "dt.entity.os",



"name": "Operating system",



"displayName": "OS",



"index": 3,



"type": "ENTITY"



},



{



"key": "dt.entity.geolocation.name",



"name": "dt.entity.geolocation.name",



"displayName": "dt.entity.geolocation.name",



"index": 4,



"type": "STRING"



},



{



"key": "dt.entity.geolocation",



"name": "Geolocation",



"displayName": "Geolocation",



"index": 5,



"type": "ENTITY"



}



],



"tags": [],



"metricValueType": {



"type": "unknown"



},



"scalar": false,



"resolutionInfSupported": true,



"warnings": [



"The field dimensionCardinalities is only supported for untransformed single metric keys and was ignored."



]



}
```

The metric splits the time series based on application, operating system, and geographic location. If you want to investigate data for a particular application regardless of OS and location, you can apply the [**splitBy** transformation](#splitby) as shown below.

```
builtin:apps.other.sessionCount.osAndGeo:splitBy("dt.entity.device_application")
```

You can even merge all dimensions into one by omitting the argument of the transformation. Let's look at the **CPU usage** (`builtin:host.cpu.usage`) metric again. In the example below, the transformation merges measurements of all your hosts into a single time series.

```
builtin:host.cpu.usage:splitBy()
```

### Data filtering

Another way to narrow down the data output is by applying the [**filter** transformation](#filter). For example, you can filter time series based on a certain thresholdâfor details, see the description of the [`series` condition](#series-condition).

In combination with space aggregation, you can build powerful selectors like the one below, which reads the maximum pod count for the `preproduction` Kubernetes cluster split by a cloud application.

```
builtin:kubernetes.pods



:filter(eq("k8s.cluster.name","preproduction"))



:splitBy("dt.entity.cloud_application")



:max
```

You can also filter data based on monitored entities by using the power of the entity selector. The selector below reads the CPU usage for all hosts that have the `easyTravel` tag.

```
builtin:host.cpu.usage



:filter(



in(



"dt.entity.host",entitySelector("type(~"HOST~"),tag(~"easyTravel~")")



)



)
```

## How to use the metric selector

### Select metrics

You need to specify a metric key to get the timeseries for it. You can also specify multiple metric keys separated by commas (for example, `metrickey1,metrickey2`).

When using the [data explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), metric key sections beginning with special characters need to be escaped with quotes (`""`). For example,

| Ingested Metric | Sample Metric Selector |
| --- | --- |
| custom.http5xx | `custom.http5xx:splitBy():auto` |
| custom.5xx\_errors | `custom."5xx_errors":splitBy():auto` |

### Apply transformations

After selecting a metric, you can apply transformations to its data. You can combine any number of transformations. The **metric selector** string is evaluated from left to right. Each successive transformation is applied to the result of the previous transformation. Let's consider an example:

```
builtin:host.cpu.user:sort(value(max,descending)):limit(10)
```

This selector queries the data for the **builtin:host.cpu.usage** metric, sorts the results by the maximum CPU usage, and returns the series for the top 10 hosts.

Dynatrace provides you with a rich set of transformations to manipulate the series data points according to your needs. Below you can find a listing of all available transformations the metric selector offers.

## Aggregation transformation

|  |  |
| --- | --- |
| Syntax | `:<aggregation>` |
| Argument | The desired aggregation. |

Specifies the aggregation of the returned data points. The following aggregation types are available:

Syntax

Description

`:auto`

Applies the default aggregation. To check the default aggregation, query a metric with the [GET metric descriptors](/docs/dynatrace-api/environment-api/metric-v2/get-descriptor "View the descriptor of a metric via Metrics v2 API.") call and check the **defaultAggregation** field.

`:avg`

Calculates the arithmetic mean of all values from the time slot. All `null` values are ignored.

`:count`

Takes the count of the values in the time slot. All `null` values are ignored.

`:histogram`

Exposes the buckets of a histogram metric as dimensions. The value of the `le` dimension denotes the upper boundary (less than or equal to) of each bucket.

`:max`

Selects the highest value from the time slot. All `null` values are ignored.

`:min`

Selects the lowest value from the time slot. All `null` values are ignored.

`:percentile(99.9)`

Calculates the Nth percentile, where N is between `0` and `100` (inclusive).

`:sum`

Sums all values from the time slot. All `null` values are ignored.

`:value`

Takes a single value as is. Only applicable to previously aggregated values and metrics that support the `value` aggregation.

## Default transformation

Syntax

`:default(<number>, always)`

Arguments

* The value (floating-point number) to replace `null` values in the result.
* Optional Whether to replace an empty result with default values. This argument is only valid when preceded by **an empty** [**splitBy** transformation](#splitby).

The **default** transformation replaces `null` values in the payload with the specified value.

When `always` is not specified, a pre-transformed time series must have at least one data point for the transformation to work; if the time series doesn't have any data points, it remains empty after transformation.

Show examples

Before default transformation

After default transformation

```
{



"totalCount": 1,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:tech.jvm.memory.pool.collectionCount",



"data": [



{



"dimensions": [



"PROCESS_GROUP_INSTANCE-A02ED607B5E9DD20",



"30382",



"G1 Old Gen",



"G1 Old Generation"



],



"dimensionMap": {



"poolname": "G1 Old Gen",



"rx_pid": "30382",



"gcname": "G1 Old Generation",



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-A02ED607B5E9DD20"



},



"timestamps": [1623585600000, 1623628800000, 1623672000000, 1623715200000],



"values": [3, null, null, 1]



}



]



}



]



}
```

```
{



"totalCount": 1,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:tech.jvm.memory.pool.collectionCount:default(0)",



"data": [



{



"dimensions": [



"PROCESS_GROUP_INSTANCE-A02ED607B5E9DD20",



"30382",



"G1 Old Gen",



"G1 Old Generation"



],



"dimensionMap": {



"poolname": "G1 Old Gen",



"rx_pid": "30382",



"gcname": "G1 Old Generation",



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-A02ED607B5E9DD20"



},



"timestamps": [1623585600000, 1623628800000, 1623672000000, 1623715200000],



"values": [3, 0, 0, 1]



}



]



}



]



}
```

Before default always transformation

After default always transformation

```
{



"totalCount": 1,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:service.errors.fivexx.count:splitBy():auto:default(0)",



"data": [],



"warnings": [



"The :default operator could not be applied as it requires at least one written data point for the metric in the query timeframe."



]



}



]



}
```

```
{



"totalCount": 1,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:service.errors.fivexx.count:splitBy():auto:default(0,always)",



"data": [



{



"dimensions": [],



"dimensionMap": {},



"timestamps": [1623585600000, 1623628800000, 1623672000000, 1623715200000],



"values": [0, 0, 0, 0]



}



]



}



]



}
```

## Delta transformation

|  |  |
| --- | --- |
| Syntax | `:delta` |
| Arguments | None |

The **delta** transformation replaces each data point with the difference from the previous data point (`0` if the difference is negative). The first data point of the original set is omitted from the result.

You must apply an [aggregation transformation](#aggregation) before using the delta transformation.

Show example

Before delta transformation

After delta transformation

```
{



"totalCount": 1,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:service.keyRequest.count.server:value",



"data": [



{



"dimensions": ["SERVICE_METHOD-BD61DD6DAC1EFDE1"],



"dimensionMap": {



"dt.entity.service_method": "SERVICE_METHOD-BD61DD6DAC1EFDE1"



},



"timestamps": [1630886400000, 1630929600000, 1630972800000, 1631016000000, 1631059200000],



"values": [8338, 8449, 8343, 8372, 8425]



}



]



}



]



}
```

```
{



"totalCount": 1,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:service.keyRequest.count.server:value:delta",



"data": [



{



"dimensions": ["SERVICE_METHOD-BD61DD6DAC1EFDE1"],



"dimensionMap": {



"dt.entity.service_method": "SERVICE_METHOD-BD61DD6DAC1EFDE1"



},



"timestamps": [1630886400000, 1630929600000, 1630972800000, 1631016000000, 1631059200000],



"values": [null, 111, 0, 29, 53]



}



]



}



]



}
```

## Filter transformation

|  |  |
| --- | --- |
| Syntax | `:filter(<condition1>,<condition2>,<conditionN>)` |
| Arguments | A list of filtering conditions. A [dimension](#dimension) has to match **all** of the conditions to pass filtering. |

The **filter** transformation filters the response by the specified criteria. It enables you to filter the data points by a secondary dimension, as **entitySelector** supports only the first dimension, which is an entity. The combination of scope and filter transformation helps you maximize data filtering efficiency.

### Conditions

The `:filter` transformation supports the following conditions.

| Syntax | Description |
| --- | --- |
| `prefix("<dimension>","<expected prefix>")` | Matches if the value of the specified dimension starts with the expected prefix. |
| `suffix("<dimension>","<expected suffix>")` | Matches if the value of the specified dimension ends with the expected suffix. |
| `contains("<dimension>","<expected contained>")` | Matches if the value of the specified dimension contains the expected value. |
| `eq("<dimension>","<expected value>")` | Matches if the value of the specified dimension equals the expected value. |
| `ne("<dimension>","<value to be excluded>")` | The reverse of the `eq` condition. The dimension with the specified name is *excluded* from the response. |
| `in("<dimension>",entitySelector("<selector>")` | Matches if the value of the specified dimension equals *any* of the expected values provided by the [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints."). |
| `existsKey("<dimension>")` | Matches if the specified dimension exists. |
| `remainder("<dimension>")` | Matches if the specified dimension is part of the [remainder](#remainder). |
| `series(<aggregation>,<operator>(<reference value>))` | The response contains only series with data points matching the provided criterion. |

Quotes (`"`) and tildes (`~`) that are part of the dimension key or dimension value (including entity selector syntax) must be escaped with a tilde (`~`).

#### Series condition

The `series` condition filters the time-aggregated value of the data points for a series by the provided criterion. That is, the specified aggregation is applied and then this single value result is compared to the reference value using the specified operator.

For example, for `series(avg, gt(10))`, the average over all data points of the series is calculated first, and then this value is checked to see whether it is greater than 10. If a series does not match this criterion, it is removed from the provided result. That is, the `series` operator cannot be used to filter individual data points of a series. To filter individual data points, you need to use the [**partition** transformation](#partition).

The condition supports the following aggregations and operators.

##### Available aggregations

* `count`
* `min`
* `max`
* `avg`
* `sum`
* `median`
* `percentile(N)`, with N in the `0` to `100` range.
* `value`

##### Available operators

* `lt`: lower than
* `le`: lower than or equal to
* `eq`: equal
* `ne`: not equal
* `gt`: greater than
* `ge`: greater than or equal to

### Compound condition

Each condition can be a combination of subconditions.

Syntax

Description

`and(<subcondition1>,<subcondition2>,<subconditionN>)`

**All** subconditions must be fulfilled.

`or(<subcondition1>,<subcondition2>,<subconditionN>)`

**At least one** subcondition must be fulfilled.

`not(<subcondition>)`

Reverses the subcondition. For example, it turns **contains** into **does not contain**.

### Syntax examples

```
:filter(or(eq("k8s.cluster.name","Server ~"North~""),eq("k8s.cluster.name","Server ~"West~"")))
```

Filters data points to those delivered by either **Server "North"** or **Server "West"**.

```
:filter(and(prefix("App Version","2."),ne("dt.entity.os","OS-472A4A3B41095B09")))
```

Filters data points to those delivered by an application of major version **2** that is not run on the **OS-472A4A3B41095B09** operating system.

## Fold transformation

|  |  |
| --- | --- |
| Syntax | `:fold(<aggregation>)` |
| Arguments | Optional The required [aggregation](#aggregation) method. |

The **fold** transformation combines a data points list into a single data point. To get the result in a specific aggregation, specify the aggregation as an argument. If the specified aggregation is not supported, the default aggregation is used. For example, `:fold(median)` on a gauge metric equals to `:fold(avg)` because median is not supported and avg is the default. If an aggregation has been applied in the transformation chain before, the argument is ignored.

Show example

Before fold transformation

After fold transformation

```
{



"metricId": "builtin:host.disk.avail",



"data": [



{



"dimensions": ["HOST-BB4DF8969CB41C60", "DISK-FB78447211EE76BF"],



"dimensionMap": {



"dt.entity.disk": "DISK-FB78447211EE76BF",



"dt.entity.host": "HOST-BB4DF8969CB41C60"



},



"timestamps": [1612794060000, 1612794120000, 1612794180000],



"values": [4.605786630826667e11, 4.424691002026667e11, 439596351488]



}



]



}
```

```
{



"metricId": "builtin:host.disk.avail:fold",



"data": [



{



"dimensions": ["HOST-BB4DF8969CB41C60", "DISK-FB78447211EE76BF"],



"dimensionMap": {



"dt.entity.disk": "DISK-FB78447211EE76BF",



"dt.entity.host": "HOST-BB4DF8969CB41C60"



},



"timestamps": [1612794480000],



"values": [4.577198298453333e11]



}



]



}
```

## Last transformation

|  |  |
| --- | --- |
| Syntax | `:last<aggregation>` `:lastReal<aggregation>` |
| Arguments | Optional The required [aggregation](#aggregation) method. |

The **last** transformation returns the most recent data point from the query timeframe. To get the result in a specific aggregation, specify the aggregation as an argument. If the specified aggregation is not supported, the default aggregation is used. For example, `:last(median)` on a gauge metric equals to `:last(avg)` because median is not supported and avg is the default. If an aggregation has been applied in the transformation chain before, the argument is ignored.

If the metric before transformation contains multiple tuples (unique combinations of metricâdimensionâdimension value), the most recent timestamp is applied for all tuples. To obtain the actual last timestamp, use the `lastReal` operator.

Show example

Before last transformation

After last transformation

```
{



"totalCount": 3,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:apps.other.sessionCount.osAndGeo:names:splitBy(\"dt.entity.geolocation.name\")",



"data": [



{



"dimensions": ["Austria"],



"dimensionMap": {



"dt.entity.geolocation.name": "Austria"



},



"timestamps": [



1617178800000, 1617180000000, 1617181200000, 1617182400000, 1617183600000, 1617184800000



],



"values": [90, 106, 110, 96, 116, 102]



},



{



"dimensions": ["Switzerland"],



"dimensionMap": {



"dt.entity.geolocation.name": "Switzerland"



},



"timestamps": [



1617178800000, 1617180000000, 1617181200000, 1617182400000, 1617183600000, 1617184800000



],



"values": [176, 168, 178, 174, 183, 172]



},



{



"dimensions": ["Germany"],



"dimensionMap": {



"dt.entity.geolocation.name": "Germany"



},



"timestamps": [



1617178800000, 1617180000000, 1617181200000, 1617182400000, 1617183600000, 1617184800000



],



"values": [1168, 1121, 1154, 1160, 1108, 1135]



}



]



}



]



}
```

```
{



"totalCount": 3,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:apps.other.sessionCount.osAndGeo:names:splitBy(\"dt.entity.geolocation.name\"):last",



"data": [



{



"dimensions": ["Austria"],



"dimensionMap": {



"dt.entity.geolocation.name": "Austria"



},



"timestamps": [1617184800000],



"values": [102]



},



{



"dimensions": ["Switzerland"],



"dimensionMap": {



"dt.entity.geolocation.name": "Switzerland"



},



"timestamps": [1617184800000],



"values": [172]



},



{



"dimensions": ["Germany"],



"dimensionMap": {



"dt.entity.geolocation.name": "Germany"



},



"timestamps": [1617184800000],



"values": [1135]



}



]



}



]



}
```

## Limit transformation

|  |  |
| --- | --- |
| Syntax | `:limit(2)` |
| Argument | The maximum number of tuples in the result. |

The **limit** transformation limits the number of tuples (unique combinations of metricâdimensionâdimension value) in the response. Only the first X tuples are included in the response; the rest are discarded.

To ensure that the required tuples are at the top of the result, apply the [**sort** transformation](#sort) before using the limit.

Show example

Before limit transformation

After limit transformation

```
{



"totalCount": 4,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:apps.other.sessionCount.osAndGeo:names:splitBy(\"dt.entity.geolocation.name\"):sort(value(sum,descending))",



"data": [



{



"dimensions": ["Austria"],



"dimensionMap": {



"dt.entity.geolocation.name": "Austria"



},



"timestamps": [1613559180000],



"values": [6593]



},



{



"dimensions": ["Switzerland"],



"dimensionMap": {



"dt.entity.geolocation.name": "Switzerland"



},



"timestamps": [1613559180000],



"values": [1002]



},



{



"dimensions": ["Germany"],



"dimensionMap": {



"dt.entity.geolocation.name": "Germany"



},



"timestamps": [1613559180000],



"values": [564]



}



]



}



]



}
```

```
{



"totalCount": 2,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:apps.other.sessionCount.osAndGeo:names:splitBy(\"dt.entity.geolocation.name\"):sort(value(sum,descending)):limit(2)",



"data": [



{



"dimensions": ["Austria"],



"dimensionMap": {



"dt.entity.geolocation.name": "Austria"



},



"timestamps": [1613559180000],



"values": [6593]



},



{



"dimensions": ["Switzerland"],



"dimensionMap": {



"dt.entity.geolocation.name": "Switzerland"



},



"timestamps": [1613559180000],



"values": [1002]



}



]



}



]



}
```

## Merge transformation

|  |  |
| --- | --- |
| Syntax | `:merge("<dimension0>","<dimension1>","<dimensionN>")` |
| Arguments | A list of [dimensions](#dimension) to be removed. A dimension must be specified by its key.  Quotes (`"`) and tildes (`~`) that are part of the dimension key must be escaped with a tilde (`~`). |

The **merge** transformation removes the specified dimensions from the result. All series/values that have the same dimensions after the removal are merged into one. The values are recalculated according to the selected aggregation.

You can apply any aggregation to the result of the **merge** transformation, including those that the original metric doesn't support.

Show example

Before merge transformation

After merge transformation

```
{



"totalCount": 2,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:synthetic.browser.event.actionDuration.load.geo:count",



"data": [



{



"dimensions": ["SYNTHETIC_TEST_STEP-002D5D5A0230A18F", "GEOLOCATION-B69A5A40388CC698"],



"dimensionMap": {



"dt.entity.synthetic_test_step": "SYNTHETIC_TEST_STEP-97EF148D63564F29",



"dt.entity.geolocation": "GEOLOCATION-0A41430434C388A9"



},



"timestamps": [1559865600000, 1560124800000, 1560384000000],



"values": [143, 156, 217]



},



{



"dimensions": ["SYNTHETIC_TEST_STEP-002D5D5A0230A18F", "GEOLOCATION-43BA84CAB24D7950"],



"timestamps": [1559865600000, 1560124800000, 1560384000000],



"values": [773, 804, 801]



}



]



}



]



}
```

```
{



"totalCount": 1,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:synthetic.browser.event.actionDuration.load.geo:count:merge(\"dt.entity.geolocation\")",



"data": [



{



"dimensions": ["SYNTHETIC_TEST_STEP-002D5D5A0230A18F"],



"dimensionMap": {



"dt.entity.synthetic_test_step": "SYNTHETIC_TEST_STEP-09D1E2CC97B5878B"



},



"timestamps": [1559865600000, 1560124800000, 1560384000000],



"values": [916, 960, 1018]



}



]



}



]



}
```

## Names transformation

|  |  |
| --- | --- |
| Syntax | `:names` |
| Arguments | None |
| Limitations | Applies only to dimensions of the entity type. |

The **names** transformation adds the name of the [dimension value](#dimension) to the **dimensions** array and **dimensionMap** object of the response. The name of each dimension is placed before the **ID** of the dimension.

Show example

Before names transformation

After names transformation

```
{



"dimensions": ["HOST-BB4DF8969CB41C60", "DISK-FB78447211EE76BF"],



"dimensionMap": {



"dt.entity.disk": "DISK-FB78447211EE76BF",



"dt.entity.host": "HOST-BB4DF8969CB41C60"



}



}
```

```
{



"dimensions": ["l-009", "HOST-BB4DF8969CB41C60", "C:\\", "DISK-FB78447211EE76BF"],



"dimensionMap": {



"dt.entity.disk.name": "C:\\",



"dt.entity.disk": "DISK-FB78447211EE76BF",



"dt.entity.host.name": "l-009",



"dt.entity.host": "HOST-BB4DF8969CB41C60"



}



}
```

## Parents transformation

|  |  |
| --- | --- |
| Syntax | `:parents` |
| Arguments | None |
| Limitations | Applies only to dimensions of the entity type listed below. |

The **parents** transformation adds the parent of the [dimension](#dimension) to the **dimensions** array and **dimensionMap** object of the response. The parent of each dimension is placed before the dimension itself.

This transformation works only if the dimension entity is part of another, bigger entity. For example, `PROCESS_GROUP_INSTANCE` is always the child of the `HOST` it runs on. The following relationships are supported.

| Child dimension | Parent dimension |
| --- | --- |
| SERVICE\_METHOD | SERVICE |
| SERVICE\_INSTANCE | SERVICE |
| APPLICATION\_METHOD | APPLICATION |
| PROCESS\_GROUP\_INSTANCE | HOST |
| DISK | HOST |
| NETWORK\_INTERFACE | HOST |
| SYNTHETIC\_TEST\_STEP | SYNTHETIC\_TEST |
| HTTP\_CHECK\_STEP | HTTP\_CHECK |
| EXTERNAL\_SYNTHETIC\_TEST\_STEP | EXTERNAL\_SYNTHETIC\_TEST |

Show example

Before parents transformation

After parents transformation

```
{



"dimensions": ["SERVICE_METHOD-D9D3A16FA577BF1C"],



"dimensionMap": {



"dt.entity.service": "SERVICE-C22F1E8EA66FF4C5"



}



}
```

```
{



"dimensions": ["SERVICE-C22F1E8EA66FF4C5", "SERVICE_METHOD-D9D3A16FA577BF1C"],



"dimensionMap": {



"dt.entity.service_method": "SERVICE_METHOD-D9D3A16FA577BF1C",



"dt.entity.service": "SERVICE-C22F1E8EA66FF4C5"



}



}
```

## Partition transformation

Syntax

`:partition("<partition dimension key>",<partition1>,<partitionN>)`

Arguments

* The key of the partition dimensionâthis is **not** an existing dimension, but a new one that the transformation will create.

  Quotes (`"`) and tildes (`~`) that are part of the dimension key must be escaped with a tilde (`~`).
* A list of partitions to be appliedâto learn how to specify them, see the [Partition syntax](#partition-syntax) section below.

The **partition** transformation splits data points of a series based on the specified criteria. It introduces a new dimension (the partition dimension), with the value determined by a partition criterion. Data points from the original series are distributed between one or several new series according to partition criteria. In each new series, data points that don't pass the criterion or are already taken by another criterion are replaced with `null`.

### Partition syntax

A single transformation can contain several partitions. These are evaluated from top to bottom; the first matching partition applies.

Each partition must contain a value for the partition dimension that will mark the passed data points and a criterion by which to filter data points.

Note that you can use either the `value` or the `dimension` condition, but not both, in a single partition operator. You can always use `otherwise` conditions.

#### Value conditions

You need to apply an [aggregation transformation](#aggregation) before using value conditions within the partition transformation.

```
value("<partition dimension value>",<criterion>)
```

The following criteria are available:

| Syntax | Description |
| --- | --- |
| `lt(X)` | Less than X |
| `le(X)` | Less than or equal to X |
| `eq(X)` | Equal to X |
| `ne(X)` | Not equal to X |
| `ge(X)` | Greater than or equal to X |
| `gt(X)` | Greater than X |
| `range(X,Y)` | Greater than or equal to X and less than Y |
| `or(<criterion1>,<criterionN>)` | At least one sub-criterion must be fulfilled. |
| `and(<criterion1>,<criterionN>)` | All sub-criteria must be fulfilled. |
| `not(<criterion>)` | Negated criterion matching all values that **do not** fulfill the criterion |

#### Dimension conditions

```
dimension("<partition dimension value>",<criterion>)
```

The following criteria are available.

| Syntax | Description |
| --- | --- |
| `prefix("<dimension>","<expected prefix>")` | Matches if the value of the specified dimension starts with the expected prefix. |
| `suffix("<dimension>","<expected suffix>")` | Matches if the value of the specified dimension ends with the expected suffix. |
| `contains("<dimension>","<expected contained>")` | Matches if the value of the specified dimension contains the expected value. |
| `eq("<dimension>","<expected value>")` | Matches if the value of the specified dimension equals the expected value. |
| `ne("<dimension>","<value to be excluded>")` | The reverse of the `eq` conditionâthe dimension with the specified name is **excluded** from the response. |
| `or(<criterion1>,<criterionN>)` | At least one sub-criterion must be fulfilled. |
| `and(<criterion1>,<criterionN>)` | All sub-criteria must be fulfilled. |
| `not(<criterion>)` | Negated criterion matching all values that **do not** fulfill the criterion |

#### Otherwise condition

```
otherwise("<partition dimension value>")
```

A universal operator matching all valuesâuse it at the end of a partition chain as the default case.

Show example

The following partition transformation is used in this example.

```
:partition(



"Action duration",



value("slow",gt(200)),



value("fast",lt(100)),



value("normal",otherwise)



)
```

It adds the **Action duration** dimension to the metric and splits data points into three categories based on it.

* `fast` for actions faster than `100` milliseconds
* `slow` for actions slower than `200` milliseconds
* `normal` for all other actions

Before partition transformation

After partition transformation

```
{



"totalCount": 1,



"nextPageKey": null,



"resolution": "10m",



"result": [



{



"metricId": "builtin:apps.web.action.domInteractive.load.browser:avg",



"data": [



{



"dimensions": ["APPLICATION_METHOD-E418A4BC1DC2C911", "BROWSER-EFB8A292CB368A8D"],



"dimensionMap": {



"dt.entity.browser": "BROWSER-EFB8A292CB368A8D",



"dt.entity.application_method": "APPLICATION_METHOD-E418A4BC1DC2C911"



},



"timestamps": [



1637152200000, 1637152800000, 1637153400000, 1637154000000, 1637154600000,



1637155200000, 1637155800000, 1637156400000, 1637157000000, 1637157600000,



1637158200000, 1637158800000, 1637159400000



],



"values": [155, 215, 247, 118, 94, 119, 67, 159, 114, 169, 113, 75, 160]



}



]



}



]



}
```

```
{



"totalCount": 3,



"nextPageKey": null,



"resolution": "10m",



"result": [



{



"metricId": "builtin:apps.web.action.domInteractive.load.browser:avg:partition(\"Action duration\",value(slow,gt(200)),value(fast,lt(100)),value(normal,otherwise))",



"data": [



{



"dimensions": [



"BROWSER-EFB8A292CB368A8D",



"APPLICATION_METHOD-E418A4BC1DC2C911",



"normal"



],



"dimensionMap": {



"dt.entity.browser": "BROWSER-EFB8A292CB368A8D",



"dt.entity.application_method": "APPLICATION_METHOD-E418A4BC1DC2C911",



"Action duration": "normal"



},



"timestamps": [



1637152200000, 1637152800000, 1637153400000, 1637154000000, 1637154600000,



1637155200000, 1637155800000, 1637156400000, 1637157000000, 1637157600000,



1637158200000, 1637158800000, 1637159400000



],



"values": [155, null, null, 118, null, 119, null, 159, 114, 169, 113, null, 160]



},



{



"dimensions": ["BROWSER-EFB8A292CB368A8D", "APPLICATION_METHOD-E418A4BC1DC2C911", "fast"],



"dimensionMap": {



"dt.entity.browser": "BROWSER-EFB8A292CB368A8D",



"dt.entity.application_method": "APPLICATION_METHOD-E418A4BC1DC2C911",



"Action duration": "fast"



},



"timestamps": [



1637154000000, 1637154600000, 1637155200000, 1637155800000, 1637156400000,



1637157000000, 1637157600000, 1637158200000, 1637158800000, 1637159400000,



1637160000000, 1637160600000, 1637161200000



],



"values": [null, null, null, null, 94, null, 67, null, null, null, null, 75, null]



},



{



"dimensions": ["BROWSER-EFB8A292CB368A8D", "APPLICATION_METHOD-E418A4BC1DC2C911", "slow"],



"dimensionMap": {



"dt.entity.browser": "BROWSER-EFB8A292CB368A8D",



"dt.entity.application_method": "APPLICATION_METHOD-E418A4BC1DC2C911",



"Action duration": "slow"



},



"timestamps": [



1637154000000, 1637154600000, 1637155200000, 1637155800000, 1637156400000,



1637157000000, 1637157600000, 1637158200000, 1637158800000, 1637159400000,



1637160000000, 1637160600000, 1637161200000



],



"values": [null, 215, 247, null, null, null, null, null, null, null, null, null, null]



}



]



}



]



}
```

## Rate transformation

Syntax

`:rate(5m)`

Argument

The base of the rate. The following values are supported:

`s`: per second  
`m`: per minute  
`h`: per hour  
`d`: per day  
`w`: per week  
`M`: per month  
`y`: per year

The **rate** transformation converts a count-based metric (for example, bytes) into a rate-based metric (for example, bytes per minute).

Any argument can be modified by an integer factor. For example, `5m` means **per 5 minutes** rate. If no argument is specified, the **per 1 minute** rate is used.

You can use the rate transformation with any metric that supports the `VALUE` aggregation. Query a metric with the [GET metric descriptors](/docs/dynatrace-api/environment-api/metric-v2/get-descriptor "View the descriptor of a metric via Metrics v2 API.") call to obtain information about available aggregations. If the metric doesn't support the `VALUE` aggregation, apply the [aggregation transformation](#aggregation) first and then the rate transformation.

* You must apply an [aggregation transformation](#aggregation) before using the rate transformation.
* You can use the rate transformation only once in a single transformation chain.

## Rollup transformation

Syntax

`:rollup(avg,15m)`

Arguments

* The required aggregation of the rollup. Supported aggregations are:

  + `avg`
  + `count`
  + `max`
  + `median`
  + `min`
  + `percentile(N)`, with N in the `0` to `100` range.
  + `sum`
  + `value`
* The duration of the rollup window in minutes. The duration must be a multiple of the query resolution. For example, if the resolution is five minutes, the rollup can be `5m`, `10m`, `15m`, and so on.

The **rollup** transformation smoothes data points, removing any spikes from the requested timeframe.

The transformation takes each data point from the query timeframe, forms a rollup window by looking into past data points (so the initial data point becomes the *last* point of the window), calculates the requested aggregation of all original values, and then replaces each data point in the window with the result of the calculation.

For example, if you specify `:rollup(avg,5m)` and the resolution of the query is one minute, the transformation takes a data point, adds the four previous data point to form a rollup window, and then uses the average of these five datapoints to calculate the final datapoint value.

Limitations

* You must apply an [aggregation transformation](#aggregation) before using the rollup transformation.
* The rollup window duration is limited to **60 minutes**.
* You can roll up data from the last **2 weeks** (including rollup windows) only. That is, the oldest data point of your query can't be more than `2w-windowDuration` in the past.

Show example

Before rollup transformation

After rollup transformation

![Rollup transformation - before](https://dt-cdn.net/images/rollup-before-872-84448811b4.png)

![Rollup transformation - after](https://dt-cdn.net/images/rollup-after-876-3776eb8906.png)

## Smooth transformation

|  |  |
| --- | --- |
| Syntax | `:smooth(skipfirst)` |
| Argument | The smoothing strategy. Only the `skipfirst` strategy is supported. |

The **smooth** transformation smooths a series of data points after a data gap (one or several data points with the value of `null`).

The `skipfirst` strategy replaces the first data point after the data gap with `null`.

Show example

Before smooth transformation

After smooth transformation

```
{



"totalCount": 1,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:service.keyRequest.count.server",



"data": [



{



"dimensions": ["SERVICE_METHOD-BBA9C77B774B0C15"],



"dimensionMap": {



"dt.entity.service_method": "SERVICE_METHOD-BBA9C77B774B0C15"



},



"timestamps": [



1628618460000, 1628618520000, 1628618580000, 1628618640000, 1628618700000,



1628618760000, 1628618820000, 1628618880000, 1628618940000, 1628619000000



],



"values": [null, 15, 13, 15, null, null, 28, 14, 14, 13]



}



]



}



]



}
```

```
{



"totalCount": 1,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:service.keyRequest.count.server:smooth(skipfirst)",



"data": [



{



"dimensions": ["SERVICE_METHOD-BBA9C77B774B0C15"],



"dimensionMap": {



"dt.entity.service_method": "SERVICE_METHOD-BBA9C77B774B0C15"



},



"timestamps": [



1628618460000, 1628618520000, 1628618580000, 1628618640000, 1628618700000,



1628618760000, 1628618820000, 1628618880000, 1628618940000, 1628619000000



],



"values": [null, null, 13, 15, null, null, null, 14, 14, 13]



}



]



}



]



}
```

## Sort transformation

|  |  |
| --- | --- |
| Syntax | `:sort(<sorting key 1>,<sorting key 2>)` |
| Arguments | One or several sorting keys. |

The **sort** transformation specifies the order of tuples (unique combinations of metricâdimensionâdimension value) in the response. You can specify one or several sorting criteria. The first criterion is used for sorting. Further criteria are used for tie-breaking. You can choose the direction of the sort:

* `ascending`
* `descending`

You can also specify the type of sort:

* `lexical`
* `natural`

### Dimension sorting

To sort results by the value of a dimension, use the `dimension("<dimension>", <direction>)` or `dimension("<dimension>", <direction>, <type>)` key. Quotes (`"`) and tildes (`~`) that are part of the dimension key must be escaped with a tilde (`~`).

Entity dimensions are sorted lexicographically (`0..9a..z`) by Dynatrace entity ID values.

String dimensions are sorted lexicographically.

#### Sorting type

The sorting type defines how dimension values are ordered.

The `lexical` sorting type arranges dimension strings lexicographically (for example, `1,11,2,21,3`). This is the default sorting type when no type is explicitly specified, as in `dimension("<dimension>", ascending)`. You can also specify it explicitly using `dimension("<dimension>", <direction>, lexical)`.

The `natural` sorting type arranges dimension strings in a human-friendly, natural order (for example, `1,2,3,11,21`). It can be specified using `dimension("<dimension>", <direction>, natural)`.

### Data points sorting

To sort results by metric data points in a dimension, use the `value(<aggregation>,<direction>`) key.

The following aggregations are available:

* `avg`
* `count`
* `max`
* `median`
* `min`
* `sum`
* `percentile(N)`, with N in the `0` to `100` range.
* `value`

The aggregation is used only for sorting and doesn't affect the returned data points.

The sorting is applied to the resulting data points of the whole transformation chain before the **sort** transformation. If the transformation chain doesn't have an [**aggregation** transformation](#aggregation), the sorting is applied to the default aggregation of the metric.

Show example

Before sort transformation

After sort transformation

```
{



"totalCount": 4,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:apps.other.sessionCount.osAndGeo:names:splitBy(\"dt.entity.geolocation.name\")",



"data": [



{



"dimensions": ["Austria"],



"dimensionMap": {



"dt.entity.geolocation.name": "Austria"



},



"timestamps": [1613557980000],



"values": [6543]



},



{



"dimensions": ["Switzerland"],



"dimensionMap": {



"dt.entity.geolocation.name": "Switzerland"



},



"timestamps": [1613557980000],



"values": [1009]



},



{



"dimensions": ["Germany"],



"dimensionMap": {



"dt.entity.geolocation.name": "Germany"



},



"timestamps": [1613557980000],



"values": [6673]



},



{



"dimensions": ["Lichtenstein"],



"dimensionMap": {



"dt.entity.geolocation.name": "Lichtenstein"



},



"timestamps": [1613557980000],



"values": [86]



}



]



}



]



}
```

```
{



"totalCount": 4,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:apps.other.sessionCount.osAndGeo:names:splitBy(\"dt.entity.geolocation.name\"):sort(dimension(\"dt.entity.geolocation.name\",ascending))",



"data": [



{



"dimensions": ["Austria"],



"dimensionMap": {



"dt.entity.geolocation.name": "Austria"



},



"timestamps": [1613557440000],



"values": [6543]



},



{



"dimensions": ["Germany"],



"dimensionMap": {



"dt.entity.geolocation.name": "Germany"



},



"timestamps": [1613557440000],



"values": [6673]



},



{



"dimensions": ["Lichtenstein"],



"dimensionMap": {



"dt.entity.geolocation.name": "Lichtenstein"



},



"timestamps": [1613557980000],



"values": [86]



},



{



"dimensions": ["Switzerland"],



"dimensionMap": {



"dt.entity.geolocation.name": "Switzerland"



},



"timestamps": [1613557440000],



"values": [1009]



}



]



}



]



}
```

## Split by transformation

|  |  |
| --- | --- |
| Syntax | `:splitBy("<dimension0>","<dimension1>","<dimensionN>")` |
| Arguments | A list of [dimensions](#dimension) to be preserved in the result. A dimension must be specified by its key.  Quotes (`"`) and tildes (`~`) that are part of the dimension key must be escaped with a tilde (`~`). |

The **split by** transformation keeps the specified dimensions in the result and merges all remaining dimensions. The values are recalculated according to the selected aggregation. Only metric series that have each of the specified dimensions are considered.

You can apply any aggregation to the result of the **split by** transformation, including those that the original metric doesn't support.

Show example

Before split by transformation

After split by transformation

```
{



"totalCount": 4,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:apps.other.sessionCount.osAndGeo:names",



"data": [



{



"dimensions": [



"easyTravel Demo",



"MOBILE_APPLICATION-752C288D59734C79",



"Android",



"OS-472A4A3B41095B09",



"Switzerland",



"GEOLOCATION-976217DC7560B588"



],



"dimensionMap": {



"dt.entity.device_application.name": "easyTravel Demo",



"dt.entity.os": "OS-472A4A3B41095B09",



"dt.entity.os.name": "Android",



"dt.entity.device_application": "MOBILE_APPLICATION-752C288D59734C79",



"dt.entity.geolocation.name": "Switzerland",



"dt.entity.geolocation": "GEOLOCATION-976217DC7560B588"



},



"timestamps": [1612950360000],



"values": [557]



},



{



"dimensions": [



"easyTravel Demo",



"MOBILE_APPLICATION-752C288D59734C79",



"Android",



"OS-472A4A3B41095B09",



"Austria",



"GEOLOCATION-EADFE05E062C8D33"



],



"dimensionMap": {



"dt.entity.device_application.name": "easyTravel Demo",



"dt.entity.os": "OS-472A4A3B41095B09",



"dt.entity.os.name": "Android",



"dt.entity.device_application": "MOBILE_APPLICATION-752C288D59734C79",



"dt.entity.geolocation.name": "Austria",



"dt.entity.geolocation": "GEOLOCATION-EADFE05E062C8D33"



},



"timestamps": [1612950360000],



"values": [328]



},



{



"dimensions": [



"easyTravel Demo",



"MOBILE_APPLICATION-752C288D59734C79",



"iOS",



"OS-62028BEE737F03D4",



"Switzerland",



"GEOLOCATION-976217DC7560B588"



],



"dimensionMap": {



"dt.entity.device_application.name": "easyTravel Demo",



"dt.entity.os": "OS-62028BEE737F03D4",



"dt.entity.os.name": "iOS",



"dt.entity.device_application": "MOBILE_APPLICATION-752C288D59734C79",



"dt.entity.geolocation.name": "Switzerland",



"dt.entity.geolocation": "GEOLOCATION-976217DC7560B588"



},



"timestamps": [1612950360000],



"values": [383]



},



{



"dimensions": [



"easyTravel Demo",



"MOBILE_APPLICATION-752C288D59734C79",



"iOS",



"OS-62028BEE737F03D4",



"Austria",



"GEOLOCATION-EADFE05E062C8D33"



],



"dimensionMap": {



"dt.entity.device_application.name": "easyTravel Demo",



"dt.entity.os": "OS-62028BEE737F03D4",



"dt.entity.os.name": "iOS",



"dt.entity.device_application": "MOBILE_APPLICATION-752C288D59734C79",



"dt.entity.geolocation.name": "Austria",



"dt.entity.geolocation": "GEOLOCATION-EADFE05E062C8D33"



},



"timestamps": [1612950360000],



"values": [214]



}



]



}



]



}
```

```
{



"totalCount": 2,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:apps.other.sessionCount.osAndGeo:names:splitBy(\"dt.entity.geolocation.name\")",



"data": [



{



"dimensions": ["Austria"],



"dimensionMap": {



"dt.entity.geolocation.name": "Austria"



},



"timestamps": [1612950360000],



"values": [542]



},



{



"dimensions": ["Switzerland"],



"dimensionMap": {



"dt.entity.geolocation.name": "Switzerland"



},



"timestamps": [1612950360000],



"values": [940]



}



]



}



]



}
```

## Time shift transformation

Syntax

`:timeshift(5m)`

Argument

The period of the shift. The following values are supported:

`s`: seconds  
`m`: minutes  
`h`: hours  
`d`: days  
`w`: weeks

The **time shift** transformation shifts the timeframe specified by the **from** and **to** query parameters and maps the resulting data points to timestamps from the original timeframe. It can help you hand data from different time zones or put yesterday's and today's data on the same chart for visual comparison.

A positive argument shifts the timeframe into the future; a negative argument shifts the timeframe into the past. In either case, there's a limit of **5 years**.

You can use this transformation to handle data from different time zones.

Let's consider an example with a timeframe from `1615550400000` (March 12, 2021 13:00 CET) to `1615557600000` (March 12, 2021 15:00 CET) and a time shift of `-1d` (one day into the past).

1. The data points will be queried for the timeframe from `1615464000000` (March 11, 2021 13:00 CET) to `1615471200000` (March 11, 2021 15:00 CET).
2. Timestamps in the response will be aligned to the original timeframe. For example, the data point with a timestamp of `1615465800000` (March 11, 2021 13:30 CET) will be returned as `1615552200000` (March 12, 2021 13:30 CET).

## Unit transformations

### Set unit

|  |  |
| --- | --- |
| Syntax | `:setUnit(<unit>)` |
| Argument | The desired unit.  To fetch the list of available units, use the [GET all units](/docs/dynatrace-api/environment-api/metrics-units/get-all-units "List all metrics that are available for your monitoring environment via the Dynatrace API.") API call. |

The **setUnit** transformation sets the unit in the metric metadata.

This transformation **does not** affect data points.

### To unit

|  |  |
| --- | --- |
| Syntax | `:toUnit(<sourceUnit>,<targetUnit>)` |
| Arguments | The source and the target unit of the transformation.  To fetch the list of available units, use the [GET all units](/docs/dynatrace-api/environment-api/metrics-units/get-all-units "List all metrics that are available for your monitoring environment via the Dynatrace API.") API call. |

The **toUnit** transformation converts data points from the source unit to target unit. If specified units are incompatible, the original unit is persisted and a warning is included in the response.

You must apply an [aggregation transformation](#aggregation) before using the unit transformations.

## Related topics

* [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.")
* [Environment API v2 - Entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.")
* [[GitHub] Examples of metric selector queriesï»¿](https://dt-url.net/metric-selector-by-example)


---


## Source: post-ingest-metrics.md


---
title: Metrics API - POST ingest data points
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics
scraped: 2026-02-16T21:25:26.208055
---

# Metrics API - POST ingest data points

# Metrics API - POST ingest data points

* Reference
* Published Aug 21, 2020

Pushes custom data points to Dynatrace.

You can access the ingested datapoints via:

* [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.")
* [GET metric data points](/docs/dynatrace-api/environment-api/metric-v2/get-data-points "Read data points of one or multiple metrics via Metrics v2 API.") request of the Metric v2 API.

Provided data points must follow the [Metrics ingestion protocol](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Learn how the data ingestion protocol for Dynatrace Metrics API works."). You don't have to register the metric first. After Dynatrace has ingested and processed the data, you can use it just like any other metrics in Dynatrace, such as in [charts](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") or [metric events](/docs/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace"). You can also provide [metadata](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/custom-metric-metadata "Provide metadata for your custom metric.") for the ingested metric via the Settings API.

Prefer to ingest metrics right on the host?

You can also push the data points directly from a OneAgent-monitored host to the Extensions Execution Controller (EEC) OneAgent module over a secure channel using the local `http://localhost:<port>/metrics/ingest` endpoint, which doesn't require token authentication. The default port is `14499`. Using this method, the Dynatrace reserved `dt.entity.host=<host-ID>` dimension is added to each metric.

You can use the dimension `dt.process.id=<PID>` to add a process group identifier dimension. When the process group identifier is provided, `dt.entity.process_group_instance` dimension will be added to a given metric. It works on OneAgent metrics ingest only via [`dynatrace_ingest`](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-pipe "Learn how to ingest metrics using local scripting integration.") API.

For more information, see [OneAgent metric API](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Use the Dynatrace API to retrieve the metrics of monitored entities.").

You can't ingest metrics with key prefix of `dt.`âthese are reserved for usage by Dynatrace.

The request consumes a `text/plain` payload. The payload is limited to 1 MB.

There's no limit on the number of metrics.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/metrics/ingest` |
| POST | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/metrics/ingest` |

## Authentication

To execute this request, you need an access token with `metrics.ingest` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | string | Data points, provided in the [line protocolï»¿](https://dt-url.net/5d63ic1). Each line represents a single data point. | body | Required |

### Request body objects

#### The `RequestBody` object

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **202** | [ValidationResponse](#openapi-definition-ValidationResponse) | The provided metric data points are accepted and will be processed in the background. |
| **400** | [ValidationResponse](#openapi-definition-ValidationResponse) | Some data points are invalid. Valid data points are accepted and will be processed in the background. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ValidationResponse` object

| Element | Type | Description |
| --- | --- | --- |
| error | [MetricIngestError](#openapi-definition-MetricIngestError) | - |
| linesInvalid | integer | - |
| linesOk | integer | - |
| warnings | [Warnings](#openapi-definition-Warnings) | - |

#### The `MetricIngestError` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | - |
| invalidLines | [InvalidLine[]](#openapi-definition-InvalidLine) | - |
| message | string | - |

#### The `InvalidLine` object

| Element | Type | Description |
| --- | --- | --- |
| error | string | - |
| line | integer | - |

#### The `Warnings` object

| Element | Type | Description |
| --- | --- | --- |
| changedMetricKeys | [WarningLine[]](#openapi-definition-WarningLine) | - |
| message | string | - |

#### The `WarningLine` object

| Element | Type | Description |
| --- | --- | --- |
| line | integer | - |
| warning | string | - |

### Response body JSON models

```
{



"error": {



"code": 1,



"invalidLines": [



{



"error": "string",



"line": 1



}



],



"message": "string"



},



"linesInvalid": 1,



"linesOk": 1,



"warnings": {



"changedMetricKeys": [



{



"line": 1,



"warning": "string"



}



],



"message": "string"



}



}
```

## Example

With this `curl` command, you'll ingest the `cpu.temperature` metric assigned to the `HOST-06F288EE2A930951` dimension.

```
curl -L -X POST 'https://mySampleEnv.live.dynatrace.com/api/v2/metrics/ingest' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: text/plain' \



--data-raw 'cpu.temperature,dt.entity.host=HOST-06F288EE2A930951,cpu=1 55'
```

## Related topics

* [Metric ingestion protocol](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Learn how the data ingestion protocol for Dynatrace Metrics API works.")
* [Custom metric metadata](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/custom-metric-metadata "Provide metadata for your custom metric.")


---


## Source: metric-v2.md


---
title: Metrics API v2
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/metric-v2
scraped: 2026-02-16T21:23:21.291868
---

# Metrics API v2

# Metrics API v2

* Reference
* Updated on Jan 22, 2026

[### Get all

Get an overview of all metrics available in your environment.](/docs/dynatrace-api/environment-api/metric-v2/get-all-metrics "List all metrics available in your monitoring environment via Metrics v2 API.")[### Get description

Get the full descriptor of a metric.](/docs/dynatrace-api/environment-api/metric-v2/get-descriptor "View the descriptor of a metric via Metrics v2 API.")[### Read data points

Get data points from metrics you need.

For each metric you can get either one aggregated data point of a list of data points.](/docs/dynatrace-api/environment-api/metric-v2/get-data-points "Read data points of one or multiple metrics via Metrics v2 API.")

[### Select the data you need

The Metrics API is a flexible instrument for obtaining data. Learn how to use metric selector transformations to fine-tune the scope of data you're reading.](/docs/dynatrace-api/environment-api/metric-v2/metric-selector "Configure the metric selector for the Metric v2 API.")[### Modify data on read

In addition to transforming your metric, you can perform simple arithmetic operations right in your query. Learn how to use metric expressions to modify the data you're reading.](/docs/dynatrace-api/environment-api/metric-v2/metric-expressions "Use metric expressions to apply arithmetic operations in a data points query via the Metrics API v2.")

[### Ingest custom metrics

Push custom data points to Dynatrace.](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API.")[### Delete a metric

Delete a metric you no longer need.](/docs/dynatrace-api/environment-api/metric-v2/delete-metric "Delete a metric ingested via Metrics v2 API.")[### Delete metrics

Delete metrics older than the specified number of days.](/docs/dynatrace-api/environment-api/metric-v2/delete-metrics "Delete metrics ingested via Metrics v2 API.")

## Related topics

* [Built-in classic metrics](/docs/analyze-explore-automate/metrics-classic/built-in-metrics "Explore the complete list of built-in Dynatrace metrics.")
* [Extend metric observability](/docs/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.")
* [Metric units API](/docs/dynatrace-api/environment-api/metrics-units "Learn about units that Dynatrace metrics use via the Dynatrace API.")


---


## Source: get-unit-convert.md


---
title: Metric units API - GET convert units
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/metrics-units/get-unit-convert
scraped: 2026-02-15T09:08:30.666383
---

# Metric units API - GET convert units

# Metric units API - GET convert units

* Reference
* Published Mar 25, 2022

Converts a source unit into a target unit.

If no target unit is set, the request finds an appropriate target unit automatically, taking into account the preferred number format (if specified).

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/units/{unitId}/convert` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/units/{unitId}/convert` |

## Authentication

To execute this request, you need an access token with `metrics.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| unitId | string | The ID of the source unit. | path | Required |
| value | number | The value to be converted. | query | Required |
| targetUnit | string | The ID of the target unit.  If not set, the request finds an appropriate target unit automatically, based on the specified number format. | query | Optional |
| numberFormat | string | The preferred number format of the target value. You can specify the following formats:  * `binary` * `decimal`  `Only used if the target unit if not set. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [UnitConversionResult](#openapi-definition-UnitConversionResult) | Success |
| **404** | - | Not found. The requested resource is not found or the query is incorrect. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `UnitConversionResult` object

The result of a unit conversion.

| Element | Type | Description |
| --- | --- | --- |
| resultValue | number | The result of the unit conversion. |
| unitId | string | The ID of the unit of this conversion result. |

### Response body JSON models

```
{



"resultValue": 1,



"unitId": "string"



}
```


---


## Source: get-network-zone.md


---
title: Network zones API - GET a network zone
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/network-zones/get-network-zone
scraped: 2026-02-16T21:23:31.860273
---

# Network zones API - GET a network zone

# Network zones API - GET a network zone

* Reference
* Published Mar 05, 2020

Gets information about the specified network zone.

The request produces an `application/json` payload.

GET

* SaaS https://{your-environment-id}.live.dynatrace.com/api/v2/networkZones/{id}

## Authentication

To execute this request, you need the **Read network zones** (`networkZones.read`) permission assigned to your API token. To learn how to obtain and use it, see [Authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required network zone. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [NetworkZone](#openapi-definition-NetworkZone) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `NetworkZone` object

Configuration of a network zone.

| Element | Type | Description |
| --- | --- | --- |
| alternativeZones | string[] | A list of alternative network zones. |
| description | string | A short description of the network zone. |
| fallbackMode | string | The fallback mode of the network zone. The element can hold these values * `ANY_ACTIVE_GATE` * `NONE` * `ONLY_DEFAULT_ZONE` |
| id | string | The ID of the network zone. |
| numOfConfiguredActiveGates | integer | The number of ActiveGates in the network zone. |
| numOfConfiguredOneAgents | integer | The number of OneAgents that are configured to use the network zone as primary. |
| numOfOneAgentsFromOtherZones | integer | The number of OneAgents from other network zones that are using ActiveGates in the network zone.  This is a fraction ofÂ **numOfOneAgentsUsing**.  One possible reason for switching to another zone is that a firewall is preventing a OneAgent from connecting to any ActiveGate in the preferred network zone. |
| numOfOneAgentsUsing | integer | The number of OneAgents that are using ActiveGates in the network zone. |
| overridesGlobal | boolean | Indicates if a global network zone is overridden (managed only). |
| scope | string | Specifies the scope of the network zone (managed only). |

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



"alternativeZones": [



"string"



],



"description": "string",



"fallbackMode": "ANY_ACTIVE_GATE",



"id": "string",



"numOfConfiguredActiveGates": 1,



"numOfConfiguredOneAgents": 1,



"numOfOneAgentsFromOtherZones": 1,



"numOfOneAgentsUsing": 1,



"overridesGlobal": true,



"scope": "string"



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

* [Network zones](/docs/manage/network-zones "Find out how network zones work in Dynatrace.")


---


## Source: network-zones.md


---
title: Network zones API
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/network-zones
scraped: 2026-02-16T21:26:06.797305
---

# Network zones API

# Network zones API

* Reference
* Published Mar 05, 2020

[### List all network zones

Get an overview of all network zones available in your Dynatrace environment.](/docs/dynatrace-api/environment-api/network-zones/get-all "List all network zones of your monitoring environment via the Dynatrace API.")[### View a network zone

Get the numbers of OneAgents using the network zone by its ID.](/docs/dynatrace-api/environment-api/network-zones/get-network-zone "View the configuration of a network zone via the Dynatrace API.")

[### Edit a network zone

Update the existing configuration of a network zone.](/docs/dynatrace-api/environment-api/network-zones/put-network-zone "Update a network zone via the Dynatrace API.")[### Delete a network zone

Delete the network zone you no longer need.](/docs/dynatrace-api/environment-api/network-zones/del-network-zone "Delete a network zone via the Dynatrace API.")[### View configuration

Get an overview of the global network zones configuration.](/docs/dynatrace-api/environment-api/network-zones/get-global-config "Retrieve the global network zones configuration via the Dynatrace API.")[### Update configuration

Update the global configuration of network zones.](/docs/dynatrace-api/environment-api/network-zones/put-global-config "Edit the global network zones configuration via the Dynatrace API.")


---


## Source: get-all-hosts-with-oneagents.md


---
title: OneAgent on a host - GET a list of hosts with OneAgent details
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents
scraped: 2026-02-06T16:31:11.346773
---

# OneAgent on a host - GET a list of hosts with OneAgent details

# OneAgent on a host - GET a list of hosts with OneAgent details

* Reference
* Published Feb 03, 2020

The **OneAgent on a host** API enables you to check the configuration of OneAgent instances on your hosts.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/oneagents` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/oneagents` |

## Authentication

To execute this request, you need an access token with one of the following scopes:

* `oneAgents.read`
* `DataExport`

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| includeDetails | boolean | Includes (`true`) or excludes (`false`) details which are queried from related entities.  Excluding details may make queries faster.  If not set, then `true` is used. | query | Optional |
| startTimestamp | integer | The start timestamp of the requested timeframe, in milliseconds (UTC).  If not set, then 72 hours behind from now is used. | query | Optional |
| endTimestamp | integer | The end timestamp of the requested timeframe, in milliseconds (UTC).  If not set, then the current timestamp is used.  The timeframe must not exceed 7 months (214 days). | query | Optional |
| relativeTime | string | The relative timeframe, back from now.  If you need to specify relative timeframe that is not presented in the list of possible values, specify the **startTimestamp** (up to 214 days back from now) and leave **endTimestamp** and **relativeTime** empty. The element can hold these values * `10mins` * `15mins` * `2hours` * `30mins` * `3days` * `5mins` * `6hours` * `day` * `hour` * `min` * `month` * `week` | query | Optional |
| tag | string[] | Filters the resulting set of hosts by the specified tag. You can specify several tags in the following format: `tag=tag1&tag=tag2`. The host has to match **all** the specified tags.  In case of key-value tags, such as imported AWS or CloudFoundry tags, use the following format: `tag=[context]key:value`. For custom key-value tags, omit the context: `tag=key:value`. | query | Optional |
| entity | string[] | Filters result to the specified hosts only.  To specify several hosts use the following format: `entity=ID1&entity=ID2`. | query | Optional |
| managementZoneId | integer | Only return hosts that are part of the specified management zone.  Specify the management zone ID here. | query | Optional |
| managementZone | string | Only return hosts that are part of the specified management zone.  Specify the management zone name here.  If the **managementZoneId** parameter is set, this parameter is ignored. | query | Optional |
| networkZoneId | string | Filters the resulting set of hosts by the specified network zone.  Specify the Dynatrace entity ID of the required network zone. You can fetch the list of available network zones with the [GET all network zonesï»¿](https://dt-url.net/u4o3r7z) call. | query | Optional |
| hostGroupId | string | Filters the resulting set of hosts by the specified host group.  Specify the Dynatrace entity ID of the required host group. | query | Optional |
| hostGroupName | string | Filters the resulting set of hosts by the specified host group.  Specify the name of the required host group. | query | Optional |
| osType | string | Filters the resulting set of hosts by the OS type. The element can hold these values * `AIX` * `DARWIN` * `HPUX` * `LINUX` * `SOLARIS` * `WINDOWS` * `ZOS` | query | Optional |
| cloudType | string | Filters the resulting set of hosts by the cloud type. The element can hold these values * `AZURE` * `EC2` * `GOOGLE_CLOUD_PLATFORM` * `OPENSTACK` * `ORACLE` * `UNRECOGNIZED` | query | Optional |
| autoInjection | string | Filters the resulting set of hosts by the auto-injection status. The element can hold these values * `DISABLED_MANUALLY` * `DISABLED_ON_INSTALLATION` * `DISABLED_ON_SANITY_CHECK` * `ENABLED` * `FAILED_ON_INSTALLATION` | query | Optional |
| availabilityState | string | Filters the resulting set of hosts by the availability state of OneAgent.  * `MONITORED`: Hosts where OneAgent is enabled and active. * `UNMONITORED`: Hosts where OneAgent is disabled and inactive. * `CRASHED`: Hosts where OneAgent has returned a crash status code. * `LOST`: Hosts where it is impossible to establish connection with OneAgent. * `PRE_MONITORED`: Hosts where OneAgent is being initialized for monitoring. * `SHUTDOWN`: Hosts where OneAgent is shutting down in a controlled process. * `UNEXPECTED_SHUTDOWN`: Hosts where OneAgent is shutting down in an uncontrolled process. * `UNKNOWN`: Hosts where the state of OneAgent is unknown. The element can hold these values * `CRASHED` * `LOST` * `MONITORED` * `PRE_MONITORED` * `SHUTDOWN` * `UNEXPECTED_SHUTDOWN` * `UNKNOWN` * `UNMONITORED` | query | Optional |
| detailedAvailabilityState | string | Filters the resulting set of hosts by the detailed availability state of OneAgent.  * `UNKNOWN`: Hosts where the state of OneAgent is unknown. * `PRE_MONITORED`: Hosts where OneAgent is being initialized for monitoring. * `CRASHED_UNKNOWN`: Hosts where OneAgent has crashed for unknown reason. * `CRASHED_FAILURE`: Hosts where OneAgent has returned a crash status code. * `LOST_UNKNOWN`: Hosts where it is impossible to establish connection with OneAgent for unknown reason. * `LOST_CONNECTION`: Hosts where OneAgent has been recognized to be inactive. * `LOST_AGENT_UPGRADE_FAILED`: Hosts where OneAgent has a potential update problem due to inactivity after update. * `SHUTDOWN_UNKNOWN_UNEXPECTED`: Hosts where OneAgent is shutting down in an uncontrolled process. * `SHUTDOWN_UNKNOWN`: Hosts where OneAgent has shutdown for unknown reason. * `SHUTDOWN_GRACEFUL`: Hosts where OneAgent has shutdown because of host shutdown. * `SHUTDOWN_STOPPED`: Hosts where OneAgent has shutdown because the host has stopped. * `SHUTDOWN_AGENT_LOST`: Hosts where PaaS module has been recognized to be inactive. * `SHUTDOWN_SPOT_INSTANCE`: Hosts where OneAgent shutdown was triggered by the AWS Spot Instance interruption. * `SHUTDOWN_K8S_NODE_SHUTDOWN`: Hosts where OneAgent shutdown was triggered by a k8s node graceful shutdown. * `UNMONITORED_UNKNOWN`: Hosts where OneAgent is disabled and inactive for unknown reason. * `UNMONITORED_TERMINATED`: Hosts where OneAgent has terminated. * `UNMONITORED_DISABLED`: Hosts where OneAgent has been disabled in configuration. * `UNMONITORED_AGENT_STOPPED`: Hosts where OneAgent is stopped. * `UNMONITORED_AGENT_RESTART_TRIGGERED`: Hosts where OneAgent is being restarted. * `UNMONITORED_AGENT_UNINSTALLED`: Hosts where OneAgent is uninstalled. * `UNMONITORED_AGENT_DISABLED`: Hosts where OneAgent reported that it was disabled. * `UNMONITORED_AGENT_UPGRADE_FAILED`: Hosts where OneAgent has a potential update problem. * `UNMONITORED_ID_CHANGED`: Hosts where OneAgent has potentially changed ID during update. * `UNMONITORED_AGENT_LOST`: Hosts where OneAgent has been recognized to be unavailable due to server communication issues. * `UNMONITORED_AGENT_UNREGISTERED`: Hosts where a code module has been recognized to be unavailable because of shutdown. * `UNMONITORED_AGENT_VERSION_REJECTED`: Hosts where OneAgent was rejected because the version does not meet the minimum agent version requirement. * `UNMONITORED_AGENT_MIGRATED`: Hosts where OneAgent was migrated to another environment. * `MONITORED`: Hosts where OneAgent is enabled and active. * `MONITORED_ENABLED`: Hosts where OneAgent has been enabled in configuration. * `MONITORED_AGENT_REGISTERED`: Hosts where the new OneAgent has been recognized. * `MONITORED_AGENT_UPGRADE_STARTED`: Hosts where OneAgent has shutdown due to an update. * `MONITORED_AGENT_ENABLED`: Hosts where OneAgent reported that it was enabled. * `MONITORED_AGENT_VERSION_ACCEPTED`: Hosts where OneAgent was accepted because the version meets the minimum agent version requirement. The element can hold these values * `CRASHED_FAILURE` * `CRASHED_UNKNOWN` * `LOST_AGENT_UPGRADE_FAILED` * `LOST_CONNECTION` * `LOST_UNKNOWN` * `MONITORED` * `MONITORED_AGENT_ENABLED` * `MONITORED_AGENT_REGISTERED` * `MONITORED_AGENT_UPGRADE_STARTED` * `MONITORED_AGENT_VERSION_ACCEPTED` * `MONITORED_ENABLED` * `PRE_MONITORED` * `SHUTDOWN_AGENT_LOST` * `SHUTDOWN_GRACEFUL` * `SHUTDOWN_K8S_NODE_SHUTDOWN` * `SHUTDOWN_SPOT_INSTANCE` * `SHUTDOWN_STOPPED` * `SHUTDOWN_UNKNOWN` * `SHUTDOWN_UNKNOWN_UNEXPECTED` * `UNKNOWN` * `UNMONITORED_AGENT_DISABLED` * `UNMONITORED_AGENT_LOST` * `UNMONITORED_AGENT_MIGRATED` * `UNMONITORED_AGENT_RESTART_TRIGGERED` * `UNMONITORED_AGENT_STOPPED` * `UNMONITORED_AGENT_UNINSTALLED` * `UNMONITORED_AGENT_UNREGISTERED` * `UNMONITORED_AGENT_UPGRADE_FAILED` * `UNMONITORED_AGENT_VERSION_REJECTED` * `UNMONITORED_DISABLED` * `UNMONITORED_ID_CHANGED` * `UNMONITORED_TERMINATED` * `UNMONITORED_UNKNOWN` | query | Optional |
| monitoringType | string | Filters the resulting set of hosts by monitoring mode of OneAgent deployed on the host. The element can hold these values * `CLOUD_INFRASTRUCTURE` * `DISCOVERY` * `FULL_STACK` * `STANDALONE` | query | Optional |
| agentVersionIs | string | Filters the resulting set of hosts to those that have a certain OneAgent version deployed on the host.  Specify the comparison operator here. The element can hold these values * `EQUAL` * `GREATER` * `GREATER_EQUAL` * `LOWER` * `LOWER_EQUAL` | query | Optional |
| agentVersionNumber | string | Filters the resulting set of hosts to those that have a certain OneAgent version deployed on the host.  Specify the version in the `<major>.<minor>.<revision>` format, for example `1.182.0`. You can fetch the list of available versions with the [GET available versionsï»¿](https://dt-url.net/fo23rb5) call. | query | Optional |
| autoUpdateSetting | string | Filters the resulting set of hosts by the actual state of the auto-update setting of deployed OneAgents. The element can hold these values * `ENABLED` * `DISABLED` | query | Optional |
| updateStatus | string | Filters the resulting set of hosts by the update status of OneAgent deployed on the host. The element can hold these values * `INCOMPATIBLE` * `OUTDATED` * `SCHEDULED` * `SUPPRESSED` * `UNKNOWN` * `UP2DATE` * `UPDATE_IN_PROGRESS` * `UPDATE_PENDING` * `UPDATE_PROBLEM` | query | Optional |
| faultyVersion | boolean | Filters the resulting set of hosts to those that run OneAgent version that is marked as faulty. | query | Optional |
| unlicensed | boolean | Filters the resulting set of hosts to those that run OneAgent that are unlicensed.  Example: Your Dynatrace license is missing the required "Foundation & Discovery" DPS capability for Discovery mode. | query | Optional |
| activeGateId | string | Filters the resulting set of hosts to those that are currently connected to the ActiveGate with the specified ID.  Use **DIRECT\_COMMUNICATION** keyword to find the hosts not connected to any ActiveGate. | query | Optional |
| technologyModuleType | string | Filters the resulting set of hosts to those that run the specified OneAgent code module.  If several code module filters are specified, the code module has to match **all** the filters. The element can hold these values * `APACHE` * `DOT_NET` * `DUMPPROC` * `GO` * `IBM_INTEGRATION_BUS` * `IIS` * `JAVA` * `LOG_ANALYTICS` * `NETTRACER` * `NETWORK` * `NGINX` * `NODE_JS` * `OPENTRACINGNATIVE` * `PHP` * `PROCESS` * `PYTHON` * `RUBY` * `SDK` * `UPDATER` * `VARNISH` * `Z_OS` | query | Optional |
| technologyModuleVersionIs | string | Filters the resulting set of hosts to those that have a certain code module version deployed on the host.  Specify the comparison operator here.  If several code module filters are specified, the code module has to match **all** the filters. The element can hold these values * `EQUAL` * `GREATER` * `GREATER_EQUAL` * `LOWER` * `LOWER_EQUAL` | query | Optional |
| technologyModuleVersionNumber | string | Filters the resulting set of hosts to those that have a certain code module version deployed on the host.  Specify the version in the `<major>.<minor>.<revision>` format, for example `1.182.0`. You can fetch the list of available versions with the [GET available versionsï»¿](https://dt-url.net/fo23rb5) call.  If several code module filters are specified, the code module has to match **all** the filters. | query | Optional |
| technologyModuleFaultyVersion | boolean | Filters the resulting set of hosts to those that run the code module version that is marked as faulty.  If several code module filters are specified, the code module has to match **all** the filters. | query | Optional |
| pluginName | string | Filters the resulting set of hosts to those that run the plugin with the specified name.  The **CONTAINS** operator is applied to the specified value.  If several plugin filters are specified, the plugin has to match **all** the filters. | query | Optional |
| pluginVersionIs | string | Filters the resulting set of hosts to those that have a certain plugin version deployed on the host.  Specify the comparison operator here.  If several plugin filters are specified, the plugin has to match **all** the filters. The element can hold these values * `EQUAL` * `GREATER` * `GREATER_EQUAL` * `LOWER` * `LOWER_EQUAL` | query | Optional |
| pluginVersionNumber | string | Filters the resulting set of hosts to those that have a certain plugin version deployed on the host.  Specify the version in the `<major>.<minor>.<revision>` format, for example `1.182.0`. You can fetch the list of available versions with the [GET available versionsï»¿](https://dt-url.net/fo23rb5) call.  `<minor>` and `<revision>` parts of the version number are optional.  If several plugin filters are specified, the plugin has to match **all** the filters. | query | Optional |
| pluginState | string | Filters the resulting set of hosts to those that run the plugin with the specified state. The element can hold these values * `DISABLED` * `ERROR_AUTH` * `ERROR_COMMUNICATION_FAILURE` * `ERROR_CONFIG` * `ERROR_TIMEOUT` * `ERROR_UNKNOWN` * `INCOMPATIBLE` * `LIMIT_REACHED` * `NOTHING_TO_REPORT` * `OK` * `STATE_TYPE_UNKNOWN` * `UNINITIALIZED` * `UNSUPPORTED` * `WAITING_FOR_STATE` | query | Optional |
| nextPageKey | string | The cursor for the next page of results, if results do not fit on one page. You can find the cursor value on the current page of the response, in the **nextPageKey** field.  To obtain subsequent pages, you must specify this cursor value in your query, and keep all other query parameters as they were in the original request.  If you don't specify the cursor, the first page will always be returned. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [HostsListPage](#openapi-definition-HostsListPage) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `HostsListPage` object

A list of hosts with OneAgent deployment information for each host.

| Element | Type | Description |
| --- | --- | --- |
| hosts | [HostAgentInfo[]](#openapi-definition-HostAgentInfo) | A list of hosts with OneAgent deployment information for each host. |
| nextPageKey | string | The cursor for the next page of results.  Has the value of `null` on the last page.  There might be another page of results even if the current page is empty. |
| percentageOfEnvironmentSearched | number | The progress of the environment search, in percent. |

#### The `HostAgentInfo` object

OneAgent deployment on a host.

| Element | Type | Description |
| --- | --- | --- |
| active | boolean | OneAgent is active (`true`) or inactive (`false`). |
| autoUpdateSetting | string | The effective auto-update setting of OneAgent. For host with inherited configuration it is calculated from its parent's configuration The element can hold these values * `ENABLED` * `DISABLED` |
| availabilityState | string | The availability state of OneAgent. The element can hold these values * `CRASHED` * `LOST` * `MONITORED` * `PRE_MONITORED` * `SHUTDOWN` * `UNEXPECTED_SHUTDOWN` * `UNKNOWN` * `UNMONITORED` |
| availableVersions | string[] | A list of versions OneAgent can be updated to. |
| configuredMonitoringEnabled | boolean | Monitoring is enabled (`true`) or disabled (`false`) in the OneAgent configuration. |
| configuredMonitoringMode | string | Configured monitoring mode of OneAgent. The element can hold these values * `CLOUD_INFRASTRUCTURE` * `DISCOVERY` * `FULL_STACK` |
| ~~currentActiveGateId~~ | integer | DEPRECATED  This field is deprecated and provided for backward compatibility.  Use the **currentActiveGateIds** field instead. |
| currentActiveGateIds | string[] | The list of ActiveGate IDs of ActiveGates to which OneAgent is currently connected. |
| currentNetworkZoneId | string | The ID of the network zone that OneAgent is using. |
| detailedAvailabilityState | string | The detailed availability state of OneAgent. The element can hold these values * `CRASHED_FAILURE` * `CRASHED_UNKNOWN` * `LOST_AGENT_UPGRADE_FAILED` * `LOST_CONNECTION` * `LOST_UNKNOWN` * `MONITORED` * `MONITORED_AGENT_ENABLED` * `MONITORED_AGENT_REGISTERED` * `MONITORED_AGENT_UPGRADE_STARTED` * `MONITORED_AGENT_VERSION_ACCEPTED` * `MONITORED_ENABLED` * `PRE_MONITORED` * `SHUTDOWN_AGENT_LOST` * `SHUTDOWN_GRACEFUL` * `SHUTDOWN_K8S_NODE_SHUTDOWN` * `SHUTDOWN_SPOT_INSTANCE` * `SHUTDOWN_STOPPED` * `SHUTDOWN_UNKNOWN` * `SHUTDOWN_UNKNOWN_UNEXPECTED` * `UNKNOWN` * `UNMONITORED_AGENT_DISABLED` * `UNMONITORED_AGENT_LOST` * `UNMONITORED_AGENT_MIGRATED` * `UNMONITORED_AGENT_RESTART_TRIGGERED` * `UNMONITORED_AGENT_STOPPED` * `UNMONITORED_AGENT_UNINSTALLED` * `UNMONITORED_AGENT_UNREGISTERED` * `UNMONITORED_AGENT_UPGRADE_FAILED` * `UNMONITORED_AGENT_VERSION_REJECTED` * `UNMONITORED_DISABLED` * `UNMONITORED_ID_CHANGED` * `UNMONITORED_TERMINATED` * `UNMONITORED_UNKNOWN` |
| faultyVersion | boolean | OneAgent version is faulty (`true`) or not (`false`). |
| hostInfo | [Host](#openapi-definition-Host) | Information about the host. |
| modules | [ModuleInfo[]](#openapi-definition-ModuleInfo) | A list of code modules deployed on the host. |
| monitoringType | string | The monitoring mode of OneAgent. The element can hold these values * `CLOUD_INFRASTRUCTURE` * `DISCOVERY` * `FULL_STACK` * `STANDALONE` |
| plugins | [PluginInfo[]](#openapi-definition-PluginInfo) | A list of plugins deployed on the host. |
| unlicensed | boolean | OneAgent is unlicensed. |
| updateStatus | string | The current update status of OneAgent. The element can hold these values * `INCOMPATIBLE` * `OUTDATED` * `SCHEDULED` * `SUPPRESSED` * `UNKNOWN` * `UP2DATE` * `UPDATE_IN_PROGRESS` * `UPDATE_PENDING` * `UPDATE_PROBLEM` |

#### The `Host` object

Information about the host.

| Element | Type | Description |
| --- | --- | --- |
| agentVersion | [AgentVersion](#openapi-definition-AgentVersion) | Defines the version of the agent currently running on the entity. |
| amiId | string | - |
| autoInjection | string | Status of auto-injection The element can hold these values * `DISABLED_MANUALLY` * `DISABLED_ON_INSTALLATION` * `DISABLED_ON_SANITY_CHECK` * `ENABLED` * `FAILED_ON_INSTALLATION` |
| autoScalingGroup | string | - |
| awsInstanceId | string | - |
| awsInstanceType | string | - |
| awsNameTag | string | The name inherited from AWS. |
| awsSecurityGroup | string[] | - |
| azureComputeModeName | string | -The element can hold these values * `DEDICATED` * `SHARED` |
| azureEnvironment | string | - |
| azureHostNames | string[] | - |
| azureResourceGroupName | string | - |
| azureResourceId | string | - |
| azureSiteNames | string[] | - |
| azureSku | string | -The element can hold these values * `BASIC` * `DYNAMIC` * `FREE` * `PREMIUM` * `SHARED` * `STANDARD` |
| azureVmName | string | - |
| azureVmScaleSetName | string | - |
| azureVmSizeLabel | string | - |
| azureZone | string | - |
| beanstalkEnvironmentName | string | - |
| bitness | string | -The element can hold these values * `32bit` * `64bit` |
| boshAvailabilityZone | string | The Cloud Foundry BOSH availability zone. |
| boshDeploymentId | string | The Cloud Foundry BOSH deployment ID. |
| boshInstanceId | string | The Cloud Foundry BOSH instance ID. |
| boshInstanceName | string | The Cloud Foundry BOSH instance name. |
| boshName | string | The Cloud Foundry BOSH name. |
| boshStemcellVersion | string | The Cloud Foundry BOSH stemcell version. |
| cloudPlatformVendorVersion | string | Defines the cloud platform vendor version. |
| cloudType | string | -The element can hold these values * `AZURE` * `EC2` * `GOOGLE_CLOUD_PLATFORM` * `OPENSTACK` * `ORACLE` * `UNRECOGNIZED` |
| consumedHostUnits | string | Consumed Host Units. Applicable only for [Dynatrace classic licensingï»¿](https://www.dynatrace.com/support/help/shortlink/application-and-infrastructure-host-units) |
| cpuCores | integer | - |
| customizedName | string | The customized name of the entity |
| discoveredName | string | The discovered name of the entity |
| displayName | string | The name of the Dynatrace entity as displayed in the UI. |
| entityId | string | The Dynatrace entity ID of the required entity. |
| esxiHostName | string | - |
| firstSeenTimestamp | integer | The timestamp of when the entity was first detected, in UTC milliseconds |
| fromRelationships | object | - |
| gceInstanceId | string | The Google Compute Engine instance ID. |
| gceInstanceName | string | The Google Compute Engine instance name. |
| gceMachineType | string | The Google Compute Engine machine type. |
| gceProject | string | The Google Compute Engine project. |
| gceProjectId | string | The Google Compute Engine numeric project ID. |
| gcePublicIpAddresses | string[] | The public IP addresses of the Google Compute Engine. |
| gcpZone | string | The Google Cloud Platform Zone. |
| hostGroup | [HostGroup](#openapi-definition-HostGroup) | - |
| hypervisorType | string | -The element can hold these values * `AHV` * `AWS_NITRO` * `GVISOR` * `HYPERV` * `KVM` * `LPAR` * `QEMU` * `UNRECOGNIZED` * `VIRTUALBOX` * `VMWARE` * `WPAR` * `XEN` |
| ipAddresses | string[] | - |
| isMonitoringCandidate | boolean | - |
| kubernetesCluster | string | The kubernetes cluster the entity is in. |
| kubernetesLabels | object | The kubernetes labels defined on the entity. |
| kubernetesNode | string | The kubernetes node the entity is in. |
| lastSeenTimestamp | integer | The timestamp of when the entity was last detected, in UTC milliseconds |
| localHostName | string | - |
| localIp | string | - |
| logicalCpuCores | integer | - |
| logicalCpus | integer | The AIX instance logical CPU count. |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | The management zones that the entity is part of. |
| monitoringMode | string | -The element can hold these values * `FULL_STACK` * `INFRASTRUCTURE` * `OFF` |
| networkZoneId | string | The ID of network zone the entity is in. |
| oneAgentCustomHostName | string | The custom name defined in OneAgent config. |
| openStackInstaceType | string | - |
| openstackAvZone | string | - |
| openstackComputeNodeName | string | - |
| openstackProjectName | string | - |
| openstackSecurityGroups | string[] | - |
| openstackVmName | string | - |
| osArchitecture | string | -The element can hold these values * `ARM` * `IA64` * `PARISC` * `PPC` * `PPCLE` * `S390` * `SPARC` * `X86` * `ZOS` |
| osType | string | -The element can hold these values * `AIX` * `DARWIN` * `HPUX` * `LINUX` * `SOLARIS` * `WINDOWS` * `ZOS` |
| osVersion | string | - |
| paasAgentVersions | [AgentVersion[]](#openapi-definition-AgentVersion) | The versions of the PaaS agents currently running on the entity. |
| paasMemoryLimit | integer | - |
| paasType | string | -The element can hold these values * `AWS_ECS_EC2` * `AWS_ECS_FARGATE` * `AWS_LAMBDA` * `AZURE_FUNCTIONS` * `AZURE_WEBSITES` * `CLOUD_FOUNDRY` * `GOOGLE_APP_ENGINE` * `GOOGLE_CLOUD_RUN` * `HEROKU` * `KUBERNETES` * `OPENSHIFT` |
| publicHostName | string | - |
| publicIp | string | - |
| scaleSetName | string | - |
| simultaneousMultithreading | integer | The AIX instance simultaneous threads count. |
| softwareTechnologies | [TechnologyInfo[]](#openapi-definition-TechnologyInfo) | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | The list of entity tags. |
| toRelationships | object | - |
| userLevel | string | -The element can hold these values * `NON_SUPERUSER` * `NON_SUPERUSER_STRICT` * `SUPERUSER` |
| virtualCpus | integer | The AIX instance virtual CPU count. |
| vmwareName | string | - |
| zosCPUModelNumber | string | The CPU model number. |
| zosCPUSerialNumber | string | The CPU serial number. |
| zosLpaName | string | Name of the LPAR. |
| zosSystemName | string | Name of the system. |
| zosTotalGeneralPurposeProcessors | integer | Number of assigned processors for this LPAR. |
| zosTotalPhysicalMemory | integer | Memory assigned to the host (Terabyte). |
| zosTotalZiipProcessors | integer | Number of assigned support processors for this LPAR. |
| zosVirtualization | string | Type of virtualization on the mainframe. |

#### The `AgentVersion` object

Defines the version of the agent currently running on the entity.

| Element | Type | Description |
| --- | --- | --- |
| major | integer | The major version number. |
| minor | integer | The minor version number. |
| revision | integer | The revision number. |
| sourceRevision | string | A string representation of the SVN revision number. |
| timestamp | string | A timestamp string: format "yyyymmdd-hhmmss |

#### The `HostGroup` object

| Element | Type | Description |
| --- | --- | --- |
| meId | string | The Dynatrace entity ID of the host group. |
| name | string | The name of the Dynatrace entity, displayed in the UI. |

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

#### The `TechnologyInfo` object

| Element | Type | Description |
| --- | --- | --- |
| edition | string | - |
| type | string | - |
| version | string | - |

#### The `TagInfo` object

Tag of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. The element can hold these values * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | The key of the tag.  Custom tags have the tag value here. |
| value | string | The value of the tag.  Not applicable to custom tags. |

#### The `ModuleInfo` object

OneAgent code module.

| Element | Type | Description |
| --- | --- | --- |
| instances | [ModuleInstance[]](#openapi-definition-ModuleInstance) | A list of instances of the code module. |
| moduleType | string | The type of the code module. The element can hold these values * `APACHE` * `DOT_NET` * `DUMPPROC` * `GO` * `IBM_INTEGRATION_BUS` * `IIS` * `JAVA` * `LOG_ANALYTICS` * `NETTRACER` * `NETWORK` * `NGINX` * `NODE_JS` * `OPENTRACINGNATIVE` * `PHP` * `PROCESS` * `PYTHON` * `RUBY` * `SDK` * `UPDATER` * `VARNISH` * `Z_OS` |

#### The `ModuleInstance` object

An instance of the OneAgent code module.

| Element | Type | Description |
| --- | --- | --- |
| active | boolean | The code module instance is active (`true`) or inactive (`false`). |
| faultyVersion | boolean | The code module version is faulty (`true`) or not (`false`). |
| instanceName | string | The name of the instance. |
| moduleVersion | string | The version of the code module. |

#### The `PluginInfo` object

OneAgent plugin.

| Element | Type | Description |
| --- | --- | --- |
| instances | [PluginInstance[]](#openapi-definition-PluginInstance) | A list of instances of the plugin. |
| pluginName | string | The name of the plugin. |

#### The `PluginInstance` object

An instance of the OneAgent plugin.

| Element | Type | Description |
| --- | --- | --- |
| pluginVersion | string | The version of the plugin. |
| state | string | The state of the plugin instance. |

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



"hosts": [



{



"active": true,



"autoUpdateSetting": "ENABLED",



"availabilityState": "CRASHED",



"availableVersions": [



"string"



],



"configuredMonitoringEnabled": true,



"configuredMonitoringMode": "CLOUD_INFRASTRUCTURE",



"currentActiveGateId": 1,



"currentActiveGateIds": [



"string"



],



"currentNetworkZoneId": "string",



"detailedAvailabilityState": "CRASHED_FAILURE",



"faultyVersion": true,



"hostInfo": {



"agentVersion": {



"major": 1,



"minor": 1,



"revision": 1,



"sourceRevision": "string",



"timestamp": "string"



},



"amiId": "string",



"autoInjection": "DISABLED_MANUALLY",



"autoScalingGroup": "string",



"awsInstanceId": "string",



"awsInstanceType": "string",



"awsNameTag": "string",



"awsSecurityGroup": [



"string"



],



"azureComputeModeName": "DEDICATED",



"azureEnvironment": "string",



"azureHostNames": [



"string"



],



"azureResourceGroupName": "string",



"azureResourceId": "string",



"azureSiteNames": [



"string"



],



"azureSku": "BASIC",



"azureVmName": "string",



"azureVmScaleSetName": "string",



"azureVmSizeLabel": "string",



"azureZone": "string",



"beanstalkEnvironmentName": "string",



"bitness": "32bit",



"boshAvailabilityZone": "string",



"boshDeploymentId": "string",



"boshInstanceId": "string",



"boshInstanceName": "string",



"boshName": "string",



"boshStemcellVersion": "string",



"cloudPlatformVendorVersion": "string",



"cloudType": "AZURE",



"consumedHostUnits": "string",



"cpuCores": 1,



"customizedName": "string",



"discoveredName": "string",



"displayName": "string",



"entityId": "string",



"esxiHostName": "string",



"firstSeenTimestamp": 1,



"fromRelationships": {



"isNetworkClientOfHost": [



"string"



]



},



"gceInstanceId": "string",



"gceInstanceName": "string",



"gceMachineType": "string",



"gceProject": "string",



"gceProjectId": "string",



"gcePublicIpAddresses": [



"string"



],



"gcpZone": "string",



"hostGroup": {



"meId": "string",



"name": "string"



},



"hypervisorType": "AHV",



"ipAddresses": [



"string"



],



"isMonitoringCandidate": true,



"kubernetesCluster": "string",



"kubernetesLabels": {},



"kubernetesNode": "string",



"lastSeenTimestamp": 1,



"localHostName": "string",



"localIp": "string",



"logicalCpuCores": 1,



"logicalCpus": 1,



"managementZones": [



{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}



],



"monitoringMode": "FULL_STACK",



"networkZoneId": "string",



"oneAgentCustomHostName": "string",



"openStackInstaceType": "string",



"openstackAvZone": "string",



"openstackComputeNodeName": "string",



"openstackProjectName": "string",



"openstackSecurityGroups": [



"string"



],



"openstackVmName": "string",



"osArchitecture": "ARM",



"osType": "AIX",



"osVersion": "string",



"paasAgentVersions": [



{}



],



"paasMemoryLimit": 1,



"paasType": "AWS_ECS_EC2",



"publicHostName": "string",



"publicIp": "string",



"scaleSetName": "string",



"simultaneousMultithreading": 1,



"softwareTechnologies": [



{



"edition": "string",



"type": "string",



"version": "string"



}



],



"tags": [



{



"context": "AWS",



"key": "string",



"value": "string"



}



],



"toRelationships": {



"isNetworkClientOfHost": [



"string"



],



"isProcessOf": [



"string"



],



"isSiteOf": [



"string"



],



"runsOn": [



"string"



]



},



"userLevel": "NON_SUPERUSER",



"virtualCpus": 1,



"vmwareName": "string",



"zosCPUModelNumber": "string",



"zosCPUSerialNumber": "string",



"zosLpaName": "string",



"zosSystemName": "string",



"zosTotalGeneralPurposeProcessors": 1,



"zosTotalPhysicalMemory": 1,



"zosTotalZiipProcessors": 1,



"zosVirtualization": "string"



},



"modules": [



{



"instances": [



{



"active": true,



"faultyVersion": true,



"instanceName": "string",



"moduleVersion": "string"



}



],



"moduleType": "APACHE"



}



],



"monitoringType": "CLOUD_INFRASTRUCTURE",



"plugins": [



{



"instances": [



{



"pluginVersion": "string",



"state": "string"



}



],



"pluginName": "string"



}



],



"unlicensed": true,



"updateStatus": "INCOMPATIBLE"



}



],



"nextPageKey": "string",



"percentageOfEnvironmentSearched": 1



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

* [OneAgent configuration on a host API](/docs/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host "Manage the configuration of OneAgent instances on your hosts via the Dynatrace API.")


---


## Source: problems-v2.md


---
title: Problems API v2
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/problems-v2
scraped: 2026-02-16T21:31:14.554543
---

# Problems API v2

# Problems API v2

* Reference
* Published Oct 12, 2020

[### Fetch the list of problems

Gain high-level overview of problems.](/docs/dynatrace-api/environment-api/problems-v2/problems/get-problems-list "Fetch the list of problems via Problems v2 API.")[### Get the problem details

When you find a problem you want to investigate, fetch details about it.](/docs/dynatrace-api/environment-api/problems-v2/problems/get-problem-details "View details of a problem via Problems v2 API.")[### Close problem

When a problem is not a concern anymore, close it.](/docs/dynatrace-api/environment-api/problems-v2/problems/post-close "Close a problem via Problems v2 API.")

[### List comments

View all comments on a problem.](/docs/dynatrace-api/environment-api/problems-v2/comments/get-all "View all comments to a problem via Problems v2 API.")[### View a comment

Check a particular comment on a specified problem.](/docs/dynatrace-api/environment-api/problems-v2/comments/get-comment "View a comment to a problem via Problems v2 API.")

[### Post comment

Post a comment on a specified problem.](/docs/dynatrace-api/environment-api/problems-v2/comments/post-comment "Post a comment to a problem via Problems v2 API.")[### Edit comment

Edit a comment on a specified problem.](/docs/dynatrace-api/environment-api/problems-v2/comments/put-comment "Edit a comment to a problem via Problems v2 API.")[### Delete comment

Delete a comment from a specified problem.](/docs/dynatrace-api/environment-api/problems-v2/comments/del-comment "Delete a comment to a problem via Problems v2 API.")

## Related topics

* [Dynatrace Intelligence](/docs/dynatrace-intelligence "Get familiar with the capabilities of Dynatrace Intelligence.")


---


## Source: remote-configuration.md


---
title: Remote configuration management API
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/remote-configuration
scraped: 2026-02-16T09:29:11.273866
---

# Remote configuration management API

# Remote configuration management API

* Reference
* Published Oct 06, 2022

### OneAgent

[Start a job](/docs/dynatrace-api/environment-api/remote-configuration/oneagent/post-config-job "Start a new configuration job for OneAgents remotely using the Dynatrace API.")

[Preview a job](/docs/dynatrace-api/environment-api/remote-configuration/oneagent/post-job-preview "Preview a configuration job for OneAgents using the Dynatrace API.")

[View current job](/docs/dynatrace-api/environment-api/remote-configuration/oneagent/get-current-job "View parameters of a current configuration job for OneAgents using the Dynatrace API.")

[List completed jobs](/docs/dynatrace-api/environment-api/remote-configuration/oneagent/get-finished-jobs "Get an overview of completed configuration jobs for OneAgents using the Dynatrace API.")

[View a job](/docs/dynatrace-api/environment-api/remote-configuration/oneagent/get-job "View parameters of a configuration job for OneAgents using the Dynatrace API.")

### ActiveGate

[Start a job](/docs/dynatrace-api/environment-api/remote-configuration/activegate/post-config-job "Start a new configuration job for ActiveGates remotely using the Dynatrace API.")

[Preview a job](/docs/dynatrace-api/environment-api/remote-configuration/activegate/post-job-preview "Preview a configuration job for ActiveGates using the Dynatrace API.")

[View current job](/docs/dynatrace-api/environment-api/remote-configuration/activegate/get-current-job "View parameters of a current configuration job for ActiveGates using the Dynatrace API.")

[List completed jobs](/docs/dynatrace-api/environment-api/remote-configuration/activegate/get-finished-jobs "Get an overview of completed configuration jobs for ActiveGates using the Dynatrace API.")

[View a job](/docs/dynatrace-api/environment-api/remote-configuration/activegate/get-job "View parameters of a configuration job for ActiveGates using the Dynatrace API.")

## Related topics

* [Remote configuration management of OneAgents and ActiveGates](/docs/ingest-from/bulk-configuration "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.")


---


## Source: geographic-regions.md


---
title: Geographic regions API
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/rum/geographic-regions
scraped: 2026-02-16T21:31:19.928023
---

# Geographic regions API

# Geographic regions API

* Reference
* Updated on May 02, 2022

[### List countries

Get an overview of countries and their codes.](/docs/dynatrace-api/environment-api/rum/geographic-regions/get-countries "View countries via Geographic regions API.")[### List regions

Get an overview of countries with a region breakdown.](/docs/dynatrace-api/environment-api/rum/geographic-regions/get-regions "View regions via Geographic regions API.")[### List regions of a country

Get an overview of regions within a country.](/docs/dynatrace-api/environment-api/rum/geographic-regions/get-regions-country "View regions in a country via Geographic regions API.")[### List cities of a country

Get an overview of cities within a country.](/docs/dynatrace-api/environment-api/rum/geographic-regions/get-cities-country "View cities in a country via Geographic regions API.")[### List cities of a region

Get an overview of cities within a region.](/docs/dynatrace-api/environment-api/rum/geographic-regions/get-cities-region "View cities of a region via Geographic regions API.")

## Related topics

* [Real User Monitoring](/docs/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.")
* [Detection of IP addresses, geolocations, and user agents](/docs/observe/digital-experience/rum-concepts/detection-of-ip-addresses-locations-and-user-agents "Dynatrace detects IP addresses and geolocations like a city, region, and country as well as browsers, devices, and operating systems.")


---


## Source: rum-cookie-names-get-cookie-names.md


---
title: RUM cookie names API - GET cookie names
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/rum/rum-cookie-names-get-cookie-names
scraped: 2026-02-16T21:31:03.617098
---

# RUM cookie names API - GET cookie names

# RUM cookie names API - GET cookie names

* Reference
* Published Jun 25, 2024

Lists RUM cookie names.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/rum/cookieNames` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/rum/cookieNames` |

## Authentication

To execute this request, you need an access token with `rumCookieNames.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [CookieNames](#openapi-definition-CookieNames) | Success. The response contains all RUM cookie names |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `CookieNames` object

The list of all cookie names.

| Element | Type | Description |
| --- | --- | --- |
| domainValidationCookieName | string | The name of the domain validation cookie. |
| latencyCookieName | string | The name of the latency cookie. |
| pageContextCookieName | string | The name of the page context cookie. |
| sessionCookieName | string | The name of the session cookie. |
| sessionTimeoutCookieName | string | The name of the session timeout cookie. |
| sourceActionCookieName | string | The name of the source action cookie. |
| visitorCookieName | string | The name of the visitor cookie. |

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



"domainValidationCookieName": "dtValidationCookie",



"latencyCookieName": "dtLatC",



"pageContextCookieName": "dtPC",



"sessionCookieName": "dtCookie",



"sessionTimeoutCookieName": "rxvt",



"sourceActionCookieName": "dtSA",



"visitorCookieName": "rxVisitor"



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

* [Real User Monitoring](/docs/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.")
* [Cookies](/docs/manage/data-privacy-and-security/data-privacy/cookies "Learn about first-party cookie usage in Dynatrace.")


---


## Source: get-inline-code.md


---
title: GET inline code
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-inline-code
scraped: 2026-02-16T09:28:33.887130
---

# GET inline code

# GET inline code

* Reference
* Updated on Sep 18, 2025

Returns the most recent [inline code](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats#inline-code "Select a format for the RUM JavaScript snippet that best fits your specific use case") for manual insertion into your web application code. It includes both the configuration and the RUM monitoring code.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/rum/inlineCode/{applicationId}` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/rum/inlineCode/{applicationId}` |

## Authentication

To execute this request, you need an access token with `rumManualInsertionTags.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| applicationId | string | The ID of the web application. | path | Required |

## Response

The response includes a `text/plain` payload containing the most recent version of the [inline code](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats#inline-code "Select a format for the RUM JavaScript snippet that best fits your specific use case") for the specified application.


---


## Source: get-javascript-tag.md


---
title: GET JavaScript tag
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-javascript-tag
scraped: 2026-02-16T09:28:08.850642
---

# GET JavaScript tag

# GET JavaScript tag

* Reference
* Updated on Sep 18, 2025

Returns the most recent [JavaScript tag](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats#js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case") for manual insertion into your web application code. It includes a reference to an external file that contains both the monitoring code and its configuration.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/rum/javaScriptTag/{applicationId}` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/rum/javaScriptTag/{applicationId}` |

## Authentication

To execute this request, you need an access token with `rumManualInsertionTags.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| applicationId | string | The ID of the web application. | path | Required |
| scriptExecutionAttribute | string | Specifies the script execution attribute: async, defer, or none. If specified, this overrides the configured value. The element can hold these values * `ASYNC` * `DEFER` * `NONE` | query | Optional |
| crossOriginAnonymous | boolean | Indicates whether to add the crossorigin="anonymous" attribute to the tag. If specified, this overrides the configured value. | query | Optional |

## Response

The response includes a `text/plain` payload containing the most recent version of the [JavaScript tag](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats#js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case") for the specified application.


---


## Source: get-oneagent-javascript-tag-with-sri.md


---
title: GET OneAgent JavaScript tag with SRI
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag-with-sri
scraped: 2026-02-16T21:26:01.354720
---

# GET OneAgent JavaScript tag with SRI

# GET OneAgent JavaScript tag with SRI

* Reference
* Updated on Sep 18, 2025

Returns the most recent [OneAgent JavaScript tag with SRI](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats#oneagent-js-tag-sri "Select a format for the RUM JavaScript snippet that best fits your specific use case") for manual insertion into your web application code. It includes configuration, a reference to the monitoring code, and an integrity hash. For more information on SRI support for RUM, see [Use Subresource Integrity (SRI) for Real User Monitoring code](/docs/observe/digital-experience/web-applications/initial-setup/subresource-integrity "Use the Subresource Integrity (SRI) browser feature to ensure the integrity of Real User Monitoring code.").

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/rum/oneAgentJavaScriptTagWithSri/{applicationId}` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/rum/oneAgentJavaScriptTagWithSri/{applicationId}` |

## Authentication

To execute this request, you need an access token with `rumManualInsertionTags.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| applicationId | string | The ID of the web application. | path | Required |
| scriptExecutionAttribute | string | Specifies the script execution attribute: async, defer, or none. If specified, this overrides the configured value. The element can hold these values * `ASYNC` * `DEFER` * `NONE` | query | Optional |

## Response

The response includes a `text/plain` payload containing the most recent version of the [OneAgent JavaScript tag with SRI](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats#oneagent-js-tag-sri "Select a format for the RUM JavaScript snippet that best fits your specific use case") for the specified application.


---


## Source: get-oneagent-javascript-tag.md


---
title: GET OneAgent JavaScript tag
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag
scraped: 2026-02-15T09:10:45.970299
---

# GET OneAgent JavaScript tag

# GET OneAgent JavaScript tag

* Reference
* Updated on Sep 18, 2025

Returns the most recent [OneAgent JavaScript tag](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats#oneagent-js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case") for manual insertion into your web application code. It includes configuration and a reference to the monitoring code.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/rum/oneAgentJavaScriptTag/{applicationId}` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/rum/oneAgentJavaScriptTag/{applicationId}` |

## Authentication

To execute this request, you need an access token with `rumManualInsertionTags.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| applicationId | string | The ID of the web application. | path | Required |
| scriptExecutionAttribute | string | Specifies the script execution attribute: async, defer, or none. If specified, this overrides the configured value. The element can hold these values * `ASYNC` * `DEFER` * `NONE` | query | Optional |

## Response

The response includes a `text/plain` payload containing the most recent version of the [OneAgent JavaScript tag](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats#oneagent-js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case") for the specified application.


---


## Source: rum-manual-insertion-tags.md


---
title: RUM manual insertion tags API
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags
scraped: 2026-02-16T21:29:09.227504
---

# RUM manual insertion tags API

# RUM manual insertion tags API

* Reference

The **RUM manual insertion tags API** allows you to retrieve the RUM JavaScript for two different manual insertion scenarios:

* [Agentless monitoring](/docs/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.") and
* [Manual insertion for pages of an auto-injected application](/docs/observe/digital-experience/web-applications/initial-setup/rum-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your applications").

Different [snippet formats](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats "Select a format for the RUM JavaScript snippet that best fits your specific use case") are available, and supported tag attributes can be controlled via API parameters. By integrating this API into your build scripts, you can automate the insertion of the RUM JavaScript and ensure that your application always uses the current configuration.

To retrieve the snippet format [code snippet](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats#code-snippet "Select a format for the RUM JavaScript snippet that best fits your specific use case"), use the [Real User Monitoring JavaScript API](/docs/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code "Learn how you can use the Dynatrace API to set up and maintain your manually injected applications using the Real User Monitoring JavaScript API.").

[### Get JavaScript tag

Retrieve the most recent JavaScript tag for manual insertion.](/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-javascript-tag "Retrieve the most recent JavaScript tag for manual insertion.")[### Get OneAgent JavaScript tag

Retrieve the most recent OneAgent JavaScript tag for manual insertion.](/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag "Retrieve the most recent OneAgent JavaScript tag for manual insertion.")[### Get OneAgent JavaScript tag with SRI

Retrieve the most recent OneAgent JavaScript tag with SRI for manual insertion.](/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag-with-sri "Retrieve the most recent OneAgent JavaScript tag with SRI for manual insertion.")[### Get inline code

Retrieve the most recent inline code for manual insertion.](/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-inline-code "Retrieve the most recent inline code for manual insertion.")


---


## Source: service-level-objectives-classic.md


---
title: Service-level Objectives API classic
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/service-level-objectives-classic
scraped: 2026-02-16T21:31:13.226279
---

# Service-level Objectives API classic

# Service-level Objectives API classic

* Reference
* Updated on Jan 07, 2025

Switch to SLO Service Public API

This is the Service-level Objectives API classic.

For the newest version, see [SLO Service Public API](/docs/dynatrace-api/environment-api/service-level-objectives "Discover the API functionalities of the new Service-Level Objectives powered by Grail.").

[### List all SLOs

Get an overview of all service-level objectives and their calculated values.](/docs/dynatrace-api/environment-api/service-level-objectives-classic/get-all "List all service-level objectives and their values via the Dynatrace API.")[### View an SLO

View the parameters and the calculated value of a service-level objective (SLO) by its ID.](/docs/dynatrace-api/environment-api/service-level-objectives-classic/get-slo "View parameters of a service-level objective classic via the Dynatrace API.")[### Create an SLO

Create a new service-level objective (SLO) with the exact parameters you need.](/docs/dynatrace-api/environment-api/service-level-objectives-classic/post-slo "Create a service-level objective (SLO) via the Dynatrace API.")[### Edit an SLO

Update the parameters of a service-level objective (SLO).](/docs/dynatrace-api/environment-api/service-level-objectives-classic/put-slo "Updates a service-level objective (SLO) parameters via the Dynatrace API.")[### Delete an SLO

Delete a service-level objective (SLO) you no longer need.](/docs/dynatrace-api/environment-api/service-level-objectives-classic/delete-slo "Delete a service-level objective (SLO) via the Dynatrace API.")[### Create an alert for an SLO

Create an alert for an SLO.](/docs/dynatrace-api/environment-api/service-level-objectives-classic/post-slo-alert "Create a service-level objective (SLO) alert via the Dynatrace API.")

## Related topics

* [Service-Level Objectives Classic](/docs/deliver/service-level-objectives-classic "Monitor and alert on service-level objectives with Dynatrace in Service-Level Objectives Classic.")


---


## Source: get-effective-values.md


---
title: Settings API - GET effective values
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/settings/objects/get-effective-values
scraped: 2026-02-16T21:29:10.601844
---

# Settings API - GET effective values

# Settings API - GET effective values

* Reference
* Published Aug 26, 2022

Lists effective settings values for the specified schemas at the specified scope.

If there are no settings objects available for the specified schema/scope combination, the request returns default values for the settings.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/effectiveValues` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/settings/effectiveValues` |

## Authentication

To execute this request, you need an access token with `settings.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| schemaIds | string | A list of comma-separated schema IDs to which the requested objects belong.  Only considered on load of the first page, when the **nextPageKey** is not set. | query | Optional |
| scope | string | The scope that the requested objects target.  The selection only matches objects directly targeting the specified scope. For example, `environment` will not match objects that target a host within environment. For more details, please see [Dynatrace Documentationï»¿](https://dt-url.net/ky03459).  To load the first page, when the **nextPageKey** is not set, this parameter is required. | query | Optional |
| fields | string | A list of fields to be included to the response. The provided set of fields replaces the default set.  Specify the required top-level fields, separated by commas (for example, `origin,value`).  Supported fields: `summary`, `searchSummary`, `created`, `modified`, `createdBy`, `modifiedBy`, `author`, `origin`, `schemaId`, `schemaVersion`, `value`, `externalId`. | query | Optional |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **nextPageKey** field of the previous response.  The first page is always returned if you don't specify the **nextPageKey** query parameter.  When the **nextPageKey** is set to obtain subsequent pages, you must omit all other query parameters. | query | Optional |
| pageSize | integer | The amount of settings objects in a single response payload.  The maximal allowed page size is 500.  If not set, 100 is used. | query | Optional |
| adminAccess | boolean | If set to true and user has settings:objects:admin permission, the endpoint will act as if the user is the owner of all objects | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [EffectiveSettingsValuesList](#openapi-definition-EffectiveSettingsValuesList) | Success |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The specified schema or scope is not found. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `EffectiveSettingsValuesList` object

A list of effective settings values.

| Element | Type | Description |
| --- | --- | --- |
| items | [EffectiveSettingsValue[]](#openapi-definition-EffectiveSettingsValue) | A list of effective settings values. |
| nextPageKey | string | The cursor for the next page of results. Has the value of `null` on the last page.  Use it in the **nextPageKey** query parameter to obtain subsequent pages of the result. |
| pageSize | integer | The number of entries per page. |
| totalCount | integer | The total number of entries in the result. |

#### The `EffectiveSettingsValue` object

An effective settings value.

| Element | Type | Description |
| --- | --- | --- |
| author | string | The user (identified by a user ID or a public token ID) who performed that most recent modification. |
| created | integer | The timestamp of the creation. |
| externalId | string | The external identifier of the settings object. |
| modified | integer | The timestamp of the last modification. |
| origin | string | The origin of the settings value. |
| schemaId | string | The schema on which the object is based. |
| schemaVersion | string | The version of the schema on which the object is based. |
| searchSummary | string | A searchable summary string of the setting value. Plain text without Markdown. |
| summary | string | A short summary of settings. This can contain Markdown and will be escaped accordingly. |
| value | string | The value of the setting.  It defines the actual values of settings' parameters.  The actual content depends on the object's schema. |

#### The `AnyValue` object

A schema representing an arbitrary value type.

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



"items": [



{



"author": "john.doe@example.com",



"created": 1,



"externalId": "string",



"modified": 1,



"origin": "HOST-D3A3C5A146830A79",



"schemaId": "builtin:container.built-in-monitoring-rule",



"schemaVersion": "1.0.0",



"searchSummary": "string",



"summary": "string",



"value": "string"



}



],



"nextPageKey": "AQAAABQBAAAABQ==",



"pageSize": 1,



"totalCount": 1



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


---


## Source: post-object.md


---
title: Settings API - POST an object
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/settings/objects/post-object
scraped: 2026-02-16T21:14:42.027783
---

# Settings API - POST an object

# Settings API - POST an object

* Reference
* Published Feb 24, 2021

Creates a new settings object or validates the provided settings object.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/objects` |
| POST | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/settings/objects` |

## Authentication

To execute this request, you need an access token with `settings.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| validateOnly | boolean | If `true`, the request runs only validation of the submitted settings objects, without saving them. | query | Optional |
| adminAccess | boolean | If set to true and user has settings:objects:admin permission, the endpoint will act as if the user is the owner of all objects | query | Optional |
| body | [SettingsObjectCreate[]](#openapi-definition-SettingsObjectCreate) | The JSON body of the request. Contains the settings objects. | body | Optional |

### Request body objects

#### The `RequestBody` object

#### The `SettingsObjectCreate` object

Configuration of a new settings object.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| externalId | string | External identifier for the object being created | Optional |
| insertAfter | string | The position of the new object. The new object will be added after the specified one.  If `null` (or unset), the new object will be placed in the last position.  If set to an empty string, the new object will be placed in the first position.  Only applicable for objects based on schemas with ordered objects (schema's `ordered` parameter is set to `true`). | Optional |
| objectId | string | The ID of the settings object that should be replaced.  Only applicable if an external identifier is provided. | Optional |
| schemaId | string | The schema on which the object is based. | Required |
| schemaVersion | string | The version of the schema on which the object is based. | Optional |
| scope | string | The scope that the object targets. For more details, please see [Dynatrace Documentationï»¿](https://dt-url.net/ky03459). | Required |
| value | string | The value of the setting.  It defines the actual values of settings' parameters.  The actual content depends on the object's schema. | Required |

#### The `AnyValue` object

A schema representing an arbitrary value type.

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
[



{



"externalId": "string",



"insertAfter": "Y2ktaGdyb3VwLTEyMythZjhjOThlOS0wN2I0LTMyMGEtOTQzNi02NTEyMmVlNWY4NGQ=",



"objectId": "Y2ktaGdyb3VwLTEyMythZjhjOThlOS0wN2I0LTMyMGEtOTQzNi02NTEyMmVlNWY4NGQ=",



"schemaId": "builtin:container.built-in-monitoring-rule",



"schemaVersion": "1.0.0",



"scope": "HOST-D3A3C5A146830A79",



"value": "string"



}



]
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SettingsObjectResponse[]](#openapi-definition-SettingsObjectResponse) | Success |
| **207** | [SettingsObjectResponse[]](#openapi-definition-SettingsObjectResponse) | Multi-status: different objects in the payload resulted in different statuses. |
| **400** | [SettingsObjectResponse[]](#openapi-definition-SettingsObjectResponse) | Failed. Schema validation failed. |
| **403** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. Forbidden. |
| **404** | [SettingsObjectResponse[]](#openapi-definition-SettingsObjectResponse) | Failed. The requested resource doesn't exist. |
| **409** | [SettingsObjectResponse[]](#openapi-definition-SettingsObjectResponse) | Failed. Conflicting resource. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ResponseBody` object

#### The `SettingsObjectResponse` object

The response to a creation- or update-request.

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code for the object. |
| error | [Error](#openapi-definition-Error) | - |
| invalidValue | string | The value of the setting.  It defines the actual values of settings' parameters.  The actual content depends on the object's schema. |
| objectId | string | For a successful request, the ID of the created or modified settings object. |

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

#### The `AnyValue` object

A schema representing an arbitrary value type.

#### The `ErrorResponseBody` object

#### The `SettingsObjectResponse` object

The response to a creation- or update-request.

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code for the object. |
| error | [Error](#openapi-definition-Error) | - |
| invalidValue | string | The value of the setting.  It defines the actual values of settings' parameters.  The actual content depends on the object's schema. |
| objectId | string | For a successful request, the ID of the created or modified settings object. |

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

#### The `AnyValue` object

A schema representing an arbitrary value type.

### Response body JSON models

```
[



{



"code": 1,



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



},



"invalidValue": "string",



"objectId": "Y2ktaGdyb3VwLTEyMythZjhjOThlOS0wN2I0LTMyMGEtOTQzNi02NTEyMmVlNWY4NGQ="



}



]
```

```
[



{



"code": 1,



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



},



"invalidValue": "string",



"objectId": "Y2ktaGdyb3VwLTEyMythZjhjOThlOS0wN2I0LTMyMGEtOTQzNi02NTEyMmVlNWY4NGQ="



}



]
```


---


## Source: builtin-app-transition-kubernetes.md


---
title: Settings API - Kubernetes app schema table
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/settings/schemas/builtin-app-transition-kubernetes
scraped: 2026-02-16T21:17:29.230447
---

# Settings API - Kubernetes app schema table

# Settings API - Kubernetes app schema table

* Published Feb 26, 2024

### Kubernetes app (`builtin:app-transition.kubernetes)`

Unlock an improved experience with the new Kubernetes app.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:app-transition.kubernetes` | * `group:cloud-and-virtualization` | `KUBERNETES_CLUSTER` - Kubernetes cluster  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:app-transition.kubernetes` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:app-transition.kubernetes` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:app-transition.kubernetes` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `kubernetesAppOptions` | [KubernetesAppOptions](#KubernetesAppOptions) | - | Required |

##### The `KubernetesAppOptions` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| New Kubernetes experience `enableKubernetesApp` | boolean | - | Required |


---


## Source: builtin-oneagent-features.md


---
title: Settings API - OneAgent features schema table
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/settings/schemas/builtin-oneagent-features
scraped: 2026-02-16T21:14:40.632242
---

# Settings API - OneAgent features schema table

# Settings API - OneAgent features schema table

* Published Dec 05, 2023

### OneAgent features (`builtin:oneagent.features)`

Dynatrace OneAgent follows a zero-configuration approach. Therefore, the set of default features apply when you roll out OneAgent the first time. When additional features become available with newer OneAgent versions, they can be activated here to make them available across your environment.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:oneagent.features` | * `group:preferences` | `PROCESS_GROUP_INSTANCE` - Process  `PROCESS_GROUP` - Process Group  `CLOUD_APPLICATION` - Kubernetes workload  `CLOUD_APPLICATION_NAMESPACE` - Kubernetes namespace  `KUBERNETES_CLUSTER` - Kubernetes cluster  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:oneagent.features` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:oneagent.features` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:oneagent.features` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Instrumentation enabled (change needs a process restart) `instrumentation` | boolean | - | Optional |
| Activate this feature also in OneAgents only fulfilling the minimum Opt-In version `forcible` | boolean | - | Optional |
| Feature `key` | text | - | Required |


---


## Source: get-schema.md


---
title: Settings API - GET a schema
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/settings/schemas/get-schema
scraped: 2026-02-16T21:14:39.310890
---

# Settings API - GET a schema

# Settings API - GET a schema

* Reference
* Published Feb 24, 2021

Gets parameters of the specified settings schema.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/{schemaId}` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/settings/schemas/{schemaId}` |

## Authentication

To execute this request, you need an access token with `settings.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| schemaId | string | The ID of the required schema. | path | Required |
| schemaVersion | string | The version of the required schema.  If not set, the most recent version is returned. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SchemaDefinitionRestDto](#openapi-definition-SchemaDefinitionRestDto) | Success |
| **403** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. Forbidden. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The specified schema doesn't exist. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `SchemaDefinitionRestDto` object

| Element | Type | Description |
| --- | --- | --- |
| allowedScopes | string[] | A list of scopes where the schema can be used. |
| constraints | [ComplexConstraint[]](#openapi-definition-ComplexConstraint) | A list of constrains limiting the values to be accepted by the schema. |
| deletionConstraints | [DeletionConstraint[]](#openapi-definition-DeletionConstraint) | Constraints limiting the values to be deleted. |
| description | string | A short description of the schema. |
| displayName | string | The display name of the schema. |
| documentation | string | An extended description of the schema and/or links to documentation. |
| dynatrace | string | The version of the data format. |
| enums | object | A list of definitions of enum properties. |
| keyProperty | string | Name of the key property in this schema. |
| maturity | string | The maturity of the schema. Possible values:  * PREVIEW: Preview features are not generally available, but might be available in specific environments as part of early-access programs. These are the most likely to change in incompatible ways. * EARLY\_ADOPTER: Features marked "early adopter" are available in all environments, but are not mature enough to warrant the "general availability" designation. We don't expect incompatible changes for these, but please be aware, that these are not fully stable yet and incompatible changes may be necessary in rare cases. * GENERAL\_AVAILABILITY: Features marked "general availability" are the most stable. While the schemas will still evolve over time, care will be taken to only do so in a backward-compatible manner.  In any case, automations should make use of the `schemaVersion` field when writing settings objects. The element can hold these values * `EARLY_ADOPTER` * `GENERAL_AVAILABILITY` * `PREVIEW` |
| maxObjects | integer | The maximum amount of objects per scope.  Only applicable when **multiObject** is set to `true`. |
| metadata | object | Metadata of the setting. |
| multiObject | boolean | Multiple (`true`) objects per scope are permitted or a single (`false`) object per scope is permitted. |
| ordered | boolean | If `true` the order of objects has semantic significance.  Only applicable when **multiObject** is set to `true`. |
| properties | object | A list of schema's properties. |
| schemaConstraints | [SchemaConstraintRestDto[]](#openapi-definition-SchemaConstraintRestDto) | Constraints limiting the values as a whole to be accepted in this configuration element. |
| schemaGroups | string[] | Names of the groups, which the schema belongs to. |
| schemaId | string | The ID of the schema. |
| tableColumns | object | Table column definitions for use in the ui. |
| types | object | A list of definitions of types.  A type is a complex property that contains its own set of subproperties. |
| uiCustomization | [UiCustomization](#openapi-definition-UiCustomization) | Customization for UI elements |
| version | string | The version of the schema. |

#### The `ComplexConstraint` object

A constraint on the values accepted for a complex settings property.

| Element | Type | Description |
| --- | --- | --- |
| checkAllProperties | boolean | Defines if modification of any property triggers secret resubmission check. |
| customMessage | string | A custom message for invalid values. |
| customValidatorId | string | The ID of a custom validator. |
| maximumPropertyCount | integer | The maximum number of properties that can be set. |
| minimumPropertyCount | integer | The minimum number of properties that must be set. |
| properties | string[] | A list of properties (defined by IDs) that are used to check the constraint. |
| skipAsyncValidation | boolean | Whether to skip validation on a change made from the UI. |
| timeout | integer | The maximum time in seconds the custom validator is allowed to run. |
| type | string | The type of the constraint. The element can hold these values * `CUSTOM_VALIDATOR_REF` * `GREATER_THAN` * `GREATER_THAN_OR_EQUAL` * `LESS_THAN` * `LESS_THAN_OR_EQUAL` * `PROPERTY_COUNT_RANGE` * `SECRET_RESUBMISSION` * `UNKNOWN` |

#### The `DeletionConstraint` object

A constraint on the values that are going to be deleted.

| Element | Type | Description |
| --- | --- | --- |
| customMessage | string | A custom message for invalid values. |
| customValidatorId | string | The ID of a custom validator. |
| schemaIds | string[] | The IDs of schemas that should be checked for references to this schema. |
| timeout | integer | The maximum time in seconds the custom validator is allowed to run. |
| type | string | The type of the deletion constraint. The element can hold these values * `CUSTOM_VALIDATOR_REF` * `REFERENTIAL_INTEGRITY` * `UNKNOWN` |

#### The `EnumType` object

Definition of an enum property.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the property. |
| displayName | string | The display name of the property. |
| documentation | string | An extended description and/or links to documentation. |
| enumClass | string | An existing Java enum class that holds the allowed values of the enum. |
| items | [EnumValue[]](#openapi-definition-EnumValue) | A list of allowed values of the enum. |
| type | string | The type of the property. The element can hold these values * `enum` |

#### The `EnumValue` object

An allowed value for an enum property.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the value. |
| displayName | string | The display name of the value. |
| enumInstance | string | The name of the value in an existing Java enum class. |
| icon | string | The icon of the value. |
| value | string | The allowed value of the enum. |

#### The `AnyValue` object

A schema representing an arbitrary value type.

#### The `PropertyDefinition` object

Configuration of a property in a settings schema.

| Element | Type | Description |
| --- | --- | --- |
| constraints | [Constraint[]](#openapi-definition-Constraint) | A list of constraints limiting the values to be accepted. |
| datasource | [DatasourceDefinition](#openapi-definition-DatasourceDefinition) | Configuration of a datasource for a property. |
| default | string | The default value to be used when no value is provided.  If a non-singleton has the value of `null`, it means an empty collection. |
| description | string | A short description of the property. |
| displayName | string | The display name of the property. |
| documentation | string | An extended description and/or links to documentation. |
| forceSecretResubmission | boolean | Defines if value is allowed to be modified when secret properties are not |
| items | [Item](#openapi-definition-Item) | An item of a collection property. |
| maxObjects | integer | The maximum number of **objects** in a collection property.  Has the value of `1` for singletons. |
| metadata | object | Metadata of the property. |
| migrationPattern | string | Pattern with references to properties to create a new value. |
| minObjects | integer | The minimum number of **objects** in a collection property. |
| modificationPolicy | string | Modification policy of the property. The element can hold these values * `ALWAYS` * `DEFAULT` * `NEVER` |
| nullable | boolean | The value can (`true`) or can't (`false`) be `null`. |
| precondition | [Precondition](#openapi-definition-Precondition) | A precondition for visibility of a property. |
| referencedType | string | The type referenced by the property value |
| subType | string | The subtype of the property's value. |
| type | string | The type of the property's value. |
| uiCustomization | [UiCustomization](#openapi-definition-UiCustomization) | Customization for UI elements |

#### The `Constraint` object

A constraint on the values accepted for a settings property.

| Element | Type | Description |
| --- | --- | --- |
| customMessage | string | A custom message for invalid values. |
| customValidatorId | string | The ID of a custom validator. |
| disallowDangerousRegex | boolean | Whether to disallow usage of dangerous regexes |
| maxLength | integer | The maximum allowed length of string values. |
| maximum | number | The maximum allowed value. |
| minLength | integer | The minimum required length of string values. |
| minimum | number | The minimum allowed value. |
| pattern | string | The regular expression pattern for valid string values. |
| skipAsyncValidation | boolean | Whether to skip validation on a change made from the UI. |
| timeout | integer | The maximum time in seconds the custom validator is allowed to run. |
| type | string | The type of the constraint. The element can hold these values * `CUSTOM_VALIDATOR_REF` * `LENGTH` * `NOT_BLANK` * `NOT_EMPTY` * `NO_WHITESPACE` * `PATTERN` * `RANGE` * `REGEX` * `TRIMMED` * `UNIQUE` * `UNKNOWN` |
| uniqueProperties | string[] | A list of properties for which the combination of values must be unique. |

#### The `DatasourceDefinition` object

Configuration of a datasource for a property.

| Element | Type | Description |
| --- | --- | --- |
| filterProperties | string[] | The properties to filter the datasource options on. |
| fullContext | boolean | Whether this datasource expects full setting payload as the context. |
| identifier | string | The identifier of a custom data source of the property's value. |
| resetValue | string | When to reset datasource value in the UI on filter change. The element can hold these values * `ALWAYS` * `INVALID_ONLY` * `NEVER` |
| useApiSearch | boolean | If true, the datasource should use the api to filter the results instead of client-side filtering. |
| validate | boolean | Whether to validate input to only allow values returned by the datasource. |

#### The `Item` object

An item of a collection property.

| Element | Type | Description |
| --- | --- | --- |
| constraints | [Constraint[]](#openapi-definition-Constraint) | A list of constraints limiting the values to be accepted. |
| datasource | [DatasourceDefinition](#openapi-definition-DatasourceDefinition) | Configuration of a datasource for a property. |
| description | string | A short description of the item. |
| displayName | string | The display name of the item. |
| documentation | string | An extended description and/or links to documentation. |
| metadata | object | Metadata of the items. |
| referencedType | string | The type referenced by the item's value. |
| subType | string | The subtype of the item's value. |
| type | string | The type of the item's value. |
| uiCustomization | [UiCustomization](#openapi-definition-UiCustomization) | Customization for UI elements |

#### The `UiCustomization` object

Customization for UI elements

| Element | Type | Description |
| --- | --- | --- |
| callback | [UiCallbackCustomization](#openapi-definition-UiCallbackCustomization) | UI customization options for defining custom callbacks |
| expandable | [UiExpandableCustomization](#openapi-definition-UiExpandableCustomization) | UI customization for expandable section |
| table | [UiTableCustomization](#openapi-definition-UiTableCustomization) | Customization for UI tables |
| tabs | [UiTabsCustomization](#openapi-definition-UiTabsCustomization) | UI customization for tabs |

#### The `UiCallbackCustomization` object

UI customization options for defining custom callbacks

| Element | Type | Description |
| --- | --- | --- |
| buttons | [UiButtonCustomization[]](#openapi-definition-UiButtonCustomization) | UI customization for defining buttons that call functions when pressed |

#### The `UiButtonCustomization` object

UI customization for defining a button that calls a function when pressed

| Element | Type | Description |
| --- | --- | --- |
| description | string | The description to be shown in a tooltip when hovering over the button |
| displayName | string | The label of the button |
| identifier | string | The identifier of the function to be called when the button is pressed |
| insert | string | The position where the button should be shown in the UI The element can hold these values * `FIRST` * `LAST` |

#### The `UiExpandableCustomization` object

UI customization for expandable section

| Element | Type | Description |
| --- | --- | --- |
| displayName | string | The display name |
| expanded | boolean | Defines if the item should be expanded by default |
| sections | [UiExpandableSectionCustomization[]](#openapi-definition-UiExpandableSectionCustomization) | A list of sections |

#### The `UiExpandableSectionCustomization` object

Expandable section customization for UI

| Element | Type | Description |
| --- | --- | --- |
| description | string | The description |
| displayName | string | The display name |
| expanded | boolean | Defines if the section should be expanded by default |
| properties | string[] | A list of properties |

#### The `UiTableCustomization` object

Customization for UI tables

| Element | Type | Description |
| --- | --- | --- |
| columns | [UiTableColumnCustomization[]](#openapi-definition-UiTableColumnCustomization) | A list of columns for the UI table |
| emptyState | [UiEmptyStateCustomization](#openapi-definition-UiEmptyStateCustomization) | UI customization for empty state in a table |

#### The `UiTableColumnCustomization` object

Customization for UI table columns

| Element | Type | Description |
| --- | --- | --- |
| builtinColumnRef | string | The ui specific builtin column-implementation for this column. |
| columnRef | string | The referenced column from the 'tableColumns' property of the schema for this column. |
| displayName | string | The display name for this column. |
| id | string | The id for this column used for filtering. Required for conflicting or pathed columns - otherwise the ref is used. |
| items | [UiTableColumnItemCustomization[]](#openapi-definition-UiTableColumnItemCustomization) | The possible items of this column. |
| propertyRef | string | The referenced property for this column. |
| type | string | The ui specific type for this column. |
| width | string | The width this column should take up on the table. |

#### The `UiTableColumnItemCustomization` object

Customization for UI table column items

| Element | Type | Description |
| --- | --- | --- |
| displayName | string | The display name of this item. |
| icon | string | The icon of this item. |
| value | string | The value of this item. |

#### The `UiEmptyStateCustomization` object

UI customization for empty state in a table

| Element | Type | Description |
| --- | --- | --- |
| text | string | The text to be shown in the empty state |

#### The `UiTabsCustomization` object

UI customization for tabs

| Element | Type | Description |
| --- | --- | --- |
| groups | [UiTabGroupCustomization[]](#openapi-definition-UiTabGroupCustomization) | A list of groups |

#### The `UiTabGroupCustomization` object

Tab group customization for UI

| Element | Type | Description |
| --- | --- | --- |
| description | string | The description |
| displayName | string | The display name |
| properties | string[] | A list of properties |

#### The `Precondition` object

A precondition for visibility of a property.

| Element | Type | Description |
| --- | --- | --- |
| expectedValue | string | The expected value of the property.  Only applicable to properties of the `EQUALS` type. |
| expectedValues | - | A list of valid values of the property.  Only applicable to properties of the `IN` type. |
| pattern | string | The Regular expression which is matched against the property.  Only applicable to properties of the `REGEX_MATCH` type. |
| precondition | [Precondition](#openapi-definition-Precondition) | A precondition for visibility of a property. |
| preconditions | [Precondition[]](#openapi-definition-Precondition) | A list of child preconditions to be evaluated.  Only applicable to properties of the `AND` and `OR` types. |
| property | string | The property to be evaluated. |
| type | string | The type of the precondition. The element can hold these values * `AND` * `EQUALS` * `IN` * `NOT` * `NULL` * `OR` * `REGEX_MATCH` |

#### The `SchemaConstraintRestDto` object

| Element | Type | Description |
| --- | --- | --- |
| byteLimit | integer | The maximum allowed size in bytes for the sum over all persisted values for the schema |
| customMessage | string | A custom message for invalid values. |
| customValidatorId | string | The ID of a custom validator. |
| flattenCollections | boolean | Whether to flatten collection properties when checking for uniqueness, so only disjoint collections are considered unique |
| skipAsyncValidation | boolean | Whether to skip validation on a change made from the UI. |
| type | string | The type of the schema constraint. The element can hold these values * `BYTE_SIZE_LIMIT` * `CUSTOM_VALIDATOR_REF` * `MULTI_SCOPE_CUSTOM_VALIDATOR_REF` * `MULTI_SCOPE_UNIQUE` * `UNIQUE` * `UNKNOWN` |
| uniqueProperties | string[] | The list of properties for which the combination of values needs to be unique |

#### The `TableColumn` object

The definition of a table column to be used in the ui.

| Element | Type | Description |
| --- | --- | --- |
| pattern | string | Pattern with references to properties to create a single value for the column. |

#### The `SchemaType` object

A list of definitions of types.

A type is a complex property that contains its own set of subproperties.

| Element | Type | Description |
| --- | --- | --- |
| constraints | [ComplexConstraint[]](#openapi-definition-ComplexConstraint) | A list of constraints limiting the values to be accepted. |
| description | string | A short description of the property. |
| displayName | string | The display name of the property. |
| documentation | string | An extended description and/or links to documentation. |
| properties | object | Definition of properties that can be persisted. |
| searchPattern | string | The pattern for the summary search(for example, "Alert after *X* minutes.") of the configuration in the UI. |
| summaryPattern | string | The pattern for the summary (for example, "Alert after *X* minutes.") of the configuration in the UI. |
| type | string | Type of the reference type. The element can hold these values * `object` |
| version | string | The version of the type. |
| versionInfo | string | A short description of the version. |

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



"allowedScopes": [



"host",



"application"



],



"constraints": [



{



"checkAllProperties": false,



"customMessage": "string",



"customValidatorId": "my-min-max",



"maximumPropertyCount": 2,



"minimumPropertyCount": 1,



"properties": [



"string"



],



"skipAsyncValidation": false,



"timeout": 5,



"type": "CUSTOM_VALIDATOR_REF"



}



],



"deletionConstraints": [



{



"customMessage": "string",



"customValidatorId": "my-min-max",



"schemaIds": [



"my-schema-id"



],



"timeout": 5,



"type": "CUSTOM_VALIDATOR_REF"



}



],



"description": "Dynatrace disables monitoring of containers that do not run any applications",



"displayName": "Built-in container monitoring rules",



"documentation": "string",



"dynatrace": "1",



"enums": {},



"keyProperty": "keyProperty",



"maturity": "GENERAL_AVAILABILITY",



"maxObjects": 10,



"metadata": {},



"multiObject": true,



"ordered": true,



"properties": {},



"schemaConstraints": [



{



"byteLimit": 500000,



"customMessage": "string",



"customValidatorId": "my-min-max",



"flattenCollections": true,



"skipAsyncValidation": false,



"type": "BYTE_SIZE_LIMIT",



"uniqueProperties": [



"my-prop-1",



"my-prop-2"



]



}



],



"schemaGroups": [



"group:some.1",



"group:some.2"



],



"schemaId": "builtin:container.built-in-monitoring-rule",



"tableColumns": {},



"types": {},



"uiCustomization": {



"callback": {



"buttons": [



{



"description": "string",



"displayName": "string",



"identifier": "string",



"insert": "FIRST"



}



]



},



"expandable": {



"displayName": "string",



"expanded": true,



"sections": [



{



"description": "string",



"displayName": "string",



"expanded": true,



"properties": [



"string"



]



}



]



},



"table": {



"columns": [



{



"builtinColumnRef": "summary",



"columnRef": "myCustomColumn",



"displayName": "Color",



"id": "color",



"items": [



{



"displayName": "Active",



"icon": "CRITICAL",



"value": "ACTIVE"



}



],



"propertyRef": "apiColor",



"type": "cell-color-picker",



"width": "10%"



}



],



"emptyState": {



"text": "string"



}



},



"tabs": {



"groups": [



{



"description": "string",



"displayName": "string",



"properties": [



"string"



]



}



]



}



},



"version": "1.4.2"



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


---


## Source: settings.md


---
title: Settings API
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/settings
scraped: 2026-02-16T21:14:37.680108
---

# Settings API

# Settings API

* Reference
* Published Feb 24, 2021

[### List schemas

Get an overview of all settings schemas in your environment.](/docs/dynatrace-api/environment-api/settings/schemas/get-all "View all settings schemas of your monitoring environment via the Dynatrace API.")[### View a schema

Get parameters of a schema.](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.")

[### List objects

Get an overview of settings objects.](/docs/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.")[### View an object

Get parameters of a settings object.](/docs/dynatrace-api/environment-api/settings/objects/get-object "View a settings object via the Dynatrace API.")

[### Create an object

Create a new settings object or validate the object you're working on.](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.")[### Edit an object

Update an existing settings object.](/docs/dynatrace-api/environment-api/settings/objects/put-object "Edit a settings object via the Dynatrace API.")[### Delete an object

Delete a settings object you no longer need.](/docs/dynatrace-api/environment-api/settings/objects/del-object "Delete a settings object via the Dynatrace API.")[### View values

Check the actual configuration of a settings object.](/docs/dynatrace-api/environment-api/settings/objects/get-effective-values "View an actual configuration for a settings schema via the Dynatrace API.")

## Related topics

* [Dynatrace settings framework](/docs/manage/settings/settings-20 "Introduction to the Settings 2.0 framework")


---


## Source: activegate-tokens.md


---
title: ActiveGate tokens API
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/tokens-v2/activegate-tokens
scraped: 2026-02-15T21:26:52.928078
---

# ActiveGate tokens API

# ActiveGate tokens API

* Reference
* Published Dec 02, 2021

[### List all tokens

Get an overview of all ActiveGate tokens available in your environment.](/docs/dynatrace-api/environment-api/tokens-v2/activegate-tokens/get-all-activegate-tokens "List all ActiveGate tokens available for your monitoring environment via Dynatrace API.")[### View a token

Get metadata of an ActiveGate token by its ID.](/docs/dynatrace-api/environment-api/tokens-v2/activegate-tokens/get-activegate-token "View metadata of an ActiveGate token via Dynatrace API.")[### Create a token

Create a new ActiveGate token with a defined scope and validity period.](/docs/dynatrace-api/environment-api/tokens-v2/activegate-tokens/post-activegate-token "Create a new ActiveGate token via Dynatrace API.")[### Delete a token

Delete an ActiveGate token your environment doesn't need anymore.](/docs/dynatrace-api/environment-api/tokens-v2/activegate-tokens/delete-activegate-token "Delete an ActiveGate token via Dynatrace API.")

## Related topics

* [Dynatrace ActiveGate](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.")


---


## Source: tenant-tokens.md


---
title: Tenant tokens API
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/tokens-v2/tenant-tokens
scraped: 2026-02-16T21:25:01.409835
---

# Tenant tokens API

# Tenant tokens API

* Reference
* Published Feb 23, 2021

[### Start rotation

Initiate rotation of the tenant token.](/docs/dynatrace-api/environment-api/tokens-v2/tenant-tokens/post-start "Initiate Dynatrace tenant token rotation.")[### Finish rotation

Complete rotation of the tenant token.](/docs/dynatrace-api/environment-api/tokens-v2/tenant-tokens/post-finish "Finish Dynatrace tenant token rotation.")[### Cancel rotation

Cancel rotation of the tenant token.](/docs/dynatrace-api/environment-api/tokens-v2/tenant-tokens/post-cancel "Cancel Dynatrace tenant token rotation.")

## Related topics

* [Tenant token classic](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Learn what a tenant token is and how to change it.")
* [ActiveGate directories](/docs/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.")
* [OneAgent configuration via command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.")


---


## Source: get-all.md


---
title: Applications API - GET all apps
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-all
scraped: 2026-02-16T21:19:23.814995
---

# Applications API - GET all apps

# Applications API - GET all apps

* Reference
* Updated on Mar 22, 2023
* Deprecated

This API is deprecated. Use the [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") instead. You can find more information about switching to the new API in the [migration guide](/docs/dynatrace-api/basics/deprecation-migration-guides/topology-v1-to-entity-v2 "Migrate your automation to the Monitored entities API.").

Fetches the list of all [applications](/docs/discover-dynatrace/get-started/glossary#app "Get acquainted with Dynatrace terminology.") in your Dynatrace environment, along with their parameters.

The full list can be lengthy, so you can narrow it down by specifying filter parameters, like tags. See the **Parameters** section for more details.

You can additionally limit the output by using the pagination:

1. Specify the number of results per page in the **pageSize** query parameter.
2. Then use the cursor from the **Next-Page-Key** response header in the **nextPageKey** query parameter to obtain subsequent pages.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/applications` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/applications` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| startTimestamp | integer | The start timestamp of the requested timeframe, in milliseconds (UTC).  If not set, then 72 hours behind from now is used. | query | Optional |
| endTimestamp | integer | The end timestamp of the requested timeframe, in milliseconds (UTC).  If not set, then the current timestamp is used.  The timeframe must not exceed 3 days. | query | Optional |
| relativeTime | string | The relative timeframe, back from now. The element can hold these values * `min` * `5mins` * `10mins` * `15mins` * `30mins` * `hour` * `2hours` * `6hours` * `day` * `3days` | query | Optional |
| tag | string[] | Filters the resulting set of applications by the specified tag. You can specify several tags in the following format: `tag=tag1&tag=tag2`. The application has to match **all** the specified tags.  In case of key-value tags, such as imported AWS or CloudFoundry tags, use the following format: `tag=[context]key:value`. For custom key-value tags, omit the context: `tag=key:value`. | query | Optional |
| entity | string[] | Filters result to the specified applications only.  To specify several applications use the following format: `entity=ID1&entity=ID2`. | query | Optional |
| managementZone | integer | Only return applications that are part of the specified management zone. | query | Optional |
| includeDetails | boolean | Includes (`true`) or excludes (`false`) details which are queried from related entities.  Excluding details may make queries faster.  If not set, then `true` is used. | query | Optional |
| pageSize | integer | The number of applications per result page.  If not set, pagination is not used and the result contains all applications fitting the specified filtering criteria. | query | Optional |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **Next-Page-Key** header of the previous response.  If you're using pagination, the first page is always returned without this cursor.  You must keep all other query parameters as they were in the first request to obtain subsequent pages. | query | Optional |

## Response headers

| Header | Type | Description |
| --- | --- | --- |
| Total-Count | integer | The estimated number of results. |
| Next-Page-Key | string | The cursor for the next page of results. Without it you'll get the first page again. |
| Page-Size | string | The maximum number of results per page. |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [Application[]](#openapi-definition-Application) | Success |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ResponseBody` object

#### The `Application` object

| Element | Type | Description |
| --- | --- | --- |
| applicationMatchTarget | string | -The element can hold these values * `DOMAIN` * `URL` |
| applicationType | string | -The element can hold these values * `AGENTLESS_MONITORING` * `AUTO_INJECTED` * `DEFAULT` * `SAAS_VENDOR` |
| customizedName | string | The customized name of the entity |
| discoveredName | string | The discovered name of the entity |
| displayName | string | The name of the Dynatrace entity as displayed in the UI. |
| entityId | string | The Dynatrace entity ID of the required entity. |
| firstSeenTimestamp | integer | The timestamp of when the entity was first detected, in UTC milliseconds |
| fromRelationships | object | The list of outgoing calls from the application. |
| lastSeenTimestamp | integer | The timestamp of when the entity was last detected, in UTC milliseconds |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | The management zones that the entity is part of. |
| ruleAppliedMatchType | string | -The element can hold these values * `ALL_URLS_AND_DOMAINS` * `CONTAINS` * `ENDS` * `EQUALS` * `MATCHES` * `STARTS` |
| ruleAppliedPattern | string | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | The list of entity tags. |
| toRelationships | object | The list of incoming calls to the application. |

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

#### The `TagInfo` object

Tag of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. The element can hold these values * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | The key of the tag.  Custom tags have the tag value here. |
| value | string | The value of the tag.  Not applicable to custom tags. |

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
[



{



"applicationMatchTarget": "DOMAIN",



"applicationType": "AGENTLESS_MONITORING",



"customizedName": "string",



"discoveredName": "string",



"displayName": "string",



"entityId": "string",



"firstSeenTimestamp": 1,



"fromRelationships": {



"calls": [



"string"



]



},



"lastSeenTimestamp": 1,



"managementZones": [



{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}



],



"ruleAppliedMatchType": "ALL_URLS_AND_DOMAINS",



"ruleAppliedPattern": "string",



"tags": [



{



"context": "AWS",



"key": "string",



"value": "string"



}



],



"toRelationships": {



"monitors": [



"string"



]



}



}



]
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

In this example, the request asks for a list all the applications in the environment.

The API token is passed in the **Authorization** header.

The result is truncated to three entries.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/entity/applications/ \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/applications
```

#### Response body

```
[



{



"entityId": "APPLICATION-EA7C4B59F27D43EB",



"displayName": "RUM Default Application",



"customizedName": "RUM Default Application",



"discoveredName": "RUM Default Application",



"firstSeenTimestamp": 1422282024216,



"lastSeenTimestamp": 1538579528065,



"tags": [



{



"context": "CONTEXTLESS",



"key": "Mytag"



},



{



"context": "CONTEXTLESS",



"key": "Test"



}



],



"fromRelationships": {



"calls": [



"SERVICE-FFE4B7A6D72F2CAC"



]



},



"toRelationships": {},



"applicationType": "DEFAULT",



"ruleAppliedPattern": "http",



"managementZones": [



{



"id": "-6239538939987181652",



"name": "allTypes"



},



{



"id": "-2519468841583898843",



"name": "app name exists"



},



{



"id": "4485554873951847460",



"name": "Applications except easyTravel"



}



]



},



{



"entityId": "APPLICATION-BBFA55551D507E2B",



"displayName": "easyTravel Ionic Web",



"discoveredName": "easyTravel Ionic Web",



"firstSeenTimestamp": 1528695861873,



"lastSeenTimestamp": 1538572321269,



"tags": [],



"fromRelationships": {



"calls": [



"SERVICE-ED0B103392AC86BF"



]



},



"toRelationships": {},



"applicationType": "RUMONLY",



"managementZones": [



{



"id": "-6239538939987181652",



"name": "allTypes"



},



{



"id": "-4085081632192243904",



"name": "easyTravel"



}



]



},



{



"entityId": "MOBILE_APPLICATION-752C288D59734C79",



"displayName": "easyTravel Demo",



"customizedName": "easyTravel Demo",



"discoveredName": "752c288d-5973-4c79-b7d1-3a49d4d42ea0",



"firstSeenTimestamp": 1469613941393,



"lastSeenTimestamp": 1538654940201,



"tags": [



{



"context": "CONTEXTLESS",



"key": "portal"



},



{



"context": "CONTEXTLESS",



"key": "easyTravel"



}



],



"fromRelationships": {



"calls": [



"SERVICE-ED0B103392AC86BF"



]



},



"toRelationships": {},



"mobileOsFamily": [



"ANDROID",



"IOS",



"WINDOWS"



],



"managementZones": [



{



"id": "-4085081632192243904",



"name": "easyTravel"



}



]



}



]
```

#### Response code

200

## Related topics

* [Real User Monitoring](/docs/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.")


---


## Source: get-an-app.md


---
title: Applications API - GET an application
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-an-app
scraped: 2026-02-16T21:19:19.598111
---

# Applications API - GET an application

# Applications API - GET an application

* Reference
* Updated on Mar 22, 2023
* Deprecated

This API is deprecated. Use the [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") instead. You can find more information about switching to the new API in the [migration guide](/docs/dynatrace-api/basics/deprecation-migration-guides/topology-v1-to-entity-v2 "Migrate your automation to the Monitored entities API.").

Gets the parameters of the specified application.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/applications/{meIdentifier}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/applications/{meIdentifier}` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| meIdentifier | string | The Dynatrace entity ID of the required application. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [Application](#openapi-definition-Application) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `Application` object

| Element | Type | Description |
| --- | --- | --- |
| applicationMatchTarget | string | -The element can hold these values * `DOMAIN` * `URL` |
| applicationType | string | -The element can hold these values * `AGENTLESS_MONITORING` * `AUTO_INJECTED` * `DEFAULT` * `SAAS_VENDOR` |
| customizedName | string | The customized name of the entity |
| discoveredName | string | The discovered name of the entity |
| displayName | string | The name of the Dynatrace entity as displayed in the UI. |
| entityId | string | The Dynatrace entity ID of the required entity. |
| firstSeenTimestamp | integer | The timestamp of when the entity was first detected, in UTC milliseconds |
| fromRelationships | object | The list of outgoing calls from the application. |
| lastSeenTimestamp | integer | The timestamp of when the entity was last detected, in UTC milliseconds |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | The management zones that the entity is part of. |
| ruleAppliedMatchType | string | -The element can hold these values * `ALL_URLS_AND_DOMAINS` * `CONTAINS` * `ENDS` * `EQUALS` * `MATCHES` * `STARTS` |
| ruleAppliedPattern | string | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | The list of entity tags. |
| toRelationships | object | The list of incoming calls to the application. |

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

#### The `TagInfo` object

Tag of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. The element can hold these values * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | The key of the tag.  Custom tags have the tag value here. |
| value | string | The value of the tag.  Not applicable to custom tags. |

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



"applicationMatchTarget": "DOMAIN",



"applicationType": "AGENTLESS_MONITORING",



"customizedName": "string",



"discoveredName": "string",



"displayName": "string",



"entityId": "string",



"firstSeenTimestamp": 1,



"fromRelationships": {



"calls": [



"string"



]



},



"lastSeenTimestamp": 1,



"managementZones": [



{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}



],



"ruleAppliedMatchType": "ALL_URLS_AND_DOMAINS",



"ruleAppliedPattern": "string",



"tags": [



{



"context": "AWS",



"key": "string",



"value": "string"



}



],



"toRelationships": {



"monitors": [



"string"



]



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

In this example, the request inquires about the properties of the **easyTravel Demo** application, which has the ID **MOBILE\_APPLICATION-752C288D59734C79**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl --request GET \



--url https://mySampleEnv.live.dynatrace.com/api/v1/entity/applications/MOBILE_APPLICATION-752C288D59734C79 \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/applications/MOBILE_APPLICATION-752C288D59734C79
```

#### Response body

```
{



"entityId": "MOBILE_APPLICATION-752C288D59734C79",



"displayName": "easyTravel Demo",



"customizedName": "easyTravel Demo",



"discoveredName": "752c288d-5973-4c79-b7d1-3a49d4d42ea0",



"firstSeenTimestamp": 1469613941393,



"lastSeenTimestamp": 1538656560201,



"tags": [



{



"context": "CONTEXTLESS",



"key": "portal"



},



{



"context": "CONTEXTLESS",



"key": "easyTravel"



}



],



"fromRelationships": {



"calls": [



"SERVICE-ED0B103392AC86BF"



]



},



"toRelationships": {},



"mobileOsFamily": [



"ANDROID",



"IOS",



"WINDOWS"



],



"managementZones": [



{



"id": "-6239538939987181652",



"name": "allTypes"



},



{



"id": "6518151499932123858",



"name": "mobile app name exists"



},



{



"id": "-4085081632192243904",



"name": "easyTravel"



}



]



}
```

#### Response code

200

## Related topics

* [Real User Monitoring](/docs/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.")


---


## Source: get-baseline.md


---
title: Applications API - GET baseline
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-baseline
scraped: 2026-02-16T21:19:15.019176
---

# Applications API - GET baseline

# Applications API - GET baseline

* Reference
* Updated on Mar 22, 2023
* Deprecated

Gets the baseline data of the specified application.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/applications/{meIdentifier}/baseline` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/applications/{meIdentifier}/baseline` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| meIdentifier | string | The Dynatrace entity ID of the required application. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ApplicationBaselineValues](#openapi-definition-ApplicationBaselineValues) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ApplicationBaselineValues` object

The baseline data for an application and its children for each available duration metric.

A duration metric is one of the following:

* **DOM interactive**
* **HTML downloaded**
* **Load event end**
* **Load event start**
* **Response time**
* **Speed index**
* **Time to first byte**
* **Visually complete**

| Element | Type | Description |
| --- | --- | --- |
| applicationDomInteractiveBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for the **DOM interactive** duration metric. |
| applicationHtmlDownloadedBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for the **HTML downloaded** duration metric. |
| applicationLoadEventEndBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for the **Load event end** duration metric. |
| applicationLoadEventStartBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for the **Load event start** duration metric. |
| applicationResponseTimeBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for the **Response time** duration metric. |
| applicationSpeedIndexBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for the **Speed index** duration metric. |
| applicationTimeToFirstByteBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for the **Time to first byte** duration metric. |
| applicationVisualCompleteBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for the **Visually complete** duration metric. |
| displayName | string | The name of the application as displayed in the UI. |
| entityId | string | The Dynatrace entity ID of the application. |

#### The `EntityBaselineData` object

The baseline data for a Dynatrace entity for a specific duration metric.

| Element | Type | Description |
| --- | --- | --- |
| childBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for child entities of this entity, for example a `SERVICE_METHOD` of a `SERVICE_METHOD_GROUP`. |
| displayName | string | The display name of the entity. |
| entityId | string | The ID of the Dynatrace entity. |
| errorRate | number | The error rate baseline. |
| hasLoadBaseline | boolean | The entity has a load baseline (`true`) or doesn't (`false`). |
| micros90thPercentile | number | The 90th percentile baseline, in microseconds. |
| microsMedian | number | The median baseline, in microseconds. |

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



"applicationDomInteractiveBaselines": [



{



"childBaselines": [



{}



],



"displayName": "string",



"entityId": "string",



"errorRate": 1,



"hasLoadBaseline": true,



"micros90thPercentile": 1,



"microsMedian": 1



}



],



"applicationHtmlDownloadedBaselines": [



{}



],



"applicationLoadEventEndBaselines": [



{}



],



"applicationLoadEventStartBaselines": [



{}



],



"applicationResponseTimeBaselines": [



{}



],



"applicationSpeedIndexBaselines": [



{}



],



"applicationTimeToFirstByteBaselines": [



{}



],



"applicationVisualCompleteBaselines": [



{}



],



"displayName": "string",



"entityId": "string"



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

* [Real User Monitoring](/docs/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.")


---


## Source: post-tags.md


---
title: Applications API - POST tags
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/applications-api/post-tags
scraped: 2026-02-16T21:19:22.297291
---

# Applications API - POST tags

# Applications API - POST tags

* Reference
* Updated on Mar 22, 2023
* Deprecated

Assigns [custom tags](/docs/manage/tags-and-metadata "Learn how to define tags and metadata. Understand how to use tags and metadata to organize your environment.") to the specified application. You only need to provide a tag value. The `CONTEXTLESS` context will be assigned automatically.

The usage of this API is limited to value-only tags. To assign key:value tags, use the [Custom tags API](/docs/dynatrace-api/environment-api/custom-tags/post-tags "Assign custom tags to monitored entities via Dynatrace API.").

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/applications/{meIdentifier}` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/applications/{meIdentifier}` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| meIdentifier | string | The Dynatrace entity ID of the application you want to update. | path | Required |
| body | [UpdateEntity](#openapi-definition-UpdateEntity) | A list of tags to be assigned to a Dynatrace entity. | body | Optional |

### Request body objects

#### The `UpdateEntity` object

A list of tags to be assigned to a Dynatrace entity.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| tags | string[] | A list of tags to be assigned to a Dynatrace entity. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"tags": [



"office-linz",



"office-klagenfurt"



]



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The parameters of the application have been updated. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
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

In this example, the request assigns the tags **iOS app** and **Android app** to the **easyTravel Demo** application, which has the ID **MOBILE\_APPLICATION-752C288D59734C79**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/entity/applications/MOBILE_APPLICATION-752C288D59734C79 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"tags": [



"iOS app",



"Android app"



]



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/applications/MOBILE_APPLICATION-752C288D59734C79
```

#### Request body

```
{



"tags": [



"iOS app",



"Android app"



]



}
```

#### Response code

204

## Related topics

* [Real User Monitoring](/docs/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.")


---


## Source: create-custom-device-via-dynatrace-api.md


---
title: Create custom device via the Dynatrace API
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/create-custom-device-via-dynatrace-api
scraped: 2026-02-16T21:19:06.696666
---

# Create custom device via the Dynatrace API

# Create custom device via the Dynatrace API

* Reference
* Updated on Mar 22, 2023
* Deprecated

The **Custom device** endpoint of the **Topology and Smartscape** API enables you to create a custom device with a specified name in your Dynatrace environment.

This page describes how to create a custom device without sending any data to it.

To learn how to report data to a custom device, see [Report custom device metric via REST API](/docs/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/report-custom-device-metric-via-rest-api "Learn how you can use the Dynatrace API to send a custom metric data point to a custom device.").

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/infrastructure/custom/{customDeviceId}` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/infrastructure/custom/{customDeviceId}` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

For this use case, the **series** element of the request body must be **omitted**.

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| customDeviceId | string | The ID of the custom device.  If you use the ID of an existing device, the respective parameters will be updated.  Don't use Dynatrace entity ID here. | path | Required |
| body | [CustomDevicePushMessage](#openapi-definition-CustomDevicePushMessage) | The JSON body of the request. Contains parameters of a custom device. | body | Optional |

### Request body objects

#### The `CustomDevicePushMessage` object

Configuration of a custom device.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| configUrl | string | The URL of a configuration web page for the custom device, such as a login page for a firewall or router. | Optional |
| displayName | string | The name of the custom device that will appear in the user interface. | Optional |
| favicon | string | The icon to be displayed for your custom component within Smartscape. Provide the full URL of the icon file. | Optional |
| group | string | User defined group ID of entity.  The group ID helps to keep a consistent picture of device-group relations. One of many cases where a proper group is important is service detection: you can define which custom devices should lead to the same service by defining the same group ID for them.  If you set a group ID, it will be hashed into the Dynatrace entity ID of the custom device. In that case the custom device can only be part of one custom device group.  If you don't set the group ID, Dynatrace will create it based on the ID or type of the custom device. Also, the group will not be hashed into the device ID which means the device may switch groups. | Optional |
| hostNames | string[] | The list of host names related to the custom device.  These names are used to automatically discover the horizontal communication relationship between this component and all other observed components within Smartscape. Once a connection is discovered, it is automatically mapped and shown within Smartscape.  If you send a value, the existing values will be overwritten.  If you send `null` or an empty value; or omit this field, the existing values will be kept. | Optional |
| ipAddresses | string[] | The list of IP addresses that belong to the custom device.  These addresses are used to automatically discover the horizontal communication relationship between this component and all other observed components within Smartscape. Once a connection is discovered, it is automatically mapped and shown within Smartscape.  If you send a value (including an empty value), the existing values will be overwritten.  If you send `null` or omit this field, the existing values will be kept. | Optional |
| listenPorts | integer[] | The list of ports the custom devices listens to.  These ports are used to discover the horizontal communication relationship between this component and all other observed components within Smartscape.  Once a connection is discovered, it is automatically mapped and shown within Smartscape.  If ports are specified, you should also add at least one IP address or a host name for the custom device.  If you send a value, the existing values will be overwritten.  If you send `null`, or an empty value, or omit this field, the existing values will be kept. | Optional |
| properties | object | The list of key-value pair properties that will be shown beneath the infographics of your custom device. | Optional |
| series | [EntityTimeseriesData[]](#openapi-definition-EntityTimeseriesData) | The list of metric values that are reported for the custom device.  The metric you're reporting must already exist in Dynatrace. To learn how to create a custom metric, see [Timeseries API v1 - PUT a custom metricï»¿](https://dt-url.net/5k143rzb).  Dynatrace aggregates all the values you report for a custom device.  If you send a value (including an empty value), it will be added to the set of existing values.  If you send `null` or omit this field, the set of existing values won't change. | Optional |
| tags | string[] | List of custom tags that you want to attach to your custom device. | Optional |
| type | string | The technology type definition of the custom device.  It must be the same technology type of the metric you're reporting.  If you send a value, the existing value will be overwritten.  If you send `null`, empty or omit this field, the existing value will be kept. | Optional |

#### The `EntityTimeseriesData` object

Information about a metric and its data points.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| dataPoints | array[] | List of data points.  Each data point is an array, containing the timestamp and the value.  Timestamp is UTC milliseconds reported as a number, for example: `1520523365557`.  You have the guaranteed timeframe of **30 minutes** into the past.  A custom metric must be registered **before** you can report a metric value. Therefore, the timestamp for reporting a value must be after the registration time of the metric. | Required |
| dimensions | object | Dimensions of the data points you're posting.  The key of the metric dimension must be defined earlier in the metric definition. | Optional |
| timeseriesId | string | The ID of the metric, where you want to post data points. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"configUrl": "http://coffee-machine.dynatrace.internal.com/coffeemachine/manage",



"displayName": "coffeeMachine",



"favicon": "https://www.freefavicon.com/freefavicons/food/cup-of-coffee-152-78475.png",



"group": "myCustomDeviceGroup",



"hostNames": [



"coffee-machine.dynatrace.internal.com"



],



"ipAddresses": [



"10.0.0.1"



],



"listenPorts": [



80



],



"properties": {},



"series": [



{



"dataPoints": [



[



1521542929000,



13



]



],



"dimensions": {



"office": "Linz"



},



"timeseriesId": "custom:created.coffee.metric"



}



],



"tags": [



"office-linz"



],



"type": "coffee machine"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [CustomDevicePushResult](#openapi-definition-CustomDevicePushResult) | Success. The custom device has been created or updated. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `CustomDevicePushResult` object

The result of a custom device push request. The entity ID is calculated automatically.

| Element | Type | Description |
| --- | --- | --- |
| entityId | string | The Dynatrace entity ID of the custom device. |
| groupId | string | The Dynatrace entity ID of the custom device group. |

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



"entityId": "string",



"groupId": "string"



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

In this example, the request creates custom device `idOfmyCustomDevice` of type `F5-Firewall`, with IP address `172.16.115.211` and listen port `9999`. The request also specifies some additional parameters.

See [Report custom device metric via the Dynatrace API](/docs/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/report-custom-device-metric-via-rest-api "Learn how you can use the Dynatrace API to send a custom metric data point to a custom device.") to learn how to submit data to the newly created custom device.

The API token is passed in the **Authorization** header.

The request returns the IDs of the custom device (see `entityId`) and its group (see `groupId`) as confirmation.

You can download or copy the example request body to try it out on your own.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/custom/idOfmyCustomDevice \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'



-H 'Content-Type: application/json' \



-d '{



"displayName" : "F5 Firewall 24",



"ipAddresses" : ["172.16.115.211"],



"listenPorts" : ["9999"],



"type" : "F5-Firewall",



"favicon" : "http://assets.dynatrace.com/global/icons/f5.png",



"configUrl" : "http://192.128.0.1:8080",



"tags": [



"REST example"



],



"properties" : {



"Sample Property 1": "Sample value 1"



}



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/custom/idOfmyCustomDevice
```

#### Request body

```
{



"displayName": "F5 Firewall 24",



"ipAddresses": ["172.16.115.211"],



"listenPorts": ["9999"],



"type": "F5-Firewall",



"favicon": "http://assets.dynatrace.com/global/icons/f5.png",



"configUrl": "http://192.128.0.1:8080",



"tags": ["REST example"],



"properties": {



"Sample Property 1": "Sample value 1"



}



}
```

#### Response body

```
{



"entityId": "CUSTOM_DEVICE-6A567B33AADC306E",



"groupId": "CUSTOM_DEVICE_GROUP-FC2E2ABF54F513D8"



}
```

#### Response code

200

#### Result

![New custom device in Smartscape](https://dt-cdn.net/images/custom-device-smartscape-1103-ba9b69e490.png)

![Properties of the custom device](https://dt-cdn.net/images/custom-device-658-bb2295e42c.png)


---


## Source: report-custom-device-metric-via-rest-api.md


---
title: Report custom device metric via Dynatrace API
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/report-custom-device-metric-via-rest-api
scraped: 2026-02-16T21:19:26.657439
---

# Report custom device metric via Dynatrace API

# Report custom device metric via Dynatrace API

* Reference
* Updated on Mar 22, 2023
* Deprecated

The **Custom device** endpoint of the **Topology and Smartscape** API enables you to send a custom metric data point to a custom device in Dynatrace. This request is also able to update the metadata of the custom device.

The metric you're reporting must already exist in Dynatrace.

See [Create custom device via the Dynatrace API](/docs/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/create-custom-device-via-dynatrace-api "Learn how you can use the Dynatrace API to create a custom device.") to learn how to create a custom device without sending data to it.

You can send data to the custom device retrospectivelyâthe **custom device** endpoint supports the reporting of data up to one hour in the past. However, to ensure the proper functioning of AI root-cause analysis and metric-based alerting, we recommend that data be sent in real time.

For this use case, the **series** element of the request body is **required**.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/infrastructure/custom/{customDeviceId}` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/infrastructure/custom/{customDeviceId}` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| customDeviceId | string | The ID of the custom device.  If you use the ID of an existing device, the respective parameters will be updated.  Don't use Dynatrace entity ID here. | path | Required |
| body | [CustomDevicePushMessage](#openapi-definition-CustomDevicePushMessage) | The JSON body of the request. Contains parameters of a custom device. | body | Optional |

### Request body objects

#### The `CustomDevicePushMessage` object

Configuration of a custom device.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| configUrl | string | The URL of a configuration web page for the custom device, such as a login page for a firewall or router. | Optional |
| displayName | string | The name of the custom device that will appear in the user interface. | Optional |
| favicon | string | The icon to be displayed for your custom component within Smartscape. Provide the full URL of the icon file. | Optional |
| group | string | User defined group ID of entity.  The group ID helps to keep a consistent picture of device-group relations. One of many cases where a proper group is important is service detection: you can define which custom devices should lead to the same service by defining the same group ID for them.  If you set a group ID, it will be hashed into the Dynatrace entity ID of the custom device. In that case the custom device can only be part of one custom device group.  If you don't set the group ID, Dynatrace will create it based on the ID or type of the custom device. Also, the group will not be hashed into the device ID which means the device may switch groups. | Optional |
| hostNames | string[] | The list of host names related to the custom device.  These names are used to automatically discover the horizontal communication relationship between this component and all other observed components within Smartscape. Once a connection is discovered, it is automatically mapped and shown within Smartscape.  If you send a value, the existing values will be overwritten.  If you send `null` or an empty value; or omit this field, the existing values will be kept. | Optional |
| ipAddresses | string[] | The list of IP addresses that belong to the custom device.  These addresses are used to automatically discover the horizontal communication relationship between this component and all other observed components within Smartscape. Once a connection is discovered, it is automatically mapped and shown within Smartscape.  If you send a value (including an empty value), the existing values will be overwritten.  If you send `null` or omit this field, the existing values will be kept. | Optional |
| listenPorts | integer[] | The list of ports the custom devices listens to.  These ports are used to discover the horizontal communication relationship between this component and all other observed components within Smartscape.  Once a connection is discovered, it is automatically mapped and shown within Smartscape.  If ports are specified, you should also add at least one IP address or a host name for the custom device.  If you send a value, the existing values will be overwritten.  If you send `null`, or an empty value, or omit this field, the existing values will be kept. | Optional |
| properties | object | The list of key-value pair properties that will be shown beneath the infographics of your custom device. | Optional |
| series | [EntityTimeseriesData[]](#openapi-definition-EntityTimeseriesData) | The list of metric values that are reported for the custom device.  The metric you're reporting must already exist in Dynatrace. To learn how to create a custom metric, see [Timeseries API v1 - PUT a custom metricï»¿](https://dt-url.net/5k143rzb).  Dynatrace aggregates all the values you report for a custom device.  If you send a value (including an empty value), it will be added to the set of existing values.  If you send `null` or omit this field, the set of existing values won't change. | Optional |
| tags | string[] | List of custom tags that you want to attach to your custom device. | Optional |
| type | string | The technology type definition of the custom device.  It must be the same technology type of the metric you're reporting.  If you send a value, the existing value will be overwritten.  If you send `null`, empty or omit this field, the existing value will be kept. | Optional |

#### The `EntityTimeseriesData` object

Information about a metric and its data points.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| dataPoints | array[] | List of data points.  Each data point is an array, containing the timestamp and the value.  Timestamp is UTC milliseconds reported as a number, for example: `1520523365557`.  You have the guaranteed timeframe of **30 minutes** into the past.  A custom metric must be registered **before** you can report a metric value. Therefore, the timestamp for reporting a value must be after the registration time of the metric. | Required |
| dimensions | object | Dimensions of the data points you're posting.  The key of the metric dimension must be defined earlier in the metric definition. | Optional |
| timeseriesId | string | The ID of the metric, where you want to post data points. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"configUrl": "http://coffee-machine.dynatrace.internal.com/coffeemachine/manage",



"displayName": "coffeeMachine",



"favicon": "https://www.freefavicon.com/freefavicons/food/cup-of-coffee-152-78475.png",



"group": "myCustomDeviceGroup",



"hostNames": [



"coffee-machine.dynatrace.internal.com"



],



"ipAddresses": [



"10.0.0.1"



],



"listenPorts": [



80



],



"properties": {},



"series": [



{



"dataPoints": [



[



1521542929000,



13



]



],



"dimensions": {



"office": "Linz"



},



"timeseriesId": "custom:created.coffee.metric"



}



],



"tags": [



"office-linz"



],



"type": "coffee machine"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [CustomDevicePushResult](#openapi-definition-CustomDevicePushResult) | Success. The custom device has been created or updated. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `CustomDevicePushResult` object

The result of a custom device push request. The entity ID is calculated automatically.

| Element | Type | Description |
| --- | --- | --- |
| entityId | string | The Dynatrace entity ID of the custom device. |
| groupId | string | The Dynatrace entity ID of the custom device group. |

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



"entityId": "string",



"groupId": "string"



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

In this example, the request reports two data points of `custom:firewall.connections.dropped` for the `idOfmyCustomDevice` device. The data points (with value `460` for the `1539860400000` timestamp and value `456` for the `1539860460000` timestamp) belong to the `ethernetcard1` value of the `nic` dimension.

The request also reports two more data points of the same metric, but for `ethernetcard2` in the same dimension, and it updates device metadata by adding a property and a tag.

The API token is passed in the **Authorization** header.

The request returns the IDs of the custom device (see `entityId`) and its group (see `groupId`) as confirmation.

You can download or copy the example request body to try it out on your own.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/custom/idOfmyCustomDevice \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"tags": [



"tag2"



],



"type": "F5-Firewall",



"properties" : {



"Sample Property 2": "Sample value 2"



},



"series" : [



{



"timeseriesId" : "custom:firewall.connections.dropped",



"dimensions" : {



"nic" : "ethernetcard1"



},



"dataPoints" : [



[ 1539860400000, 460 ],



[ 1539860460000, 456 ]



]



},



{



"timeseriesId" : "custom:firewall.connections.dropped",



"dimensions" : {



"nic" : "ethernetcard2"



},



"dataPoints" : [



[ 1539860430000, 439 ],



[ 1539860490000, 460 ]



]



}



]



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/custom/idOfmyCustomDevice
```

#### Request body

```
{



"tags": ["tag2"],



"type": "F5-Firewall",



"properties": {



"Sample Property 2": "Sample value 2"



},



"series": [



{



"timeseriesId": "custom:firewall.connections.dropped",



"dimensions": {



"nic": "ethernetcard1"



},



"dataPoints": [



[1539860400000, 460],



[1539860460000, 456]



]



},



{



"timeseriesId": "custom:firewall.connections.dropped",



"dimensions": {



"nic": "ethernetcard2"



},



"dataPoints": [



[1539860430000, 439],



[1539860490000, 460]



]



}



]



}
```

#### Response body

```
{



"entityId": "CUSTOM_DEVICE-6A567B33AADC306E",



"groupId": "CUSTOM_DEVICE_GROUP-FC2E2ABF54F513D8"



}
```

#### Response code

200

#### Result

![Metrics of the custom device in chart](https://dt-cdn.net/images/custom-devices-chart-1410-2a46660659.png)


---


## Source: get-a-host.md


---
title: Hosts API - GET a host
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/get-a-host
scraped: 2026-02-16T21:19:03.523448
---

# Hosts API - GET a host

# Hosts API - GET a host

* Reference
* Updated on Mar 22, 2023
* Deprecated

This API is deprecated. Use the [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") instead. You can find more information about switching to the new API in the [migration guide](/docs/dynatrace-api/basics/deprecation-migration-guides/topology-v1-to-entity-v2 "Migrate your automation to the Monitored entities API.").

Gets the parameters of the specified host.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/infrastructure/hosts/{meIdentifier}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/infrastructure/hosts/{meIdentifier}` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| meIdentifier | string | The Dynatrace entity ID of the required host. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [Host](#openapi-definition-Host) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `Host` object

Information about the host.

| Element | Type | Description |
| --- | --- | --- |
| agentVersion | [AgentVersion](#openapi-definition-AgentVersion) | Defines the version of the agent currently running on the entity. |
| amiId | string | - |
| autoInjection | string | Status of auto-injection The element can hold these values * `DISABLED_MANUALLY` * `DISABLED_ON_INSTALLATION` * `DISABLED_ON_SANITY_CHECK` * `ENABLED` * `FAILED_ON_INSTALLATION` |
| autoScalingGroup | string | - |
| awsInstanceId | string | - |
| awsInstanceType | string | - |
| awsNameTag | string | The name inherited from AWS. |
| awsSecurityGroup | string[] | - |
| azureComputeModeName | string | -The element can hold these values * `DEDICATED` * `SHARED` |
| azureEnvironment | string | - |
| azureHostNames | string[] | - |
| azureResourceGroupName | string | - |
| azureResourceId | string | - |
| azureSiteNames | string[] | - |
| azureSku | string | -The element can hold these values * `BASIC` * `DYNAMIC` * `FREE` * `PREMIUM` * `SHARED` * `STANDARD` |
| azureVmName | string | - |
| azureVmScaleSetName | string | - |
| azureVmSizeLabel | string | - |
| azureZone | string | - |
| beanstalkEnvironmentName | string | - |
| bitness | string | -The element can hold these values * `32bit` * `64bit` |
| boshAvailabilityZone | string | The Cloud Foundry BOSH availability zone. |
| boshDeploymentId | string | The Cloud Foundry BOSH deployment ID. |
| boshInstanceId | string | The Cloud Foundry BOSH instance ID. |
| boshInstanceName | string | The Cloud Foundry BOSH instance name. |
| boshName | string | The Cloud Foundry BOSH name. |
| boshStemcellVersion | string | The Cloud Foundry BOSH stemcell version. |
| cloudPlatformVendorVersion | string | Defines the cloud platform vendor version. |
| cloudType | string | -The element can hold these values * `AZURE` * `EC2` * `GOOGLE_CLOUD_PLATFORM` * `OPENSTACK` * `ORACLE` * `UNRECOGNIZED` |
| consumedHostUnits | string | Consumed Host Units. Applicable only for [Dynatrace classic licensingï»¿](https://www.dynatrace.com/support/help/shortlink/application-and-infrastructure-host-units) |
| cpuCores | integer | - |
| customizedName | string | The customized name of the entity |
| discoveredName | string | The discovered name of the entity |
| displayName | string | The name of the Dynatrace entity as displayed in the UI. |
| entityId | string | The Dynatrace entity ID of the required entity. |
| esxiHostName | string | - |
| firstSeenTimestamp | integer | The timestamp of when the entity was first detected, in UTC milliseconds |
| fromRelationships | object | - |
| gceInstanceId | string | The Google Compute Engine instance ID. |
| gceInstanceName | string | The Google Compute Engine instance name. |
| gceMachineType | string | The Google Compute Engine machine type. |
| gceProject | string | The Google Compute Engine project. |
| gceProjectId | string | The Google Compute Engine numeric project ID. |
| gcePublicIpAddresses | string[] | The public IP addresses of the Google Compute Engine. |
| gcpZone | string | The Google Cloud Platform Zone. |
| hostGroup | [HostGroup](#openapi-definition-HostGroup) | - |
| hypervisorType | string | -The element can hold these values * `AHV` * `AWS_NITRO` * `GVISOR` * `HYPERV` * `KVM` * `LPAR` * `QEMU` * `UNRECOGNIZED` * `VIRTUALBOX` * `VMWARE` * `WPAR` * `XEN` |
| ipAddresses | string[] | - |
| isMonitoringCandidate | boolean | - |
| kubernetesCluster | string | The kubernetes cluster the entity is in. |
| kubernetesLabels | object | The kubernetes labels defined on the entity. |
| kubernetesNode | string | The kubernetes node the entity is in. |
| lastSeenTimestamp | integer | The timestamp of when the entity was last detected, in UTC milliseconds |
| localHostName | string | - |
| localIp | string | - |
| logicalCpuCores | integer | - |
| logicalCpus | integer | The AIX instance logical CPU count. |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | The management zones that the entity is part of. |
| monitoringMode | string | -The element can hold these values * `FULL_STACK` * `INFRASTRUCTURE` * `OFF` |
| networkZoneId | string | The ID of network zone the entity is in. |
| oneAgentCustomHostName | string | The custom name defined in OneAgent config. |
| openStackInstaceType | string | - |
| openstackAvZone | string | - |
| openstackComputeNodeName | string | - |
| openstackProjectName | string | - |
| openstackSecurityGroups | string[] | - |
| openstackVmName | string | - |
| osArchitecture | string | -The element can hold these values * `ARM` * `IA64` * `PARISC` * `PPC` * `PPCLE` * `S390` * `SPARC` * `X86` * `ZOS` |
| osType | string | -The element can hold these values * `AIX` * `DARWIN` * `HPUX` * `LINUX` * `SOLARIS` * `WINDOWS` * `ZOS` |
| osVersion | string | - |
| paasAgentVersions | [AgentVersion[]](#openapi-definition-AgentVersion) | The versions of the PaaS agents currently running on the entity. |
| paasMemoryLimit | integer | - |
| paasType | string | -The element can hold these values * `AWS_ECS_EC2` * `AWS_ECS_FARGATE` * `AWS_LAMBDA` * `AZURE_FUNCTIONS` * `AZURE_WEBSITES` * `CLOUD_FOUNDRY` * `GOOGLE_APP_ENGINE` * `GOOGLE_CLOUD_RUN` * `HEROKU` * `KUBERNETES` * `OPENSHIFT` |
| publicHostName | string | - |
| publicIp | string | - |
| scaleSetName | string | - |
| simultaneousMultithreading | integer | The AIX instance simultaneous threads count. |
| softwareTechnologies | [TechnologyInfo[]](#openapi-definition-TechnologyInfo) | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | The list of entity tags. |
| toRelationships | object | - |
| userLevel | string | -The element can hold these values * `NON_SUPERUSER` * `NON_SUPERUSER_STRICT` * `SUPERUSER` |
| virtualCpus | integer | The AIX instance virtual CPU count. |
| vmwareName | string | - |
| zosCPUModelNumber | string | The CPU model number. |
| zosCPUSerialNumber | string | The CPU serial number. |
| zosLpaName | string | Name of the LPAR. |
| zosSystemName | string | Name of the system. |
| zosTotalGeneralPurposeProcessors | integer | Number of assigned processors for this LPAR. |
| zosTotalPhysicalMemory | integer | Memory assigned to the host (Terabyte). |
| zosTotalZiipProcessors | integer | Number of assigned support processors for this LPAR. |
| zosVirtualization | string | Type of virtualization on the mainframe. |

#### The `AgentVersion` object

Defines the version of the agent currently running on the entity.

| Element | Type | Description |
| --- | --- | --- |
| major | integer | The major version number. |
| minor | integer | The minor version number. |
| revision | integer | The revision number. |
| sourceRevision | string | A string representation of the SVN revision number. |
| timestamp | string | A timestamp string: format "yyyymmdd-hhmmss |

#### The `HostGroup` object

| Element | Type | Description |
| --- | --- | --- |
| meId | string | The Dynatrace entity ID of the host group. |
| name | string | The name of the Dynatrace entity, displayed in the UI. |

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

#### The `TechnologyInfo` object

| Element | Type | Description |
| --- | --- | --- |
| edition | string | - |
| type | string | - |
| version | string | - |

#### The `TagInfo` object

Tag of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. The element can hold these values * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | The key of the tag.  Custom tags have the tag value here. |
| value | string | The value of the tag.  Not applicable to custom tags. |

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



"agentVersion": {



"major": 1,



"minor": 1,



"revision": 1,



"sourceRevision": "string",



"timestamp": "string"



},



"amiId": "string",



"autoInjection": "DISABLED_MANUALLY",



"autoScalingGroup": "string",



"awsInstanceId": "string",



"awsInstanceType": "string",



"awsNameTag": "string",



"awsSecurityGroup": [



"string"



],



"azureComputeModeName": "DEDICATED",



"azureEnvironment": "string",



"azureHostNames": [



"string"



],



"azureResourceGroupName": "string",



"azureResourceId": "string",



"azureSiteNames": [



"string"



],



"azureSku": "BASIC",



"azureVmName": "string",



"azureVmScaleSetName": "string",



"azureVmSizeLabel": "string",



"azureZone": "string",



"beanstalkEnvironmentName": "string",



"bitness": "32bit",



"boshAvailabilityZone": "string",



"boshDeploymentId": "string",



"boshInstanceId": "string",



"boshInstanceName": "string",



"boshName": "string",



"boshStemcellVersion": "string",



"cloudPlatformVendorVersion": "string",



"cloudType": "AZURE",



"consumedHostUnits": "string",



"cpuCores": 1,



"customizedName": "string",



"discoveredName": "string",



"displayName": "string",



"entityId": "string",



"esxiHostName": "string",



"firstSeenTimestamp": 1,



"fromRelationships": {



"isNetworkClientOfHost": [



"string"



]



},



"gceInstanceId": "string",



"gceInstanceName": "string",



"gceMachineType": "string",



"gceProject": "string",



"gceProjectId": "string",



"gcePublicIpAddresses": [



"string"



],



"gcpZone": "string",



"hostGroup": {



"meId": "string",



"name": "string"



},



"hypervisorType": "AHV",



"ipAddresses": [



"string"



],



"isMonitoringCandidate": true,



"kubernetesCluster": "string",



"kubernetesLabels": {},



"kubernetesNode": "string",



"lastSeenTimestamp": 1,



"localHostName": "string",



"localIp": "string",



"logicalCpuCores": 1,



"logicalCpus": 1,



"managementZones": [



{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}



],



"monitoringMode": "FULL_STACK",



"networkZoneId": "string",



"oneAgentCustomHostName": "string",



"openStackInstaceType": "string",



"openstackAvZone": "string",



"openstackComputeNodeName": "string",



"openstackProjectName": "string",



"openstackSecurityGroups": [



"string"



],



"openstackVmName": "string",



"osArchitecture": "ARM",



"osType": "AIX",



"osVersion": "string",



"paasAgentVersions": [



{}



],



"paasMemoryLimit": 1,



"paasType": "AWS_ECS_EC2",



"publicHostName": "string",



"publicIp": "string",



"scaleSetName": "string",



"simultaneousMultithreading": 1,



"softwareTechnologies": [



{



"edition": "string",



"type": "string",



"version": "string"



}



],



"tags": [



{



"context": "AWS",



"key": "string",



"value": "string"



}



],



"toRelationships": {



"isNetworkClientOfHost": [



"string"



],



"isProcessOf": [



"string"



],



"isSiteOf": [



"string"



],



"runsOn": [



"string"



]



},



"userLevel": "NON_SUPERUSER",



"virtualCpus": 1,



"vmwareName": "string",



"zosCPUModelNumber": "string",



"zosCPUSerialNumber": "string",



"zosLpaName": "string",



"zosSystemName": "string",



"zosTotalGeneralPurposeProcessors": 1,



"zosTotalPhysicalMemory": 1,



"zosTotalZiipProcessors": 1,



"zosVirtualization": "string"



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

In this example, the request queries the parameters of the **tag009** host, which has the ID of **HOST-B7A6F9EE9F366CB5**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/hosts/HOST-B7A6F9EE9F366CB5 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/hosts/HOST-B7A6F9EE9F366CB5
```

#### Response body

```
{



"entityId": "HOST-B7A6F9EE9F366CB5",



"displayName": "tag009",



"discoveredName": "tag009",



"firstSeenTimestamp": 1538473087608,



"lastSeenTimestamp": 1538641647769,



"tags": [



{



"context": "CONTEXTLESS",



"key": "loadtest"



},



{



"context": "CONTEXTLESS",



"key": "host tag"



}



],



"fromRelationships": {



"isNetworkClientOfHost": [



"HOST-80FF8584D8954C1D",



"HOST-A281F848361E79A1"



]



},



"toRelationships": {



"isProcessOf": [



"PROCESS_GROUP_INSTANCE-9146FB8A6A155F93"



],



"isSiteOf": [



"GEOLOC_SITE-F72DF471AE5F56F6"



],



"isNetworkClientOfHost": [



"HOST-80FF8584D8954C1D"



],



"runsOn": [



"PROCESS_GROUP-83D74C22E79B074F"



]



},



"osType": "LINUX",



"osArchitecture": "X86",



"osVersion": "Ubuntu 18.04.1",



"ipAddresses": [



"127.0.0.1",



"192.168.1.1"



],



"bitness": "64bit",



"cpuCores": 4,



"logicalCpuCores": 8,



"consumedHostUnits": 2,



"managementZones": [



{



"id": "6164525246045854296",



"name": "Zone Service E"



},



{



"id": "5678",



"name": "Infrastructure Linux"



}



]



}
```

#### Response code

200

## Related topics

* [Hosts Classic](/docs/observe/infrastructure-observability/hosts "Learn how to get started with host monitoring, understand which measures contribute to host health, how to set up custom host names, and more.")


---


## Source: get-all.md


---
title: Hosts API - GET all hosts
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/get-all
scraped: 2026-02-16T21:19:05.251823
---

# Hosts API - GET all hosts

# Hosts API - GET all hosts

* Reference
* Updated on Mar 22, 2023
* Deprecated

This API is deprecated. Use the [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") instead. You can find more information about switching to the new API in the [migration guide](/docs/dynatrace-api/basics/deprecation-migration-guides/topology-v1-to-entity-v2 "Migrate your automation to the Monitored entities API.").

Gets the list of all hosts in your Dynatrace environment, along with their parameters.

The full list can be lengthy, so you can narrow it down by specifying filter parameters, like tags. See the **Parameters** section for more details.

You can additionally limit the output by using the pagination:

1. Specify the number of results per page in the **pageSize** query parameter.
2. Then use the cursor from the **Next-Page-Key** response header in the **nextPageKey** query parameter to obtain subsequent pages.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/infrastructure/hosts` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/infrastructure/hosts` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The timeframe is restricted to a **maximum period of 3 days**.

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| startTimestamp | integer | The start timestamp of the requested timeframe, in milliseconds (UTC).  If not set, then 72 hours behind from now is used. | query | Optional |
| endTimestamp | integer | The end timestamp of the requested timeframe, in milliseconds (UTC).  If not set, then the current timestamp is used.  The timeframe must not exceed 3 days. | query | Optional |
| relativeTime | string | The relative timeframe, back from now. The element can hold these values * `min` * `5mins` * `10mins` * `15mins` * `30mins` * `hour` * `2hours` * `6hours` * `day` * `3days` | query | Optional |
| tag | string[] | Filters the resulting set of hosts by the specified tag. You can specify several tags in the following format: `tag=tag1&tag=tag2`. The host has to match **all** the specified tags.  In case of key-value tags, such as imported AWS or CloudFoundry tags, use the following format: `tag=[context]key:value`. For custom key-value tags, omit the context: `tag=key:value`. | query | Optional |
| showMonitoringCandidates | boolean | Includes (`true`) or excludes (`false`) a monitoring candidate in the response.  Monitoring candidates are network entities that are detected but not monitored. | query | Optional |
| entity | string[] | Filters result to the specified hosts only.  To specify several hosts use the following format: `entity=ID1&entity=ID2`. | query | Optional |
| managementZone | integer | Only return hosts that are part of the specified management zone. | query | Optional |
| hostGroupId | string | Filters the resulting set of hosts by the specified host group.  Specify the Dynatrace IDs of the host group you're interested in. | query | Optional |
| hostGroupName | string | Filters the resulting set of hosts by the specified host group.  Specify the name of the host group you're interested in. | query | Optional |
| includeDetails | boolean | Includes (`true`) or excludes (`false`) details which are queried from related entities.  Excluding details may make queries faster.  If not set, then `true` is used. | query | Optional |
| pageSize | integer | The number of hosts per result page.  If not set, pagination is not used and the result contains all hosts fitting the specified filtering criteria. | query | Optional |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **Next-Page-Key** header of the previous response.  If you're using pagination, the first page is always returned without this cursor.  You must keep all other query parameters as they were in the first request to obtain subsequent pages. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [Host[]](#openapi-definition-Host) | Success |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ResponseBody` object

#### The `Host` object

Information about the host.

| Element | Type | Description |
| --- | --- | --- |
| agentVersion | [AgentVersion](#openapi-definition-AgentVersion) | Defines the version of the agent currently running on the entity. |
| amiId | string | - |
| autoInjection | string | Status of auto-injection The element can hold these values * `DISABLED_MANUALLY` * `DISABLED_ON_INSTALLATION` * `DISABLED_ON_SANITY_CHECK` * `ENABLED` * `FAILED_ON_INSTALLATION` |
| autoScalingGroup | string | - |
| awsInstanceId | string | - |
| awsInstanceType | string | - |
| awsNameTag | string | The name inherited from AWS. |
| awsSecurityGroup | string[] | - |
| azureComputeModeName | string | -The element can hold these values * `DEDICATED` * `SHARED` |
| azureEnvironment | string | - |
| azureHostNames | string[] | - |
| azureResourceGroupName | string | - |
| azureResourceId | string | - |
| azureSiteNames | string[] | - |
| azureSku | string | -The element can hold these values * `BASIC` * `DYNAMIC` * `FREE` * `PREMIUM` * `SHARED` * `STANDARD` |
| azureVmName | string | - |
| azureVmScaleSetName | string | - |
| azureVmSizeLabel | string | - |
| azureZone | string | - |
| beanstalkEnvironmentName | string | - |
| bitness | string | -The element can hold these values * `32bit` * `64bit` |
| boshAvailabilityZone | string | The Cloud Foundry BOSH availability zone. |
| boshDeploymentId | string | The Cloud Foundry BOSH deployment ID. |
| boshInstanceId | string | The Cloud Foundry BOSH instance ID. |
| boshInstanceName | string | The Cloud Foundry BOSH instance name. |
| boshName | string | The Cloud Foundry BOSH name. |
| boshStemcellVersion | string | The Cloud Foundry BOSH stemcell version. |
| cloudPlatformVendorVersion | string | Defines the cloud platform vendor version. |
| cloudType | string | -The element can hold these values * `AZURE` * `EC2` * `GOOGLE_CLOUD_PLATFORM` * `OPENSTACK` * `ORACLE` * `UNRECOGNIZED` |
| consumedHostUnits | string | Consumed Host Units. Applicable only for [Dynatrace classic licensingï»¿](https://www.dynatrace.com/support/help/shortlink/application-and-infrastructure-host-units) |
| cpuCores | integer | - |
| customizedName | string | The customized name of the entity |
| discoveredName | string | The discovered name of the entity |
| displayName | string | The name of the Dynatrace entity as displayed in the UI. |
| entityId | string | The Dynatrace entity ID of the required entity. |
| esxiHostName | string | - |
| firstSeenTimestamp | integer | The timestamp of when the entity was first detected, in UTC milliseconds |
| fromRelationships | object | - |
| gceInstanceId | string | The Google Compute Engine instance ID. |
| gceInstanceName | string | The Google Compute Engine instance name. |
| gceMachineType | string | The Google Compute Engine machine type. |
| gceProject | string | The Google Compute Engine project. |
| gceProjectId | string | The Google Compute Engine numeric project ID. |
| gcePublicIpAddresses | string[] | The public IP addresses of the Google Compute Engine. |
| gcpZone | string | The Google Cloud Platform Zone. |
| hostGroup | [HostGroup](#openapi-definition-HostGroup) | - |
| hypervisorType | string | -The element can hold these values * `AHV` * `AWS_NITRO` * `GVISOR` * `HYPERV` * `KVM` * `LPAR` * `QEMU` * `UNRECOGNIZED` * `VIRTUALBOX` * `VMWARE` * `WPAR` * `XEN` |
| ipAddresses | string[] | - |
| isMonitoringCandidate | boolean | - |
| kubernetesCluster | string | The kubernetes cluster the entity is in. |
| kubernetesLabels | object | The kubernetes labels defined on the entity. |
| kubernetesNode | string | The kubernetes node the entity is in. |
| lastSeenTimestamp | integer | The timestamp of when the entity was last detected, in UTC milliseconds |
| localHostName | string | - |
| localIp | string | - |
| logicalCpuCores | integer | - |
| logicalCpus | integer | The AIX instance logical CPU count. |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | The management zones that the entity is part of. |
| monitoringMode | string | -The element can hold these values * `FULL_STACK` * `INFRASTRUCTURE` * `OFF` |
| networkZoneId | string | The ID of network zone the entity is in. |
| oneAgentCustomHostName | string | The custom name defined in OneAgent config. |
| openStackInstaceType | string | - |
| openstackAvZone | string | - |
| openstackComputeNodeName | string | - |
| openstackProjectName | string | - |
| openstackSecurityGroups | string[] | - |
| openstackVmName | string | - |
| osArchitecture | string | -The element can hold these values * `ARM` * `IA64` * `PARISC` * `PPC` * `PPCLE` * `S390` * `SPARC` * `X86` * `ZOS` |
| osType | string | -The element can hold these values * `AIX` * `DARWIN` * `HPUX` * `LINUX` * `SOLARIS` * `WINDOWS` * `ZOS` |
| osVersion | string | - |
| paasAgentVersions | [AgentVersion[]](#openapi-definition-AgentVersion) | The versions of the PaaS agents currently running on the entity. |
| paasMemoryLimit | integer | - |
| paasType | string | -The element can hold these values * `AWS_ECS_EC2` * `AWS_ECS_FARGATE` * `AWS_LAMBDA` * `AZURE_FUNCTIONS` * `AZURE_WEBSITES` * `CLOUD_FOUNDRY` * `GOOGLE_APP_ENGINE` * `GOOGLE_CLOUD_RUN` * `HEROKU` * `KUBERNETES` * `OPENSHIFT` |
| publicHostName | string | - |
| publicIp | string | - |
| scaleSetName | string | - |
| simultaneousMultithreading | integer | The AIX instance simultaneous threads count. |
| softwareTechnologies | [TechnologyInfo[]](#openapi-definition-TechnologyInfo) | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | The list of entity tags. |
| toRelationships | object | - |
| userLevel | string | -The element can hold these values * `NON_SUPERUSER` * `NON_SUPERUSER_STRICT` * `SUPERUSER` |
| virtualCpus | integer | The AIX instance virtual CPU count. |
| vmwareName | string | - |
| zosCPUModelNumber | string | The CPU model number. |
| zosCPUSerialNumber | string | The CPU serial number. |
| zosLpaName | string | Name of the LPAR. |
| zosSystemName | string | Name of the system. |
| zosTotalGeneralPurposeProcessors | integer | Number of assigned processors for this LPAR. |
| zosTotalPhysicalMemory | integer | Memory assigned to the host (Terabyte). |
| zosTotalZiipProcessors | integer | Number of assigned support processors for this LPAR. |
| zosVirtualization | string | Type of virtualization on the mainframe. |

#### The `AgentVersion` object

Defines the version of the agent currently running on the entity.

| Element | Type | Description |
| --- | --- | --- |
| major | integer | The major version number. |
| minor | integer | The minor version number. |
| revision | integer | The revision number. |
| sourceRevision | string | A string representation of the SVN revision number. |
| timestamp | string | A timestamp string: format "yyyymmdd-hhmmss |

#### The `HostGroup` object

| Element | Type | Description |
| --- | --- | --- |
| meId | string | The Dynatrace entity ID of the host group. |
| name | string | The name of the Dynatrace entity, displayed in the UI. |

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

#### The `TechnologyInfo` object

| Element | Type | Description |
| --- | --- | --- |
| edition | string | - |
| type | string | - |
| version | string | - |

#### The `TagInfo` object

Tag of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. The element can hold these values * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | The key of the tag.  Custom tags have the tag value here. |
| value | string | The value of the tag.  Not applicable to custom tags. |

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
[



{



"agentVersion": {



"major": 1,



"minor": 1,



"revision": 1,



"sourceRevision": "string",



"timestamp": "string"



},



"amiId": "string",



"autoInjection": "DISABLED_MANUALLY",



"autoScalingGroup": "string",



"awsInstanceId": "string",



"awsInstanceType": "string",



"awsNameTag": "string",



"awsSecurityGroup": [



"string"



],



"azureComputeModeName": "DEDICATED",



"azureEnvironment": "string",



"azureHostNames": [



"string"



],



"azureResourceGroupName": "string",



"azureResourceId": "string",



"azureSiteNames": [



"string"



],



"azureSku": "BASIC",



"azureVmName": "string",



"azureVmScaleSetName": "string",



"azureVmSizeLabel": "string",



"azureZone": "string",



"beanstalkEnvironmentName": "string",



"bitness": "32bit",



"boshAvailabilityZone": "string",



"boshDeploymentId": "string",



"boshInstanceId": "string",



"boshInstanceName": "string",



"boshName": "string",



"boshStemcellVersion": "string",



"cloudPlatformVendorVersion": "string",



"cloudType": "AZURE",



"consumedHostUnits": "string",



"cpuCores": 1,



"customizedName": "string",



"discoveredName": "string",



"displayName": "string",



"entityId": "string",



"esxiHostName": "string",



"firstSeenTimestamp": 1,



"fromRelationships": {



"isNetworkClientOfHost": [



"string"



]



},



"gceInstanceId": "string",



"gceInstanceName": "string",



"gceMachineType": "string",



"gceProject": "string",



"gceProjectId": "string",



"gcePublicIpAddresses": [



"string"



],



"gcpZone": "string",



"hostGroup": {



"meId": "string",



"name": "string"



},



"hypervisorType": "AHV",



"ipAddresses": [



"string"



],



"isMonitoringCandidate": true,



"kubernetesCluster": "string",



"kubernetesLabels": {},



"kubernetesNode": "string",



"lastSeenTimestamp": 1,



"localHostName": "string",



"localIp": "string",



"logicalCpuCores": 1,



"logicalCpus": 1,



"managementZones": [



{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}



],



"monitoringMode": "FULL_STACK",



"networkZoneId": "string",



"oneAgentCustomHostName": "string",



"openStackInstaceType": "string",



"openstackAvZone": "string",



"openstackComputeNodeName": "string",



"openstackProjectName": "string",



"openstackSecurityGroups": [



"string"



],



"openstackVmName": "string",



"osArchitecture": "ARM",



"osType": "AIX",



"osVersion": "string",



"paasAgentVersions": [



{}



],



"paasMemoryLimit": 1,



"paasType": "AWS_ECS_EC2",



"publicHostName": "string",



"publicIp": "string",



"scaleSetName": "string",



"simultaneousMultithreading": 1,



"softwareTechnologies": [



{



"edition": "string",



"type": "string",



"version": "string"



}



],



"tags": [



{



"context": "AWS",



"key": "string",



"value": "string"



}



],



"toRelationships": {



"isNetworkClientOfHost": [



"string"



],



"isProcessOf": [



"string"



],



"isSiteOf": [



"string"



],



"runsOn": [



"string"



]



},



"userLevel": "NON_SUPERUSER",



"virtualCpus": 1,



"vmwareName": "string",



"zosCPUModelNumber": "string",



"zosCPUSerialNumber": "string",



"zosLpaName": "string",



"zosSystemName": "string",



"zosTotalGeneralPurposeProcessors": 1,



"zosTotalPhysicalMemory": 1,



"zosTotalZiipProcessors": 1,



"zosVirtualization": "string"



}



]
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

## Response headers

| Header | Type | Description |
| --- | --- | --- |
| Total-Count | integer | The estimated number of results. |
| Next-Page-Key | string | The cursor for the next page of results. Without it you'll get the first page again. |
| Page-Size | string | The maximum number of results per page. |

## Example

In this example, the request lists all hosts in the environment.

The API token is passed in the **Authorization** header.

The result is truncated to two entries.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/hosts \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/hosts
```

#### Response body

```
[



{



"entityId": "HOST-B7A6F9EE9F366CB5",



"displayName": "tag009",



"discoveredName": "tag009",



"firstSeenTimestamp": 1538473087608,



"lastSeenTimestamp": 1538641647769,



"tags": [



{



"context": "CONTEXTLESS",



"key": "loadtest"



},



{



"context": "CONTEXTLESS",



"key": "host tag"



}



],



"fromRelationships": {



"isNetworkClientOfHost": [



"HOST-80FF8584D8954C1D",



"HOST-A281F848361E79A1"



]



},



"toRelationships": {



"isProcessOf": [



"PROCESS_GROUP_INSTANCE-9146FB8A6A155F93"



],



"isSiteOf": [



"GEOLOC_SITE-F72DF471AE5F56F6"



],



"isNetworkClientOfHost": [



"HOST-80FF8584D8954C1D"



],



"runsOn": [



"PROCESS_GROUP-83D74C22E79B074F"



]



},



"osType": "LINUX",



"osArchitecture": "X86",



"osVersion": "Ubuntu 18.04.1",



"ipAddresses": [



"127.0.0.1",



"192.168.1.1"



],



"bitness": "64bit",



"cpuCores": 4,



"logicalCpuCores": 8,



"consumedHostUnits": 2,



"managementZones": [



{



"id": "6164525246045854296",



"name": "Zone Service E"



},



{



"id": "5678",



"name": "Infrastructure Linux"



}



]



},



{



"entityId": "HOST-2540A456786EEBCA",



"displayName": "RD40",



"discoveredName": "RD40",



"firstSeenTimestamp": 1536455342329,



"lastSeenTimestamp": 1538661752404,



"tags": [



{



"context": "CONTEXTLESS",



"key": "loadtest"



},



],



"fromRelationships": {},



"toRelationships": {



"isProcessOf": [



"PROCESS_GROUP_INSTANCE-0014EF34F2D03461",



"PROCESS_GROUP_INSTANCE-306710DC5239D390"



],



"isSiteOf": [



"GEOLOC_SITE-2D77938DBFF32A41",



"AZURE_REGION-D4D61746B479FE16"



],



"runsOn": [



"PROCESS_GROUP-1527B48A2A57385A",



"PROCESS_GROUP-25544B628ABEDFAB"



]



},



"osType": "WINDOWS",



"osArchitecture": "X86",



"osVersion": "Windows Server 2016 Datacenter",



"hypervisorType": "HYPERV",



"ipAddresses": [



"127.0.0.1"



],



"bitness": "64bit",



"cpuCores": 2,



"logicalCpuCores": 2,



"cloudType": "AZURE",



"paasType": "AZURE_WEBSITES",



"paasMemoryLimit": 3583,



"azureHostNames": [



"contosomomentshkai3q.azurewebsites.net"



],



"azureSiteNames": [



"contosomomentshkai3q"



],



"azureComputeModeName": "DEDICATED",



"azureSku": "STANDARD",



"consumedHostUnits": 0.25,



"managementZones": [



{



"id": "5130731705740636866",



"name": "Windows"



}



]



}



]
```

#### Response code

200

## Related topics

* [Hosts Classic](/docs/observe/infrastructure-observability/hosts "Learn how to get started with host monitoring, understand which measures contribute to host health, how to set up custom host names, and more.")


---


## Source: post-tags.md


---
title: Hosts API - POST tags
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/post-tags
scraped: 2026-02-16T21:19:08.087928
---

# Hosts API - POST tags

# Hosts API - POST tags

* Reference
* Updated on Mar 22, 2023
* Deprecated

Assigns [custom tags](/docs/manage/tags-and-metadata "Learn how to define tags and metadata. Understand how to use tags and metadata to organize your environment.") to the specified host. You only need to provide a tag value. The `CONTEXTLESS` context will be assigned automatically.

The usage of this API is limited to value-only tags. To assign key:value tags, use the [Custom tags API](/docs/dynatrace-api/environment-api/custom-tags/post-tags "Assign custom tags to monitored entities via Dynatrace API.").

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/infrastructure/hosts/{meIdentifier}` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/infrastructure/hosts/{meIdentifier}` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| meIdentifier | string | The Dynatrace entity ID of the host to be updated. | path | Required |
| body | [UpdateEntity](#openapi-definition-UpdateEntity) | A list of tags to be assigned to a Dynatrace entity. | body | Optional |

### Request body objects

#### The `UpdateEntity` object

A list of tags to be assigned to a Dynatrace entity.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| tags | string[] | A list of tags to be assigned to a Dynatrace entity. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"tags": [



"office-linz",



"office-klagenfurt"



]



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The parameters of the host have been updated. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
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

In this example, the request assigns the **Linux** and **Rack 123** tags to the **tag009** host, which has the ID of **HOST-B7A6F9EE9F366CB5**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/hosts/HOST-B7A6F9EE9F366CB5 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"tags": [



"Linux",



"Rack 123"



]



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/hosts/HOST-B7A6F9EE9F366CB5
```

#### Request body

```
{



"tags": [



"iOS app",



"Adnroid app"



]



}
```

#### Response code

204

## Related topics

* [Hosts Classic](/docs/observe/infrastructure-observability/hosts "Learn how to get started with host monitoring, understand which measures contribute to host health, how to set up custom host names, and more.")


---


## Source: get-a-process-group.md


---
title: Process groups API - GET a process group
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/get-a-process-group
scraped: 2026-02-16T21:19:28.580940
---

# Process groups API - GET a process group

# Process groups API - GET a process group

* Reference
* Updated on Mar 22, 2023
* Deprecated

This API is deprecated. Use the [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") instead. You can find more information about switching to the new API in the [migration guide](/docs/dynatrace-api/basics/deprecation-migration-guides/topology-v1-to-entity-v2 "Migrate your automation to the Monitored entities API.").

Gets the parameters of the specified [process group](/docs/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.").

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/infrastructure/process-groups/{meIdentifier}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/infrastructure/process-groups/{meIdentifier}` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| meIdentifier | string | The Dynatrace entity ID of the required process group. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ProcessGroup](#openapi-definition-ProcessGroup) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ProcessGroup` object

Parameters of a process group.

| Element | Type | Description |
| --- | --- | --- |
| azureHostName | string | - |
| azureSiteName | string | - |
| customizedName | string | The customized name of the entity |
| discoveredName | string | The discovered name of the entity |
| displayName | string | The name of the Dynatrace entity as displayed in the UI. |
| entityId | string | The Dynatrace entity ID of the required entity. |
| firstSeenTimestamp | integer | The timestamp of when the entity was first detected, in UTC milliseconds |
| fromRelationships | object | - |
| lastSeenTimestamp | integer | The timestamp of when the entity was last detected, in UTC milliseconds |
| listenPorts | integer[] | - |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | The management zones that the entity is part of. |
| metadata | object | - |
| softwareTechnologies | [TechnologyInfo[]](#openapi-definition-TechnologyInfo) | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | The list of entity tags. |
| toRelationships | object | - |

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

#### The `TechnologyInfo` object

| Element | Type | Description |
| --- | --- | --- |
| edition | string | - |
| type | string | - |
| version | string | - |

#### The `TagInfo` object

Tag of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. The element can hold these values * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | The key of the tag.  Custom tags have the tag value here. |
| value | string | The value of the tag.  Not applicable to custom tags. |

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



"azureHostName": "string",



"azureSiteName": "string",



"customizedName": "string",



"discoveredName": "string",



"displayName": "string",



"entityId": "string",



"firstSeenTimestamp": 1,



"fromRelationships": {



"isNetworkClientOfProcessGroup": [



"string"



],



"runsOn": [



"string"



]



},



"lastSeenTimestamp": 1,



"listenPorts": [



1



],



"managementZones": [



{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}



],



"metadata": {



"adobe.em.env_type": [



"string"



],



"adobe.em.program": [



"string"



],



"adobe.em.service": [



"string"



],



"adobe.em.tier": [



"string"



],



"agentValueMetadata": {},



"apacheConfigPaths": [



"string"



],



"apacheSparkMasterIpAddresses": [



"string"



],



"aspDotNetCoreApplicationPaths": [



"string"



],



"awsEcrImageAccountIds": [



"string"



],



"awsEcrImageRegions": [



"string"



],



"awsEcsCluster": [



"string"



],



"awsEcsContainerARN": [



"string"



],



"awsEcsContainerName": [



"string"



],



"awsEcsDockerID": [



"string"



],



"awsEcsDockerName": [



"string"



],



"awsEcsFamily": [



"string"



],



"awsEcsRevision": [



"string"



],



"awsEcsTaskARN": [



"string"



],



"awsLambdaFunctionNames": [



"string"



],



"awsRegions": [



"string"



],



"azure.containerapp.dnssuffix": [



"string"



],



"azure.containerapp.hostname": [



"string"



],



"azure.containerapp.name": [



"string"



],



"azure.containerapp.replica.name": [



"string"



],



"azure.servicefabric.application.id": [



"string"



],



"azure.servicefabric.application.name": [



"string"



],



"azure.servicefabric.codepackage.name": [



"string"



],



"azure.servicefabric.hostedservice.name": [



"string"



],



"azure.servicefabric.instance.id": [



"string"



],



"azure.servicefabric.replica.id": [



"string"



],



"azure.servicefabric.servicepackage.name": [



"string"



],



"azure.spring.application.name": [



"string"



],



"azure.spring.cloudconfiguri": [



"string"



],



"azure.website.instance.id": [



"string"



],



"azure.website.owner.name": [



"string"



],



"azure.website.site.name": [



"string"



],



"cassandraClusterNames": [



"string"



],



"catalinaBaseValues": [



"string"



],



"catalinaHomeValues": [



"string"



],



"cloudFoundryAppIds": [



"string"



],



"cloudFoundryAppNames": [



"string"



],



"cloudFoundryInstanceIndexes": [



"string"



],



"cloudFoundrySpaceIds": [



"string"



],



"cloudFoundrySpaceNames": [



"string"



],



"cloudfoundryMetadata": {},



"coldfusionJvmConfigFiles": [



"string"



],



"commandLineArgs": [



"string"



],



"datasourceMonitoringConfigId": [



"string"



],



"declarativeConfigRuleId": [



"string"



],



"declarativeId": [



"string"



],



"dockerContainerIds": [



"string"



],



"dockerContainerImageNames": [



"string"



],



"dockerContainerImageVersions": [



"string"



],



"dockerContainerNames": [



"string"



],



"dotNetCommands": [



"string"



],



"dotnetCommandPath": [



"string"



],



"dynatraceClusterIds": [



"string"



],



"dynatraceNodeIds": [



"string"



],



"elasticSearchClusterNames": [



"string"



],



"elasticSearchNodeNames": [



"string"



],



"envVariables": {},



"equinoxConfigPath": [



"string"



],



"executablePaths": [



"string"



],



"executables": [



"string"



],



"glassfishDomainNames": [



"string"



],



"glassfishInstanceNames": [



"string"



],



"google.appengine.version": [



"string"



],



"google.cloudrun.execution": [



"string"



],



"google.cloudrun.job": [



"string"



],



"google.cloudrun.revision": [



"string"



],



"googleAppEngineInstances": [



"string"



],



"googleAppEngineServices": [



"string"



],



"googleCloudInstanceId": [



"string"



],



"googleCloudInstanceRegion": [



"string"



],



"googleCloudProjects": [



"string"



],



"googleCloudRunService": [



"string"



],



"googleComputeEngineMetadata": {},



"heroku.appdefaultdomainname": [



"string"



],



"heroku.dyno": [



"string"



],



"heroku.releaseversion": [



"string"



],



"hostGroups": [



"string"



],



"hybrisBinDirectories": [



"string"



],



"hybrisConfigDirectories": [



"string"



],



"hybrisDataDirectories": [



"string"



],



"ibmApplid": [



"string"



],



"ibmCicsImsApplid": [



"string"



],



"ibmCicsImsJobName": [



"string"



],



"ibmCicsRegion": [



"string"



],



"ibmCtgName": [



"string"



],



"ibmImsConnectRegions": [



"string"



],



"ibmImsControlRegions": [



"string"



],



"ibmImsMessageProcessingRegions": [



"string"



],



"ibmImsSoapGwName": [



"string"



],



"ibmIntegrationNodeName": [



"string"



],



"ibmIntegrationServerName": [



"string"



],



"ibmJobName": [



"string"



],



"iisAppPools": [



"string"



],



"iisRoleNames": [



"string"



],



"javaJarFiles": [



"string"



],



"javaJarPaths": [



"string"



],



"javaMainClasses": [



"string"



],



"javaMainModules": [



"string"



],



"jbossHomes": [



"string"



],



"jbossModes": [



"string"



],



"jbossServerNames": [



"string"



],



"kubernetesAnnotations": {},



"kubernetesBasePodNames": [



"string"



],



"kubernetesClusterId": [



"string"



],



"kubernetesContainerNames": [



"string"



],



"kubernetesFullPodNames": [



"string"



],



"kubernetesNamespaces": [



"string"



],



"kubernetesPodUids": [



"string"



],



"kubernetesRuleResult": [



"string"



],



"linkage": [



"string"



],



"mssqlInstanceName": [



"string"



],



"nodejsAppBaseDirectories": [



"string"



],



"nodejsAppNames": [



"string"



],



"nodejsScriptNames": [



"string"



],



"oracleSid": [



"string"



],



"osagent.groupIdName": [



"string"



],



"osagent.instanceIdName": [



"string"



],



"phpScripts": [



"string"



],



"phpWorkingDirectories": [



"string"



],



"pluginMetadata": {},



"pythonModule": [



"string"



],



"pythonScript": [



"string"



],



"pythonScriptPath": [



"string"



],



"rke2Type": [



"string"



],



"rubyAppRootPaths": [



"string"



],



"rubyScriptPaths": [



"string"



],



"ruleResult": [



"string"



],



"serviceNames": [



"string"



],



"softwareAgInstallRoot": [



"string"



],



"softwareAgProductPropertyName": [



"string"



],



"springBootAppName": [



"string"



],



"springBootProfileName": [



"string"



],



"springBootStartupClass": [



"string"



],



"tibcoBWEnginePropertyFilePaths": [



"string"



],



"tibcoBusinessWorksAppNodeName": [



"string"



],



"tibcoBusinessWorksAppSpaceName": [



"string"



],



"tibcoBusinessWorksCeAppName": [



"string"



],



"tibcoBusinessWorksCeVersion": [



"string"



],



"tibcoBusinessWorksDomainName": [



"string"



],



"tibcoBusinessWorksEnginePropertyFiles": [



"string"



],



"tibcoBusinessWorksHome": [



"string"



],



"varnishInstanceNames": [



"string"



],



"weblogicClusterNames": [



"string"



],



"weblogicDomainNames": [



"string"



],



"weblogicHomeValues": [



"string"



],



"weblogicNames": [



"string"



],



"websphereCellNames": [



"string"



],



"websphereClusterNames": [



"string"



],



"websphereLibertyServerName": [



"string"



],



"websphereNodeNames": [



"string"



],



"websphereServerNames": [



"string"



],



"zCodeModuleVersion": [



"string"



]



},



"softwareTechnologies": [



{



"edition": "string",



"type": "string",



"version": "string"



}



],



"tags": [



{



"context": "AWS",



"key": "string",



"value": "string"



}



],



"toRelationships": {



"isInstanceOf": [



"string"



],



"isNetworkClientOfProcessGroup": [



"string"



],



"runsOn": [



"string"



]



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

In this example, the request gets the details of the **PHP-FPM** process group, which has the ID of **PROCESS\_GROUP-E5C3CC7EC1F80B5B**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X GET \



'https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/process-groups/PROCESS_GROUP-E5C3CC7EC1F80B5B' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/process-groups/PROCESS_GROUP-E5C3CC7EC1F80B5B
```

#### Response body

```
{



"entityId": "PROCESS_GROUP-E5C3CC7EC1F80B5B",



"displayName": "PHP-FPM",



"discoveredName": "PHP-FPM",



"firstSeenTimestamp": 1503909407206,



"lastSeenTimestamp": 1545150389821,



"tags": [],



"fromRelationships": {



"isNetworkClientOfProcessGroup": [



"PROCESS_GROUP-49C926A7091830E3"



],



"runsOn": [



"HOST-249385B2CEBFE51F",



"HOST-890A0495CB619DDF",



"HOST-3FBF48320E4079EF"



]



},



"toRelationships": {



"isInstanceOf": [



"PROCESS_GROUP_INSTANCE-BBFBABB27B2686F2",



"PROCESS_GROUP_INSTANCE-7E988C3503AE8803"



],



"isNetworkClientOfProcessGroup": [



"PROCESS_GROUP-49C926A7091830E3"



],



"runsOn": [



"SERVICE-72503CBDD2AEF066"



]



},



"metadata": {



"hostGroups": [



"authoring"



],



"commandLineArgs": [



"/usr/sbin/php-fpm7.0 --nodaemonize --fpm-config /etc/php/7.0/fpm/php-fpm.conf"



],



"executables": [



"php-fpm7.0"



],



"executablePaths": [



"/usr/sbin/php-fpm7.0"



]



},



"softwareTechnologies": [



{



"type": "SQLITE",



"edition": null,



"version": null



},



{



"type": "PHP",



"edition": "FPM",



"version": "7.0.32"



},



{



"type": "PHP_FPM",



"edition": null,



"version": null



}



]



}
```

#### Response code

200

## Related topics

* [Process groups](/docs/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.")


---


## Source: get-all.md


---
title: Process groups API - GET all process groups
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/get-all
scraped: 2026-02-16T21:19:13.654825
---

# Process groups API - GET all process groups

# Process groups API - GET all process groups

* Reference
* Updated on Mar 22, 2023
* Deprecated

This API is deprecated. Use the [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") instead. You can find more information about switching to the new API in the [migration guide](/docs/dynatrace-api/basics/deprecation-migration-guides/topology-v1-to-entity-v2 "Migrate your automation to the Monitored entities API.").

Gets the list of all [process groups](/docs/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.") in your Dynatrace environment, along with their parameters and relationships.

The full list can be lengthy, so you can narrow it down by specifying filter parameters, like tags. See the **Parameters** section for more details.

You can additionally limit the output by using the pagination:

1. Specify the number of results per page in the **pageSize** query parameter.
2. Then use the cursor from the **Next-Page-Key** response header in the **nextPageKey** query parameter to obtain subsequent pages.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/infrastructure/process-groups` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/infrastructure/process-groups` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The timeframe is restricted to a **maximum period of 3 days**.

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| startTimestamp | integer | The start timestamp of the requested timeframe, in milliseconds (UTC).  If not set, then 72 hours behind from now is used. | query | Optional |
| endTimestamp | integer | The end timestamp of the requested timeframe, in milliseconds (UTC).  If not set, then the current timestamp is used.  The timeframe must not exceed 3 days. | query | Optional |
| relativeTime | string | The relative timeframe, back from now. The element can hold these values * `min` * `5mins` * `10mins` * `15mins` * `30mins` * `hour` * `2hours` * `6hours` * `day` * `3days` | query | Optional |
| tag | string[] | Filters the resulting set of process groups by the specified tag. You can specify several tags in the following format: `tag=tag1&tag=tag2`. The process group has to match **all** the specified tags.  In case of key-value tags, such as imported AWS or CloudFoundry tags, use the following format: `tag=[context]key:value`. For custom key-value tags, omit the context: `tag=key:value`. | query | Optional |
| entity | string[] | Filters result to the specified process groups only.  To specify several process groups use the following format: `entity=ID1&entity=ID2`. | query | Optional |
| host | string[] | Filters process groups by the host they're running at.  Specify Dynatrace IDs of the host you're interested in.  To specify several hosts use the following format: `host=hostID1&host=hostID2`.  The **OR** logic applies. | query | Optional |
| managementZone | integer | Only return process groups that are part of the specified management zone. | query | Optional |
| includeDetails | boolean | Includes (`true`) or excludes (`false`) details which are queried from related entities.  Excluding details may make queries faster.  If not set, then `true` is used. | query | Optional |
| pageSize | integer | The number of process groups per result page.  If not set, pagination is not used and the result contains all process groups fitting the specified filtering criteria. | query | Optional |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **Next-Page-Key** header of the previous response.  If you're using pagination, the first page is always returned without this cursor.  You must keep all other query parameters as they were in the first request to obtain subsequent pages. | query | Optional |

## Response headers

| Header | Type | Description |
| --- | --- | --- |
| Total-Count | integer | The estimated number of results. |
| Next-Page-Key | string | The cursor for the next page of results. Without it you'll get the first page again. |
| Page-Size | string | The maximum number of results per page. |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ProcessGroup[]](#openapi-definition-ProcessGroup) | Success |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ResponseBody` object

#### The `ProcessGroup` object

Parameters of a process group.

| Element | Type | Description |
| --- | --- | --- |
| azureHostName | string | - |
| azureSiteName | string | - |
| customizedName | string | The customized name of the entity |
| discoveredName | string | The discovered name of the entity |
| displayName | string | The name of the Dynatrace entity as displayed in the UI. |
| entityId | string | The Dynatrace entity ID of the required entity. |
| firstSeenTimestamp | integer | The timestamp of when the entity was first detected, in UTC milliseconds |
| fromRelationships | object | - |
| lastSeenTimestamp | integer | The timestamp of when the entity was last detected, in UTC milliseconds |
| listenPorts | integer[] | - |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | The management zones that the entity is part of. |
| metadata | object | - |
| softwareTechnologies | [TechnologyInfo[]](#openapi-definition-TechnologyInfo) | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | The list of entity tags. |
| toRelationships | object | - |

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

#### The `TechnologyInfo` object

| Element | Type | Description |
| --- | --- | --- |
| edition | string | - |
| type | string | - |
| version | string | - |

#### The `TagInfo` object

Tag of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. The element can hold these values * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | The key of the tag.  Custom tags have the tag value here. |
| value | string | The value of the tag.  Not applicable to custom tags. |

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
[



{



"azureHostName": "string",



"azureSiteName": "string",



"customizedName": "string",



"discoveredName": "string",



"displayName": "string",



"entityId": "string",



"firstSeenTimestamp": 1,



"fromRelationships": {



"isNetworkClientOfProcessGroup": [



"string"



],



"runsOn": [



"string"



]



},



"lastSeenTimestamp": 1,



"listenPorts": [



1



],



"managementZones": [



{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}



],



"metadata": {



"adobe.em.env_type": [



"string"



],



"adobe.em.program": [



"string"



],



"adobe.em.service": [



"string"



],



"adobe.em.tier": [



"string"



],



"agentValueMetadata": {},



"apacheConfigPaths": [



"string"



],



"apacheSparkMasterIpAddresses": [



"string"



],



"aspDotNetCoreApplicationPaths": [



"string"



],



"awsEcrImageAccountIds": [



"string"



],



"awsEcrImageRegions": [



"string"



],



"awsEcsCluster": [



"string"



],



"awsEcsContainerARN": [



"string"



],



"awsEcsContainerName": [



"string"



],



"awsEcsDockerID": [



"string"



],



"awsEcsDockerName": [



"string"



],



"awsEcsFamily": [



"string"



],



"awsEcsRevision": [



"string"



],



"awsEcsTaskARN": [



"string"



],



"awsLambdaFunctionNames": [



"string"



],



"awsRegions": [



"string"



],



"azure.containerapp.dnssuffix": [



"string"



],



"azure.containerapp.hostname": [



"string"



],



"azure.containerapp.name": [



"string"



],



"azure.containerapp.replica.name": [



"string"



],



"azure.servicefabric.application.id": [



"string"



],



"azure.servicefabric.application.name": [



"string"



],



"azure.servicefabric.codepackage.name": [



"string"



],



"azure.servicefabric.hostedservice.name": [



"string"



],



"azure.servicefabric.instance.id": [



"string"



],



"azure.servicefabric.replica.id": [



"string"



],



"azure.servicefabric.servicepackage.name": [



"string"



],



"azure.spring.application.name": [



"string"



],



"azure.spring.cloudconfiguri": [



"string"



],



"azure.website.instance.id": [



"string"



],



"azure.website.owner.name": [



"string"



],



"azure.website.site.name": [



"string"



],



"cassandraClusterNames": [



"string"



],



"catalinaBaseValues": [



"string"



],



"catalinaHomeValues": [



"string"



],



"cloudFoundryAppIds": [



"string"



],



"cloudFoundryAppNames": [



"string"



],



"cloudFoundryInstanceIndexes": [



"string"



],



"cloudFoundrySpaceIds": [



"string"



],



"cloudFoundrySpaceNames": [



"string"



],



"cloudfoundryMetadata": {},



"coldfusionJvmConfigFiles": [



"string"



],



"commandLineArgs": [



"string"



],



"datasourceMonitoringConfigId": [



"string"



],



"declarativeConfigRuleId": [



"string"



],



"declarativeId": [



"string"



],



"dockerContainerIds": [



"string"



],



"dockerContainerImageNames": [



"string"



],



"dockerContainerImageVersions": [



"string"



],



"dockerContainerNames": [



"string"



],



"dotNetCommands": [



"string"



],



"dotnetCommandPath": [



"string"



],



"dynatraceClusterIds": [



"string"



],



"dynatraceNodeIds": [



"string"



],



"elasticSearchClusterNames": [



"string"



],



"elasticSearchNodeNames": [



"string"



],



"envVariables": {},



"equinoxConfigPath": [



"string"



],



"executablePaths": [



"string"



],



"executables": [



"string"



],



"glassfishDomainNames": [



"string"



],



"glassfishInstanceNames": [



"string"



],



"google.appengine.version": [



"string"



],



"google.cloudrun.execution": [



"string"



],



"google.cloudrun.job": [



"string"



],



"google.cloudrun.revision": [



"string"



],



"googleAppEngineInstances": [



"string"



],



"googleAppEngineServices": [



"string"



],



"googleCloudInstanceId": [



"string"



],



"googleCloudInstanceRegion": [



"string"



],



"googleCloudProjects": [



"string"



],



"googleCloudRunService": [



"string"



],



"googleComputeEngineMetadata": {},



"heroku.appdefaultdomainname": [



"string"



],



"heroku.dyno": [



"string"



],



"heroku.releaseversion": [



"string"



],



"hostGroups": [



"string"



],



"hybrisBinDirectories": [



"string"



],



"hybrisConfigDirectories": [



"string"



],



"hybrisDataDirectories": [



"string"



],



"ibmApplid": [



"string"



],



"ibmCicsImsApplid": [



"string"



],



"ibmCicsImsJobName": [



"string"



],



"ibmCicsRegion": [



"string"



],



"ibmCtgName": [



"string"



],



"ibmImsConnectRegions": [



"string"



],



"ibmImsControlRegions": [



"string"



],



"ibmImsMessageProcessingRegions": [



"string"



],



"ibmImsSoapGwName": [



"string"



],



"ibmIntegrationNodeName": [



"string"



],



"ibmIntegrationServerName": [



"string"



],



"ibmJobName": [



"string"



],



"iisAppPools": [



"string"



],



"iisRoleNames": [



"string"



],



"javaJarFiles": [



"string"



],



"javaJarPaths": [



"string"



],



"javaMainClasses": [



"string"



],



"javaMainModules": [



"string"



],



"jbossHomes": [



"string"



],



"jbossModes": [



"string"



],



"jbossServerNames": [



"string"



],



"kubernetesAnnotations": {},



"kubernetesBasePodNames": [



"string"



],



"kubernetesClusterId": [



"string"



],



"kubernetesContainerNames": [



"string"



],



"kubernetesFullPodNames": [



"string"



],



"kubernetesNamespaces": [



"string"



],



"kubernetesPodUids": [



"string"



],



"kubernetesRuleResult": [



"string"



],



"linkage": [



"string"



],



"mssqlInstanceName": [



"string"



],



"nodejsAppBaseDirectories": [



"string"



],



"nodejsAppNames": [



"string"



],



"nodejsScriptNames": [



"string"



],



"oracleSid": [



"string"



],



"osagent.groupIdName": [



"string"



],



"osagent.instanceIdName": [



"string"



],



"phpScripts": [



"string"



],



"phpWorkingDirectories": [



"string"



],



"pluginMetadata": {},



"pythonModule": [



"string"



],



"pythonScript": [



"string"



],



"pythonScriptPath": [



"string"



],



"rke2Type": [



"string"



],



"rubyAppRootPaths": [



"string"



],



"rubyScriptPaths": [



"string"



],



"ruleResult": [



"string"



],



"serviceNames": [



"string"



],



"softwareAgInstallRoot": [



"string"



],



"softwareAgProductPropertyName": [



"string"



],



"springBootAppName": [



"string"



],



"springBootProfileName": [



"string"



],



"springBootStartupClass": [



"string"



],



"tibcoBWEnginePropertyFilePaths": [



"string"



],



"tibcoBusinessWorksAppNodeName": [



"string"



],



"tibcoBusinessWorksAppSpaceName": [



"string"



],



"tibcoBusinessWorksCeAppName": [



"string"



],



"tibcoBusinessWorksCeVersion": [



"string"



],



"tibcoBusinessWorksDomainName": [



"string"



],



"tibcoBusinessWorksEnginePropertyFiles": [



"string"



],



"tibcoBusinessWorksHome": [



"string"



],



"varnishInstanceNames": [



"string"



],



"weblogicClusterNames": [



"string"



],



"weblogicDomainNames": [



"string"



],



"weblogicHomeValues": [



"string"



],



"weblogicNames": [



"string"



],



"websphereCellNames": [



"string"



],



"websphereClusterNames": [



"string"



],



"websphereLibertyServerName": [



"string"



],



"websphereNodeNames": [



"string"



],



"websphereServerNames": [



"string"



],



"zCodeModuleVersion": [



"string"



]



},



"softwareTechnologies": [



{



"edition": "string",



"type": "string",



"version": "string"



}



],



"tags": [



{



"context": "AWS",



"key": "string",



"value": "string"



}



],



"toRelationships": {



"isInstanceOf": [



"string"



],



"isNetworkClientOfProcessGroup": [



"string"



],



"runsOn": [



"string"



]



}



}



]
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

In this example, the request lists all the process groups of the environment detected **within the last 5 minutes**.

The API token is passed in the **Authorization** header.

The result is truncated to two entries.

#### Curl

```
curl -X GET \



'https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/process-groups?relativeTime=5mins' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/process-groups?relativeTime=5mins
```

#### Response body

```
[



{



"entityId": "PROCESS_GROUP-B34081EFF9E5F516",



"displayName": "Apache Web Server apache2",



"discoveredName": "Apache Web Server apache2",



"firstSeenTimestamp": 1405316247660,



"lastSeenTimestamp": 1545149212556,



"tags": [],



"fromRelationships": {},



"toRelationships": {



"runsOn": [



"SERVICE-B8C88BAA442098CF"



]



},



"metadata": {



"commandLineArgs": [



"/usr/sbin/apache2 -k start"



],



"executables": [



"apache2"



],



"executablePaths": [



"/usr/sbin/apache2"



],



"apacheConfigPaths": [



"/etc/apache2/apache2.conf"



]



},



"softwareTechnologies": [



{



"type": "PHP",



"edition": "Apache",



"version": "5.5.9"



},



{



"type": "APACHE_HTTPD",



"edition": null,



"version": "2.4.7"



},



{



"type": "SQLITE",



"edition": null,



"version": null



}



]



},



{



"entityId": "PROCESS_GROUP-E5C3CC7EC1F80B5B",



"displayName": "PHP-FPM",



"discoveredName": "PHP-FPM",



"firstSeenTimestamp": 1503909407206,



"lastSeenTimestamp": 1545149349700,



"tags": [],



"fromRelationships": {



"runsOn": [



"HOST-74CDC8809AD43931",



"HOST-9A81EACCA0270218"



]



},



"toRelationships": {



"isInstanceOf": [



"PROCESS_GROUP_INSTANCE-7E988C3503AE8803"



],



"isNetworkClientOfProcessGroup": [



"PROCESS_GROUP-49C926A7091830E3"



],



"runsOn": [



"SERVICE-72503CBDD2AEF066"



]



},



"metadata": {



"hostGroups": [



"authoring"



],



"commandLineArgs": [



"/usr/sbin/php-fpm7.0 --nodaemonize --fpm-config /etc/php/7.0/fpm/php-fpm.conf"



],



"executables": [



"php-fpm7.0"



],



"executablePaths": [



"/usr/sbin/php-fpm7.0"



]



},



"softwareTechnologies": [



{



"type": "SQLITE",



"edition": null,



"version": null



},



{



"type": "PHP",



"edition": "FPM",



"version": "7.0.32"



},



{



"type": "PHP_FPM",



"edition": null,



"version": null



}



]



}



]
```

#### Response code

200

## Related topics

* [Process groups](/docs/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.")


---


## Source: post-tags.md


---
title: Process groups API - POST tags
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/post-tags
scraped: 2026-02-16T21:19:11.671621
---

# Process groups API - POST tags

# Process groups API - POST tags

* Reference
* Updated on Mar 22, 2023
* Deprecated

Assigns [custom tags](/docs/manage/tags-and-metadata "Learn how to define tags and metadata. Understand how to use tags and metadata to organize your environment.") to the specified [process group](/docs/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring."). You need only provide a tag value. The `CONTEXTLESS` context will be assigned automatically.

The usage of this API is limited to value-only tags. To assign key:value tags, use the [Custom tags API](/docs/dynatrace-api/environment-api/custom-tags/post-tags "Assign custom tags to monitored entities via Dynatrace API.").

The request produces an `application/json`

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/infrastructure/process-groups/{meIdentifier}` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/infrastructure/process-groups/{meIdentifier}` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| meIdentifier | string | The Dynatrace entity ID of the process group to be updated. | path | Required |
| body | [UpdateEntity](#openapi-definition-UpdateEntity) | The JSON body of the request. Contains tags to be added to the process group. | body | Optional |

### Request body objects

#### The `UpdateEntity` object

A list of tags to be assigned to a Dynatrace entity.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| tags | string[] | A list of tags to be assigned to a Dynatrace entity. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"tags": [



"office-linz",



"office-klagenfurt"



]



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The parameters of the process group have been updated. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
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

In this example, the request assigns the **PHP** tag to the **PHP-FPM** process group, which has the ID of **PROCESS\_GROUP-E5C3CC7EC1F80B5B**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/process-groups/PROCESS_GROUP-E5C3CC7EC1F80B5B \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"tags": [



"PHP"



]



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/process-groups/PROCESS_GROUP-E5C3CC7EC1F80B5B
```

#### Request body

```
{



"tags": [



"PHP"



]



}
```

#### Response code

204

## Related topics

* [Process groups](/docs/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.")


---


## Source: get-a-process.md


---
title: Processes API - GET a process
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/processes-api/get-a-process
scraped: 2026-02-16T21:18:58.622088
---

# Processes API - GET a process

# Processes API - GET a process

* Reference
* Updated on Mar 22, 2023
* Deprecated

This API is deprecated. Use the [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") instead. You can find more information about switching to the new API in the [migration guide](/docs/dynatrace-api/basics/deprecation-migration-guides/topology-v1-to-entity-v2 "Migrate your automation to the Monitored entities API.").

Gets the parameters of the specified [process](/docs/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.").

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/infrastructure/processes/{meIdentifier}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/infrastructure/processes/{meIdentifier}` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| meIdentifier | string | The Dynatrace entity ID of the required process. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ProcessGroupInstance](#openapi-definition-ProcessGroupInstance) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ProcessGroupInstance` object

Parameters of a process.

| Element | Type | Description |
| --- | --- | --- |
| agentVersions | [AgentVersion[]](#openapi-definition-AgentVersion) | Versions of OneAgents currently running on the entity. |
| azureHostName | string | - |
| azureSiteName | string | - |
| bitness | string | -The element can hold these values * `32bit` * `64bit` |
| customizedName | string | The customized name of the entity |
| discoveredName | string | The discovered name of the entity |
| displayName | string | The name of the Dynatrace entity as displayed in the UI. |
| entityId | string | The Dynatrace entity ID of the required entity. |
| firstSeenTimestamp | integer | The timestamp of when the entity was first detected, in UTC milliseconds |
| fromRelationships | object | - |
| lastSeenTimestamp | integer | The timestamp of when the entity was last detected, in UTC milliseconds |
| listenPorts | integer[] | - |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | The management zones that the entity is part of. |
| metadata | object | - |
| modules | string[] | - |
| monitoringState | [MonitoringState](#openapi-definition-MonitoringState) | Defines the current monitoring state of an entity. |
| softwareTechnologies | [TechnologyInfo[]](#openapi-definition-TechnologyInfo) | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | The list of entity tags. |
| toRelationships | object | - |
| versionedModules | [ProcessGroupInstanceModule[]](#openapi-definition-ProcessGroupInstanceModule) | - |

#### The `AgentVersion` object

Defines the version of the agent currently running on the entity.

| Element | Type | Description |
| --- | --- | --- |
| major | integer | The major version number. |
| minor | integer | The minor version number. |
| revision | integer | The revision number. |
| sourceRevision | string | A string representation of the SVN revision number. |
| timestamp | string | A timestamp string: format "yyyymmdd-hhmmss |

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

#### The `MonitoringState` object

Defines the current monitoring state of an entity.

| Element | Type | Description |
| --- | --- | --- |
| actualMonitoringState | string | The current actual monitoring state on the entity. The element can hold these values * `OFF` * `ON` |
| expectedMonitoringState | string | The monitoring state that is expected from the configuration The element can hold these values * `OFF` * `ON` |
| restartRequired | boolean | Defines whether or not the process has to restarted to enable monitoring |

#### The `TechnologyInfo` object

| Element | Type | Description |
| --- | --- | --- |
| edition | string | - |
| type | string | - |
| version | string | - |

#### The `TagInfo` object

Tag of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. The element can hold these values * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | The key of the tag.  Custom tags have the tag value here. |
| value | string | The value of the tag.  Not applicable to custom tags. |

#### The `ProcessGroupInstanceModule` object

| Element | Type | Description |
| --- | --- | --- |
| name | string | - |
| version | string | - |

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



"agentVersions": [



{



"major": 1,



"minor": 1,



"revision": 1,



"sourceRevision": "string",



"timestamp": "string"



}



],



"azureHostName": "string",



"azureSiteName": "string",



"bitness": "32bit",



"customizedName": "string",



"discoveredName": "string",



"displayName": "string",



"entityId": "string",



"firstSeenTimestamp": 1,



"fromRelationships": {



"isInstanceOf": [



"string"



],



"isNetworkClientOf": [



"string"



],



"isProcessOf": [



"string"



]



},



"lastSeenTimestamp": 1,



"listenPorts": [



1



],



"managementZones": [



{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}



],



"metadata": {



"adobe.em.env_type": [



"string"



],



"adobe.em.program": [



"string"



],



"adobe.em.service": [



"string"



],



"adobe.em.tier": [



"string"



],



"agentValueMetadata": {},



"apacheConfigPaths": [



"string"



],



"apacheSparkMasterIpAddresses": [



"string"



],



"aspDotNetCoreApplicationPaths": [



"string"



],



"awsEcrImageAccountIds": [



"string"



],



"awsEcrImageRegions": [



"string"



],



"awsEcsCluster": [



"string"



],



"awsEcsContainerARN": [



"string"



],



"awsEcsContainerName": [



"string"



],



"awsEcsDockerID": [



"string"



],



"awsEcsDockerName": [



"string"



],



"awsEcsFamily": [



"string"



],



"awsEcsRevision": [



"string"



],



"awsEcsTaskARN": [



"string"



],



"awsLambdaFunctionNames": [



"string"



],



"awsRegions": [



"string"



],



"azure.containerapp.dnssuffix": [



"string"



],



"azure.containerapp.hostname": [



"string"



],



"azure.containerapp.name": [



"string"



],



"azure.containerapp.replica.name": [



"string"



],



"azure.servicefabric.application.id": [



"string"



],



"azure.servicefabric.application.name": [



"string"



],



"azure.servicefabric.codepackage.name": [



"string"



],



"azure.servicefabric.hostedservice.name": [



"string"



],



"azure.servicefabric.instance.id": [



"string"



],



"azure.servicefabric.replica.id": [



"string"



],



"azure.servicefabric.servicepackage.name": [



"string"



],



"azure.spring.application.name": [



"string"



],



"azure.spring.cloudconfiguri": [



"string"



],



"azure.website.instance.id": [



"string"



],



"azure.website.owner.name": [



"string"



],



"azure.website.site.name": [



"string"



],



"cassandraClusterNames": [



"string"



],



"catalinaBaseValues": [



"string"



],



"catalinaHomeValues": [



"string"



],



"cloudFoundryAppIds": [



"string"



],



"cloudFoundryAppNames": [



"string"



],



"cloudFoundryInstanceIndexes": [



"string"



],



"cloudFoundrySpaceIds": [



"string"



],



"cloudFoundrySpaceNames": [



"string"



],



"cloudfoundryMetadata": {},



"coldfusionJvmConfigFiles": [



"string"



],



"commandLineArgs": [



"string"



],



"datasourceMonitoringConfigId": [



"string"



],



"declarativeConfigRuleId": [



"string"



],



"declarativeId": [



"string"



],



"dockerContainerIds": [



"string"



],



"dockerContainerImageNames": [



"string"



],



"dockerContainerImageVersions": [



"string"



],



"dockerContainerNames": [



"string"



],



"dotNetCommands": [



"string"



],



"dotnetCommandPath": [



"string"



],



"dynatraceClusterIds": [



"string"



],



"dynatraceNodeIds": [



"string"



],



"elasticSearchClusterNames": [



"string"



],



"elasticSearchNodeNames": [



"string"



],



"envVariables": {},



"equinoxConfigPath": [



"string"



],



"executablePaths": [



"string"



],



"executables": [



"string"



],



"glassfishDomainNames": [



"string"



],



"glassfishInstanceNames": [



"string"



],



"google.appengine.version": [



"string"



],



"google.cloudrun.execution": [



"string"



],



"google.cloudrun.job": [



"string"



],



"google.cloudrun.revision": [



"string"



],



"googleAppEngineInstances": [



"string"



],



"googleAppEngineServices": [



"string"



],



"googleCloudInstanceId": [



"string"



],



"googleCloudInstanceRegion": [



"string"



],



"googleCloudProjects": [



"string"



],



"googleCloudRunService": [



"string"



],



"googleComputeEngineMetadata": {},



"heroku.appdefaultdomainname": [



"string"



],



"heroku.dyno": [



"string"



],



"heroku.releaseversion": [



"string"



],



"hostGroups": [



"string"



],



"hybrisBinDirectories": [



"string"



],



"hybrisConfigDirectories": [



"string"



],



"hybrisDataDirectories": [



"string"



],



"ibmApplid": [



"string"



],



"ibmCicsImsApplid": [



"string"



],



"ibmCicsImsJobName": [



"string"



],



"ibmCicsRegion": [



"string"



],



"ibmCtgName": [



"string"



],



"ibmImsConnectRegions": [



"string"



],



"ibmImsControlRegions": [



"string"



],



"ibmImsMessageProcessingRegions": [



"string"



],



"ibmImsSoapGwName": [



"string"



],



"ibmIntegrationNodeName": [



"string"



],



"ibmIntegrationServerName": [



"string"



],



"ibmJobName": [



"string"



],



"iisAppPools": [



"string"



],



"iisRoleNames": [



"string"



],



"javaJarFiles": [



"string"



],



"javaJarPaths": [



"string"



],



"javaMainClasses": [



"string"



],



"javaMainModules": [



"string"



],



"jbossHomes": [



"string"



],



"jbossModes": [



"string"



],



"jbossServerNames": [



"string"



],



"kubernetesAnnotations": {},



"kubernetesBasePodNames": [



"string"



],



"kubernetesClusterId": [



"string"



],



"kubernetesContainerNames": [



"string"



],



"kubernetesFullPodNames": [



"string"



],



"kubernetesNamespaces": [



"string"



],



"kubernetesPodUids": [



"string"



],



"kubernetesRuleResult": [



"string"



],



"linkage": [



"string"



],



"mssqlInstanceName": [



"string"



],



"nodejsAppBaseDirectories": [



"string"



],



"nodejsAppNames": [



"string"



],



"nodejsScriptNames": [



"string"



],



"oracleSid": [



"string"



],



"osagent.groupIdName": [



"string"



],



"osagent.instanceIdName": [



"string"



],



"phpScripts": [



"string"



],



"phpWorkingDirectories": [



"string"



],



"pluginMetadata": {},



"pythonModule": [



"string"



],



"pythonScript": [



"string"



],



"pythonScriptPath": [



"string"



],



"rke2Type": [



"string"



],



"rubyAppRootPaths": [



"string"



],



"rubyScriptPaths": [



"string"



],



"ruleResult": [



"string"



],



"serviceNames": [



"string"



],



"softwareAgInstallRoot": [



"string"



],



"softwareAgProductPropertyName": [



"string"



],



"springBootAppName": [



"string"



],



"springBootProfileName": [



"string"



],



"springBootStartupClass": [



"string"



],



"tibcoBWEnginePropertyFilePaths": [



"string"



],



"tibcoBusinessWorksAppNodeName": [



"string"



],



"tibcoBusinessWorksAppSpaceName": [



"string"



],



"tibcoBusinessWorksCeAppName": [



"string"



],



"tibcoBusinessWorksCeVersion": [



"string"



],



"tibcoBusinessWorksDomainName": [



"string"



],



"tibcoBusinessWorksEnginePropertyFiles": [



"string"



],



"tibcoBusinessWorksHome": [



"string"



],



"varnishInstanceNames": [



"string"



],



"weblogicClusterNames": [



"string"



],



"weblogicDomainNames": [



"string"



],



"weblogicHomeValues": [



"string"



],



"weblogicNames": [



"string"



],



"websphereCellNames": [



"string"



],



"websphereClusterNames": [



"string"



],



"websphereLibertyServerName": [



"string"



],



"websphereNodeNames": [



"string"



],



"websphereServerNames": [



"string"



],



"zCodeModuleVersion": [



"string"



]



},



"modules": [



"string"



],



"monitoringState": {



"actualMonitoringState": "OFF",



"expectedMonitoringState": "OFF",



"restartRequired": true



},



"softwareTechnologies": [



{



"edition": "string",



"type": "string",



"version": "string"



}



],



"tags": [



{



"context": "AWS",



"key": "string",



"value": "string"



}



],



"toRelationships": {



"isNetworkClientOf": [



"string"



],



"runsOnProcessGroupInstance": [



"string"



]



},



"versionedModules": [



{



"name": "string",



"version": "string"



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

In this example, the request gets the details of the **Apache Web Server apache2** process, which has the ID of **PROCESS\_GROUP\_INSTANCE-EC9688429EB24B6B**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/processes/PROCESS_GROUP_INSTANCE-EC9688429EB24B6B \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/processes/PROCESS_GROUP_INSTANCE-EC9688429EB24B6B
```

#### Response body

```
{



"entityId": "PROCESS_GROUP_INSTANCE-EC9688429EB24B6B",



"displayName": "Apache Web Server apache2",



"discoveredName": "Apache Web Server apache2",



"firstSeenTimestamp": 1464951001104,



"lastSeenTimestamp": 1545147232609,



"tags": [],



"fromRelationships": {



"isProcessOf": [



"HOST-5FD609AD6757BE7D"



],



"isInstanceOf": [



"PROCESS_GROUP-B34081EFF9E5F516"



]



},



"toRelationships": {



"runsOnProcessGroupInstance": [



"SERVICE-C3173FEB08025322",



"SERVICE-443EACA6DCAEE651",



"SERVICE-B8C88BAA442098CF"



]



},



"metadata": {



"commandLineArgs": [



"/usr/sbin/apache2 -k start"



],



"executables": [



"apache2"



],



"executablePaths": [



"/usr/sbin/apache2"



],



"apacheConfigPaths": [



"/etc/apache2/apache2.conf"



]



},



"softwareTechnologies": [



{



"type": "PHP",



"edition": "Apache",



"version": "5.5.9"



},



{



"type": "APACHE_HTTPD",



"edition": null,



"version": "2.4.7"



},



{



"type": "SQLITE",



"edition": null,



"version": null



}



],



"listenPorts": [



80,



443



],



"bitness": "64bit",



"modules": [



"mod_auth_basic.c",



"mod_authn_file.c",



"mod_negotiation.c",



"mod_dir.c",



"mod_rewrite.c"



],



"monitoringState": {



"actualMonitoringState": "ON",



"expectedMonitoringState": "ON",



"restartRequired": false



},



"agentVersions": [



{



"major": 1,



"minor": 157,



"revision": 210,



"timestamp": "20181213-075558",



"sourceRevision": ""



}



]



}
```

#### Response code

200

## Related topics

* [Process groups](/docs/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.")


---


## Source: get-all.md


---
title: Processes API - GET all processes
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/processes-api/get-all
scraped: 2026-02-16T21:19:10.202601
---

# Processes API - GET all processes

# Processes API - GET all processes

* Reference
* Updated on Mar 22, 2023
* Deprecated

This API is deprecated. Use the [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") instead. You can find more information about switching to the new API in the [migration guide](/docs/dynatrace-api/basics/deprecation-migration-guides/topology-v1-to-entity-v2 "Migrate your automation to the Monitored entities API.").

Fetches the list of all [processes](/docs/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.") in your Dynatrace environment, along with their parameters and relationships.

The full list can be lengthy, so you can narrow it down by specifying filter parameters, like tags. See the **Parameters** section for more details.

You can additionally limit the output by using the pagination:

1. Specify the number of results per page in the **pageSize** query parameter.
2. Then use the cursor from the **Next-Page-Key** response header in the **nextPageKey** query parameter to obtain subsequent pages.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/infrastructure/processes` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/infrastructure/processes` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The timeframe is restricted to a **maximum period of 3 days**.

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| startTimestamp | integer | The start timestamp of the requested timeframe, in milliseconds (UTC).  If not set, then 72 hours behind from now is used. | query | Optional |
| endTimestamp | integer | The end timestamp of the requested timeframe, in milliseconds (UTC).  If not set, then the current timestamp is used.  The timeframe must not exceed 3 days. | query | Optional |
| relativeTime | string | The relative timeframe, back from now. The element can hold these values * `min` * `5mins` * `10mins` * `15mins` * `30mins` * `hour` * `2hours` * `6hours` * `day` * `3days` | query | Optional |
| tag | string[] | Filters the resulting set of processes by the specified tag. You can specify several tags in the following format: `tag=tag1&tag=tag2`. The process has to match **all** the specified tags.  In case of key-value tags, such as imported AWS or CloudFoundry tags, use the following format: `tag=[context]key:value`. For custom key-value tags, omit the context: `tag=key:value`. | query | Optional |
| entity | string[] | Filters result to the specified processes only.  To specify several processes use the following format: `entity=ID1&entity=ID2`. | query | Optional |
| hostTag | string[] | Filters processes by the host they're running at.  Specify tags of the host you're interested in. | query | Optional |
| host | string[] | Filters processes by the host they're running at.  Specify Dynatrace IDs of the host you're interested in.  To specify several hosts use the following format: `host=hostID1&host=hostID2`.  The **OR** logic applies. | query | Optional |
| actualMonitoringState | string | Filters processes by the actual monitoring state of the process. The element can hold these values * `OFF` * `ON` | query | Optional |
| expectedMonitoringState | string | Filters processes by the expected monitoring state of the process. The element can hold these values * `OFF` * `ON` | query | Optional |
| managementZone | integer | Only return processes that are part of the specified management zone. | query | Optional |
| includeDetails | boolean | Includes (`true`) or excludes (`false`) details which are queried from related entities.  Excluding details may make queries faster.  If not set, then `true` is used. | query | Optional |
| pageSize | integer | The number of processes per result page.  If not set, pagination is not used and the result contains all processes fitting the specified filtering criteria. | query | Optional |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **Next-Page-Key** header of the previous response.  If you're using pagination, the first page is always returned without this cursor.  You must keep all other query parameters as they were in the first request to obtain subsequent pages. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ProcessGroupInstance[]](#openapi-definition-ProcessGroupInstance) | Success |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ResponseBody` object

#### The `ProcessGroupInstance` object

Parameters of a process.

| Element | Type | Description |
| --- | --- | --- |
| agentVersions | [AgentVersion[]](#openapi-definition-AgentVersion) | Versions of OneAgents currently running on the entity. |
| azureHostName | string | - |
| azureSiteName | string | - |
| bitness | string | -The element can hold these values * `32bit` * `64bit` |
| customizedName | string | The customized name of the entity |
| discoveredName | string | The discovered name of the entity |
| displayName | string | The name of the Dynatrace entity as displayed in the UI. |
| entityId | string | The Dynatrace entity ID of the required entity. |
| firstSeenTimestamp | integer | The timestamp of when the entity was first detected, in UTC milliseconds |
| fromRelationships | object | - |
| lastSeenTimestamp | integer | The timestamp of when the entity was last detected, in UTC milliseconds |
| listenPorts | integer[] | - |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | The management zones that the entity is part of. |
| metadata | object | - |
| modules | string[] | - |
| monitoringState | [MonitoringState](#openapi-definition-MonitoringState) | Defines the current monitoring state of an entity. |
| softwareTechnologies | [TechnologyInfo[]](#openapi-definition-TechnologyInfo) | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | The list of entity tags. |
| toRelationships | object | - |
| versionedModules | [ProcessGroupInstanceModule[]](#openapi-definition-ProcessGroupInstanceModule) | - |

#### The `AgentVersion` object

Defines the version of the agent currently running on the entity.

| Element | Type | Description |
| --- | --- | --- |
| major | integer | The major version number. |
| minor | integer | The minor version number. |
| revision | integer | The revision number. |
| sourceRevision | string | A string representation of the SVN revision number. |
| timestamp | string | A timestamp string: format "yyyymmdd-hhmmss |

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

#### The `MonitoringState` object

Defines the current monitoring state of an entity.

| Element | Type | Description |
| --- | --- | --- |
| actualMonitoringState | string | The current actual monitoring state on the entity. The element can hold these values * `OFF` * `ON` |
| expectedMonitoringState | string | The monitoring state that is expected from the configuration The element can hold these values * `OFF` * `ON` |
| restartRequired | boolean | Defines whether or not the process has to restarted to enable monitoring |

#### The `TechnologyInfo` object

| Element | Type | Description |
| --- | --- | --- |
| edition | string | - |
| type | string | - |
| version | string | - |

#### The `TagInfo` object

Tag of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. The element can hold these values * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | The key of the tag.  Custom tags have the tag value here. |
| value | string | The value of the tag.  Not applicable to custom tags. |

#### The `ProcessGroupInstanceModule` object

| Element | Type | Description |
| --- | --- | --- |
| name | string | - |
| version | string | - |

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
[



{



"agentVersions": [



{



"major": 1,



"minor": 1,



"revision": 1,



"sourceRevision": "string",



"timestamp": "string"



}



],



"azureHostName": "string",



"azureSiteName": "string",



"bitness": "32bit",



"customizedName": "string",



"discoveredName": "string",



"displayName": "string",



"entityId": "string",



"firstSeenTimestamp": 1,



"fromRelationships": {



"isInstanceOf": [



"string"



],



"isNetworkClientOf": [



"string"



],



"isProcessOf": [



"string"



]



},



"lastSeenTimestamp": 1,



"listenPorts": [



1



],



"managementZones": [



{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}



],



"metadata": {



"adobe.em.env_type": [



"string"



],



"adobe.em.program": [



"string"



],



"adobe.em.service": [



"string"



],



"adobe.em.tier": [



"string"



],



"agentValueMetadata": {},



"apacheConfigPaths": [



"string"



],



"apacheSparkMasterIpAddresses": [



"string"



],



"aspDotNetCoreApplicationPaths": [



"string"



],



"awsEcrImageAccountIds": [



"string"



],



"awsEcrImageRegions": [



"string"



],



"awsEcsCluster": [



"string"



],



"awsEcsContainerARN": [



"string"



],



"awsEcsContainerName": [



"string"



],



"awsEcsDockerID": [



"string"



],



"awsEcsDockerName": [



"string"



],



"awsEcsFamily": [



"string"



],



"awsEcsRevision": [



"string"



],



"awsEcsTaskARN": [



"string"



],



"awsLambdaFunctionNames": [



"string"



],



"awsRegions": [



"string"



],



"azure.containerapp.dnssuffix": [



"string"



],



"azure.containerapp.hostname": [



"string"



],



"azure.containerapp.name": [



"string"



],



"azure.containerapp.replica.name": [



"string"



],



"azure.servicefabric.application.id": [



"string"



],



"azure.servicefabric.application.name": [



"string"



],



"azure.servicefabric.codepackage.name": [



"string"



],



"azure.servicefabric.hostedservice.name": [



"string"



],



"azure.servicefabric.instance.id": [



"string"



],



"azure.servicefabric.replica.id": [



"string"



],



"azure.servicefabric.servicepackage.name": [



"string"



],



"azure.spring.application.name": [



"string"



],



"azure.spring.cloudconfiguri": [



"string"



],



"azure.website.instance.id": [



"string"



],



"azure.website.owner.name": [



"string"



],



"azure.website.site.name": [



"string"



],



"cassandraClusterNames": [



"string"



],



"catalinaBaseValues": [



"string"



],



"catalinaHomeValues": [



"string"



],



"cloudFoundryAppIds": [



"string"



],



"cloudFoundryAppNames": [



"string"



],



"cloudFoundryInstanceIndexes": [



"string"



],



"cloudFoundrySpaceIds": [



"string"



],



"cloudFoundrySpaceNames": [



"string"



],



"cloudfoundryMetadata": {},



"coldfusionJvmConfigFiles": [



"string"



],



"commandLineArgs": [



"string"



],



"datasourceMonitoringConfigId": [



"string"



],



"declarativeConfigRuleId": [



"string"



],



"declarativeId": [



"string"



],



"dockerContainerIds": [



"string"



],



"dockerContainerImageNames": [



"string"



],



"dockerContainerImageVersions": [



"string"



],



"dockerContainerNames": [



"string"



],



"dotNetCommands": [



"string"



],



"dotnetCommandPath": [



"string"



],



"dynatraceClusterIds": [



"string"



],



"dynatraceNodeIds": [



"string"



],



"elasticSearchClusterNames": [



"string"



],



"elasticSearchNodeNames": [



"string"



],



"envVariables": {},



"equinoxConfigPath": [



"string"



],



"executablePaths": [



"string"



],



"executables": [



"string"



],



"glassfishDomainNames": [



"string"



],



"glassfishInstanceNames": [



"string"



],



"google.appengine.version": [



"string"



],



"google.cloudrun.execution": [



"string"



],



"google.cloudrun.job": [



"string"



],



"google.cloudrun.revision": [



"string"



],



"googleAppEngineInstances": [



"string"



],



"googleAppEngineServices": [



"string"



],



"googleCloudInstanceId": [



"string"



],



"googleCloudInstanceRegion": [



"string"



],



"googleCloudProjects": [



"string"



],



"googleCloudRunService": [



"string"



],



"googleComputeEngineMetadata": {},



"heroku.appdefaultdomainname": [



"string"



],



"heroku.dyno": [



"string"



],



"heroku.releaseversion": [



"string"



],



"hostGroups": [



"string"



],



"hybrisBinDirectories": [



"string"



],



"hybrisConfigDirectories": [



"string"



],



"hybrisDataDirectories": [



"string"



],



"ibmApplid": [



"string"



],



"ibmCicsImsApplid": [



"string"



],



"ibmCicsImsJobName": [



"string"



],



"ibmCicsRegion": [



"string"



],



"ibmCtgName": [



"string"



],



"ibmImsConnectRegions": [



"string"



],



"ibmImsControlRegions": [



"string"



],



"ibmImsMessageProcessingRegions": [



"string"



],



"ibmImsSoapGwName": [



"string"



],



"ibmIntegrationNodeName": [



"string"



],



"ibmIntegrationServerName": [



"string"



],



"ibmJobName": [



"string"



],



"iisAppPools": [



"string"



],



"iisRoleNames": [



"string"



],



"javaJarFiles": [



"string"



],



"javaJarPaths": [



"string"



],



"javaMainClasses": [



"string"



],



"javaMainModules": [



"string"



],



"jbossHomes": [



"string"



],



"jbossModes": [



"string"



],



"jbossServerNames": [



"string"



],



"kubernetesAnnotations": {},



"kubernetesBasePodNames": [



"string"



],



"kubernetesClusterId": [



"string"



],



"kubernetesContainerNames": [



"string"



],



"kubernetesFullPodNames": [



"string"



],



"kubernetesNamespaces": [



"string"



],



"kubernetesPodUids": [



"string"



],



"kubernetesRuleResult": [



"string"



],



"linkage": [



"string"



],



"mssqlInstanceName": [



"string"



],



"nodejsAppBaseDirectories": [



"string"



],



"nodejsAppNames": [



"string"



],



"nodejsScriptNames": [



"string"



],



"oracleSid": [



"string"



],



"osagent.groupIdName": [



"string"



],



"osagent.instanceIdName": [



"string"



],



"phpScripts": [



"string"



],



"phpWorkingDirectories": [



"string"



],



"pluginMetadata": {},



"pythonModule": [



"string"



],



"pythonScript": [



"string"



],



"pythonScriptPath": [



"string"



],



"rke2Type": [



"string"



],



"rubyAppRootPaths": [



"string"



],



"rubyScriptPaths": [



"string"



],



"ruleResult": [



"string"



],



"serviceNames": [



"string"



],



"softwareAgInstallRoot": [



"string"



],



"softwareAgProductPropertyName": [



"string"



],



"springBootAppName": [



"string"



],



"springBootProfileName": [



"string"



],



"springBootStartupClass": [



"string"



],



"tibcoBWEnginePropertyFilePaths": [



"string"



],



"tibcoBusinessWorksAppNodeName": [



"string"



],



"tibcoBusinessWorksAppSpaceName": [



"string"



],



"tibcoBusinessWorksCeAppName": [



"string"



],



"tibcoBusinessWorksCeVersion": [



"string"



],



"tibcoBusinessWorksDomainName": [



"string"



],



"tibcoBusinessWorksEnginePropertyFiles": [



"string"



],



"tibcoBusinessWorksHome": [



"string"



],



"varnishInstanceNames": [



"string"



],



"weblogicClusterNames": [



"string"



],



"weblogicDomainNames": [



"string"



],



"weblogicHomeValues": [



"string"



],



"weblogicNames": [



"string"



],



"websphereCellNames": [



"string"



],



"websphereClusterNames": [



"string"



],



"websphereLibertyServerName": [



"string"



],



"websphereNodeNames": [



"string"



],



"websphereServerNames": [



"string"



],



"zCodeModuleVersion": [



"string"



]



},



"modules": [



"string"



],



"monitoringState": {



"actualMonitoringState": "OFF",



"expectedMonitoringState": "OFF",



"restartRequired": true



},



"softwareTechnologies": [



{



"edition": "string",



"type": "string",



"version": "string"



}



],



"tags": [



{



"context": "AWS",



"key": "string",



"value": "string"



}



],



"toRelationships": {



"isNetworkClientOf": [



"string"



],



"runsOnProcessGroupInstance": [



"string"



]



},



"versionedModules": [



{



"name": "string",



"version": "string"



}



]



}



]
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

## Response headers

| Header | Type | Description |
| --- | --- | --- |
| Total-Count | integer | The estimated number of results. |
| Next-Page-Key | string | The cursor for the next page of results. Without it you'll get the first page again. |
| Page-Size | string | The maximum number of results per page. |

## Example

In this example, the request lists all processes in your Dynatrace environment detected **within the last 5 minutes**.

The API token is passed in the **Authorization** header.

The result is truncated to two entries.

#### Curl

```
curl -X GET \



'https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/processes?relativeTime=5mins' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/processes?relativeTime=5mins
```

#### Response body

```
[



{



"entityId": "PROCESS_GROUP_INSTANCE-EC9688429EB24B6B",



"displayName": "Apache Web Server apache2",



"discoveredName": "Apache Web Server apache2",



"firstSeenTimestamp": 1464951001104,



"lastSeenTimestamp": 1544024894801,



"tags": [],



"fromRelationships": {



"isProcessOf": [



"HOST-5FD609AD6757BE7D"



],



"isInstanceOf": [



"PROCESS_GROUP-B34081EFF9E5F516"



]



},



"toRelationships": {



"runsOnProcessGroupInstance": [



"SERVICE-C3173FEB08025322",



"SERVICE-B8C88BAA442098CF"



]



},



"metadata": {



"commandLineArgs": [



"/usr/sbin/apache2 -k start"



],



"executables": [



"apache2"



],



"executablePaths": [



"/usr/sbin/apache2"



],



"apacheConfigPaths": [



"/etc/apache2/apache2.conf"



]



},



"softwareTechnologies": [



{



"type": "PHP",



"edition": "Apache",



"version": "5.5.9"



},



{



"type": "APACHE_HTTPD",



"edition": null,



"version": "2.4.7"



},



{



"type": "SQLITE",



"edition": null,



"version": null



}



],



"listenPorts": [



443,



80



],



"bitness": "64bit",



"monitoringState": {



"actualMonitoringState": "ON",



"expectedMonitoringState": "ON",



"restartRequired": false



},



"agentVersions": [



{



"major": 1,



"minor": 157,



"revision": 167,



"timestamp": "20181127-152923",



"sourceRevision": ""



}



]



},



{



"entityId": "PROCESS_GROUP_INSTANCE-C43E52A77ED8F809",



"displayName": "OneAgent network monitoring",



"discoveredName": "OneAgent network monitoring",



"firstSeenTimestamp": 1543571247077,



"lastSeenTimestamp": 1544024847791,



"tags": [



{



"context": "CONTEXTLESS",



"key": "sample tag"



}



],



"fromRelationships": {



"isProcessOf": [



"HOST-CCEA78FDE257A4B9"



],



"isInstanceOf": [



"PROCESS_GROUP-E2B399E9E7FF43C0"



],



"isNetworkClientOf": [



"PROCESS_GROUP_INSTANCE-9E7865921C2C984E"



]



},



"toRelationships": {},



"metadata": {



"hostGroups": [



"wazuh"



]



},



"softwareTechnologies": [



{



"type": "APMNG",



"edition": null,



"version": null



}



],



"bitness": "64bit",



"monitoringState": {



"actualMonitoringState": "ON",



"expectedMonitoringState": "ON",



"restartRequired": false



}



}



]
```

#### Response code

200

## Related topics

* [Process groups](/docs/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.")


---


## Source: get-a-service.md


---
title: Services API - GET a service
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-a-service
scraped: 2026-02-16T21:19:16.545103
---

# Services API - GET a service

# Services API - GET a service

* Reference
* Updated on Mar 22, 2023
* Deprecated

This API is deprecated. Use the [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") instead. You can find more information about switching to the new API in the [migration guide](/docs/dynatrace-api/basics/deprecation-migration-guides/topology-v1-to-entity-v2 "Migrate your automation to the Monitored entities API.").

Gets the parameters of a specified service.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/services/{meIdentifier}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/services/{meIdentifier}` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| meIdentifier | string | The Dynatrace entity ID of the required service. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [Service](#openapi-definition-Service) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `Service` object

| Element | Type | Description |
| --- | --- | --- |
| agentTechnologyType | string | -The element can hold these values * `APACHE` * `DOTNET` * `DUMPPROC` * `GO` * `IIS` * `JAVA` * `LOG_ANALYTICS` * `N/A` * `NET` * `NETTRACER` * `NGINX` * `NODEJS` * `OPENTRACINGNATIVE` * `OS` * `PHP` * `PLUGIN` * `PROCESS` * `PYTHON` * `REMOTE_PLUGIN` * `RUBY` * `SDK` * `UPDATER` * `VARNISH` * `WSMB` * `Z` |
| akkaActorSystem | string | The services of the akka actor system. |
| className | string | - |
| contextRoot | string | - |
| customizedName | string | The customized name of the entity |
| databaseHostNames | string[] | - |
| databaseName | string | - |
| databaseVendor | string | - |
| discoveredName | string | The discovered name of the entity |
| displayName | string | The name of the Dynatrace entity as displayed in the UI. |
| entityId | string | The Dynatrace entity ID of the required entity. |
| esbApplicationName | string | The ESB application name. |
| firstSeenTimestamp | integer | The timestamp of when the entity was first detected, in UTC milliseconds |
| fromRelationships | object | - |
| ibmCtgGatewayUrl | string | The IBM CTG gateway URL. |
| ibmCtgServerName | string | The IBM CICS Transaction Gateway name. |
| iibApplicationName | string | The IIB application name. |
| ipAddresses | string[] | - |
| isExternalService | boolean | - |
| lastSeenTimestamp | integer | The timestamp of when the entity was last detected, in UTC milliseconds |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | The management zones that the entity is part of. |
| path | string | - |
| port | integer | - |
| publicDomainName | object | Public domain name. |
| remoteEndpoint | string | The endpoint of the remote service. |
| remoteServiceName | string | The name of the remote service. |
| serviceDetectionAttributes | object | Attributes that contributed to the service id. |
| serviceTechnologyTypes | string[] | - |
| serviceType | string | -The element can hold these values * `Cics` * `CicsInteraction` * `CustomApplication` * `Database` * `EnterpriseServiceBus` * `External` * `Ims` * `ImsInteraction` * `Messaging` * `Method` * `Mobile` * `Process` * `QueueInteraction` * `QueueListener` * `RemoteCall` * `Rmi` * `SaasVendor` * `Span` * `Unified` * `Unknown` * `WebRequest` * `WebService` * `WebSite` * `ZosConnect` |
| softwareTechnologies | [TechnologyInfo[]](#openapi-definition-TechnologyInfo) | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | The list of entity tags. |
| toRelationships | object | - |
| webApplicationId | string | - |
| webServerName | string | - |
| webServiceName | string | - |
| webServiceNamespace | string | - |

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

#### The `TechnologyInfo` object

| Element | Type | Description |
| --- | --- | --- |
| edition | string | - |
| type | string | - |
| version | string | - |

#### The `TagInfo` object

Tag of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. The element can hold these values * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | The key of the tag.  Custom tags have the tag value here. |
| value | string | The value of the tag.  Not applicable to custom tags. |

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



"agentTechnologyType": "APACHE",



"akkaActorSystem": "string",



"className": "string",



"contextRoot": "string",



"customizedName": "string",



"databaseHostNames": [



"string"



],



"databaseName": "string",



"databaseVendor": "string",



"discoveredName": "string",



"displayName": "string",



"entityId": "string",



"esbApplicationName": "string",



"firstSeenTimestamp": 1,



"fromRelationships": {



"calls": [



"string"



],



"runsOn": [



"string"



],



"runsOnProcessGroupInstance": [



"string"



]



},



"ibmCtgGatewayUrl": "string",



"ibmCtgServerName": "string",



"iibApplicationName": "string",



"ipAddresses": [



"string"



],



"isExternalService": true,



"lastSeenTimestamp": 1,



"managementZones": [



{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}



],



"path": "string",



"port": 1,



"publicDomainName": {},



"remoteEndpoint": "string",



"remoteServiceName": "string",



"serviceDetectionAttributes": {},



"serviceTechnologyTypes": [



"string"



],



"serviceType": "Cics",



"softwareTechnologies": [



{



"edition": "string",



"type": "string",



"version": "string"



}



],



"tags": [



{



"context": "AWS",



"key": "string",



"value": "string"



}



],



"toRelationships": {



"calls": [



"string"



]



},



"webApplicationId": "string",



"webServerName": "string",



"webServiceName": "string",



"webServiceNamespace": "string"



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

In this example, the request gets the details of the **PHP-FPM via domain socket /run/php7-fpm.sock** service, which has the ID of **SERVICE-72503CBDD2AEF066**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X GET \



'https://mySampleEnv.live.dynatrace.com/api/v1/entity/services/SERVICE-72503CBDD2AEF066' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/services/SERVICE-72503CBDD2AEF066
```

#### Response body

```
{



"entityId": "SERVICE-72503CBDD2AEF066",



"displayName": "PHP-FPM via domain socket /run/php7-fpm.sock",



"discoveredName": "PHP-FPM via domain socket /run/php7-fpm.sock",



"firstSeenTimestamp": 1505902015554,



"lastSeenTimestamp": 1546010106998,



"tags": [],



"fromRelationships": {



"runsOnProcessGroupInstance": [



"PROCESS_GROUP_INSTANCE-9BA70456D770536E",



"PROCESS_GROUP_INSTANCE-7E988C3503AE8803"



],



"runsOn": [



"PROCESS_GROUP-E5C3CC7EC1F80B5B"



]



},



"toRelationships": {



"calls": [



"SERVICE-5304CCF4AFBFF35E"



]



},



"agentTechnologyType": "N/A",



"serviceType": "WebRequest",



"softwareTechnologies": [



{



"type": "SQLITE",



"edition": null,



"version": null



},



{



"type": "PHP",



"edition": "FPM",



"version": "7.0.32"



},



{



"type": "PHP_FPM",



"edition": null,



"version": null



}



]



}
```

#### Response code

200

## Related topics

* [Services](/docs/observe/application-observability/services "Learn how to monitor and analyze your services, define and use request attributes, and more.")


---


## Source: get-all.md


---
title: Services API - GET all services
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-all
scraped: 2026-02-16T21:19:18.146820
---

# Services API - GET all services

# Services API - GET all services

* Reference
* Updated on Mar 22, 2023
* Deprecated

This API is deprecated. Use the [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") instead. You can find more information about switching to the new API in the [migration guide](/docs/dynatrace-api/basics/deprecation-migration-guides/topology-v1-to-entity-v2 "Migrate your automation to the Monitored entities API.").

Gets a list of all services in your Dynatrace environment, along with their parameters and relationships.

The full list can be lengthy, so you can narrow it down by specifying filter parameters, like tags. See the **Parameters** section for more details.

You can additionally limit the output by using the pagination:

1. Specify the number of results per page in the **pageSize** query parameter.
2. Then use the cursor from the **Next-Page-Key** response header in the **nextPageKey** query parameter to obtain subsequent pages.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/services` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/services` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The timeframe is restricted to a **maximum period of 3 days**.

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| startTimestamp | integer | The start timestamp of the requested timeframe, in milliseconds (UTC).  If not set, then 72 hours behind from now is used. | query | Optional |
| endTimestamp | integer | The end timestamp of the requested timeframe, in milliseconds (UTC).  If not set, then the current timestamp is used.  The timeframe must not exceed 3 days. | query | Optional |
| relativeTime | string | The relative timeframe, back from now. The element can hold these values * `min` * `5mins` * `10mins` * `15mins` * `30mins` * `hour` * `2hours` * `6hours` * `day` * `3days` | query | Optional |
| tag | string[] | Filters the resulting set of services by the specified tag. You can specify several tags in the following format: `tag=tag1&tag=tag2`. The service has to match **all** the specified tags.  In case of key-value tags, such as imported AWS or CloudFoundry tags, use the following format: `tag=[context]key:value`. For custom key-value tags, omit the context: `tag=key:value`. | query | Optional |
| entity | string[] | Filters result to the specified services only.  To specify several services use the following format: `entity=ID1&entity=ID2`. | query | Optional |
| managementZone | integer | Only return services that are part of the specified management zone. | query | Optional |
| includeDetails | boolean | Includes (`true`) or excludes (`false`) details which are queried from related entities.  Excluding details may make queries faster.  If not set, then `true` is used. | query | Optional |
| pageSize | integer | The number of services per result page.  If not set, pagination is not used and the result contains all services fitting the specified filtering criteria. | query | Optional |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **Next-Page-Key** header of the previous response.  If you're using pagination, the first page is always returned without this cursor.  You must keep all other query parameters as they were in the first request to obtain subsequent pages. | query | Optional |

## Response headers

| Header | Type | Description |
| --- | --- | --- |
| Total-Count | integer | The estimated number of results. |
| Next-Page-Key | string | The cursor for the next page of results. Without it you'll get the first page again. |
| Page-Size | string | The maximum number of results per page. |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [Service[]](#openapi-definition-Service) | Success |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ResponseBody` object

#### The `Service` object

| Element | Type | Description |
| --- | --- | --- |
| agentTechnologyType | string | -The element can hold these values * `APACHE` * `DOTNET` * `DUMPPROC` * `GO` * `IIS` * `JAVA` * `LOG_ANALYTICS` * `N/A` * `NET` * `NETTRACER` * `NGINX` * `NODEJS` * `OPENTRACINGNATIVE` * `OS` * `PHP` * `PLUGIN` * `PROCESS` * `PYTHON` * `REMOTE_PLUGIN` * `RUBY` * `SDK` * `UPDATER` * `VARNISH` * `WSMB` * `Z` |
| akkaActorSystem | string | The services of the akka actor system. |
| className | string | - |
| contextRoot | string | - |
| customizedName | string | The customized name of the entity |
| databaseHostNames | string[] | - |
| databaseName | string | - |
| databaseVendor | string | - |
| discoveredName | string | The discovered name of the entity |
| displayName | string | The name of the Dynatrace entity as displayed in the UI. |
| entityId | string | The Dynatrace entity ID of the required entity. |
| esbApplicationName | string | The ESB application name. |
| firstSeenTimestamp | integer | The timestamp of when the entity was first detected, in UTC milliseconds |
| fromRelationships | object | - |
| ibmCtgGatewayUrl | string | The IBM CTG gateway URL. |
| ibmCtgServerName | string | The IBM CICS Transaction Gateway name. |
| iibApplicationName | string | The IIB application name. |
| ipAddresses | string[] | - |
| isExternalService | boolean | - |
| lastSeenTimestamp | integer | The timestamp of when the entity was last detected, in UTC milliseconds |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | The management zones that the entity is part of. |
| path | string | - |
| port | integer | - |
| publicDomainName | object | Public domain name. |
| remoteEndpoint | string | The endpoint of the remote service. |
| remoteServiceName | string | The name of the remote service. |
| serviceDetectionAttributes | object | Attributes that contributed to the service id. |
| serviceTechnologyTypes | string[] | - |
| serviceType | string | -The element can hold these values * `Cics` * `CicsInteraction` * `CustomApplication` * `Database` * `EnterpriseServiceBus` * `External` * `Ims` * `ImsInteraction` * `Messaging` * `Method` * `Mobile` * `Process` * `QueueInteraction` * `QueueListener` * `RemoteCall` * `Rmi` * `SaasVendor` * `Span` * `Unified` * `Unknown` * `WebRequest` * `WebService` * `WebSite` * `ZosConnect` |
| softwareTechnologies | [TechnologyInfo[]](#openapi-definition-TechnologyInfo) | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | The list of entity tags. |
| toRelationships | object | - |
| webApplicationId | string | - |
| webServerName | string | - |
| webServiceName | string | - |
| webServiceNamespace | string | - |

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

#### The `TechnologyInfo` object

| Element | Type | Description |
| --- | --- | --- |
| edition | string | - |
| type | string | - |
| version | string | - |

#### The `TagInfo` object

Tag of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. The element can hold these values * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | The key of the tag.  Custom tags have the tag value here. |
| value | string | The value of the tag.  Not applicable to custom tags. |

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
[



{



"agentTechnologyType": "APACHE",



"akkaActorSystem": "string",



"className": "string",



"contextRoot": "string",



"customizedName": "string",



"databaseHostNames": [



"string"



],



"databaseName": "string",



"databaseVendor": "string",



"discoveredName": "string",



"displayName": "string",



"entityId": "string",



"esbApplicationName": "string",



"firstSeenTimestamp": 1,



"fromRelationships": {



"calls": [



"string"



],



"runsOn": [



"string"



],



"runsOnProcessGroupInstance": [



"string"



]



},



"ibmCtgGatewayUrl": "string",



"ibmCtgServerName": "string",



"iibApplicationName": "string",



"ipAddresses": [



"string"



],



"isExternalService": true,



"lastSeenTimestamp": 1,



"managementZones": [



{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}



],



"path": "string",



"port": 1,



"publicDomainName": {},



"remoteEndpoint": "string",



"remoteServiceName": "string",



"serviceDetectionAttributes": {},



"serviceTechnologyTypes": [



"string"



],



"serviceType": "Cics",



"softwareTechnologies": [



{



"edition": "string",



"type": "string",



"version": "string"



}



],



"tags": [



{



"context": "AWS",



"key": "string",



"value": "string"



}



],



"toRelationships": {



"calls": [



"string"



]



},



"webApplicationId": "string",



"webServerName": "string",



"webServiceName": "string",



"webServiceNamespace": "string"



}



]
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

In this example, the request lists all the services of the environment detected **within the last 5 minutes**.

The API token is passed in the **Authorization** header.

The result is truncated to two entries.

#### Curl

```
curl -X GET \



'https://mySampleEnv.live.dynatrace.com/api/v1/entity/services?relativeTime=5mins' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/services?relativeTime=5mins
```

#### Response body

```
[



{



"entityId": "SERVICE-72503CBDD2AEF066",



"displayName": "PHP-FPM via domain socket /run/php7-fpm.sock",



"discoveredName": "PHP-FPM via domain socket /run/php7-fpm.sock",



"firstSeenTimestamp": 1505902015554,



"lastSeenTimestamp": 1544025169570,



"tags": [



{



"context": "CONTEXTLESS",



"key": "Sample tag"



}



],



"fromRelationships": {



"runsOnProcessGroupInstance": [



"PROCESS_GROUP_INSTANCE-165E2E1655782C30",



"PROCESS_GROUP_INSTANCE-2E41AD6095ACE67B",



"PROCESS_GROUP_INSTANCE-3E537F0F455E9757"



],



"runsOn": [



"PROCESS_GROUP-E5C3CC7EC1F80B5B"



]



},



"toRelationships": {



"calls": [



"SERVICE-5304CCF4AFBFF35E"



]



},



"agentTechnologyType": "N/A",



"serviceType": "WebRequest",



"softwareTechnologies": [



{



"type": "SQLITE",



"edition": null,



"version": null



},



{



"type": "PHP",



"edition": "FPM",



"version": "7.0.32"



},



{



"type": "PHP_FPM",



"edition": null,



"version": null



}



]



},



{



"entityId": "SERVICE-52AC624D70C377BC",



"displayName": "Requests to public networks",



"discoveredName": "Requests to public networks",



"firstSeenTimestamp": 1421376505750,



"lastSeenTimestamp": 1544025153570,



"tags": [],



"fromRelationships": {},



"toRelationships": {



"calls": [



"SERVICE-635F6C4CAD07BC56",



"SERVICE-74C7ACD74FA27688",



"SERVICE-C7790E5EDD1F895E"



]



},



"agentTechnologyType": "N/A",



"serviceType": "WebRequest"



}



]
```

#### Response code

200

## Related topics

* [Services](/docs/observe/application-observability/services "Learn how to monitor and analyze your services, define and use request attributes, and more.")


---


## Source: get-baseline.md


---
title: Services API - GET baseline
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-baseline
scraped: 2026-02-16T21:19:00.013180
---

# Services API - GET baseline

# Services API - GET baseline

* Reference
* Updated on Mar 22, 2023
* Deprecated

Gets the baseline data of the specified service.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/services/{meIdentifier}/baseline` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/services/{meIdentifier}/baseline` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| meIdentifier | string | The Dynatrace entity ID of the required service. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ServiceBaselineValues](#openapi-definition-ServiceBaselineValues) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ServiceBaselineValues` object

The baseline data for a service and its children for the **Response time** duration metric.

| Element | Type | Description |
| --- | --- | --- |
| displayName | string | The display name of the service. |
| entityId | string | The ID of the service. |
| serviceResponseTimeBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for the **Response time** duration metric. |

#### The `EntityBaselineData` object

The baseline data for a Dynatrace entity for a specific duration metric.

| Element | Type | Description |
| --- | --- | --- |
| childBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for child entities of this entity, for example a `SERVICE_METHOD` of a `SERVICE_METHOD_GROUP`. |
| displayName | string | The display name of the entity. |
| entityId | string | The ID of the Dynatrace entity. |
| errorRate | number | The error rate baseline. |
| hasLoadBaseline | boolean | The entity has a load baseline (`true`) or doesn't (`false`). |
| micros90thPercentile | number | The 90th percentile baseline, in microseconds. |
| microsMedian | number | The median baseline, in microseconds. |

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



"displayName": "string",



"entityId": "string",



"serviceResponseTimeBaselines": [



{



"childBaselines": [



{}



],



"displayName": "string",



"entityId": "string",



"errorRate": 1,



"hasLoadBaseline": true,



"micros90thPercentile": 1,



"microsMedian": 1



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

## Related topics

* [Services](/docs/observe/application-observability/services "Learn how to monitor and analyze your services, define and use request attributes, and more.")


---


## Source: post-tags.md


---
title: Services API - POST tags
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/services-api/post-tags
scraped: 2026-02-16T21:19:25.173724
---

# Services API - POST tags

# Services API - POST tags

* Reference
* Updated on Mar 22, 2023
* Deprecated

Assigns [custom tags](/docs/manage/tags-and-metadata "Learn how to define tags and metadata. Understand how to use tags and metadata to organize your environment.") to the specified service. You need to provide only a tag value. The `CONTEXTLESS` context will be assigned automatically.

The usage of this API is limited to value-only tags. To assign key:value tags, use the [Custom tags API](/docs/dynatrace-api/environment-api/custom-tags/post-tags "Assign custom tags to monitored entities via Dynatrace API.").

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/services/{meIdentifier}` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/services/{meIdentifier}` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| meIdentifier | string | The Dynatrace entity ID of the service you're inquiring. | path | Required |
| body | [UpdateEntity](#openapi-definition-UpdateEntity) | A list of tags to be assigned to a Dynatrace entity. | body | Optional |

### Request body objects

#### The `UpdateEntity` object

A list of tags to be assigned to a Dynatrace entity.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| tags | string[] | A list of tags to be assigned to a Dynatrace entity. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"tags": [



"office-linz",



"office-klagenfurt"



]



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The parameters of the service have been updated. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
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

In this example, the request assigns the **PHP** tag to the **PHP-FPM via domain socket /run/php7-fpm.sock** service, which has the ID of **SERVICE-72503CBDD2AEF066**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/entity/services/SERVICE-72503CBDD2AEF066 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"tags": [



"PHP"



]



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/services/SERVICE-72503CBDD2AEF066
```

#### Request body

```
{



"tags": [



"PHP"



]



}
```

#### Response code

204

## Related topics

* [Services](/docs/observe/application-observability/services "Learn how to monitor and analyze your services, define and use request attributes, and more.")


---


## Source: topology-and-smartscape.md


---
title: Topology and Smartscape API
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape
scraped: 2026-02-16T21:10:56.700334
---

# Topology and Smartscape API

# Topology and Smartscape API

* Reference
* Updated on Mar 22, 2023
* Deprecated

This API is deprecated. Use the [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") instead. You can find more information about switching to the new API in the [migration guide](/docs/dynatrace-api/basics/deprecation-migration-guides/topology-v1-to-entity-v2 "Migrate your automation to the Monitored entities API.").

The **Topology and Smartscape** API delivers details about applications, services, process groups, and infrastructure entities that Dynatrace automatically detects and monitors within a given environment.

The returned information contains important attributes about the monitored entities as well as outgoing and incoming relationships. This family of endpoints is organized along the five major environment layers: applications, hosts, processes, process groups, and services.

### Applications

* [Fetch the list](/docs/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-all "List all monitored applications via Dynatrace API.")
* [Get details](/docs/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-an-app "View a monitored application via Dynatrace API.")
* [Assign tags](/docs/dynatrace-api/environment-api/topology-and-smartscape/applications-api/post-tags "Assign tags to a monitored application via Dynatrace API.")
* [Get baseline data](/docs/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-baseline "View the baseline data of a monitored application via Dynatrace API.")

### Hosts

* [Fetch the list](/docs/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/get-all "List all monitored hosts via Dynatrace API.")
* [Get details](/docs/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/get-a-host "View a monitored host via Dynatrace API.")
* [Assign tags](/docs/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/post-tags "Assign tags to a monitored host via Dynatrace API.")

### Processes

* [Fetch the list](/docs/dynatrace-api/environment-api/topology-and-smartscape/processes-api/get-all "List all monitored processes via Dynatrace API.")
* [Get details](/docs/dynatrace-api/environment-api/topology-and-smartscape/processes-api/get-a-process "View a monitored process via Dynatrace API.")

### Process groups

* [Fetch the list](/docs/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/get-all "List all monitored process groups via Dynatrace API.")
* [Get details](/docs/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/get-a-process-group "View a monitored process group via Dynatrace API.")
* [Assign tags](/docs/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/post-tags "Assign tags to a monitored process group via Dynatrace API.")

### Services

* [Fetch the list](/docs/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-all "Lists all monitored services via Dynatrace API.")
* [Get details](/docs/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-a-service "View a monitored service via Dynatrace API.")
* [Assign tags](/docs/dynatrace-api/environment-api/topology-and-smartscape/services-api/post-tags "Assign tags to a service via Dynatrace API.")
* [Get baseline data](/docs/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-baseline "View the baseline data of a monitored service via Dynatrace API.")

### Create a custom device

[Create a custom device](/docs/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/create-custom-device-via-dynatrace-api "Learn how you can use the Dynatrace API to create a custom device.") with the exact parameters you need.

### Send data to a custom device

[Report custom device metric](/docs/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/report-custom-device-metric-via-rest-api "Learn how you can use the Dynatrace API to send a custom metric data point to a custom device.").

## Related topics

* [Visualize your environment through Smartscape Classic](/docs/analyze-explore-automate/smartscape-classic "Learn how Smartscape Classic visualizes all the entities and dependencies in your environment.")


---
