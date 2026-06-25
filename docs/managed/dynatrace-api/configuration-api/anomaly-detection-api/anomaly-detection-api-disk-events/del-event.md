---
title: Disk events anomaly detection API - DELETE an event
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events/del-event
scraped: 2026-05-12T11:20:22.293650
---

# Disk events anomaly detection API - DELETE an event

# Disk events anomaly detection API - DELETE an event

* Reference
* Published Aug 29, 2019

Deletes the specified disk event rule.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/diskEvents/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/diskEvents/{id}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the disk event rule to be deleted. | path | Required |

## Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | Success. The disk event rule has been deleted. Response doesn't have a body. |

## Example

In this example, the request deletes the **very slow disk** rule we created in the [POST request](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events/post-event#example "Create a disk event rule via the Dynatrace API.") example. The response code of **204** indicates that the deletion was successful.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X DELETE \



https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/diskEvents/fdd83212-9c08-44ba-a0cf-dbb471cd819a \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/diskEvents/fdd83212-9c08-44ba-a0cf-dbb471cd819a
```

#### Response code

204

## Related topics

* [DavisÂ® AI](/managed/dynatrace-intelligence "Get familiar with the capabilities of Davis AI.")