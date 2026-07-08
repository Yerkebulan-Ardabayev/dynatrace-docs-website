---
title: Metrics API - DELETE an ingested metric
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metric-v2/delete-metric
---

# Metrics API - DELETE an ingested metric

# Metrics API - DELETE an ingested metric

* Reference
* Updated on Jan 22, 2026

Deletes the specified [ingested metric](/managed/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.").

* You can only delete metrics that have been ingested via the Metrics v2 API.
* You can't delete a metric if it has data points ingested within the last two hours.
* Deleted metrics cannot be restored.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/metrics/{metricKey}` |
| DELETE | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/metrics/{metricKey}` |

## Authentication

To execute this request, you need an access token with `metrics.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| metricKey | string | The key of the required metric. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **202** | - | Success. The deletion of the metric has been triggered. |
| **400** | - | Failed. The metric has been written within the last two hours. |
| **404** | - | Failed. The metric cannot be found or the key cannot be parsed. |
| **500** | - | Failed. The deletion of metric dimensions failed. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

## Example

In this example, the request deletes the **cpu.temperature** metric. The response code of **202** indicates that the deletion has been triggered successfully.

The API token is passed in the **Authorization** header.

#### Curl

```
curl --request DELETE \



--url https://mySampleEnv.live.dynatrace.com/api/v2/metrics/cpu.temperature \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/metrics/cpu.temperature
```

#### Response code

202

## Related topics

* [Extend metric observability](/managed/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.")