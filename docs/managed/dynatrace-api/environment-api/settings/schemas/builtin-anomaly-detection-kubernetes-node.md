---
title: Settings API - Kubernetes node anomaly detection schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-kubernetes-node
scraped: 2026-05-12T11:40:39.254450
---

# Settings API - Kubernetes node anomaly detection schema table

# Settings API - Kubernetes node anomaly detection schema table

* Published Dec 05, 2023

### Kubernetes node anomaly detection (`builtin:anomaly-detection.kubernetes.node)`

Dynatrace automatically detects a wide range of common Kubernetes-related issues. Use these settings to configure alerts relevant to your Kubernetes nodes. Changing thresholds resets the observation period. Additional information can be found on our [documentation pageï»¿](https://dt-url.net/wq02okj#node).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.kubernetes.node` | * `group:anomaly-detection.kubernetes` * `group:anomaly-detection` | `KUBERNETES_CLUSTER` - Kubernetes cluster  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.node` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.node` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.node` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `readinessIssues` | [ReadinessIssues](#ReadinessIssues) | Alerts if node has not been available for a given amount of time | Required |
| `nodeProblematicCondition` | [NodeProblematicCondition](#NodeProblematicCondition) | - | Required |
| `cpuRequestsSaturation` | [CpuRequestsSaturation](#CpuRequestsSaturation) | - | Required |
| `memoryRequestsSaturation` | [MemoryRequestsSaturation](#MemoryRequestsSaturation) | - | Required |
| `podsSaturation` | [PodsSaturation](#PodsSaturation) | - | Required |

##### The `ReadinessIssues` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect node readiness issues `enabled` | boolean | Evaluates node condition 'Ready' | Required |
| `configuration` | [ReadinessIssuesConfig](#ReadinessIssuesConfig) | Alert if | Required |

##### The `NodeProblematicCondition` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect problematic node conditions `enabled` | boolean | Evaluates node conditions  * MemoryPressure * DiskPressure * PIDPressure * OutOfDisk * NetworkUnavailable * KernelDeadlock * ReadonlyFilesystem * FrequentKubeletRestart * FrequentDockerRestart * FrequentContainerdRestart * KubeletUnhealthy * ContainerRuntimeUnhealthy * ContainerRuntimeProblem * CorruptDockerOverlay2 * FilesystemCorruptionProblem * FrequentGcfsdRestart * FrequentGcfsSnapshotterRestart * FrequentUnregisterNetDevice * GcfsdUnhealthy * GcfsSnapshotterMissingLayer * GcfsSnapshotterUnhealthy * KubeletProblem | Required |
| `configuration` | [NodeProblematicConditionConfig](#NodeProblematicConditionConfig) | Alert if | Required |

##### The `CpuRequestsSaturation` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect node CPU-request saturation `enabled` | boolean | - | Required |
| `configuration` | [CpuRequestsSaturationConfig](#CpuRequestsSaturationConfig) | Alert if | Required |

##### The `MemoryRequestsSaturation` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect node memory-request saturation `enabled` | boolean | - | Required |
| `configuration` | [MemoryRequestsSaturationConfig](#MemoryRequestsSaturationConfig) | Alert if | Required |

##### The `PodsSaturation` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect node pod-saturation `enabled` | boolean | Number of running pods in percent of the node's maximum pod capacity | Required |
| `configuration` | [PodsSaturationConfig](#PodsSaturationConfig) | Alert if | Required |

##### The `ReadinessIssuesConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| node is not ready for at least `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |

##### The `NodeProblematicConditionConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| node has problematic conditions for at least `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |

##### The `CpuRequestsSaturationConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| amount of requested CPU is higher than `threshold` | integer | - | Required |
| of node CPU capacity for at least `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |

##### The `MemoryRequestsSaturationConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| amount of requested memory is higher than `threshold` | integer | - | Required |
| of node memory capacity for at least `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |

##### The `PodsSaturationConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| number of pods running on node is higher than `threshold` | integer | - | Required |
| of node capacity for at least `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |