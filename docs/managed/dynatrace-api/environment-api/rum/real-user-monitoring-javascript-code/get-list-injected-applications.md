---
title: RUM JavaScript API - GET list of injected applications
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-list-injected-applications
---

# RUM JavaScript API - GET list of injected applications

# RUM JavaScript API - GET list of injected applications

* Reference
* Updated on May 02, 2022

Lists all of your manually injected applications, along with their metadata.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/rum/manualApps` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/rum/manualApps` |

## Authentication

To execute this request, you need an access token with `RumJavaScriptTagManagement` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ManualApplication](#openapi-definition-ManualApplication)[] | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ResponseBody` object

#### The `ManualApplication` object

Parameters of a manually injected application.

| Element | Type | Description |
| --- | --- | --- |
| applicationId | string | The Dynatrace entity ID of the application. |
| displayName | string | The name of the application. |
| monitoringEnabled | boolean | Monitoring is enabled (`true`) or disabled (`false`). |
| revision | string | The application settings revision. |

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
[



{



"applicationId": "APPLICATION-C15B48CBCADC863B",



"displayName": "manually injected application",



"monitoringEnabled": true,



"revision": 1456380804910



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

In this example, the request inquires all the manually injected applications of the environment

The API token is passed in the **Authorization** header.

The result is truncated to three entries.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/rum/manualApps \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/rum/manualApps
```

#### Response body

```
[



{



"applicationId": "APPLICATION-BBFA55551D507E2B",



"displayName": "easyTravel Ionic Web",



"monitoringEnabled": true,



"revision": 1539076354681



},



{



"applicationId": "APPLICATION-31F18E1B2C50038A",



"displayName": "SaaS App Monitoring",



"monitoringEnabled": true,



"revision": 1536827568615



},



{



"applicationId": "APPLICATION-AE767ECC2D7B33BF",



"displayName": "Node JS demo",



"monitoringEnabled": true,



"revision": 1536827567516



}



]
```

#### Response code

200