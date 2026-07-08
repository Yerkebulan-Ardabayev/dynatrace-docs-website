---
title: Azure Service Bus (built-in)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-service-bus-builtin
---

# Azure Service Bus (built-in)

# Azure Service Bus (built-in)

* How-to guide
* 1-min read
* Published Jul 27, 2022

Dynatrace ingests metrics from Azure Metrics API for **Azure Service Bus**. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.201+
* Environment ActiveGate version 1.195+

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
| builtin:cloud.azure.serviceBus.namespace.connections.active | Total active connections | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.namespace.errors.server | Server errors | Count | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.namespace.errors.user | User errors | Count | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.namespace.messages.count | Count of messages | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.namespace.messages.countActive | Count of active messages | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.namespace.messages.countDeadLettered | Count of dead-lettered messages | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.namespace.messages.countScheduled | Count of scheduled messages | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.namespace.messages.incoming | Incoming messages | Count | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.namespace.messages.outgoing | Outgoing messages | Count | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.namespace.requests.incoming | Incoming requests | Count | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.namespace.requests.successful | Total successful requests | Count | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.namespace.requests.throttled | Throttled requests | Count | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.namespace.cpu | Service bus premium namespace CPU usage metric | Percent (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.namespace.memory | Service bus premium namespace memory usage metric | Percent (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.namespace.size | Service bus size | Byte | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.queue.errors.server | Server errors | Count | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.queue.errors.user | User errors | Count | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.queue.messages.count | Count of messages in queue | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.queue.messages.countActive | Count of active messages in a queue | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.queue.messages.countDeadLettered | Count of dead-lettered messages in a queue | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.queue.messages.countScheduled | Count of scheduled messages in a queue | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.queue.messages.incoming | Incoming messages | Count | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.queue.messages.outgoing | Outgoing messages | Count | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.queue.requests.incoming | Incoming requests | Count | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.queue.requests.successful | Total successful requests | Count | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.queue.requests.throttled | Throttled requests | Count | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.queue.size | Size of an queue | Byte | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.topic.errors.server | Server errors | Count | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.topic.errors.user | User errors | Count | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.topic.messages.count | Count of messages in topic | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.topic.messages.countActive | Count of active messages in a topic | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.topic.messages.countDeadLettered | Count of dead-lettered messages in a topic | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.topic.messages.countScheduled | Count of scheduled messages in a topic | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.topic.messages.incoming | Incoming messages | Count | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.topic.messages.outgoing | Outgoing messages | Count | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.topic.requests.incoming | Incoming requests | Count | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.topic.requests.successful | Total successful requests | Count | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.topic.requests.throttled | Throttled requests | Count | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.topic.size | Size of a topic | Byte | autoavgmaxmin | DDUs |