---
title: Settings API - Performance thresholds schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-http-performance-thresholds
scraped: 2026-05-12T11:48:36.033185
---

# Settings API - Performance thresholds schema table

# Settings API - Performance thresholds schema table

* Published Dec 05, 2023

### Performance thresholds (`builtin:synthetic.http.performance-thresholds)`

Dynatrace generates a new problem if this synthetic monitor exceeds any of the performance thresholds below in 3 of the 5 most recent executions at a given location, unless there is an open maintenance window for the synthetic monitor. Multiple locations with 3 such violations can be included in a problem. The problem is closed if no performance threshold is violated in the 5 most recent executions at each of the previously affected locations.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:synthetic.http.performance-thresholds` | - | `HTTP_CHECK` - HTTP monitor |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.http.performance-thresholds` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:synthetic.http.performance-thresholds` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.http.performance-thresholds` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Generate a problem and send an alert on performance threshold violations `enabled` | boolean | - | Required |
| Performance thresholds `thresholds` | Set<[ThresholdEntry](#ThresholdEntry)> | - | Required |

##### The `ThresholdEntry` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Request `event` | text | - | Required |
| Threshold (in seconds) `threshold` | float | - | Required |