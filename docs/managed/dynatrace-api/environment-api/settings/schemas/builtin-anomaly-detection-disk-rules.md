---
title: Settings API - Disk anomaly detection rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-disk-rules
---

# Settings API - Disk anomaly detection rules schema table

# Settings API - Disk anomaly detection rules schema table

* Published Dec 05, 2023

### Disk anomaly detection rules (`builtin:anomaly-detection.disk-rules)`

Dynatrace automatically detects infrastructure-related performance anomalies such as low disk-space conditions. Use these settings (and the Infrastructure settings (`<your-dynatrace-url>//ui/settings/builtin:anomaly-detection.infrastructure-disks "Visit Infrastructure anomaly detection settings"`)) to configure detection sensitivity, set alert thresholds, or disable alerting for disks.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.disk-rules` | * `group:anomaly-detection.infrastructure` * `group:anomaly-detection` | `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.disk-rules` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.disk-rules` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.disk-rules` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Name `name` | text | - | Required |
| Enabled `enabled` | boolean | - | Required |
| Metric to alert on `metric` | enum | The element has these enums * `LOW_DISK_SPACE` * `LOW_INODES` * `READ_TIME_EXCEEDING` * `WRITE_TIME_EXCEEDING` | Required |
| Alert if lower than `thresholdPercent` | float | - | Required |
| Alert if higher than `thresholdMilliseconds` | float | - | Required |
| Sample limit `sampleLimit` | [SampleLimit](#SampleLimit) | Only alert if the threshold was violated in at least *n* of the last *m* samples | Required |
| Disk name filter `diskNameFilter` | [DiskNameFilter](#DiskNameFilter) | Only apply to disks whose name matches | Required |
| Host filter `tagFilters` | set | Only apply to hosts that have the following tags | Required |

##### The `SampleLimit` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Minimum number of violating samples `violatingSamples` | integer | - | Required |
| ... within the last `samples` | integer | - | Required |

##### The `DiskNameFilter` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Operator `operator` | enum | The element has these enums * `CONTAINS` * `DOES_NOT_CONTAIN` * `EQUALS` * `DOES_NOT_EQUAL` * `STARTS_WITH` * `DOES_NOT_START_WITH` | Required |
| Matching text `value` | text | - | Optional |