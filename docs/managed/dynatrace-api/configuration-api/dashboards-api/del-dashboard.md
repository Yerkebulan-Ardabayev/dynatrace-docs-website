---
title: "Dashboards API - DELETE a dashboard"
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/dashboards-api/del-dashboard
updated: 2026-02-09
---

# Dashboards API - DELETE a dashboard

# Dashboards API - DELETE a dashboard

* Reference
* Published Aug 30, 2019

Deletes the specified dashboard.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/dashboards/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/dashboards/{id}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the dashboard to be deleted. | path | Required |

## Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | Success. The dashboard has been deleted. Response doesn't have a body. |

## Example

In this example, the request deletes the dashboard created in the [POST request](/managed/dynatrace-api/configuration-api/dashboards-api/del-dashboard#example "Delete a dashboard via the Dynatrace Classic API.") example. The response code of **204** indicates that the deletion was successful.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X DELETE \



https://mySampleEnv.live.dynatrace.com/api/config/v1/dashboards/7dd386fe-f91d-42e3-a2ec-0c88070933f4 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
DELETE https://mySampleEnv.live.dynatrace.com/api/config/v1/dashboards/7dd386fe-f91d-42e3-a2ec-0c88070933f4
```

#### Response code

204

## Related topics

* [Dashboards](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")
