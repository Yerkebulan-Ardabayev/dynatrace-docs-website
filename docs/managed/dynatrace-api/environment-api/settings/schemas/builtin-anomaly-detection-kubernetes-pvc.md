---
title: Settings API - Kubernetes persistent volume claim anomaly detection schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-kubernetes-pvc
scraped: 2026-05-12T11:43:48.390360
---

# Settings API - Kubernetes persistent volume claim anomaly detection schema table

# Settings API - Kubernetes persistent volume claim anomaly detection schema table

* Published Dec 05, 2023

### Kubernetes persistent volume claim anomaly detection (`builtin:anomaly-detection.kubernetes.pvc)`

Dynatrace automatically detects a wide range of common Kubernetes-related issues. Use these settings to configure alerts relevant to your Kubernetes persistent volume claims. Changing thresholds resets the observation period. Additional information can be found on our [documentation pageï»¿](https://dt-url.net/wq02okj#persistent-volume-claims).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.kubernetes.pvc` | * `group:anomaly-detection.kubernetes` * `group:anomaly-detection` | `CLOUD_APPLICATION_NAMESPACE` - Kubernetes namespace  `KUBERNETES_CLUSTER` - Kubernetes cluster  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.pvc` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.pvc` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.pvc` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `lowDiskSpaceCritical` | [LowDiskSpaceCritical](#LowDiskSpaceCritical) | Alerts on low disk space in megabytes for a persistent volume claim. | Required |
| `lowDiskSpaceCriticalPercentage` | [LowDiskSpaceCriticalPercentage](#LowDiskSpaceCriticalPercentage) | Alerts on low disk space in % for a persistent volume claim. | Required |

##### The `LowDiskSpaceCritical` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect low disk space (MiB) `enabled` | boolean | - | Required |
| `configuration` | [LowDiskSpaceCriticalConfig](#LowDiskSpaceCriticalConfig) | Alert if | Required |

##### The `LowDiskSpaceCriticalPercentage` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect low disk space (%) `enabled` | boolean | - | Required |
| `configuration` | [LowDiskSpaceCriticalPercentageConfig](#LowDiskSpaceCriticalPercentageConfig) | Alert if | Required |

##### The `LowDiskSpaceCriticalConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| the available disk space is below `threshold` | integer | - | Required |
| for at least `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |

##### The `LowDiskSpaceCriticalPercentageConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| the available disk space is below `threshold` | integer | - | Required |
| for at least `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |