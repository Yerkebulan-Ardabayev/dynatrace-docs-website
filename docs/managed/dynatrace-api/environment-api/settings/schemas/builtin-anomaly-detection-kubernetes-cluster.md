---
title: Settings API - Kubernetes cluster anomaly detection schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-kubernetes-cluster
---

# Settings API - Kubernetes cluster anomaly detection schema table

# Settings API - Kubernetes cluster anomaly detection schema table

* Published Dec 05, 2023

### Kubernetes cluster anomaly detection (`builtin:anomaly-detection.kubernetes.cluster)`

Dynatrace automatically detects a wide range of common Kubernetes-related issues. Use these settings to configure alerts relevant to your Kubernetes cluster. Changing thresholds resets the observation period. Additional information can be found on our [documentation page﻿](https://dt-url.net/wq02okj#cluster).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.kubernetes.cluster` | * `group:anomaly-detection.kubernetes` * `group:anomaly-detection` | `KUBERNETES_CLUSTER` - Kubernetes cluster  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.cluster` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.cluster` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.cluster` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `readinessIssues` | [ReadinessIssues](#ReadinessIssues) | Alerts if cluster has not been ready for a given amount of time | Required |
| `cpuRequestsSaturation` | [CpuRequestsSaturation](#CpuRequestsSaturation) | - | Required |
| `memoryRequestsSaturation` | [MemoryRequestsSaturation](#MemoryRequestsSaturation) | - | Required |
| `podsSaturation` | [PodsSaturation](#PodsSaturation) | - | Required |
| `monitoringIssues` | [MonitoringIssues](#MonitoringIssues) | - | Required |

##### The `ReadinessIssues` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect cluster readiness issues `enabled` | boolean | Evaluates the Kubernetes readyz endpoint | Required |
| `configuration` | [ReadinessIssuesConfig](#ReadinessIssuesConfig) | Alert if | Required |

##### The `CpuRequestsSaturation` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect cluster CPU-request saturation `enabled` | boolean | - | Required |
| `configuration` | [CpuRequestsSaturationConfig](#CpuRequestsSaturationConfig) | Alert if | Required |

##### The `MemoryRequestsSaturation` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect cluster memory-request saturation `enabled` | boolean | - | Required |
| `configuration` | [MemoryRequestsSaturationConfig](#MemoryRequestsSaturationConfig) | Alert if | Required |

##### The `PodsSaturation` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect cluster pod-saturation `enabled` | boolean | - | Required |
| `configuration` | [PodsSaturationConfig](#PodsSaturationConfig) | Alert if | Required |

##### The `MonitoringIssues` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect monitoring issues `enabled` | boolean | - | Required |
| `configuration` | [MonitoringIssuesConfig](#MonitoringIssuesConfig) | Alert if | Required |

##### The `ReadinessIssuesConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| cluster is not ready for at least `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |

##### The `CpuRequestsSaturationConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| amount of requested CPU is above `threshold` | integer | - | Required |
| of cluster CPU capacity for at least `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |

##### The `MemoryRequestsSaturationConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| amount of requested memory is above `threshold` | integer | - | Required |
| of cluster memory capacity for at least `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |

##### The `PodsSaturationConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| number of running pods is higher than `threshold` | integer | - | Required |
| of schedulable pod capacity for at least `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |

##### The `MonitoringIssuesConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| monitoring is not available for at least `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |