---
title: "Davis Security Advisor API"
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/application-security/davis-security-advice
updated: 2026-02-09
---

# Davis Security Advisor API

# Davis Security Advisor API

* Reference
* Updated on May 03, 2022

The **Davis Security Advisor** API lists [Davis recommendations](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-advisor "Get recommendations for security fixes from Davis Security Advisor.") related to open and unmuted [vulnerabilities](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities "Monitor the security issues of your third-party libraries.").

You can limit the output by using the pagination:

1. Specify the number of results per page in the **pageSize** query parameter.
2. Then use the cursor from the **nextPageKey** field of the previous response in the **nextPageKey** query parameter to obtain subsequent pages.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/davis/securityAdvices` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/davis/securityAdvices` |

## Authentication

To execute this request, you need an access token with `securityProblems.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| managementZoneFilter | string | To specify management zones, use one of the options listed below. For each option you can specify multiple comma-separated values. If several values are specified, the **OR** logic applies. All values are case-sensitive and must be quoted.  * Management zone ID: ids("mzId-1", "mzId-2"). * Management zone names: names("mz-1", "mz-2").  You can specify several comma-separated criteria (for example, `names("myMz"),ids("9130632296508575249")`). | query | Optional |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **nextPageKey** field of the previous response.  The first page is always returned if you don't specify the **nextPageKey** query parameter.  When the **nextPageKey** is set to obtain subsequent pages, you must omit all other query parameters. | query | Optional |
| pageSize | integer | The amount of security advices in a single response payload.  The maximal allowed page size is 500.  If not set, 5 is used. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [DavisSecurityAdviceList](#openapi-definition-DavisSecurityAdviceList) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `DavisSecurityAdviceList` object

A list of advice from the Davis security advisor.

| Element | Type | Description |
| --- | --- | --- |
| advices | [DavisSecurityAdvice[]](#openapi-definition-DavisSecurityAdvice) | - |
| nextPageKey | string | The cursor for the next page of results. Has the value of `null` on the last page.  Use it in the **nextPageKey** query parameter to obtain subsequent pages of the result. |
| pageSize | integer | The number of entries per page. |
| totalCount | integer | The total number of entries in the result. |

#### The `DavisSecurityAdvice` object

Security advice from the Davis security advisor.

| Element | Type | Description |
| --- | --- | --- |
| adviceType | string | The type of the advice. The element can hold these values * `UPGRADE` |
| critical | string[] | IDs of `critical` level [security problemsï»¿](https://dt-url.net/p103u1h) caused by vulnerable component. |
| high | string[] | IDs of `high` level [security problemsï»¿](https://dt-url.net/p103u1h) caused by vulnerable component. |
| low | string[] | IDs of `low` level [security problemsï»¿](https://dt-url.net/p103u1h) caused by vulnerable component. |
| medium | string[] | IDs of `medium` level [security problemsï»¿](https://dt-url.net/p103u1h) caused by vulnerable component. |
| name | string | The name of the advice. |
| none | string[] | IDs of `none` level [security problemsï»¿](https://dt-url.net/p103u1h) caused by vulnerable component. |
| technology | string | The technology of the vulnerable component. The element can hold these values * `DOTNET` * `GO` * `JAVA` * `KUBERNETES` * `NODE_JS` * `PHP` * `PYTHON` |
| vulnerableComponent | string | The vulnerable component to which advice applies. |

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



"advices": [



{



"adviceType": "UPGRADE",



"critical": [



"string"



],



"high": [



"string"



],



"low": [



"string"



],



"medium": [



"string"



],



"name": "string",



"none": [



"string"



],



"technology": "DOTNET",



"vulnerableComponent": "string"



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
* [Vulnerabilities API](/managed/dynatrace-api/environment-api/application-security/vulnerabilities "Find out what the vulnerabilities API offers.")
