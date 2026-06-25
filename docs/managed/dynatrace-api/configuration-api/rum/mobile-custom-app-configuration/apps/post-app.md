---
title: Mobile and custom app API - POST an app
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/apps/post-app
scraped: 2026-05-12T11:15:32.993290
---

# Mobile and custom app API - POST an app

# Mobile and custom app API - POST an app

* Reference
* Published Nov 05, 2020

Creates a new mobile or custom app.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [NewMobileCustomAppConfig](#openapi-definition-NewMobileCustomAppConfig) | The JSON body of the request. Contains the parameters of the new mobile or custom application. | body | Optional |

### Request body objects

#### The `NewMobileCustomAppConfig` object

Configuration of a mobile or custom application to be created.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| apdexSettings | [MobileCustomApdex](#openapi-definition-MobileCustomApdex) | Apdex configuration of a mobile or custom application.  A duration less than the **tolerable** threshold is considered satisfied. | Optional |
| applicationId | string | The UUID of the application.  It is used only by OneAgent to send data to Dynatrace. | Optional |
| applicationType | string | The type of the application. The element can hold these values * `CUSTOM_APPLICATION` * `MOBILE_APPLICATION` | Required |
| beaconEndpointType | string | The type of the beacon endpoint. The element can hold these values * `CLUSTER_ACTIVE_GATE` * `ENVIRONMENT_ACTIVE_GATE` * `INSTRUMENTED_WEB_SERVER` | Optional |
| beaconEndpointUrl | string | The URL of the beacon endpoint.  Only applicable when the **beaconEndpointType** is set to `ENVIRONMENT_ACTIVE_GATE` or `INSTRUMENTED_WEB_SERVER`. | Optional |
| costControlUserSessionPercentage | integer | The percentage of user sessions to be analyzed. | Optional |
| iconType | string | Custom application icon.  Mobile apps always use the mobile device icon, so this icon can only be set for custom apps. The element can hold these values * `AMAZON_ECHO` * `DESKTOP` * `EMBEDDED` * `IOT` * `MICROSOFT_HOLOLENS` * `UFO` * `USERS` | Optional |
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
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Success. The application has been created. The response contains the identifier and name of the new application. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **409** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The applicationId is already used by another application. |

### Response body objects

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

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



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



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

## Validate payload

We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/validator` |

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