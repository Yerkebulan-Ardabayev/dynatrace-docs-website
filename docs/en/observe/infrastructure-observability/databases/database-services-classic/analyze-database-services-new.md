---
title: Analyze database services (new page)
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/databases/database-services-classic/analyze-database-services-new
scraped: 2026-02-24T21:30:07.703878
---

# Analyze database services (new page)

# Analyze database services (new page)

* Explanation
* 5-min read
* Published Jun 20, 2023

We have redesigned the database overview page.

* This documentation describes the new design.
* If you want to revert to the classic database page, on the database overview page select **More** (**â¦**) > **Return to classic page** and then refer to the [documentation for the classic database page](/docs/observe/infrastructure-observability/databases/database-services-classic/analyze-database-services "Analyze your database services with Dynatrace (classic page).").

All databases detected by Dynatrace in your environment are displayed on the **Databases** page. You can analyze each database and drill down to code-level information.

How to get there:

1. Go to ![Databases Services Classic](https://dt-cdn.net/images/databases-512-6aa6fff194.png "Databases Services Classic") **Database Services Classic**.
2. Select a database name in the list to go to that database's overview page.

Each **Database** page lists the most important information for that database.

![Database overview | Unified analysis](https://dt-cdn.net/images/database-ua-overview-3502-2a520ae771.png)

All relevant database metrics are shown on a single page, which is divided into several logical sections. Other panes of the database overview page show database performance and serve as entry points to deeper analysis.

## Notifications bar

The database notifications bar gives you a quick overview of the database state. Select a notification item to display more information.

### Properties and tags

Select **Properties and tags** on the notifications bar to display the **Properties and tags** panel, which displays metadata about the selected database:

* **Tags** lists tags currently applied to the database.  
  Select **Add Tag** to add a tag to the database metadata.
* **Properties** lists various database properties, such as application name, database type, technologies, and management zones.

### Problems

* On the notifications bar, **Problems** indicates active and closed problems related to the selected database.
* Select **Problems** on the notifications bar to display the **Problems** panel, which lists the problems.

  + Select a problem to display details.
  + Select **Go to problems** to go to the [Problems](/docs/dynatrace-intelligence "Get familiar with the capabilities of Dynatrace Intelligence.") page filtered by the selected database.

### SLOs

* On the notifications bar, **SLOs** indicates the current number of [SLOs](/docs/deliver/service-level-objectives-classic "Monitor and alert on service-level objectives with Dynatrace in Service-Level Objectives Classic.") related to the selected database.
* Select **SLOs** on the notifications bar to display the **Service-level objectives** panel, which lists SLOs that are directly or indirectly connected to the database.

#### Directly connected SLOs

* An SLO is directly connected to a service when the [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") of an SLO meets the following criteria:

  + The entity type is set to `"DATABASE"`.
  + The entity ID is set to the database ID.
* To see only SLOs that are directly connected to the database, make sure that **Show only directly connected SLOs** is turned on.

#### Indirectly connected SLOs

* An SLO isn't directly connected to a database when, in the [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") of an SLO, no entity ID is provided.

  Example: When generic values such as `type("DATABASE"),tag("slo")` are provided, the query results in all SLOs for all databases, including the current database.
* To see SLOs that are not directly connected to the database, turn off **Show only directly connected SLOs**.

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

### Database availability

Select **Database availability** on the notifications bar to display a chart summarizing any detected availability issue for the database in the selected timeframe.

### Owners

Select **Owners** on the notifications bar to display the **Ownership** panel, which lists [owners](/docs/deliver/ownership "Map team ownership to monitored entities for better collaboration, task assignment, incident and vulnerability response, and service-level management.") of the selected database.

* Select  to learn more about the current ownership.
* To add an ownership tag, select **Add Ownership tag**.

## Performance

### Database service overview

You can configure the **Database service overview** section to focus on various metrics of the database performance. For each metric, you can select **More** (**â¦**) and

* Analyze the metric in Data Explorer.
* Create a metric event.
* Pin the metric to a classic dashboard. For details, see [Pin tiles to your dashboard](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Learn to pin tiles to your dashboards.").

### Topology

In the **Topology** section, you can learn

* The services that are calling the database and the services that are called by the database.  
  Select **Related services** to understand the service relation. Expand **Details** to view a chart of the respective service metrics. To proceed with your analysis, you can select [**View backtrace**](/docs/observe/application-observability/services-classic/service-backtrace "Trace the sequence of service calls all the way back up to the browser click that triggered the sequence of calls.").
* The processes and hosts on which the service is running.  
  Expand **Details** to view a chart of the respective process metrics. Select the name of the process to analyze it.

### Statement types

Contains an overview of statement types found for the database in the selected timeframe.

* Expand **Details** to view a chart of the respective statement.
* Select the name of a statement type to analyze the database statements filtered by the selected type.
* Select **View all statements** to analyze all statements for the database.

### Distributed traces

The **Distributed traces** section provides an overview of the most recent traces for the selected timeframe. Select **Full search** to go to the [distributed traces overview for the database](/docs/observe/application-observability/distributed-traces/analysis/get-started "Get started with distributed trace analysis in Dynatrace.").

### Events

Lists [events](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Gain an understanding of the Events section on each host, process, and service overview page.") that affect the database in the current timeframe.

### Related logs

Lists [logs](/docs/analyze-explore-automate/logs "Log Management and Analytics provides a unified approach to controlling and studying your log data in Dynatrace.") related to the database in the current timeframe.

* To analyze all the logs for the related database, select **Go to logs** .
* To analyze a specific log, expand **Details**. If a trace or a user session is found for the log line, you can directly access it from this view.

## Related topics

* [Unified analysis pages](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis "Extend the Dynatrace web UI using entity-tailored unified analysis pages.")