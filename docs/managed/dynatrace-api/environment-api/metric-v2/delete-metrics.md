---
title: Metrics API - DELETE ingested metrics
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metric-v2/delete-metrics
scraped: 2026-05-12T11:27:53.271624
---

# Metrics API - DELETE ingested metrics

# Metrics API - DELETE ingested metrics

* Reference
* Published Jan 16, 2026

Dynatrace version 1.330+

Deletes [ingested metrics](/managed/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.") older than the specified number of days.

* You can only delete metrics that have been ingested via the Metrics v2 API.
* Deleted metrics cannot be restored.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/metrics` |
| DELETE | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/metrics` |

## Authentication

To execute this request, you need an access token with `metrics.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| metricSelector | string | Selects metrics to be considered for deletion.  You can select a full set of related metrics by using a trailing asterisk (`*`) wildcard. For example, `airflow_*` selects all custom airflow metrics, `*` selects all custom metrics. | query | Required |
| minUnusedDays | integer | The number of days since the metric was last used. Must be between `30` and `1825` (5 years). | query | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **202** | - | Success. The deletion of the metrics has been triggered. |
| **400** | - | Failed. |
| **500** | - | Failed. The bulk-deletion failed. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

## Example

In this example, the request deletes all metrics that have not been written in the last 60 days:

```
DELETE /api/v2/metrics?metricSelector=<your-selector>&minUnusedDays=60
```

## Related topics

* [Extend metric observability](/managed/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.")