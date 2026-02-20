---
title: Azure Database for MariaDB monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-db-mariadb
scraped: 2026-02-20T21:23:33.924536
---

# Azure Database for MariaDB monitoring

# Azure Database for MariaDB monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Jun 25, 2020

On the Azure Database for MariaDB overview page you can see if youâre running out of CPU or facing a high I/O percentage, so you always know which queries need to be optimized.

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

![Mariadb dash](https://dt-cdn.net/images/azuredbformariadb-3481-86c2844045.png)

### Set up a management zone

To import a dashboard for Azure Database for MariaDB, you need to [set up a management zone](/docs/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones.") to limit the entities displayed on the dashboard to those relevant to this service.

When you create a management zone for this dashboard:

1. Create a rule that identifies services based on a common property:

   * Service type: `Database`
   * Technology: `MariaDB`
   * Service topology: `Opaque service`
2. Add a condition for the database name to contain the `mariadb` string (case sensitive.)

Example

![Azure management zone](https://dt-cdn.net/images/azuredbformariadbmanagementzone-2686-28aa52c965.png)

After you create the management zone, select it from your dashboard (**Edit** > **Settings** > **Default management zone**). For more information, see [Dashboard timeframe and management zone](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard timeframe and management zone settings.").

## Available metrics

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| active\_connections | Active connections | Count | Applicable |
| backup\_storage\_used | Backup storage used | Bytes |  |
| cpu\_percent | CPU percent | Percent | Applicable |
| connections\_failed | Failed connections | Count | Applicable |
| io\_consumption\_percent | IO percent | Percent | Applicable |
| memory\_percent | Memory percent | Percent | Applicable |
| network\_bytes\_ingress | Network In across active connections | Bytes | Applicable |
| network\_bytes\_egress | Network Out across active connections | Bytes | Applicable |
| seconds\_behind\_master | Replication lag in seconds | Count | Applicable |
| serverlog\_storage\_limit | Server log storage limit | Bytes |  |
| serverlog\_storage\_percent | Server log storage percent | Percent | Applicable |
| serverlog\_storage\_usage | Server log storage used | Bytes |  |
| storage\_limit | Storage limit | Bytes |  |
| storage\_percent | Storage percent | Percent | Applicable |
| storage\_used | Storage used | Bytes |  |