---
title: Azure Cache for Redis monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cache-for-redis
scraped: 2026-02-28T21:33:26.642873
---

# Azure Cache for Redis monitoring

# Azure Cache for Redis monitoring

* Latest Dynatrace
* How-to guide
* 23-min read
* Updated on Nov 15, 2023

For information about differences between classic services and other services, see [Migrate from Azure classic (formerly 'built-in') services to cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Migrate Azure classic services to their new versions.").

Dynatrace ingests metrics from Azure Metrics API for Azure Cache for Redis. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

This service monitors a part of Azure Cache for Redis (`Microsoft.Cache/redis`).

While you have this service configured, you **can't** have Azure Redis Cache (built-in) service turned on.

Enterprise Azure Cache for Redis service (`Microsoft.Cache/redisEnterprise`) currently cannot be monitored; to request this type of monitoring, please create an RFE (Request for Enhancement).

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

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| Connected clients | The number of client connections to the cache. | Shard ID | Count | Applicable |
| Total operations | The total number of commands processed by the cache server. | Shard ID | Count | Applicable |
| Cache hits | The number of successful key lookups. | Shard ID | Count | Applicable |
| Cache misses | The number of failed key lookups. | Shard ID | Count | Applicable |
| Cache miss rate | The % of get requests that miss. | Shard ID | Percent | Applicable |
| Gets | The number of get operations from the cache. | Shard ID | Count |  |
| Sets | The number of set operations to the cache. | Shard ID | Count |  |
| Operations per second | The number of instantaneous operations per second executed on the cache. | Shard ID | Count |  |
| Evicted keys | The number of items evicted from the cache. | Shard ID | Count |  |
| Total keys | The total number of items in the cache. | Shard ID | Count |  |
| Expired keys | The number of items expired from the cache. | Shard ID | Count |  |
| Used memory | The amount of cache memory used for key/value pairs in the cache in MB. | Shard ID | Byte |  |
| Used memory percentage | The percentage of cache memory used for key/value pairs. | Shard ID | Percent | Applicable |
| Used memory RSS | The amount of cache memory used in MB, including fragmentation and metadata. | Shard ID | Byte |  |
| Server load | The percentage of cycles in which the Redis server is busy processing and not waiting idle for messages. | Shard ID | Percent |  |
| Cache write | The amount of data written to the cache in bytes per second. | Shard ID | BytePerSecond |  |
| Cache read | The amount of data read from the cache in bytes per second. | Shard ID | BytePerSecond |  |
| Connections created per second (instance based) | The number of instantaneous connections created per second on the cache via port 6379 or 6380 (SSL). | Shard ID, Primary, SSL | PerSecond |  |
| Connections closed per second (instance based) | The number of instantaneous connections closed per second on the cache via port 6379 or 6380 (SSL). | Shard ID, Primary, SSL | PerSecond |  |
| Connected clients (instance based) | The number of client connections to the cache. | Shard ID, Port, Primary | Count |  |
| Total operations (instance based) | The total number of commands processed by the cache server. | Shard ID, Port, Primary | Count |  |
| Cache hits (instance based) | The number of successful key lookups. | Shard ID, Port, Primary | Count |  |
| Cache misses (instance based) | The number of failed key lookups. | Shard ID, Port, Primary | Count |  |
| Gets (instance based) | The number of get operations from the cache. | Shard ID, Port, Primary | Count |  |
| Sets (instance based) | The number of set operations to the cache. | Shard ID, Port, Primary | Count |  |
| Operations per second (instance based) | The number of instantaneous operations per second executed on the cache. | Shard ID, Port, Primary | Count |  |
| Evicted keys (instance based) | The number of items evicted from the cache. | Shard ID, Port, Primary | Count |  |
| Total keys (instance based) | The total number of items in the cache. | Shard ID, Port, Primary | Count |  |
| Expired keys (instance based) | The number of items expired from the cache. | Shard ID, Port, Primary | Count |  |
| Used memory (instance based) | The amount of cache memory used for key/value pairs in the cache in MB. | Shard ID, Port, Primary | Byte |  |
| Used memory percentage (instance based) | The percentage of cache memory used for key/value pairs. | Shard ID, Port, Primary | Percent |  |
| Used memory RSS (instance based) | The amount of cache memory used in MB, including fragmentation and metadata. | Shard ID, Port, Primary | Byte |  |
| Server load (instance based) | The percentage of cycles in which the Redis server is busy processing and not waiting idle for messages. | Shard ID, Port, Primary | Percent |  |
| Cache write (instance based) | The amount of data written to the cache in bytes per second. | Shard ID, Port, Primary | BytePerSecond |  |
| Cache read (instance based) | The amount of data read from the cache in bytes per second. | Shard ID, Port, Primary | BytePerSecond |  |
| CPU (instance based) | The CPU utilization of the Azure Redis Cache server as a percentage. | Shard ID, Port, Primary | Percent |  |
| CPU | The CPU utilization of the Azure Redis Cache server as a percentage. | Shard ID | Percent | Applicable |
| Cache latency microseconds (preview) | The latency to the cache in microseconds. | Shard ID | Count |  |
| Errors | The number errors that occurred on the cache. | Shard ID, Error type | Count |  |
| Connected clients (shard 0) | The number of client connections to the cache. |  | Count |  |
| Total operations (shard 0) | The total number of commands processed by the cache server. |  | Count |  |
| Cache hits (shard 0) | The number of successful key lookups. |  | Count |  |
| Cache misses (shard 0) | The number of failed key lookups. |  | Count |  |
| Gets (shard 0) | The number of get operations from the cache. |  | Count |  |
| Sets (shard 0) | The number of set operations to the cache. |  | Count |  |
| Operations per second (shard 0) | The number of instantaneous operations per second executed on the cache. |  | Count |  |
| Evicted keys (shard 0) | The number of items evicted from the cache. |  | Count |  |
| Total keys (shard 0) | The total number of items in the cache. |  | Count |  |
| Expired keys (shard 0) | The number of items expired from the cache. |  | Count |  |
| Used memory (shard 0) | The amount of cache memory used for key/value pairs in the cache in MB. |  | Byte |  |
| Used memory RSS (shard 0) | The amount of cache memory used in MB, including fragmentation and metadata. |  | Byte |  |
| Server load (shard 0) | The percentage of cycles in which the Redis server is busy processing and not waiting idle for messages. |  | Percent |  |
| Cache write (shard 0) | The amount of data written to the cache in bytes per second. |  | BytePerSecond |  |
| Cache read (shard 0) | The amount of data read from the cache in bytes per second. |  | BytePerSecond |  |
| CPU (shard 0) | The CPU utilization of the Azure Redis Cache server as a percentage. |  | Percent |  |
| Connected clients (shard 1) | The number of client connections to the cache. |  | Count |  |
| Total operations (shard 1) | The total number of commands processed by the cache server. |  | Count |  |
| Cache hits (shard 1) | The number of successful key lookups. |  | Count |  |
| Cache misses (shard 1) | The number of failed key lookups. |  | Count |  |
| Gets (shard 1) | The number of get operations from the cache. |  | Count |  |
| Sets (shard 1) | The number of set operations to the cache. |  | Count |  |
| Operations per second (shard 1) | The number of instantaneous operations per second executed on the cache. |  | Count |  |
| Evicted keys (shard 1) | The number of items evicted from the cache. |  | Count |  |
| Total keys (shard 1) | The total number of items in the cache. |  | Count |  |
| Expired keys (shard 1) | The number of items expired from the cache. |  | Count |  |
| Used memory (shard 1) | The amount of cache memory used for key/value pairs in the cache in MB. |  | Byte |  |
| Used memory RSS (shard 1) | The amount of cache memory used in MB, including fragmentation and metadata. |  | Byte |  |
| Server load (shard 1) | The percentage of cycles in which the Redis server is busy processing and not waiting idle for messages. |  | Percent |  |
| Cache write (shard 1) | The amount of data written to the cache in bytes per second. |  | BytePerSecond |  |
| Cache read (shard 1) | The amount of data read from the cache in bytes per second. |  | BytePerSecond |  |
| CPU (shard 1) | The CPU utilization of the Azure Redis Cache server as a percentage. |  | Percent |  |
| Connected clients (shard 2) | The number of client connections to the cache. |  | Count |  |
| Total operations (shard 2) | The total number of commands processed by the cache server. |  | Count |  |
| Cache hits (shard 2) | The number of successful key lookups. |  | Count |  |
| Cache misses (shard 2) | The number of failed key lookups. |  | Count |  |
| Gets (shard 2) | The number of get operations from the cache. |  | Count |  |
| Sets (shard 2) | The number of set operations to the cache. |  | Count |  |
| Operations per second (shard 2) | The number of instantaneous operations per second executed on the cache. |  | Count |  |
| Evicted keys (shard 2) | The number of items evicted from the cache. |  | Count |  |
| Total keys (shard 2) | The total number of items in the cache. |  | Count |  |
| Expired keys (shard 2) | The number of items expired from the cache. |  | Count |  |
| Used memory (shard 2) | The amount of cache memory used for key/value pairs in the cache in MB. |  | Byte |  |
| Used memory RSS (shard 2) | The amount of cache memory used in MB, including fragmentation and metadata. |  | Byte |  |
| Server load (shard 2) | The percentage of cycles in which the Redis server is busy processing and not waiting idle for messages. |  | Percent |  |
| Cache write (shard 2) | The amount of data written to the cache in bytes per second. |  | BytePerSecond |  |
| Cache read (shard 2) | The amount of data read from the cache in bytes per second. |  | BytePerSecond |  |
| CPU (shard 2) | The CPU utilization of the Azure Redis Cache server as a percentage. |  | Percent |  |
| Connected clients (shard 3) | The number of client connections to the cache. |  | Count |  |
| Total operations (shard 3) | The total number of commands processed by the cache server. |  | Count |  |
| Cache hits (shard 3) | The number of successful key lookups. |  | Count |  |
| Cache misses (shard 3) | The number of failed key lookups. |  | Count |  |
| Gets (shard 3) | The number of get operations from the cache. |  | Count |  |
| Sets (shard 3) | The number of set operations to the cache. |  | Count |  |
| Operations per second (shard 3) | The number of instantaneous operations per second executed on the cache. |  | Count |  |
| Evicted keys (shard 3) | The number of items evicted from the cache. |  | Count |  |
| Total keys (shard 3) | The total number of items in the cache. |  | Count |  |
| Expired keys (shard 3) | The number of items expired from the cache. |  | Count |  |
| Used memory (shard 3) | The amount of cache memory used for key/value pairs in the cache in MB. |  | Byte |  |
| Used memory RSS (shard 3) | The amount of cache memory used in MB, including fragmentation and metadata. |  | Byte |  |
| Server load (shard 3) | The percentage of cycles in which the Redis server is busy processing and not waiting idle for messages. |  | Percent |  |
| Cache write (shard 3) | The amount of data written to the cache in bytes per second. |  | BytePerSecond |  |
| Cache read (shard 3) | The amount of data read from the cache in bytes per second. |  | BytePerSecond |  |
| CPU (shard 3) | The CPU utilization of the Azure Redis Cache server as a percentage. |  | Percent |  |
| Connected clients (shard 4) | The number of client connections to the cache. |  | Count |  |
| Total operations (shard 4) | The total number of commands processed by the cache server. |  | Count |  |
| Cache hits (shard 4) | The number of successful key lookups. |  | Count |  |
| Cache misses (shard 4) | The number of failed key lookups. |  | Count |  |
| Gets (shard 4) | The number of get operations from the cache. |  | Count |  |
| Sets (shard 4) | The number of set operations to the cache. |  | Count |  |
| Operations per second (shard 4) | The number of instantaneous operations per second executed on the cache. |  | Count |  |
| Evicted keys (shard 4) | The number of items evicted from the cache. |  | Count |  |
| Total keys (shard 4) | The total number of items in the cache. |  | Count |  |
| Expired keys (shard 4) | The number of items expired from the cache. |  | Count |  |
| Used memory (shard 4) | The amount of cache memory used for key/value pairs in the cache in MB. |  | Byte |  |
| Used memory RSS (shard 4) | The amount of cache memory used in MB, including fragmentation and metadata. |  | Byte |  |
| Server load (shard 4) | The percentage of cycles in which the Redis server is busy processing and not waiting idle for messages. |  | Percent |  |
| Cache write (shard 4) | The amount of data written to the cache in bytes per second. |  | BytePerSecond |  |
| Cache read (shard 4) | The amount of data read from the cache in bytes per second. |  | BytePerSecond |  |
| CPU (shard 4) | The CPU utilization of the Azure Redis Cache server as a percentage. |  | Percent |  |
| Connected clients (shard 5) | The number of client connections to the cache. |  | Count |  |
| Total operations (shard 5) | The total number of commands processed by the cache server. |  | Count |  |
| Cache hits (shard 5) | The number of successful key lookups. |  | Count |  |
| Cache misses (shard 5) | The number of failed key lookups. |  | Count |  |
| Gets (shard 5) | The number of get operations from the cache. |  | Count |  |
| Sets (shard 5) | The number of set operations to the cache. |  | Count |  |
| Operations per second (shard 5) | The number of instantaneous operations per second executed on the cache. |  | Count |  |
| Evicted keys (shard 5) | The number of items evicted from the cache. |  | Count |  |
| Total keys (shard 5) | The total number of items in the cache. |  | Count |  |
| Expired keys (shard 5) | The number of items expired from the cache. |  | Count |  |
| Used memory (shard 5) | The amount of cache memory used for key/value pairs in the cache in MB. |  | Byte |  |
| Used memory RSS (shard 5) | The amount of cache memory used in MB, including fragmentation and metadata. |  | Byte |  |
| Server load (shard 5) | The percentage of cycles in which the Redis server is busy processing and not waiting idle for messages. |  | Percent |  |
| Cache write (shard 5) | The amount of data written to the cache in bytes per second. |  | BytePerSecond |  |
| Cache read (shard 5) | The amount of data read from the cache in bytes per second. |  | BytePerSecond |  |
| CPU (shard 5) | The CPU utilization of the Azure Redis Cache server as a percentage. |  | Percent |  |
| Connected clients (shard 6) | The number of client connections to the cache. |  | Count |  |
| Total operations (shard 6) | The total number of commands processed by the cache server. |  | Count |  |
| Cache hits (shard 6) | The number of successful key lookups. |  | Count |  |
| Cache misses (shard 6) | The number of failed key lookups. |  | Count |  |
| Gets (shard 6) | The number of get operations from the cache. |  | Count |  |
| Sets (shard 6) | The number of set operations to the cache. |  | Count |  |
| Operations per second (shard 6) | The number of instantaneous operations per second executed on the cache. |  | Count |  |
| Evicted keys (shard 6) | The number of items evicted from the cache. |  | Count |  |
| Total keys (shard 6) | The total number of items in the cache. |  | Count |  |
| Expired keys (shard 6) | The number of items expired from the cache. |  | Count |  |
| Used memory (shard 6) | The amount of cache memory used for key/value pairs in the cache in MB. |  | Byte |  |
| Used memory RSS (shard 6) | The amount of cache memory used in MB, including fragmentation and metadata. |  | Byte |  |
| Server load (shard 6) | The percentage of cycles in which the Redis server is busy processing and not waiting idle for messages. |  | Percent |  |
| Cache write (shard 6) | The amount of data written to the cache in bytes per second. |  | BytePerSecond |  |
| Cache read (shard 6) | The amount of data read from the cache in bytes per second. |  | BytePerSecond |  |
| CPU (shard 6) | The CPU utilization of the Azure Redis Cache server as a percentage. |  | Percent |  |
| Connected clients (shard 7) | The number of client connections to the cache. |  | Count |  |
| Total operations (shard 7) | The total number of commands processed by the cache server. |  | Count |  |
| Cache hits (shard 7) | The number of successful key lookups. |  | Count |  |
| Cache misses (shard 7) | The number of failed key lookups. |  | Count |  |
| Gets (shard 7) | The number of get operations from the cache. |  | Count |  |
| Sets (shard 7) | The number of set operations to the cache. |  | Count |  |
| Operations per second (shard 7) | The number of instantaneous operations per second executed on the cache. |  | Count |  |
| Evicted keys (shard 7) | The number of items evicted from the cache. |  | Count |  |
| Total keys (shard 7) | The total number of items in the cache. |  | Count |  |
| Expired keys (shard 7) | The number of items expired from the cache. |  | Count |  |
| Used memory (shard 7) | The amount of cache memory used for key/value pairs in the cache in MB. |  | Byte |  |
| Used memory RSS (shard 7) | The amount of cache memory used in MB, including fragmentation and metadata. |  | Byte |  |
| Server load (shard 7) | The percentage of cycles in which the Redis server is busy processing and not waiting idle for messages. |  | Percent |  |
| Cache write (shard 7) | The amount of data written to the cache in bytes per second. |  | BytePerSecond |  |
| Cache read (shard 7) | The amount of data read from the cache in bytes per second. |  | BytePerSecond |  |
| CPU (shard 7) | The CPU utilization of the Azure Redis Cache server as a percentage. |  | Percent |  |
| Connected clients (shard 8) | The number of client connections to the cache. |  | Count |  |
| Total operations (shard 8) | The total number of commands processed by the cache server. |  | Count |  |
| Cache hits (shard 8) | The number of successful key lookups. |  | Count |  |
| Cache misses (shard 8) | The number of failed key lookups. |  | Count |  |
| Gets (shard 8) | The number of get operations from the cache. |  | Count |  |
| Sets (shard 8) | The number of set operations to the cache. |  | Count |  |
| Operations per second (shard 8) | The number of instantaneous operations per second executed on the cache. |  | Count |  |
| Evicted keys (shard 8) | The number of items evicted from the cache. |  | Count |  |
| Total keys (shard 8) | The total number of items in the cache. |  | Count |  |
| Expired keys (shard 8) | The number of items expired from the cache. |  | Count |  |
| Used memory (shard 8) | The amount of cache memory used for key/value pairs in the cache in MB. |  | Byte |  |
| Used memory RSS (shard 8) | The amount of cache memory used in MB, including fragmentation and metadata. |  | Byte |  |
| Server load (shard 8) | The percentage of cycles in which the Redis server is busy processing and not waiting idle for messages. |  | Percent |  |
| Cache write (shard 8) | The amount of data written to the cache in bytes per second. |  | BytePerSecond |  |
| Cache read (shard 8) | The amount of data read from the cache in bytes per second. |  | BytePerSecond |  |
| CPU (shard 8) | The CPU utilization of the Azure Redis Cache server as a percentage. |  | Percent |  |
| Connected clients (shard 9) | The number of client connections to the cache. |  | Count |  |
| Total operations (shard 9) | The total number of commands processed by the cache server. |  | Count |  |
| Cache hits (shard 9) | The number of successful key lookups. |  | Count |  |
| Cache misses (shard 9) | The number of failed key lookups. |  | Count |  |
| Gets (shard 9) | The number of get operations from the cache. |  | Count |  |
| Sets (shard 9) | The number of set operations to the cache. |  | Count |  |
| Operations per second (shard 9) | The number of instantaneous operations per second executed on the cache. |  | Count |  |
| Evicted keys (shard 9) | The number of items evicted from the cache. |  | Count |  |
| Total keys (shard 9) | The total number of items in the cache. |  | Count |  |
| Expired keys (shard 9) | The number of items expired from the cache. |  | Count |  |
| Used memory (shard 9) | The amount of cache memory used for key/value pairs in the cache in MB. |  | Byte |  |
| Used memory RSS (shard 9) | The amount of cache memory used in MB, including fragmentation and metadata. |  | Byte |  |
| Server load (shard 9) | The percentage of cycles in which the Redis server is busy processing and not waiting idle for messages. |  | Percent |  |
| Cache write (shard 9) | The amount of data written to the cache in bytes per second. |  | BytePerSecond |  |
| Cache read (shard 9) | The amount of data read from the cache in bytes per second. |  | BytePerSecond |  |
| CPU (shard 9) | The CPU utilization of the Azure Redis Cache server as a percentage. |  | Percent |  |
| Geo - replication healthy | The health status of geo-replication link. 1 if healthy and 0 if disconnected or unhealthy. | Shard ID | Count |  |
| Geo - replication data sync offset | Approximate amount of data in bytes that needs to be synchronized to geo-secondary cache. | Shard ID | Byte |  |
| Geo - replication connectivity lag | Time in seconds since last successful data synchronization with geo-primary cache. Value will continue to increase if the link status is down. | Shard ID | Second |  |
| Geo - replication full sync event started | Fired on initiation of a full synchronization event between geo-replicated caches. This metric reports 0 most of the time because geo-replication uses partial resynchronizations for any new data added after the initial full synchronization. | Shard ID | Count |  |
| Geo - replication full sync event finished | Fired on completion of a full synchronization event between geo-replicated caches. This metric reports 0 most of the time because geo-replication uses partial resynchronizations for any new data added after the initial full synchronization. | Shard ID | Count |  |