---
title: Sizing guide for Dynatrace ActiveGates in the Kubernetes monitoring use-case
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits
scraped: 2026-02-22T21:27:34.508301
---

# Sizing guide for Dynatrace ActiveGates in the Kubernetes monitoring use-case

# Sizing guide for Dynatrace ActiveGates in the Kubernetes monitoring use-case

* Latest Dynatrace
* Reference
* 5-min read
* Updated on Feb 18, 2026

Setting appropriate resource requests (and limits, when needed) keeps Dynatrace ActiveGate instances stable and predictable. This guide details sizing methods based on scale and workload.

A stable, healthy ActiveGate ensures continuous gapâfree monitoring data.

## Understanding the sizing drivers

Actual required resources increase with:

* **Number of pods**âThe primary sizing driver is the number of monitored pods. The resource consumption (CPU and memory) for Dynatrace ActiveGate components scales with the number of pods primarily due to increased data processing and storage needs. As the number of monitored pods grows, the ActiveGate handles more entity data, events, and metrics, resulting in higher CPU load for ingestion and processing, as well as increased memory for caching pod-related information. This is the primary sizing driver, with consumption scaling proportionally to pod count.
* **Prometheus metrics volume**âThe number of Prometheus annotated pods directly correlates with increased resource requirements for Dynatrace ActiveGate, primarily through higher CPU consumption. As the count of annotated pods rises, the volume of scraped metrics grows, demanding more CPU cycles for collection, aggregation, and forwarding tasks. Memory impact is secondary, as metrics are forwarded to the Dynatrace tenant without long-term storage on the ActiveGate, though it scales proportionally with peak ingest rates.
* **Number of nodes**âThe resource consumption (CPU and memory) for Dynatrace ActiveGate components scales with the number of nodes primarily due to increased monitoring overhead and load from node-level system pods. As the node count grows, the ActiveGate must handle more system-level data collection, entity processing, and event ingestion, leading to higher computational demands. This is a secondary driver compared to the number of pods, but it contributes proportionally to overall resource needs, especially in larger clusters where node-level monitoring adds cumulative load.
* **Number of clusters monitored**âA single ActiveGate can monitor multiple clusters, however, this deployment pattern is **not recommended**. Monitoring multiple clusters with a single ActiveGate increases both CPU and memory requirements proportionally for each additional cluster, as the ActiveGate must handle more data processing, entity management, and event ingestion across clusters. This can lead to resource contention, higher risk of throttling or OOM restarts, and potential gaps in monitoring data.

**We recommend a setup where one containerized ActiveGate is monitoring one Kubernetes cluster.**

This ensures optimal performance and reliability. This approach simplifies troubleshooting, avoids resource contention, and ensures predictable scaling as each ActiveGate handles only one clusterâs workload.

## Signs of an unhealthy ActiveGate

These symptoms indicate exhausted resources and potential data loss.

### Gaps in monitoring data

ActiveGate collects different types of data independently (for example, Prometheus metrics, Kubernetes events, entities). If one collection task takes longer than 1 minute, only that data type experiences a gap for that window. Other collection tasks continue operating normally.

* Metrics will have missing data point for the given minute.
* Events for the given collection timeframes are not available at all.
* Entities may not reflect the latest updates or may be missing at all if short-living.

### Heavy CPU throttling

Sustained high throttling means insufficient CPU. Heavy throttling can cause gaps. Minor throttling is usually harmless.
If the throttling affects the pod serving the monitoring ActiveGate this can cause data gaps.

### Outâofâmemory restarts

If the ActiveGate is OOM-killed, data becomes unavailable until it restarts. After a restart, repeated OOM kills are likely to occur.

## Monitoring and validation

The following indicators can be tracked to understand if the ActiveGate is in a healthy operational state.

* **CPU usage vs requests**âIf CPU utilization consistently exceeds 85% increase the CPU request.
* **CPU throttling** (container\_cpu\_cfs\_throttled\_periods\_total / periods)âIf throttling exceeds 10% consistently, increase the CPU request.
* **Memory working set vs request**âIf usage consistently exceeds 80%, increase the memory request.
* **ActiveGate restart count**âAfter an OOM-based restart, promptly raise the configured memory to prevent recurrence.
* **Processing duration / cycle time** âIf the execution time of pipelines consistently exceeds 50 - 60 seconds, increase the CPU request. The pipeline execution time also depends on the amount of ingested data and other factors.
* **Garbage collection times**âIncreasing garbage collection times are a clear indicator for an under-provisioned ActiveGate.

Metrics reference

The indicators for unhealthy ActiveGates are as following:

