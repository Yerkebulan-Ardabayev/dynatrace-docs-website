---
title: Settings API - Metric query schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-metric-query
---

# Settings API - Metric query schema table

# Settings API - Metric query schema table

* Published Dec 05, 2023

### Metric query (`builtin:metric.query)`

A stored metric query allows you to calculate the metrics' values through a metric expression.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:metric.query` | * `group:metrics` | `metric` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:metric.query` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:metric.query` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:metric.query` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Query `metricSelector` | text | - | Required |