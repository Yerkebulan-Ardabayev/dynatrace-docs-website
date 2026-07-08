---
title: Settings API - Anomaly detection for classic AWS services schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-infrastructure-aws
---

# Settings API - Anomaly detection for classic AWS services schema table

# Settings API - Anomaly detection for classic AWS services schema table

* Published Dec 05, 2023

### Anomaly detection for classic AWS services (`builtin:anomaly-detection.infrastructure-aws)`

Dynatrace automatically detects infrastructure-related performance anomalies such as high CPU saturation, memory outages, and low disk-space conditions. These settings allow you to configure detection sensitivity, set alert thresholds, or disable alerting for classic infrastructure components.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.infrastructure-aws` | * `group:anomaly-detection.infrastructure` * `group:anomaly-detection` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.infrastructure-aws` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.infrastructure-aws` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.infrastructure-aws` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `ec2CandidateHighCpuDetection` | [Ec2CandidateHighCpuDetectionConfig](#Ec2CandidateHighCpuDetectionConfig) | - | Required |
| `rdsHighCpuDetection` | [RdsHighCpuDetectionConfig](#RdsHighCpuDetectionConfig) | - | Required |
| `rdsHighWriteReadLatencyDetection` | [RdsHighWriteReadLatencyDetectionConfig](#RdsHighWriteReadLatencyDetectionConfig) | - | Required |
| `rdsLowStorageDetection` | [RdsLowStorageDetectionConfig](#RdsLowStorageDetectionConfig) | - | Required |
| `rdsHighMemoryDetection` | [RdsHighMemoryDetectionConfig](#RdsHighMemoryDetectionConfig) | - | Required |
| `elbHighConnectionErrorsDetection` | [ElbHighConnectionErrorsDetectionConfig](#ElbHighConnectionErrorsDetectionConfig) | - | Required |
| `rdsRestartsSequenceDetection` | [RdsRestartsSequenceDetectionConfig](#RdsRestartsSequenceDetectionConfig) | - | Required |
| `lambdaHighErrorRateDetection` | [LambdaHighErrorRateDetectionConfig](#LambdaHighErrorRateDetectionConfig) | - | Required |

##### The `Ec2CandidateHighCpuDetectionConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect high CPU saturation on EC2 monitoring candidate `enabled` | boolean | - | Required |
| Detection mode `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [Ec2CandidateHighCpuDetectionThresholds](#Ec2CandidateHighCpuDetectionThresholds) | Alert if the condition is met in 3 out of 5 samples | Required |

##### The `RdsHighCpuDetectionConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect high CPU utilization on RDS `enabled` | boolean | - | Required |
| Detection mode `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [RdsHighCpuDetectionThresholds](#RdsHighCpuDetectionThresholds) | Alert if the condition is met in 3 out of 5 samples | Required |

##### The `RdsHighWriteReadLatencyDetectionConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect high RDS write/read latency `enabled` | boolean | - | Required |
| Detection mode `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [RdsHighWriteReadLatencyDetectionThresholds](#RdsHighWriteReadLatencyDetectionThresholds) | Alert if the condition is met in 3 out of 5 samples | Required |

##### The `RdsLowStorageDetectionConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect low free storage space on RDS `enabled` | boolean | - | Required |
| Detection mode `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [RdsLowStorageDetectionThresholds](#RdsLowStorageDetectionThresholds) | Alert if the condition is met in 3 out of 5 samples | Required |

##### The `RdsHighMemoryDetectionConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect RDS running out of memory `enabled` | boolean | - | Required |
| Detection mode `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [RdsHighMemoryDetectionThresholds](#RdsHighMemoryDetectionThresholds) | Alert if **both** conditions is met in 3 out of 5 samples | Required |

##### The `ElbHighConnectionErrorsDetectionConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect high number of backend connection errors on ELB `enabled` | boolean | - | Required |
| Detection mode `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [ElbHighConnectionErrorsDetectionThresholds](#ElbHighConnectionErrorsDetectionThresholds) | Alert if the condition is met in 3 out of 5 samples | Required |

##### The `RdsRestartsSequenceDetectionConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect restarts sequence on RDS `enabled` | boolean | - | Required |
| Detection mode `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [RdsRestartsSequenceDetectionThresholds](#RdsRestartsSequenceDetectionThresholds) | Alert if the condition is met in 2 out of 20 samples | Required |

##### The `LambdaHighErrorRateDetectionConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect AWS Lambda high error rate `enabled` | boolean | - | Required |
| Detection mode `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [LambdaHighErrorRateDetectionThresholds](#LambdaHighErrorRateDetectionThresholds) | Alert if the condition is met in 3 out of 5 samples | Required |

##### The `Ec2CandidateHighCpuDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| CPU usage is higher than `cpuUsage` | float | - | Required |

##### The `RdsHighCpuDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| CPU usage is higher than `cpuUsage` | float | - | Required |

##### The `RdsHighWriteReadLatencyDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Read/write latency is higher than `readWriteLatency` | integer | - | Required |

##### The `RdsLowStorageDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Free storage space divided by allocated storage is lower than `freeStoragePercentage` | integer | - | Required |

##### The `RdsHighMemoryDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Freeable memory is lower than `freeMemory` | float | - | Required |
| Swap usage is higher than `swapUsage` | float | - | Required |

##### The `ElbHighConnectionErrorsDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Number of backend connection errors is higher than `connectionErrorsPerMinute` | integer | - | Required |

##### The `RdsRestartsSequenceDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Number of restarts per minute is equal or higher than `restartsPerMinute` | integer | - | Required |

##### The `LambdaHighErrorRateDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Failed invocations rate is higher than `failedInvocationsRate` | integer | - | Required |