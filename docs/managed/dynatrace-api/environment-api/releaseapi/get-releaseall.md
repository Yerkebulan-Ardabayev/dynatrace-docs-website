---
title: Releases API - GET releases
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/releaseapi/get-releaseall
scraped: 2026-05-12T11:55:50.023568
---

# Releases API - GET releases

# Releases API - GET releases

* Reference
* Published Apr 20, 2021

Lists all available releases.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/releases` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/releases` |

## Authentication

To execute this request, you need an access token with `releases.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| from | string | The start of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the relative timeframe of two weeks is used (`now-2w`). | query | Optional |
| to | string | The end of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the current timestamp is used. | query | Optional |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **nextPageKey** field of the previous response.  The first page is always returned if you don't specify the **nextPageKey** query parameter.  When the **nextPageKey** is set to obtain subsequent pages, you must omit all other query parameters. | query | Optional |
| pageSize | integer | The amount of Releases in a single response payload.  The maximal allowed page size is 1000.  If not set, 100 is used. | query | Optional |
| demo | boolean | Get your Releases (`false`) or a set of demo Releases (`true`). | query | Optional |
| releasesSelector | string | Defines the scope of the query. Only Releases matching the provided criteria are included in the response.  You can add one or several of the criteria listed below.  * Management zone: type(PROCESS\_GROUP\_INSTANCE),mzName("ManagementZone-A"). Filters for all releases in the given management zone. The filter is case-sensitive. * Monitoring state: monitoringState("Active") or monitoringState("Inactive"). You can specify only one monitoring state. * Health state: healthState("HEALTHY") or healthState("UNHEALTHY"). You can specify only one health state. * Security vulnerability: affectedBySecurityProblem("Detected") or affectedBySecurityProblem("Not detected"). You can specify only one security vulnerability state. * Name: entityName("name"). Filters for all releases that contain the given value in their name. The filter is case-insensitive. * Entity ID: entityId("id"). * Product: releasesProduct("product"). Filters for all releases that contain the given value in their product. The filter is case-insensitive. * Stage: releasesStage("stage"). Filters for all releases that contain the given value in their stage. The filter is case-insensitive. * Version: releasesVersion("version"). Filters for all releases that contain the given value in their version. The filter is case-insensitive.  To set several criteria, separate them with comma (,). Only results matching all criteria are included in the response. e.g., .../api/v2/releases?releasesSelector=name("Server"),monitoringState("Active"),healthState("HEALTHY"),releasesVersion("1.0.7").  The special characters ~ and " need to be escaped using a ~ (e.g. double quote search entityName("~""). | query | Optional |
| sort | string | Specifies the field that is used for sorting the releases list. The field has a sign prefix (+/-) which corresponds to the sorting order ('+' for ascending and '-' for descending). If no sign prefix is set, then the default ascending sorting order will be applied. You can sort by the following properties:  * 'product': Product name * 'name': Release name * 'stage': Stage name * 'version': Version * 'instances': Instances * 'traffic': Traffic  If not set, the ascending order sorting for name is applied. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [Releases](#openapi-definition-Releases) | Success |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `Releases` object

A list of releases.

| Element | Type | Description |
| --- | --- | --- |
| nextPageKey | string | The cursor for the next page of results. Has the value of `null` on the last page.  Use it in the **nextPageKey** query parameter to obtain subsequent pages of the result. |
| pageSize | integer | The number of entries per page. |
| releases | [Release[]](#openapi-definition-Release) | A list of releases. |
| releasesWithProblems | integer | Number of releases with problems. |
| totalCount | integer | The total number of entries in the result. |

#### The `Release` object

Contains data related to a single release of a component.
A Release is a combination of a component and a version.
A Component can be any form of deployable that can be associated with a version.
In the first draft, a Component is always a Service.

The tuple <name, product, stage, version> is always unique.

| Element | Type | Description |
| --- | --- | --- |
| affectedByProblems | boolean | The entity has one or more problems |
| affectedBySecurityVulnerabilities | boolean | The entity has one or more security vulnerabilities |
| instances | [ReleaseInstance[]](#openapi-definition-ReleaseInstance) | The instances entityIds included in this release |
| name | string | The entity name |
| problemCount | integer | The number of problems of the entity |
| product | string | The product name |
| releaseEntityId | string | The entity id of correlating release. |
| running | boolean | The related PGI is still running/monitored |
| securityVulnerabilitiesCount | integer | The number of security vulnerabilities of the entity |
| securityVulnerabilitiesEnabled | boolean | Indicates that the security vulnerabilities feature is enabled |
| softwareTechs | [SoftwareTechs[]](#openapi-definition-SoftwareTechs) | The software technologies of the release |
| stage | string | The stage name |
| throughput | number | The count of bytes per second of the entity |
| version | string | The identified release version |

#### The `ReleaseInstance` object

Contains data related to a single instance of a release.
An instance is a Process Group Instance and has an optional build version.

| Element | Type | Description |
| --- | --- | --- |
| buildVersion | string | The build version |
| entityId | string | The entity id of the instance. |
| problems | string[] | List of event Ids of open problems |
| securityVulnerabilities | string[] | List of Security vulnerabilities Ids |

#### The `SoftwareTechs` object

Contains information about the used software technology.

| Element | Type | Description |
| --- | --- | --- |
| edition | string | The edition of the technology. |
| technology | string | The type of the technology. |
| verbatimType | string | The verbatim type of the technology. |
| version | string | The version of the technology. |

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



"nextPageKey": "AQAAABQBAAAABQ==",



"pageSize": 1,



"releases": [



{



"affectedByProblems": true,



"affectedBySecurityVulnerabilities": true,



"instances": [



"PROCESS_GROUP_INSTANCE-49D94B90FB71C45B",



"PROCESS_GROUP_INSTANCE-7EA049157C82D1A5"



],



"name": "cluster",



"problemCount": 4,



"product": "Sockshop",



"releaseEntityId": "PROCESS_GROUP-DFDBAC9CBF104253",



"running": true,



"securityVulnerabilitiesCount": 4,



"securityVulnerabilitiesEnabled": true,



"softwareTechs": [



{



"edition": "OpenJDK",



"technology": "JAVA",



"verbatimType": "Java",



"version": "1.8.0_242"



}



],



"stage": "staging",



"throughput": 923234,



"version": "1.195.34.12341232423-012342"



}



],



"releasesWithProblems": 1,



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

* [Release monitoring](/managed/deliver/release-monitoring "Detect versions of monitored applications and analyze the software product lifecycle of your releases.")