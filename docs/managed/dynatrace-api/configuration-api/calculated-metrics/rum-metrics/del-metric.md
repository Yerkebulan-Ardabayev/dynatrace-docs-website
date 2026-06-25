---
title: Web application metrics API - DELETE a metric
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/calculated-metrics/rum-metrics/del-metric
scraped: 2026-05-12T11:17:51.663120
---

# Web application metrics API - DELETE a metric

# Web application metrics API - DELETE a metric

* Reference
* Published Feb 28, 2020

Deletes the specified calculated web application metric. Deletion cannot be undone!

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/rum/{metricKey}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/rum/{metricKey}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| metricKey | string | The key of the metric to be deleted. | path | Required |

## Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | Deleted. Response doesn't have a body. |

## Related topics

* [Create calculated metrics for web applications](/managed/observe/digital-experience/web-applications/additional-configuration/rum-calculated-metrics-web "Create calculated metrics as well as custom charts based on calculated metrics for your web applications.")