---
title: Azure SQL Data Warehouse (legacy)
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-data-warehouse
scraped: 2026-02-23T21:33:55.345286
---

# Azure SQL Data Warehouse (legacy)

# Azure SQL Data Warehouse (legacy)

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Aug 12, 2021

The Azure SQL Data Warehouse overview page gives you a comprehensive view of how many jobs and tasks were completed over a period of time. You can also track nodes in different states, such as running, idle, or offline.

## Prerequisites

* Dynatrace version 1.224+
* Environment ActiveGate version 1.205+

This service monitors the data warehouse type of SQL Databases. You can find the already monitored resources on the Azure overview page in the **Cloud services** section.

To monitor the SQL Databases user kind, check Azure SQL Servers and the **Databases components** sections on the Azure overview page.

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| Active queries | Active queries. Using this metric unfiltered and unsplit displays all active queries running on the system. |  | Count | Applicable |
| Blocked by firewall | The number of logins to the data warehouse from the database application that the firewall blocks. |  | Count | Applicable |
| CPU percentage | The percentage of CPU that all nodes utilize for the data warehouse. |  | Percent | Applicable |
| Cache hit percentage | The sum of all columnstore segments hits in the local SSD cache. |  | Percent |  |
| Cache used percentage | The sum of all bytes in the local SSD cache across all nodes. |  | Percent |  |
| DWU limit | The Data Warehouse Unit, which is the service-level objective of the data warehouse. |  | Count | Applicable |
| DWU percentage | The maximum value when compared between CPU percentage and Data IO percentage. |  | Percent | Applicable |
| DWU used | DWU limit \* DWU percentage |  | Count | Applicable |
| Data IO percentage | The percentage of IO that all nodes utilize for the data warehouse. |  | Percent | Applicable |
| Effective cap resource percent | The effective cap resource percent for the workload group. If there are other workload groups with the effective min resource percent higher than `0`, the effective cap resource percent is lowered proportionally. | Is user defined, workload group | Percent |  |
| Effective min resource percent | The effective minimum resource percentage setting allowed, considering the service level and the workload group settings. | Is user defined, workload group | Percent |  |
| Failed connections | The number of failed connections to the data warehouse from the database application. |  | Count | Applicable |
| Local tempdb percentage | The percentage of the local tempdb that all compute nodes utilize. |  | Percent |  |
| Memory percentage | The percentage of memory of the SQL Server utilized across all nodes for the data warehouse. |  | Percent | Applicable |
| Queued queries | Cumulative count of requests queued after the maximum concurrency limit was reached. |  | Count | Applicable |
| Successful connections | The number of successful connections to the data from the database application. |  | Count | Applicable |
| Workload group active queries | The active queries within the workload group. Using this metric unfiltered and unsplit displays all active queries running on the system. | Is user defined, workload group | Count |  |
| Workload group allocation by cap resource percent |  |  |  |  |
| The percentage allocation of resources relative to the effective cap resource percent per workload group. This metric provides the effective utilization of the workload group. | Is user defined, Workload group. | Percent |  |  |
| Workload group allocation by system percent | The percentage allocation of resources relative to the entire system. | Is user defined, workload group | Percent |  |
| Workload group query timeouts | Queries for the workload group that have timed out. | Is user defined, workload group | Count |  |
| Workload group queued queries | Cumulative count of requests queued after the maximum concurrency limit was reached. | Is user defined, workload group | Count |  |