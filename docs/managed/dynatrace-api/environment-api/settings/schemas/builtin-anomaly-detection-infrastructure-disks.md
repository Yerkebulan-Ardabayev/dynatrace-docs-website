---
title: Settings API - Anomaly detection for infrastructure- Disk schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-infrastructure-disks
scraped: 2026-05-12T11:45:02.908654
---

# Settings API - Anomaly detection for infrastructure- Disk schema table

# Settings API - Anomaly detection for infrastructure- Disk schema table

* Published Dec 05, 2023

### Anomaly detection for infrastructure: Disk (`builtin:anomaly-detection.infrastructure-disks)`

Dynatrace automatically detects infrastructure-related performance anomalies such as low disk-space conditions. Use these settings to configure detection sensitivity, set alert thresholds, or disable alerting for disks.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.infrastructure-disks` | * `group:anomaly-detection.infrastructure` * `group:anomaly-detection` | `HOST` - Host  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.infrastructure-disks` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.infrastructure-disks` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.infrastructure-disks` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Disk `disk` | [disk](#disk) | - | Required |

##### The `disk` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `diskLowSpaceDetection` | [diskLowSpaceDetection](#diskLowSpaceDetection) | - | Required |
| `diskSlowWritesAndReadsDetection` | [diskSlowWritesAndReadsDetection](#diskSlowWritesAndReadsDetection) | - | Required |
| `diskLowInodesDetection` | [diskLowInodesDetection](#diskLowInodesDetection) | - | Required |

##### The `diskLowSpaceDetection` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect low disk space `enabled` | boolean | - | Required |
| Detection mode for low disk space `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [diskLowSpaceDetectionThresholds](#diskLowSpaceDetectionThresholds) | - | Required |

##### The `diskSlowWritesAndReadsDetection` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect slow-running disks `enabled` | boolean | - | Required |
| Detection mode for slow running disks `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [diskSlowWritesAndReadsDetectionThresholds](#diskSlowWritesAndReadsDetectionThresholds) | - | Required |

##### The `diskLowInodesDetection` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect low inodes number available `enabled` | boolean | - | Required |
| Detection mode for low inodes number available `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [diskLowInodesDetectionThresholds](#diskLowInodesDetectionThresholds) | - | Required |

##### The `diskLowSpaceDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Alert if free disk space is lower than this percentage in 3 out of 5 samples `freeSpacePercentage` | integer | - | Required |

##### The `diskSlowWritesAndReadsDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Alert if disk read time or write time is higher than this threshold in 3 out of 5 samples `writeAndReadTime` | integer | - | Required |

##### The `diskLowInodesDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Alert if the percentage of available inodes is lower than this threshold in 3 out of 5 samples `freeInodesPercentage` | integer | - | Required |