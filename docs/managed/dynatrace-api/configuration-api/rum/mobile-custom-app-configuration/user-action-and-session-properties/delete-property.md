---
title: Mobile and custom app API - DELETE user session property
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/user-action-and-session-properties/delete-property
scraped: 2026-05-12T11:15:34.223674
---

# Mobile and custom app API - DELETE user session property

# Mobile and custom app API - DELETE user session property

* Reference
* Published Nov 05, 2020

Deletes the specified user session property from an app.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/userActionAndSessionProperties/{key}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/userActionAndSessionProperties/{key}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| applicationId | string | The UUID of the required mobile or custom application. It can be found in the Instrumentation Wizard of your app. | path | Required |
| key | string | The key of the required mobile session or user action property. | path | Required |

## Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | Success. The property has been deleted. The response doesn't have a body. |
| **404** | Failed. The specified entity doesn't exist. |