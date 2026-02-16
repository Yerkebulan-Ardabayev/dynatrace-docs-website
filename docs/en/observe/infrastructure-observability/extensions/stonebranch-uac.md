---
title: Stonebranch Universal Automation Center extension
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/extensions/stonebranch-uac
scraped: 2026-02-16T21:26:44.934793
---

# Stonebranch Universal Automation Center extension

# Stonebranch Universal Automation Center extension

* Latest Dynatrace
* Extension
* Published Dec 12, 2025

Monitor Stonebranch Universal Automation Center (UAC) via OpenTelemetry.

## Get started

### Overview

This extension collects UAC metrics via Dynatrace ActiveGate and turns them into a UC-aware view inside Dynatrace. It discovers Universal Controllers, OMS servers, Universal Agents, workflows, and business services from metric labels and maps them into a topology with dedicated Unified Analysis Screens and example dashboards.

IT Ops, SREs, and platform teams can use this extension to:

* Track task execution and workflow outcomes.
* Monitor controller, JVM, and process health.
* Watch UAC license consumption and capacity limits.
* Receive UAC-specific alerts when OMS, agents, or licenses are in trouble.

All of this is done through metric scrapingâno custom scripting is required.

### Use cases

* Overview of your entire UAC environment: Get an overview of one or more Universal Controllers with an all-in-one view inside of Dynatrace.
* Controller and OMS health monitoring: Detect controller node or OMS issues early using status and connection metrics.
* Automation workload visibility: Monitor execution counts, active instances, and outcome distributions across workflows and task types.
* License and capacity management: Track usage of agents, nodes, executions, and tasks against license quotas to avoid overages.
* Workflow- and agent-centric views: Use workflow and Universal Agent entity screens to understand where tasks run, how they perform, and which business services they belong to.
* Integrated troubleshooting inside Dynatrace: Use dashboards, entity screens, and alerts to quickly isolate whether a problem is in the automation logic, the controller, the agents, or the underlying infrastructure.

### Compatibility information

* Universal Controller: 7.9.0.0+
* Universal Agent: 7.9.0.0+

## Activation and setup

1. Install and activate the extension from the Dynatrace Hub.
2. Configure the metric endpoint. Point the extension to your Universal Controller Prometheus metrics endpoint.
3. Configure authentication. Make sure that the UC user (or the equivalent service user) has the `ops_service` role.
4. recommended Enable workflow and business context labels. For deeper insights into workflows, agents, and business services, configure additional labels in `uc.properties` so they appear in metrics such as `uc_history_total`.

   For example

   * `task_name` (workflow/task name)
   * `security_business_services` (business service names)
   * `agent_id`
   * `cluster_node_id`

   These labels are used in topology mapping (Workflows, Business Services, Universal Agents), workflow/agent dashboards, and entity screens.

   For more details, see:

   * The Stonebranch documentation for properties: [Propertiesï»¿](https://stonebranchdocs.atlassian.net/wiki/spaces/UC79/pages/1614542260/Properties).
   * Implementation details and examples: [Dynatrace Observability for UAC â Implementation Guideï»¿](https://stonebranchdocs.atlassian.net/wiki/spaces/UE/pages/1949892609/Dynatrace+Observability+for+UAC+-+Implementation+Guide).

## Details

### Metric ingestion

The extension uses Dynatrace ActiveGate to scrape Prometheus-format metrics from one or more Universal Controllers. Metrics are grouped into feature sets, including

* Universal Controller metrics

  + Workload and history
  + Database connection pool
* Standard process metrics

  These are based on metrics like `process_cpu_seconds_total`, `process_virtual_memory_bytes`.
  Examples include

  + CPU time
  + Virtual and resident memory
  + Process start time
  + Open/max file descriptors
* JVM metrics

  + Heap and non-heap memory usage and pools
  + Buffer pool usage and capacity
  + GC collection time
  + Thread counts and states
  + Class loading statistics
  + JVM runtime info
* Universal Agent and OMS metrics

  + Agent Status
  + OMS Status
  + Server Session
  + Last Connection Time
* License and capacity metrics

  + Distributed agents currently used
  + Maximum number of distributed agents that can be used
  + z/OS agents used / max
  + Cluster nodes used / max
  + Monthly executions used / max
  + Task definitions used / max
  + `uc_monthly_executions` for current-month execution count

These metrics provide a high-level view of the UAC.

### Topology and entity model

The extension maps metric dimensions into Dynatrace entities and relationships, allowing you to navigate your automation landscape visually. For example, you can navigate from a controller to the workflows running on it, down to the agents executing them.

Entity types

* Universal Controller
* OMS
* Workflows
* Business Services
* Universal Agent

### Unified Analysis Screens and dashboards

The extension ships with

* Universal Controller Overview dashboard for high-level monitoring
* Unified Analysis Screens for

  + Universal Controller
  + Workflow
  + Universal Agent

Example views include

* UC-wide history distribution by task type and task name
* Active task instances by status
* Monthly execution counts
* Workflow instance status and business service grouping
* Universal Agent task distributions by type and status

### Built-in alerts

The extension includes predefined alert configurations, which are saved as alert templates. These are available for

* OMS server availability
* UC cluster node availability
* Database connection pool health
* Various alerts relating to the UC license

These alerts are based purely on metrics and can be adjusted or extended in Dynatrace as needed.

### Licensing and cost

There is no charge to use the extension. You are only charged for the data that the extension ingests. The license consumption details depend on which licensing model you're using. This can either be [Dynatrace classic licensing](/docs/license/monitoring-consumption-classic "Understand how Dynatrace monitoring consumption is calculated for classic licensing.") or the [Dynatrace Platform Subscription (DPS)](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") model.

#### Metrics

License consumption is based on the number of metric data points ingested. A rough annual estimate, assuming all feature sets are enabled, is shown below.

```
(



(



( 1 * number of UC Cluster Nodes )



+ ( 46 * number of Universal Controllers )



+ ( 1 * number of OMS )



+ ( 4 * number of Universal Agents )



+ ( 5 * number of unique Task Names )



)



) * 60 minutes * 24 hours * 365 days per year
```

#### Classic licensing

In the Dynatrace classic licensing model, metric ingestion consumes [Davis Data Units (DDUs)](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).") at the rate of .001 DDUs per metric data point.
To estimate annual DDU usage, take the result of the above formula for annual data points and multiply it by .001.

## FAQ

Does this extension collect traces or logs?

No. This extension focuses on metrics-based monitoring and topology. Traces and logs can be added separately using UAC's OpenTelemetry or log forwarding capabilities.

Can I customize dashboards and alerts?

Yes. The shipped examples and alert templates are meant as a starting point. You can clone and adapt them in Dynatrace.

Why are some tiles not working?

If some tiles do not show data, check if the user has access to read the metrics endpoint of the Universal Controller or if you have the optional metrics enabled in your `uc.properties`.