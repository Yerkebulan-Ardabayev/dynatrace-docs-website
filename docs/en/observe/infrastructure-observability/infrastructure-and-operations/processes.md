---
title: Processes
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/infrastructure-and-operations/processes
scraped: 2026-02-18T05:34:38.711063
---

# Processes

# Processes

* Latest Dynatrace
* Explanation
* 2-min read
* Published Nov 25, 2025

The  **Processes** view in ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** provides a dedicated inventory for viewing, filtering, and inspecting processes independently or in relation to hosts and containers. Navigate between entities to see how they are interconnected.

Filter processes by host, container, process group, and other fields to analyze and compare across your environment. Each process displays detailed insights, including CPU and memory usage trends, logs, events, and time-series charts.

## Overview

The  **Processes** view provides different perspectives for viewing your processes (**Health**, **Utilization**, and **Metadata**).

The **Health** perspective includes the following default columns:

* **Process**: The process name or identifier. Select the name for a comprehensive, full-page view with detailed metadata, logs, events, and time-series charts.
* **Process group name**: The group to which the process belongs.
* **Health alerts**: Displays health alerts and warning signals powered by [Dynatrace Intelligence](/docs/dynatrace-intelligence "Get familiar with the capabilities of Dynatrace Intelligence."). For details, see [View health alerts and warning signals](/docs/observe/infrastructure-observability/infrastructure-and-operations#health-alerts "Monitor hosts, VMs, processes, and networks to detect issues and improve infrastructure performance.").
* **Custom alerts**: Lists any active custom alerts associated with the process.
* **Availability**: Shows the current availability status of the process.
* **Technologies**: The technologies detected for this process.

## Use cases

* Filter and inspect processes across multiple hosts and containers

  Use filters to view processes by host, container, process group, and other relevant fields, enabling broader analysis across your entire environment.
* Access detailed metrics and charts

  Select a process to access a full-page view with detailed metadata, logs, events, and time-series charts (for example, CPU, memory, network traffic) for deeper analysis and troubleshooting.
* Navigate between related entities

  Navigate between hosts, containers, and processes to see how they are interconnected and view the full infrastructure context.
* Identify problematic processes

  Use the **Health alerts** and **Custom alerts** columns with status filters to quickly identify processes with problems.
* Visualize resource trends

  Visualize CPU and memory usage trends across all processes using the graph view to compare performance and identify anomalies.
* Organize with tags

  Add technology-type tags at the process or process group level for simplified filtering and automation.
* Deep monitoring insights

  Drill down to detailed process-level insights, including versioning and release information, when deep monitoring is activated.