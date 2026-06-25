---
title: Monitor Function Service (built-in)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/monitor-func-service-builtin
scraped: 2026-05-12T11:38:19.445764
---

# Monitor Function Service (built-in)

# Monitor Function Service (built-in)

* How-to guide
* 1-min read
* Updated on Feb 10, 2025

Dynatrace ingests metrics from Azure Metrics API for **Azure Function App**. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Environment ActiveGate
* To disable monitoring of built-in services, you need Environment ActiveGate version 1.245+ and Dynatrace version 1.247+.

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view Azure service metrics in your Dynatrace environment on the Azure subscription page or on your own dashboard.

Values in the table depend upon the selected timeframe. For more details, see [Troubleshoot timeframe comparison for Azure monitoring setup)ï»¿](https://dt-url.net/7j438f0).

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

Metrics visibility depends on the type of application.

* builtin:cloud.azure.appService

  + for WebApps (`Microsoft.Web/sites, kind = app`)
* builtin:cloud.azure.appService.functions

  + for FunctionApps (`Microsoft.Web/sites, kind = functionapp`)
  + for Logic Apps created on the Standard Plan (`"type": "Microsoft.Web/sites", "kind": "functionapp,workflowapp"`)

| Metric key | Name | Unit | Aggregations | Monitoring consumption |
| --- | --- | --- | --- | --- |
| builtin:cloud.azure.appService.applicationQueue.requests | Requests in application queue | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.functions.applicationQueue.requests | Requests in application queue | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.functions.execution.count | Function execution count | Count | autovalue | DDUs |
| builtin:cloud.azure.appService.functions.execution.unitsCount | Function execution units count | Count | autovalue | DDUs |
| builtin:cloud.azure.appService.functions.http.status.http5xx | HTTP 5xx | Count | autovalue | DDUs |
| builtin:cloud.azure.appService.functions.io.operations.other | IO other operations/s | Per second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.functions.io.operations.read | IO read operations/s | Per second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.functions.io.operations.write | IO write operations/s | Per second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.functions.io.other | IO other bytes/s | Byte/second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.functions.io.read | IO read bytes/s | Byte/second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.functions.io.write | IO write bytes/s | Byte/second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.functions.traffic.bytesReceived | Received bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.appService.functions.traffic.bytesSent | Sent bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.appService.http.status.http2xx | HTTP 2xx | Count | autovalue | DDUs |
| builtin:cloud.azure.appService.http.status.http403 | HTTP 403 | Count | autovalue | DDUs |
| builtin:cloud.azure.appService.http.status.http5xx | HTTP 5xx | Count | autovalue | DDUs |
| builtin:cloud.azure.appService.io.operations.other | IO other operations/s | Per second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.io.operations.read | IO read operations/s | Per second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.io.operations.write | IO write operations/s | Per second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.io.other | IO other bytes/s | Byte/second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.io.read | IO read bytes/s | Byte/second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.io.write | IO write bytes/s | Byte/second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.response.avg | Response time avg | Second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.traffic.bytesReceived | Received bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.appService.traffic.bytesSent | Sent bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.appService.traffic.requests | Requests count | Count | autovalue | DDUs |