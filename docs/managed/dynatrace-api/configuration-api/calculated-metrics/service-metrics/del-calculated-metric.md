---
title: Service metrics API - DELETE a metric
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/calculated-metrics/service-metrics/del-calculated-metric
scraped: 2026-05-12T11:15:55.235200
---

# Service metrics API - DELETE a metric

# Service metrics API - DELETE a metric

* Reference
* Published Dec 16, 2019

Deletes the specified calculated service metric. Deletion cannot be undone!

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/service/{metricKey}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/service/{metricKey}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| metricKey | string | The key of the calculated service metric to be deleted. | path | Required |

## Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | Success. The calculated service metric has been deleted. Response doesn't have a body. |

## Example

In this example, the request deletes the **Requests by code** calculated service metric created in the [POST request example](/managed/dynatrace-api/configuration-api/calculated-metrics/service-metrics/post-calculated-metric#example "Create a calculated service metric via the Dynatrace API.").

The API token is passed in the **Authorization** header.

The response code of **204** indicates that the update was successful.

#### Curl

```
curl -X DELETE \



https://mySampleEnv.live.dynatrace.com/api/config/v1/calculatedMetrics/service/calc:service.requestsbycode \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/calculatedMetrics/service/calc:service.requestsbycode
```

#### Response code

204

## Related topics

* [Calculated metrics for services](/managed/observe/application-observability/services/calculated-service-metric "Learn how to create a calculated metric based on web requests.")
* [Multidimensional analysis](/managed/observe/application-observability/multidimensional-analysis "Configure a multidimensional analysis view and save it as a calculated metric.")