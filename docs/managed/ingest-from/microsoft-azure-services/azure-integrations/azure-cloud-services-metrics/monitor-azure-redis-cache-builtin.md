---
title: Azure Redis Cache (built-in)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-redis-cache-builtin
scraped: 2026-05-12T11:27:29.739751
---

# Azure Redis Cache (built-in)

# Azure Redis Cache (built-in)

* How-to guide
* 1-min read
* Updated on Nov 15, 2023

For information about differences between classic services and other services, see [Migrate from Azure classic (formerly 'built-in') services to cloud services](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Migrate Azure classic services to their new versions.").

Dynatrace ingests metrics from Azure Metrics API for **Azure Redis Cache**. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Environment ActiveGate
* To disable monitoring of built-in services, you need Environment ActiveGate version 1.245+ and Dynatrace version 1.247+.

This service monitors Azure Cache for Redis (`Microsoft.Cache/redis`).

Enterprise Azure Cache for Redis service (`Microsoft.Cache/redisEnterprise`) currently cannot be monitored; to request this type of monitoring, please create an RFE (Request for Enhancement).

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

| Metric key | Name | Unit | Aggregations | Monitoring consumption |
| --- | --- | --- | --- | --- |
| builtin:cloud.azure.redis.cache.hits | Cache hits | Count | autovalue | DDUs |
| builtin:cloud.azure.redis.cache.misses | Cache misses | Count | autovalue | DDUs |
| builtin:cloud.azure.redis.cache.read | Read bytes/s | Byte/second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.redis.cache.write | Write bytes/s | Byte/second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.redis.commands.get | Get commands | Count | autovalue | DDUs |
| builtin:cloud.azure.redis.commands.set | Set commands | Count | autovalue | DDUs |
| builtin:cloud.azure.redis.commands.total | Total no. of processed commands | Count | autovalue | DDUs |
| builtin:cloud.azure.redis.keys.evicted | No. of evicted keys | Count | autovalue | DDUs |
| builtin:cloud.azure.redis.keys.expired | No. of expired keys | Count | autovalue | DDUs |
| builtin:cloud.azure.redis.keys.total | Total no. of keys | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.redis.memory.used | Used memory | Byte | autoavgmaxmin | DDUs |
| builtin:cloud.azure.redis.memory.usedRss | Used memory RSS | Byte | autoavgmaxmin | DDUs |
| builtin:cloud.azure.redis.connected | Connected clients | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.redis.load | Server load | Percent (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.redis.processorTime | Processor time | Percent (%) | autoavgmaxmin | DDUs |