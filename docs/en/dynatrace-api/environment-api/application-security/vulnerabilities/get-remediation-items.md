---
title: Vulnerabilities API - GET remediation items
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/application-security/vulnerabilities/get-remediation-items
scraped: 2026-02-23T21:37:19.809209
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