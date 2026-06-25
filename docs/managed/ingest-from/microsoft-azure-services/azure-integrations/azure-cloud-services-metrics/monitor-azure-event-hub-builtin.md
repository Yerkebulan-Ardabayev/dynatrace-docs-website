---
title: Azure Event Hubs (built-in)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-event-hub-builtin
scraped: 2026-05-12T11:27:11.878032
---

# Azure Event Hubs (built-in)

# Azure Event Hubs (built-in)

* How-to guide
* 1-min read
* Published Jul 26, 2022

Dynatrace ingests metrics from Azure Metrics API for **Azure Event Hubs**. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Environment ActiveGate
* To disable monitoring of built-in services, you need Environment ActiveGate version 1.245+ and Dynatrace version 1.247+.

This service monitors both `Microsoft.EventHub/namespaces` and `Microsoft.EventHub/namespaces/eventHubs`.

Only monitored Event Hubs (as opposed to Event Hub Namespaces) are directly presented on the Azure overview page, in the **Event hubs** section. To view metrics for Event Hub Namespace, create a custom dashboard.

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
| builtin:cloud.azure.eventHub.capture.backlog | Capture backlog | Count | autovalue | DDUs |
| builtin:cloud.azure.eventHub.capture.bytes | Captured bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.eventHub.capture.msg | Captured messages | Count | autovalue | DDUs |
| builtin:cloud.azure.eventHub.errors.quotaExceeded | Quota exceeded errors | Count | autovalue | DDUs |
| builtin:cloud.azure.eventHub.errors.server | Server errors | Count | autovalue | DDUs |
| builtin:cloud.azure.eventHub.errors.user | User errors | Count | autovalue | DDUs |
| builtin:cloud.azure.eventHub.requests.incoming | Incoming requests | Count | autovalue | DDUs |
| builtin:cloud.azure.eventHub.requests.successful | Successful requests | Count | autovalue | DDUs |
| builtin:cloud.azure.eventHub.requests.throttled | Throttled requests | Count | autovalue | DDUs |
| builtin:cloud.azure.eventHub.traffic.bytesIn | Incoming bytes | Byte/minute | autovalue | DDUs |
| builtin:cloud.azure.eventHub.traffic.bytesOut | Outgoing bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.eventHub.traffic.msgIn | Incoming messages | Count | autovalue | DDUs |
| builtin:cloud.azure.eventHub.traffic.msgOut | Outgoing messages | Count | autovalue | DDUs |
| builtin:cloud.azure.eventHubNamespace.connections.active | Active connections | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.eventHubNamespace.connections.closed | Closed connections | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.eventHubNamespace.connections.opened | Opened connections | Count | autoavgmaxmin | DDUs |