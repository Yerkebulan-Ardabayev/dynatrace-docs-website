---
title: Settings API - Anomaly detection for VMware schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-infrastructure-vmware
scraped: 2026-05-12T11:46:49.200874
---

# Settings API - Anomaly detection for VMware schema table

# Settings API - Anomaly detection for VMware schema table

* Published Dec 05, 2023

### Anomaly detection for VMware (`builtin:anomaly-detection.infrastructure-vmware)`

Dynatrace automatically detects infrastructure-related performance anomalies such as high CPU saturation, memory outages, and low disk-space conditions. Use these settings to configure detection sensitivity, set alert thresholds, or disable alerting for infrastructure components.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.infrastructure-vmware` | * `group:anomaly-detection.infrastructure` * `group:anomaly-detection` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.infrastructure-vmware` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.infrastructure-vmware` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.infrastructure-vmware` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `esxiHighCpuDetection` | [EsxiHighCpuDetectionConfig](#EsxiHighCpuDetectionConfig) | - | Required |
| `guestCpuLimitDetection` | [GuestCPULimitDetectionConfig](#GuestCPULimitDetectionConfig) | - | Required |
| `esxiHighMemoryDetection` | [EsxiHighMemoryDetectionConfig](#EsxiHighMemoryDetectionConfig) | - | Required |
| `overloadedStorageDetection` | [OverloadedStorageDetectionConfig](#OverloadedStorageDetectionConfig) | - | Required |
| `undersizedStorageDetection` | [UndersizedStorageDetectionConfig](#UndersizedStorageDetectionConfig) | - | Required |
| `slowPhysicalStorageDetection` | [SlowPhysicalStorageDetectionConfig](#SlowPhysicalStorageDetectionConfig) | - | Required |
| `droppedPacketsDetection` | [DroppedPacketsDetectionConfig](#DroppedPacketsDetectionConfig) | - | Required |
| `lowDatastoreSpaceDetection` | [LowDatastoreSpaceDetectionConfig](#LowDatastoreSpaceDetectionConfig) | - | Required |

##### The `EsxiHighCpuDetectionConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect high CPU saturation on ESXi host `enabled` | boolean | - | Required |
| Detection mode `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [EsxiHighCpuDetectionThresholds](#EsxiHighCpuDetectionThresholds) | Alert if **all three** conditions are met in 3 out of 5 samples | Required |

##### The `GuestCPULimitDetectionConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect guest CPU limit reached `enabled` | boolean | - | Required |
| Detection mode `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [GuestCPULimitDetectionThresholds](#GuestCPULimitDetectionThresholds) | Alert if **all three** conditions are met in 3 out of 5 samples | Required |

##### The `EsxiHighMemoryDetectionConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect memory saturation on ESXi host `enabled` | boolean | - | Required |
| Detection mode `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [EsxiHighMemoryDetectionThresholds](#EsxiHighMemoryDetectionThresholds) | Alert if the condition is met in 3 out of 5 samples | Required |

##### The `OverloadedStorageDetectionConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect overloaded storage on physical storage device `enabled` | boolean | - | Required |
| Detection mode `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [OverloadedStorageDetectionThresholds](#OverloadedStorageDetectionThresholds) | Alert if the condition is met in 3 out of 5 samples | Required |

##### The `UndersizedStorageDetectionConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect undersized storage device `enabled` | boolean | - | Required |
| Detection mode `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [UndersizedStorageDetectionThresholds](#UndersizedStorageDetectionThresholds) | Alert if **any** condition is met in 3 out of 5 samples | Required |

##### The `SlowPhysicalStorageDetectionConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect physical storage device running slow `enabled` | boolean | - | Required |
| Detection mode `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [SlowPhysicalStorageDetectionThresholds](#SlowPhysicalStorageDetectionThresholds) | Alert if **any** condition is met in 4 out of 5 samples | Required |

##### The `DroppedPacketsDetectionConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect high number of dropped packets `enabled` | boolean | - | Required |
| Detection mode `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [DroppedPacketsDetectionThresholds](#DroppedPacketsDetectionThresholds) | Alert if the condition is met in 3 out of 5 samples | Required |

##### The `LowDatastoreSpaceDetectionConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect low datastore space `enabled` | boolean | - | Required |
| Detection mode `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [LowDatastoreSpaceDetectionThresholds](#LowDatastoreSpaceDetectionThresholds) | Alert if the condition is met in 1 out of 5 samples | Required |

##### The `EsxiHighCpuDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| CPU usage is higher than `cpuUsagePercentage` | integer | - | Required |
| VM CPU ready is higher than `vmCpuReadyPercentage` | integer | - | Required |
| At least one peak occurred when Hypervisor CPU usage was higher than `cpuPeakPercentage` | integer | - | Required |

##### The `GuestCPULimitDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Hypervisor CPU usage is higher than `hostCpuUsagePercentage` | integer | - | Required |
| VM CPU usage (VM CPU Usage Mhz / VM CPU limit in Mhz) is higher than `vmCpuUsagePercentage` | integer | - | Required |
| VM CPU ready is higher than `vmCpuReadyPercentage` | integer | - | Required |

##### The `EsxiHighMemoryDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| ESXi host swap IN/OUT or compression/decompression rate is higher than `compressionDecompressionRate` | float | - | Required |

##### The `OverloadedStorageDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Number of command aborts is higher than `commandAbortsNumber` | integer | - | Required |

##### The `UndersizedStorageDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Average queue command latency is higher than `averageQueueCommandLatency` | integer | - | Required |
| Peak queue command latency is higher than `peakQueueCommandLatency` | integer | - | Required |

##### The `SlowPhysicalStorageDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Read/write latency is higher than `avgReadWriteLatency` | integer | - | Required |
| Peak value for read/write latency is higher than `peakReadWriteLatency` | integer | - | Required |

##### The `DroppedPacketsDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Receive/transmit dropped packets rate on NIC is higher than `droppedPacketsPerSecond` | integer | - | Required |

##### The `LowDatastoreSpaceDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Datastore free space is lower than `freeSpacePercentage` | integer | - | Required |