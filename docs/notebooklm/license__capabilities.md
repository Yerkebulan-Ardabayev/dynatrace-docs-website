# Dynatrace Documentation: license/capabilities

Generated: 2026-02-16

Files combined: 11

---


## Source: foundation-and-discovery.md


---
title: Calculate your consumption of Foundation & Discovery (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/app-infra-observability/foundation-and-discovery
scraped: 2026-02-15T21:13:28.489892
---

# Calculate your consumption of Foundation & Discovery (DPS)

# Calculate your consumption of Foundation & Discovery (DPS)

* Latest Dynatrace
* Explanation
* 1-min read
* Updated on Dec 10, 2025

Dynatrace OneAgent can be configured for Foundation & Discovery mode, which provides basic monitoring for your hosts (for example, host health, disk status, and OS service status).
Unlike other tools that provide basic monitoring, Foundation & Discovery leverages core OneAgent features: discovery and topology.

Foundation & Discovery mode detects process-to-process communication and populates the [Smartscape topology](/docs/analyze-explore-automate/smartscape-classic "Learn how Smartscape Classic visualizes all the entities and dependencies in your environment.") accordingly.
This provides important clues for AIOps which is included with OneAgent, see [DavisÂ® AI automatic root cause analysis](/docs/dynatrace-intelligence "Get familiar with the capabilities of Dynatrace Intelligence.") for details.

Broad deployment of Foundation & Discovery mode enables you to select the right monitoring mode for each of your hosts.
A hostâs criticality can be determined based on which processes, technologies, externally accessible services, and topological connections.

OneAgent in all modes also includes automated [log ingestion](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa "Ingest log data to Dynatrace using OneAgent and have Dynatrace transform it into meaningful log messages."), which consumes [Log Management and Analytics](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.").

### Host hours

The unit of measure for calculating consumption of host monitoring in Foundation & Discovery mode is a host hour.
Each instance of Dynatrace OneAgent installed and running on an operating system instance (deployed on either a physical or virtual machine) with Foundation & Discovery mode enabled consumes host hours.
The longer that a host is monitored, the more host hours are consumed.
Consumption is independent from a host's memory size.

Host-hour cost of Foundation & Discovery

While Foundation & Discovery and Infrastructure Monitoring both use host hours as their unit of measure for calculating monitoring consumption, Foundation & Discovery has a lower cost per host hour, reflecting its limited capabilities.
For details on [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/), see your rate card, or speak to your Dynatrace account manager.

#### Billing granularity for host-hour consumption

Dynatrace is built for elastic cloud-native environments where hosts and services are rapidly spun up and destroyed.
Therefore, billing granularity for host-hour consumption is based on 15-minute intervals.
When a host is monitored for fewer than 15 minutes in an interval, host-hour consumption is rounded up to 15 minutes before consumption is calculated.

The image below illustrates how host-hour consumption per host, calculated at 15-minute intervals.

![Foundation & Discovery consumption calculation](https://dt-cdn.net/images/discovery-consumption-1974-85ac28a179.webp)

### Metrics

Foundation & Discovery includes basic built-in metrics.
Unlike Full-Stack and Infrastructure Monitoring, Foundation & Discovery doesnât offer included custom metrics.
For more information, see [OneAgent monitoring modes](/docs/platform/oneagent/monitoring-modes/monitoring-modes#discovery "Find out more about the available monitoring modes when using OneAgent.").

## Consumption details: Foundation & Discovery

Dynatrace provides built-in usage metrics that help you understand and analyze your organization's consumption of Foundation & Discovery.
To use these metrics, in ![Data Explorer](https://dt-cdn.net/images/data-explorer-512-743267b1fc.png "Data Explorer") **Data Explorer**, enter `DPS` in the **Search** field.
These metrics are also available via the Environment API and your **Account Management** portal (**Usage summary** > **Foundation & Discovery** > **Actions** > **View details**).

(DPS) Foundation & Discovery billing usage
:   Key: `builtin:billing.foundation_and_discovery.usage`

    Dimension: count

    Resolution: 15 min

    Description: Total number of host hours in Foundation & Discovery mode, counted in 15 min intervals.

(DPS) Foundation & Discovery billing usage per host
:   Key: `builtin:billing.foundation_and_discovery.usage_per_host`

    Dimension: `dt.entity.host`

    Resolution: 15 min

    Description: Host hours per host in Foundation & Discovery mode, counted in 15 min intervals.

(DPS) Ingested metric data points for Foundation & Discovery
:   Key: `builtin:billing.foundation_and_discovery.metric_data_points.ingested`

    Dimension: count

    Resolution: 15 min

    Description: Number of metric data points aggregated over all Foundation & Discovery monitored hosts.

(DPS) Ingested metric data points for Foundation & Discovery per host
:   Key: `builtin:billing.foundation_and_discovery.metric_data_points.ingested_by_host`

    Dimension: `dt.entity.host`

    Resolution: 15 min

    Description: Number of metric data points split per Foundation & Discovery monitored host.

## Related topics

* [Dynatrace OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.")
* [Application & Infrastructure Observability overview (DPS)](/docs/license/capabilities/app-infra-observability "Learn about the different Application & Infrastructure Observability options that are available with a Dynatrace Platform Subscription (DPS) license.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)


---


## Source: full-stack-monitoring.md


---
title: Calculate your consumption of Full-Stack Monitoring (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/app-infra-observability/full-stack-monitoring
scraped: 2026-02-15T21:19:05.606150
---

# Calculate your consumption of Full-Stack Monitoring (DPS)

# Calculate your consumption of Full-Stack Monitoring (DPS)

* Latest Dynatrace
* Explanation
* 5-min read
* Updated on Dec 10, 2025

Full-Stack Monitoring for hosts and containers offers comprehensive application performance monitoring.
Application performance monitoring includes: distributed tracing, code-level visibility, CPU profiling, memory profiling, and deep process monitoring for hosts and containers.

* Host-based Full-Stack Monitoring:

  + Consumption is based on host memory, see [GiB-hours](#gib-hour).
  + Additionally offers all features of [Infrastructure Monitoring](/docs/license/capabilities/app-infra-observability/infrastructure-monitoring "Learn how your consumption of the Dynatrace Infrastructure Monitoring DPS capability is billed and charged.").

  + Additionally offers all features of [Kubernetes Platform Monitoring](/docs/license/capabilities/container-monitoring#kubernetes-monitoring "Learn about the different container monitoring modes that are available with a Dynatrace Platform Subscription (DPS) license.")[1](#fn-1-1-def) [2](#fn-1-2-def).

  + Dynatrace Extensions can be enabled on hosts with host-based Full-Stack Monitoring and may consume [Full-Stack custom metric data points](#full-stack-metrics) and [Log Analytics](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.").
* Container-based application-only Full-Stack Monitoring: Consumption is based on container memory, see [GiB-hour calculation for application-only container monitoring](#app-only-gib-hour)[3](#fn-1-3-def).

To learn more about supported platforms, see [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.").

1

Host-based Full-Stack monitoring includes Kubernetes Platform Monitoring for all pods running on Full-Stack monitored hosts.
Pods running on non-Full-Stack monitored hosts and pods stuck in Pending are not included in host-based Full-Stack monitoring.
These two types of pods are charged per pod-hour as described in [Kubernetes Platform Monitoring](/docs/license/capabilities/container-monitoring/kubernetes-platform-monitoring#how-consumption-is-calculated-pod-hour "Learn how your consumption of the Dynatrace Kubernetes Platform Monitoring DPS capability is billed and charged.").

2

For Kubernetes Platform Monitoring to be included with host-based Full-Stack monitoring, you must have OneAgent version 1.301+.
If you have OneAgent version 1.300 or earlier, Kubernetes Platform Monitoring will still be available, but pod-hour charges will apply as described in [Kubernetes Platform Monitoring](/docs/license/capabilities/container-monitoring/kubernetes-platform-monitoring#how-consumption-is-calculated-pod-hour "Learn how your consumption of the Dynatrace Kubernetes Platform Monitoring DPS capability is billed and charged.").

3

Container-based application-only Full-Stack Monitoring does not include Infrastructure Monitoring or Kubernetes Platform Monitoring.

## GiB-hours

Dynatrace uses GiB-hours (referred to as "memory-gibibyte-hours" in your rate card) as the unit of measure for calculating your organization's consumption of host monitoring in Full-Stack Monitoring mode.
The more memory that a host has, and the longer that the host is monitored, the higher the number of GiB-hours that the host consumes.

The advantage of the GiB-hour approach to monitoring consumption is its simplicity and transparency.
Technology-specific factors (for example, the number of JVMs or the number of microservices hosted on a server) don't affect consumption.
It doesn't matter if a host runs Kubernetes or other containerized applications, .NET-based applications, Java-based applications, or something else.
You can have 10 or 1,000 JVMs; such factors don't affect an environment's monitoring consumption.

### Billing granularity for GiB-hour consumption

Dynatrace is built for dynamic cloud-native environments where hosts and services are rapidly spun up and destroyed.
Therefore, billing granularity for GiB-hour consumption is calculated in 15-minute intervals.
When a host or container is monitored for fewer than 15 minutes in an interval, GiB-hour consumption is rounded up to 15 minutes before consumption is calculated.

### GiB-hour calculation for physical hosts and virtual machines (VMs)

Each installed instance of Dynatrace OneAgent running on an operating system instance (deployed on, for example, a physical or virtual machine) in Full-Stack Monitoring mode consumes GiB-hours based on the monitored host's physical or virtual RAM, calculated in 15-minute intervals (see the diagram example below).

The RAM of each VM or host is rounded up to the next multiple of 0.25 GiB (which equates to 256 MiB) before monitoring consumption is calculated.
A 4 GiB minimum is applied to GiB-hour consumption for physical and virtual hosts.
For example, a host with 8.3 GiB memory is counted as an 8.5 GiB host, being the next multiple of 0.25 GiB, while a host with 2 GiB memory is counted as a 4 GiB host (no rounding needed, but application of the 4 GiB minimum).

### GiB-hour calculation for application-only container monitoring

In cloud-native environments, services and hosts are often short-lived.
Therefore, calculating monitoring consumption in 15-minute time intervals, rather than full hours, better reflects actual usage.
Containers, which are an essential mechanism in cloud-native environments, typically use less memory than hosts.
Therefore, the minimum memory threshold for containers is 256 MiB, rather than 4 GiB, the minimum memory threshold for hosts.

The same rounding as for hosts, to the next multiple of 0.25 GiB, also applies to containers.
For example, a container with 780 MiB memory is counted as a 1 GiB container (780 MiB, which equals 0.78 GiB, being rounded up to the next multiple of 0.25 GiB).

The figure below illustrates how memory is counted for GiB-hour consumption calculations at 15-minute intervals.
Each interval is divided by four in order to reach the GiB-hour consumption unit of measure.

![Full-Stack consumption](https://dt-cdn.net/images/fullstack-monitoring-consumption-5584-2d3c737d8b.jpg)

#### Memory-size calculations

Memory-size calculations for containers monitored in an application-only approach are based on either:

* The container's used memory.

  + OneAgent version 1.275+ (for Kubernetes containers)
  + OneAgent version 1.297+ (for serverless containers)
* Container-defined memory limits.
  If no memory limit is set, the memory of the underlying virtual machine is used instead.

  + OneAgent version <1.275 (for Kubernetes containers)
  + OneAgent version <1.297 (for serverless containers)

[Automatic container detection](/docs/observe/infrastructure-observability/process-groups/configuration/cloud-app-and-workload-detection#automatic-container-detection "Detect cloud applications and workloads, and define rules to merge similar Kubernetes workloads into process groups.") needs to be enabled for existing tenants.

Certain monitoring scenarios have their own calculations for GiB-hour consumption, as described in the table below.

| Scenario | Description |
| --- | --- |
| Azure App Services (running on the App Service (dedicated) plan for Windows) | Consumption is based on the number and memory of the plan's instances. It does not matter how many applications run on the instances.  The minimum billed memory is 256 MiB (instead of 4 GiB). |
| Azure App Service (running on Linux OS or Linux containers) OneAgent version 1.297+ | If automatic container detection is enabled: consumption is based on the used memory of the container.  If automatic container detection is not enabled: consumption is based on the memory of the plan's instance, multiplied by the number of running containers. |
| Azure App Service (running on Linux OS or Linux containers) OneAgent version <1.297 | Consumption is based on the memory of the plan's instance, multiplied by the number of running containers, regardless if automatic container detection is enabled or not. |
| Oracle Solaris Zones | Solaris Zones are counted as hosts. |
| Monitored containers that are not detected as containers | These containers are counted as hosts. |

## Metrics

This section assumes that you have followed the Dynatrace-recommended deployment options.
If you implement a custom deployment, the charging of included Metrics may still work as describedâbut this is not guaranteed by Dynatrace.

Full-Stack Monitoring includes all Infrastructure Monitoring metrics, application performance monitoring metrics, and [other built-in metrics](/docs/license/capabilities/metrics/dps-metrics-ingest#billable-and-non-billable-metrics "Learn how your consumption of the Metrics - Ingest & Process DPS capability is billed and charged.").
These metrics are included and never produce any charge.

Full-Stack Monitoring also includes a defined amount of custom metric data points.
Every contributing GiB of host or application memory adds 900 custom metric data points in each 15-minute interval.
Included metric data points that are not consumed within the 15-minute interval in which they are granted do not roll over to subsequent intervals.
Your environment's included metric data points are applied automatically to metrics that originate at hosts and containers that are monitored by OneAgent in Full-Stack Monitoring mode.

All metric keys starting with `dt.service.*` are for [service monitoring](/docs/observe/application-observability/services "Learn how to monitor and analyze your services, define and use request attributes, and more.") and consume included Full-Stack metric data points if the span data itself originate at hosts and containers that are monitored by OneAgent in Full-Stack Monitoring mode.
If the span data originates at any other source, these metrics are charged as [Metrics powered by Grail](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").
Such metric keys include, for example:

* `dt.service.request.count`
* `dt.service.request.failure_count`
* `dt.service.request.response_time`
* `dt.service.request.service_mesh.count`
* `dt.service.request.service_mesh.failure_count`
* `dt.service.request.service_mesh.response_time`
* `dt.service.messaging.process.count`
* `dt.service.messaging.process.failure_count`
* `dt.service.messaging.publish.count`
* `dt.service.messaging.receive.count`

Metric data points that exceed your included volume are charged as:

* If Metrics powered by Grail exists on your rate card, these are charged as [Metrics powered by Grail](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").
* If Metrics powered by Grail does not exist on your rate card, these are charged as [Custom Metrics Classic](/docs/license/capabilities/platform-extensions/custom-metrics-classic "Learn how your consumption of the Dynatrace Custom Metrics Classic DPS capability is billed and charged.").

Your environment's included metric data points are applied automatically to metrics that originate at hosts and containers that are monitored by OneAgent in Full-Stack Monitoring mode.
This applies to custom metrics as described in the table below.

Origin

Examples (including but not limited to)

A Full-Stack monitored host sending metrics via the [OneAgent metric API](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Use the Dynatrace API to retrieve the metrics of monitored entities.")

* OpenTelemetry metrics
* Spring Micrometer
* StatsD
* JMX
* Extensions run locally on the host by OneAgent
* a host-local Telegraf

An application monitored with Container-based application-only Full-Stack Monitoring via the OneAgent code module

* OpenTelemetry metrics
* Spring Micrometer
* JMX

A Full-Stack monitored Kubernetes node or container, either via [Cloud Native Full-Stack](/docs/ingest-from/setup-on-k8s/deployment/full-stack-observability "Deploy Dynatrace Operator in cloud-native full-stack mode to Kubernetes"), [Classic Full-Stack](/docs/ingest-from/setup-on-k8s/deployment/other/classic-full-stack "Deploy Dynatrace Operator in classic full-stack mode to Kubernetes"), or [Application Observability](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") [1](#fn-2-1-def)

* OpenTelemetry metrics
* Spring Micrometer
* JMX
* [Prometheus metrics via ActiveGate](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.")
* Metrics sent via the Dynatrace Collector [2](#fn-2-2-def) or OpenTelemetry Collector [3](#fn-2-3-def)

[Service monitoring](/docs/observe/application-observability/services "Learn how to monitor and analyze your services, define and use request attributes, and more.") from a Full-Stack monitored application either via [Cloud Native Full-Stack](/docs/ingest-from/setup-on-k8s/deployment/full-stack-observability "Deploy Dynatrace Operator in cloud-native full-stack mode to Kubernetes"), [Classic Full-Stack](/docs/ingest-from/setup-on-k8s/deployment/other/classic-full-stack "Deploy Dynatrace Operator in classic full-stack mode to Kubernetes"), or [Application Observability](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") [1](#fn-2-1-def)

* `dt.service.request.count`
* `dt.service.request.failure_count`
* `dt.service.request.response_time`
* `dt.service.request.service_mesh.count`
* `dt.service.request.service_mesh.failure_count`
* `dt.service.request.service_mesh.response_time`

1

Metric data points originating from Application Observability are included only if [Metrics powered by Grail overview (DPS)](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.") exists on your rate card.

2

Metric data points sent via the Dynatrace Collector are included only if [Metrics powered by Grail overview (DPS)](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.") exists on your rate card.

3

Metric data points sent via the OpenTelemetry Collector are included only if [Metrics powered by Grail overview (DPS)](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.") exists on your rate card and the OpenTelemetry Collector has been configured as described in [Enrich from Kubernetes](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.").

### Included metric data point calculation example

Considering the example shown in Figure 1, here are the calculations for the included metric data point volumes for each of the four 15-minute intervals, assuming a volume of 900 included metric data points for each 15-minute interval.

* First 15-minute interval: `900 (included metric data points) Ã 13.5 (GiB memory) = 12,150 included metric data points`
* Second 15-minute interval: `900 (included metric data points) Ã 9.5 (GiB memory) = 8,550 included metric data points`
* Third 15-minute interval: `900 (included metric data points) Ã 8.75 (GiB memory) = 7,875 included metric data points`
* Fourth 15-minute interval: `900 (included metric data points) Ã 0.25 (GiB memory) = 225 included metric data points`

### How metric data points are consumed in Full-Stack Monitoring mode

Metric data point consumption takes many forms.
An equal number of data points can be consumed:

* By a few high-resolution metrics or numerous low-resolution metrics.
* Equally across multiple 15-minute intervals or all at once in a single minute.
* By all monitored hosts, a subset of all Full-Stack monitored hosts, or a single host.

## Distributed traces

Full-Stack Monitoring includes a defined amount of trace data volume.
Every contributing GiB of host or application memory adds 200 KiB of trace data per minute, for a total of 3000 KiB of trace data in each 15-minute interval of the [Monitoring environment](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
This volume addresses the majority of customer use cases.
If necessary, customers can explicitly [extend the trace ingest](#extend-trace-ingest).

Included trace data volume that is not consumed within the 15-minute interval in which it is granted does not roll over to subsequent intervals.

Environments that have less then 320 memory GiB contributing to the included trace volume will receive a fixed minimum peak volume of 64,000 KiB/minute, which is equivalent to 937.5 MiB in a single 15-minute interval.

Full-Stack Monitoring trace data comes from two sources and takes one of two forms.

* Trace data from the Dynatrace OneAgent: OneAgent automatically manages the volume of captured trace data via [Adaptive Traffic Management](/docs/ingest-from/dynatrace-oneagent/adaptive-traffic-management#dps "Dynatrace Adaptive Traffic Management provides dynamic sampling to ensure that the amount of capture traces stays within the Full-Stack Monitoring included trace volume.").
  It automatically and continuously adjusts the sampling rate in an intelligent way and keeps the ingested trace data volume roughly within your included trace-data volume, which prevents any unexpected costs.
* The second data source is trace data sent via the [OneAgent Trace API](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") or, more generally, OpenTelemetry traces that originate at a Full-Stack Monitoring host or application and are sent via the OTLP API.
  Trace data sent this way may be sampled by an OpenTelemetry agent, the SDK, or Collector at a fixed rate.
  These mechanisms are not controlled by Dynatrace or by [Adaptive Traffic Management](/docs/ingest-from/dynatrace-oneagent/adaptive-traffic-management#dps "Dynatrace Adaptive Traffic Management provides dynamic sampling to ensure that the amount of capture traces stays within the Full-Stack Monitoring included trace volume.").
  This means this trace data is not automatically kept below the included trace data volume.
  OpenTelemetry traces that are sent this way count against the included trace data volume (200 KiB of trace data per minute), and any trace data that exceeds the include trace data volume is charged as [Traces - Ingest & Process](/docs/license/capabilities/traces#trace-ingest-usage "Learn how Dynatrace Traces powered by Grail consumption is calculated using the Dynatrace Platform Subscription (DPS) model.").

  Note that traces sent via the Custom Trace API and not coming from a Full-Stack Monitoring host or application are always charged as [Traces - Ingest & Process](/docs/license/capabilities/traces#trace-ingest-usage "Learn how Dynatrace Traces powered by Grail consumption is calculated using the Dynatrace Platform Subscription (DPS) model.").

What about the included trace volume in DPS prior to Traces powered by Grail

While the uncompressed amount of spans and traces has not changed, the way Dynatrace measures this has changed with the release of Traces powered by Grail.
Due to this the stated included trace volume and the stated peak trace volume for DPS subscriptions prior the enablement of traces powered by Grail is different.

For non-Grail enabled DPS:

* Every contributing GiB of host or application memory adds a peak trace volume of 45 KiB/min.
* Each environment has a minimum trace peak volume of 14 MiB/min.

### Peak trace volume/minute calculation example

* First 15-minute interval: `200 KiB (peak trace volume) Ã 1350 (GiB memory) = 263.67 MiB/minute`
* Second 15-minute interval: `200 KiB (peak trace volume) Ã 950 (GiB memory) = 185.55 MiB/minute`
* Third 15-minute interval: `200 KiB (peak trace volume) Ã 875 (GiB memory) = 170.9 MiB/minute`
* Fourth 15-minute interval: `200 KiB (peak trace volume) Ã 25 (GiB memory) = 58.6 MiB/minute`

(In the fourth 15-minute interval the actually ingested amount would be below the minimum trace volume, hence the actual applied limit is equal to this minimum.)

### Included and extended Trace retention

Dynatrace [retains all traces](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods#purepath "Check retention times for various data types.") ingested from your environment for 10 days.

Dynatrace provides the ability to extend trace retention on a selective basis for up to 10 years, regardless of the ingest method or volume.
This is achieved by [creating custom buckets](/docs/platform/grail/organize-data "Insights on the Grail data model consisting of buckets, tables, and views.") in Grail.
The first 10 days of retention are always included.
Any trace data retained longer than 10 days is charged on a per-gibibyte basis as [Traces - Retain](/docs/license/capabilities/traces#trace-retain-usage "Learn how Dynatrace Traces powered by Grail consumption is calculated using the Dynatrace Platform Subscription (DPS) model.").

### Extended Trace ingest for Full-Stack Monitoring

Full-Stack Monitoring includes a defined amount of trace data volume.
Every contributing GiB of host or application memory adds 200 KiB of trace data per minute, for a total of 3000 KiB of trace data in each 15-minute interval of the [Monitoring environment](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").

Dynatrace provides the ability to extend the amount of trace data ingested with OneAgent.
To do this you can request an increased Trace ingest limit beyond the 200 KiB of trace data included per memory-gibibyte.
Adaptive Traffic Management keeps your trace ingestion within the requested volume, which prevents any unexpected costs.
(For an explanation of Adaptive Traffic Management, see [Distributed traces](#full-stack-traces)).
The trace data ingested that exceeds the included volume of 3000 KiB in a given 15-minute interval is charged as [Traces - Ingest & Process](/docs/license/capabilities/traces#trace-ingest-usage "Learn how Dynatrace Traces powered by Grail consumption is calculated using the Dynatrace Platform Subscription (DPS) model.").

The **Full-Stack Adaptive Traffic Management and trace capture** dashboard contains a calculator that helps you estimate how much data this will be based on your desired trace ingest volume.
To request Extended trace ingest for Full-Stack Monitoring, Please contact a Dynatrace product expert via live chat within your environment.

For example, your current trace capture rate is 100% most of times, but drops to 50% during peak times for 2 hours a day.
You can request a 2x Trace ingest volume limit, which would raise it to 400 KiB per contributing gibibyte in each 15-minute interval.
For those 2 hours per day you now ingest twice the amount of trace volume.
As a result your trace capture rate is now at 100% also during peak hours.
It does not charge anything for the 22 hours a day that you are already at 100% before the change.
During the 2 peak hours per day though about half the trace ingest volume will be charged as [Traces - Ingest & Process](/docs/license/capabilities/traces#trace-ingest-usage "Learn how Dynatrace Traces powered by Grail consumption is calculated using the Dynatrace Platform Subscription (DPS) model.").

### CPU, memory, and thread profiling

Full-Stack Monitoring includes [CPU](/docs/observe/application-observability/profiling-and-optimization/cpu-profiling "Learn how you can use Dynatrace to perform enhanced code analysis."), [memory](/docs/observe/application-observability/profiling-and-optimization/memory-profiling "Analyze memory allocation with Dynatrace."), and thread profiling for technologies like Java, .NET, Go, Node.js, and PHP.
OneAgent uses an intelligent patented mechanism to manage the volume of profiling data.
Dynatrace [retains the total amount of ingested profiling data](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods#purepath "Check retention times for various data types.") from your environment for 10 days.

## Consumption details: Full-Stack

Dynatrace provides built-in usage metrics that help you understand and analyze your organization's consumption of Full-Stack Monitoring.
To use these metrics, in ![Data Explorer](https://dt-cdn.net/images/data-explorer-512-743267b1fc.png "Data Explorer") **Data Explorer**, enter `DPS` in the **Search** field.
These metrics are also available via the Environment API and in Account Management (**Usage summary** > **Full-Stack Monitoring** > **Actions** > **View details**).

Here are the metrics you can use to monitor the consumption of Dynatrace Full-Stack Monitoring.

(DPS) Full-Stack Monitoring billing usage
:   Key: `builtin:billing.full_stack_monitoring.usage`

    Dimension: count

    Resolution: 15 min

    Description: Total GiB memory of all hosts monitored in Full-Stack Monitoring mode counted in 15-min intervals.

(DPS) Full-Stack Monitoring billing usage per host
:   Key: `builtin:billing.full_stack_monitoring.usage_per_host`

    Dimension: Host (`dt.entity.host`)

    Resolution: 15 min

    Description: GiB memory per host monitored in Full-Stack Monitoring mode counted in 15-min intervals.

(DPS) Full-stack usage by container type
:   Key: `builtin:billing.full_stack_monitoring.usage_per_container`

    Dimension: application\_only\_type; k8s.cluster.uid; k8s.namespace.name

    Resolution: 15 min

    Description: GiB memory per container monitored in Full-Stack application-only Monitoring mode counted in 15-min intervals.

(DPS) Total metric data points reported by Full-Stack monitored hosts
:   Key: `builtin:billing.full_stack_monitoring.metric_data_points.ingested`

    Dimension: Count

    Resolution: 15 min

    Description: Number of reported metric data points aggregated over all Full-Stack monitored hosts.

(DPS) Metric data points reported and split by Full-Stack monitored hosts
:   Key: `builtin:billing.full_stack_monitoring.metric_data_points.ingested_by_host`

    Dimension: Host (`dt.entity.host`)

    Resolution: 15 min

    Description: Number of reported metric data points split by Full-Stack monitored hosts.

(DPS) Available included metric data points for Full-Stack monitored hosts
:   Key: `builtin:billing.full_stack_monitoring.metric_data_points.included`

    Dimension: Count

    Resolution: 15 min

    Description: Total number of included metric data points that can be deducted from the consumed metric data points reported by Full-Stack monitored hosts.

(DPS) Used included metric data points for Full-Stack monitored hosts
:   Key: `builtin:billing.full_stack_monitoring.metric_data_points.included_used`

    Dimension: Count

    Resolution: 15 min

    Description: Number of consumed included metric data points for Full-Stack monitored hosts.

### Monitor memory-GiB-hour consumption for Full-Stack monitored hosts

You can monitor the total memory-GiB-hour consumption aggregated across all Full-Stack monitored hosts for different intervals (15 min, hour, day, or week) for any selected timeframe using the "(DPS) Full-Stack Monitoring billing usage" metric.
The example below shows memory GiB monitored in 1-hour intervals.
Between 11:00 and 14:00, 523 memory-GiB were monitored each 1 hour.
This results in 523 memory-GiB-hours consumed.

![Full-Stack Monitoring (DPS)](https://dt-cdn.net/images/image001-1183-79f381ccb1.png)

You can break down the total memory-GiB-hour consumption using the "(DPS) Full-Stack Monitoring billing usage per host" metric.
The example below shows the list of all hosts that contributed to the 523 memory-GiB-hour consumption between 13:00 and 14:00.
The respective number of memory-GiB-hours per host is displayed as well.

![Full-Stack Monitoring (DPS)](https://dt-cdn.net/images/image004-905-f0e44ad601.png)

### Monitor memory-GiB-hour consumption for Full-Stack monitored containers

Platform and cluster owners can monitor their Kubernetes clusters using [Kubernetes Platform Monitoring](/docs/license/capabilities/container-monitoring "Learn about the different container monitoring modes that are available with a Dynatrace Platform Subscription (DPS) license.").
Application owners can leverage container-based Full-Stack Monitoring to monitor applications running within Kubernetes clusters.

To get consumption insights for monitored Kubernetes clusters or namespaces, you can query memory-GiB-hour consumption by leveraging the "(DPS) Full-Stack Monitoring billing usage per container" metric, as shown in the following query:

`builtin:billing.full_stack_monitoring.usage_per_container:filter(eq("application_only_type","kubernetes")):splitBy()`

In the example below, 1.58 TiB of memory was consumed by the Kubernetes cluster within the past 30 days.

![Kubernetes Platform Monitoring](https://dt-cdn.net/images/billing-full-stack-monitoring-usage-per-container-1025-3019577b21.png)

Of course, you can filter your analysis for deeper insights (for example, add a split for Kubernetes namespaces).

![Kubernetes Platform Monitoring](https://dt-cdn.net/images/billing-full-stack-monitoring-usage-per-container-by-namespace-1023-c5e1c10583.png)

### Monitor metric consumption for Full-Stack monitored hosts

To monitor your metrics budget for the whole pool of metric data points in your environment, you can track available included metric data points against total reported metrics data points using these two metrics: "(DPS) Available included metric data points for Full-Stack monitored hosts" and "(DPS) Total metric data points reported by Full-Stack monitored hosts".
The example below shows data for a full day.
At no time was the number of included metrics for this environment's metric pool (purple line) overspent.

![Full-Stack Monitoring (DPS)](https://dt-cdn.net/images/image005-1212-35369921df.png)

In cases where the number of included metrics for an environment's metric pool are overspent, the following analysis can help you to identify the hosts that are contributing to the overspending.
Use the metric "(DPS) Metric data points reported and split by Full-Stack monitored hosts" for this analysis.

The example below shows that between 10:45 and 11:00, each of the first 3 hosts in the list reported far more than 2,000 metric data points.
In the same period, each of these 3 hosts shows a memory-GiB-hour consumption of 2 GiB.
Dynatrace offers 900 included custom metric data points for each GiB of host memory, calculated at 15-minute intervals.
This means that the first 3 hosts contribute 1,800 (2\*900) metric data points to the environment's pool of available data points.
However these hosts consumed more data points than they contributed during the same time period.

![Full-Stack Monitoring (DPS)](https://dt-cdn.net/images/image008-905-929928d644.png)

When using the metric "(DPS) Total metric data points billed for Full-Stack monitored hosts" from Custom Metrics Classic you can see that no overspending occurred for this environment's Full-Stack Monitoring metric pool between 10:45 and 11:00 because no metric data points were billed.

![Full-Stack Monitoring (DPS)](https://dt-cdn.net/images/image009-1210-914bc4742c.png)

## Related topics

* [Dynatrace OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.")
* [Application & Infrastructure Observability overview (DPS)](/docs/license/capabilities/app-infra-observability "Learn about the different Application & Infrastructure Observability options that are available with a Dynatrace Platform Subscription (DPS) license.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)


---


## Source: infrastructure-monitoring.md


---
title: Calculate your consumption of Infrastructure Monitoring (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/app-infra-observability/infrastructure-monitoring
scraped: 2026-02-15T21:13:27.338221
---

# Calculate your consumption of Infrastructure Monitoring (DPS)

# Calculate your consumption of Infrastructure Monitoring (DPS)

* Latest Dynatrace
* Explanation
* 1-min read
* Updated on Dec 10, 2025

Dynatrace OneAgent can be configured for Infrastructure Monitoring mode, which provides comprehensive host monitoring for physical and virtual hosts.

In addition to all features of [Foundation & Discovery](/docs/license/capabilities/app-infra-observability/foundation-and-discovery "Learn how your consumption of the Dynatrace Foundation & Discovery DPS capability is billed and charged."), Infrastructure Monitoring also includes detailed process performance metrics, disk performance metrics, process-to-process network analysis, and per process memory analysis.
Dynatrace Extensions can be enabled on hosts with Infrastructure Monitoring mode and may consume [custom metric data points](/docs/license/capabilities/app-infra-observability/infrastructure-monitoring#infra-metrics "Learn how your consumption of the Dynatrace Infrastructure Monitoring DPS capability is billed and charged.") and [Log Analytics](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.").

### Host hours

The unit of measure for calculating consumption of host monitoring in Infrastructure Monitoring mode is a host-hour.
Each instance of Dynatrace OneAgent installed and running on an operating system instance (deployed on, for example, a physical or virtual machine) with Infrastructure Monitoring mode enabled consumes host hours.
The longer that a host is monitored, the more host-hours you consume.
Consumption is independent from a host's memory size.

### Billing granularity for host-hour consumption

Dynatrace is built for dynamic cloud-native environments where hosts and services are rapidly spun up and destroyed.
Therefore, billing granularity for host-hour consumption is calculated in 15-minute intervals.
When a host is monitored for fewer than 15 minutes in an interval, host-hour consumption is rounded up to 15 minutes before consumption is calculated.

The figure below illustrates how host-hour consumption per host is calculated at 15-minute intervals.

![Infrastructure Monitoring consumption](https://dt-cdn.net/images/infrastructure-monitoring-consumption-5843-2c70d0f91c.jpg)

### Metrics

This section assumes that you have followed the Dynatrace-recommended deployment options.
If you implement a custom deployment, the charging of included Metrics may still work as describedâbut this is not guaranteed by Dynatrace.

Dynatrace Infrastructure Monitoring includes Infrastructure Monitoring metrics and [other built-in metrics](/docs/license/capabilities/metrics/dps-metrics-ingest#billable-and-non-billable-metrics "Learn how your consumption of the Metrics - Ingest & Process DPS capability is billed and charged.").
These metrics are included and never produce any charge.

Infrastructure Monitoring also includes a defined amount of custom metric data points.
Every host adds 1,500 custom metric data points in each 15-minute interval.
Included metric data points that are not consumed within the 15-minute interval in which they are granted do not roll over to subsequent intervals.
Your environment's included metric data points are applied automatically to metrics that originate at hosts that are monitored by OneAgent in Infrastructure Monitoring mode.
This applies to custom metrics as described in the table below.

Metric data points that exceed your included volume are charged as:

* If Metrics powered by Grail exists on your rate card, these are charged as [Metrics powered by Grail](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").
* If Metrics powered by Grail does not exist on your rate card, these are charged as [Custom Metrics Classic](/docs/license/capabilities/platform-extensions/custom-metrics-classic "Learn how your consumption of the Dynatrace Custom Metrics Classic DPS capability is billed and charged.").

Origin

Examples (including but not limited to)

An Infrastructure-monitored host and sent via the [OneAgent metric API](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Use the Dynatrace API to retrieve the metrics of monitored entities.")

* OpenTelemetry metrics
* Spring Micrometer
* StatsD
* JMX
* Extensions run locally on the host by OneAgent
* a host-local Telegraf

An Infrastructure-monitored Kubernetes node

* OpenTelemetry metrics
* Spring Micrometer
* JMX
* [Prometheus metrics via ActiveGate](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.")

* Metrics sent via the Dynatrace Collector [1](#fn-1-1-def) or OpenTelemetry Collector [2](#fn-1-2-def)

1

Metric data points sent via the Dynatrace Collector are included only if [Metrics powered by Grail overview (DPS)](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.") exists on your rate card.

2

Metric data points sent via the OpenTelemetry Collector are included only if [Metrics powered by Grail overview (DPS)](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.") exists on your rate card and the OpenTelemetry Collector has been configured as described in [Enrich from Kubernetes](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.").

Looking at Figure 2 above, the included custom metric data point volume for the four 15-minute intervals is shown below.

### Included custom metric data points calculation example

* First 15-minute interval: `1 (hosts monitored) Ã 1,500 (metric data points) = 1,500 Included custom metric data points`
* Second 15-minute interval: `2 (hosts monitored) Ã 1,500 (metric data points) = 3,000 Included custom metric data points`
* Third 15-minute interval: `1 (hosts monitored) Ã 1,500 (metric data points) = 1,500 Included custom metric data points`
* Fourth 15-minute interval: `1 (hosts monitored) Ã 1,500 (metric data points) = 1,500 Included custom metric data points`

### How custom metric data points are consumed in Infrastructure Monitoring mode

Custom metric data point consumption takes many forms.
An equal number of custom metric data points can be consumed:

* By a few high-resolution metrics or numerous low-resolution metrics.
* Equally across multiple 15-minute intervals or all at once in a single minute.
* By all Infrastructure-monitored hosts, a subset of all Infrastructure-monitored hosts, or a single infrastructure-monitored host.

## Consumption details: Infrastructure

Dynatrace provides built-in usage metrics that help you understand and analyze your organization's consumption of Infrastructure Monitoring.
To use these metrics, in ![Data Explorer](https://dt-cdn.net/images/data-explorer-512-743267b1fc.png "Data Explorer") **Data Explorer**, enter `DPS` in the **Search** field.
These metrics are also available via the Environment API and in Account Management (**Usage summary** > **Infrastructure Monitoring** > **Actions** > **View details**)
.

Here is the list of metrics you can use to monitor the consumption details for Infrastructure Monitoring.

(DPS) Infrastructure Monitoring billing usage
:   Key: `builtin:billing.infrastructure_monitoring.usage`

    Dimension: Count

    Resolution: 15 min

    Description: Total number of host hours consumed in Infrastructure Monitoring mode.

(DPS) Infrastructure Monitoring billing usage per host
:   Key: `builtin:billing.infrastructure_monitoring.usage_per_host`

    Dimension: Host (`dt.entity.host`)

    Resolution: 15 min

    Description: Consumed host hours in Infrastructure Monitoring mode per host.

(DPS) Total metric data points reported by Infrastructure hosts
:   Key: `builtin:billing.infrastructure_monitoring.metric_data_points.ingested`

    Dimension: Count

    Resolution: 15 min

    Description: Number of metric data points consumed by all Infrastructure-monitored hosts.

(DPS) Metric data points reported and split by Infrastructure hosts
:   Key: `builtin:billing.infrastructure_monitoring.metric_data_points.ingested_by_host`

    Dimension: Host (`dt.entity.host`)

    Resolution: 15 min

    Description: Number of metric data points, split by Infrastructure-monitored hosts.

(DPS) Available included metric data points for Infrastructure-monitored hosts
:   Key: `builtin:billing.infrastructure_monitoring.metric_data_points.included`

    Dimension: Count

    Resolution: 15 min

    Description: Total number of included metric data points deductible from the metric data points reported by all Infrastructure-monitored hosts.

(DPS) Consumed included metric data points for Infrastructure hosts
:   Key: `builtin:billing.infrastructure_monitoring.metric_data_points.included_used`

    Dimension: Count

    Resolution: 15 min

    Description: Number of consumed included metric data points for Infrastructure-monitored hosts.

(DPS) Total metric data points billed for Infrastructure hosts
:   Key: `builtin:billing.custom_metrics_classic.usage.infrastructure_hosts`

    Dimension: Count

    Resolution: 15 min

    Description: Number of metric data points billed for all Infrastructure-monitored hosts.

### Monitor host-hour consumption

You can monitor the total host-hour consumption for different intervals (15 min, hour, day, or week) for any selected timeframe using the "(DPS) Infrastructure Monitoring billing usage" metric.
The example below shows that 5 hosts were monitored, leading to total consumption of 5 host-hours for each hour.

![Infrastructure Monitoring (DPS)](https://dt-cdn.net/images/image011-1099-50bac22dd0.png)

You can split the total host hour consumption using the metric "(DPS) Infrastructure Monitoring billing usage per host".
The example below shows the list of all hosts that reported consumption.

![Infrastructure Monitoring (DPS)](https://dt-cdn.net/images/image013-1099-cb1470f609.png)

### Monitor metric consumption for Infrastructure monitored hosts

Use the metric "(DPS) Total metric data points billed for Infrastructure hosts" to monitor the number of metric data points that are billed for Infrastructure monitored hosts, as shown in the example below.

![Infrastructure Monitoring (DPS)](https://dt-cdn.net/images/image015-1101-5c4b7620a4.png)

To manage your metrics budget, you can monitor the number of available included metric data points against the number of total consumed metrics data points using these two metrics: "(DPS) Available included metric data points for Infrastructure hosts" and "(DPS) Total metric data points reported by Infrastructure hosts".
The example below shows that more metric data points were consumed that were included with these Infrastructure monitored hosts.

![Infrastructure Monitoring (DPS)](https://dt-cdn.net/images/image017-1100-7b133be12d.png)

You can use the metric "(DPS) Metric data points reported and split by Infrastructure hosts" to track the number of metric data points consumed per Infrastructure monitored host.
The split view helps in discovering the hosts that consume the most metric data points.
The example below shows that one of the Infrastructure monitored hosts reported significantly more metrics data points than the others.

![Infrastructure Monitoring (DPS)](https://dt-cdn.net/images/image019-1768-c4ed044b93.png)

## Related topics

* [Dynatrace OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.")
* [Application & Infrastructure Observability overview (DPS)](/docs/license/capabilities/app-infra-observability "Learn about the different Application & Infrastructure Observability options that are available with a Dynatrace Platform Subscription (DPS) license.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)


---


## Source: mainframe.md


---
title: Calculate your consumption of Mainframe Monitoring (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/app-infra-observability/mainframe
scraped: 2026-02-15T21:19:09.783938
---

# Calculate your consumption of Mainframe Monitoring (DPS)

# Calculate your consumption of Mainframe Monitoring (DPS)

* Latest Dynatrace
* Explanation
* 1-min read
* Updated on Dec 10, 2025

Dynatrace Mainframe Monitoring provides automatic end-to-end application performance monitoring for transactions, regions, and apps deployed on IBM z/OS.
It includes distributed tracing, metrics, topology, and code-level insight for [30+ supported technologies](/docs/ingest-from/technology-support/mainframe-technology-support "Learn which technologies Dynatrace supports for Mainframe monitoring.").

With the DPS capability for Mainframe Monitoring:

* You get flexibility in licensing for incremental monitoring rollouts (for example, you can start small and expand coverage over time).
* You only pay for the active monitoring period (for example, downtimes are not charged).
* You get cost transparency and budget management in Account Management.
* The usage of ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** and ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** is included with Dynatrace.
  No query consumption is generated by these apps.

The technical prerequisites for DPS are:

* Dynatrace Cluster version 1.279+
* [zRemote module](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Prepare and install the zRemote for z/OS monitoring.") version 1.265+
* [zDC subsystem](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc "Set up the z/OS Data Collection subsystem (zDC).") version 1.247+

A monitored Logical Partition (LPAR) is represented as a host in Dynatrace.
The billing for monitoring an LPAR depends on the partitionâs Million Service Unit (MSU) value and the duration of Dynatrace monitoring.
An MSU is an IBM measurement of the amount of processing work an IBM Z mainframe can perform in one hour.

### MSU hours

The unit of measure for Mainframe Monitoring is an MSU hour.
Mainframe Monitoring consumption derives MSU hours based on the [IBM Tailored Fit Pricingï»¿](https://www.ibm.com/support/z-content-solutions/tailored-fit-pricing/) software consumption solution, retrieved per LPAR from [SMF type 70 subtype 1 recordsï»¿](https://www.ibm.com/docs/en/zos/2.5.0?topic=conditions-cpu-activity-smf-record-type-70-1) (actual number of consumed MSUs).

The more MSUs an LPAR has, and the longer Dynatrace monitors it, the higher the MSU-hour consumption.

### Billing granularity for MSU-hour consumption

The billing granularity for MSU-hour consumption is calculated in four 15-minute intervals per hour.
If an LPAR is monitored for less than 15 minutes in an interval, MSU-hour consumption is rounded up to 15 minutes before consumption is calculated.
The sum of MSU hours of all monitored LPARs represents the total consumption.

### Distributed tracing

### Included and extended Trace retention

Dynatrace [retains the total amount of ingested trace volume](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods#purepath "Check retention times for various data types.") from your environment for 10 days.

Dynatrace provides the ability to extend trace retention on a selective basis for up to 10 years.
This is achieved by [creating custom buckets](/docs/platform/grail/organize-data "Insights on the Grail data model consisting of buckets, tables, and views.") in Grail.
The first 10 days of retention are always included.
Any trace data retained longer than 10 days is charged on a per-Gibibyte basis as [Trace Retain](/docs/license/capabilities/traces#trace-retain-usage "Learn how Dynatrace Traces powered by Grail consumption is calculated using the Dynatrace Platform Subscription (DPS) model.").

### Metrics

Mainframe Monitoring includes application performance monitoring and related built-in metrics, except custom metrics, which are measured in metric data points and charged as [Metrics powered by Grail](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").
For example, [custom JMX metrics](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/zos-java-custom-jmx-metrics "Learn how to set up JMX metrics monitoring for your Java applications on z/OS.") consume metric data points.

How are metrics charged in DPS prior to Metrics powered by Grail

If [Metrics powered by Grail](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.") does not exist on your rate card, metric data points are charged as [Custom Metrics Classic](/docs/license/capabilities/platform-extensions/custom-metrics-classic "Learn how your consumption of the Dynatrace Custom Metrics Classic DPS capability is billed and charged.").

## Consumption details: Mainframe

Dynatrace provides a usage metric that helps you understand and analyze your MSU-hour consumption.
To use this metric, in ![Data Explorer](https://dt-cdn.net/images/data-explorer-512-743267b1fc.png "Data Explorer") **Data Explorer**, enter the following metric key or name in the **Search** field.

Alternatively, you can query this metric via the [Environment API - Metrics API v2](/docs/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

(DPS) Mainframe Monitoring billing usage
:   Key: `builtin:billing.mainframe_monitoring.usage`

    Dimension: Host (`dt.entity.host`)

    Resolution: 15 min

    Description: Total number of MSU hours monitored, counted in 15 min intervals.

You can break down the MSU-hour consumption per LPAR.
The example below shows all LPARs that contributed to the consumption in 1-hour intervals within the last 24 hours.

![DPS Mainframe Monitoring billing metric](https://dt-cdn.net/images/billing-metric-1559-0f648884c8.png)

You can also view the usage metric in Account Management.
Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **Subscription** > **Overview** > **Cost and usage details** > **Usage summary** and select the **Mainframe Monitoring** capability.

![MSU Usage Summary](https://dt-cdn.net/images/msu-usage-summary-1505-3ab6abffd5.png)

## Consumption estimate: Mainframe

Use the [IBM Sub-Capacity Reporting Tool (SCRT) reportï»¿](https://www.ibm.com/docs/en/zos/2.5.0?topic=tool-about-sub-capacity-reporting) to estimate the required MSU-hour consumption per year.

1. In Section **C5**, check the **Reporting Period** of the SCRT report.
   Typically, it contains one month of data.
2. In Section **N7**, sum the **Total MSU Consumed** value for each LPAR to be monitored.
3. If the reporting period is one month, multiply the **Total MSU Consumed** by 12 months to get annual consumption.

![SCRT report example](https://dt-cdn.net/images/scrt-report-example-936-7ea2942e4f.png)

In this example, the three LPARs (S1LP01, S2LP02, and TF1LP1) consumed 99,000 MSU hours in September 2023.

Multiplied by 12 months, this equates to 1,188,000 MSU hours per year.

Notes:

* This approach might not consider seasonal workload fluctuations, which can lead to deviations in actual consumption.
* Section **N7** has been available since IBM SCRT version 25.2.
  It was released by IBM in December 2017.

Network availability monitoring (NAM) monitors don't have a separate line on the Dynatrace rate card. Instead, you're billed based on the [number of metric data points](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.") generated during each execution of a NAM test. For more information, please contact your Dynatrace account manager.

Metric data point calculations

The following details apply to metric data points:

* Metric data points related to monitor and step execution are non-billable.
* Only the consumption of metrics produced at the request level affects your billing.
* Each request execution within ping tests generates 6 metric data points.

  + The number of packets used in a ping test does not impact the number of metrics produced or your billing.
  + The number of packets does not affect the price.
* Each request execution within TCP/DNS tests generates 3 metric data points.
* The price stays the same regardless of whether you create several tests containing a single request, or you create one test with numerous requests for the same set of hosts or devices.

## Related topics

* [Dynatrace OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.")
* [Application & Infrastructure Observability overview (DPS)](/docs/license/capabilities/app-infra-observability "Learn about the different Application & Infrastructure Observability options that are available with a Dynatrace Platform Subscription (DPS) license.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)


---


## Source: appengine-functions.md


---
title: AppEngine Functions (Serverless Functions) overview (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/appengine-functions
scraped: 2026-02-15T09:09:13.036073
---

# AppEngine Functions (Serverless Functions) overview (DPS)

# AppEngine Functions (Serverless Functions) overview (DPS)

* Latest Dynatrace
* Explanation
* 6-min read
* Updated on May 22, 2025

AppEngine Functions are the backend for your app.
They are written in TypeScript and run within the [Dynatrace JavaScript runtimeï»¿](https://developer.dynatrace.com/reference/javascript-runtime/).

There are three types of AppEngine Functions:

* App functions:
  These functions represent the backend of an app and are built, bundled, and deployed together with your custom app.
* Ad-hoc functions:
  Custom code that accomplishes a specific use case is referred to as an ad-hoc function.
  These functions can be invoked from within ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**, or directly via API.
* Custom actions:
  A specific type of app function that, together with a UI component, can be declared as a custom workflow action to extend ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**.
  Custom actions can then be selected as a task within ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** and can be executed within a workflow.

All AppEngine Functions are deployed in an environment with 256 MiB RAM.

AppEngine Functions work out-of-the-box: no external hosting is required, and there is no need to worry about maintaining a runtime environment to execute logic or code.

## Related topics

* [AppEngine](/docs/platform/appengine "Develop feature-rich Dynatrace apps for you and the world!")
* [App functionsï»¿](https://developer.dynatrace.com/develop/functions/ "Basic concepts of app functions, which represent an app backend")
* [License Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)


---


## Source: kubernetes-platform-monitoring.md


---
title: Calculate your consumption of Kubernetes Platform Monitoring (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/container-monitoring/kubernetes-platform-monitoring
scraped: 2026-02-06T16:26:50.506651
---

# Calculate your consumption of Kubernetes Platform Monitoring (DPS)

# Calculate your consumption of Kubernetes Platform Monitoring (DPS)

* Latest Dynatrace
* Explanation
* 3-min read
* Updated on Nov 12, 2025

Kubernetes Platform Monitoring feature overview

This page describes how the Kubernetes Platform Monitoring DPS capability is consumed and billed.
For an overview of the capability, including its main features, see [Kubernetes Platform Monitoring](/docs/license/capabilities/container-monitoring#kubernetes-monitoring "Learn about the different container monitoring modes that are available with a Dynatrace Platform Subscription (DPS) license.").

## How consumption is calculated: pod-hour

The unit of measure for calculating consumption of Kubernetes Platform Monitoring is a pod-hour.
The longer a pod is monitored, the more pod-hours the environment consumes.
Note that a pod-hour is independent of the size of the pod.

OneAgent version 1.301+ When Kubernetes Platform Monitoring is run in combination with Full-Stack Monitoring, consumption for all pods running on a Full-Stack monitored host is included with [Full-Stack Monitoring](/docs/license/capabilities/app-infra-observability/full-stack-monitoring "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.").

Pods on non-Full-Stack hosts, as well as pods stuck in Pending, still contribute to your consumption of pod-hours, as described on this page.

## Billing granularity for pod-hour consumption

Dynatrace is built for elastic cloud-native environments where services are often short-livedâwhich is the case for pods running in Kubernetes environments.
Therefore, billing granularity for pod-hour consumption is based on 15-minute intervals.
When a pod is monitored for fewer than 15 minutes in an interval, pod-hour consumption is rounded up to the full 15 minutes before consumption is calculated.

The image below illustrates how pod-hour consumption per pod is calculated.

![Pod-hour consumption per pod, calculated at 15-minute intervals](https://dt-cdn.net/images/kubernetes-platform-monitoring-diagram-v1-1-2x-3466-8555efc78a.png)

## What observability value is included in a pod-hour?

Kubernetes Platform Monitoring offers in-depth observability insights for Kubernetes clusters, including the following signals:

* A comprehensive set of resource and health metrics for clusters, namespaces, pods, containers, and nodes.
* Kubernetes warning events are included on a fair-use basis.
  The fair-use quota is designed to cover all Kubernetes warning events in regular scenarios.  
  A pod-hour includes 60 Kubernetes warning events per pod.
  The Kubernetes warning events are pooled across all pods.
  The consumption of the fair-use quota is calculated in 15-minute intervals.

  Dynatrace currently doesnât charge for Kubernetes warning events in excess of the amount allowed under your fair-use quota.

  Additional events are licensed via Custom Events Classic pricing.
  By March 2024, additional events will be billed via Events powered by Grail.
* Kubernetes anomaly detection for alerting.

Kubernetes info events, Prometheus metrics, and Istio metrics are not included in a pod-hour.

## Track your consumption

This section describes the different Dynatrace tools that you can use to track consumption and costs.

### Track your consumption with Metrics

Dynatrace provides built-in usage metrics that help you understand and analyze your organization's consumption of Kubernetes Platform Monitoring.
To use these metrics, in Data Explorer, enter `DPS` in the Search field.

Here is the metric you can use to monitor the consumption details for Kubernetes Platform Monitoring.

(DPS) Kubernetes Monitoring billing usage
:   Key: `builtin:billing.kubernetes_monitoring.usage`

    Dimension: Kubernetes cluster; Kubernetes namespace

    Resolution: 15 min

    Description: Total number of pod-hours consumed.

Example scenario: Monitor pod-hour consumption

You can monitor the total pod-hour consumption for different intervals (hour, day, or week) for any selected timeframe using the (DPS) Kubernetes Monitoring billing usage metric.
The example below shows consumption aggregated in 1-hour intervals and split by Kubernetes cluster.
You can monitor the total pod-hour consumption for different intervals (hour, day, or week) for any selected timeframe using the (DPS) Kubernetes Monitoring billing usage metric.
Aggregated consumption metrics will also be provided in Account Management.
The example below shows consumption aggregated in 1-hour intervals and split by Kubernetes cluster.

![Pod - hour consumption](https://dt-cdn.net/images/pod-hour-consumption-2764-a622f9aa28.png)

### Track your consumption and costs in Account Management

You can track your usage in Account Management.
Go to **Cost and usage details** > **Usage summary** > **Kubernetes monitoring** > **Actions** > **View details**.

### Track your consumption and costs via API

You can query metrics via the [Environment API - Metrics API v2](/docs/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").


---


## Source: events.md


---
title: Events powered by Grail overview (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/events
scraped: 2026-02-15T21:17:36.637514
---

# Events powered by Grail overview (DPS)

# Events powered by Grail overview (DPS)

* Latest Dynatrace
* Overview
* 5-min read
* Updated on Jan 28, 2026

This page describes the different Events-related capabilities and the features that they provide with a DPS subscription.

For information about how usage of a specific capability translates to consumption of your DPS license commit, see

* [Events - Ingest & Process](/docs/license/capabilities/events/dps-events-ingest "Learn how your consumption of the Events powered by Grail - Ingest & Process DPS capability is billed and charged.")
* [Events - Retain](/docs/license/capabilities/events/dps-events-retain "Learn how your consumption of the Events powered by Grail - Retain DPS capability is billed and charged.")
* [Events - Query](/docs/license/capabilities/events/dps-events-query "Learn how your consumption of the Events powered by Grail - Query DPS capability is billed and charged.")

Dynatrace provides monitoring and reporting of

* Built-in event types via OneAgent or cloud integrations.
* Custom events and/or event-ingestion channels.
  These include

  + Any custom event sent to Dynatrace via the [Events API v2](/docs/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.") or the [OneAgent API](/docs/ingest-from/extend-dynatrace/extend-events#oneagent "Learn how to extend event observability in Dynatrace.").
  + Any custom event (such as a Kubernetes event) created from log messages by a [log processing rule](/docs/analyze-explore-automate/logs/lma-classic-log-processing#lmc-log-processing-rules "Utilize log processing rules to reshape incoming log data for better understanding, analysis, or further transformation.").
  + Any custom event created in a [processing step](/docs/platform/openpipeline/concepts/processing "Learn the core concepts of Dynatrace OpenPipeline processing.") in OpenPipeline.

The consumption of all events is billable, except for certain included events, as described in the "Included events" table below.

List of billable event types

The following events are billable:

* Business events
* SDLC events
* Custom events, including

  + Security events
  + Davis events
  + Kubernetes warning events
  + Generic custom events
  + Customer-defined custom events

Included events

The table below describes events that are included with a separate rate-card capability package.

Built-in event kind

Relevant capability

Ingest & Process

Retain[1](#fn-1-1-def)

Query

Dynatrace Intelligence problems and events

Full-Stack Monitoring

Included

First 15 months are included

Included

Kubernetes warning events

Kubernetes Platform Monitoring

60 warning events per pod-hour are included

First 15 months are included

Queries generated from within ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** are included

Built-in security events

Runtime Vulnerability Analytics (RVA)

Included

First 3 years are included

Queries generated from within ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** are included

1

Retention beyond the included timeframe is billable as Events powered by Grail - Retain.

## Events - Ingest & Process feature overview

Here's what's included with the Ingest & Process data-usage dimension:

Concept

Explanation

Data delivery

Delivery of events via OneAgent, RUM JavaScript, or Generic Event Ingestion API (via ActiveGate)

Topology enrichment

Enrichment of events with data source and topology metadata

Data transformation

* Add, edit, or drop any business event attribute
* Perform mathematical transformations on numerical values (for example, creating new attributes based on calculations of existing fields)
* Extract business, infrastructure, application, or other data from raw business events.
  This can be a single character, string, number, array of values, or other.
  Extracted data can be turned into a new field, allowing additional querying, filtering, etc.
* Mask sensitive data by replacing specific business attributes with a masked string

Data-retention control

Manage data retention periods of incoming events based on bucket assignment rules

Conversion to timeseries

Create metrics from event attributes (note that creating custom metrics generates additional consumption beyond the consumption for ingestion and processing.)

## Events - Retain feature overview

Here's what's included with the Retain data-usage dimension:

Concept

Explanation

Data availability

Retained data is accessible for analysis and querying until the end of the retention period.
Events retention is defined at the bucket level, ensuring tailored retention periods for specific events.

Retention periods

Choose a retention period

* 10 days (10 days)
* 2 weeks (15 days)
* 1 month (35 days) (this is the default period)
* 3 months (95 days)
* 1 year (372 days)
* 15 months (462 days)
* 3 years (1,102 days)
* 5 years (1,832 days)
* 7 years (2,562 days)
* 10 years (3,657 days)

## Events - Query feature overview

Query data usage occurs when:

* Submitting custom DQL queries in the Logs & Events viewer in advanced mode.
* Business Observability Apps (Business Flow, Salesforce Insights, and Carbon Impact)
* Executing DQL queries in Notebooks, Dashboards, Workflows, Custom apps, and via API.

Here's what's included with the Query data-usage dimension:

Concept

Explanation

On-read parsing

* Use DQL to query historical events in storage and extract business, infrastructure, or other data across any timeframe, and use extracted data for follow-up analysis.
* No upfront indexes or schema required for on-read parsing

Aggregation

Perform aggregation, summarization, or statistical analysis of data in events across specific timeframes or time patterns (for example, data occurrences in 30-second or 10-minute intervals), mathematical, or logical functions.

Reporting

Create reports or summaries with customized fields (columns) by adding, modifying, or dropping existing event attributes.

Context

Use DQL to analyze event data in context with relevant data on the Dynatrace platform, for example, user sessions or distributed traces.

## Related topics

* [Log events](/docs/analyze-explore-automate/logs/lma-log-processing/lma-log-events "Create log events based on log data and use them in problem detection.")
* [Metric events](/docs/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace")
* [Events API v2](/docs/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.")
* [What is Dynatrace Grail?](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more.")
* [License Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)


---


## Source: dps-log-query.md


---
title: Calculate your consumption of Log Management & Analytics - Query (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/log-analytics/dps-log-query
scraped: 2026-02-15T21:10:47.683062
---

# Calculate your consumption of Log Management & Analytics - Query (DPS)

# Calculate your consumption of Log Management & Analytics - Query (DPS)

* Latest Dynatrace
* Explanation
* 6-min read
* Updated on Nov 04, 2025

Log - Query feature overview

This page describes how the Log Management & Analytics - Query DPS capability is consumed and billed.
For an overview of the capability, including its main features, see [Log Analytics (DPS)](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.").

The usage of ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** and ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** is included with Dynatrace.
No consumption is generated by these apps.

## How consumption is calculated: GiB scanned

Queried data is the volume of data read during the execution of a DQL query.
It is calculated per gibibyte scanned (GiB scanned).

Apply the following calculation to determine your consumption for the Query data-usage dimension:

`consumption = (number of GiB of uncompressed data read during query execution) Ã (GiB scanned price as per your rate card)`

Query consumption is based on the GiB of data scanned to return a result.
The highest potential cost for a query is equal to the volume of logs within the queryâs search range times the price on your rate card.

Grail applies various optimizations to improve response time and reduce cost.
In some cases, these optimizations will identify portions of data that are not relevant to the query resultâthe price for scanning that data is discounted by 98%.

The impact of Grail scan optimizations varies based on data and query attributes.
It may evolve as Dynatrace continues to improve Grail query intelligence.

## Track your consumption

This section describes the different Dynatrace tools that you can use to track consumption and costs.

### Track your consumption with Metrics

Dynatrace provides a built-in usage metric that helps you understand and analyze your organization's consumption of Log Management & Analytics - Query.
To use this metric, in Data Explorer, enter `DPS` in the **Search** field.

Log Management & Analytics - Query
:   Key: `builtin:billing.log.query.usage`

    Dimension: Byte

    Resolution: 1 hour

    Description: Number of bytes read during the execution of a DQL query, including sampled data.

Example metric usage: monitor the total number of bytes scanned in hourly intervals

You can monitor the total scanned bytes for [Query](#query) in hourly intervals for any selected timeframe using the metric `builtin:billing.log.query.usage`.

The example below shows usage aggregated in 1-hour intervals between 2023-09-04 and 2023-09-11 (last 7 days).

![Log Management & Analytics - Query](https://dt-cdn.net/images/image034-806-25e7da895d.png)

### Track your consumption with DQL queries

Example metric usage: monitor the total number of gibibytes scanned

The following DQL query provides an overview of total [Query](#query) usage in gibibytes scanned:

```
fetch dt.system.events



| filter event.kind == "BILLING_USAGE_EVENT"



| filter event.type == "Log Management & Analytics - Query"



| dedup event.id



| summarize {



data_read_bytes = sum(billed_bytes)



}, by: {



startHour = bin(timestamp, 1d)



}
```

The example below shows the daily query usage visualized in a line chart for the last 30 days:

![Retain with included Queries (LMA)](https://dt-cdn.net/images/image-5-screenshot-2024-10-17-at-15-19-09-1243-832a39ebb6.png)

### Track your consumption and costs in Account Management

You can also view usage metrics in Account Management.
Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **Subscription** > **Overview** > **Cost and usage details** > **Usage summary** and select the **Log Management & Analytics - Query** capability.

### Track your consumption and costs via API

You can query metrics via the [Environment API - Metrics API v2](/docs/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

## Related topics

* [Log Analytics (DPS)](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.")
* [What is Dynatrace Grail?](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [License Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)


---


## Source: log-analytics.md


---
title: Log Analytics (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/log-analytics
scraped: 2026-02-15T21:12:13.906941
---

# Log Analytics (DPS)

# Log Analytics (DPS)

* Latest Dynatrace
* Overview
* 10-min read
* Updated on Nov 25, 2025

This page describes log observability capabilities and the features that they provide with a DPS subscription.

For information about how usage of a specific capability translates to consumption of your DPS license commit, see

* [Log - Ingest & Process](/docs/license/capabilities/log-analytics/dps-log-ingest "Learn how your consumption of the Log Management & Analytics - Ingest & Process DPS capability is billed and charged.")
* [Log - Retain](/docs/license/capabilities/log-analytics/dps-log-retain "Learn how your consumption of the Log Management & Analytics - Retain DPS capability is billed and charged.")
* [Log - Query](/docs/license/capabilities/log-analytics/dps-log-query "Learn how your consumption of the Log Management & Analytics - Query DPS capability is billed and charged.")
* [Log - Retain with Included Queries](/docs/license/capabilities/log-analytics/dps-log-retain-included "Learn how your consumption of the Log Management & Analytics - Retain with Included Queries DPS capability is billed and charged.")

Dynatrace offers

* A usage-based model, with Log - Retain and Log - Query charged separately.
* Retain with Included Queries.

## Usage-based model

In the usage-based model, Log - Retain and Log - Query are charged separately.

In this case, you pay for each query.
This is ideal if you have historical data that you do not access frequently.

## Log - Ingest & Process feature overview

What's included with the Ingest & Process data-usage dimension?

| Concept | Explanation |
| --- | --- |
| Data delivery | Delivery of log data via OneAgent or Log ingestion API (via ActiveGate) |
| Topology enrichment | Enrichment of log events with data source and topology metadata |
| Data transformation | - Add, edit, or drop any log attribute - Perform mathematical transformations on numerical values (for example, creating new attributes based on calculations of existing attributes) - Mask sensitive data by replacing either the whole log record, one specific log record attribute, or certain text with a masked string - Extract business, infrastructure, application, or other data from raw logs. This can be a single character, string, number, array of values, or other. Extracted data can be turned into a new attribute allowing additional querying and filtering. Metrics can be created from newly extracted attributes (see Conversion to time series below) |
| Data-retention control | - Filter and exclude incoming logs based on content, topology, or metadata (filtering generates usage for Ingest & Process, but not for Retain) - Manage data retention periods of incoming logs based on data-retention rules |
| Conversion to time series | Create metrics from log records or attributes (note that creating custom metrics generates additional consumption as described here) |

Apply the following calculation to determine your consumption for the Ingest & Process data-usage dimension:

`consumption = (number of GiBs ingested) Ã (GiB price as per your rate card)`

Data enrichment and processing can increase your data volume significantly.
Depending on the source of the data, the technology, the attributes, and metadata added during processing, the total data volume after processing can increase by a factor of 2 or more.

Dynatrace reserves the right to work with customers to adjust or disable parsing rules, processors, or pipelines that are experiencing service degradation.

## Log - Retain feature overview

Here's what's included with the Retain data-usage dimension:

| Concept | Explanation |
| --- | --- |
| Data availability | Retained data is accessible for analysis and querying until the end of the retention period. |
| Retention periods | Choose a desired retention period. For log buckets, the available retention period ranges from 1 day to 10 years.  Metrics retention is defined at the bucket level, ensuring tailored retention periods for specific metrics. |

## Log - Query feature overview

Query data usage occurs when:

* Executing DQL queries in Notebooks, Workflows, Custom Apps and via API
* Dashboard tiles that are based on log data trigger the execution of DQL queries on refresh and include sampled data
* Submitting DQL queries by clicking the âRun queryâ button (for example, in the Logs & Events viewer in simple and advanced mode or on unified analysis pages)

What's included with the Query data-usage dimension?

| Concept | Explanation |
| --- | --- |
| On-read parsing | Use DQL to query historical logs in storage and extract business, infrastructure, or other data across any timeframe, and use extracted data for follow-up analysis |
| Aggregation | Perform aggregation, summarization, or statistical analysis of data in logs across specific timeframes or time patterns (for example, data occurrences in 30-second or 10-minute intervals) |
| Reporting | Create reports or summaries with customized fields (columns) by adding, modifying, or dropping existing log attributes |
| Context | Use DQL to analyze log data in context with relevant data on the Dynatrace platform, for example, user sessions or distributed traces |

## Log - Retain with Included Queries feature overview

Dynatrace version 1.316+

In the Retain with Included Queries model, retained log data within a configured time period can be queried free of charge, as often as you want.
This is ideal if you frequently access recent data, or look at highly predictable consumption patterns.

Customers can split a log bucketâs retention period into two parts:

* An Included Queries retention period (10â35 days of data retention).
* The overall retention period (up to 10 years) that follows the usage-based [Retain](#retain) and [Query](#query) model.

With the Retain with Included Queries model, Log - Ingest & Process consumption continues to be calculated separately and is charged only once for the initial ingestion into your tenant.

Customers who select the Retain with Included Queries option in the bucket configuration are not charged for those queries executed within the scope of the **Included Queries** retention period. (The retention period is defined on a log bucket within the Dynatrace Platform.)
For queries that are executed and include a scope outside of the Included Queries period, only these logs outside of the Retain with Included Queries are billed individually with the usage based [Log - Query](#query) model.

`Included query usage per day = (GiB of logs within the defined Included Queries retention period) Ã 15`

In any 24-hour period, customers with this licensing option activated are entitled to run queries with an aggregate scanned-GiB volume of up to 15 times the volume of log data that is retained within the **Included Queries** timeframe at that time.
Example: You ingest and retain 1 GiB per day, and set the Included Queries retention period to 10 days. Your query quota is 150 GiB per 24 hours (1 GiB x 10 Days x 15 Multiplier = 150 GiB).

Using this formula, we have included sufficient queries for the majority of customers.
In case you exceed the included query volume, the Dynatrace team will reach out and help you to evaluate and optimize query consumption.
Alternatively, if the Retain with Included Query option does not meet your use case and requirements, you can reconfigure a bucket at any time to use individually billed on-demand queries without losing data.

## Related topics

* [Log Analytics](/docs/analyze-explore-automate/logs "Log Management and Analytics provides a unified approach to controlling and studying your log data in Dynatrace.")
* [What is Dynatrace Grail?](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more.")
* [License Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)


---


## Source: metrics.md


---
title: Metrics powered by Grail overview (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/metrics
scraped: 2026-02-15T21:17:35.356793
---

# Metrics powered by Grail overview (DPS)

# Metrics powered by Grail overview (DPS)

* Latest Dynatrace
* Overview
* 7-min read
* Updated on Jan 26, 2026

For information about how usage of a specific capability translates to consumption of your DPS license commit, see

* [Metrics - Ingest & Process](/docs/license/capabilities/metrics/dps-metrics-ingest "Learn how your consumption of the Metrics - Ingest & Process DPS capability is billed and charged.")
* [Metrics - Retain](/docs/license/capabilities/metrics/dps-metrics-retain "Learn how your consumption of the Metrics - Retain DPS capability is billed and charged.")
* [Metrics - Query](/docs/license/capabilities/metrics/dps-metrics-query "Learn how your consumption of the Metrics - Query DPS capability is billed and charged.")

## Metrics - Ingest & Process feature overview

Here's what's included with the Ingest & Process data-usage dimension:

Concept

Explanation

Data delivery

Delivery of metrics via OneAgent, extensions or ingest API

Topology enrichment

Enrichment of metrics with data source and topology metadata

Data transformation

* Rollup of data to reduced granularity to optimize queries for longer timeframes
* Use of efficient data structures to derive metrics from high volume spans like service response time metrics

Data-retention control

Manage data retention period of incoming metrics based on bucket assignment rules

## Metrics - Retain feature overview

Here's what's included with the Retain data-usage dimension:

Concept

Explanation

Data availability

Retained data is accessible for analysis and querying until the end of the retention period.
Metrics retention is defined at the bucket level, ensuring tailored retention periods for specific metrics.

Retention periods

Choose a desired retention period.
For the default metrics bucket, the available retention period ranges from 15 months (462 days) to 10 years (3,657 days).

## Metrics - Query feature overview

Here's what's included with the Query data-usage dimension:

| Concept | Explanation |
| --- | --- |
| DQL query execution | A [DQL query](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") scans and fetches data that is stored in Grail. Querying metrics using the `timeseries` command is always included. |
| App usage | DQL queries can be executed by:  - Apps such as Notebooks **Notebooks**, Dashboards **Dashboards**, Workflows **Workflows**, and Anomaly Detection - new **Anomaly Detection**. - Dashboard tiles that are based on metrics trigger the execution of DQL queries on refresh - Custom apps - The Dynatrace API |

## Related topics

* [Metrics](/docs/analyze-explore-automate/metrics "Metrics powered by Grail offer a comprehensive solution to manage your metrics data, in integration with logs, spans, and events, providing a unified approach to data analysis.")
* [What is Dynatrace Grail?](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more.")
* [License Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)


---


## Source: traces.md


---
title: Traces powered by Grail overview (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/traces
scraped: 2026-02-15T21:15:01.480316
---

# Traces powered by Grail overview (DPS)

# Traces powered by Grail overview (DPS)

* Latest Dynatrace
* Overview
* 9-min read
* Updated on Jun 23, 2025

The Traces powered by Grail DPS capability gives customers access to:

* Distributed trace ingestion for OpenTelemetry via the OTLP API.
* Distributed trace ingestion for serverless functions.
* Extended trace ingestion for [Full-Stack Monitoring](/docs/license/capabilities/app-infra-observability "Learn about the different Application & Infrastructure Observability options that are available with a Dynatrace Platform Subscription (DPS) license.") beyond the [included trace data volume](/docs/license/capabilities/app-infra-observability/full-stack-monitoring#full-stack-traces "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.").
* Extended trace data retention for up to 10 years.
* Advanced tracing analytics in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**, and via API.

This page describes the different tracing capabilities and the features that they provide with a DPS subscription.

For information about how usage of a specific capability translates to consumption of your DPS license commit, see

* [Traces - Ingest & Process](/docs/license/capabilities/traces/dps-traces-ingest "Learn how your consumption of the Traces - Ingest & Process DPS capability is billed and charged.")
* [Traces - Retain](/docs/license/capabilities/traces/dps-traces-retain "Learn how your consumption of the Traces - Retain DPS capability is billed and charged.")
* [Traces - Query](/docs/license/capabilities/traces/dps-traces-query "Learn how your consumption of the Traces - Query DPS capability is billed and charged.")

## Traces - Ingest feature overview

Ingest & Process replaces the platform extensions [Custom Traces Classic](/docs/license/capabilities/platform-extensions/custom-traces-classic "Learn how your consumption of the Dynatrace Custom Traces Classic DPS capability is billed and charged.") and [Serverless Functions Classic](/docs/license/capabilities/platform-extensions/serverless-functions-classic "Learn how your consumption of the Dynatrace Serverless Functions Classic DPS capability is billed and charged.").
They cannot be used simultaneously.

Ingest & Process usage occurs when:

| Concept | Explanation |
| --- | --- |
| Data ingest | Distributed trace data ingested from the following sources is charged as [Ingest & Process](#trace-ingest-usage):  - Via the OpenTelemetry [OTLP Trace Ingest API](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") from non-Full-Stack sources. - Via [serverless functions](/docs/discover-dynatrace/get-started/serverless-monitoring "Serverless observability with Dynatrace"). - Extended trace ingest for [Full-Stack Monitoring](/docs/license/capabilities/app-infra-observability/full-stack-monitoring "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.") (if the customer [explicitly requests extended trace ingest](/docs/license/capabilities/app-infra-observability/full-stack-monitoring#extend-trace-ingest "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.")).  Enrichment of spans with additional metadata at the source, such as [Kubernetes metadata](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment "Guides for telemetry enrichment on Kubernetes"), increase the size of ingested data that is charged as [Ingest & Process](#trace-ingest-usage). |
| Data processing via OpenPipeline | - Data processing via OpenPipeline is included in [Traces â Ingest & Process](#trace-ingest-usage). However, it increases the size of span data that is charged as [Traces â Retain](#trace-retain-usage). - Topology enrichment based on Dynatrace entities (`dt.entity.*` entity types) does not increase the billable span size or [Traces â Ingest & Process](#trace-ingest-usage) consumption. - Custom metrics are created from span data and are charged as [Metrics - Ingest & Process](/docs/license/capabilities/metrics/dps-metrics-ingest "Learn how your consumption of the Metrics - Ingest & Process DPS capability is billed and charged."). These are Grail metric keys and therefore are available only in latest Dynatrace. |

Dynatrace reserves the right to work with customers to adjust or disable parsing rules, processors, or pipelines that experience service degradation.

## Traces - Retain feature overview

Retain usage occurs when:

| Concept | Explanation |
| --- | --- |
| Data availability | Retained data is accessible for analysis and querying until the end of the retention period (with limitations described in the note below this table). |
| Retention period | Choose the desired retention period. For trace data, the available [retention period](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods "Check retention times for various data types.") ranges from 10 days to 10 years. Trace retention is defined at the bucket level, allowing tailored retention periods for specific traces. Retain calculation is independent of the trace ingestion source, whether Full-Stack, Mainframe, or Ingest & Process. The first 10 days of retention are always included. |
| Topology enrichment | Spans are enriched and processed in OpenPipeline. Enriched data (including Topology enrichment and Data processing as described in [Ingest & Process](#trace-ingest-usage)) is the basis for Retain usage for data that is stored longer than the included 10 days. |
| Data processing | Services, endpoints, and failures are detected based on span data. |
| Data storage control | Spans are filtered or excluded based on content, topology, or metadata. They are routed to a dedicated bucket. |

For Traces - Retain, data availability in certain apps is limited:

* ![Distributed Traces Classic](https://dt-cdn.net/images/distributed-traces-classic-7197cdacfb.svg "Distributed Traces Classic") **Distributed Traces Classic** provides access to only the first 10 days of retained data.
  This app is superseded by ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**.
* ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic** provides access only to the first 10 days of retained data.
  This app will be superseded by ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**.
* ![Multidimensional Analysis](https://dt-cdn.net/images/multidimensional-analysis-512-3aed148cfe.png "Multidimensional Analysis") **Multidimensional Analysis** provides access only to the first 35 days of retained data.
  This app will be superseded by ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.

## Traces - Query feature overview

Query usage occurs when:

| Concept | Explanation |
| --- | --- |
| DQL query execution | A [DQL query](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") scans and fetches data that is stored in Grail. Spans can be joined and analyzed in context with other signals on the Dynatrace platform, such as logs, events, or metrics. |
| App usage | DQL queries can be executed by:  - Apps such as Notebooks **Notebooks**, Dashboards **Dashboards**, Workflows **Workflows**, and Anomaly Detection - new **Anomaly Detection**. (Note: Distributed Tracing **Distributed Tracing** and Services **Services** don't consume any Query usage.) - Dashboard tiles that are based on span data trigger the execution of DQL queries on refresh - Custom apps - The Dynatrace API |

The usage of ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** and ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** is included with Dynatrace.
No query consumption is generated by these apps.

When other data types are also read in a query, this can result in consumption of the corresponding capability, such as [Log - Query](/docs/license/capabilities/log-analytics/dps-log-query "Learn how your consumption of the Log Management & Analytics - Query DPS capability is billed and charged.").

## Related topics

* [Distributed Tracing](/docs/observe/application-observability/distributed-tracing "Trace and analyze in real time highly distributed systems with Grail.")
* [Traces](/docs/semantic-dictionary/model/trace "Get to know the Semantic Dictionary models related to traces.")
* [License Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)


---
