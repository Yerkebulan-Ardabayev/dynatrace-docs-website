---
title: Mobile and custom app API - PUT an app
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/apps/put-app
scraped: 2026-05-12T11:15:38.277755
---

# Mobile and custom app API - PUT an app

# Mobile and custom app API - PUT an app

* Reference
* Published Nov 05, 2020

Updates the specified mobile or custom app.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{id}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{id}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The UUID of the required mobile or custom application. It can be found in the Instrumentation Wizard of your app. | path | Required |
| body | [MobileCustomAppConfig](#openapi-definition-MobileCustomAppConfig) | The JSON body of the request. Contains updated configuration of the mobile or custom application.  Do not set the identifier in the body. | body | Optional |

### Request body objects

#### The `MobileCustomAppConfig` object

Configuration of an existing mobile or custom application.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| apdexSettings | [MobileCustomApdex](#openapi-definition-MobileCustomApdex) | Apdex configuration of a mobile or custom application.  A duration less than the **tolerable** threshold is considered satisfied. | Required |
| applicationId | string | The UUID of the application.  It is used only by OneAgent to send data to Dynatrace. | Optional |
| applicationType | string | The type of the application. The element can hold these values * `CUSTOM_APPLICATION` * `MOBILE_APPLICATION` | Optional |
| beaconEndpointType | string | The type of the beacon endpoint. The element can hold these values * `CLUSTER_ACTIVE_GATE` * `ENVIRONMENT_ACTIVE_GATE` * `INSTRUMENTED_WEB_SERVER` | Required |
| beaconEndpointUrl | string | The URL of the beacon endpoint.  Only applicable when the **beaconEndpointType** is set to `ENVIRONMENT_ACTIVE_GATE` or `INSTRUMENTED_WEB_SERVER`. | Optional |
| costControlUserSessionPercentage | integer | The percentage of user sessions to be analyzed. | Required |
| iconType | string | Custom application icon.  Mobile apps always use the mobile device icon, so this icon can only be set for custom apps. The element can hold these values * `AMAZON_ECHO` * `DESKTOP` * `EMBEDDED` * `IOT` * `MICROSOFT_HOLOLENS` * `UFO` * `USERS` | Optional |
| identifier | string | The Dynatrace entity ID of the application. | Optional |
| name | string | The name of the application. | Required |
| optInModeEnabled | boolean | The opt-in mode is enabled (`true`) or disabled (`false`).  This value is only applicable to mobile and not to custom apps. | Optional |
| sessionReplayEnabled | boolean | The session replay is enabled (`true`) or disabled (`false`). This value is only applicable to mobile and not to custom apps. | Optional |
| sessionReplayOnCrashEnabled | boolean | **Deprecated**. Please use `sessionReplayEnabled` to enable or disable session replay for mobile apps. | Optional |

#### The `MobileCustomApdex` object

Apdex configuration of a mobile or custom application.

A duration less than the **tolerable** threshold is considered satisfied.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| frustratedOnError | boolean | Apdex error condition: if `true` the user session is considered frustrated when an error is reported. | Required |
| frustratingThreshold | integer | Apdex **frustrated** threshold, in milliseconds: a duration greater than or equal to this value is considered frustrated. | Required |
| toleratedThreshold | integer | Apdex **tolerable** threshold, in milliseconds: a duration greater than or equal to this value is considered tolerable. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"apdexSettings": {



"frustratedOnError": true,



"frustratingThreshold": 1,



"toleratedThreshold": 1



},



"applicationId": "string",



"applicationType": "CUSTOM_APPLICATION",



"beaconEndpointType": "CLUSTER_ACTIVE_GATE",



"beaconEndpointUrl": "string",



"costControlUserSessionPercentage": 1,



"iconType": "AMAZON_ECHO",



"identifier": "string",



"name": "string",



"optInModeEnabled": true,



"sessionReplayEnabled": true,



"sessionReplayOnCrashEnabled": true



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The application has been updated. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **404** | - | Failed. The specified entity doesn't exist. |

### Response body objects

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

## Validate payload

We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{id}/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{id}/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The submitted configuration is valid. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

#### Response body objects

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

#### Response body JSON models

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