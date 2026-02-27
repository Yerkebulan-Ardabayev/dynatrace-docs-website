---
title: Azure Storage Account Classic (Blob, File, Queue, Table) monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account-classic
scraped: 2026-02-27T21:21:20.390812
---

# Azure Storage Account Classic (Blob, File, Queue, Table) monitoring

# Azure Storage Account Classic (Blob, File, Queue, Table) monitoring

* Latest Dynatrace
* How-to guide
* 11-min read
* Updated on Nov 15, 2023

Dynatrace ingests metrics for multiple preselected namespaces, including Azure Storage Account Classic. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.196+
* Environment ActiveGate version 1.195+

This service monitors a part of Storage Account Classic (`Microsoft.ClassicStorage/storageAccounts`). You can find the already monitored resources on the Azure overview page in the **Cloud services** section or use a dashboard preset.

To monitor resources of the `Microsoft.Storage/storageAccounts` (including Storage, StorageV2 and BlobStorage) type, check Storage Accounts and the **Storage accounts** section on the Azure overview page.

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

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

![Storage Account Classic](https://dt-cdn.net/images/storageaccountnew-2908-6a758a1c35.png)

## Available metrics

**Storage Account (Classic)**

| Name | Description | Unit | Dimensions | Recommended |
| --- | --- | --- | --- | --- |
| Availability | The percentage of availability for the storage service or the specified API operation. Availability is calculated by taking the TotalBillableRequests value and dividing it by the number of applicable requests, including those that produced unexpected errors. All unexpected errors result in reduced availability for the storage service or the specified API operation. | Percent | Authentication, GeoType, ApiName | Applicable |
| Egress | The amount of egress data, in bytes. This number includes egress from an external client into Azure Storage as well as egress within Azure. As a result, this number does not reflect billable egress. | Byte | Authentication, GeoType, ApiName | Applicable |
| Ingress | The amount of ingress data, in bytes. This number includes ingress from an external client into Azure Storage as well as ingress within Azure. | Byte | Authentication, GeoType, ApiName | Applicable |
| SuccessE2ELatency | The end-to-end latency of successful requests made to a storage service or the specified API operation, in milliseconds. This value includes the required processing time within Azure Storage to read the request, send the response, and receive acknowledgment of the response. | MilliSecond | Authentication, GeoType, ApiName | Applicable |
| SuccessServerLatency | The latency used by Azure Storage to process a successful request, in milliseconds. This value does not include the network latency specified in SuccessE2ELatency. | MilliSecond | Authentication, GeoType, ApiName |  |
| Transactions | The number of requests made to a storage service or the specified API operation. This number includes successful and failed requests, as well as requests which produced errors. Use ResponseType dimension for the number of different type of response. | Count | Authentication, GeoType, ResponseType, ApiName | Applicable |
| UsedCapacity | Account used capacity. | Byte |  | Applicable |

**Azure Storage Blob Services (Classic)**

This service monitors a part of Storage Account Classic (Microsoft.ClassicStorage/storageAccounts). You can find the already monitored resources on the Azure overview page in the `Cloud services` section or use a dashboard preset. To monitor resources of the Microsoft.Storage/storageAccounts type (including Storage, StorageV2 and BlobStorage), check Storage Accounts and the `Storage accounts` section on the Azure overview page.

| Name | Description | Unit | Dimensions | Recommended |
| --- | --- | --- | --- | --- |
| Availability | The percentage of availability for the storage service or the specified API operation. Availability is calculated by taking the TotalBillableRequests value and dividing it by the number of applicable requests, including those that produced unexpected errors. All unexpected errors result in reduced availability for the storage service or the specified API operation. | Percent | Authentication, GeoType, ApiName | Applicable |
| BlobCapacity | The amount of storage used by the storage accountâs Blob service in bytes. | Byte | BlobType | Applicable |
| BlobCount | The number of Blob in the storage accountâs Blob service. | Count | BlobType | Applicable |
| ContainerCount | The number of containers in the storage accountâs Blob service. | Count |  | Applicable |
| Egress | The amount of egress data, in bytes. This number includes egress from an external client into Azure Storage as well as egress within Azure. As a result, this number does not reflect billable egress. | Byte | Authentication, GeoType, ApiName | Applicable |
| IndexCapacity | The amount of storage used by ADLS Gen2 (Hierarchical) Index in bytes. | Byte |  |  |
| Ingress | The amount of ingress data, in bytes. This number includes ingress from an external client into Azure Storage as well as ingress within Azure. | Byte | Authentication, GeoType, ApiName | Applicable |
| SuccessE2ELatency | The end-to-end latency of successful requests made to a storage service or the specified API operation, in milliseconds. This value includes the required processing time within Azure Storage to read the request, send the response, and receive acknowledgment of the response. | MilliSecond | Authentication, GeoType, ApiName | Applicable |
| SuccessServerLatency | The latency used by Azure Storage to process a successful request, in milliseconds. This value does not include the network latency specified in SuccessE2ELatency. | MilliSecond | Authentication, GeoType, ApiName |  |
| Transactions | The number of requests made to a storage service or the specified API operation. This number includes successful and failed requests, as well as requests which produced errors. Use ResponseType dimension for the number of different type of response. | Count | Authentication, GeoType, ResponseType, ApiName | Applicable |

**Azure Storage File Services (Classic)**

This service monitors a part of Storage Account Classic (Microsoft.ClassicStorage/storageAccounts). You can find the already monitored resources in Azure overview page in `Cloud services` section or use a dashboard preset. To monitor resources of the Microsoft.Storage/storageAccounts type (including Storage, StorageV2 and BlobStorage), check Storage Accounts and the `Storage accounts` section on the Azure overview page.

| Name | Description | Unit | Dimensions | Recommended |
| --- | --- | --- | --- | --- |
| Availability | The percentage of availability for the storage service or the specified API operation. Availability is calculated by taking the TotalBillableRequests value and dividing it by the number of applicable requests, including those that produced unexpected errors. All unexpected errors result in reduced availability for the storage service or the specified API operation. | Percent | Authentication, FileShare, GeoType, ApiName | Applicable |
| Egress | The amount of egress data, in bytes. This number includes egress from an external client into Azure Storage as well as egress within Azure. As a result, this number does not reflect billable egress. | Byte | Authentication, FileShare, GeoType, ApiName | Applicable |
| FileCapacity | The amount of storage used by the storage accountâs File service in bytes. | Byte | FileShare | Applicable |
| FileCount | The number of file in the storage accountâs File service. | Count | FileShare | Applicable |
| FileShareCount | The number of file shares in the storage accountâs File service. | Count |  | Applicable |
| FileShareQuota | The upper limit on the amount of storage that can be used by Azure Files Service in bytes. | Byte | FileShare | Applicable |
| FileShareSnapshotCount | The number of snapshots present on the share in storage accountâs Files Service. | Count | FileShare |  |
| FileShareSnapshotSize | The amount of storage used by the snapshots in storage accountâs File service in bytes. | Byte | FileShare |  |
| Ingress | The amount of ingress data, in bytes. This number includes ingress from an external client into Azure Storage as well as ingress within Azure. | Byte | Authentication, FileShare, GeoType, ApiName | Applicable |
| SuccessE2ELatency | The end-to-end latency of successful requests made to a storage service or the specified API operation, in milliseconds. This value includes the required processing time within Azure Storage to read the request, send the response, and receive acknowledgment of the response. | MilliSecond | Authentication, FileShare, GeoType, ApiName | Applicable |
| SuccessServerLatency | The latency used by Azure Storage to process a successful request, in milliseconds. This value does not include the network latency specified in SuccessE2ELatency. | MilliSecond | Authentication, FileShare, GeoType, ApiName |  |
| Transactions | The number of requests made to a storage service or the specified API operation. This number includes successful and failed requests, as well as requests which produced errors. Use ResponseType dimension for the number of different type of response. | Count | Authentication, FileShare, GeoType, ResponseType, ApiName | Applicable |

**Azure Storage Queue Services (Classic)**

This service monitors a part of Storage Account Classic (Microsoft.ClassicStorage/storageAccounts). You can find the already monitored resources in Azure overview page in `Cloud services` section or use a dashboard preset. To monitor resources of type Microsoft.Storage/storageAccounts (including Storage, StorageV2 and BlobStorage), check Storage Accounts and Azure overview section `Storage accounts`.

| Name | Description | Unit | Dimensions | Recommended |
| --- | --- | --- | --- | --- |
| Availability | The percentage of availability for the storage service or the specified API operation. Availability is calculated by taking the TotalBillableRequests value and dividing it by the number of applicable requests, including those that produced unexpected errors. All unexpected errors result in reduced availability for the storage service or the specified API operation. | Percent | Authentication, GeoType, ApiName | Applicable |
| Egress | The amount of egress data, in bytes. This number includes egress from an external client into Azure Storage as well as egress within Azure. As a result, this number does not reflect billable egress. | Byte | Authentication, GeoType, ApiName | Applicable |
| Ingress | The amount of ingress data, in bytes. This number includes ingress from an external client into Azure Storage as well as ingress within Azure. | Byte | Authentication, GeoType, ApiName | Applicable |
| QueueCapacity | The amount of storage used by the storage accountâs Queue service in bytes. | Byte |  | Applicable |
| QueueCount | The number of queue in the storage accountâs Queue service. | Count |  | Applicable |
| QueueMessageCount | The approximate number of queue messages in the storage accountâs Queue service. | Count |  | Applicable |
| SuccessE2ELatency | The end-to-end latency of successful requests made to a storage service or the specified API operation, in milliseconds. This value includes the required processing time within Azure Storage to read the request, send the response, and receive acknowledgment of the response. | MilliSecond | Authentication, GeoType, ApiName | Applicable |
| SuccessServerLatency | The latency used by Azure Storage to process a successful request, in milliseconds. This value does not include the network latency specified in SuccessE2ELatency. | MilliSecond | Authentication, GeoType, ApiName |  |
| Transactions | The number of requests made to a storage service or the specified API operation. This number includes successful and failed requests, as well as requests which produced errors. | Count | Authentication, GeoType, ResponseType, ApiName | Applicable |

**Azure Storage Table Services (Classic)**

This service monitors a part of Storage Account Classic (Microsoft.ClassicStorage/storageAccounts). You can find the already monitored resources in Azure overview page in `Cloud services` section or use a dashboard preset. To monitor resources of the Microsoft.Storage/storageAccounts type (including Storage, StorageV2 and BlobStorage), check Storage Accounts and the `Storage accounts` section on the Azure overview page.

| Name | Description | Unit | Dimensions | Recommended |
| --- | --- | --- | --- | --- |
| Availability | The percentage of availability for the storage service or the specified API operation. Availability is calculated by taking the TotalBillableRequests value and dividing it by the number of applicable requests, including those that produced unexpected errors. All unexpected errors result in reduced availability for the storage service or the specified API operation. | Percent | Authentication, GeoType, ApiName | Applicable |
| Egress | The amount of egress data, in bytes. This number includes egress from an external client into Azure Storage as well as egress within Azure. As a result, this number does not reflect billable egress. | Byte | Authentication, GeoType, ApiName | Applicable |
| Ingress | The amount of ingress data, in bytes. This number includes ingress from an external client into Azure Storage as well as ingress within Azure. | Byte | Authentication, GeoType, ApiName | Applicable |
| SuccessE2ELatency | The end-to-end latency of successful requests made to a storage service or the specified API operation, in milliseconds. This value includes the required processing time within Azure Storage to read the request, send the response, and receive acknowledgment of the response. | MilliSecond | Authentication, GeoType, ApiName | Applicable |
| SuccessServerLatency | The latency used by Azure Storage to process a successful request, in milliseconds. This value does not include the network latency specified in SuccessE2ELatency. | MilliSecond | Authentication, GeoType, ApiName |  |
| TableCapacity | The amount of storage used by the storage accountâs Table service in bytes. | Byte |  | Applicable |
| TableCount | The number of table in the storage accountâs Table service. | Count |  | Applicable |
| TableEntityCount | The number of table entities in the storage accountâs Table service. | Count |  | Applicable |
| Transactions | The number of requests made to a storage service or the specified API operation. This number includes successful and failed requests, as well as requests which produced errors. Use ResponseType dimension for the number of different type of response. | Count | Authentication, GeoType, ResponseType, ApiName | Applicable |