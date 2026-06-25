---
title: Web application configuration API - GET key user actions
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/key-user-actions/get-configuration
scraped: 2026-05-12T11:17:04.697696
---

# Web application configuration API - GET key user actions

# Web application configuration API - GET key user actions

* Reference
* Published Sep 24, 2020

Gets the list of the key user action in the specified application.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}/keyUserActions` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}/keyUserActions` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required web application. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [KeyUserActionList](#openapi-definition-KeyUserActionList) | Success |

### Response body objects

#### The `KeyUserActionList` object

The list of key user actions in the web application

| Element | Type | Description |
| --- | --- | --- |
| keyUserActionList | [KeyUserAction[]](#openapi-definition-KeyUserAction) | - |

#### The `KeyUserAction` object

Configuration of the key user action.

| Element | Type | Description |
| --- | --- | --- |
| actionType | string | The type of the action. The element can hold these values * `Custom` * `Load` * `Xhr` |
| domain | string | The domain where the action is performed. |
| meIdentifier | string | The Dynatrace entity ID of the action. |
| name | string | The name of the action. |

### Response body JSON models

```
{



"keyUserActionList": [



{



"actionType": "Load",



"domain": "test.com",



"meIdentifier": "APPLICATION_METHOD-1234",



"name": "Loading of page /example"



}



]



}
```

## Related topics

* [User actions](/managed/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.")