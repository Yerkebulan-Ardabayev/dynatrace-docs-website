---
title: Vulnerabilities API - GET vulnerable functions
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/application-security/vulnerabilities/get-vulnerable-functions
scraped: 2026-02-27T21:19:23.938129
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