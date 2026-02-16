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