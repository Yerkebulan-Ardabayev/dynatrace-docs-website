---
title: Monitor hosts that send OpenTelemetry data to Dynatrace
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/host-monitoring
---

# Monitor hosts that send OpenTelemetry data to Dynatrace

# Monitor hosts that send OpenTelemetry data to Dynatrace

* How-to guide
* 2-min read
* Updated on Apr 01, 2026

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

* One of the following Collector distributions with the [`hostmetrics`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/hostmetricsreceiver) and [`journald`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/journaldreceiver) receivers, and the [`resource_detection`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/resourcedetectionprocessor), [`filter`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/filterprocessor), and [`transform`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/transformprocessor) processors.

  + The [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [OTel Collector Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + A [custom-built OTel Collector](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* Activated the OpenTelemetry Host Monitoring extension.
  For more information about the extension, see [OpenTelemetry Host Monitoring extension](/managed/observe/infrastructure-observability/extensions/opentelemetry-host-monitoring "Monitor OpenTelemetry-instrumented hosts with auto-generated entity topology, metric visualizations, and alerts for faster infrastructure analysis.").

## Reference configuration

A reference configuration is available in the Dynatrace OTel Collector's GitHub repo, see [`host-metrics.yaml`﻿](https://github.com/Dynatrace/dynatrace-otel-collector/blob/main/config_examples/host-metrics.yaml).

You can use this configuration as-is, or modify it to meet your specific needs.

## Components

For our configuration, we configured the following components that are specific to this extension.

### Receivers

Under `receivers`, we specify the following receivers:

* [`hostmetrics`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/hostmetricsreceiver)
* [`journald`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/journaldreceiver)

#### hostmetrics

The [`hostmetrics` receiver﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/hostmetricsreceiver) collects host-level metrics.
It is configured with three collection intervals: 10 seconds, 5 minutes, and 1 hour.

* Use short intervals for the most important metrics to ensure that Dynatrace provides fast alerts for important changes.
* Send non-critical metrics less frequently to help control consumption and therefore costs.

#### journald

The [`journald` receiver﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/journaldreceiver) collects systemd journal logs from the host and ingests them into the logs pipeline alongside your metrics.
It is configured to read from `/var/log/journal` (the default persistent journal path on Linux hosts) and applies `move` operators to rename journal fields to OpenTelemetry semantic conventions.

* `body._PID` is renamed to `body.pid`
* `body._EXE` is renamed to `attributes["process.executable.name"]`
* `body.MESSAGE` is renamed to `body.message`

This ensures that host logs are linked to the same process entities as the `hostmetrics` data, enabling correlation between metrics and logs in Dynatrace.

The `journald` receiver is supported on Linux OS only, and requires the `journalctl` binary on the host.
The Collector process must have permission to read the systemd journal.

On Linux hosts, add the user running the Collector to the `systemd-journal` group.

For full details, see [Use journald to ingest systemd journal logs with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/journald "Configure the OpenTelemetry Collector to ingest systemd journal logs from Linux hosts into Dynatrace.").

### Processors

Under `processors`, we specify the following processors:

* [`resource_detection` processor﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/resourcedetectionprocessor), which can be used to detect resource information from the host, in a format that conforms to the OpenTelemetry resource semantic conventions, and append or override the resource value in telemetry data with this information.
* [`filter`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/filterprocessor) is used twice: once to clean up unnecessary metrics dimensions, and secondly to (optionally) filter out unneeded process metrics.
* [`transform`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/transformprocessor).

### Exporters

Under `exporters`, we specify the [`otlp_http` exporter﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`).
* `DT_API_TOKEN` contains the [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

## How-to

### Topology

This extension automatically generates topology for infrastructure monitored via the Collector.
Specifically, it creates the following entity types based on metadata extracted from metrics, logs, and traces:

| Entity type | Entity ID |
| --- | --- |
| OpenTelemetry Host | dt.entity.otel:host |
| OpenTelemetry Process | dt.entity.otel:process |

These entities enable Dynatrace to correlate your metrics, logs, and spans and provide unified context across your monitored environment.

### Enrich application telemetry

If you send your application telemetry to your local host Collector, it will automatically enrich the data with the required host attributes so that the signals are correctly attached to the OpenTelemetry host entity.

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

This overlapp occurs because the Kubernetes monitoring use case uses the [`kubelet_stats` receiver﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/kubeletstatsreceiver), which reports node-level resource metrics that represent the same underlying data as the `hostmetrics` receiver.

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
  If you don't do this, the metric will be prevented from being captured.
* The `journald` receiver is only supported on Linux. Attempting to use the `journald` receiver on a different operating system will cause the Collector to return an error and exit on startup.