| Indicator | Platform metrics for validation | Classic metrics for validation | Detail level |
| --- | --- | --- | --- |
| CPU usage | `dt.kubernetes.container.cpu_usage` | `builtin:kubernetes.node.cpu_usage` `builtin:kubernetes.workload.cpu_usage` | ActiveGate pod |
| CPU requests | `dt.kubernetes.resourcequota.requests_cpu` | `builtin:kubernetes.node.requests_cpu` `builtin:kubernetes.workload.requests_cpu` | ActiveGate pod |
| CPU throttling | `dt.kubernetes.container.cpu_throttled` | `builtin:kubernetes.workload.cpu_throttled` `builtin:kubernetes.node.cpu_throttled` | ActiveGate pod |
| Memory working set | `dt.kubernetes.container.memory_working_set` | `builtin:kubernetes.node.memory_working_set` `builtin:kubernetes.workload.memory_working_set` | ActiveGate pod |
| Memory requests | `dt.kubernetes.resourcequota.requests_memory` | `builtin:kubernetes.node.requests_memory` `builtin:kubernetes.workload.requests_memory` | ActiveGate pod |
| Restart count | `dt.kubernetes.container.restarts` | `builtin:kubernetes.container.restarts` | ActiveGate pod |
| OOM kills | `dt.kubernetes.container.oom_kills` | `builtin:kubernetes.container.oom_kills` | ActiveGate pod |
| Processing duration | `dt.sfm.active_gate.kubernetes.pipeline_duration` | `dsfm:active_gate.kubernetes.pipeline_duration` | ActiveGate ID |
| Garbage collection times | `dt.sfm.active_gate.jvm.gc.major_collection_time` | `dsfm:active_gate.jvm.gc.major_collection_time` | ActiveGate ID |

### Increasing resources

Start with the recommended values below.

1. Verify ActiveGate health using the monitoring indicators.
2. Adjust resources as needed:

   * Increase memory in 2Gi increments.
   * Increase CPU in 500m increments.
3. Adjust request first and in a later step adjust the limits.

   * Regarding CPU: Use limits only if required by policy.

## Using a dedicated ActiveGate for Kubernetes platform monitoring

Splitting ActiveGate responsibilities into two groups is recommended: One group handling everything related to Kubernetes platform monitoring, including KSPM, and the other managing Agent traffic routing, telemetry ingest, and extensions. This separation provides several advantages:

* **Isolation**âResource contention in one module doesn't affect the other. A spike in OneAgent traffic won't slow down Kubernetes metrics collection, and vice versa.
* **Independent scaling**âTraffic forwarding and platform monitoring have fundamentally different scaling characteristics:

  + **Kubernetes platform monitoring** can only scale vertically â when cluster size grows, you increase CPU and memory resources for the corresponding ActiveGate.
  + **OneAgent traffic routing** can be horizontally scaled â when OneAgent traffic increases, additional routing ActiveGate replicas help distribute and share the load.

  Separate ActiveGates let you scale each dimension independently without overâprovisioning resources. For example, you can add 3 more routing replicas to handle increased application traffic without unnecessarily increasing resources for platform monitoring.
* **Easier troubleshooting** â When issues occur, you can immediately identify whether they originate from platform monitoring or OneAgent traffic, reducing diagnosis time.

## Sizing ActiveGate

Scenarios are established based on the number of pods that are monitored by a single ActiveGate. The necessary resources can be taken from the following tables.

* **Scenario S**: <1000 pods
* **Scenario M**: 1000â5000 pods
* **Scenario L**: 5000â20000 pods

  This guide does not cover environments with more than 20,000 pods. Due to the many variables involved, providing precise recommendations for such large-scale setups isnât feasible. As a starting point, you can use the guidance for the L scenario and gradually increase resources until stable gap-free monitoring is established.
  For tailored advice, we recommend reaching out to Dynatrace Support to ensure the best configuration for your environment.

### Secondary factors

#### Node count

As the number of nodes in your Kubernetes cluster increases, the ActiveGate needs more CPU and memory resources to handle the extra monitoring workload. This includes processing data from node-level system components and events, which adds up proportionally.
We group node counts into these categories for sizing guidance:

* Up to 25 nodes
* Up to 100 nodes
* Up to 500 nodes

If your cluster has more than 100 nodes, you'll need to adjust the resource allocations upward to account for the additional demands, ensuring stable and gap-free monitoring. For clusters beyond 500 nodes, consult Dynatrace Support for tailored recommendations.

#### Amount of Prometheus metrics scraped

Dynatrace supports up to 1000 pod exporters, with each exporter able to provide up to 1000 metrics. If your environment approaches these limits, you'll need to increase the resources allocated to the ActiveGate to ensure reliable performance.

### ActiveGate for Kubernetes platform monitoring

All the following use cases have actually the same requirements on the ActiveGate taking over the Kubernetes platform monitoring part.

* Kubernetes platform monitoring only
* Kubernetes platform monitoring + Application observability
* Kubernetes platform monitoring + Full-stack observability

