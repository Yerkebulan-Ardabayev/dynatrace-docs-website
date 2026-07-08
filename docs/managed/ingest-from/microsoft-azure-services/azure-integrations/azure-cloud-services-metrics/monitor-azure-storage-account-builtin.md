---
title: Azure Storage Accounts (built-in)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account-builtin
---

# Azure Storage Accounts (built-in)

# Azure Storage Accounts (built-in)

* How-to guide
* 1-min read
* Updated on Nov 15, 2023

For information about differences between classic services and other services, see [Migrate from Azure classic (formerly 'built-in') services to cloud services](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Migrate Azure classic services to their new versions.").

Dynatrace ingests metrics from Azure Metrics API for **Azure Storage Accounts**. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Environment ActiveGate
* To disable monitoring of built-in services, you need Environment ActiveGate version 1.245+ and Dynatrace version 1.247+.

This service monitors Storage Accounts (`Microsoft.Storage/storageAccounts`). You can find the already monitored resources on the Azure overview page in **Storage accounts** section.

The Storage, StorageV2 and BlobStorage service types are supported. To monitor resources of the `Microsoft.ClassicStorage/storageAccounts` type, check **Storage Account Classic** and the **Cloud services** section on the Azure overview page.

This service monitors the same Azure resources as Azure Storage Account and Azure Storage Blob/File/Queue Services from **Cloud services** section. For more customizable monitoring switch to the latter ones. The historical (built-in) and new versions can't be switched on at the same time.

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
| builtin:cloud.azure.storage.blob.transactions | Transactions count | Count | autovalue | DDUs |
| builtin:cloud.azure.storage.blob.transactions.network.latency.success.e2e | E2E success latency | Millisecond | autoavgmaxmin | DDUs |
| builtin:cloud.azure.storage.blob.transactions.network.latency.success.server | Server success latency | Millisecond | autoavgmaxmin | DDUs |
| builtin:cloud.azure.storage.blob.transactions.network.egress | Egress bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.storage.blob.transactions.network.ingress | Ingress bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.storage.blob.capacity | Blob capacity | Byte | autoavgcountmaxminsum | DDUs |
| builtin:cloud.azure.storage.blob.containers | Blob container count | Count | autoavgcountmaxminsum | DDUs |
| builtin:cloud.azure.storage.blob.entities | Blob count | Count | autoavgcountmaxminsum | DDUs |
| builtin:cloud.azure.storage.file.transactions | Transactions count | Count | autovalue | DDUs |
| builtin:cloud.azure.storage.file.transactions.network.latency.success.e2e | E2E success latency | Millisecond | autoavgmaxmin | DDUs |
| builtin:cloud.azure.storage.file.transactions.network.latency.success.server | Server success latency | Millisecond | autoavgmaxmin | DDUs |
| builtin:cloud.azure.storage.file.transactions.network.egress | Egress bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.storage.file.transactions.network.ingress | Ingress bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.storage.file.capacity | File capacity | Byte | autoavgcountmaxminsum | DDUs |
| builtin:cloud.azure.storage.file.containers | File share count | Count | autoavgcountmaxminsum | DDUs |
| builtin:cloud.azure.storage.file.entities | File count | Count | autoavgcountmaxminsum | DDUs |
| builtin:cloud.azure.storage.queue.transactions | Transactions count | Count | autovalue | DDUs |
| builtin:cloud.azure.storage.queue.transactions.network.latency.success.e2e | E2E success latency | Millisecond | autoavgmaxmin | DDUs |
| builtin:cloud.azure.storage.queue.transactions.network.latency.success.server | Server success latency | Millisecond | autoavgmaxmin | DDUs |
| builtin:cloud.azure.storage.queue.transactions.network.egress | Egress bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.storage.queue.transactions.network.ingress | Ingress bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.storage.queue.capacity | Queue capacity | Byte | autoavgcountmaxminsum | DDUs |
| builtin:cloud.azure.storage.queue.containers | Queue count | Count | autoavgcountmaxminsum | DDUs |
| builtin:cloud.azure.storage.queue.entities | Queue message count | Count | autoavgcountmaxminsum | DDUs |
| builtin:cloud.azure.storage.table.transactions | Transactions count | Count | autovalue | DDUs |
| builtin:cloud.azure.storage.table.transactions.network.latency.success.server | Server success latency | Millisecond | autoavgmaxmin | DDUs |
| builtin:cloud.azure.storage.table.transactions.network.latency.success.server.e2e | E2E success latency | Millisecond | autoavgmaxmin | DDUs |
| builtin:cloud.azure.storage.table.transactions.network.egress | Egress bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.storage.table.transactions.network.ingress | Ingress bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.storage.table.capacity | Table capacity | Byte | autoavgcountmaxminsum | DDUs |
| builtin:cloud.azure.storage.table.containers | Table count | Count | autoavgcountmaxminsum | DDUs |
| builtin:cloud.azure.storage.table.entities | Table entity count | Count | autoavgcountmaxminsum | DDUs |

## Additional notes

* `Azure Storage Accounts (built-in)` monitors the same Azure resources as `Azure Storage Account` and `Azure Storage Blob/File/Queue Services` from `Cloud services` section. For more customizable monitoring switch to the latter ones. The built-in and generic versions can't be switched on simultaneously:

  + Enabling the built-in version will disable all of the generic versions.
  + Enabling any of the generic versions will disable the built-in version.