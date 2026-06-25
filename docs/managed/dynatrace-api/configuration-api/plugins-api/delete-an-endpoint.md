---
title: Plugins API - DELETE a plugin's endpoint
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/plugins-api/delete-an-endpoint
scraped: 2026-05-12T11:21:04.451668
---

# Plugins API - DELETE a plugin's endpoint

# Plugins API - DELETE a plugin's endpoint

* Reference
* Published Jun 07, 2019

Deletes the specified endpoint of the ActiveGate plugin.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/endpoints/{endpointId}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/endpoints/{endpointId}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the plugin where you want to delete an endpoint. | path | Required |
| endpointId | string | The ID of the endpoint to be deleted. | path | Required |

## Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | Deleted. Response doesn't have a body. |

## Example

In this example, the request deletes the endpoint with the ID of **8757307336635955682** from the SAP plugin, which has the ID of **custom.remote.python.sap**. The response code of 204 indicates that the deletion was successful.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X DELETE \



https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.sap/endpoints/8757307336635955682 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
DELETE https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.sap/endpoints/8757307336635955682
```

#### Response code

204