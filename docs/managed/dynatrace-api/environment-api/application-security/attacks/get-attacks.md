---
title: Attacks API - GET all attacks
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/application-security/attacks/get-attacks
scraped: 2026-05-12T11:58:03.842060
---

# Attacks API - GET all attacks

# Attacks API - GET all attacks

* Reference
* Published Aug 30, 2023

Lists all detected [attacks](/managed/secure/application-security/application-protection/manage-attacks "Monitor the attacks on your application code.") on your applications.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/attacks` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/attacks` |

## Authentication

To execute this request, you need an access token with `attacks.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **nextPageKey** field of the previous response.  The first page is always returned if you don't specify the **nextPageKey** query parameter.  When the **nextPageKey** is set to obtain subsequent pages, you must omit all other query parameters. | query | Optional |
| pageSize | integer | The amount of attacks in a single response payload.  The maximal allowed page size is 500.  If not set, 100 is used. | query | Optional |
| attackSelector | string | Defines the scope of the query. Only attacks matching the specified criteria are included in the response. You can add one or more of the following criteria. Values are *not* case-sensitive and the `EQUALS` operator is used unless otherwise specified.  * State: `state("value")`. The state of the attack. Possible values are `EXPLOITED`, `BLOCKED`, and `ALLOWLISTED`. * Attack Type: `attackType("value")`. The type of the attack. Find the possible values in the description of the **attackType** field of the response. * Country Code: `countryCode("value")`. The country code of the attacker. Supported values include all ISO-3166-1 alpha-2 country codes (2-letter). Supplying empty filter value `countryCode()` will return attacks, where location is not available. * Request path contains: `requestPathContains("value")`. Filters for a substring in the request path. The `CONTAINS` operator is used. A maximum of 48 characters are allowed. * Process group name contains: `processGroupNameContains("value")`. Filters for a substring in the targeted process group's name. The `CONTAINS` operator is used. * Vulnerability ID: `vulnerabilityId("123456789")`. The exact ID of the vulnerability. * Source IPs: `sourceIps("93.184.216.34", "63.124.6.12")`. The exact IPv4/IPv6 addresses of the attacker. * Management zone ID: `managementZoneIds("mzId-1", "mzId-2")`. * Management zone name: `managementZones("name-1", "name-2")`. Values are case sensitive. * Technology: `technology("technology-1", "technology-2")`. Find the possible values in the description of the **technology** field of the response. The `EQUALS` operator is used.  To set several criteria, separate them with a comma (`,`). Only results matching (**all** criteria are included in the response.  Specify the value of a criterion as a quoted string. The following special characters must be escaped with a tilde (`~`) inside quotes:  * Tilde `~` * Quote `"` | query | Optional |
| sort | string | Specifies one or more fields for sorting the attack list. Multiple fields can be concatenated using a comma (`,`) as a separator (e.g. `+state,-timestamp`).  You can sort by the following properties with a sign prefix for the sorting order.  * `displayId`: The attack's display ID. * `displayName`: The attack's display name. * `attackType`: The type of the attack (e.g. SQL\_INJECTION, JNDI\_INJECTION, etc.). * `state`: The state of the attack. (`+` low severity state first `-` high severity state first) * `sourceIp`: The IP address of the attacker. Sorts by the numerical IP value. * `requestPath`: The request path where the attack was started. * `timestamp`: When the attack was executed. (`+` old attacks first or `-` new attacks first)   If no prefix is set, `+` is used. | query | Optional |
| fields | string | A list of additional attack properties you can add to the response.  The following properties are available (all other properties are always included and you can't remove them from the response):  * `attackTarget`: The targeted host/database of an attack. * `request`: The request that was sent from the attacker. * `entrypoint`: The entry point used by an attacker to start a specific attack. * `vulnerability`: The vulnerability utilized by the attack. * `securityProblem`: The related security problem. * `attacker`: The attacker of an attack. * `managementZones`: The related management zones. * `affectedEntities`: The affected entities of an attack.  To add properties, specify them in a comma-separated list and prefix each property with a plus (for example, `+attackTarget,+securityProblem`). | query | Optional |
| from | string | The start of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the relative timeframe of thirty days is used (`now-30d`). | query | Optional |
| to | string | The end of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the current timestamp is used. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [AttackList](#openapi-definition-AttackList) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `AttackList` object

A list of attacks.

| Element | Type | Description |
| --- | --- | --- |
| attacks | [Attack[]](#openapi-definition-Attack) | A list of attacks. |
| nextPageKey | string | The cursor for the next page of results. Has the value of `null` on the last page.  Use it in the **nextPageKey** query parameter to obtain subsequent pages of the result. |
| pageSize | integer | The number of entries per page. |
| totalCount | integer | The total number of entries in the result. |

#### The `Attack` object

Describes an attack.

| Element | Type | Description |
| --- | --- | --- |
| affectedEntities | [AffectedEntities](#openapi-definition-AffectedEntities) | Information about affected entities of an attack. |
| attackId | string | The ID of the attack. |
| attackTarget | [AttackTarget](#openapi-definition-AttackTarget) | Information about the targeted host/database of an attack. |
| attackType | string | The type of the attack. The element can hold these values * `COMMAND_INJECTION` * `JNDI_INJECTION` * `SQL_INJECTION` * `SSRF` |
| attacker | [Attacker](#openapi-definition-Attacker) | Attacker of an attack. |
| displayId | string | The display ID of the attack. |
| displayName | string | The display name of the attack. |
| entrypoint | [AttackEntrypoint](#openapi-definition-AttackEntrypoint) | Describes the entrypoint used by an attacker to start a specific attack. |
| managementZones | [ManagementZone[]](#openapi-definition-ManagementZone) | A list of management zones which the affected entities belong to. |
| request | [RequestInformation](#openapi-definition-RequestInformation) | Describes the complete request information of an attack. |
| securityProblem | [AttackSecurityProblem](#openapi-definition-AttackSecurityProblem) | Assessment information and the ID of a security problem related to an attack. |
| state | string | The state of the attack. The element can hold these values * `ALLOWLISTED` * `BLOCKED` * `EXPLOITED` |
| technology | string | The technology of the attack. The element can hold these values * `DOTNET` * `GO` * `JAVA` * `NODE_JS` |
| timestamp | integer | The timestamp when the attack occurred. |
| vulnerability | [Vulnerability](#openapi-definition-Vulnerability) | Describes the exploited vulnerability. |

#### The `AffectedEntities` object

Information about affected entities of an attack.

| Element | Type | Description |
| --- | --- | --- |
| processGroup | [AffectedEntity](#openapi-definition-AffectedEntity) | Information about an affected entity. |
| processGroupInstance | [AffectedEntity](#openapi-definition-AffectedEntity) | Information about an affected entity. |

#### The `AffectedEntity` object

Information about an affected entity.

| Element | Type | Description |
| --- | --- | --- |
| id | string | The monitored entity ID of the affected entity. |
| name | string | The name of the affected entity. |

#### The `AttackTarget` object

Information about the targeted host/database of an attack.

| Element | Type | Description |
| --- | --- | --- |
| entityId | string | The monitored entity ID of the targeted host/database. |
| name | string | The name of the targeted host/database. |

#### The `Attacker` object

Attacker of an attack.

| Element | Type | Description |
| --- | --- | --- |
| location | [AttackerLocation](#openapi-definition-AttackerLocation) | Location of an attacker. |
| sourceIp | string | The source IP of the attacker. |

#### The `AttackerLocation` object

Location of an attacker.

| Element | Type | Description |
| --- | --- | --- |
| city | string | City of the attacker. |
| country | string | The country of the attacker. |
| countryCode | string | The country code of the country of the attacker, according to the ISO 3166-1 Alpha-2 standard. |

#### The `AttackEntrypoint` object

Describes the entrypoint used by an attacker to start a specific attack.

| Element | Type | Description |
| --- | --- | --- |
| codeLocation | [CodeLocation](#openapi-definition-CodeLocation) | Information about a code location. |
| entrypointFunction | [FunctionDefinition](#openapi-definition-FunctionDefinition) | Information about a function definition. |
| payload | object[] | A list of values that has possibly been truncated. |

#### The `CodeLocation` object

Information about a code location.

| Element | Type | Description |
| --- | --- | --- |
| className | string | The fully qualified class name of the code location. |
| columnNumber | integer | The column number of the code location. |
| displayName | string | A human readable string representation of the code location. |
| fileName | string | The file name of the code location. |
| functionName | string | The function/method name of the code location. |
| lineNumber | integer | The line number of the code location. |
| parameterTypes | [TruncatableListString](#openapi-definition-TruncatableListString) | A list of values that has possibly been truncated. |
| returnType | string | The return type of the function. |

#### The `TruncatableListString` object

A list of values that has possibly been truncated.

| Element | Type | Description |
| --- | --- | --- |
| truncationInfo | [TruncationInfo](#openapi-definition-TruncationInfo) | Information on a possible truncation. |
| values | string[] | Values of the list. |

#### The `TruncationInfo` object

Information on a possible truncation.

| Element | Type | Description |
| --- | --- | --- |
| truncated | boolean | If the list/value has been truncated. |

#### The `FunctionDefinition` object

Information about a function definition.

| Element | Type | Description |
| --- | --- | --- |
| className | string | The fully qualified class name of the class that includes the function. |
| displayName | string | A human readable string representation of the function definition. |
| fileName | string | The file name of the function definition. |
| functionName | string | The function/method name of the function definition. |
| parameterTypes | [TruncatableListString](#openapi-definition-TruncatableListString) | A list of values that has possibly been truncated. |
| returnType | string | The return type of the function. |

#### The `EntrypointPayload` object

Describes a payload sent to an entrypoint during an attack.

| Element | Type | Description |
| --- | --- | --- |
| name | string | Name of the payload, if applicable. |
| type | string | Type of the payload. The element can hold these values * `HTTP_BODY` * `HTTP_COOKIE` * `HTTP_HEADER_NAME` * `HTTP_HEADER_VALUE` * `HTTP_OTHER` * `HTTP_PARAMETER_NAME` * `HTTP_PARAMETER_VALUE` * `HTTP_URL` * `UNKNOWN` |
| value | string | Value of the payload. |

#### The `ManagementZone` object

A short representation of a management zone.

| Element | Type | Description |
| --- | --- | --- |
| id | string | The ID of the management zone. |
| name | string | The name of the management zone. |

#### The `RequestInformation` object

Describes the complete request information of an attack.

| Element | Type | Description |
| --- | --- | --- |
| host | string | The target host of the request. |
| path | string | The request path. |
| protocolDetails | [ProtocolDetails](#openapi-definition-ProtocolDetails) | Details that are specific to the used protocol. |
| url | string | The requested URL. |

#### The `ProtocolDetails` object

Details that are specific to the used protocol.

| Element | Type | Description |
| --- | --- | --- |
| http | [HttpProtocolDetails](#openapi-definition-HttpProtocolDetails) | HTTP specific request details. |

#### The `HttpProtocolDetails` object

HTTP specific request details.

| Element | Type | Description |
| --- | --- | --- |
| headers | [TruncatableListAttackRequestHeader](#openapi-definition-TruncatableListAttackRequestHeader) | A list of values that has possibly been truncated. |
| parameters | [TruncatableListHttpRequestParameter](#openapi-definition-TruncatableListHttpRequestParameter) | A list of values that has possibly been truncated. |
| requestMethod | string | The HTTP request method. |

#### The `TruncatableListAttackRequestHeader` object

A list of values that has possibly been truncated.

| Element | Type | Description |
| --- | --- | --- |
| truncationInfo | [TruncationInfo](#openapi-definition-TruncationInfo) | Information on a possible truncation. |
| values | [AttackRequestHeader[]](#openapi-definition-AttackRequestHeader) | Values of the list. |

#### The `AttackRequestHeader` object

A header element of the attack's request.

| Element | Type | Description |
| --- | --- | --- |
| name | string | The name of the header element. |
| value | string | The value of the header element. |

#### The `TruncatableListHttpRequestParameter` object

A list of values that has possibly been truncated.

| Element | Type | Description |
| --- | --- | --- |
| truncationInfo | [TruncationInfo](#openapi-definition-TruncationInfo) | Information on a possible truncation. |
| values | [HttpRequestParameter[]](#openapi-definition-HttpRequestParameter) | Values of the list. |

#### The `HttpRequestParameter` object

An HTTP request parameter.

| Element | Type | Description |
| --- | --- | --- |
| name | string | The name of the parameter. |
| value | string | The value of the parameter. |

#### The `AttackSecurityProblem` object

Assessment information and the ID of a security problem related to an attack.

| Element | Type | Description |
| --- | --- | --- |
| assessment | [AttackSecurityProblemAssessmentDto](#openapi-definition-AttackSecurityProblemAssessmentDto) | The assessment of a security problem related to an attack. |
| securityProblemId | string | The security problem ID. |

#### The `AttackSecurityProblemAssessmentDto` object

The assessment of a security problem related to an attack.

| Element | Type | Description |
| --- | --- | --- |
| dataAssets | string | The reachability of data assets by the attacked target. The element can hold these values * `NOT_AVAILABLE` * `NOT_DETECTED` * `REACHABLE` |
| exposure | string | The level of exposure of the attacked target The element can hold these values * `NOT_AVAILABLE` * `NOT_DETECTED` * `PUBLIC_NETWORK` |
| numberOfReachableDataAssets | integer | The number of data assets reachable by the attacked target. |

#### The `Vulnerability` object

Describes the exploited vulnerability.

| Element | Type | Description |
| --- | --- | --- |
| codeLocation | [CodeLocation](#openapi-definition-CodeLocation) | Information about a code location. |
| displayName | string | The display name of the vulnerability. |
| vulnerabilityId | string | The id of the vulnerability. |
| vulnerableFunction | [FunctionDefinition](#openapi-definition-FunctionDefinition) | Information about a function definition. |
| vulnerableFunctionInput | [VulnerableFunctionInput](#openapi-definition-VulnerableFunctionInput) | Describes what got passed into the code level vulnerability. |

#### The `VulnerableFunctionInput` object

Describes what got passed into the code level vulnerability.

| Element | Type | Description |
| --- | --- | --- |
| inputSegments | [VulnerableFunctionInputSegment[]](#openapi-definition-VulnerableFunctionInputSegment) | A list of input segments. |
| type | string | The type of the input. The element can hold these values * `COMMAND` * `HTTP_CLIENT` * `JNDI` * `SQL_STATEMENT` |

#### The `VulnerableFunctionInputSegment` object

Describes one segment that was passed into a vulnerable function.

| Element | Type | Description |
| --- | --- | --- |
| type | string | The type of the input segment. The element can hold these values * `MALICIOUS_INPUT` * `REGULAR_INPUT` * `TAINTED_INPUT` |
| value | string | The value of the input segment. |

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



"attacks": [



{



"affectedEntities": {



"processGroup": {



"id": "string",



"name": "string"



},



"processGroupInstance": {}



},



"attackId": "string",



"attackTarget": {



"entityId": "string",



"name": "string"



},



"attackType": "COMMAND_INJECTION",



"attacker": {



"location": {



"city": "string",



"country": "string",



"countryCode": "string"



},



"sourceIp": "string"



},



"displayId": "string",



"displayName": "string",



"entrypoint": {



"codeLocation": {



"className": "string",



"columnNumber": 1,



"displayName": "string",



"fileName": "string",



"functionName": "string",



"lineNumber": 1,



"parameterTypes": {



"truncationInfo": {



"truncated": true



},



"values": [



"string"



]



},



"returnType": "string"



},



"entrypointFunction": {



"className": "string",



"displayName": "string",



"fileName": "string",



"functionName": "string",



"parameterTypes": {},



"returnType": "string"



},



"payload": [



{



"truncationInfo": {},



"values": [



{



"name": "string",



"type": "HTTP_BODY",



"value": "string"



}



]



}



]



},



"managementZones": [



{



"id": "string",



"name": "string"



}



],



"request": {



"host": "string",



"path": "string",



"protocolDetails": {



"http": {



"headers": {



"truncationInfo": {},



"values": [



{



"name": "string",



"value": "string"



}



]



},



"parameters": {



"truncationInfo": {},



"values": [



{



"name": "string",



"value": "string"



}



]



},



"requestMethod": "string"



}



},



"url": "string"



},



"securityProblem": {



"assessment": {



"dataAssets": "NOT_AVAILABLE",



"exposure": "NOT_AVAILABLE",



"numberOfReachableDataAssets": 1



},



"securityProblemId": "string"



},



"state": "ALLOWLISTED",



"technology": "DOTNET",



"timestamp": 1,



"vulnerability": {



"codeLocation": {},



"displayName": "string",



"vulnerabilityId": "string",



"vulnerableFunction": {},



"vulnerableFunctionInput": {



"inputSegments": [



{



"type": "MALICIOUS_INPUT",



"value": "string"



}



],



"type": "COMMAND"



}



}



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

## Related topics

* [Application Security](/managed/secure/application-security "Access the Dynatrace Application Security functionalities.")
* [Davis Security Advisor API](/managed/dynatrace-api/environment-api/application-security/davis-security-advice "View the Davis Security Advisor recommendations via Dynatrace API.")
* [Manage attacks](/managed/secure/application-security/application-protection/manage-attacks "Monitor the attacks on your application code.")