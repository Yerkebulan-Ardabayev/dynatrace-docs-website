---
title: Service analysis
source: https://www.dynatrace.com/docs/observe/application-observability/services-classic/service-analysis-new
scraped: 2026-02-22T21:23:54.475985
---

# Service analysis

# Service analysis

* How-to guide
* 6-min read
* Updated on Jun 13, 2025

This topic is about the ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic** page and is a redesign of the classic page. Check out the [![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** app](/docs/observe/application-observability/services/services-app "Maintain centralized control over service health, performance, and resources with the Services app.") for the latest experience.

All services detected by Dynatrace in your environment are displayed on the ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic** page. You can analyze each service and drill down to code-level information.

![Services list](https://dt-cdn.net/images/services-page-1504-133c9f1b72.png)

How to get there:

1. Go to ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic**.
2. Select a service name in the list to go to that service's overview page.

![Service overview with Unified Analysis new design](https://dt-cdn.net/images/service-overview-new-design-1768-fe1ab99c85.png)

Each **Service** page lists the most important information for that service. All relevant service metrics are shown on a single page, which is divided into several logical sections. Other panes of the service overview page show service performance and serve as entry points to deeper analysis.

## Notifications bar

The service notifications bar gives you a quick overview of the service state. Select a notification item to display more information.

### Properties and tags

Select **Properties and tags** on the notifications bar to display the **Properties and tags** panel, which displays metadata about the selected service:

* **Tags** lists tags currently applied to the service.  
  Select **Add Tag** to add a tag to the service metadata.
* **Properties** lists various service properties, such as application name, service type, technologies, and management zones.

### Problems

* On the notifications bar, **Problems** indicates active and closed problems related to the selected service.
* Select **Problems** on the notifications bar to display the **Problems** panel, which lists the problems.

  + Select a problem to display details.
  + Select **Go to problems** to go to the [Problems](/docs/dynatrace-intelligence "Get familiar with the capabilities of Dynatrace Intelligence.") page filtered by the selected service.

### SLOs

* On the notifications bar, **SLOs** indicates the current number of [SLOs](/docs/deliver/service-level-objectives-classic "Monitor and alert on service-level objectives with Dynatrace in Service-Level Objectives Classic.") related to the selected service.
* Select **SLOs** on the notifications bar to display the **Service-level objectives** panel, which lists SLOs that are directly or indirectly connected to the service.

#### Directly connected SLOs

* An SLO is directly connected to a service when the [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") of an SLO meets the following criteria:

  + The entity type is set to `"SERVICE"`.
  + The entity ID is set to the service ID.
* To see only SLOs that are directly connected to the service, make sure that **Show only directly connected SLOs** is turned on.

#### Indirectly connected SLOs

* An SLO isn't directly connected to a service when, in the [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") of an SLO, no entity ID is provided.

  Example: When generic values, such as `type("SERVICE"),tag("slo")` are provided, the query results in all SLOs for all services, including the current service.
* To see SLOs that are not directly connected to the service, turn off **Show only directly connected SLOs**.

#### Options

* Expand **Details** to view a chart of the respective SLO metrics.
* In **Actions**, select

  + **View in Data Explorer** to [see SLO metrics in Data Explorer](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#explorer "Create, configure, and monitor service-level objectives with Dynatrace.").
  + **Pin to Dashboard** to [pin the SLO to your dashboard](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#dash "Create, configure, and monitor service-level objectives with Dynatrace.").
  + **SLO definition** to edit the SLO in **Service-level objective definitions**.
  + **Clone** to [clone the SLO](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#clone "Create, configure, and monitor service-level objectives with Dynatrace.").
  + **Create alert** to [create an alert for the SLO](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#alerts "Create, configure, and monitor service-level objectives with Dynatrace.").

#### No SLOs

If no SLOs are found, you can

* Select a different timeframe in the upper-right corner.

  ![Timeframe selector: menu bar](https://dt-cdn.net/images/timeframe-selector-menu-bar-264-8193110c8c.png)
* Select **Add SLO** to create an SLO in the [SLO wizard](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#wizard "Create, configure, and monitor service-level objectives with Dynatrace.").

### Owners

Select **Owners** on the notifications bar to display the **Ownership** panel, which lists [owners](/docs/deliver/ownership "Map team ownership to monitored entities for better collaboration, task assignment, incident and vulnerability response, and service-level management.") of the selected service.

* Select  to learn more about a current ownership.
* To add an ownership, select **Add a new Ownership tag**.

## Performance

### Service overview

You can configure the **Service overview** card to focus on various metrics of the service performance.

* In the **Service overview**, you can

  + See the service in Smartscape by selecting **Smartscape view** .
  + Analyze **Response time hotspots**, **Details of failures**, and method hotspots.
  + Compare service request performance indicators, such us response time, failures, CPU, and load, based on different timeframes.
* For each metric, you can select **More** (**â¦**) and

  + Analyze the metric in Data Explorer.
  + Create a metric event.
  + Pin the metric to a classic dashboard. For details, see [Pin tiles to your dashboard](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Learn to pin tiles to your dashboards.").

### Endpoints

Unified service

The **Endpoints** card offers an overview of the monitored service endpoints.

* To analyze an endpoint metrics, in the **Details** column select .
* To analyze an endpoint distributed traces, in the **Actions** column select **More** (**â¦**) > **View distributed traces**.

Data availability depends on endpoint metrics, which consume DDUs. To get started on endpoint monitoring, see [Manage endpoint monitoring](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types/unified-service#endpoint-monitoring "Define services on observability signals ingested via Trace ingest APIs.").

### Service mesh metrics

Unified service

If a service mesh is detected in your application, service mesh metrics are displayed for the related service. [ISTIO logs and metrics](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-istio-metrics "Istio metric ingestion and topology detection") are enriched with service mesh ID, putting data into context. Note that service mesh metrics are created from ingested service mesh traces.

### Key requests

The **Key requests** card offers an overview of the key requests found for the service in the selected timeframe. You can quickly access analysis for other requests related to the services such as:

* [**View all requests**](/docs/observe/application-observability/services-classic#charts "Learn about Dynatrace's classic service monitoring")
* [**Top web requests**](/docs/observe/application-observability/multidimensional-analysis/top-web-requests "Learn how to analyze all web requests across all of your services using Dynatrace.")
* [**View outliers**](/docs/observe/application-observability/services-classic/response-time-distribution-and-outlier-analysis#outlier-analysis "Gain insights into the distribution of response times across all requests, including those that are either unusually high or unusually low.")

### Topology



In the **Topology** card, you can learn

* Which services are calling and which are called by the service.  
  Select **Related services** to understand the service relation. Expand **Details** to view a chart of the respective service metrics. You can quickly access further analysis options such as [**View backtrace**](/docs/observe/application-observability/services-classic/service-backtrace "Trace the sequence of service calls all the way back up to the browser click that triggered the sequence of calls.") and [**Service flow**](/docs/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.").
* On which processes and hosts the service is running on.  
  Expand **Details** to view a chart of the respective process metrics. Select the name of the process to analyze it deeper.
* Which HTTP monitors and (mobile) applications are calling the service.  
  Select the name of a calling entity to analyze it deeper.

![Topology - Service overview](https://dt-cdn.net/images/topology-services-2886-fc9dda7f82.png)

### Distributed traces

The **Distributed traces** card provides an overview of the most recent traces, depending on the selected timeframe. Select **Full search** to directly access the [distributed traces overview for the service](/docs/observe/application-observability/distributed-traces/analysis/get-started "Get started with distributed trace analysis in Dynatrace.").

### Events

Contains a list of [events](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Gain an understanding of the Events section on each host, process, and service overview page.") that affect the service in the current timeframe.

### Related logs

Contains a list of [logs](/docs/analyze-explore-automate/logs "Log Management and Analytics provides a unified approach to controlling and studying your log data in Dynatrace.") related to the service in the current timeframe.

* To analyze all the logs for the related service, select **Go to logs** .
* To analyze a specific log, expand **Details**. If a trace or a user session is found for the log line, you can directly access it from this view.

## Related topics

* [Unified analysis pages](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis "Extend the Dynatrace web UI using entity-tailored unified analysis pages.")