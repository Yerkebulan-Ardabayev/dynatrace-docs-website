---
title: Azure Database for PostgreSQL (Single Server, Hyperscale, Flexible Server) monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-db-postgresql
scraped: 2026-03-01T21:21:20.552232
---

# Azure Database for PostgreSQL (Single Server, Hyperscale, Flexible Server) monitoring

# Azure Database for PostgreSQL (Single Server, Hyperscale, Flexible Server) monitoring

* Latest Dynatrace
* How-to guide
* 6-min read
* Published Jun 25, 2020

On the Azure Database for PostgreSQL (Single Server, Hyperscale, Flexible Server) overview pages you get insights into various aspects of database performance, including CPU and memory usage, active connections, storage space, and much more.

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

![Postgres dash](https://dt-cdn.net/images/azuredbforpostgresql-2976-bc0290ba6d.png)

![Hyper](https://dt-cdn.net/images/azuredbforpostgresqlhyperscale-3017-95194857cf.png)

### Set up a management zone

To import a dashboard for Azure Database for PostgreSQL, you need to [set up a management zone](/docs/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones.") to limit the entities displayed on the dashboard to those relevant to this service.

When you create a management zone for this dashboard:

1. Create a rule that identifies services based on a common property:

   * Service topology: `Opaque service`
   * Service type: `Database`
2. Add a condition for the database name to contain the `postgres` string (case sensitive.)

Example

![Azure management zone](https://dt-cdn.net/images/azuredbforpostgresqlmanagementzone-2700-c85a5f89c0.webp)

You can see whether a dashboard requires a management zone in the rules setup.

After you create the management zone, assign it to your dashboard (from the dashboard, select **Edit** > **Settings** > **Default management zone**). For more information, see [Dashboard timeframe and management zone](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard timeframe and management zone settings.").

## Available metrics

### Azure Database for PostgreSQL (Single Server)

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| active\_connections | The number of active connections to the server | Count | Applicable |
| backup\_storage\_used | The amount of backup storage used. This metric represents the sum of storage consumed by all the full database backups, differential backups, and log backups retained based on the backup retention period set for the server. | Bytes |  |
| cpu\_percent | The percentage of CPU in use | Percent | Applicable |
| connections\_failed | The number of established connections that failed | Count | Applicable |
| io\_consumption\_percent | The percentage of IO in use | Percent | Applicable |
| pg\_replica\_log\_delay\_in\_bytes | Lag in bytes of the most lagging replica | Bytes |  |
| memory\_percent | The percentage of memory in use | Percent | Applicable |
| network\_bytes\_ingress | Network in across active connections | Bytes | Applicable |
| network\_bytes\_egress | Network out across active connections | Bytes | Applicable |
| pg\_replica\_log\_delay\_in\_seconds | The time since the last replayed transaction. This metric is available for replica servers only. | Seconds | Applicable |
| serverlog\_storage\_limit | The maximum server log storage for this server | Bytes |  |
| serverlog\_storage\_percent | The percentage of server log storage used out of the server's maximum server log storage | Percent | Applicable |
| serverlog\_storage\_usage | The amount of server log storage in use | Bytes |  |
| storage\_limit | The maximum storage for this server | Bytes |  |
| storage\_percent | The percentage of storage used out of the server's maximum | Percent | Applicable |
| storage\_used | The amount of storage in use. The storage used by the service may include the database files, transaction logs, and the server logs. | Bytes |  |

### Azure Database for PostgreSQL Hyperscale

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| active\_connections | The number of active connections to the server | Count | Applicable |
| cpu\_percent | The percentage of CPU in use | Percent | Applicable |
| iops | The number of requests that your application is sending to the storage disks in one second | Count | Applicable |
| memory\_percent | The percentage of memory in use | Percent | Applicable |
| network\_bytes\_egress | Network out across active connections | Byte | Applicable |
| network\_bytes\_ingress | Network in across active connections | Byte | Applicable |
| storage\_percent | The percentage of storage used out of the server's maximum | Percent | Applicable |
| storage\_used | The amount of storage in use. The storage used by the service may include the database files, transaction logs, and the server logs. | Byte |  |

### Azure Database for PostgreSQL - Flexible Server

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| active\_connections | Number of connections to your server. | Count | Applicable |
| backup\_storage\_used | Amount of backup storage used. This metric represents the sum of storage consumed by all the full database backups, differential backups, and log backups retained based on the backup retention period set for the server. The frequency of the backups is service managed. For geo-redundant storage, backup storage usage is twice that of the locally redundant storage. | Byte |  |
| connections\_failed | Failed connections. | Count | Applicable |
| connections\_succeeded | Succeeded connections. | Count |  |
| cpu\_credits\_consumed | Number of credits used by the flexible server. Applicable to Burstable tier. | Count |  |
| cpu\_credits\_remaining | Number of credits available to burst. Applicable to Burstable tier. | Count |  |
| cpu\_percent | Percentage of CPU in use. | Percent | Applicable |
| disk\_queue\_depth | Number of outstanding I/O operations to the data disk. | Count |  |
| iops | Number of I/O operations to disk per second. | Count | Applicable |
| maximum\_used\_transactionIDs | Maximum transaction ID in use. | Count |  |
| memory\_percent | Percentage of memory in use. | Percent | Applicable |
| network\_bytes\_ingress | Amount of incoming network traffic. | Byte | Applicable |
| network\_bytes\_egress | Amount of outgoing network traffic. | Byte | Applicable |
| read\_iops | Number of data disk I/O read operations per second. | Count |  |
| read\_throughput | Bytes read per second from disk. | Count | Applicable |
| storage\_free | Amount of storage space available. | Byte |  |
| storage\_percent | Percent of storage space used. The storage used by the service may include the database files, transaction logs, and the server logs. | Percent | Applicable |
| storage\_used | The storage used by the service may include the database files, transaction logs, and the server logs. | Byte |  |
| txlogs\_storage\_used | Amount of storage space used by the transaction logs. | Byte |  |
| write\_iops | Number of data disk I/O write operations per second. | Count |  |
| write\_throughput | Bytes written per second to disk. | Count | Applicable |