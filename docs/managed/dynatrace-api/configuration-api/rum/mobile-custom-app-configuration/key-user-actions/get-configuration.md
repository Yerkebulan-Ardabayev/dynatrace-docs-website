---
title: Mobile and custom app API - GET key user actions
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/key-user-actions/get-configuration
---

# Mobile and custom app API - GET key user actions

# Mobile and custom app API - GET key user actions

* Reference
* Published Nov 05, 2020

Gets the list of the key user actions in the specified app.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/keyUserActions` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/keyUserActions` |

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
| **200** | [KeyUserActionMobileList](#openapi-definition-KeyUserActionMobileList) | Success |
| **404** | - | Failed. The specified entity doesn't exist. |

### Response body objects

#### The `KeyUserActionMobileList` object

A list of key actions in an application.

| Element | Type | Description |
| --- | --- | --- |
| keyUserActions | [KeyUserActionMobile](#openapi-definition-KeyUserActionMobile)[] | A list of key actions in an application. |

#### The `KeyUserActionMobile` object

A key user action.

| Element | Type | Description |
| --- | --- | --- |
| name | string | The name of the key user action. |

### Response body JSON models

```
{



"keyUserActions": [



{



"name": "string"



}



]



}
```

## Related topics

* [User actions in RUM Classic](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.")