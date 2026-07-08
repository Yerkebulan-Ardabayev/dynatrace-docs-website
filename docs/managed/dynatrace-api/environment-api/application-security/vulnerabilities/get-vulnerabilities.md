---
title: Vulnerabilities API - GET vulnerabilities
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/application-security/vulnerabilities/get-vulnerabilities
---

# Vulnerabilities API - GET vulnerabilities

# Vulnerabilities API - GET vulnerabilities

* Reference
* Updated on Nov 09, 2023

Lists the third-party and code-level vulnerabilities detected in your applications.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/securityProblems` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems` |

## Authentication

To execute this request, you need an access token with `securityProblems.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **nextPageKey** field of the previous response.  The first page is always returned if you don't specify the **nextPageKey** query parameter.  When the **nextPageKey** is set to obtain subsequent pages, you must omit all other query parameters. | query | Optional |
| pageSize | integer | The amount of security problems in a single response payload.  The maximal allowed page size is 500.  If not set, 100 is used. | query | Optional |
| securityProblemSelector | string | Defines the scope of the query. Only security problems matching the specified criteria are included in the response.  You can add one or more of the following criteria. Values are *not* case-sensitive and the `EQUALS` operator is used unless otherwise specified.  * Status: `status("value")`. Find the possible values in the description of the **status** field of the response. If not set, all security problems are returned. * Muted: `muted("value")`. Possible values are `TRUE` or `FALSE`. * Risk level: `riskLevel("value")`. The Davis risk level. Find the possible values in the description of the **riskLevel** field of the response. * Minimum risk score: `minRiskScore("5.5")`. The Davis minimum risk score. The `GREATER THAN OR EQUAL TO` operator is used. Specify a number between `1.0` and `10.0`. * Maximum risk score: `maxRiskScore("5.5")`. The Davis maximum risk score. The `LESS THAN` operator is used. Specify a number between `1.0` and `10.0`. * Base risk level: `baseRiskLevel("value")`. The Base risk level from the CVSS. Find the possible values in the description of the **riskLevel** field of the response. * Minimum base risk score: `minBaseRiskScore("5.5")`. The minimum base risk score from the CVSS. The `GREATER THAN OR EQUAL TO` operator is used. Specify a number between `1.0` and `10.0`. * Maximum base risk score: `maxBaseRiskScore("5.5")`. The maximum base risk score from the CVSS. The `LESS THAN` operator is used. Specify a number between `1.0` and `10.0`. * External vulnerability ID contains: `externalVulnerabilityIdContains("id-1")`. The `CONTAINS` operator is used. Maximum value length is 48 characters. * External vulnerability ID: `externalVulnerabilityId("id-1", "id-2")`. * CVE ID: `cveId("id")`. * Risk assessment `riskAssessment("value-1", "value-2")` Possible values are `EXPOSED`, `SENSITIVE`, `EXPLOIT`, `VULNERABLE_FUNCTION_IN_USE` and `ACCURACY_REDUCED`. * Related host ID: `relatedHostIds("value-1", "value-2")`. Specify Dynatrace entity IDs here. * Related host name: `relatedHostNames("value-1", "value-2")`. Values are case-sensitive. * Related host name contains: `relatedHostNameContains("value-1")`. The `CONTAINS` operator is used. * Related Kubernetes cluster ID: `relatedKubernetesClusterIds("value-1", "value-2")`. Specify Dynatrace entity IDs here. * Related Kubernetes cluster name: `relatedKubernetesClusterNames("value-1", "value-2")`. Values are case-sensitive. * Related Kubernetes cluster name contains: `relatedKubernetesClusterNameContains("value-1")`. The `CONTAINS` operator is used. * Related Kubernetes workload ID: `relatedKubernetesWorkloadIds("value-1", "value-2")`. Specify Dynatrace entity IDs here. * Related Kubernetes workload name: `relatedKubernetesWorkloadNames("value-1", "value-2")`. Values are case-sensitive. * Related Kubernetes workload name contains: `relatedKubernetesWorkloadNameContains("value-1")`. The `CONTAINS` operator is used. * Management zone ID: `managementZoneIds("mzId-1", "mzId-2")`. * Management zone name: `managementZones("name-1", "name-2")`. Values are case-sensitive. * Affected process group instance ID: `affectedPgiIds("pgiId-1", "pgiId-2")`. Specify Dynatrace entity IDs here. * Affected process group ID: `affectedPgIds("pgId-1", "pgId-2")`. Specify Dynatrace entity IDs here. * Affected process group name: `affectedPgNames("name-1", "name-2")`. Values are case-sensitive. * Affected process group name contains: `affectedPgNameContains("name-1")`. The `CONTAINS` operator is used. * Vulnerable component ID: `vulnerableComponentIds("componentId-1", "componentId-2")`. Specify component IDs here. * Vulnerable component name: `vulnerableComponentNames("name-1", "name-2")`. Values are case-sensitive. * Vulnerable component name contains: `vulnerableComponentNameContains("name-1")`. The `CONTAINS` operator is used. * Host tags: `hostTags("hostTag-1")`. The `CONTAINS` operator is used. Maximum value length is 48 characters. * Process group tags: `pgTags("pgTag-1")`. The `CONTAINS` operator is used. Maximum value length is 48 characters. * Process group instance tags: `pgiTags("pgiTag-1")`. The `CONTAINS` operator is used. Maximum value length is 48 characters. * Tags: `tags("tag-1")`. The `CONTAINS` operator is used. This selector picks hosts, process groups, and process group instances at the same time. Maximum value length is 48 characters. * Display ID: `displayIds("S-1234", "S-5678")`. The `EQUALS` operator is used. * Security problem ID: `securityProblemIds("12544152654387159360", "5904857564184044850")`. The `EQUALS` operator is used. * Technology: `technology("technology-1", "technology-2")`. Find the possible values in the description of the **technology** field of the response. The `EQUALS` operator is used. * Vulnerability type: `vulnerabilityType("type-1", "type-2")`. Possible values are `THIRD_PARTY`, `CODE_LEVEL`, `RUNTIME`.  Risk score and risk category are mutually exclusive (cannot be used at the same time).  To set several criteria, separate them with a comma (`,`). Only results matching **all** criteria are included in the response.  Specify the value of a criterion as a quoted string. The following special characters must be escaped with a tilde (`~`) inside quotes:  * Tilde `~` * Quote `"` | query | Optional |
| sort | string | Specifies one or more fields for sorting the security problem list. Multiple fields can be concatenated using a comma (`,`) as a separator (e.g. `+status,-timestamp`).  You can sort by the following properties with a sign prefix for the sorting order.  * `status`: The security problem status (`+` open first or `-` resolved first) * `muted`: The security problem mute state (`+` unmuted first or `-` muted first) * `technology`: The security problem technology * `firstSeenTimestamp`: The timestamp of the first occurrence of the security problem (`+` new problems first or `-` old problems first) * `lastUpdatedTimestamp`: The timestamp of the last update of the security problem (`+` recently updated problems first or `-` earlier updated problems first) * `securityProblemId`: The auto-generated ID of the security problem (`+` lower number first or `-` higher number first) * `externalVulnerabilityId`: The ID of the external vulnerability (`+` lower number first or `-` higher number first) * `displayId`: The display ID (`+` lower number first or `-` higher number first) * `riskAssessment.riskScore`: Davis Security Score (`+` lower score first or `-` higher score first) * `riskAssessment.riskLevel`: Davis Security Score level (`+` lower level first or `-` higher level first) * `riskAssessment.exposure`: Whether the problem is exposed to the internet * `riskAssessment.baseRiskScore`: The CVSS score (`+` lower score first or `-` higher score first) * `riskAssessment.baseRiskLevel`: The CVSS level (`+` lower level first or `-` higher level first) * `riskAssessment.dataAssets`: Whether data assets are affected * `riskAssessment.vulnerableFunctionUsage`: Whether vulnerable functions are used * `riskAssessment.assessmentAccuracy`: The assessments accuracy (`+` less accuracy first or `-` more accuracy first) * `globalCounts.affectedNodes`: Number of affected nodes (`+` lower number first or `-` higher number first) * `globalCounts.affectedProcessGroupInstances`: Number of affected process group instances (`+` lower number first or `-` higher number first) * `globalCounts.affectedProcessGroups`: Number of affected process groups (`+` lower number first or `-` higher number first) * `globalCounts.exposedProcessGroups`: Number of exposed process groups (`+` lower number first or `-` higher number first) * `globalCounts.reachableDataAssets`: Number of reachable data assets (`+` lower number first or `-` higher number first) * `globalCounts.relatedApplications`: Number of related applications (`+` lower number first or `-` higher number first) * `globalCounts.relatedAttacks`: Number of attacks on the security problem (`+` lower number first or `-` higher number first) * `globalCounts.relatedHosts`: Number of related hosts (`+` lower number first or `-` higher number first) * `globalCounts.relatedKubernetesClusters`: Number of related Kubernetes cluster (`+` lower number first or `-` higher number first) * `globalCounts.relatedKubernetesWorkloads`: Number of related Kubernetes workloads (`+` lower number first or `-` higher number first) * `globalCounts.relatedServices`: Number of related services (`+` lower number first or `-` higher number first) * `globalCounts.vulnerableComponents`: Number of vulnerable components (`+` lower number first or `-` higher number first)  If no prefix is set, `+` is used. | query | Optional |
| fields | string | A list of additional security problem properties you can add to the response.  The following properties are available (all other properties are always included and you can't remove them from the response):  * `riskAssessment`: A risk assessment of the security problem. * `managementZones`: The management zone where the security problem occurred. * `codeLevelVulnerabilityDetails`: Details of the code-level vulnerability. * `globalCounts`: Globally calculated statistics about the security problem. No management zone information is taken into account.  To add properties, specify them in a comma-separated list and prefix each property with a plus (for example, `+riskAssessment,+managementZones`). | query | Optional |
| from | string | The start of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the relative timeframe of thirty days is used (`now-30d`). | query | Optional |
| to | string | The end of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the current timestamp is used.  The end of the timeframe must not be older than 365 days. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SecurityProblemList](#openapi-definition-SecurityProblemList) | Success. The response contains the list of security problems. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `SecurityProblemList` object

A list of security problems.

| Element | Type | Description |
| --- | --- | --- |
| nextPageKey | string | The cursor for the next page of results. Has the value of `null` on the last page.  Use it in the **nextPageKey** query parameter to obtain subsequent pages of the result. |
| pageSize | integer | The number of entries per page. |
| securityProblems | [SecurityProblem](#openapi-definition-SecurityProblem)[] | A list of security problems. |
| totalCount | integer | The total number of entries in the result. |

#### The `SecurityProblem` object

Parameters of a security problem

| Element | Type | Description |
| --- | --- | --- |
| codeLevelVulnerabilityDetails | [CodeLevelVulnerabilityDetails](#openapi-definition-CodeLevelVulnerabilityDetails) | The details of a code-level vulnerability. |
| cveIds | string[] | A list of CVE IDs of the security problem. |
| displayId | string | The display ID of the security problem. |
| externalVulnerabilityId | string | The external vulnerability ID of the security problem. |
| firstSeenTimestamp | integer | The timestamp of the first occurrence of the security problem. |
| globalCounts | [GlobalCountsDto](#openapi-definition-GlobalCountsDto) | Globally calculated statistics about the security problem. No management zone information is taken into account. |
| lastOpenedTimestamp | integer | The timestamp when the security problem was last opened. |
| lastResolvedTimestamp | integer | The timestamp when the security problem was last resolved. |
| lastUpdatedTimestamp | integer | The timestamp of the most recent security problem change. |
| managementZones | [ManagementZone](#openapi-definition-ManagementZone)[] | A list of management zones which the affected entities belong to. |
| muted | boolean | The security problem is (`true`) or is not (`false`) muted. |
| packageName | string | The package name of the security problem. |
| riskAssessment | [RiskAssessment](#openapi-definition-RiskAssessment) | Risk assessment of a security problem. |
| securityProblemId | string | The ID of the security problem. |
| status | string | The status of the security problem. The element can hold these values * `OPEN` * `RESOLVED` |
| technology | string | The technology of the security problem. The element can hold these values * `DOTNET` * `GO` * `JAVA` * `KUBERNETES` * `NODE_JS` * `PHP` * `PYTHON` |
| title | string | The title of the security problem. |
| url | string | The URL to the security problem details page. |
| vulnerabilityType | string | The type of the vulnerability. The element can hold these values * `CODE_LEVEL` * `RUNTIME` * `THIRD_PARTY` |

#### The `CodeLevelVulnerabilityDetails` object

The details of a code-level vulnerability.

| Element | Type | Description |
| --- | --- | --- |
| processGroupIds | string[] | The list of encoded MEIdentifier of the process groups. |
| processGroups | string[] | The list of affected process groups. |
| shortVulnerabilityLocation | string | The code location of the vulnerability without package and parameter. |
| type | string | The type of code level vulnerability. The element can hold these values * `CMD_INJECTION` * `IMPROPER_INPUT_VALIDATION` * `SQL_INJECTION` * `SSRF` |
| vulnerabilityLocation | string | The code location of the vulnerability. |
| vulnerableFunction | string | The vulnerable function of the vulnerability. |
| vulnerableFunctionInput | [VulnerableFunctionInput](#openapi-definition-VulnerableFunctionInput) | Describes what got passed into the code level vulnerability. |

#### The `VulnerableFunctionInput` object

Describes what got passed into the code level vulnerability.

| Element | Type | Description |
| --- | --- | --- |
| inputSegments | [VulnerableFunctionInputSegment](#openapi-definition-VulnerableFunctionInputSegment)[] | A list of input segments. |
| type | string | The type of the input. The element can hold these values * `COMMAND` * `HTTP_CLIENT` * `JNDI` * `SQL_STATEMENT` |

#### The `VulnerableFunctionInputSegment` object

Describes one segment that was passed into a vulnerable function.

| Element | Type | Description |
| --- | --- | --- |
| type | string | The type of the input segment. The element can hold these values * `MALICIOUS_INPUT` * `REGULAR_INPUT` * `TAINTED_INPUT` |
| value | string | The value of the input segment. |

#### The `GlobalCountsDto` object

Globally calculated statistics about the security problem. No management zone information is taken into account.

| Element | Type | Description |
| --- | --- | --- |
| affectedNodes | integer | Number of affected nodes |
| affectedProcessGroupInstances | integer | Number of affected process group instances |
| affectedProcessGroups | integer | Number of affected process groups |
| exposedProcessGroups | integer | Number of exposed process groups |
| reachableDataAssets | integer | Number of reachable data assets exposed |
| relatedApplications | integer | Number of related applications |
| relatedAttacks | integer | Number of attacks on the exposed security problem |
| relatedHosts | integer | Number of related hosts |
| relatedKubernetesClusters | integer | Number of related kubernetes cluster |
| relatedKubernetesWorkloads | integer | Number of related kubernetes workloads |
| relatedServices | integer | Number of related services |
| vulnerableComponents | integer | Number of vulnerable components |

#### The `ManagementZone` object

A short representation of a management zone.

| Element | Type | Description |
| --- | --- | --- |
| id | string | The ID of the management zone. |
| name | string | The name of the management zone. |

#### The `RiskAssessment` object

Risk assessment of a security problem.

| Element | Type | Description |
| --- | --- | --- |
| assessmentAccuracy | string | The accuracy of the assessment. The element can hold these values * `FULL` * `NOT_AVAILABLE` * `REDUCED` |
| assessmentAccuracyDetails | [AssessmentAccuracyDetails](#openapi-definition-AssessmentAccuracyDetails) | The assessment accuracy details. |
| baseRiskLevel | string | The risk level from the CVSS score. The element can hold these values * `CRITICAL` * `HIGH` * `LOW` * `MEDIUM` * `NONE` |
| baseRiskScore | number | The risk score (1-10) from the CVSS score. |
| baseRiskVector | string | The original attack vector of the CVSS assessment. |
| dataAssets | string | The reachability of related data assets by affected entities. The element can hold these values * `NOT_AVAILABLE` * `NOT_DETECTED` * `REACHABLE` |
| exposure | string | The level of exposure of affected entities. The element can hold these values * `NOT_AVAILABLE` * `NOT_DETECTED` * `PUBLIC_NETWORK` |
| publicExploit | string | The availability status of public exploits. The element can hold these values * `AVAILABLE` * `NOT_AVAILABLE` |
| riskLevel | string | The Davis risk level.  It is calculated by Dynatrace on the basis of CVSS score. The element can hold these values * `CRITICAL` * `HIGH` * `LOW` * `MEDIUM` * `NONE` |
| riskScore | number | The Davis risk score (1-10).  It is calculated by Dynatrace on the basis of CVSS score. |
| riskVector | string | The attack vector calculated by Dynatrace based on the CVSS attack vector. |
| vulnerableFunctionUsage | string | The state of vulnerable code execution. The element can hold these values * `IN_USE` * `NOT_AVAILABLE` * `NOT_IN_USE` |

#### The `AssessmentAccuracyDetails` object

The assessment accuracy details.

| Element | Type | Description |
| --- | --- | --- |
| reducedReasons | string[] | The reason for a reduced accuracy of the assessment. The element can hold these values * `LIMITED_AGENT_SUPPORT` * `LIMITED_BY_CONFIGURATION` |

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



"nextPageKey": "AQAAABQBAAAABQ==",



"pageSize": 1,



"securityProblems": [



{



"codeLevelVulnerabilityDetails": {



"processGroupIds": [



"string"



],



"processGroups": [



"string"



],



"shortVulnerabilityLocation": "string",



"type": "CMD_INJECTION",



"vulnerabilityLocation": "string",



"vulnerableFunction": "string",



"vulnerableFunctionInput": {



"inputSegments": [



{



"type": "MALICIOUS_INPUT",



"value": "string"



}



],



"type": "COMMAND"



}



},



"cveIds": [



"string"



],



"displayId": "string",



"externalVulnerabilityId": "string",



"firstSeenTimestamp": 1,



"globalCounts": {



"affectedNodes": 1,



"affectedProcessGroupInstances": 1,



"affectedProcessGroups": 1,



"exposedProcessGroups": 1,



"reachableDataAssets": 1,



"relatedApplications": 1,



"relatedAttacks": 1,



"relatedHosts": 1,



"relatedKubernetesClusters": 1,



"relatedKubernetesWorkloads": 1,



"relatedServices": 1,



"vulnerableComponents": 1



},



"lastOpenedTimestamp": 1,



"lastResolvedTimestamp": 1,



"lastUpdatedTimestamp": 1,



"managementZones": [



{



"id": "string",



"name": "string"



}



],



"muted": true,



"packageName": "string",



"riskAssessment": {



"assessmentAccuracy": "FULL",



"assessmentAccuracyDetails": {



"reducedReasons": [



"LIMITED_AGENT_SUPPORT"



]



},



"baseRiskLevel": "CRITICAL",



"baseRiskScore": 1,



"baseRiskVector": "string",



"dataAssets": "NOT_AVAILABLE",



"exposure": "NOT_AVAILABLE",



"publicExploit": "AVAILABLE",



"riskLevel": "CRITICAL",



"riskScore": 1,



"riskVector": "string",



"vulnerableFunctionUsage": "IN_USE"



},



"securityProblemId": "string",



"status": "OPEN",



"technology": "DOTNET",



"title": "string",



"url": "string",



"vulnerabilityType": "CODE_LEVEL"



}



],



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

Query for top ten open vulnerabilities sorted by risk score in descending order.

Required filters:

* `fields=%2BriskAssessment`
* `securityProblemSelector=status(OPEN)`
* `sort=-riskAssessment.riskScore`

#### Curl

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems?pageSize=10&fields=%2BriskAssessment&securityProblemSelector=status(OPEN)&sort=-riskAssessment.riskScore' \



-H 'Authorization: Api-Token [your_token]' \



-H 'Accept: application/json'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems?pageSize=10&fields=%2BriskAssessment&securityProblemSelector=status(OPEN)&sort=-riskAssessment.riskScore
```

#### Response body

```
{



"totalCount": 306,



"pageSize": 10,



"nextPageKey": "vu8XQiDj3q0SIU59KgHvowAAAX_qbpspAAABgITtYykAAAAKAQAxc3RhdHVzKE9QRU4pLCB2dWxuZXJhYmlsaXR5VHlwZShUSElSRF9QQVJUWV9TTllLKQI0VT4tJAUu9QMBAQEAAzguNjRVPi0kBS71AgEBAQATNzY3ODM5MzU0NDcwOTM2NjkzMAEADytyaXNrQXNzZXNzbWVudL7vF0Ig496t",



"securityProblems": [



{



"securityProblemId": "11497873967941161718",



"displayId": "S-3454",



"status": "OPEN",



"muted": true,



"externalVulnerabilityId": "SNYK-JAVA-ORGAPACHELOGGINGLOG4J-2314720",



"vulnerabilityType": "THIRD_PARTY",



"title": "Remote Code Execution (RCE)",



"packageName": "org.apache.logging.log4j:log4j-core",



"url": "https://mySampleEnv.live.dynatrace.com/ui/security/problem/11497873967941161718",



"technology": "JAVA",



"firstSeenTimestamp": 1639135014832,



"lastUpdatedTimestamp": 1651497109253,



"riskAssessment": {



"riskLevel": "CRITICAL",



"riskScore": 10.0,



"riskVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H",



"baseRiskLevel": "CRITICAL",



"baseRiskScore": 10.0,



"baseRiskVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H/E:H",



"exposure": "PUBLIC_NETWORK",



"dataAssets": "REACHABLE",



"publicExploit": "AVAILABLE",



"vulnerableFunctionUsage": "NOT_AVAILABLE"



},



"cveIds": [



"CVE-2021-44228"



]



},



{



"securityProblemId": "7968806720724378002",



"displayId": "S-3352",



"status": "OPEN",



"muted": true,



"externalVulnerabilityId": "SNYK-JAVA-CHQOSLOGBACK-31407",



"vulnerabilityType": "THIRD_PARTY",



"title": "Arbitrary Code Execution",



"packageName": "ch.qos.logback:logback-classic",



"url": "https://mySampleEnv.live.dynatrace.com/ui/security/problem/7968806720724378002",



"technology": "JAVA",



"firstSeenTimestamp": 1629276816755,



"lastUpdatedTimestamp": 1651497109253,



"riskAssessment": {



"riskLevel": "CRITICAL",



"riskScore": 9.8,



"riskVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",



"baseRiskLevel": "CRITICAL",



"baseRiskScore": 9.8,



"baseRiskVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",



"exposure": "PUBLIC_NETWORK",



"dataAssets": "REACHABLE",



"publicExploit": "NOT_AVAILABLE",



"vulnerableFunctionUsage": "NOT_AVAILABLE"



},



"cveIds": [



"CVE-2017-5929"



]



},



{



"securityProblemId": "13131808379454186608",



"displayId": "S-3343",



"status": "OPEN",



"muted": true,



"externalVulnerabilityId": "SNYK-JAVA-CHQOSLOGBACK-30208",



"vulnerabilityType": "THIRD_PARTY",



"title": "Arbitrary Code Execution",



"packageName": "ch.qos.logback:logback-core",



"url": "https://mySampleEnv.live.dynatrace.com/ui/security/problem/13131808379454186608",



"technology": "JAVA",



"firstSeenTimestamp": 1629276816755,



"lastUpdatedTimestamp": 1651497109253,



"riskAssessment": {



"riskLevel": "CRITICAL",



"riskScore": 9.8,



"riskVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",



"baseRiskLevel": "CRITICAL",



"baseRiskScore": 9.8,



"baseRiskVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",



"exposure": "PUBLIC_NETWORK",



"dataAssets": "REACHABLE",



"publicExploit": "NOT_AVAILABLE",



"vulnerableFunctionUsage": "NOT_AVAILABLE"



},



"cveIds": [



"CVE-2017-5929"



]



},



{



"securityProblemId": "13080692565938470532",



"displayId": "S-3342",



"status": "OPEN",



"muted": true,



"externalVulnerabilityId": "SNYK-JAVA-ORGAPACHELOGGINGLOG4J-31409",



"vulnerabilityType": "THIRD_PARTY",



"title": "Deserialization of Untrusted Data",



"packageName": "org.apache.logging.log4j:log4j-core",



"url": "https://mySampleEnv.live.dynatrace.com/ui/security/problem/13080692565938470532",



"technology": "JAVA",



"firstSeenTimestamp": 1629276816755,



"lastUpdatedTimestamp": 1651497109253,



"riskAssessment": {



"riskLevel": "CRITICAL",



"riskScore": 9.8,



"riskVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",



"baseRiskLevel": "CRITICAL",



"baseRiskScore": 9.8,



"baseRiskVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:F",



"exposure": "PUBLIC_NETWORK",



"dataAssets": "REACHABLE",



"publicExploit": "AVAILABLE",



"vulnerableFunctionUsage": "NOT_AVAILABLE"



},



"cveIds": [



"CVE-2017-5645"



]



},



{



"securityProblemId": "12458843765122204362",



"displayId": "S-3337",



"status": "OPEN",



"muted": true,



"externalVulnerabilityId": "SNYK-JAVA-LOG4J-572732",



"vulnerabilityType": "THIRD_PARTY",



"title": "Deserialization of Untrusted Data",



"packageName": "log4j:log4j",



"url": "https://mySampleEnv.live.dynatrace.com/ui/security/problem/12458843765122204362",



"technology": "JAVA",



"firstSeenTimestamp": 1629276816755,



"lastUpdatedTimestamp": 1651497109253,



"riskAssessment": {



"riskLevel": "CRITICAL",



"riskScore": 9.8,



"riskVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",



"baseRiskLevel": "CRITICAL",



"baseRiskScore": 9.8,



"baseRiskVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:P",



"exposure": "PUBLIC_NETWORK",



"dataAssets": "REACHABLE",



"publicExploit": "AVAILABLE",



"vulnerableFunctionUsage": "NOT_AVAILABLE"



},



"cveIds": [



"CVE-2019-17571"



]



},



{



"securityProblemId": "10489033029364122206",



"displayId": "S-3457",



"status": "OPEN",



"muted": false,



"externalVulnerabilityId": "SNYK-JAVA-ORGAPACHELOGGINGLOG4J-2320014",



"vulnerabilityType": "THIRD_PARTY",



"title": "Remote Code Execution (RCE)",



"packageName": "org.apache.logging.log4j:log4j-core",



"url": "https://mySampleEnv.live.dynatrace.com/ui/security/problem/10489033029364122206",



"technology": "JAVA",



"firstSeenTimestamp": 1639510404699,



"lastUpdatedTimestamp": 1651497109253,



"riskAssessment": {



"riskLevel": "CRITICAL",



"riskScore": 9.0,



"riskVector": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H",



"baseRiskLevel": "CRITICAL",



"baseRiskScore": 9.0,



"baseRiskVector": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H/E:P/RL:O/RC:C",



"exposure": "PUBLIC_NETWORK",



"dataAssets": "REACHABLE",



"publicExploit": "AVAILABLE",



"vulnerableFunctionUsage": "NOT_AVAILABLE"



},



"cveIds": [



"CVE-2021-45046"



]



},



{



"securityProblemId": "16904121786356925180",



"displayId": "S-3534",



"status": "OPEN",



"muted": true,



"externalVulnerabilityId": "SNYK-JAVA-ORGAPACHESTRUTS-30207",



"vulnerabilityType": "THIRD_PARTY",



"title": "Arbitrary Code Execution",



"packageName": "org.apache.struts:struts2-core",



"url": "https://mySampleEnv.live.dynatrace.com/ui/security/problem/16904121786356925180",



"technology": "JAVA",



"firstSeenTimestamp": 1647434489381,



"lastUpdatedTimestamp": 1651497109253,



"riskAssessment": {



"riskLevel": "HIGH",



"riskScore": 8.8,



"riskVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H/MAV:A/MC:L/MI:L",



"baseRiskLevel": "CRITICAL",



"baseRiskScore": 10.0,



"baseRiskVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H/E:F/RL:O/RC:C",



"exposure": "NOT_DETECTED",



"dataAssets": "NOT_DETECTED",



"publicExploit": "AVAILABLE",



"vulnerableFunctionUsage": "IN_USE"



},



"cveIds": [



"CVE-2017-5638"



]



},



{



"securityProblemId": "13912219969549620585",



"displayId": "S-3315",



"status": "OPEN",



"muted": false,



"externalVulnerabilityId": "SNYK-JAVA-COMGOOGLEPROTOBUF-173761",



"vulnerabilityType": "THIRD_PARTY",



"title": "Integer Overflow",



"packageName": "com.google.protobuf:protobuf-java",



"url": "https://mySampleEnv.live.dynatrace.com/ui/security/problem/13912219969549620585",



"technology": "JAVA",



"firstSeenTimestamp": 1629276761566,



"lastUpdatedTimestamp": 1651497109253,



"riskAssessment": {



"riskLevel": "HIGH",



"riskScore": 8.8,



"riskVector": "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H",



"baseRiskLevel": "HIGH",



"baseRiskScore": 8.8,



"baseRiskVector": "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H",



"exposure": "PUBLIC_NETWORK",



"dataAssets": "REACHABLE",



"publicExploit": "NOT_AVAILABLE",



"vulnerableFunctionUsage": "NOT_AVAILABLE"



},



"cveIds": [



"CVE-2015-5237"



]



},



{



"securityProblemId": "1340823583484240022",



"displayId": "S-3630",



"status": "OPEN",



"muted": true,



"externalVulnerabilityId": "SNYK-JAVA-ORGSPRINGFRAMEWORK-2436751",



"vulnerabilityType": "THIRD_PARTY",



"title": "Remote Code Execution",



"packageName": "org.springframework:spring-beans",



"url": "https://mySampleEnv.live.dynatrace.com/ui/security/problem/1340823583484240022",



"technology": "JAVA",



"firstSeenTimestamp": 1648683464474,



"lastUpdatedTimestamp": 1651497109253,



"riskAssessment": {



"riskLevel": "HIGH",



"riskScore": 8.8,



"riskVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/MAV:A",



"baseRiskLevel": "CRITICAL",



"baseRiskScore": 9.8,



"baseRiskVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:F",



"exposure": "NOT_DETECTED",



"dataAssets": "REACHABLE",



"publicExploit": "AVAILABLE",



"vulnerableFunctionUsage": "IN_USE"



},



"cveIds": [



"CVE-2022-22965"



]



},



{



"securityProblemId": "7678393544709366930",



"displayId": "S-3252",



"status": "OPEN",



"muted": false,



"externalVulnerabilityId": "SNYK-JAVA-ORGSPRINGFRAMEWORK-1009832",



"vulnerabilityType": "THIRD_PARTY",



"title": "Improper Input Validation",



"packageName": "org.springframework:spring-web",



"url": "https://mySampleEnv.live.dynatrace.com/ui/security/problem/7678393544709366930",



"technology": "JAVA",



"firstSeenTimestamp": 1629277776755,



"lastUpdatedTimestamp": 1651497109253,



"riskAssessment": {



"riskLevel": "HIGH",



"riskScore": 8.6,



"riskVector": "CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H",



"baseRiskLevel": "HIGH",



"baseRiskScore": 8.6,



"baseRiskVector": "CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H",



"exposure": "NOT_DETECTED",



"dataAssets": "REACHABLE",



"publicExploit": "NOT_AVAILABLE",



"vulnerableFunctionUsage": "NOT_IN_USE"



},



"cveIds": [



"CVE-2020-5421"



]



}



]



}
```

## Related topics

* [Application Security](/managed/secure/application-security "Access the Dynatrace Application Security functionalities.")
* [Davis Security Advisor API](/managed/dynatrace-api/environment-api/application-security/davis-security-advice "View the Davis Security Advisor recommendations via Dynatrace API.")