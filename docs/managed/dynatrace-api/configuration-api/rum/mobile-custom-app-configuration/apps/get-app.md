---
title: Mobile and custom app API - GET an app
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/apps/get-app
---

# Mobile and custom app API - GET an app

# Mobile and custom app API - GET an app

* Reference
* Published Nov 05, 2020

Gets parameters of the specified mobile or custom app.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{id}` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The UUID of the required mobile or custom application. It can be found in the Instrumentation Wizard of your app. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [MobileCustomAppConfig](#openapi-definition-MobileCustomAppConfig) | Success |
| **404** | - | Failed. The specified entity doesn't exist. |

### Response body objects

#### The `MobileCustomAppConfig` object

Configuration of an existing mobile or custom application.

| Element | Type | Description |
| --- | --- | --- |
| apdexSettings | [MobileCustomApdex](#openapi-definition-MobileCustomApdex) | Apdex configuration of a mobile or custom application.  A duration less than the **tolerable** threshold is considered satisfied. |
| applicationId | string | The UUID of the application.  It is used only by OneAgent to send data to Dynatrace. |
| applicationType | string | The type of the application. The element can hold these values * `CUSTOM_APPLICATION` * `MOBILE_APPLICATION` |
| beaconEndpointType | string | The type of the beacon endpoint. The element can hold these values * `CLUSTER_ACTIVE_GATE` * `ENVIRONMENT_ACTIVE_GATE` * `INSTRUMENTED_WEB_SERVER` |
| beaconEndpointUrl | string | The URL of the beacon endpoint.  Only applicable when the **beaconEndpointType** is set to `ENVIRONMENT_ACTIVE_GATE` or `INSTRUMENTED_WEB_SERVER`. |
| costControlUserSessionPercentage | integer | The percentage of user sessions to be analyzed. |
| iconType | string | Custom application icon.  Mobile apps always use the mobile device icon, so this icon can only be set for custom apps. The element can hold these values * `AMAZON_ECHO` * `DESKTOP` * `EMBEDDED` * `IOT` * `MICROSOFT_HOLOLENS` * `UFO` * `USERS` |
| identifier | string | The Dynatrace entity ID of the application. |
| name | string | The name of the application. |
| optInModeEnabled | boolean | The opt-in mode is enabled (`true`) or disabled (`false`).  This value is only applicable to mobile and not to custom apps. |
| sessionReplayEnabled | boolean | The session replay is enabled (`true`) or disabled (`false`). This value is only applicable to mobile and not to custom apps. |
| sessionReplayOnCrashEnabled | boolean | **Deprecated**. Please use `sessionReplayEnabled` to enable or disable session replay for mobile apps. |

#### The `MobileCustomApdex` object

Apdex configuration of a mobile or custom application.

A duration less than the **tolerable** threshold is considered satisfied.

| Element | Type | Description |
| --- | --- | --- |
| frustratedOnError | boolean | Apdex error condition: if `true` the user session is considered frustrated when an error is reported. |
| frustratingThreshold | integer | Apdex **frustrated** threshold, in milliseconds: a duration greater than or equal to this value is considered frustrated. |
| toleratedThreshold | integer | Apdex **tolerable** threshold, in milliseconds: a duration greater than or equal to this value is considered tolerable. |

### Response body JSON models

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