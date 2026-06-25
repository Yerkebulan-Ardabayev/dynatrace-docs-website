---
title: Synthetic metrics API - DELETE a metric
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics/del-metric
scraped: 2026-05-12T11:19:19.488919
---

# Synthetic metrics API - DELETE a metric

# Synthetic metrics API - DELETE a metric

* Reference
* Published Apr 16, 2020

Deletes the specified calculated synthetic metric. Deletion cannot be undone!

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/synthetic/{metricKey}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/synthetic/{metricKey}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| metricKey | string | The key of the calculated synthetic metric to be deleted. | path | Required |

## Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | Deleted. Response doesn't have a body. |

## Related topics

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")