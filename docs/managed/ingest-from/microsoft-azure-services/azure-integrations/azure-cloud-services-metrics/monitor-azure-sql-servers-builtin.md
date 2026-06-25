---
title: Azure SQL Servers (built-in)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-servers-builtin
scraped: 2026-05-12T11:26:54.560141
---

# Azure SQL Servers (built-in)

# Azure SQL Servers (built-in)

* How-to guide
* 1-min read
* Updated on Nov 15, 2023

For information about differences between classic services and other services, see [Migrate from Azure classic (formerly 'built-in') services to cloud services](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Migrate Azure classic services to their new versions.").

Dynatrace ingests metrics from Azure Metrics API for **Azure SQL (SQL Servers, SQL Databases, SQL elastic pools)**. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Environment ActiveGate
* To disable monitoring of built-in services, you need Environment ActiveGate version 1.245+ and Dynatrace version 1.247+.

This service monitors SQL Servers, SQL Databases (only containing the user kind) and SQL elastic pools.

You can find the already monitored resources on the Azure overview page, **Databases components** view.

To monitor resources of the hyperscale/data warehouse resources, or Managed deployments, check the SQL Database Hyperscale/SQL Data Warehouse/SQL Managed Instance and the Azure overview page, **Cloud services** view.

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view Azure service metrics in your Dynatrace environment on the Azure subscription page or on your own dashboard.

Values in the table depend upon the selected timeframe. For more details, see [Troubleshoot timeframe comparison for Azure monitoring setup)](https://dt-url.net/7j438f0).

### View metrics on the Azure account page

To access metrics on the Azure account page

1. Go to **Azure**.
2. Choose the Azure subscription.
3. Select the service whose metrics you want to check. Metrics for the selected service are visible under the infographic in the service section, similarly to the example below.

   ![Azure service metrics](https://dt-cdn.net/images/azure-service-1109-9488bfa5e4.png)

   Azure service metrics

### View metrics on a dashboard

You can create your own dashboard for viewing Azure service metrics. For information on how to create dashboards, see [Create and edit Dynatrace dashboards](/managed/analyze-explore-automate/dashboards-classic/dashboards/create-dashboards "Learn how to create and edit Dynatrace dashboards.").

## Available metrics

### SQL Databases

| Metric key | Name | Unit | Aggregations | Monitoring consumption |
| --- | --- | --- | --- | --- |
| builtin:cloud.azure.sqlDatabase.connections.blockedByFirewall | Blocked by firewall | Count | autovalue | DDUs |
| builtin:cloud.azure.sqlDatabase.connections.failed | Failed connections | Count | autovalue | DDUs |
| builtin:cloud.azure.sqlDatabase.connections.successful | Successful connections | Count | autovalue | DDUs |
| builtin:cloud.azure.sqlDatabase.dtu.limit.count | DTU limit | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlDatabase.dtu.limit.used | DTU used | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlDatabase.dtu.consumptionPerc | DTU percentage | Percent (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlDatabase.io.dataRead | Data I/O percentage | Percent (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlDatabase.io.logWrite | Log I/O percentage | Percent (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlDatabase.storage.percent | Database size percentage | Percent (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlDatabase.storage.totalBytes | Total database size | Byte | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlDatabase.storage.xtpPercent | In-Memory OLTP storage percent | Percent (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlDatabase.cpuPercent | CPU percentage | Percent (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlDatabase.deadlocks | Deadlocks | Count | autovalue | DDUs |
| builtin:cloud.azure.sqlDatabase.sessions | Sessions percentage | Percent (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlDatabase.workers | Workers percentage | Percent (%) | autoavgmaxmin | DDUs |

### SQL elastic pools

| Metric key | Name | Unit | Aggregations | Monitoring consumption |
| --- | --- | --- | --- | --- |
| builtin:cloud.azure.sqlElasticPool.dtu.storage.limitBytes | Storage limit | Byte | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlElasticPool.dtu.storage.percent | Database size percentage | Percent (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlElasticPool.dtu.storage.usedBytes | Storage used | Byte | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlElasticPool.dtu.storage.xtpPercent | In-memory OLTP storage percent | Percent (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlElasticPool.dtu.consumption | DTU percentage | Percent (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlElasticPool.edtu.limit | eDTU limit | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlElasticPool.edtu.used | eDTU used | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlElasticPool.io.dataRead | Data I/O percentage | Percent (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlElasticPool.io.logWrite | Log I/O percentage | Percent (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlElasticPool.cpuPercent | CPU percentage | Percent (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlElasticPool.sessions | Sessions percentage | Percent (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlElasticPool.workers | Workers percentage | Percent (%) | autoavgmaxmin | DDUs |