| Pod count | CPU resource | Memory resource |
| --- | --- | --- |
| < 1000 ( Small ) | requests: 200m (limits: 1000m) | requests: 6Gi limits: 6Gi |
| < 5000 ( Medium ) | requests: 1000m (limits: 2000m) | requests: 10Gi limits: 10Gi |
| < 20000 ( Large ) | requests: 2000m (limits: 4000m) | requests: 12Gi limits: 12Gi |

We recommend running ActiveGates without CPU limits.

### ActiveGate for OneAgent traffic routing and proxying

The second ActiveGate does not actively participate in Kubernetes platform monitoring but is instead used as a router/proxy on behalf of data streams originating from the OneAgent.
We recommend to use separate ActiveGates for traffic forwarding and platform monitoring. Traffic forwarding scales horizontally by adding replicas. Kubernetes monitoring itself does not scale horizontally; instead increase resources.

This setup is required in the following use-cases:

* Kubernetes platform monitoring + Application observability
* Kubernetes platform monitoring + Full-stack observability

| Pod count | CPU resource | Memory resource | replicas |
| --- | --- | --- | --- |
| < 1000 ( Small ) | requests: 250m (limits: 1000m) | requests: 2Gi limits: 2Gi | 3 |
| < 5000 ( Medium ) | requests: 500m (limits: 2000m) | requests: 4Gi limits: 4Gi | 3 |
| < 20000 ( Large ) | requests: 1000m (limits: 4000m) | requests: 6Gi limits: 6Gi | 6 |

We recommend running ActiveGates without CPU limits.

## Getting started

The following examples apply the reasoning of splitting the ActiveGates into units with separate concerns. One ActiveGate is responsible for Kubernetes platform monitoring and Kubernetes security posture management, whereas the 2nd ActiveGate is then responsible for agent traffic routing, telemetry ingest and extensions.
Adjust requests (and limits if required) to fit your environment.

The following manifests includes two DynaKube resources for configuring ActiveGates:

* **k8s-monitoring** â Configures an ActiveGate dedicated to Kubernetes platform monitoring.
* **agents** â Configures an ActiveGate that supports OneAgent, telemetry ingest, and additional features.

You can apply both manifests at once or apply only the DynaKube you need.

CPU limits are commented out. We recommend defining requests only so the ActiveGate can use additional CPU when available. If limits are required, set them equal to or higher than requests.

This snippet includes configuration for Kubernetes Security Posture Management. It's a complementing, opt-in security feature next to Kubernetes platform monitoring.
This snippet also includes configurations for log monitoring, extensions and telemetry ingest. These sections are considered optional on a per-section basis.

DynaKubes for both Kubernetes platform monitoring and OneAgent, telemetry ingest, and additional features

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: k8s-monitoring



namespace: dynatrace



annotations:



feature.dynatrace.com/k8s-app-enabled: "true"



spec:



apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



tokens: <SECRET NAME>



# Link to api reference for further information: https://docs.dynatrace.com/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters



activeGate:



capabilities:



- kubernetes-monitoring



resources:



requests:



cpu: 1000m



memory: 10Gi



limits:



# cpu: 2000m



memory: 10Gi



#kspm:



#mappedHostPaths:



#- /boot



#- /etc



#- /proc/sys/kernel



#- /sys/fs



#- /sys/kernel/security/apparmor



#- /usr/lib/systemd/system



#- /var/lib



#templates:



#kspmNodeConfigurationCollector:



#imageRef:



#repository: public.ecr.aws/dynatrace/dynatrace-k8s-node-config-collector



#tag: 1.5.2



---



apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: agents



namespace: dynatrace



# Link to api reference for further information: https://docs.dynatrace.com/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters



spec:



apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



tokens: <SECRET NAME>



metadataEnrichment:



enabled: true



oneAgent:



applicationMonitoring: {}



activeGate:



capabilities:



- routing



- debugging



resources:



requests:



cpu: 1000m



memory: 6Gi



limits:



# cpu: 4000m



memory: 6Gi



replicas: 6



#customProperties:



#value: |



#[otlp_ingest]



#otlp_ingest_enabled = true



#logMonitoring: {}



#extensions: {}



#telemetryIngest:



#protocols:



#- jaeger



#- otlp



#- statsd



#- zipkin



#serviceName: telemetry-ingest



templates:



#logMonitoring:



#imageRef:



#repository: public.ecr.aws/dynatrace/dynatrace-logmodule



#tag: <>



#tolerations:



#- effect: NoSchedule



#  key: node-role.kubernetes.io/master



#  operator: Exists



#- effect: NoSchedule



#  key: node-role.kubernetes.io/control-plane



#  operator: Exists



#extensionExecutionController:



#imageRef:



#repository: <ENVIRONMENTID>/dynatrace/linux/dynatrace-eec



#tag: latest



#otelCollector:



#replicas: 1



#imageRef:



#repository: public.ecr.aws/dynatrace/dynatrace-otel-collector



#tag: <tag>
```