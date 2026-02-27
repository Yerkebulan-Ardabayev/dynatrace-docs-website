---
title: Azure Cosmos DB Account (MongoDB) monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cosmos-db-account-mongodb
scraped: 2026-02-27T21:21:51.645810
---

# Azure Cosmos DB Account (MongoDB) monitoring

# Azure Cosmos DB Account (MongoDB) monitoring

* Latest Dynatrace
* How-to guide
* 5-min read
* Updated on Nov 15, 2023

For information about differences between classic services and other services, see [Migrate from Azure classic (formerly 'built-in') services to cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Migrate Azure classic services to their new versions.").

Dynatrace ingests metrics from Azure Metrics API for Azure Cosmos DB Account (MongoDB). You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

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

## Available metrics

This service monitors a part of Azure Cosmos DB Account (Microsoft.DocumentDB/databaseAccounts). While you have this service configured, you can't have Azure Cosmos Database (built-in) service turned on.

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| AddRegion | Region Added | Region | Count |  |
| AutoscaleMaxThroughput | Autoscale Max Throughput | Collection name, Database name | Count | Applicable |
| CreateAccount | Account Created |  | Count |  |
| DataUsage | Total data usage reported at 5 minutes granularity | Collection name, Database name, Region | Byte | Applicable |
| DeleteAccount | Account Deleted |  | Count |  |
| DocumentCount | Total document count reported at 5 minutes, 1 hour and 1 day granularity | Collection name, Database name, Region | Count | Applicable |
| DocumentQuota | Total storage quota reported at 5 minutes granularity | Collection name, Database name, Region | Byte | Applicable |
| IndexUsage | Total index usage reported at 5 minutes granularity | Collection name, Database name, Region | Byte | Applicable |
| MetadataRequests | Count of metadata requests. Cosmos DB maintains system metadata collection for each account, that allows you to enumerate collections, databases, etc, and their configurations, free of charge. | Collection name, Database name, Region, Status code | Count | Applicable |
| MongoCollectionCreate | Mongo Collection Created | Collection name, Database name | Count |  |
| MongoCollectionDelete | Mongo Collection Deleted | Collection name, Database name | Count |  |
| MongoCollectionThroughputUpdate | Mongo Collection Throughput Updated | Collection name, Database name | Count |  |
| MongoCollectionUpdate | Mongo Collection Updated | Collection name, Database name | Count |  |
| MongoDBDatabaseCreate | Mongo Database Created | Database name | Count |  |
| MongoDBDatabaseUpdate | Mongo Database Updated | Database name | Count |  |
| MongoDatabaseDelete | Mongo Database Deleted | Database name | Count |  |
| MongoDatabaseThroughputUpdate | Mongo Database Throughput Updated | Database name | Count |  |
| MongoRequestCharge | Mongo Request Units Consumed | Collection name, Command name, Database name, Error code, Region, Status | Count |  |
| MongoRequests | Number of Mongo Requests Made | Collection name, Command name, Database name, Error code, Region, Status | Count |  |
| NormalizedRUConsumption | Max RU consumption percentage per minute | Collection name, Collection rid, Database name, Partition key range ID, Physical partition ID, Region | Percent | Applicable |
| OfflineRegion | Region Offlined | Region, Status code | Count |  |
| OnlineRegion | Region Onlined | Region, Status code | Count |  |
| PhysicalPartitionSizeInfo | Physical Partition Size in bytes | Collection name, Database name, Physical partition ID, Region, Resource ID | Byte |  |
| PhysicalPartitionThroughputInfo | Physical Partition Throughput | Collection name, Database name, Physical partition ID, Region, Resource ID | Count |  |
| ProvisionedThroughput | Provisioned Throughput | Collection name, Database name | Count | Applicable |
| RegionFailover | Region Failed Over |  | Count |  |
| RemoveRegion | Region Removed | Region | Count |  |
| ReplicationLatency | P99 Replication Latency across source and target regions for geo-enabled account | Source region, Target region | MilliSecond |  |
| ServerSideLatency | Server Side Latency | Collection name, Connection mode, Database name, Operation type, Publicapi type, Region | MilliSecond | Applicable |
| ServerSideLatencyDirect | Server Side Latency in Direct Connection Mode | Collection name, Database name, Operation type, Publicapi type, Region | MilliSecond |  |
| ServerSideLatencyGateway | Server Side Latency in Gateway Connection Mode | Collection name, Database name, Operation type, Publicapi type, Region | MilliSecond |  |
| ServiceAvailability | Account requests availability at one hour, day or month granularity |  | Percent | Applicable |
| TotalRequestUnits | SQL Request Units consumed | Capacity type, Collection name, Database name, Operation type, Region, Status, Status code | Count | Applicable |
| TotalRequests | Number of requests made | Capacity type, Collection name, Database name, Operation type, Region, Status, Status code | Count | Applicable |
| UpdateAccountKeys | Account Keys Updated | Key type | Count |  |
| UpdateAccountNetworkSettings | Account Network Settings Updated |  | Count |  |
| UpdateAccountReplicationSettings | Account Replication Settings Updated |  | Count |  |
| UpdateDiagnosticsSettings | Account Diagnostic Settings Updated | Diagnostic settings name, Resource group name | Count |  |