---
title: Web application configuration API - DELETE a key user action
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/key-user-actions/del-configuration
scraped: 2026-05-12T11:16:57.861868
---

# Web application configuration API - DELETE a key user action

# Web application configuration API - DELETE a key user action

* Reference
* Published Sep 24, 2020

Removes a user action from the list of key user actions in the specified application.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}/keyUserActions/{keyUserActionId}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}/keyUserActions/{keyUserActionId}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required web application. | path | Required |
| keyUserActionId | string | The ID of the user action to be removed from the key user actions list. | path | Required |

## Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | Success. The user action has been removed from the list of key user actions. The response doesn't have a body. |

## Related topics

* [User actions](/managed/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.")