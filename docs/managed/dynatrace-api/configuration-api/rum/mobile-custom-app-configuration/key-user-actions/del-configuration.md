---
title: Mobile and custom app API - DELETE a key user action
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/key-user-actions/del-configuration
---

# Mobile and custom app API - DELETE a key user action

# Mobile and custom app API - DELETE a key user action

* Reference
* Published Nov 05, 2020

Removes a user action from the list of key user actions in the specified app.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/keyUserActions/{actionName}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/keyUserActions/{actionName}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| applicationId | string | The UUID of the required mobile or custom application. It can be found in the Instrumentation Wizard of your app. | path | Required |
| actionName | string | The ID of the user action to be removed from the key user actions list. | path | Required |

## Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | Success. The user action has been removed from the list of key user actions. The response doesn't have a body. |
| **404** | Failed. The specified entity doesn't exist. |

## Related topics

* [User actions in RUM Classic](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.")