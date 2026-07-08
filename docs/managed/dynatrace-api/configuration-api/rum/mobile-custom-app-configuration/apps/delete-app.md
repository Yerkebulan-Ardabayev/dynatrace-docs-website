---
title: Mobile and custom app API - DELETE an app
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/apps/delete-app
---

# Mobile and custom app API - DELETE an app

# Mobile and custom app API - DELETE an app

* Reference
* Published Nov 05, 2020

Deletes the specified mobile or custom app.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{id}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The UUID of the required mobile or custom application. It can be found in the Instrumentation Wizard of your app. | path | Required |

## Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | Success. The application has been deleted. The response doesn't have a body. |
| **404** | Failed. The specified entity doesn't exist. |

## Related topics

* [Delete a mobile application in RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/delete-application-mobile "Delete your mobile applications via the Dynatrace web UI or API.")
* [Delete a custom application in RUM Classic](/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/delete-application-custom "Delete your custom applications via the Dynatrace web UI or API.")