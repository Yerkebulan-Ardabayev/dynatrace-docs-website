---
title: Monitor hosts that send OpenTelemetry data to Dynatrace
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/host-monitoring
---

# Monitor hosts that send OpenTelemetry data to Dynatrace

# Monitor hosts that send OpenTelemetry data to Dynatrace

* How-to guide
* 2-min read
* Updated on Sep 10, 2026

OpenTelemetry Host Monitoring is a Dynatrace feature that transforms raw telemetry data from OTel Collectors into actionable insights.
Rather than simply ingesting metrics, logs, and traces, Dynatrace automatically builds meaningful context around your infrastructure.
It creates host and process entities, establishes topology relationships, and presents data through purpose-built analysis screens.

With the extension, you can:

* Use auto-generated entities (based on extracted metadata) to correlate metrics, logs, and spans and provide unified context across your monitoring environment.

This use case and its reference configuration are designed primarily for VMs and bare-metal hosts with a Linux OS.

* If you want to run host monitoring on Kubernetes nodes, see [Host monitoring on Kubernetes nodes](#kubernetes-considerations) for deployment requirements and limitations.
* If you want to run host monitoring on Windows OS or macOS, remove all references to `journald` from the pipeline–`journald` is only available for Linux OS.

## Prerequisites

This use case assumes that you have:

* One of the following Collector distributions with the [`hostmetrics`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.160.0/receiver/hostmetricsreceiver), [`journald`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.160.0/receiver/journaldreceiver), and [`otlp`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.160.0/receiver/otlpreceiver) receivers, and the [`resource_detection`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.160.0/processor/resourcedetectionprocessor), [`filter`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.160.0/processor/filterprocessor), and [`transform`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.160.0/processor/transformprocessor) processors.

  + The [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [OTel Collector Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + A [custom-built OTel Collector](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* Activated the OpenTelemetry Host Monitoring extension.
  For more information about the extension, see [OpenTelemetry Host Monitoring extension](/managed/observe/infrastructure-observability/extensions/opentelemetry-host-monitoring "Monitor OpenTelemetry-instrumented hosts with auto-generated entity topology, metric visualizations, and alerts for faster infrastructure analysis.").

## Reference configuration

A reference configuration is available in the Dynatrace OTel Collector's GitHub repo, see [`host-metrics.yaml`﻿](https://github.com/Dynatrace/dynatrace-otel-collector/blob/main/config_examples/host-metrics.yaml).

You can use this configuration as-is, or modify it to meet your specific needs.

If your hosts are cloud VMs that are already monitored through [Dynatrace Cloud Monitoring](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed."), add a `transform` processor to this configuration to link the OpenTelemetry host entity to its cloud VM entity.
See [Correlate hosts with their cloud VM entity](#cloud-entity-correlation).

## Components

For our configuration, we configured the following components that are specific to this extension.

### Receivers

Under `receivers`, we specify the following receivers:

* [`hostmetrics`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.160.0/receiver/hostmetricsreceiver)
* [`journald`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.160.0/receiver/journaldreceiver)
* [`otlp`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.160.0/receiver/otlpreceiver)

#### hostmetrics

The [`hostmetrics` receiver﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.160.0/receiver/hostmetricsreceiver) collects host-level metrics.
It is configured with three collection intervals: 10 seconds, 5 minutes, and 1 hour.

* Use short intervals for the most important metrics to ensure that Dynatrace provides fast alerts for important changes.
* Send non-critical metrics less frequently to help control consumption and therefore costs.

#### journald

The [`journald` receiver﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.160.0/receiver/journaldreceiver) collects systemd journal logs from the host and ingests them into the logs pipeline alongside your metrics.
It is configured to read from `/run/log/journal` and applies `move` operators to rename journal fields to OpenTelemetry semantic conventions.

* `body._PID` is renamed to `body.pid`
* `body._EXE` is renamed to `attributes["process.executable.name"]`
* `body.MESSAGE` is renamed to `body.message`

This ensures that host logs are linked to the same process entities as the `hostmetrics` data, enabling correlation between metrics and logs in Dynatrace.

The `journald` receiver is supported on Linux OS only, and requires the `journalctl` binary on the host.
The Collector process must have permission to read the systemd journal.

On Linux hosts, add the user running the Collector to the `systemd-journal` group.

For full details, see [Use journald to ingest systemd journal logs with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/journald "Configure the OpenTelemetry Collector to ingest systemd journal logs from Linux hosts into Dynatrace.").

#### otlp

The [`otlp` receiver﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.160.0/receiver/otlpreceiver) accepts OTLP over gRPC on port `4317` and over HTTP on port `4318`.

In this configuration it is wired into the logs pipeline only, so that application logs sent to the local host Collector are enriched with the host attributes before they are ingested.
Application metrics and spans are not part of this use case.

### Processors

Under `processors`, we specify the following processors.
All of them are required, and the order in which they are listed in a pipeline is significant—see [Service pipelines](#service-pipelines).

* [`resource_detection`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.160.0/processor/resourcedetectionprocessor) detects resource information from the host in a format that conforms to the OpenTelemetry resource semantic conventions, and appends it to the telemetry data.
  This is what adds `host.id`, `host.name`, and the other host attributes that entity extraction depends on.
  Without it, no host or process entity is created.
* [`filter`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.160.0/processor/filterprocessor) is used twice: once to clean up unnecessary metrics dimensions, and secondly to (optionally) filter out unneeded process metrics.
* [`transform`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.160.0/processor/transformprocessor) reshapes the scraped metrics.
  Among other things, it converts `host.ip` from an array to a single value, which the attributes added by `resource_detection` are needed for.
* [`cumulative_to_delta`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.160.0/processor/cumulativetodeltaprocessor) converts the cumulative counters emitted by `hostmetrics` into delta temporality.
  Dynatrace does not ingest cumulative counters, so without this processor every counter metric in this configuration is discarded.

### Exporters

Under `exporters`, we specify the [`otlp_http` exporter﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.160.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`).
* One token variable, depending on the token type you use:

  + **Platform token**: Use `Authorization: Bearer ${env:DT_PLATFORM_TOKEN}` in the exporter headers and assign the `openpipeline:logs:ingest` and `openpipeline:metrics:ingest` scopes.
  + **Classic access token**: Use `Authorization: Api-Token ${env:DT_API_TOKEN}` in the exporter headers and assign the **Ingest logs** (`logs.ingest`) and **Ingest metrics** (`metrics.ingest`) scopes.

### Service pipelines

Under `service`, we assemble the receivers, processors, and exporter into two pipelines.

```
service:



pipelines:



metrics:



receivers: [hostmetrics/10s, hostmetrics/5m, hostmetrics/1h]



processors: [filter, resource_detection, transform, filter/delete-metrics, cumulative_to_delta]



exporters: [otlp_http]



logs:



receivers: [otlp, journald]



processors: [resource_detection]



exporters: [otlp_http]
```

The **metrics** pipeline carries host and process metrics from the three `hostmetrics` receivers.
The **logs** pipeline carries host logs from `journald` and application logs received over OTLP.
There is no traces pipeline.

Processors run in the order in which they are listed, and each step in the metrics pipeline depends on the one before it.

* `filter` runs first, so that the CPU datapoints it discards are gone before `transform` aggregates the remainder.
* `resource_detection` runs before `transform`, because `transform` reads the host attributes that `resource_detection` adds.
* `transform` runs before `filter/delete-metrics`, because it sets the marker attribute that `filter/delete-metrics` selects on.
* `cumulative_to_delta` runs last, once the set of metrics to be exported is final.

Reordering these processors does not produce a configuration error: it produces incorrect or missing data.
So, keep the order as given.

`resource_detection` is what attaches the host attributes, and it only applies to the pipelines that list it.
Telemetry that reaches the Collector through a pipeline without `resource_detection` is exported without host attributes and is not attached to the OpenTelemetry host entity.

## How-to

### Topology

This extension automatically generates topology for infrastructure monitored via the Collector.
Specifically, it creates the entity types based on metadata extracted from metrics, logs, and traces.

| Entity type | Entity ID |
| --- | --- |
| OpenTelemetry host | `dt.entity.otel:host` |
| OpenTelemetry process | `dt.entity.otel:process` |

These entities enable Dynatrace to correlate your metrics, logs, and spans and provide unified context across your monitored environment.

Required attributes for entity extraction

In order for Dynatrace to extract host and process entities, the following resource attributes must be present on your telemetry data.
If you use the reference configuration, these are automatically included by default.
If you use a custom Collector configuration that differs from the reference configuration, make sure these attributes are included.

| Signal | `otel:host` | `otel:process` |
| --- | --- | --- |
| Metrics | * `host.id` * `host.name` * `dt.metrics.source` must be `opentelemetry` | * All resource attributes as in `otel:host` * Additionally, `process.executable.name` |
| Logs | * `host.id` * `host.name` * `dt.openpipeline.source` must be `/api/v2/otlp/v1/logs`   This is automatically set by OpenPipeline; if it is changed or removed, this cause entity extraction to not function properly. | * All resource attributes as in `otel:host` * Additionally, `process.executable.name` |
| Spans | * `host.id` * `host.name` * `telemetry.sdk.name` must be `opentelemetry`, `odin`, or `otel` | * All resource attributes as in `otel:host` * Additionally, `process.executable.name` |

### Enrich application telemetry

If you send your application logs to your local host Collector, the reference configuration enriches them with the required host attributes so that they are correctly attached to the OpenTelemetry host entity.
This applies to logs only; the reference configuration doesn't accept application metrics or spans over OTLP.
If you extend it with additional service pipelines for metrics or spans, add `resource_detection` to those pipelines as well to enrich them with the same host attributes.
See [Service pipelines](#service-pipelines).

To enrich application telemetry with the corresponding process entity, all signals (metrics, logs, and spans) need to have the `process.executable.name` resource attribute.
For logs and spans to have this attribute, you need to initialize your OTel SDK with the [process resource detector﻿](https://opentelemetry.io/docs/languages/go/resources/).

If this is not implemented for your technology's OTel SDK, you can always set the `process.executable.name` attribute through the `OTEL_RESOURCE_ATTRIBUTES` [environment variable﻿](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/#general-sdk-configuration).

### Limit sending of process metrics

By default, all process metrics are sent to Dynatrace.

You can also exclude certain process metrics to control the amount of OTel process entities and improve cardinality.
For example, you might want to filter out insignificant processes that use less than 1 MiB of memory.

To do this, you can filter via the process memory usage or an allow list.

* To filter via process memory usage, use the following `transform` and `filter` processor configurations in your host monitoring configuration YAML.
  Adjust the `datapoint.value_int` value (in bytes) according to your use case.

  If the memory usage of the process fluctuates around the configured limit, metrics could be ingested and dropped intermittently.
  These data gaps would affect cumulative data like counts or sums.

  ```
  transform:



  error_mode: ignore



  metric_statements:



  - set(resource.attributes["low-memory-process"], "true") where metric.name == "process.memory.usage" and datapoint.value_int < 1048576 and resource.attributes["process.executable.name"] != nil



  filter/delete-metrics:



  metric_conditions:



  - resource.attributes["low-memory-process"] != nil
  ```
* To create an allowlist, use the following `transform` and `filter` processors in your host monitoring configuration YAML.
  Adjust the `ContainsValue()` and `resource.attributes[]` variable names according to your use case.

  ```
  transform:



  error_mode: ignore



  metric_statements:



  - delete_key(resource.attributes, "low-memory-process") where ContainsValue(["my-process", "another-process"], resource.attributes["process.executable.name"])



  filter/delete-metrics:



  metric_conditions:



  - resource.attributes["low-memory-process"] != nil
  ```

## Host monitoring on cloud VMs

If a host runs on a cloud VM that Dynatrace monitors through Cloud Monitoring, that VM already exists in Dynatrace as its own entity—an AWS EC2 instance, an Azure virtual machine, or a Google Compute Engine instance.

* By default, the OpenTelemetry host entity created from your Collector data and that cloud VM entity are unrelated, even though they describe the same machine.
* To correlate the OpenTelemetry host entity with its cloud VM entity, configure the Collector to send the cloud provider's resource identifier along with the host metrics. Dynatrace then joins the two and creates a `runs_on` relationship from the OpenTelemetry host to the cloud VM.
  In Smartscape, you can follow this relationship from your OpenTelemetry host and process data to the cloud VM's tags, account, and region.

### Prerequisites

* Cloud Monitoring is enabled in your environment for the account, subscription, or project the host belongs to.
  Cloud VM entities come from Cloud Monitoring only. The Collector cannot create them, and a VM that Dynatrace doesn't monitor can't be correlated.
* The Collector runs on the cloud VM itself, so that the cloud provider's instance metadata service is reachable.

### Add the correlation processor

Add a `transform/dt-cloud-correlation` processor to the metrics pipeline, and add your cloud provider's detector to `resource_detection`.

* The `transform/dt-cloud-correlation` processor composes the identity attribute that Dynatrace joins on.
* The `resource_detection` processor emits the parts the attribute is composed of: the account ID, the region or zone, and the instance name or ID. It doesn't emit the final attribute directly.

The following sections show the detector, the identity attribute, and the statement that composes it for each provider.

#### AWS

Detector: `ec2`. Identity attribute: `aws.arn`.

```
processors:



resource_detection:



detectors: ["ec2", "system"]



transform/dt-cloud-correlation:



error_mode: ignore



metric_statements:



- context: resource



statements:



- set(resource.attributes["aws.arn"], Concat(["arn:aws:ec2:", resource.attributes["cloud.region"], ":", resource.attributes["cloud.account.id"], ":instance/", resource.attributes["host.id"]], "")) where resource.attributes["cloud.provider"] == "aws"
```

#### Azure

Detector: `azure`. Identity attribute: `azure.resource.id`.

```
processors:



resource_detection:



detectors: ["azure", "system"]



transform/dt-cloud-correlation:



error_mode: ignore



metric_statements:



- context: resource



statements:



- set(resource.attributes["azure.resource.id"], ConvertCase(Concat(["/subscriptions/", resource.attributes["cloud.account.id"], "/resourcegroups/", resource.attributes["azure.resourcegroup.name"], "/providers/microsoft.compute/virtualmachines/", resource.attributes["azure.vm.name"]], ""), "lower")) where resource.attributes["cloud.provider"] == "azure" and resource.attributes["azure.vm.scaleset.name"] == nil
```

The lowercase conversion is required. Dynatrace stores the value of `azure.resource.id` fully lowercased, and a mixed-case value doesn't correlate.

The statement skips VMs in a virtual machine scale set, because their resource ID follows a different format.

#### Google Cloud

Detector: `gcp`. Identity attribute: `gcp.resource.name`.

```
processors:



resource_detection:



detectors: ["gcp", "system"]



gcp:



resource_attributes:



gcp.gce.instance.name:



enabled: true



transform/dt-cloud-correlation:



error_mode: ignore



metric_statements:



- context: resource



statements:



- set(resource.attributes["gcp.resource.name"], Concat(["//compute.googleapis.com/projects/", resource.attributes["cloud.account.id"], "/zones/", resource.attributes["cloud.availability_zone"], "/instances/", resource.attributes["gcp.gce.instance.name"]], "")) where resource.attributes["cloud.provider"] == "gcp"
```

The `gcp.gce.instance.name` attribute is disabled by default, so you need to enable it explicitly.

#### Pipeline placement

Add the processor to the metrics pipeline directly after `resource_detection`, which provides the attributes it reads.

```
service:



pipelines:



metrics:



processors: [filter, resource_detection, transform/dt-cloud-correlation, transform, filter/delete-metrics, cumulative_to_delta]
```

List the respective cloud detector (`azure`, `ec2`, or `gcp`) **before** `system` in `resource_detection`.
Detectors are merged first-writer-wins, and both the cloud detector and `system` emit `host.id`.
With `system` first, `host.id` holds the operating system machine ID instead of the cloud instance ID, so the composed identifier is well-formed but matches no cloud VM.
The Collector would not log any error in this case, and no relationship would be created.

## Host monitoring on Kubernetes nodes

The reference configuration and this use case are optimized for VMs and bare-metal hosts.
You can run OTel host monitoring on Kubernetes nodes, but there are additional deployment requirements and important caveats to consider.

### Deployment

To collect host-level metrics from every node in your cluster, deploy the Collector as a **DaemonSet**.
This ensures one Collector pod runs on each node and reports that node's metrics.

The `hostmetrics` receiver works without any additional configuration on Kubernetes.
The same receiver configuration you use on VMs applies to containerized deployments.

### journald on Kubernetes

To collect journald logs on Kubernetes nodes, the Collector must run as root (`runAsUser: 0`) because container isolation prevents group-based journal access.
You also need to mount the journal directory from the host and adjust the `directory` setting to the mounted path.

On Kubernetes, the in-memory journal path is typically `/run/log/journal` rather than the persistent `/var/log/journal` used on VMs.
See [Use journald to ingest systemd journal logs with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/journald "Configure the OpenTelemetry Collector to ingest systemd journal logs from Linux hosts into Dynatrace.") for the full Kubernetes deployment configuration, including the required security context and host volume mounts.

### Metric overlap with Kubernetes monitoring

If you run both OTel host monitoring and [Kubernetes cluster monitoring](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-monitoring "Configure the OpenTelemetry Collector to monitor your Kubernetes clusters.") on the same nodes, be aware that some metrics overlap: the same measurements may be ingested as two separate metric keys.
This is because they have different metric names that follow different semantic conventions, so Dynatrace ingests them as separate metric keys.

The following table shows common overlapping metrics:

| `hostmetrics` receiver | `kubelet_stats` receiver | What they measure |
| --- | --- | --- |
| `system.cpu.*` | `k8s.node.cpu.*` | Node CPU usage |
| `system.memory.*` | `k8s.node.memory.*` | Node memory usage |
| `system.filesystem.*` | `k8s.node.filesystem.*` | Node filesystem usage |
| `system.network.*` | `k8s.node.network.*` | Node network I/O |

This overlapp occurs because the Kubernetes monitoring use case uses the [`kubelet_stats` receiver﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.160.0/receiver/kubeletstatsreceiver), which reports node-level resource metrics that represent the same underlying data as the `hostmetrics` receiver.

To avoid unnecessary duplication on Kubernetes, use only Kubernetes monitoring or only OTel host monitoring, if possible:

* Use Kubernetes monitoring only if you don't require process-level detail and host entity topology.
  [Kubernetes cluster monitoring](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-monitoring "Configure the OpenTelemetry Collector to monitor your Kubernetes clusters.") provides node-level metrics through the `kubelet_stats` receiver. Adding `hostmetrics` on top duplicates the node-level resource metrics.
* Use host monitoring only if you don't require Kubernetes-specific object metrics such as pods and deployments.
  OTel host monitoring provides host and process entities with topology in Dynatrace.
* If you require both use cases, use the `filter` processor to drop overlapping node-level metrics from one of the two pipelines.
  For example, filter out `system.cpu.*`, `system.memory.*`, `system.filesystem.*`, and `system.network.*` from the host monitoring pipeline if the Kubernetes monitoring pipeline already covers them.

## Limitations

* The `system.processes.created` metric is only available on Linux.
* The `process.disk.io` metric requires running the Collector with privileged access.
  Without privileged access, the metric is not captured.
* The `journald` receiver is only supported on Linux. Attempting to use the `journald` receiver on a different operating system will cause the Collector to return an error and exit on startup.