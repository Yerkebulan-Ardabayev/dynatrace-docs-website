---
title: Alert on common Kubernetes/OpenShift issues
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/alert-on-kubernetes-issues
scraped: 2026-02-24T21:27:31.984651
---

# Alert on common Kubernetes/OpenShift issues

# Alert on common Kubernetes/OpenShift issues

* 18-min read
* Updated on Feb 21, 2025

Dynatrace version 1.254+

ActiveGate version 1.253+

To [alert on common Kubernetes platform issuesï»¿](https://dt-url.net/zg034mg), follow the instructions below.

## Configure

There are three ways to configure alerts for common Kubernetes/OpenShift issues.

Configuring an alert on a different level is only intended to simplify the configuration of multiple entities at once. It does not change the behavior of an alert.

For example, enabling a workload CPU usage saturation alert will still evaluate and raise problems for each Kubernetes workload separately, even if it has been configured on the Kubernetes cluster level.

For further details on the settings hierarchy, see [Settings documentation](/docs/manage/settings/settings-20#scope-and-hierarchy-of-settings "Introduction to the Settings 2.0 framework").

Per tenant level

Per cluster level

Per namespace level

* Settings apply to all clusters, nodes, namespaces, or workloads in the Kubernetes/OpenShift tenant.
* To configure settings, go to **Settings** > **Anomaly detection** and select any page under the **Kubernetes** section.

**Example:**

![Kubernetes anomaly detection settings tenant](https://dt-cdn.net/images/k8s-anomaly-settings-tenant-899-e99e56395b.png)

* Settings apply to a selected cluster, or to nodes, namespaces, and workloads from a selected cluster.
* To configure settings, go to the settings of a selected Kubernetes cluster and select any page under **Anomaly detection**.

**Example:**

![Kubernetes anomaly detection settings cluster](https://dt-cdn.net/images/k8s-anomaly-settings-cluster-948-0650f7b0a9.png)

* Settings apply to selected namespaces or workloads.
* To configure settings, go to the settings of a selected namespace and select any page under **Anomaly detection**.

**Example:**

![Kubernetes anomaly detection settings namespace](https://dt-cdn.net/images/k8s-anomaly-settings-namespace-899-1870ebd4ea.png)

## View alerts

Manually closed problems will show up again after 60 days if their root cause remains unresolved.

You can view alerts

* On the **Problems** page.

  **Example problem:**

  ![k8s-alert-view-in-problems](https://dt-cdn.net/images/image-12-1416-df0a0171a6.png)
* In the **Events** section of a cluster details page.

  **Example event:**

  ![k8s-alert-view-in-events](https://dt-cdn.net/images/image-13-799-41970d77a3.png)

  Select the event to navigate to Data Explorer for more information about the metric that generated the event.

## Available alerts

See below for a list of available alerts.

### Cluster alerts

Cluster metric and DQL expressions

#### Detect cluster CPU-request saturation

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.node.requests_cpu:splitBy():sum/builtin:kubernetes.node.cpu_allocatable:splitBy():sum*100.0` |
| DQL | `timeseries {o1=sum(dt.kubernetes.container.requests_cpu, rollup: avg), o2=sum(dt.kubernetes.node.cpu_allocatable, rollup: avg)}, by: {}| fieldsAdd result=o1[]/o2[]* 100.0| fieldsRemove {o1,o2}` |

#### Detect cluster memory-request saturation

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.node.requests_memory:splitBy():sum/builtin:kubernetes.node.memory_allocatable:splitBy():sum*100.0` |
| DQL | `timeseries {o1=sum(dt.kubernetes.container.requests_memory, rollup: avg), o2=sum(dt.kubernetes.node.memory_allocatable, rollup: avg)}, by: {}| fieldsAdd result=o1[]/o2[]* 100.0| fieldsRemove {o1,o2}` |

#### Detect cluster pod-saturation

| Type | Expression |
| --- | --- |
| Metric expression | `(builtin:kubernetes.node.pods:filter(and(eq(pod_condition,Ready))):splitBy():sum/builtin:kubernetes.node.pods_allocatable:splitBy():sum):default(0.0)*100.0` |
| DQL | `timeseries o1=sum(dt.kubernetes.pods, rollup: avg), nonempty:true, filter: {((pod_condition=="Ready"))}, by: {}| join [timeseries operand=sum(dt.kubernetes.node.pods_allocatable, rollup: avg), nonempty:true, by: {}], on: {interval}, fields: {o2=operand}| fieldsAdd result=if(isNull(o1[]/o2[]), 0.0, else: o1[]/o2[])* 100.0| fieldsRemove {o1,o2}` |

#### Detect cluster readiness issues

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.cluster.readyz:splitBy():sum` |
| DQL | `timeseries {sum(dt.kubernetes.cluster.readyz, rollup: avg)}, by: {}` |

#### Detect monitoring issues

| Type | Expression |
| --- | --- |
| Metric expression | `(no metric expression)` |
| DQL | `(no DQL)` |

Default alerts for new tenants

### Namespace alerts

Namespace metric and DQL expressions

#### Detect namespace CPU-limit quota saturation

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.resourcequota.limits_cpu_used:splitBy(k8s.namespace.name):sum/builtin:kubernetes.resourcequota.limits_cpu:splitBy(k8s.namespace.name):sum*100.0` |
| DQL | `timeseries {o1=sum(dt.kubernetes.resourcequota.limits_cpu_used, rollup: avg), o2=sum(dt.kubernetes.resourcequota.limits_cpu, rollup: avg)}, by: {k8s.namespace.name}| fieldsAdd result=o1[]/o2[]* 100.0| fieldsRemove {o1,o2}` |

#### Detect namespace CPU-request quota saturation

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.resourcequota.requests_cpu_used:splitBy(k8s.namespace.name):sum/builtin:kubernetes.resourcequota.requests_cpu:splitBy(k8s.namespace.name):sum*100.0` |
| DQL | `timeseries {o1=sum(dt.kubernetes.resourcequota.requests_cpu_used, rollup: avg), o2=sum(dt.kubernetes.resourcequota.requests_cpu, rollup: avg)}, by: {k8s.namespace.name}| fieldsAdd result=o1[]/o2[]* 100.0| fieldsRemove {o1,o2}` |

#### Detect namespace memory-limit quota saturation

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.resourcequota.limits_memory_used:splitBy(k8s.namespace.name):sum/builtin:kubernetes.resourcequota.limits_memory:splitBy(k8s.namespace.name):sum*100.0` |
| DQL | `timeseries {o1=sum(dt.kubernetes.resourcequota.limits_memory_used, rollup: avg), o2=sum(dt.kubernetes.resourcequota.limits_memory, rollup: avg)}, by: {k8s.namespace.name}| fieldsAdd result=o1[]/o2[]* 100.0| fieldsRemove {o1,o2}` |

#### Detect namespace memory-request quota saturation

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.resourcequota.requests_memory_used:splitBy(k8s.namespace.name):sum/builtin:kubernetes.resourcequota.requests_memory:splitBy(k8s.namespace.name):sum*100.0` |
| DQL | `timeseries {o1=sum(dt.kubernetes.resourcequota.requests_memory_used, rollup: avg), o2=sum(dt.kubernetes.resourcequota.requests_memory, rollup: avg)}, by: {k8s.namespace.name}| fieldsAdd result=o1[]/o2[]* 100.0| fieldsRemove {o1,o2}` |

#### Detect namespace pod quota saturation

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.resourcequota.pods_used:splitBy(k8s.namespace.name):sum/builtin:kubernetes.resourcequota.pods:splitBy(k8s.namespace.name):sum*100.0` |
| DQL | `timeseries {o1=sum(dt.kubernetes.resourcequota.pods_used, rollup: avg), o2=sum(dt.kubernetes.resourcequota.pods, rollup: avg)}, by: {k8s.namespace.name}| fieldsAdd result=o1[]/o2[]* 100.0| fieldsRemove {o1,o2}` |

### Node alerts



Node metric and DQL expressions

#### Detect node CPU-request saturation

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.node.requests_cpu:splitBy(dt.kubernetes.node.system_uuid,k8s.node.name):sum/builtin:kubernetes.node.cpu_allocatable:splitBy(dt.kubernetes.node.system_uuid,k8s.node.name):sum*100.0` |
| DQL | `timeseries {o1=sum(dt.kubernetes.container.requests_cpu, rollup: avg), o2=sum(dt.kubernetes.node.cpu_allocatable, rollup: avg)}, by: {dt.kubernetes.node.system_uuid,k8s.node.name}| fieldsAdd result=o1[]/o2[]* 100.0| fieldsRemove {o1,o2}` |

#### Detect node memory-request saturation

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.node.requests_memory:splitBy(dt.kubernetes.node.system_uuid,k8s.node.name):sum/builtin:kubernetes.node.memory_allocatable:splitBy(dt.kubernetes.node.system_uuid,k8s.node.name):sum*100.0` |
| DQL | `timeseries {o1=sum(dt.kubernetes.container.requests_memory, rollup: avg), o2=sum(dt.kubernetes.node.memory_allocatable, rollup: avg)}, by: {dt.kubernetes.node.system_uuid,k8s.node.name}| fieldsAdd result=o1[]/o2[]* 100.0| fieldsRemove {o1,o2}` |

#### Detect node pod-saturation

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.node.pods:filter(and(eq(pod_phase,Running))):splitBy(dt.kubernetes.node.system_uuid,k8s.node.name):sum/builtin:kubernetes.node.pods_allocatable:splitBy(dt.kubernetes.node.system_uuid,k8s.node.name):sum*100.0` |
| DQL | `timeseries o1=sum(dt.kubernetes.pods, rollup: avg), nonempty:true, filter: {((pod_phase=="Running"))}, by: {dt.kubernetes.node.system_uuid,k8s.node.name}| join [timeseries operand=sum(dt.kubernetes.node.pods_allocatable, rollup: avg), nonempty:true, by: {dt.kubernetes.node.system_uuid,k8s.node.name}], on: {interval}, fields: {o2=operand}| fieldsAdd result=o1[]/o2[]* 100.0| fieldsRemove {o1,o2}` |

#### Detect node readiness issues

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.node.conditions:filter(and(eq(node_condition,Ready),ne(condition_status,True))):splitBy(dt.kubernetes.node.system_uuid,k8s.node.name):sum` |
| DQL | `timeseries {sum(dt.kubernetes.node.conditions, rollup: avg)}, filter: {((node_condition=="Ready")AND(condition_status!=true))}, by: {dt.kubernetes.node.system_uuid,k8s.node.name}` |

#### Detect problematic node conditions

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.node.conditions:filter(and(or(eq(node_condition,ContainerRuntimeProblem),eq(node_condition,ContainerRuntimeUnhealthy),eq(node_condition,CorruptDockerOverlay2),eq(node_condition,DiskPressure),eq(node_condition,FilesystemCorruptionProblem),eq(node_condition,FrequentContainerdRestart),eq(node_condition,FrequentDockerRestart),eq(node_condition,FrequentGcfsSnapshotterRestart),eq(node_condition,FrequentGcfsdRestart),eq(node_condition,FrequentKubeletRestart),eq(node_condition,FrequentUnregisterNetDevice),eq(node_condition,GcfsSnapshotterMissingLayer),eq(node_condition,GcfsSnapshotterUnhealthy),eq(node_condition,GcfsdUnhealthy),eq(node_condition,KernelDeadlock),eq(node_condition,KubeletProblem),eq(node_condition,KubeletUnhealthy),eq(node_condition,MemoryPressure),eq(node_condition,NetworkUnavailable),eq(node_condition,OutOfDisk),eq(node_condition,PIDPressure),eq(node_condition,ReadonlyFilesystem)),eq(condition_status,True))):splitBy(dt.kubernetes.node.system_uuid,k8s.node.name):sum` |
| DQL | `timeseries {sum(dt.kubernetes.node.conditions, rollup: avg)}, filter: {(((node_condition=="ContainerRuntimeProblem")OR(node_condition=="ContainerRuntimeUnhealthy")OR(node_condition=="CorruptDockerOverlay2")OR(node_condition=="DiskPressure")OR(node_condition=="FilesystemCorruptionProblem")OR(node_condition=="FrequentContainerdRestart")OR(node_condition=="FrequentDockerRestart")OR(node_condition=="FrequentGcfsSnapshotterRestart")OR(node_condition=="FrequentGcfsdRestart")OR(node_condition=="FrequentKubeletRestart")OR(node_condition=="FrequentUnregisterNetDevice")OR(node_condition=="GcfsSnapshotterMissingLayer")OR(node_condition=="GcfsSnapshotterUnhealthy")OR(node_condition=="GcfsdUnhealthy")OR(node_condition=="KernelDeadlock")OR(node_condition=="KubeletProblem")OR(node_condition=="KubeletUnhealthy")OR(node_condition=="MemoryPressure")OR(node_condition=="NetworkUnavailable")OR(node_condition=="OutOfDisk")OR(node_condition=="PIDPressure")OR(node_condition=="ReadonlyFilesystem"))AND(condition_status==true))}, by: {dt.kubernetes.node.system_uuid,k8s.node.name}` |

Default alerts for new tenants

### Persistent volume claims alerts

Persistent volume claims metric and DQL expressions

#### Detect low disk space (%)

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.persistentvolumeclaim.available:splitBy(k8s.namespace.name,k8s.persistent_volume_claim.name):avg/builtin:kubernetes.persistentvolumeclaim.capacity:splitBy(k8s.namespace.name,k8s.persistent_volume_claim.name):avg*100.0` |
| DQL | `timeseries {o1=avg(dt.kubernetes.persistentvolumeclaim.available), o2=avg(dt.kubernetes.persistentvolumeclaim.capacity)}, by: {k8s.namespace.name,k8s.persistent_volume_claim.name}| fieldsAdd result=o1[]/o2[]* 100.0| fieldsRemove {o1,o2}` |

#### Detect low disk space (MiB)

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.persistentvolumeclaim.available:splitBy(k8s.namespace.name,k8s.persistent_volume_claim.name):avg` |
| DQL | `timeseries {avg(dt.kubernetes.persistentvolumeclaim.available)}, by: {k8s.namespace.name,k8s.persistent_volume_claim.name}` |

### Workload alerts



Workload metric and DQL expressions

#### Detect CPU usage saturation

| Type | Expression |
| --- | --- |
| Metric expression | `(builtin:kubernetes.workload.cpu_usage:splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum/builtin:kubernetes.workload.limits_cpu:splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum):default(0.0)*100.0` |
| DQL | `timeseries {o1=sum(dt.kubernetes.container.cpu_usage, rollup: avg), o2=sum(dt.kubernetes.container.limits_cpu, rollup: avg)}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}| fieldsAdd result=if(isNull(o1[]/o2[]), 0.0, else: o1[]/o2[])* 100.0| fieldsRemove {o1,o2}` |

#### Detect container restarts

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.container.restarts:splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum:default(0.0)` |
| DQL | `timeseries {sum(dt.kubernetes.container.restarts, default:0.0, rollup: avg)}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}` |

#### Detect high CPU throttling

| Type | Expression |
| --- | --- |
| Metric expression | `(builtin:kubernetes.workload.cpu_throttled:splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum/builtin:kubernetes.workload.limits_cpu:splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum):default(0.0)*100.0` |
| DQL | `timeseries {o1=sum(dt.kubernetes.container.cpu_throttled, rollup: avg), o2=sum(dt.kubernetes.container.limits_cpu, rollup: avg)}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}| fieldsAdd result=if(isNull(o1[]/o2[]), 0.0, else: o1[]/o2[])* 100.0| fieldsRemove {o1,o2}` |

#### Detect job failure events

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.events:filter(and(or(eq(k8s.event.reason,BackoffLimitExceeded),eq(k8s.event.reason,DeadlineExceeded),eq(k8s.event.reason,PodFailurePolicy)),or(eq(k8s.workload.kind,job),eq(k8s.workload.kind,cronjob)))):splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum:default(0.0)` |
| DQL | `timeseries {sum(dt.kubernetes.events, default:0.0, rollup: avg)}, filter: {(((k8s.event.reason=="BackoffLimitExceeded")OR(k8s.event.reason=="DeadlineExceeded")OR(k8s.event.reason=="PodFailurePolicy"))AND((k8s.workload.kind=="job")OR(k8s.workload.kind=="cronjob")))}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}` |

#### Detect memory usage saturation

| Type | Expression |
| --- | --- |
| Metric expression | `(builtin:kubernetes.workload.memory_working_set:splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum/builtin:kubernetes.workload.limits_memory:splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum):default(0.0)*100.0` |
| DQL | `timeseries {o1=sum(dt.kubernetes.container.memory_working_set, rollup: avg), o2=sum(dt.kubernetes.container.limits_memory, rollup: avg)}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}| fieldsAdd result=if(isNull(o1[]/o2[]), 0.0, else: o1[]/o2[])* 100.0| fieldsRemove {o1,o2}` |

#### Detect out-of-memory kills

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.container.oom_kills:splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum:default(0.0)` |
| DQL | `timeseries {sum(dt.kubernetes.container.oom_kills, default:0.0, rollup: avg)}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}` |

#### Detect pod backoff events

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.events:filter(and(eq(k8s.event.reason,BackOff))):splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum:default(0.0)` |
| DQL | `timeseries {sum(dt.kubernetes.events, default:0.0, rollup: avg)}, filter: {((k8s.event.reason=="BackOff"))}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}` |

#### Detect pod eviction events

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.events:filter(and(eq(k8s.event.reason,Evicted))):splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum:default(0.0)` |
| DQL | `timeseries {sum(dt.kubernetes.events, default:0.0, rollup: avg)}, filter: {((k8s.event.reason=="Evicted"))}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}` |

#### Detect pod preemption events

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.events:filter(or(eq(k8s.event.reason,Preempted),eq(k8s.event.reason,Preempting))):splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum:default(0.0)` |
| DQL | `timeseries {sum(dt.kubernetes.events, default:0.0, rollup: avg)}, filter: {((k8s.event.reason=="Preempted")OR(k8s.event.reason=="Preempting"))}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}` |

#### Detect pods stuck in pending

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.pods:filter(and(eq(pod_phase,Pending))):splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum` |
| DQL | `timeseries {sum(dt.kubernetes.pods, rollup: avg)}, filter: {((pod_phase=="Pending"))}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}` |

#### Detect pods stuck in terminating

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.pods:filter(and(eq(pod_status,Terminating))):splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum` |
| DQL | `timeseries {sum(dt.kubernetes.pods, rollup: avg)}, filter: {((pod_status=="Terminating"))}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}` |

#### Detect stuck deployments

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.workload.conditions:filter(and(eq(workload_condition,Progressing),eq(condition_status,False))):splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum` |
| DQL | `timeseries {sum(dt.kubernetes.workload.conditions, rollup: avg)}, filter: {((workload_condition=="Progressing")AND(condition_status==false))}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}` |

#### Detect workloads with non-ready pods

The following expression returns the number of pending and running pods in the non-ready condition. Pods of Jobs and CronJobs are excluded.

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.pods:filter(and(ne(pod_phase,Failed),ne(pod_phase,Succeeded),ne(k8s.workload.kind,job),ne(k8s.workload.kind,cronjob),ne(pod_status,Terminating))):splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum-builtin:kubernetes.pods:filter(and(ne(pod_phase,Failed),ne(pod_phase,Succeeded),ne(k8s.workload.kind,job),ne(k8s.workload.kind,cronjob),eq(pod_condition,Ready),ne(pod_status,Terminating))):splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum:default(0.0)` |
| DQL | `timeseries o1=sum(dt.kubernetes.pods, rollup: avg), filter: {((pod_phase!="Failed")AND(pod_phase!="Succeeded")AND(k8s.workload.kind!="job")AND(k8s.workload.kind!="cronjob")AND(pod_status!="Terminating"))}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}| join [timeseries operand=sum(dt.kubernetes.pods, default:0.0, rollup: avg), nonempty:true, filter: {((pod_phase!="Failed")AND(pod_phase!="Succeeded")AND(k8s.workload.kind!="job")AND(k8s.workload.kind!="cronjob")AND(pod_condition=="Ready")AND(pod_status!="Terminating"))}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}], on: {interval}, fields: {o2=operand}| fieldsAdd result=o1[]-o2[]| fieldsRemove {o1,o2}` |

#### Detect workloads without ready pods

The following expression returns the number of pending and running pods in the ready condition. Pods of Jobs and CronJobs are excluded.

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.pods:filter(and(ne(pod_phase,Failed),ne(pod_phase,Succeeded),ne(k8s.workload.kind,job),ne(k8s.workload.kind,cronjob))):splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum-builtin:kubernetes.pods:filter(and(ne(pod_phase,Failed),ne(pod_phase,Succeeded),ne(k8s.workload.kind,job),ne(k8s.workload.kind,cronjob),ne(pod_condition,Ready))):splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum:default(0.0)` |
| DQL | `timeseries o1=sum(dt.kubernetes.pods, rollup: avg), filter: {((pod_phase!="Failed")AND(pod_phase!="Succeeded")AND(k8s.workload.kind!="job")AND(k8s.workload.kind!="cronjob"))}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}| join [timeseries operand=sum(dt.kubernetes.pods, default:0.0, rollup: avg), nonempty:true, filter: {((pod_phase!="Failed")AND(pod_phase!="Succeeded")AND(k8s.workload.kind!="job")AND(k8s.workload.kind!="cronjob")AND(pod_condition!="Ready"))}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}], on: {interval}, fields: {o2=operand}| fieldsAdd result=o1[]-o2[]| fieldsRemove {o1,o2}` |

#### Default alerts for new tenants

## Related topics

* [Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")