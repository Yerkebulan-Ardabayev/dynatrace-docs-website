---
title: Size Dynatrace ActiveGates in Kubernetes
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits
---

# Size Dynatrace ActiveGates in Kubernetes

# Size Dynatrace ActiveGates in Kubernetes

* How-to guide
* 5-min read
* Updated on Jul 15, 2026

Setting appropriate resource requests (and limits, when needed) keeps your ActiveGate instances stable and predictable. A stable, healthy ActiveGate ensures continuous gap‑free monitoring data.

This guide details sizing recommendations according to the deployment type, deployment size, and assumed workload.

## Deployment recommendations

### Use separate ActiveGates

We recommend to run two sets of ActiveGates for production deployments:

* One set should cover Kubernetes platform monitoring, including any Prometheus integration and Kubernetes Security Posture Management (KSPM) functionalities.
* One set should cover OneAgent traffic routing and telemetry ingest (including OTLP log ingest).

Using two sets of ActiveGates has several advantages:

* **Isolation**: A spike in OneAgent traffic won't slow down Kubernetes metrics collection, and vice versa.
* **Independent scaling**: OneAgent traffic routing and platform monitoring have fundamentally different scaling characteristics, see [How to scale ActiveGates](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits#how-to-scale "Find CPU and memory resource recommendations for Dynatrace ActiveGates deployed in Kubernetes, sized by cluster scale and workload type.").
  Separate ActiveGates let you scale each dimension independently without over‑provisioning resources.
* **Easier troubleshooting**: When issues occur, you can immediately identify whether they originate from platform monitoring or OneAgent traffic, reducing diagnosis time.

### How to scale ActiveGates

When traffic increases beyond the capacity of your current ActiveGate deployment, you can scale in two ways:

* **Scale horizontally**: Increase the number of ActiveGate replicas in your DynaKube configuration. This allows the Kubernetes Service to distribute incoming traffic across multiple ActiveGate instances.
* **Scale vertically**: Increase CPU and memory resource requests for your ActiveGate replicas. Use the resource recommendations tables above as a starting point and adjust based on your actual throughput requirements. Adjust the requests first and then, if necessary, adjust the limits. Use CPU limits only if required by policy.

## Sizing recommendations

The following sections cover the four main deployment types: Kubernetes Platform Monitoring, OneAgent traffic routing and proxying, OTLP log ingestion, and combined log ingestion and OneAgent traffic routing. Identify your deployment type and apply the corresponding recommendations.

For each deployment type, we've organized recommendations according to the following cluster sizes: small, medium, and large.

| Cluster size | Pods | Nodes |
| --- | --- | --- |
| Small | <1,000 | Up to 25 |
| Medium | 1,000–5,000 | Up to 100 |
| Large | 5,000–20,000 | Up to 500 |

This guide does not cover environments with more than 20,000 pods; as a starting point, use the large cluster size guidance and gradually increase resources until stable gap-free monitoring is established.

Node count is a secondary sizing driver. For clusters beyond 500 nodes, contact Dynatrace Support for tailored recommendations.

### Kubernetes Platform Monitoring

This section provides sizing recommendations for the ActiveGate that handles Kubernetes Platform Monitoring, whether alone or in combination with Application Observability and Full-Stack Observability.

| Cluster size | CPU requests | CPU limits | Memory requests | Memory limits |
| --- | --- | --- | --- | --- |
| Small | 200m | 1000m | 6 GiB | 6 GiB |
| Medium | 1000m | 2000m | 10 GiB | 10 GiB |
| Large | 2000m | 4000m | 12 GiB | 12 GiB |

### OneAgent traffic routing and proxying

This section provides sizing recommendations for an ActiveGate that handles OneAgent traffic routing and proxying.
If this ActiveGate should also handle log ingest via API, see [Combined log ingestion and OneAgent traffic routing](#ag-log-oa).

| Cluster size | CPU requests | CPU limits | Memory requests | Memory limits | Replicas |
| --- | --- | --- | --- | --- | --- |
| Small | 250m | 1000m | 2 GiB | 2 GiB | 3 |
| Medium | 500m | 2000m | 4 GiB | 4 GiB | 3 |
| Large | 1000m | 4000m | 6 GiB | 6 GiB | 6 |

The sizing recommendations are based on representative workload testing:

* **Workload**: OneAgent traffic routing including metrics, traces, events, and log module data.
* **Log traffic assumption**: Average production load of 100 KB/min per monitored pod.

### OTLP log ingestion

This section provides sizing recommendations and throughput benchmarks for ActiveGates that handle log ingestion via the OTLP API endpoint.

| Cluster size | CPU requests | CPU limits | Memory requests | Memory limits | OTLP log throughput per replica |
| --- | --- | --- | --- | --- | --- |
| Small | 250m | 1000m | 2 GiB | 2 GiB | 350 MB/min |
| Medium | 500m | 2000m | 4 GiB | 4 GiB | 650 MB/min |
| Large | 1000m | 4000m | 6 GiB | 6 GiB | 1,200 MB/min |

The sizing recommendations are based on representative workload testing:

* **Workload**: Sustained log ingest via OTLP over HTTP (uncompressed).
* **Message sizes**: 5% extra-small (1.5 KB), 20% small (1.5 KB), 50% medium (2.2 KB), 20% large (3 KB), 5% extra-large (7.8 KB).
* **Attribute counts**: Varying from 5 to 100 attributes per log record.
* **Batch sizes**: Varying from 10 to 100 messages per API call.
* **Test environment**: Kubernetes cluster on Google Cloud Platform using e2-standard-8 machines (`x86_64`).
* **Deployment configuration**: ActiveGate provisioned with resource allocations matching the recommendations in the table above.

These resource configurations provide headroom for traffic spikes and replica failover during updates.

The sustained throughput values represent performance that meets all quality gates. Peak burst throughput may be higher for short durations.

### Combined log ingestion and OneAgent traffic routing

This section provides sizing recommendations for an ActiveGate that handles both log ingestion and OneAgent traffic routing in a unified deployment.
If your ActiveGate does not have any log ingestion via API, see [OneAgent traffic routing and proxying](#activegate-for-oneagent-traffic-routing-and-proxying).

1. **Determine base configuration**: Start with the base ActiveGate configuration for your cluster size from [OneAgent traffic routing and proxying](#activegate-for-oneagent-traffic-routing-and-proxying).
2. **Calculate additional replicas for OTLP log traffic**: Use the per-replica throughput values from [OTLP log ingestion](#activegate-for-otlp-log-ingestion) to calculate how many additional replicas your deployment needs: `additional replicas = ceil(expected log traffic (MB/min) ÷ throughput per replica)`.
   Add these replicas to your base configuration as calculated in step 1.

As an example, if your cluster generates 1,500 MB/min of OTLP log traffic and you're using the medium resource config (650 MB/min per replica): `ceil(1,500 ÷ 650) = 3 additional replicas`.

If you observe consistent resource exhaustion (CPU usage >80%, memory usage >85%, or frequent GC pauses), consider splitting the workload into separate ActiveGate deployments rather than continuously increasing resources for a single deployment. Separate deployments provide better isolation and independent scaling.
For more information, see [Deployment recommendations](#ag-for-k8s-platform-monitoring).

### Log Agent traffic routing capacity benchmarks

This section provides a reference benchmark for ActiveGate throughput when handling Log Agent traffic routing. The throughput values shown represent compressed log data volume and reflect the recommended operating maximum under sustained conditions.

How to use this benchmark:

* **Calculate your log traffic volume**: Estimate your total OneAgent log traffic volume (in MB/min). This depends on your application's logging behavior and volume, not just the number of pods.
* **Scale resources proportionally**: Throughput scales approximately linearly with CPU and memory. Use the benchmark values in the table above as a reference point and adjust resources based on your expected log traffic volume.
* **Headroom is included**: The listed values already reserve capacity for traffic spikes and replica failover. If you consistently exceed the recommended throughput, add replicas or increase per-replica resources. For more information, see [How to scale ActiveGates](#how-to-scale).

| CPU requests | CPU limits | Memory resource requests | Memory resource limits | Sustained maximum throughput per replica |
| --- | --- | --- | --- | --- |
| 500m | 2000m | 4Gi | 4Gi | 750 MB/min |

Actual throughput may vary depending on your infrastructure, OneAgent version, and workload composition. Monitor your ActiveGate instances and adjust resources based on observed performance.

## Monitor and validate

Monitor your ActiveGate instances to ensure load is distributed appropriately and adjust your scaling strategy based on observed performance and resource utilization patterns.

This section describes how to monitor your ActiveGates and verify they're behaving as expected.

### Signs of an unhealthy ActiveGate

These symptoms indicate exhausted resources and potential data loss:

* **Gaps in monitoring data**: ActiveGate collects different types of data independently (for example, Prometheus metrics, Kubernetes events, entities). If one collection task takes longer than one minute, only that data type experiences a gap for that window. Other collection tasks continue operating normally.

  + Metrics will have missing data point for the given minute.
  + Events for the given collection timeframes are not available at all.
  + Entities may not reflect the latest updates or may be missing at all if short-living.
* **Heavy CPU throttling**: Sustained high throttling means insufficient CPU. Heavy throttling can cause gaps. Minor throttling is usually harmless.
  If the throttling affects the pod serving the monitoring ActiveGate this can cause data gaps.
* **Out‑of‑memory kills**: If the ActiveGate is OOM-killed, data becomes unavailable until it restarts. After a restart, repeated OOM kills are likely to occur.

### Observe health with platform metrics

Dynatrace provides two [ready-made dashboards](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") to help you observe your ActiveGate health: **ActiveGate diagnostic overview** and **Kubernetes Monitoring Statistics**. To access these, go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** >  **Ready-made** and search for the dashboard by name.

Additionally, you can use [DQL](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") to query the following platform metrics and build your own dashboards or notebooks.

| Indicator | When to act | Classic metrics for validation | Detail level |
| --- | --- | --- | --- |
| CPU usage | Utilization consistently exceeds 85%: increase the CPU request. | `builtin:kubernetes.node.cpu_usage`, `builtin:kubernetes.workload.cpu_usage` | ActiveGate pod |
| CPU requests | Utilization consistently exceeds 85%: increase the CPU request. | `builtin:kubernetes.node.requests_cpu`, `builtin:kubernetes.workload.requests_cpu` | ActiveGate pod |
| CPU throttling | Throttling consistently exceeds 10%: increase the CPU request. Calculate by dividing `container_cpu_cfs_throttled_periods_total` by the number of periods. | `builtin:kubernetes.workload.cpu_throttled`, `builtin:kubernetes.node.cpu_throttled` | ActiveGate pod |
| Memory working set | Usage consistently exceeds 80%: increase the memory requests. | `builtin:kubernetes.node.memory_working_set`, `builtin:kubernetes.workload.memory_working_set` | ActiveGate pod |
| Memory requests | Usage consistently exceeds 80%: increase the memory requests. | `builtin:kubernetes.node.requests_memory` `builtin:kubernetes.workload.requests_memory` | ActiveGate pod |
| Restart count | After an OOM-based restart, promptly raise the configured memory to prevent recurrence. | `builtin:kubernetes.container.restarts` | ActiveGate pod |
| OOM kills | Any OOM kills: increase memory limits to prevent restart cycles. | `builtin:kubernetes.container.oom_kills` | ActiveGate pod |
| Processing duration | Pipeline execution consistently exceeds 50–60 seconds: increase the CPU request. Also depends on ingested data volume and other factors. | `dsfm:active_gate.kubernetes.pipeline_duration` | ActiveGate ID |
| Garbage collection times | Increasing GC times indicate an under-provisioned ActiveGate. | `dsfm:active_gate.jvm.gc.major_collection_time` | ActiveGate ID |

### Factors that drive an increase in resource consumption

Actual required resources increase with:

* **Number of pods**: The primary sizing driver is the number of monitored pods. The resource consumption (CPU and memory) for Dynatrace ActiveGate components scales with the number of pods primarily due to increased data processing and storage needs. As the number of monitored pods grows, the ActiveGate handles more entity data, events, and metrics, resulting in higher CPU load for ingestion and processing, as well as increased memory for caching pod-related information. This is the primary sizing driver, with consumption scaling proportionally to pod count.
* **Log traffic volume**: For ActiveGates handling log ingestion (via OTLP endpoints or OneAgent log modules), log traffic volume is an important sizing driver. Resource requirements scale with the volume of log data (measured in MB/min), not only the number of pods. A small number of pods with verbose logging can generate more traffic than many pods with minimal logging.
* **Prometheus metrics volume**: The number of Prometheus annotated pods directly correlates with increased resource requirements for Dynatrace ActiveGate, primarily through higher CPU consumption. As the count of annotated pods rises, the volume of scraped metrics grows, demanding more CPU cycles for collection, aggregation, and forwarding tasks. Memory impact is secondary, as metrics are forwarded to the Dynatrace tenant without long-term storage on the ActiveGate, though it scales proportionally with peak ingest rates.
* **Number of nodes**: The resource consumption (CPU and memory) for Dynatrace ActiveGate components scales with the number of nodes primarily due to increased monitoring overhead and load from node-level system pods. As the node count grows, the ActiveGate must handle more system-level data collection, entity processing, and event ingestion, leading to higher computational demands. This is a secondary driver compared to the number of pods, but it contributes proportionally to overall resource needs, especially in larger clusters where node-level monitoring adds cumulative load.

### Scrape Prometheus metrics

Dynatrace supports up to 1,000 pod exporters, with each exporter able to provide up to 1,000 metrics. If your environment approaches these limits, you'll need to increase the resources allocated to the ActiveGate to ensure reliable performance.

For high-volume Prometheus scraping, and for new deployments, we recommend the [OpenTelemetry Collector](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus "Configure the OpenTelemetry Collector to scrape Prometheus endpoints and ingest the data into Dynatrace.").

## Example DynaKube resources

This section provides an example manifest that includes two DynaKube resources that you can use to configure your ActiveGates.

It follows the deployment recommendation to use two sets of ActiveGates: one for Kubernetes Platform Monitoring, and one for OneAgent traffic routing and telemetry ingest.
You can apply one or both manifests according to your deployment.

* The `k8s-monitoring` DynaKube resource handles Kubernetes platform monitoring, and is sized for a medium cluster (1,000–5,000 nodes).
  It includes an optional (commented-out) configuration for Kubernetes Security Posture Management.
* The `agents` DynaKube resource handles OneAgent traffic routing, and is sized for a large cluster (5,000–20,000 nodes).
  It includes an optional (commented-out) configuration for OTLP log ingest, log monitoring, telemetry ingest, and the OTel Collector.

Adjust requests (and limits if required) to fit your environment.

CPU limits are commented out. We recommend defining requests only so the ActiveGate can use additional CPU when available. If limits are required, set them equal to or higher than requests.

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: k8s-monitoring



namespace: dynatrace



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



#otelCollector:



#replicas: 1



#imageRef:



#repository: public.ecr.aws/dynatrace/dynatrace-otel-collector



#tag: <tag>
```