---
title: Databases app
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/databases/database-app
scraped: 2026-02-22T21:10:02.875320
---

# Databases app

# Databases app

* Latest Dynatrace
* App
* 4-min read
* Updated on Jan 28, 2026

The Dynatrace ![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") **Databases** enables you to monitor, analyze, and optimize database environments with clarity and control. It offers detailed insights into performance, health, and configuration, helping you identify issues early and maintain reliable operations.

By integrating with Dynatrace observability ecosystem, ![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") **Databases** connects database metrics with application and infrastructure data, supporting faster troubleshooting and smarter decision-making.

## Prerequisites

Before you begin, ensure the following:

* ActiveGate configuration

  + Assign one or more [ActiveGate group](/docs/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.") to connect to the target database servers remotely.
* Required components

  + For databases requiring additional components (for example, JDBC drivers), install them on all designated ActiveGates according to the [extension guidelines](/docs/ingest-from/extensions/concepts#ag "Learn more about the concept of Dynatrace Extensions.").
* Network and [permissions](/docs/observe/infrastructure-observability/databases/database-app#permissions "The Databases app gives you an overview of all your Extensions Framework 2.0-monitored databases.")

  + Validate network connectivity and firewall rules for each database type. ActiveGate should be able to establish a direct network connection to the database host.
  + Create a monitoring user account with appropriate permissions (for example, access to system views, performance metrics, and schemas).

### Permissions

The following table describes the required permissions.

Permission

Description

davis:analyzers:execute

Execute Davis analyzer for entity problems

settings:objects:read

Read settings objects from settings V2 for Ownership and SLOs

settings:objects:write

Write settings objects from settings V2 for Ownership and SLOs

state:user-app-states:read

Read user app state

state:user-app-states:write

Store UI state

storage:buckets:read

Read buckets from Grail buckets

storage:entities:read

Read entities from Grail

storage:events:read

Read events from Grail

storage:logs:read

Read logs from Grail

storage:metrics:read

Read metrics from Grail

10

rows per page

Page

1

of 1

### Installation steps

1. Install ![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") **Databases** from the Dynatrace  **Hub**.
2. Configure the app to monitor supported database instances. For vendor-specific setup instructions, see [Get started with database monitoring](/docs/observe/infrastructure-observability/databases/database-app/get-started "Set up database monitoring and learn how to extend Dynatrace Databases monitoring.").
3. Add the required monitoring configurations (for example, credentials, endpoints) for each instance.

## Get started

Use ![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") **Databases** to monitor, analyze, and optimize your database environments. The app integrates with the Dynatrace observability ecosystem and delivers actionable insights to help you ensure reliability, improve performance, and reduce downtime.

![Get an overview of your entire database fleet](https://cdn.hub.central.dynatrace.com/hub/console/drafts/171/media/DB_Overview.png)![Get an overview of what's happening across your entire database fleet](https://cdn.hub.central.dynatrace.com/hub/console/drafts/196/media/Overview_4.jpg)![See a full view of activity metrics](https://cdn.hub.central.dynatrace.com/hub/console/drafts/196/media/Activity_metrics_3.jpg)

1 of 3Get an overview of your entire database fleet

### Databases app overview

#### Centralized dashboard

The **Overview** tab provides a high-level summary of your database landscape:

* **Database health**: Visualize healthy and unhealthy database instances to identify problem areas quickly.
* **Host metrics**: Access data from hosts running OneAgent for deeper analysis of resource dependencies.

#### Explore database instances

Select the **Explorer** tab to view a list of all your monitored instances. The **Database instances** table displays these instances.

* **Health**: Unified statuses and Davis-detected problems help you quickly identify critical issues.
* **Utilization**: Metrics such as CPU usage, memory consumption, user calls, and active sessions provide insights into resource efficiency.
* **Host details**: Drill down into host metrics or access the **Infrastructure and Operations** view for a comprehensive analysis.

##### Entity details panel

For an overview of a single instance, do one of the following:

* Go to the **Explorer** tab and select the instance name in the **Database instances** table.
* In the rightmost column, select the  (**Statement performance**) icon.

From here, you can access the **Entity details** panel and analyze all the metrics collected by the extension.

#### Statement performance analysis

Analyze resource-intensive queries to optimize performance:

* Filter queries by time, CPU, disk, or wait metrics.
* Access execution plans to understand query interactions and identify optimization opportunities.

##### Statement performance

If the extension provides related information, you can display **Statement performance analysis** to track the performance of statements that consume the most resources.

To focus your analysis:

* Set the **Filter statements** to a search string.
* Set **Contextual analysis** to the context of predefined metrics (**Time**, **CPU**, **Disk**, or **Waits**), or select the  column settings icon to customize columns and adapt the context to your needs.
* Select the **Request execution plan** to understand how the database executes the statement for optimization.

### Advanced features

The app helps you proactively address potential issues before they affect operations, reduce downtime, and improve reliability.

* Detect and resolve anomalies that use AI-powered analysis.
* Pinpoint root causes of performance degradation or failures.
* Receive actionable recommendations for query and configuration optimizations.

### Benefits

![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") **Databases** helps you maintain reliable, efficient, and optimized database operations. The app addresses issues proactively and provides actionable insights, allowing you to focus on strategic priorities.

* **Minimize downtime:** Detect and resolve issues before they impact operations.
* **Improve performance:** Optimize queries, schemas, and configurations for better efficiency.
* **Ensure reliability:** Support stable database operations across diverse environments.
* **Enhance productivity:** Automate observability tasks and reduce manual troubleshooting.

## Concepts

### Health score

A predefined, non-configurable metric evaluates availability, performance, configuration, and resource usage.

#### Health alerts and warning signals

Health alerts and warning signals help you monitor your infrastructure by providing clear, actionable insights. These features reduce the noise from infrastructure issues and improve alerting capabilities, so you can focus on what matters most. This is achieved through better categorization of detected malfunctions.

* For critical events, a Health alert is raised, triggering a [Dynatrace Problems](/docs/dynatrace-intelligence/davis-problems-app "Use the Problems app to quickly get to the root cause of incidents in your environment.") investigation.
* For non-critical situations, a Warning signal informs you of a potential challenge.

You can set up the ready-made health alerts and warning signals through the **Alert templates** tab.

In the **Alert templates** tab, we provide pre-defined alert templates for the most popular DB vendors. Easily create a new alert by selecting a template and **New Alert**. Next, either customize the alert in the **Anomaly Detection** wizard or create the alert with one step.

Find all the custom alerts, more details of capabilities, and limits in [Anomaly Detection](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.").

### Insights

Insights highlight patterns, anomalies, and trends based on built-in domain expertise. They go beyond raw metrics to surface meaningful findings such as performance degradation, resource bottlenecks, and violations of best practices. These insights help you focus on what matters most and take informed, corrective actions quickly.

### Deployment flexibility

![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") **Databases** supports diverse deployment models:

* **On-premises**: Monitor traditional database setups.
* **Cloud**: Gain visibility into cloud-hosted databases (for example, AWS RDS).
* **Hybrid**: Ensure consistent observability across mixed environments.

## Use cases

### Understand database health



![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") **Databases** provides a real-time overview of your database's health. The app continuously evaluates key metrics to provide a health score that reflects the current state of your database environment. This health score helps you quickly identify areas that might require attention.

* Tracks performance indicators such as query execution times, resource utilization, and connection issues.
* Highlights anomalies and potential risks affecting database reliability.

### Analyze and optimize query performance

Queries are often the root cause of database inefficiencies. The app provides tools to analyze query execution and identify areas for improvement. This ensures that your databases can handle workloads effectively.

* Detects slow or inefficient queries that impact database performance.
* Provides recommendations for query optimizations, such as rewriting queries or adding indexes to improve performance.
* Offers detailed execution plans to help you understand how queries interact with your database.

### Detect and resolve database issues

![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") **Databases** helps you address problems before they affect your database operations. The app uses Dynatrace AI capabilities to identify issues, analyze their root causes, and suggest actionable solutions.

* Detects anomalies in database behavior using AI-powered analysis.
* Pinpoints root causes of performance degradation or failures.
* Recommends remediation steps, such as configuration changes or query optimizations, based on actionable insights.

### Integrate with Dynatrace for end-to-end observability

![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") **Databases** is part of the Dynatrace ecosystem and provides comprehensive observability across your entire technology stack. The app integrates with other Dynatrace tools to provide a unified view of your database and its dependencies.

* **Grail**: Processes large volumes of data for scalable analytics.
* **Smartscape**: Maps real-time dependencies for context-aware analysis.
* **Davis AI**: Detects anomalies and provides intelligent recommendations.

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Get an overview of all your extension-monitored databases.](https://www.dynatrace.com/hub/detail/database-overview/?utm_source=doc&utm_medium=link&utm_campaign=cross)

## Databases documentation overview

[01Get started with database monitoring

* How-to guide](/docs/observe/infrastructure-observability/databases/database-app/get-started)[02Data collected with Dynatrace database monitoring

* Reference](/docs/observe/infrastructure-observability/databases/database-app/data-collected)