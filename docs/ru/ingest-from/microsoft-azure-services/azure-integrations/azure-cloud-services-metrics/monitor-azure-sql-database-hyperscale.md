---
title: Azure SQL Database Hyperscale monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-database-hyperscale
scraped: 2026-02-28T21:26:15.168120
---

# Azure SQL Database Hyperscale monitoring

# Azure SQL Database Hyperscale monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Apr 13, 2021

Dynatrace ingests metrics from Azure Metrics API for Azure SQL Database Hyperscale. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.215+
* Environment ActiveGate version 1.205+

This service monitors the hyperscale type of SQL Databases. You can find the already monitored resources on the Azure overview page in the **Cloud services** section or use a dashboard preset. To monitor the SQL Databases user kind, check Azure SQL Servers and the **Databases components** sections on the Azure overview page.

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

![Hyperscale](https://dt-cdn.net/images/azi-2615-eba6f59034.png)

## Available metrics

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| allocated\_data\_storage | Data space allocated | Byte | Applicable |
| base\_blob\_size\_bytes | Base blob storage size | Byte |  |
| blocked\_by\_firewall | Blocked by firewall | Count | Applicable |
| connection\_failed | Failed connections | Count | Applicable |
| connection\_successful | Successful connections | Count | Applicable |
| cpu\_limit | CPU limit | Count | Applicable |
| cpu\_percent | CPU percentage | Percent | Applicable |
| cpu\_used | CPU used | Count | Applicable |
| deadlock | Deadlocks | Count | Applicable |
| log\_backup\_size\_bytes | Log backup storage size | Byte | Applicable |
| log\_write\_percent | Log IO percentage | Percent |  |
| physical\_data\_read\_percent | Data IO percentage | Percent | Applicable |
| sessions\_percent | Sessions percentage | Percent | Applicable |
| snapshot\_backup\_size\_bytes | Snapshot backup storage size | Byte |  |
| sqlserver\_process\_core\_percent | SQL server process core percent | Percent |  |
| sqlserver\_process\_memory\_percent | SQL server process memory percent | Percent |  |
| tempdb\_data\_size | Tempdb data file size kb | Count |  |
| tempdb\_log\_size | Tempdb log file size kb | Count |  |
| tempdb\_log\_used\_percent | Tempdb percent log used | Percent | Applicable |
| workers\_percent | Workers percentage | Percent | Applicable |
| xtp\_storage\_percent | In-memory OLTP storage percent | Percent |  |