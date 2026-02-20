---
title: RUM cookie names API - GET cookie names
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/rum/rum-cookie-names-get-cookie-names
scraped: 2026-02-20T21:26:57.769563
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