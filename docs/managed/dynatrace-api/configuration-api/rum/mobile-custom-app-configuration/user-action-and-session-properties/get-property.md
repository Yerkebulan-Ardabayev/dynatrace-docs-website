---
title: Mobile and custom app API - GET user session property
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/user-action-and-session-properties/get-property
---

# Mobile and custom app API - GET user session property

# Mobile and custom app API - GET user session property

* Reference
* Published Nov 05, 2020

Gets the parameters of the specified user session property of an app.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/userActionAndSessionProperties/{key}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/userActionAndSessionProperties/{key}` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| applicationId | string | The UUID of the required mobile or custom application. It can be found in the Instrumentation Wizard of your app. | path | Required |
| key | string | The key of the required mobile session or user action property. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [MobileSessionUserActionProperty](#openapi-definition-MobileSessionUserActionProperty) | Success |
| **404** | - | Failed. The specified entity doesn't exist. |

### Response body objects

#### The `MobileSessionUserActionProperty` object

Configuration of the mobile session or user action property.

| Element | Type | Description |
| --- | --- | --- |
| aggregation | string | The aggregation type of the property.  It defines how multiple values of the property are aggregated. The element can hold these values * `AVERAGE` * `FIRST` * `LAST` * `MAX` * `MIN` * `SUM` |
| cleanupRule | string | The cleanup rule of the property.  Defines how to extract the data you need from a string value. Specify the [regular expression﻿](https://dt-url.net/k9e0iaq?dt=m) for the data you need there. |
| displayName | string | The display name of the property. |
| key | string | The unique key of the mobile session or user action property. |
| name | string | The name of the reported value.  Only applicable when the **origin** is set to `API`. |
| origin | string | The origin of the property The element can hold these values * `API` * `SERVER_SIDE_REQUEST_ATTRIBUTE` |
| serverSideRequestAttribute | string | The ID of the request attribute.  Only applicable when the **origin** is set to `SERVER_SIDE_REQUEST_ATTRIBUTE`. |
| storeAsSessionProperty | boolean | If `true`, the property is stored as a session property |
| storeAsUserActionProperty | boolean | If `true`, the property is stored as a user action property |
| type | string | The data type of the property. The element can hold these values * `DOUBLE` * `LONG` * `STRING` |

### Response body JSON models

```
{



"aggregation": "AVERAGE",



"cleanupRule": "string",



"displayName": "string",



"key": "string",



"name": "string",



"origin": "API",



"serverSideRequestAttribute": "string",



"storeAsSessionProperty": true,



"storeAsUserActionProperty": true,



"type": "DOUBLE"



}
```