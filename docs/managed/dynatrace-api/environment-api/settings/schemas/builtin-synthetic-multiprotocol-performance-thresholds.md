---
title: Settings API - Performance thresholds schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-multiprotocol-performance-thresholds
scraped: 2026-05-12T11:45:08.080013
---

# Settings API - Performance thresholds schema table

# Settings API - Performance thresholds schema table

* Published Jul 31, 2024

### Performance thresholds (`builtin:synthetic.multiprotocol.performance-thresholds)`

Dynatrace generates a new problem if this synthetic monitor exceeds any of the performance thresholds below in {violatingSamples} of the {samples} most recent request executions at a given location, unless there is an open maintenance window for the synthetic monitor. Multiple locations with {violatingSamples} such violations can be included in a problem. The problem is closed if no performance threshold is violated in the {dealertingSamples} most recent request executions at each of the previously affected locations.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:synthetic.multiprotocol.performance-thresholds` | * `group:web-and-mobile-monitoring` * `group:synthetic.multiprotocol` * `group:web-and-mobile-monitoring.multiprotocol-monitor-default-settings` | `MULTIPROTOCOL_MONITOR` - Network availability monitor |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.multiprotocol.performance-thresholds` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:synthetic.multiprotocol.performance-thresholds` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.multiprotocol.performance-thresholds` |

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
| Threshold (in ms) `threshold` | integer | - | Required |
| Step index `stepIndex` | integer | - | Required |
| Aggregation type `aggregation` | enum | The element has these enums * `AVG` * `MIN` * `MAX` | Required |
| Number of violating request executions in analyzed sliding window `violatingSamples` | integer | - | Required |
| Number of request executions in analyzed sliding window (sliding window size) `samples` | integer | - | Required |
| Number of most recent non-violating request executions that closes the problem `dealertingSamples` | integer | - | Required |