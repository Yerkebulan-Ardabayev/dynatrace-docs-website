---
title: Mobile and custom app API - POST a key user action
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/key-user-actions/post-configuration
---

# Mobile and custom app API - POST a key user action

# Mobile and custom app API - POST a key user action

* Reference
* Published Nov 05, 2020

Adds a user action to the list of key user actions in the specified app.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/keyUserActions/{actionName}` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/keyUserActions/{actionName}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| applicationId | string | The UUID of the required mobile or custom application. It can be found in the Instrumentation Wizard of your app. | path | Required |
| actionName | string | The name of the user action to be marked as a key user action. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [KeyUserActionMobile](#openapi-definition-KeyUserActionMobile) | Success. The action has been marked as a key user action. The response contains its name. |
| **404** | - | Failed. The specified entity doesn't exist. |
| **409** | - | Failed. The max number of key user actions has been reached for the application. |

### Response body objects

#### The `KeyUserActionMobile` object

A key user action.

| Element | Type | Description |
| --- | --- | --- |
| name | string | The name of the key user action. |

### Response body JSON models

```
{



"name": "string"



}
```

## Related topics

* [User actions in RUM Classic](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.")