---
title: Scrape Prometheus metrics with the OTel Collector (standard)
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/prometheus/standard
---

# Scrape Prometheus metrics with the OTel Collector (standard)

# Scrape Prometheus metrics with the OTel Collector (standard)

* How-to guide
* 12-min read
* Published Jun 23, 2026

Use this page to scrape and process Prometheus endpoints with the standard, production-grade deployment.
This setup uses architecture with the [Target Allocator﻿](https://github.com/Dynatrace/otel-target-allocator) and separate Collector pools for scraping and processing.
It is the recommended approach for most production deployments, and is built for Kubernetes clusters that need auto-scaling, redundancy, and high-volume Prometheus workloads.

## When to use this approach

Use this architecture when one or more of the following scenarios apply.

* The workload exceeds what a single Collector or a small set of duplicated Collectors can handle.
* You scrape thousands of pods, or hundreds of distinct endpoints.
* Total ingest is in the millions of data points per minute.
* You want horizontal scaling across the scraper and gateway pools instead of manually partitioning targets.

If you scrape a small or static set of endpoints and don't need auto-scaling or redundancy, you can use the simplified deployment with a single Collector instead.
For more information, see [Scrape Prometheus metrics with the OTel Collector (simplified)](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus/simplified "Configure a single OpenTelemetry Collector to scrape Prometheus endpoints for small and medium-scale workloads.").

## Prerequisites

This use case assumes that you have:

You don't need to install everything below up front. The [Deploy the tiered architecture](#deploy-the-tiered-architecture) walkthrough installs the CRDs, Target Allocator, and both Collector tiers step by step. Treat this list as a reference for what the deployment needs—only the Kubernetes cluster and Dynatrace API access are true prerequisites.

* A Kubernetes cluster with the Prometheus Operator Custom Resource Definitions (CRDs)—`ServiceMonitor`, `PodMonitor`, and `ScrapeConfig`—installed. You need only these CRDs, not the full [Prometheus Operator﻿](https://prometheus-operator.dev/docs/getting-started/installation/). [Step 1](#deploy-the-tiered-architecture) of the walkthrough installs the CRD-only bundle.
* One of the following Collector distributions for the scraper tier, with the [`prometheus` receiver﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.155.0/receiver/prometheusreceiver) and the [`loadbalancing` exporter﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.155.0/exporter/loadbalancingexporter):

  + The [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [OTel Collector Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + A [custom-built OTel Collector](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* One of the following Collector distributions for the gateway tier, with the [`metric_start_time`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.155.0/processor/metricstarttimeprocessor), [`cumulativetodelta`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.155.0/processor/cumulativetodeltaprocessor), [`k8sattributes`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.155.0/processor/k8sattributesprocessor), and [`transform`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.155.0/processor/transformprocessor) processors and the [`otlphttp` exporter﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.155.0/exporter/otlphttpexporter):

  + The [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [OTel Collector Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + A [custom-built OTel Collector](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* One of the following Target Allocator distributions deployed via the upstream `opentelemetry-target-allocator` Helm chart:

  + The [Dynatrace Target Allocator﻿](https://github.com/Dynatrace/otel-target-allocator)
  + The [upstream OpenTelemetry Target Allocator﻿](https://opentelemetry.io/docs/platforms/kubernetes/operator/target-allocator/)
* The [Dynatrace API endpoint URL](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported.
* An [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope (only required for SaaS and ActiveGate).

## Architecture overview

![Architecture overview of the standard OTel Prometheus scraping scenario](https://dt-cdn.net/images/prometheus-large-scale-arch-40e1b468cb.svg)

Architecture overview of the standard OTel Prometheus scraping scenario

This setup has the following components:

* Target Allocator: The Target Allocator (TA) discovers Prometheus targets via a `ServiceMonitor`, `PodMonitor`, or `ScrapeConfig` Custom Resource Definition (CRD) and distributes them across the scraper pool using consistent hashing.

  The hashing algorithm is deterministic, so every replica produces the same target-to-scraper assignment independently. Run multiple replicas for failure tolerance.
* Scrapers: Deployment of Collectors. Each scraper polls the TA, scrapes its assigned Prometheus targets, and forwards data to the gateway pool through the `loadbalancing` exporter.

  The `loadbalancing` exporter routes by resource hash, so all data from a given source pod consistently lands on the same gateway, which keeps per-series state consistent.
* Gateways: StatefulSet of Collectors. Receives OTLP from the scrapers, runs the stateful `metric_start_time` and `cumulativetodelta` processors, applies Kubernetes enrichment via `k8sattributes` and `transform`, and exports to Dynatrace.

  The `metric_start_time` and `cumulativetodelta` processors are stateful and must see every consecutive sample of a series in one place to compute deltas correctly. They run on the gateway tier rather than the scrapers because the `loadbalancing` exporter consistently routes all data from a given source to the same gateway, so each series' full sample stream converges there even as the scraper pool autoscales.
  Running gateways as a StatefulSet gives each replica a stable identity and ordered rollout, which keeps the gateway pool's endpoint set predictable during scale events.

## Reference configuration

A reference configuration is available in the Dynatrace OTel Collector's GitHub repo, see
[`config_examples/prometheus-large-scale/`﻿](https://github.com/Dynatrace/dynatrace-otel-collector/tree/main/config_examples/prometheus-large-scale).

The set includes the following YAML files.

* `allocator.values.yaml`: Helm values for the TA
* `tier1-scraper.values.yaml`: Helm values for the scraper Deployment
* `tier2-gateway.values.yaml`: Helm values for the gateway StatefulSet
* `rbac.yaml`: ServiceAccounts, ClusterRoles, and bindings for all tiers
* `scrapeconfig.yaml`: example `ScrapeConfig` CRD for annotation-based discovery
* `selfmon-scraper.yaml`: Helm values for a dedicated self-monitoring Collector that collects self-monitoring metrics from all tiers and exports them directly to Dynatrace, independent of the main pipeline

Apply the values as-is or adapt them to your cluster, see [Customize the configuration](#customize-configuration).

## Deploy the tiered architecture

The walkthrough below references the Helm charts and manifests linked from the reference configuration.

This walkthrough uses Helm values, but it isn't the only option.
You can also deploy both Collector tiers and the Target Allocator through the [OpenTelemetry Operator﻿](https://github.com/open-telemetry/opentelemetry-operator) using its `OpenTelemetryCollector` and `TargetAllocator` custom resources.
Either route requires the same RBAC.

1. Install the Prometheus Operator CRDs (`ServiceMonitor`, `PodMonitor`, `ScrapeConfig`) so the TA can discover targets.

   ```
   kubectl apply -f https://github.com/prometheus-operator/prometheus-operator/releases/download/v0.91.0/stripped-down-crds.yaml
   ```
2. Apply RBAC for the TA and Collector ServiceAccounts.

   ```
   kubectl apply -f rbac.yaml
   ```
3. Deploy the TA with the upstream `opentelemetry-target-allocator` Helm chart and the provided values. Run multiple replicas for failure tolerance if needed.

   ```
   helm install otel-allocator open-telemetry/opentelemetry-target-allocator \



   --values allocator.values.yaml
   ```
4. Apply `ServiceMonitor` and `PodMonitor` CRDs for the workloads you want to scrape. Optionally, apply a `ScrapeConfig` for annotation-based discovery. For examples of each, see [Configure the Target Allocator](#configure-the-target-allocator). If you're moving from a single Collector, see [Migrate from a single Collector](#migrate).
5. Deploy the gateway pool before the scrapers so the `loadbalancing` exporter has destinations available on first start.

   ```
   helm install otel-gateway open-telemetry/opentelemetry-collector \



   --values tier2-gateway.values.yaml
   ```
6. Deploy the scraper pool.

   ```
   helm install otel-scraper open-telemetry/opentelemetry-collector \



   --values tier1-scraper.values.yaml
   ```

## Configure the Target Allocator

The TA discovers Prometheus scrape targets from `ServiceMonitor`, `PodMonitor`, and `ScrapeConfig` CRDs and distributes them across the scraper pool using consistent hashing. It maintains a single authoritative view of which scraper is responsible for which target.

Configure which CRDs the TA watches by setting label selectors in the Helm values. The reference configuration uses the `prometheus.dynatrace.com: "true"` label:

```
prometheus_cr:



enabled: true



scrapeInterval: 15s



service_monitor_selector:



matchlabels:



prometheus.dynatrace.com: "true"



pod_monitor_selector:



matchlabels:



prometheus.dynatrace.com: "true"



scrape_config_selector:



matchlabels:



prometheus.dynatrace.com: "true"
```

### Migrate from a single Collector

If you're coming from the [simplified deployment](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus/simplified "Configure a single OpenTelemetry Collector to scrape Prometheus endpoints for small and medium-scale workloads."), your targets are defined as static `scrape_configs` on the Prometheus receiver. The Target Allocator discovers targets through CRDs instead, so convert each scrape job into a `ServiceMonitor` (recommended) or `PodMonitor`.

For the quickest path off `scrape_configs` with minimal changes, wrap your existing static targets in a `ScrapeConfig` CRD instead (see [ScrapeConfig](#scrapeconfig)). This keeps the static target list, so it doesn't benefit from label-based service discovery. In the long term, we recommend to convert to `ServiceMonitor` or `PodMonitor`.

The following example shows how to convert a single static job into an equivalent `ServiceMonitor`.

* Before, on the single Collector:

  ```
  receivers:



  prometheus:



  config:



  scrape_configs:



  - job_name: my-app



  scrape_interval: 60s



  metrics_path: /metrics



  static_configs:



  - targets: ['my-app.my-namespace.svc:8080']
  ```
* After, as a `ServiceMonitor` (see [ServiceMonitor](#servicemonitor) for the full schema):

  ```
  apiVersion: monitoring.coreos.com/v1



  kind: ServiceMonitor



  metadata:



  name: my-app



  labels:



  prometheus.dynatrace.com: "true"



  spec:



  selector:



  matchLabels:



  app: my-app



  endpoints:



  - port: metrics



  interval: 60s



  path: /metrics
  ```

The `metric_start_time`, `cumulativetodelta`, and `otlp_http` configuration from your single Collector moves to the gateway pool unchanged. Only target discovery changes form.

### ServiceMonitor

`ServiceMonitor` selects Kubernetes Services by label. The TA discovers the endpoints behind each Service and allocates them to scrapers.

Add the `prometheus.dynatrace.com: "true"` label to your `ServiceMonitor`:

```
apiVersion: monitoring.coreos.com/v1



kind: ServiceMonitor



metadata:



name: my-service



labels:



prometheus.dynatrace.com: "true"



spec:



selector:



matchLabels:



app: my-service



endpoints:



- port: metrics



interval: 60s
```

### PodMonitor

`PodMonitor` selects pods directly by label, bypassing the Service abstraction. Use it when pods expose metrics but are not fronted by a Service.

```
apiVersion: monitoring.coreos.com/v1



kind: PodMonitor



metadata:



name: my-pods



labels:



prometheus.dynatrace.com: "true"



spec:



selector:



matchLabels:



app: my-app



podMetricsEndpoints:



- port: metrics



interval: 60s
```

### ScrapeConfig

`ScrapeConfig` exposes native Prometheus scrape configuration. It is useful as a migration path for setups that already use `metrics.dynatrace.com/scrape` pod annotations from the ActiveGate Kubernetes module.

The following `ScrapeConfig` discovers all pods in the cluster and keeps only those with the `metrics.dynatrace.com/scrape: "true"` annotation. It reads the `port`, `path`, and `secure` annotations to build the scrape target. To limit the TA's memory footprint, scope the `kubernetesSDConfigs` to specific namespaces instead of cluster-wide discovery.

```
apiVersion: monitoring.coreos.com/v1alpha1



kind: ScrapeConfig



metadata:



name: dynatrace-annotations



labels:



prometheus.dynatrace.com: "true"



spec:



jobName: dynatrace-annotations



scrapeInterval: 60s



kubernetesSDConfigs:



- role: Pod



relabelings:



- sourceLabels:



- __meta_kubernetes_pod_annotation_metrics_dynatrace_com_scrape



- __meta_kubernetes_pod_annotationpresent_metrics_dynatrace_com_scrape



action: keep



regex: true;true



- sourceLabels:



- __meta_kubernetes_pod_annotation_metrics_dynatrace_com_secure



- __meta_kubernetes_pod_annotationpresent_metrics_dynatrace_com_secure



action: replace



regex: true;true



targetLabel: __scheme__



replacement: https



- sourceLabels:



- __address__



- __meta_kubernetes_pod_annotation_metrics_dynatrace_com_port



- __meta_kubernetes_pod_annotationpresent_metrics_dynatrace_com_port



action: replace



regex: (.+?)(?::\d+)?;(\d+);true



targetLabel: __address__



replacement: $1:$2



- sourceLabels:



- __meta_kubernetes_pod_annotation_metrics_dynatrace_com_path



- __meta_kubernetes_pod_annotationpresent_metrics_dynatrace_com_path



action: replace



regex: (.+);true



targetLabel: __metrics_path__



replacement: $1



- sourceLabels:



- __meta_kubernetes_pod_phase



action: drop



regex: (Failed|Succeeded)
```

This approach requires no application-side changes. For new workloads, prefer `ServiceMonitor` or `PodMonitor` for a standard Prometheus Operator setup.

### Scale the Target Allocator

The TA holds all Prometheus service discovery metadata (pod labels, annotations, node information) in memory. On large clusters this can consume multiple gigabytes.

Run multiple TA replicas for failure tolerance. Because the consistent-hashing algorithm is deterministic, all replicas independently produce the same target-to-scraper assignments without coordination.

When memory becomes a bottleneck, you can:

* Scale vertically. Increase the TA's memory limit in the Helm values. Optionally use a [Vertical Pod Autoscaler﻿](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler) to automate this.
* Reduce your discovery scope. Tighten relabeling rules in `ScrapeConfig` CRDs or scope `kubernetesSDConfigs` to specific namespaces to limit the amount of metadata the TA holds.
* Use sharded TAs. Run multiple independent TA instances, each watching a distinct subset of namespaces. Each shard requires its own dedicated scraper pool because a scraper can only poll a single TA endpoint. Downstream gateway Collectors can be shared across shards.

## Customize the configuration

The reference configuration is a starting point. Adjust the following settings to match your workload.

### `cumulativetodelta` staleness

The `cumulativetodelta` processor converts Prometheus counters to delta metrics by tracking the previous value of each series in memory. `max_staleness` controls how long the processor keeps per-series state after the last observed data point. Once that window expires without an update, the processor drops the series from the cache. The next sample for that series is treated as a fresh starting point, so one delta is lost.

Set `cumulativetodelta.max_staleness` on the gateway to roughly 10 times the Prometheus receiver `scrape_interval`. The factor of 10 covers occasional missed scrapes (target restarts, network blips, slow endpoints) without keeping state for series that are genuinely gone.

Higher values keep state for inactive series longer, so gateway memory can grow without bound as series churn over time (pod restarts, autoscaled workloads, label changes). Lower values evict still-active series between scrapes, which creates visible gaps and resets the running delta for each affected series.

### Horizontal pod autoscaling

The scraper Deployment and the gateway StatefulSet support Kubernetes [Horizontal Pod Autoscalers﻿](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) (HPAs). The reference configuration includes HPA settings for both tiers. For the full configuration, see the following YAML files in the Dynatrace Collector GitHub repo.

* [`tier1-scraper.values.yaml`﻿](https://github.com/Dynatrace/dynatrace-otel-collector/blob/main/config_examples/prometheus-large-scale/tier1-scraper.values.yaml)
* [`tier2-gateway.values.yaml`﻿](https://github.com/Dynatrace/dynatrace-otel-collector/blob/main/config_examples/prometheus-large-scale/tier2-gateway.values.yaml)

Both tiers use the same target utilization percentages: when either 50% memory or 70% CPU are reached, the HPA will scale out, and start to add pods automatically. Adjust `minReplicas` and `maxReplicas` based on your expected load range. Memory is typically the dominant constraint for scrapers because the Prometheus receiver buffers scraped data in memory. Gateways consume both CPU and memory, and the stateful `cumulativetodelta` processor memory usage grows proportionally with the number of tracked series.

#### Target Allocator behavior during scaling

The Target Allocator detects Collector pod changes automatically. When the HPA adds or removes scraper pods, the Target Allocator redistributes targets across the updated pool. Consistent hashing minimizes reshuffling: Most targets stay on the same scraper, and only a fraction moves to the new or remaining pods.

#### Stabilization window tuning

Prometheus scrapes cause periodic CPU and memory spikes. Without a scale-down stabilization window, these spikes can trigger premature scale-down after temporary dips between scrapes. Set the HPA stabilization windows relative to the Prometheus `scrape_interval`.

* Scale up is controlled by `stabilizationWindowSeconds`. Set `stabilizationWindowSeconds: 0` (the Kubernetes default) to ensure the HPA scales up immediately when utilization exceeds the target, which lets the fleet absorb load increases without delay.
* Scale down is controlled by `stabilizationWindowSeconds`. Set `stabilizationWindowSeconds: <scrape_interval * 5>` to ensure the HPA only scales down after the load has stabilized.

The YAML below shows an appropriate configuration for a 60-second scrape interval.

```
behavior:



scaleUp:



stabilizationWindowSeconds: 0



scaleDown:



stabilizationWindowSeconds: 300
```

The immediate scale-up ensures the fleet reacts quickly to sustained load increases. The longer scale-down window prevents premature scale-down during temporary dips between scrapes.

## Resource sizing reference

The following table shows approximate replica counts at different load levels, measured in data points per minute (DPM) with a 60-second scrape interval. Use these counts as a ballpark for initial sizing. Actual replica counts depend on the number of series per target, label cardinality, and processor configuration.

The reference configuration uses the following resource limits per pod.

* Scraper: 1 CPU, 6 GiB memory
* Gateway: 2 CPUs, 8 GiB memory

These limits include headroom above typical steady-state usage. The Prometheus receiver buffers entire scrape responses in memory before processing, which causes sharp spikes at each scrape cycle. Scrapers are memory-bound because of this buffering behavior, so the scraper resource limit absorbs those periodic spikes without out-of-memory (OOM) kills. Gateways need headroom for the `cumulativetodelta` processor, which grows memory proportionally to the number of tracked series, and CPU usage scales with the volume of incoming data. The gateway resource limit accounts for both steady-state tracking and burst processing when multiple scrapers flush data simultaneously.

| Load | Scrape targets | Scraper replicas | Gateway replicas |
| --- | --- | --- | --- |
| 1M DPM | 5 | 2 | 2 |
| 5M DPM | 30 | 6 | 2 |
| 10M DPM | 60 | 13 | 4 |
| 30M DPM | 334 | 38 | 8 |
| 60M DPM | 667 | 74 | 18 |
| 90M DPM | 1,000 | 102 | 23 |

Set your resource requests and HPA `minReplicas` to handle your baseline load, and let the HPA scale up from there. Different resource limits per pod change the replica counts.

For general information about scaling the Collector, see [Scale OpenTelemetry Collector deployments](/managed/ingest-from/opentelemetry/collector/scaling "How to scale the OpenTelemetry Collector.").

### Custom sizing and vertical scaling

If you would like to tune the resource allocation of your Collector pods to fit your particular use-case, we suggest starting with the following limits for each tier, assuming one instance in each tier, per 1 million data points per minute (DPM):

* Scraper Collectors: 1 core CPU, 6 GiB memory
* Gateway Collectors: 500 millicores CPU, 2 GiB memory

While a single pod in each tier should be sufficient for this level of load, it is still suggested to run at least one extra Collector for redundancy to prevent data loss.

Resource requirements scale linearly with load in this setup, so multiples of these limits can also be used as a guidepost to determine the right sizing for your situation.

Vertical scaling will be required when handling particularly large targets, which can not be split amongst multiple scrapers. See the section on [troubleshooting hotspots](#hotspots-from-uneven-load) for more information on how to identify when you may be encountering this situation.

### Modifying resource allocation for the Target Allocator

The Target Allocator is very efficient at even high loads. Since it does not process data itself, it does not scale with the rate of metric ingestion but rather with the number of pods exposing Prometheus metrics. It operates as a singleton and (in most cases) will not need to be tuned.

The following table shows suggested Target Allocator resource limits that can be used to help guide appropriate sizing for your cluster. Note that the resource requirements do not scale linearly with scraper target count; they grow relatively slowly.

| Scrape targets | CPU limit | Memory limit |
| --- | --- | --- |
| 200 | 10m | 256 MiB |
| 5000 | 100m | 512 MiB |
| 20000 | 1 (1000m) | 1 GiB |

## Limitations of hash-based load distribution

The Target Allocator and the `loadbalancing` exporter distribute work by hash, not by actual resource consumption. The HPA scales the fleet based on average utilization, but neither component rebalances work toward instances with less load.

* Scraper tier: The Target Allocator assigns targets to scrapers by hashing the target identity; it does not consider how many series each target produces. A target with 500,000 series and a target with 100 series are handled the same. The `loadbalancing` exporter on the scraper then routes data to gateways by hashing the resource identity, which pins all data from a given source pod to a single gateway.
* Gateway tier: A gateway that receives data from a heavy source pod carries more load than its peers, regardless of how many gateway replicas the HPA adds.
* A single target must fit into one pod. The Target Allocator assigns each target to exactly one scraper, and that scraper buffers the entire scrape response in memory. The pod's resource limits are the hard ceiling for any individual target. The HPA can add more pods to the fleet, but it cannot split a single target across multiple pods. If one target produces more data than a single pod can handle, adding replicas does not help.
* Adding replicas does not move existing assignments. The HPA can grow or shrink the fleet, but a heavy target stays on the same scraper and its data stays pinned to the same gateway.

To mitigate these behaviors, you can:

* Separate heavy workloads into distinct scrape targets. If an application can expose metrics on multiple ports or paths, each one becomes a separate target that the Target Allocator can assign to a different scraper. Similarly, use separate `ServiceMonitor` or `ScrapeConfig` CRDs with narrow label selectors to ensure heavy pods are seen as individual targets rather than grouped together.
* Scale vertically for the heaviest target. Set per-pod resource limits high enough to handle the single largest target that any one scraper might receive. Since the HPA cannot split a target across pods, the per-pod limits determine the maximum target size the architecture can support.
* Accept the imbalance. When only a few targets are heavy and splitting is impractical, slightly over-provision resources across the pool.

## Verify the deployment

After you deploy all tiers, verify that data flows from the scraped targets through the Collector pipeline into Dynatrace.

### Check self-monitoring metrics

Self-monitoring is enabled by default on all Collectors. Confirm that the key metrics report healthy values on every Collector in the architecture. For setup instructions , see [Enable OpenTelemetry Collector self-monitoring](/managed/ingest-from/opentelemetry/collector/self-monitoring "How to monitor OpenTelemetry Collectors with self-monitoring features.").

Set self-monitoring `level: detailed` so that all metrics listed below are available. The reference configuration already includes a self-monitoring telemetry exporter in each tier's Helm values.

Check the following metrics on each tier.

#### Scraper tier

| Metric | What to look for |
| --- | --- |
| `otelcol_receiver_accepted_metric_points` | Increases after every scrape cycle. If it stays constant or at zero, the Prometheus receiver is not scraping any targets. |
| `otelcol_processor_incoming_items` / `otelcol_processor_outgoing_items` | Incoming and outgoing counts should be equal. A gap between them indicates a processor is dropping data (for example, `memory_limiter` kicking in). |
| `otelcol_exporter_send_failed_metric_points` | Should be zero or near zero. Non-zero values mean the `loadbalancing` exporter cannot reach the gateway pool. |
| `otelcol_loadbalancer_num_resolutions` | Increments each time the exporter re-resolves the gateway DNS. Frequent spikes during steady state indicate DNS instability or gateway pod churn. |

#### Gateway tier

| Metric | What to look for |
| --- | --- |
| `otelcol_receiver_accepted_metric_points` | Should match the total sent by all scrapers. A significant mismatch means data is lost between the tiers. |
| `otelcol_processor_incoming_items` / `otelcol_processor_outgoing_items` | Incoming and outgoing counts should be equal. A gap indicates a processor (typically `memory_limiter`) is dropping data on the gateway. |
| `otelcol_exporter_sent_metric_points` | Increases steadily. If it falls behind the receiver count, check exporter errors and queue size. |

### Inspect Target Allocator assignments

Query the Target Allocator HTTP API to confirm that it discovered your targets and distributed them across the scraper pool.

1. Port-forward to the Target Allocator pod.

   ```
   kubectl port-forward svc/otel-allocator 8080:80
   ```
2. List all discovered scrape jobs.

   ```
   curl -s http://localhost:8080/jobs | jq .
   ```
3. List targets and their assigned Collector for a specific job. Replace `<job-name>` with a job name from the previous step.

   ```
   curl -s http://localhost:8080/jobs/<job-name>/targets | jq .
   ```

The response groups targets by Collector ID. Each key is a collector and its value contains the targets assigned to that collector. Verify that:

* All expected targets appear in the response.
* Targets are distributed across multiple Collector IDs (not all assigned to one scraper).
* No targets are listed as unassigned.

For a visual overview of target-to-Collector assignments, use the [`ta-visualize.py`﻿](https://bitbucket.lab.dynatrace.org/users/bernhard.aichinger/repos/k8s-monitoring/browse/phase-2-tiered/ta-visualize.py) script. It queries the Target Allocator API and renders a human-readable mapping of which targets are assigned to which scraper.

## Troubleshoot common issues

### Missing metrics

If expected metrics do not appear in Dynatrace, check the following causes.

* **Label selector mismatch in CRDs**: The Target Allocator discovers targets through `ServiceMonitor`, `PodMonitor`, or `ScrapeConfig` CRDs. If the labels on the target workload do not match, the Target Allocator never discovers it. Use `kubectl get servicemonitor -o yaml` and compare the `matchLabels` against the actual labels on the target Service or Pod.
* **RBAC missing for the Target Allocator**: The Target Allocator ServiceAccount needs `get`, `list`, and `watch` permissions on `ServiceMonitor`, `PodMonitor`, `ScrapeConfig`, Pods, Services, Endpoints, and Nodes. Missing permissions cause silent discovery failures. Check the Target Allocator logs for permission errors.
* **Target unreachable from scraper pods**: The scraper must be able to reach the target's metrics endpoint over the network. Verify that no `NetworkPolicy` blocks traffic from the scraper namespace to the target namespace, and that the target port is correct.
* **Service or Pod selector does not match any workload**: A `ServiceMonitor` can reference a Service that has no matching Endpoints, or a `PodMonitor` can have a `selector` that matches zero Pods. Use `kubectl get endpoints <service-name>` to verify that the Service has active endpoints.

### Data duplication

If you see duplicate metric values in Dynatrace, check for these scenarios.

* **Multiple scrapers with the same `collector_id`**: Each scraper must register with the Target Allocator under a unique Collector ID. If two scrapers share the same ID, both receive the same target assignments and scrape the same endpoints. The reference configuration sets `collector_id: ${K8S_POD_NAME}` in the Prometheus receiver's `target_allocator` block, which ensures each pod registers with its own name. Use the steps in [Inspect Target Allocator assignments](#inspect-target-allocator-assignments) to check which Collector IDs appear and whether the same targets are assigned to multiple scrapers.
* **Collectors outside the Target Allocator's `collector_selector`**: If you run additional Collectors that scrape Prometheus endpoints independently (not managed by the Target Allocator), they may overlap with the Target Allocator-managed scrapers. Ensure that only Target Allocator-managed scrapers scrape the targets assigned by the Target Allocator.

### Target Allocator not distributing targets

If the `/targets` API returns no entries or all targets are assigned to one scraper, check the following.

* **CRDs not picked up**: The Target Allocator watches for `ServiceMonitor`, `PodMonitor`, and `ScrapeConfig` resources. If these CRDs are in a namespace that the Target Allocator is not configured to watch, they are ignored. Check the Target Allocator's `prometheus_cr` configuration: the `service_monitor_selector`, `pod_monitor_selector`, and `scrape_config_selector` fields filter which CRDs the Target Allocator picks up by label.
* **Target Allocator pod not running**: Use `kubectl get pods` to confirm the Target Allocator pod is running and ready. Check its logs for errors.
* **`collector_selector` missing or incorrect**: The Target Allocator uses `collector_selector` to discover which Collector pods to distribute targets to. If this selector does not match the scraper pods' labels, the Target Allocator has no pool to distribute to. Verify that the label selector in the Target Allocator's `collector_selector` matches the labels on the scraper Deployment's pod template.

### Hotspots from uneven load

If some scraper or gateway pods show significantly higher resource utilization than their peers, the hash-based distribution is causing an imbalance. See [Limitations of hash-based load distribution](#limitations-of-hash-based-load-distribution) for an explanation of why this happens.

Signs of imbalance in self-monitoring metrics:

* One scraper shows a much higher `otelcol_receiver_accepted_metric_points` rate than the others.
* One gateway shows higher memory or CPU usage than the others, visible in the `otelcol_process_memory_rss` or `otelcol_process_cpu_seconds` metrics.

To mitigate hotspots, scale vertically by increasing per-pod resource limits for the tier that is overloaded.

### OOM kills on scrapers or gateways

If scraper or gateway pods are killed with `OOMKilled` status, the pod's memory limit is too low for the workload.

* **Scraper OOM kills**: The Prometheus receiver buffers the entire scrape response in memory. A single target that exposes a large number of series can cause a memory spike that exceeds the pod's limit. Increase the scraper pod's memory limit, or reduce the number of series per target by splitting heavy targets.
* **Gateway OOM kills**: The `cumulativetodelta` processor tracks per-series state in memory. High series cardinality or a long `max_staleness` value grows memory usage over time. Reduce `max_staleness` to evict stale series sooner, or increase the gateway pod's memory limit.
* **`memory_limiter` processor**: If configured, the `memory_limiter` processor drops data before the pod reaches its memory limit. Compare `otelcol_processor_incoming_items` and `otelcol_processor_outgoing_items` on the affected tier. A gap between them means the `memory_limiter` is dropping data. If it triggers frequently, the pod is under-provisioned for the workload.

### Load-balancing exporter routing issues

The `loadbalancing` exporter on the scraper tier routes data to gateways by hashing a key derived from the OTLP data.

* **`routing_key: resource` vs. `routing_key: streamID`**: The `resource` routing key (the default) hashes all resource attributes, so all metrics from a given source pod land on the same gateway. This is efficient because the exporter computes one hash per resource, but it can create hotspots when a single source pod emits many series. The `streamID` routing key hashes the full stream identity (resource, scope, metric name, and datapoint attributes), which distributes individual metric streams across gateways for a more even load. The `cumulativetodelta` processor still works correctly with `streamID` because each unique stream is consistently routed to the same gateway. However, `streamID` computes a hash for every individual datapoint stream rather than once per resource, which significantly increases CPU usage on the scraper tier. The `cumulativetodelta` processor on the gateway tier tracks state by stream identity regardless of the routing key, so the total memory usage across all gateways stays the same. Only the distribution of that state across gateways changes.
* **Resolver cache freshness during pod churn**: The `loadbalancing` exporter uses the `k8s` resolver to discover gateway pod IPs by watching Kubernetes `EndpointSlice` objects. The watch API reacts faster than DNS polling, but there is still a brief window during gateway pod restarts or scaling events where the resolver's view does not match the actual topology. During this window, the exporter may route data to a pod that is terminating or miss a newly started pod, which causes send failures. Monitor `otelcol_loadbalancer_num_resolutions` and `otelcol_exporter_send_failed_metric_points` during scaling events. The `k8s` resolver requires the Collector's ServiceAccount to have `get`, `list`, and `watch` permissions on `discovery.k8s.io/v1` `EndpointSlice` objects in the gateway namespace; without these permissions, the resolver cache stays empty and the exporter cannot route to any backend.

## Related topics

* [Scrape Prometheus metrics with the OTel Collector (simplified)](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus/simplified "Configure a single OpenTelemetry Collector to scrape Prometheus endpoints for small and medium-scale workloads.")