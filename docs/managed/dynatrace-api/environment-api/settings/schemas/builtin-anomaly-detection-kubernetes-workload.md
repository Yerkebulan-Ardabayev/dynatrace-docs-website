---
title: Settings API - Kubernetes workload anomaly detection schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-kubernetes-workload
---

# Settings API - Kubernetes workload anomaly detection schema table

# Settings API - Kubernetes workload anomaly detection schema table

* Published Dec 05, 2023

### Kubernetes workload anomaly detection (`builtin:anomaly-detection.kubernetes.workload)`

Dynatrace automatically detects a wide range of common Kubernetes-related issues. Use these settings to configure alerts relevant to your Kubernetes workload. Changing thresholds resets the observation period. Additional information can be found on our [documentation page﻿](https://dt-url.net/wq02okj#workload).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.kubernetes.workload` | * `group:anomaly-detection.kubernetes` * `group:anomaly-detection` | `CLOUD_APPLICATION_NAMESPACE` - Kubernetes namespace  `KUBERNETES_CLUSTER` - Kubernetes cluster  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.workload` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.workload` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.workload` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `containerRestarts` | [ContainerRestarts](#ContainerRestarts) | - | Required |
| `deploymentStuck` | [DeploymentStuck](#DeploymentStuck) | - | Required |
| `pendingPods` | [PendingPods](#PendingPods) | - | Required |
| `podStuckInTerminating` | [PodStuckInTerminating](#PodStuckInTerminating) | - | Required |
| `workloadWithoutReadyPods` | [WorkloadWithoutReadyPods](#WorkloadWithoutReadyPods) | - | Required |
| `notAllPodsReady` | [NotAllPodsReady](#NotAllPodsReady) | - | Required |
| `highMemoryUsage` | [HighMemoryUsage](#HighMemoryUsage) | - | Required |
| `highCpuUsage` | [HighCpuUsage](#HighCpuUsage) | - | Required |
| `highCpuThrottling` | [HighCpuThrottling](#HighCpuThrottling) | - | Required |
| `oomKills` | [OOMKills](#OOMKills) | - | Required |
| `jobFailureEvents` | [JobFailureEvents](#JobFailureEvents) | - | Required |
| `podBackoffEvents` | [PodBackoffEvents](#PodBackoffEvents) | - | Required |
| `podEvictionEvents` | [PodEvictionEvents](#PodEvictionEvents) | - | Required |
| `podPreemptionEvents` | [PodPreemptionEvents](#PodPreemptionEvents) | - | Required |

##### The `ContainerRestarts` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect container restarts `enabled` | boolean | - | Required |
| `configuration` | [ContainerRestartsConfig](#ContainerRestartsConfig) | Alert if | Required |

##### The `DeploymentStuck` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect stuck deployments `enabled` | boolean | Evaluates workload condition 'Progressing' | Required |
| `configuration` | [DeploymentStuckConfig](#DeploymentStuckConfig) | Alert if | Required |

##### The `PendingPods` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect pods stuck in pending `enabled` | boolean | Number of pods in `Pending` phase | Required |
| `configuration` | [PendingPodsConfig](#PendingPodsConfig) | Alert if | Required |

##### The `PodStuckInTerminating` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect pods stuck in terminating `enabled` | boolean | Deleted pods in 'Running' phase | Required |
| `configuration` | [PodStuckInTerminatingConfig](#PodStuckInTerminatingConfig) | Alert if | Required |

##### The `WorkloadWithoutReadyPods` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect workloads without ready pods `enabled` | boolean | As of specific pod life cycles of different workload types, cronjobs and jobs are excluded. | Required |
| `configuration` | [WorkloadWithoutReadyPodsConfig](#WorkloadWithoutReadyPodsConfig) | Alert if | Required |

##### The `NotAllPodsReady` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect workloads with non-ready pods `enabled` | boolean | As of specific pod life cycles of different workload types, cronjobs and jobs are excluded. | Required |
| `configuration` | [NotAllPodsReadyConfig](#NotAllPodsReadyConfig) | Alert if | Required |

##### The `HighMemoryUsage` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect memory usage saturation `enabled` | boolean | Memory usage (working set memory) is close to limits. | Required |
| `configuration` | [HighMemoryUsageConfig](#HighMemoryUsageConfig) | Alert if | Required |

##### The `HighCpuUsage` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect CPU usage saturation `enabled` | boolean | CPU usage is close to limits. | Required |
| `configuration` | [HighCpuUsageConfig](#HighCpuUsageConfig) | Alert if | Required |

##### The `HighCpuThrottling` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect high CPU throttling `enabled` | boolean | The CPU throttling to limits ratio exceeds the specified threshold. Important: This alert uses throttled seconds / limits (in millicores) in contrast to Prometheus and Grafana, which use throttled periods / total periods for the throttling ratio. | Required |
| `configuration` | [HighCpuThrottlingConfig](#HighCpuThrottlingConfig) | Alert if | Required |

##### The `OOMKills` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect out-of-memory kills `enabled` | boolean | - | Required |
| `configuration` | [OOMKillsConfig](#OOMKillsConfig) | Alert if | Required |

##### The `JobFailureEvents` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect job failure events `enabled` | boolean | Alerts on any occurrence of Kubernetes events with reason 'BackoffLimitExceeded', 'DeadlineExceeded', or 'PodFailurePolicy'.  If 'Filter events' is enabled, make certain that you ingest events with the aforementioned reasons in order to receive alerts. | Required |
| `configuration` | [JobFailureEventsConfig](#JobFailureEventsConfig) | Alert if | Required |

##### The `PodBackoffEvents` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect pod backoff events `enabled` | boolean | Alerts on any occurrence of Kubernetes events with reason 'BackOff', as observed on pod statuses 'ImagePullBackOff', and 'CrashLoopBackOff'.  If 'Filter events' is enabled, make certain that you ingest events with the aforementioned reasons in order to receive alerts. | Required |
| `configuration` | [PodBackoffEventsConfig](#PodBackoffEventsConfig) | Alert if | Required |

##### The `PodEvictionEvents` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect pod eviction events `enabled` | boolean | Eviction is the process of terminating one or more pods on a node to free up resources.  Alerts on any occurrence of Kubernetes events with reason 'Evicted'.  If 'Filter events' is enabled, make certain that you ingest events with the aforementioned reasons in order to receive alerts. | Required |
| `configuration` | [PodEvictionEventsConfig](#PodEvictionEventsConfig) | Alert if | Required |

##### The `PodPreemptionEvents` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect pod preemption events `enabled` | boolean | Preemption is the process of terminating pods with lower priority so that pods with higher priority can be scheduled on a node.  Alerts on any occurrence of Kubernetes events with reason 'Preempted', or 'Preempting'.  If 'Filter events' is enabled, make certain that you ingest events with the aforementioned reasons in order to receive alerts. | Required |
| `configuration` | [PodPreemptionEventsConfig](#PodPreemptionEventsConfig) | Alert if | Required |

##### The `ContainerRestartsConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| there is at least `threshold` | integer | - | Required |
| per minute, for any `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |

##### The `DeploymentStuckConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| workload stops progressing for at least `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |

##### The `PendingPodsConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| there is at least `threshold` | integer | - | Required |
| stuck in pending state for at least `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |

##### The `PodStuckInTerminatingConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| pod termination stops progressing for at least `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |

##### The `WorkloadWithoutReadyPodsConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| workload has no ready pods for at least `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |

##### The `NotAllPodsReadyConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| some workload pods are not ready for at least `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |

##### The `HighMemoryUsageConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| amount of utilized workload memory is above `threshold` | integer | - | Required |
| of defined memory limits for at least `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |

##### The `HighCpuUsageConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| amount of utilized workload CPU is above `threshold` | integer | - | Required |
| of defined CPU limits for at least `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |

##### The `HighCpuThrottlingConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| amount of CPU throttling is above `threshold` | integer | - | Required |
| of CPU usage for at least `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |

##### The `OOMKillsConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| events occurred within any `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |

##### The `JobFailureEventsConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| events occurred within any `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |

##### The `PodBackoffEventsConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| events occurred within any `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |

##### The `PodEvictionEventsConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| events occurred within any `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |

##### The `PodPreemptionEventsConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| events occurred within any `samplePeriodInMinutes` | integer | - | Required |
| within the last `observationPeriodInMinutes` | integer | - | Required |