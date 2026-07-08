---
title: Settings API - Kubernetes namespace anomaly detection schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-kubernetes-namespace
---

# Settings API - Kubernetes namespace anomaly detection schema table

# Settings API - Kubernetes namespace anomaly detection schema table

* Published Dec 05, 2023

### Kubernetes namespace anomaly detection (`builtin:anomaly-detection.kubernetes.namespace)`

Dynatrace automatically detects a wide range of common Kubernetes-related issues. Use these settings to configure alerts relevant to your Kubernetes namespace. Changing thresholds resets the observation period. Additional information can be found on our [documentation page﻿](https://dt-url.net/wq02okj#namespace).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.kubernetes.namespace` | * `group:anomaly-detection.kubernetes` * `group:anomaly-detection` | `CLOUD_APPLICATION_NAMESPACE` - Kubernetes namespace  `KUBERNETES_CLUSTER` - Kubernetes cluster  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.namespace` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.namespace` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.namespace` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `cpuRequestsQuotaSaturation` | [CpuRequestsQuotaSaturation](#CpuRequestsQuotaSaturation) | Alerts if almost no CPU-request quota left in namespace | Required |
| `cpuLimitsQuotaSaturation` | [CpuLimitsQuotaSaturation](#CpuLimitsQuotaSaturation) | Alerts if almost no CPU-limit quota left in namespace | Required |
| `memoryRequestsQuotaSaturation` | [MemoryRequestsQuotaSaturation](#MemoryRequestsQuotaSaturation) | Alerts if almost no memory-request quota left in namespace | Required |
| `memoryLimitsQuotaSaturation` | [MemoryLimitsQuotaSaturation](#MemoryLimitsQuotaSaturation) | Alerts if almost no memory-limit quota left in namespace | Required |
| `podsQuotaSaturation` | [PodsQuotaSaturation](#PodsQuotaSaturation) | Alerts if almost no pod quota left in namespace | Required |

##### The `CpuRequestsQuotaSaturation` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect namespace CPU-request quota saturation `enabled` | boolean | - | Required |
| `configuration` | [CpuRequestsQuotaSaturationConfig](#CpuRequestsQuotaSaturationConfig) | Alert if | Required |

##### The `CpuLimitsQuotaSaturation` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect namespace CPU-limit quota saturation `enabled` | boolean | - | Required |
| `configuration` | [CpuLimitsQuotaSaturationConfig](#CpuLimitsQuotaSaturationConfig) | Alert if | Required |

##### The `MemoryRequestsQuotaSaturation` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect namespace memory-request quota saturation `enabled` | boolean | - | Required |
| `configuration` | [MemoryRequestsQuotaSaturationConfig](#MemoryRequestsQuotaSaturationConfig) | Alert if | Required |

##### The `MemoryLimitsQuotaSaturation` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect namespace memory-limit quota saturation `enabled` | boolean | - | Required |
| `configuration` | [MemoryLimitsQuotaSaturationConfig](#MemoryLimitsQuotaSaturationConfig) | Alert if | Required |

##### The `PodsQuotaSaturation` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect namespace pod quota saturation `enabled` | boolean | - | Required |
| `configuration` | [PodsQuotaSaturationConfig](#PodsQuotaSaturationConfig) | Alert if | Required |

##### The `CpuRequestsQuotaSaturationConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| amount of requested namespace CPU is above `threshold` | integer | - | Required |
| of quota for at least `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |

##### The `CpuLimitsQuotaSaturationConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| amount of utilized namespace CPU is above `threshold` | integer | - | Required |
| of quota for at least `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |

##### The `MemoryRequestsQuotaSaturationConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| amount of requested namespace memory is above `threshold` | integer | - | Required |
| of quota for at least `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |

##### The `MemoryLimitsQuotaSaturationConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| amount of utilized namespace memory is above `threshold` | integer | - | Required |
| of quota for at least `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |

##### The `PodsQuotaSaturationConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| number of utilized namespace pods is above `threshold` | integer | - | Required |
| of quota for at least `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |