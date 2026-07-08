---
title: Azure Application Gateways (built-in)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-app-gateways-builtin
---

# Azure Application Gateways (built-in)

# Azure Application Gateways (built-in)

* How-to guide
* 1-min read
* Updated on Nov 15, 2023

For information about differences between classic services and other services, see [Migrate from Azure classic (formerly 'built-in') services to cloud services](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Migrate Azure classic services to their new versions.").

Dynatrace ingests metrics from Azure Metrics API for Azure Application Gateways. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Environment ActiveGate
* To disable monitoring of built-in services, you need Environment ActiveGate version 1.245+ and Dynatrace version 1.247+.

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view Azure service metrics in your Dynatrace environment on the Azure subscription page or on your own dashboard.

Values in the table depend upon the selected timeframe. For more details, see [Troubleshoot timeframe comparison for Azure monitoring setup)﻿](https://dt-url.net/7j438f0).

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
| builtin:cloud.azure.appGateway.backend.settings.pool.host.healthy | Healthy host count | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appGateway.backend.settings.pool.host.unhealthy | Unhealthy host count | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appGateway.backend.settings.traffic.requests.failed | Requests failed | Count | autovalue | DDUs |
| builtin:cloud.azure.appGateway.backend.settings.traffic.requests.total | Requests total | Count | autovalue | DDUs |
| builtin:cloud.azure.appGateway.http.status.response | Response status | Count | autovalue | DDUs |
| builtin:cloud.azure.appGateway.network.connections.count | Current connections count | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appGateway.network.throughput | Network throughput | Byte/second | autoavgmaxmin | DDUs |