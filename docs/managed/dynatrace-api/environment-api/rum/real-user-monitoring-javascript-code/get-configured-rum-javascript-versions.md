---
title: RUM JavaScript API - GET configured RUM JavaScript versions
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-configured-rum-javascript-versions
scraped: 2026-05-12T11:56:01.432277
---

# RUM JavaScript API - GET configured RUM JavaScript versions

# RUM JavaScript API - GET configured RUM JavaScript versions

* Reference
* Published Apr 15, 2025

Returns the latest stable, previous stable, and custom RUM JavaScript versions configured on the environment.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/rum/jsConfiguredVersions` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/rum/jsConfiguredVersions` |

## Authentication

To execute this request, you need an access token with `RumJavaScriptTagManagement` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ConfiguredVersions](#openapi-definition-ConfiguredVersions) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ConfiguredVersions` object

Configured LATEST\_STABLE, PREVIOUS\_STABLE and CUSTOM RUM JavaScript versions.

| Element | Type | Description |
| --- | --- | --- |
| custom | integer | The custom configured version of the RUM JavaScript. |
| latestIE11Supported | integer | The latest IE11 supported version of the RUM JavaScript. |
| latestIESupported | integer | The latest IE7-10 supported version of the RUM JavaScript. |
| latestStable | integer | The latest stable version of the RUM JavaScript. |
| previousStable | integer | The previous stable version of the RUM JavaScript. |

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



"latestStable": 10156181011154334,



"previousStable": 10156181011154332,



"latestIESupported": 10155181011154332,



"custom": 10156181011154330



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

In this example, the request inquires the versions of the RUM JavaScript configured on the environment.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/rum/jsConfiguredVersions \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/rum/jsConfiguredVersions
```

#### Response body

```
{



"latestStable": 10156181011154334,



"previousStable": 10156181011154332,



"latestIESupported": 10155181011154332,



"custom": 10156181011154330



}
```

#### Response code

200