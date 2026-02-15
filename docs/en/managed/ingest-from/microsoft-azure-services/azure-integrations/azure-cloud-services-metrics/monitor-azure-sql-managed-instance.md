---
title: Azure SQL Managed Instance monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-managed-instance
scraped: 2026-02-15T09:08:16.369287
---

# Azure SQL Managed Instance monitoring

# Azure SQL Managed Instance monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jul 02, 2020

On the Azure SQL Managed Instance overview page you get insights into various aspects of database performance, including CPU usage, virtual core count, storage space, IO bytes sent/received, and much more.

## Prerequisites

* Dynatrace version 1.196+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

Optionally, for OneAgent integration, see [how database activity is monitored](/docs/observe/infrastructure-observability/databases/database-services-classic/how-database-activity-is-monitored "Learn about automatic detection and monitoring of database services in your application environment.").

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

![SQL dash](https://dt-cdn.net/images/sqlmanagedinstances-1303-b09d61719b.png)

## Available metrics

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| avg\_cpu\_percent | Average CPU percentage | Percent | Applicable |
| io\_bytes\_read | IO bytes read | Bytes | Applicable |
| io\_bytes\_written | IO bytes written | Bytes | Applicable |
| io\_requests | IO requests count | Count | Applicable |
| reserved\_storage\_mb | Storage space reserved | Count | Applicable |
| storage\_space\_used\_mb | Storage space used | Count | Applicable |
| virtual\_core\_count | Virtual core count | Count | Applicable |