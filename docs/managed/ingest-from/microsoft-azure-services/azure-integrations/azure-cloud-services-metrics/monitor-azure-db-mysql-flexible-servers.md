---
title: Azure Database for MySQL Flexible Servers monitoring
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-db-mysql-flexible-servers
scraped: 2026-05-12T11:26:18.720978
---

# Azure Database for MySQL Flexible Servers monitoring

# Azure Database for MySQL Flexible Servers monitoring

* How-to guide
* 3-min read
* Published Aug 27, 2024

From 16 September 2024, Azure Database for MySQL Flexible Servers replaces [Azure Database for MySQL Single Server](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-db-mysql "Monitor Azure DB for MySQL and view available metrics.").

The Azure Database for MySQL Flexible Servers overview page serves as a comprehensive overview of your MySQL servers and database instances. From here you can gain full visibility and check if your database is healthy, under-performing, or if there are any failed connections.

## Prerequisites

* Dynatrace version 1.298+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

Optionally, for OneAgent integration, see [how database activity is monitored](/managed/observe/infrastructure-observability/databases/database-services-classic/how-database-activity-is-monitored "Learn about automatic detection and monitoring of database services in your application environment.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to **Technologies & Processes**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**…**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**…**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

Clone hide azure

## Available metrics

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| aborted\_connections | Aborted connections | Count | Applicable |
| active\_connections | Active connections | Count | Applicable |
| active\_transactions | Active transactions | Count |  |
| backup\_storage\_used | Backup storage used | Byte |  |
| binlog\_storage\_used | Binlog storage used | Byte |  |
| cpu\_credits\_consumed | CPU credits consumed | Count |  |
| cpu\_credits\_remaining | CPU credits remaining | Count |  |
| Com\_alter\_table | Com alter table | Count |  |
| Com\_create\_db | Com create DB | Count |  |
| Com\_create\_table | Com create table | Count |  |
| Com\_delete | Com delete | Count |  |
| Com\_drop\_db | Com drop DB | Count |  |
| Com\_drop\_table | Com drop table | Count |  |
| Com\_insert | Com insert | Count |  |
| Com\_select | Com select | Count |  |
| Com\_update | Com update | Count |  |
| data\_storage\_used | Data storage used | Byte |  |
| HA\_IO\_status | Ha IO status | Count |  |
| HA\_SQL\_status | Ha SQL status | Count |  |
| HA\_replication\_lag | Ha replication lag | Second |  |
| cpu\_percent | Host CPU percent | Percent | Applicable |
| network\_bytes\_ingress | Host network in | Byte | Applicable |
| network\_bytes\_egress | Host network out | Byte | Applicable |
| ibdata1\_storage\_used | Ibdata1 storage used | Byte |  |
| Innodb\_buffer\_pool\_pages\_data | Innodb buffer pool pages data | Count |  |
| Innodb\_buffer\_pool\_pages\_dirty | Innodb buffer pool pages dirty | Count |  |
| Innodb\_buffer\_pool\_pages\_flushed | Innodb buffer pool pages flushed | Count |  |
| Innodb\_buffer\_pool\_pages\_free | Innodb buffer pool pages free | Count |  |
| Innodb\_buffer\_pool\_reads | Innodb buffer pool reads | Count |  |
| Innodb\_data\_writes | Innodb data writes | Count |  |
| Innodb\_row\_lock\_time | Innodb row lock time | MilliSecond |  |
| Innodb\_row\_lock\_waits | Innodb row lock waits | Count |  |
| memory\_percent | Memory percent | Percent | Applicable |
| trx\_rseg\_history\_len | Mysql history list length | Count |  |
| lock\_deadlocks | Mysql lock deadlocks | Count |  |
| lock\_timeouts | Mysql lock timeouts | Count |  |
| Uptime | Mysql uptime | Second |  |
| others\_storage\_used | Others storage used | Byte |  |
| Queries | Queries | Count |  |
| Replica\_IO\_Running | Replica IO status | Count |  |
| Replica\_SQL\_Running | Replica SQL status | Count |  |
| replication\_lag | Replication lag in seconds | Second | Applicable |
| serverlog\_storage\_limit | Serverlog storage limit | Byte |  |
| serverlog\_storage\_percent | Serverlog storage percent | Percent | Applicable |
| serverlog\_storage\_usage | Serverlog storage used | Byte |  |
| Slow\_queries | Slow queries | Count |  |
| storage\_io\_count | Storage IO count | Count |  |
| io\_consumption\_percent | Storage IO percent | Percent | Applicable |
| storage\_limit | Storage limit | Byte |  |
| storage\_percent | Storage percent | Percent |  |
| storage\_used | Storage used | Byte |  |
| Threads\_running | Threads running | Count |  |
| total\_connections | Total connections | Count |  |