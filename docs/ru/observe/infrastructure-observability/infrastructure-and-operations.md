---
title: Infrastructure & Operations
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/infrastructure-and-operations
scraped: 2026-02-26T21:14:31.153002
---

# Infrastructure & Operations

# Infrastructure & Operations

* Latest Dynatrace
* App
* 13-min read
* Updated on Jan 29, 2026

The ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** app simplifies infrastructure health monitoring and facilitates root cause analysis for problems.

* Health indicators powered by Dynatrace Intelligence help you detect early signs of performance degradation to quickly see which areas of your environment need attention.
* Check infrastructure host health metrics, logs, and events for all infrastructure entities.
* Drill down from ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** to any infrastructure entity metrics, logs, or events.

## Prerequisites

1. Deploy [Dynatrace OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") on your hostsâit's the optimal choice to collect the most granular metrics and network insights.
2. If you are using cloud services, integrate your cloud infrastructure with Dynatrace. Follow the specific integration guides for AWS, Azure, Google Cloud, or other cloud providers.

### Permissions

The following table describes the required permissions.

storage:logs:read

Query logs from GRAIL

storage:events:read

Query events from GRAIL

storage:buckets:read

Read buckets

storage:metrics:read

Query metrics from GRAIL

storage:entities:read

Query entities from GRAIL

storage:fieldsets:read

Read masked/sensitive fields

state:user-app-states:read

Read user-state

state:user-app-states:write

Write user-state

settings:objects:read

Read settings configurations from Settings 2.0

settings:objects:write

Write settings configurations to Settings 2.0

## Get started

![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** provides an up-to-date and comprehensive view of your monitored environments. Use the app to quickly identify areas that require attention and drill down to the exact root cause of issues.

![List view of all data centers, automatically sorted by Davis Intelligence identified problems.](https://dt-cdn.net/hub/Screenshot_2025-07-07_at_13.47.23.png)![Hosts view for a selected data center helps to quickly identify the most problematic hosts within the data center.  Drill down to host details.](https://dt-cdn.net/hub/Screenshot_2025-07-07_at_13.48.54.png)![View host health overview, properties, tags, and ownership information. Drill down to all host details.](https://dt-cdn.net/hub/Screenshot_2025-07-07_at_13.51.12.png)![Host health overview, technologies and all host entities such as disks and network interfaces. Drill down to process details and entity metrics.](https://dt-cdn.net/hub/Screenshot_2025-07-07_at_13.51.24.png)![Detailed process analysis. Drill down to process details.](https://dt-cdn.net/hub/Screenshot_2025-07-07_at_13.52.09.png)![Network device metrics overview.](https://dt-cdn.net/hub/Screenshot_2025-07-07_at_13.52.34.png)

1 of 6List view of all data centers, automatically sorted by Davis Intelligence identified problems.

### Navigation

The ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** app presents the data for your data centers, hosts, and network devices in lists.

Use the table options to navigate to the details that you need.

* To sort the table by a particular column, select the column header.
* To show or hide columns, select  **Column settings** and then select the columns you want to display.

#### Access details of entities

To get the details about an entity

1. Go to ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** and select  **Hosts** ,  **Containers**,  **Processes** or  **Network devices**.
2. Select an entity from the list. You can sort and filter the list as needed.

### Filtering

You can filter the tables in the app by using the filter field with listed suggestions. Currently, you can use basic syntax (grouping filter statements and using logical operators is not supported). As you type, the relevant options are displayed.

You can add several statements to narrow down the filter results. For example, `"Alert status" = Critical` `name != *1b*`. In this case, you narrow the search to hosts with more than 4 problems and names that don't include `1b`.

For more details on using filters, see [Filter field](/docs/discover-dynatrace/get-started/dynatrace-ui/ui-filter-field "The filter field is a powerful tool that allows you to quickly find relevant information or narrow down results within apps.").

### Segments

You can use segments in ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** to logically structure observability data for your devices.

Some of the advantages of using segments are

* **Flexibility**: Segments can be used across different apps that support that feature.
* **Ease of use**: You can create and use complex filters quickly.
* **Option to share**: You can share filters across different users.

#### Apply a segment

1. Go to ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** >  **Segments**.
2. Select the segment name from the drop-down menu. If needed, select parameters for the selected segment.
3. Select **Apply** to activate the segment.

#### Add a segment

1. Go to ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** >  **Segments**.
2. Select  **Manage segments** >  **Segment**.
3. Add a name for the segment.
4. Optional Add a description.
5. Use one of the available options for filtering data

   * Add a variable. This requires creating a query.
   * Add data types. Select from the available options in the menu.
   * Add entities and topology. Select from the available options in the menu.
6. Select **Save**.

For more details on managing segments, refer to [Segments](/docs/manage/segments "Segments logically structure monitoring data in Grail and function as convenient filters for data that users are allowed to access based on permissions.").

### Analyze overview charts

You can define which metrics are displayed in the charts by selecting ![Expand menu](https://dt-cdn.net/images/dashboards-app-menu-expand-3398af0cdf.svg "Expand menu") in the upper left corner of each graph or chart.

#### Export data to Notebooks

To further analyze the data from ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace."):

1. Go to ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations**.
2. Select an entity to see its details.
3. Select the graph or chart you want to analyze and select  > **Open in Notebooks** ![Open with](https://dt-cdn.net/images/open-with-003fc82dcd.svg "Open with").
4. Choose whether to open the graph in a new or existing notebook.

### View host processes

The **Processes** tab in the host full-page view displays the **CPU usage** and **Memory usage** charts with a table showing 5 contributors.

To view processes on a host

1. Open the full-page view of a host.
2. Select the **Processes** tab.

The **CPU usage** and **Memory usage** charts display with a table showing 5 contributors. Change the contributors by selecting other metrics, such as health alerts, custom warnings, and CPU usage.

To view all processes across your environment, switch to the [Processes](#processes) inventory.

Note that processes can run directly on hosts or in containers running on hosts.

### Display code-module metrics

You can inject code modules and display the injected data in the app. For more details, see [Universal injection of code modules](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix#universal-injection "Learn which capabilities are supported by OneAgent on different operating systems and platforms.").

After selecting a process from the list, the data is presented in a dedicated tab.

### Monitor incoming and outgoing connections



In the full-page view of a host, under **Connections**, you can see a quick overview of each type of connection, the total number of connected entities, and the number of problems. Expand the panel to see a list of connected entities and possible problems for each of them. You can also see which processes from the current host communicate with other processes or services that aren't part of the host.

The **Connections** table allows you to identify potential sources of problems that don't happen directly on the host. Select the connected entity marked with  to navigate to its details page and investigate the issue.

The incoming and outgoing process connections in the table display processes with the most issues based on network and CPU usage.

### Measure the reachability of a host or device

The **Reachability** column on the **Hosts** and **Network devices** pages shows how easily you can access a device or a host over the network from a remote location. For more details, see [Synthetic Monitoring](/docs/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.").

The value presents the ratio of fully available Network Availability Monitors (NAM) (with 100% availability over the selected time period) to all configured monitors for the given host or network device.

To use this feature, you need to configure NAM for the desired device or host. For details, refer to [Configure a NAM monitor](/docs/observe/digital-experience/synthetic-monitoring/network-availability-monitors/create-a-nam-monitor "Learn how to set up a NAM monitor to check the performance and availability of your site.").

### View health alerts and warning signals

In ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations**, you can view health alerts and warning signals.

Health alerts and warning signals help you monitor your infrastructure by providing clear, actionable insights. These features reduce the noise from infrastructure issues and improve alerting capabilities, so you can focus on what matters most. This is achieved through better categorization of detected malfunctions.

* For critical events, a Health alert is raised, triggering a [Dynatrace Problems](/docs/dynatrace-intelligence/davis-problems-app "Use the Problems app to quickly get to the root cause of incidents in your environment.") investigation.
* For non-critical situations, a Warning signal informs you of a potential challenge.

To take advantage of this feature in ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations**, you need to enable it. Once enabled, certain alerts that were previously classified as critical will be reclassified as warnings, as they are not considered critical enough to require immediate attention.

To enable this option

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings**.
2. Select  **Analyze and alert** > **Alerts**.
3. Under **Category update**, select **Ready-made alerts category update**.
4. Enable **Updated classification for select ready-made alerts**.

Once you enable the option, these alerts will be converted to warnings:

| Entity type | Event type[1](#fn-1-1-def) | Description |
| --- | --- | --- |
| HOST | OSI\_HIGH\_CPU | CPU Usage |
| HOST | OSI\_NIC\_DROPPED\_PACKETS\_HIGH | High rate of dropped packets |
| HOST | RESOURCE\_CONTENTION | Slow disk |
| PGI | PROCESS\_RESTART | Process restart |

1

Once converted into warnings, the events with the `event.type` listed here, will be marked as `event.type = WARNING`. Their former value is removed.

### View data from imported technologies

![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** detects installed extensions and displays them in the **Technologies** inventory. Extensions are organized by category, making it easy to explore and analyze your technology stack.

To view installed technologies

1. Go to ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** > **Technologies**.
2. Select an extension from the list to view more details.

For details on setting up extensions, see [Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.").

Minimum required versions of extensions

Ensure your system has these minimum versions of the installed extensions to avoid any issues with displaying the data in ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations**.

This list concerns extensions for supporting network devices and is not exhaustive. Each network device can have more extensions.

| Extension | Minimum version |
| --- | --- |
| SNMP Autodiscovery | 2.2.8 |
| Generic Cisco Device | 2.1.4 |
| F5 BIG-IP | 2.10.0 |
| Palo Alto firewalls | 2.7.0 |
| Juniper Networks (SNMP) | 1.5.0 |
| Generic network device | 2.0.0 |
| Fortigate | 1.2.21 |

See our detailed [Generic network topology](/docs/ingest-from/extend-dynatrace/extend-topology/network-topology "Use the generic network topology model available in Dynatrace extensions.") guide on how to make your custom extensions appear in ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations**.

## Concepts

![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** has the following core components:

[#### Data centers

Monitor the health and performance of your data centers and availability zones to detect and resolve critical issues.

Data centers](/docs/observe/infrastructure-observability/infrastructure-and-operations/data-centers)[#### Hosts

Monitor infrastructure hosts across physical machines, VMs, and cloud instances to track health, performance, and resource utilization.

Hosts](/docs/observe/infrastructure-observability/infrastructure-and-operations/hosts)[#### Containers

Monitor and troubleshoot containerized workloads across Kubernetes and standalone hosts.

Containers](/docs/observe/infrastructure-observability/infrastructure-and-operations/containers)[#### Processes

Monitor processes running on hosts and containers with detailed insights into CPU and memory usage trends and key metrics.

Processes](/docs/observe/infrastructure-observability/infrastructure-and-operations/processes)[#### Networks

Monitor network devices and gain insights into networking components with Dynatrace Intelligence-powered analytics and flexible observability options.

Networks](/docs/observe/infrastructure-observability/infrastructure-and-operations/networks)

### Relation between hosts, containers, and processes

Hosts, containers, and processes are interconnected, and you can navigate between them to understand dependencies and troubleshoot issues.

#### Hosts

* The host full-page view includes **Processes** and **Containers** tabs showing related processes and containers. Select an entity to navigate to its details.

#### Containers

* Containers run on hosts. The container metadata displays the host name.
* The container full-page view includes an **Overview** tab with links to the host and container group. Selecting the host navigates to the host details. Selecting the container group filters the container list to show all containers in that group.
* The **Processes** tab shows related processes. Select a process to navigate to its details.

#### Processes

* Processes run directly on hosts or in containers. The process metadata displays the related host and container name (if applicable).
* The process side panel shows information about technologies, host, process group, container (if applicable), and deep monitoring details.
* The process full-page view includes an **Overview** tab with links to the host, process group, and container (if applicable). Selecting the host navigates to the host details. Selecting the process group filters the process list to show all processes in that group. Selecting the container navigates to the container details.

## Use cases

* View and identify the status of all data centers, hosts and network devices.
* Quickly identify the root cause of infrastructure problems
* Gain awareness of infrastructure performance and optimize it

  + See data center health at a glance and identify problematic data centers
  + Quickly see host health and identify problematic hosts, network devices, technologies, processes, disks, containers, and networks
  + See infrastructure host health metrics, logs, and events for all infrastructure entities
  + See network devices health metrics, traps, and events.
  + Assess the network reachability of hosts and network devices by integrating with synthetic Network Availability Monitors (NAM).

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

View the status of all data centers and hosts and identify the root cause of infrastructure problems.](https://www.dynatrace.com/hub/?filter=infrastructure-monitoring&internal_source=doc&internal_medium=link&internal_campaign=cross)