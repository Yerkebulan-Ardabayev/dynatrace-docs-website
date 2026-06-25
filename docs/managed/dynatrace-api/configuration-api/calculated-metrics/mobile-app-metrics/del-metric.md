---
title: Mobile app metrics API - DELETE a metric
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/calculated-metrics/mobile-app-metrics/del-metric
scraped: 2026-05-12T11:17:30.865331
---

# Mobile app metrics API - DELETE a metric

# Mobile app metrics API - DELETE a metric

* Reference
* Published Apr 16, 2020

Deletes the specified calculated mobile app metric. Deletion cannot be undone!

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/mobile/{metricKey}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/mobile/{metricKey}` |

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

* [Create calculated metrics for mobile applications](/managed/observe/digital-experience/mobile-applications/additional-configuration/rum-calculated-metrics-mobile "Create calculated metrics as well as custom charts based on calculated metrics for your mobile applications.")
* [Create calculated metrics for custom applications](/managed/observe/digital-experience/custom-applications/additional-configuration/rum-calculated-metrics-custom "Create calculated metrics as well as custom charts based on calculated metrics for your custom applications.")