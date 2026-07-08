---
title: Mobile and custom app API - GET all user session properties
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/user-action-and-session-properties/get-all
---

# Mobile and custom app API - GET all user session properties

# Mobile and custom app API - GET all user session properties

* Reference
* Published Nov 05, 2020

Lists all user session and user action properties from the specified mobile or custom app.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/userActionAndSessionProperties` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/userActionAndSessionProperties` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| applicationId | string | The UUID of the required mobile or custom application. It can be found in the Instrumentation Wizard of your app. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [MobileSessionUserActionPropertyList](#openapi-definition-MobileSessionUserActionPropertyList) | Success |

### Response body objects

#### The `MobileSessionUserActionPropertyList` object

Contains lists of short representations of mobile session properties and mobile user action properties.

| Element | Type | Description |
| --- | --- | --- |
| sessionProperties | [MobileSessionUserActionPropertyShort](#openapi-definition-MobileSessionUserActionPropertyShort)[] | A list of short representations of mobile session properties. |
| userActionProperties | [MobileSessionUserActionPropertyShort](#openapi-definition-MobileSessionUserActionPropertyShort)[] | A list of short representations of mobile user action properties. |

#### The `MobileSessionUserActionPropertyShort` object

A short representation of mobile session or user action property.

| Element | Type | Description |
| --- | --- | --- |
| displayName | string | The display name of the session or user action property. |
| key | string | The key of the session or user action property. |

### Response body JSON models

```
{



"sessionProperties": [



{



"displayName": "string",



"key": "string"



}



],



"userActionProperties": [



{}



]



}
```