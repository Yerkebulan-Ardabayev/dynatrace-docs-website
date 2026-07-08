---
title: Maintenance windows API - DELETE a maintenance window
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/maintenance-windows-api/delete-mw
---

# Maintenance windows API - DELETE a maintenance window

# Maintenance windows API - DELETE a maintenance window

* Reference
* Updated on Apr 28, 2020

This API is deprecated. Use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with the **Maintenance windows** (`builtin:alerting.maintenance-window`) schema instead.

Deletes the specified maintenance window. Deletions can't be undone.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/maintenanceWindows/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/maintenanceWindows/{id}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the maintenance window to be deleted. | path | Required |

## Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | Success. The maintenance window has been deleted. Response doesn't have a body. |

## Example

In this example the request deletes the maintenance window with the ID of **b8fc7c5b-4332-423a-a223-b60292c3263d**. The response code of **204** indicates that the deletion was successful.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X DELETE \



"https://mySampleEnv.live.dynatrace.com/api/config/v1/maintenanceWindows/b8fc7c5b-4332-423a-a223-b60292c3263d" \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/maintenanceWindows/b8fc7c5b-4332-423a-a223-b60292c3263d
```

#### Response code

204

## Related topics

* [Maintenance windows](/managed/analyze-explore-automate/notifications-and-alerting/maintenance-windows "Understand when to use a maintenance window. Read about the supported maintenance window types.")