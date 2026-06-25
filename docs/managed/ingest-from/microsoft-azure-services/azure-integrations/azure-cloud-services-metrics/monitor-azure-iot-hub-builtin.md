---
title: Azure IoT Hub (built-in)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-iot-hub-builtin
scraped: 2026-05-12T11:25:22.462758
---

# Azure IoT Hub (built-in)

# Azure IoT Hub (built-in)

* How-to guide
* 1-min read
* Updated on Nov 15, 2023

For information about differences between classic services and other services, see [Migrate from Azure classic (formerly 'built-in') services to cloud services](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Migrate Azure classic services to their new versions.").

Dynatrace ingests metrics from Azure Metrics API for **Azure IoT Hub**. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Environment ActiveGate
* To disable monitoring of built-in services, you need Environment ActiveGate version 1.245+ and Dynatrace version 1.247+.

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
| builtin:cloud.azure.iotHub.command.abandoned | Commands abandoned | Count | autovalue | DDUs |
| builtin:cloud.azure.iotHub.command.completed | Commands completed | Count | autovalue | DDUs |
| builtin:cloud.azure.iotHub.command.rejected | Commands rejected | Count | autovalue | DDUs |
| builtin:cloud.azure.iotHub.device.connected | Connected devices | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.iotHub.device.dailyThroughputThrottling | Number of throttling errors | Count | autovalue | DDUs |
| builtin:cloud.azure.iotHub.device.dataUsage | Total device data usage | Byte | autoavgmaxmin | DDUs |
| builtin:cloud.azure.iotHub.device.registered | Total devices | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.iotHub.eventHub.builtInEventHub.messages.delivered | Messages delivered to the built-in endpoint (messages/events) | Count | autovalue | DDUs |
| builtin:cloud.azure.iotHub.eventHub.builtInEventHub.averageLatencyMs | Message latency for the built-in endpoint (messages/events) | Millisecond | autoavgmaxmin | DDUs |
| builtin:cloud.azure.iotHub.eventHub.messages.delivered | Messages delivered to Event Hub endpoints | Count | autovalue | DDUs |
| builtin:cloud.azure.iotHub.eventHub.averageLatencyMs | Message latency for event hub endpoints | Millisecond | autoavgmaxmin | DDUs |
| builtin:cloud.azure.iotHub.messages.dropped | Dropped messages | Count | autovalue | DDUs |
| builtin:cloud.azure.iotHub.messages.invalidForAllEndpoints | Invalid messages | Count | autovalue | DDUs |
| builtin:cloud.azure.iotHub.messages.orphaned | Orphaned messages | Count | autovalue | DDUs |
| builtin:cloud.azure.iotHub.messages.sendAttempts | Telemetry message send attempts | Count | autovalue | DDUs |
| builtin:cloud.azure.iotHub.messages.sent | Telemetry messages sent | Count | autovalue | DDUs |
| builtin:cloud.azure.iotHub.messages.sentToFallback | Messages matching fallback condition | Count | autovalue | DDUs |
| builtin:cloud.azure.iotHub.serviceBus.queues.averageLatencyMs | Message latency for service bus queue endpoints | Millisecond | autoavgmaxmin | DDUs |
| builtin:cloud.azure.iotHub.serviceBus.queues.messagesDelivered | Messages delivered to service bus queue endpoints | Count | autovalue | DDUs |
| builtin:cloud.azure.iotHub.serviceBus.topics.averageLatencyMs | Message latency for service bus topic endpoints | Millisecond | autoavgmaxmin | DDUs |
| builtin:cloud.azure.iotHub.serviceBus.topics.messagesDelivered | Messages delivered to service bus topic endpoints | Count | autovalue | DDUs |
| builtin:cloud.azure.iotHub.storageEndpoints.avgLatencyMs | Message latency for storage endpoints | Millisecond | autoavgmaxmin | DDUs |
| builtin:cloud.azure.iotHub.storageEndpoints.blobsWritten | Blobs written to storage | Count | autovalue | DDUs |
| builtin:cloud.azure.iotHub.storageEndpoints.bytesWritten | Data written to storage | Byte | autoavgmaxmin | DDUs |
| builtin:cloud.azure.iotHub.storageEndpoints.messageDelivered | Messages delivered to storage endpoints | Count | autovalue | DDUs |