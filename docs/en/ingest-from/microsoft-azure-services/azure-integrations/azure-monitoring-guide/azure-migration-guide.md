---
title: Migrate from Azure classic (formerly 'built-in') services to cloud services
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide
scraped: 2026-02-23T21:40:06.671015
---

# Migrate from Azure classic (formerly 'built-in') services to cloud services

# Migrate from Azure classic (formerly 'built-in') services to cloud services

* Latest Dynatrace
* How-to guide
* 15-min read
* Updated on Jun 27, 2024

From the Azure overview page, you can access Dynatrace classic services and cloud services for Azure monitoring. Both types of services share the same Azure resources. However, classic services use a predefined set of metrics, so configuring which metrics to monitor, or determining which ones are already monitored, is not supported.

## Classic services vs cloud services

As previously mentioned, classic services and cloud services share the same Azure resources. However, cloud services support a wider range of configuration options, such as new metrics and customizable monitored metrics. To give you more customization options, weâve started the following:

* Adding more services to the **Cloud services** section so you can customize which metrics and dimensions you want to monitor.
* Adding more metrics for cloud services; not only are they configurable, but you can now monitor much more than before.
* Replacing the classic services with cloud services that have more configuration options regarding metrics and dimensions.

![public-cloud-services-section-infographic](https://dt-cdn.net/images/public-cloud-services-section-infographic-950-ccb7323d99.png)

If you're using classic services, we recommend migrating to cloud services to take advantage of the wider range of customizable configuration options.

## Impact of the migration

Even though classic and cloud services monitor the same Azure resources on Dynatrace side, they are monitored as two different entities.

* They have different entity IDs and metric keys.
* Data for each Dynatrace entity type is collected and stored separately.
* ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Breaking change You need to adapt the configuration of dashboards, alerts, and management zones based on entity ID or [metric keys with the monitored service type](#metrics).

You do have the option to choose from a classic or cloud service to preserve historical data, for now. But be aware of the following:

* Historical data is persisted on the classic services. If you switch back, monitored data will present gaps for the period in which the resources were monitored via the cloud service.
* You canât have both of them turned on simultaneously. Even though on Dynatrace side theyâre two different services, the legacy and new versions monitor the same Azure resource. If you had two versions switched on simultaneously, you would be charged double for polling the same data twice.
* If you turn on the new version, the classic version is turned off automatically, and vice versa.
* There is no direct link between entities containing historical and new data.
* Logs from [Azure log forwarder](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Use Azure log forwarding to ingest Azure logs.") are still linked to historical data and entities.

To monitor cloud services, you need to have [Environment ActiveGateï»¿](https://dt-url.net/sc0396g) configured.

## Changes in the UI

Your Azure overview page changes after configuring a new version of a service.

For example, letâs look at **Azure Storage Account**.

* If the legacy **Azure Storage Accounts** service is configured, this is what the **Storage accounts** section of the Azure overview looks like.

![azure-public-cloud-vct-dev1-storage](https://dt-cdn.net/images/azure-public-cloud-vct-dev1-storage-1449-46980fd72d.png)

* Select **Cloud services** to find new overview pages for the services.

![azure-public-cloud-vct-dev1-services](https://dt-cdn.net/images/azure-public-cloud-vct-dev1-services-1112-707a41c03e.png)

* After configuring **Azure Storage Account**, **Azure Storage Blob**, **Azure Storage File**, **Azure Storage Queue**, and **Azure Storage Table** services, this is what the **Storage accounts** section of the Azure overview looks like.

![azure-public-cloud-vct-dev1-storage](https://dt-cdn.net/images/azure-public-cloud-vct-dev1-storage-1452-a16425bb86.png)

* Additionally, you can configure metrics for cloud services via UI.

![azure-settings-manage-services](https://dt-cdn.net/images/azure-settings-manage-services-1297-d00845930c.png)

![azure-settings-storage-blob-services](https://dt-cdn.net/images/azure-settings-storage-blob-services-1311-5b78cf0ab1.png)

## Cloud services and their corresponding classic services

| new Cloud service | old Classic service |
| --- | --- |
| [Azure API Management Service](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-api-management-service "Monitor Azure API Management Service and view available metrics.") | [Azure API Management services (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-api-management-services-builtin "Monitor Azure API Management Services and view available metrics.") Deprecated |
| [Azure Application Gateway](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-application-gateway "Monitor Azure Application Gateway and view available metrics.") | [Azure Application Gateway (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-app-gateways-builtin "Monitor Azure Application Gateways and view available metrics.") |
| [Azure Basic Load Balancer](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-basic-load-balancer "Monitor Azure Basic Load Balancer and view available metrics.") | [Azure Load Balancer (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-load-balancers-builtin "Monitor Azure Load Balancers and view available metrics.") |
| [Azure Gateway Load Balancer](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-gateway-load-balancer "Monitor Azure Gateway Load Balancer and view available metrics.") | [Azure Load Balancer (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-load-balancers-builtin "Monitor Azure Load Balancers and view available metrics.") |
| [Azure Standard Load Balancer](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-standard-load-balancer "Monitor Azure Standard Load Balancer and view available metrics.") | [Azure Load Balancer (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-load-balancers-builtin "Monitor Azure Load Balancers and view available metrics.") |
| [Azure Cache for Redis](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cache-for-redis "Monitor Azure Cache for Redis and view available metrics.") | [Azure Redis (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-redis-cache-builtin "Monitor Azure Redis Cache and view available metrics.") |
| [Azure Cosmos DB Account (GlobalDocumentDB)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cosmos-db-account-globaldocumentdb "Monitor Azure Cosmos DB Account (GlobalDocumentDB) and view available metrics.") | [Azure Cosmos DB (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cosmos-db-builtin "Monitor Azure Cosmos DB and view available metrics.") |
| [Azure Cosmos DB Account (MongoDB)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cosmos-db-account-mongodb "Monitor Azure Cosmos DB Account (MongoDB) and view available metrics.") | [Azure Cosmos DB (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cosmos-db-builtin "Monitor Azure Cosmos DB and view available metrics.") |
| [Azure IoT Hub](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-iot-hub "Monitor Azure IoT Hub and view available metrics.") | [Azure IoT Hubs (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-iot-hub-builtin "Monitor Azure IoT Hub and view available metrics.") |
| [Azure SQL Server](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-server "Monitor Azure SQL Server and view available metrics.") | [Azure SQL (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-servers-builtin "Monitor Azure SQL Servers and view available metrics.") |
| [Azure SQL Database (DTU)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-database-dtu "Monitor Azure SQL Database (DTU) and view available metrics.") | [Azure SQL (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-servers-builtin "Monitor Azure SQL Servers and view available metrics.") |
| [Azure SQL Database (vCore)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-database-vcore "Monitor Azure SQL Database (vCore) and view available metrics.") | [Azure SQL (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-servers-builtin "Monitor Azure SQL Servers and view available metrics.") |
| [Azure SQL elastic pool (DTU)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-elastic-pool-dtu "Monitor Azure SQL elastic pool (DTU) and view available metrics.") | [Azure SQL (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-servers-builtin "Monitor Azure SQL Servers and view available metrics.") |
| [Azure SQL elastic pool (vCore)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-elastic-pool-vcore "Monitor Azure SQL elastic pool (vCore) and view available metrics.") | [Azure SQL (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-servers-builtin "Monitor Azure SQL Servers and view available metrics.") |
| [Azure Storage Account](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account "Monitor Azure Storage Account and view available metrics.") | [Azure Storage accounts (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account-builtin "Monitor Azure Storage Accounts and view available metrics.") |
| [Azure Storage Blob Services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account "Monitor Azure Storage Account and view available metrics.") | [Azure Storage accounts (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account-builtin "Monitor Azure Storage Accounts and view available metrics.") |
| [Azure Storage File Services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account "Monitor Azure Storage Account and view available metrics.") | [Azure Storage accounts (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account-builtin "Monitor Azure Storage Accounts and view available metrics.") |
| [Azure Storage Queue Services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account "Monitor Azure Storage Account and view available metrics.") | [Azure Storage accounts (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account-builtin "Monitor Azure Storage Accounts and view available metrics.") |
| [Azure Storage Table Services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account "Monitor Azure Storage Account and view available metrics.") | [Azure Storage accounts (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account-builtin "Monitor Azure Storage Accounts and view available metrics.") |

## Metrics migration

Below you can find tables with classic services metrics and their corresponding cloud services metrics. Empty cells indicate the lack of an identical corresponding metric.

### Azure API Management Service

| Classic service metric name | Classic service metric key | Cloud service metric name | Cloud service metric key |
| --- | --- | --- | --- |
| Failed requests | builtin:cloud.azure.apiMgmt.requests.failed | Requests | ext:cloud.azure.microsoft\_apimanagement.service.requests:filter(or(eq("Gateway response code", "400"), eq("Gateway response code category", "5xx"))) |
| Other requests | builtin:cloud.azure.apiMgmt.requests.other | Requests | ext:cloud.azure.microsoft\_apimanagement.service.requests:filter(and(ne("Gateway response code category", "1xx"), ne("Gateway response code category", "2xx"), ne("Gateway response code", "300"), ne("Gateway response code", "301"), ne("Gateway response code", "304"), ne("Gateway response code", "307"), ne("Gateway response code", "400"), ne("Gateway response code", "401"), ne("Gateway response code", "403"), ne("Gateway response code", "429"), ne("Gateway response code category", "5xx"))) |
| Successful requests | builtin:cloud.azure.apiMgmt.requests.successful | Requests | ext:cloud.azure.microsoft\_apimanagement.service.requests:filter(or(eq("Gateway response code category", "1xx"), eq("Gateway response code category", "2xx"), eq("Gateway response code", "300"), eq("Gateway response code", "301"), eq("Gateway response code", "304"), eq("Gateway response code", "307"))) |
| Total requests | builtin:cloud.azure.apiMgmt.requests.total | Requests | ext:cloud.azure.microsoft\_apimanagement.service.requests |
| Unauthorized requests | builtin:cloud.azure.apiMgmt.requests.unauth | Requests | ext:cloud.azure.microsoft\_apimanagement.service.requests:filter(or(eq("Gateway response code", "401"), eq("Gateway response code", "403"), eq("Gateway response code", "429"))) |
| Capacity | builtin:cloud.azure.apiMgmt.capacity | Capacity | ext:cloud.azure.microsoft\_apimanagement.service.capacity |
| Duration | builtin:cloud.azure.apiMgmt.duration | Overall duration of gateway requests | ext:cloud.azure.microsoft\_apimanagement.service.duration |

### Azure Application Gateway

| Classic service metric name | Classic service metric key | Cloud service metric name | Cloud service metric key |
| --- | --- | --- | --- |
| Healthy host count | builtin:cloud.azure.appGateway.backend.settings.pool.host.healthy | Healthy host count | ext:cloud.azure.microsoft\_network.applicationgateways.healthyhostcount |
| Unhealthy host count | builtin:cloud.azure.appGateway.backend.settings.pool.host.unhealthy | Unhealthy host count | ext:cloud.azure.microsoft\_network.applicationgateways.unhealthyhostcount |
| Requests failed | builtin:cloud.azure.appGateway.backend.settings.traffic.requests.failed | Failed requests | ext:cloud.azure.microsoft\_network.applicationgateways.failedrequests |
| Requests total | builtin:cloud.azure.appGateway.backend.settings.traffic.requests.total | Total requests | ext:cloud.azure.microsoft\_network.applicationgateways.totalrequests |
| Response status | builtin:cloud.azure.appGateway.http.status.response | Response status | ext:cloud.azure.microsoft\_network.applicationgateways.responsestatus |
| Current connections count | builtin:cloud.azure.appGateway.network.connections.count | Current connections | ext:cloud.azure.microsoft\_network.applicationgateways.currentconnections |
| Network throughput | builtin:cloud.azure.appGateway.network.throughput | Throughput | ext:cloud.azure.microsoft\_network.applicationgateways.throughput |

### Azure Load Balancers

| Classic service metric name | Classic service metric key | Cloud service metric name | Cloud service metric key |
| --- | --- | --- | --- |
| Load balancer DIP TCP availability | builtin:cloud.azure.loadbalancer.availability.dipTcp | Health probe status | ext:cloud.azure.microsoft\_network.loadbalancers.dipavailability:filter(eq("ProtocolType", "Tcp")) / 100 |
| Load balancer DIP UDP availability | builtin:cloud.azure.loadbalancer.availability.dipUdp | Health probe status | ext:cloud.azure.microsoft\_network.loadbalancers.dipavailability:filter(eq("ProtocolType", "Udp")) / 100 |
| Load Balancer VIP availability | builtin:cloud.azure.loadbalancer.availability.vip | Data path availability | ext:cloud.azure.microsoft\_network.loadbalancers.vipavailability / 100 |
| SNAT connections successful | builtin:cloud.azure.loadbalancer.snatConnection.est | SNAT connection count | ext:cloud.azure.microsoft\_network.loadbalancers.snatconnectioncount:filter(eq("ConnectionState" ,"Successful")) |
| SNAT connections pending | builtin:cloud.azure.loadbalancer.snatConnection.pending | SNAT connection count | ext:cloud.azure.microsoft\_network.loadbalancers.snatconnectioncount:filter(eq("ConnectionState" ,"Pending")) |
| SNAT connections failed | builtin:cloud.azure.loadbalancer.snatConnection.rej | SNAT connection count | ext:cloud.azure.microsoft\_network.loadbalancers.snatconnectioncount:filter(eq("ConnectionState" ,"Failed")) |
| Bytes received | builtin:cloud.azure.loadbalancer.traffic.byteIn | Byte count | ext:cloud.azure.microsoft\_network.loadbalancers.bytecount:filter(eq("Direction", "In")) |
| Bytes sent | builtin:cloud.azure.loadbalancer.traffic.byteOut | Byte count | ext:cloud.azure.microsoft\_network.loadbalancers.bytecount:filter(eq("Direction", "Out")) |
| Packets received | builtin:cloud.azure.loadbalancer.traffic.packetIn | Packet count | ext:cloud.azure.microsoft\_network.loadbalancers.packetcount:filter(eq("Direction", "In")) |
| Packets sent | builtin:cloud.azure.loadbalancer.traffic.packetOut | Packet count | ext:cloud.azure.microsoft\_network.loadbalancers.packetcount:filter(eq("Direction", "Out")) |
| SYN packets received | builtin:cloud.azure.loadbalancer.traffic.packetSynIn | SYN count | ext:cloud.azure.microsoft\_network.loadbalancers.syncount:filter(eq("Direction", "In")) |
| SYN packets sent | builtin:cloud.azure.loadbalancer.traffic.packetSynOut | SYN count | ext:cloud.azure.microsoft\_network.loadbalancers.syncount:filter(eq("Direction", "Out")) |

### Azure Cache for Redis

| Classic service metric name | Classic service metric key | Cloud service metric name | Cloud service metric key |
| --- | --- | --- | --- |
| Cache hits | builtin:cloud.azure.redis.cache.hits | Cache hits | ext:cloud.azure.microsoft\_cache.redis.cachehits |
| Cache misses | builtin:cloud.azure.redis.cache.misses | Cache misses | ext:cloud.azure.microsoft\_cache.redis.cachemisses |
| Read bytes/s | builtin:cloud.azure.redis.cache.read | Cache read | ext:cloud.azure.microsoft\_cache.redis.cacheread |
| Write bytes/s | builtin:cloud.azure.redis.cache.write | Cache write | ext:cloud.azure.microsoft\_cache.redis.cachewrite |
| Get commands | builtin:cloud.azure.redis.commands.get | Gets | ext:cloud.azure.microsoft\_cache.redis.getcommands |
| Set commands | builtin:cloud.azure.redis.commands.set | Sets | ext:cloud.azure.microsoft\_cache.redis.setcommands |
| Total no. of processed commands | builtin:cloud.azure.redis.commands.total | Total operations | ext:cloud.azure.microsoft\_cache.redis.totalcommandsprocessed |
| No. of evicted keys | builtin:cloud.azure.redis.keys.evicted | Evicted keys | ext:cloud.azure.microsoft\_cache.redis.evictedkeys |
| No. of expired keys | builtin:cloud.azure.redis.keys.expired | Expired keys | ext:cloud.azure.microsoft\_cache.redis.expiredkeys |
| Total no. of keys | builtin:cloud.azure.redis.keys.total | Total keys | ext:cloud.azure.microsoft\_cache.redis.totalkeys |
| Used memory | builtin:cloud.azure.redis.memory.used | Used memory | ext:cloud.azure.microsoft\_cache.redis.usedmemory |
| Used memory RSS | builtin:cloud.azure.redis.memory.usedRss | Used memory RSS | ext:cloud.azure.microsoft\_cache.redis.usedmemoryrss |
| Connected clients | builtin:cloud.azure.redis.connected | Connected clients | ext:cloud.azure.microsoft\_cache.redis.connectedclients |
| Server load | builtin:cloud.azure.redis.load | Server load | ext:cloud.azure.microsoft\_cache.redis.serverload |
| Processor time | builtin:cloud.azure.redis.processorTime | CPU | ext:cloud.azure.microsoft\_cache.redis.percentprocessortime |

### Azure Cosmos Database

| Classic service metric name | Classic service metric key | Cloud service metric name | Cloud service metric key |
| --- | --- | --- | --- |
| Available Storage | builtin:cloud.azure.cosmos.availableStorage | - | - |
| Data Usage | builtin:cloud.azure.cosmos.dataUsage | Data usage | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.datausage |
| Document Count | builtin:cloud.azure.cosmos.documentCount | Document count | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.documentcount |
| Document Quota | builtin:cloud.azure.cosmos.documentQuota | Document quota | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.documentquota |
| Index Usage | builtin:cloud.azure.cosmos.indexUsage | Index usage | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.indexusage |
| Metadata Requests | builtin:cloud.azure.cosmos.metadataRequests | Metadata requests | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.metadatarequests |
| Normalized request units consumption | builtin:cloud.azure.cosmos.normalizedRUConsumption | Normalized ru consumption | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.normalizedruconsumption |
| Provisioned Throughput | builtin:cloud.azure.cosmos.provisionedThroughput | Provisioned throughput | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.provisionedthroughput |
| Replication Latency | builtin:cloud.azure.cosmos.replicationLatency | P99 replication latency | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.replicationlatency |
| Total number of request units | builtin:cloud.azure.cosmos.requestUnits | Total request units | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.totalrequestunits |
| Total number of requests | builtin:cloud.azure.cosmos.requests | Total requests | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.totalrequests |
| Service Availability | builtin:cloud.azure.cosmos.serviceAvailability | Service availability | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.serviceavailability |

### Azure Iot Hub

| Classic service metric name | Classic service metric key | Cloud service metric name | Cloud service metric key |
| --- | --- | --- | --- |
| Commands abandoned | builtin:cloud.azure.iotHub.command.abandoned | C2D messages abandoned | ext:cloud.azure.microsoft\_devices.iothubs.c2d\_commands\_egress\_abandon\_success |
| Commands completed | builtin:cloud.azure.iotHub.command.completed | C2D message deliveries completed | ext:cloud.azure.microsoft\_devices.iothubs.c2d\_commands\_egress\_complete\_success |
| Commands rejected | builtin:cloud.azure.iotHub.command.rejected | C2D messages rejected | ext:cloud.azure.microsoft\_devices.iothubs.c2d\_commands\_egress\_reject\_success |
| Connected devices | builtin:cloud.azure.iotHub.device.connected | Connected devices | ext:cloud.azure.microsoft\_devices.iothubs.connecteddevicecount |
| Number of throttling errors | builtin:cloud.azure.iotHub.device.dailyThroughputThrottling | Number of throttling errors | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_telemetry\_ingress\_sendthrottle |
| Total device data usage | builtin:cloud.azure.iotHub.device.dataUsage | Total device data usage Total device data usage (preview) | ext:cloud.azure.microsoft\_devices.iothubs.devicedatausage ext:cloud.azure.microsoft\_devices.iothubs.devicedatausagev2 |
| Total devices | builtin:cloud.azure.iotHub.device.registered | Total devices | ext:cloud.azure.microsoft\_devices.iothubs.totaldevicecount |
| Messages delivered to the built-in endpoint (messages/events) | builtin:cloud.azure.iotHub.eventHub.builtInEventHub.messages.delivered | Routing - messages delivered to messages/events | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_egress\_builtin\_events |
| Message latency for the built-in endpoint (messages/events) | builtin:cloud.azure.iotHub.eventHub.builtInEventHub.averageLatencyMs | Routing - message latency for messages/events | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_latency\_builtin\_events |
| Messages delivered to Event Hub endpoints | builtin:cloud.azure.iotHub.eventHub.messages.delivered | Routing - messages delivered to event hub | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_egress\_eventhubs |
| Message latency for event hub endpoints | builtin:cloud.azure.iotHub.eventHub.averageLatencyMs | Routing - message latency for event hub | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_latency\_eventhubs |
| Dropped messages | builtin:cloud.azure.iotHub.messages.dropped | Routing - telemetry messages dropped | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_telemetry\_egress\_dropped |
| Invalid messages | builtin:cloud.azure.iotHub.messages.invalidForAllEndpoints | Routing - telemetry messages incompatible | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_telemetry\_egress\_invalid |
| Orphaned messages | builtin:cloud.azure.iotHub.messages.orphaned | Routing - telemetry messages orphaned | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_telemetry\_egress\_orphaned |
| Telemetry message send attempts | builtin:cloud.azure.iotHub.messages.sendAttempts | Telemetry message send attempts | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_telemetry\_ingress\_allprotocol |
| Telemetry messages sent | builtin:cloud.azure.iotHub.messages.sent | Telemetry messages sent | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_telemetry\_ingress\_success |
| Messages matching fallback condition | builtin:cloud.azure.iotHub.messages.sentToFallback | Routing - messages delivered to fallback | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_telemetry\_egress\_fallback |
| Message latency for service bus queue endpoints | builtin:cloud.azure.iotHub.serviceBus.queues.averageLatencyMs | Routing - message latency for service bus queue | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_latency\_servicebusqueues |
| Messages delivered to service bus queue endpoints | builtin:cloud.azure.iotHub.serviceBus.queues.messagesDelivered | Routing - messages delivered to service bus queue | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_egress\_servicebusqueues |
| Message latency for service bus topic endpoints | builtin:cloud.azure.iotHub.serviceBus.topics.averageLatencyMs | Routing - message latency for service bus topic | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_latency\_servicebustopics |
| Messages delivered to service bus topic endpoints | builtin:cloud.azure.iotHub.serviceBus.topics.messagesDelivered | Routing - messages delivered to service bus topic | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_egress\_servicebustopics |
| Message latency for storage endpoints | builtin:cloud.azure.iotHub.storageEndpoints.avgLatencyMs | Routing - message latency for storage | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_latency\_storage |
| Blobs written to storage | builtin:cloud.azure.iotHub.storageEndpoints.blobsWritten | Routing - blobs delivered to storage | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_egress\_storage\_blobs |
| Data written to storage | builtin:cloud.azure.iotHub.storageEndpoints.bytesWritten | Routing - data delivered to storage | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_egress\_storage\_bytes |
| Messages delivered to storage endpoints | builtin:cloud.azure.iotHub.storageEndpoints.messageDelivered | Routing - messages delivered to storage | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_egress\_storage |

### Azure SQL Server

#### Azure SQL Databases

| Classic service metric name | Classic service metric key | Cloud service metric name | Cloud service metric |
| --- | --- | --- | --- |
| Blocked by firewall | builtin:cloud.azure.sqlDatabase.connections.blockedByFirewall | Blocked by firewall | ext:cloud.azure.microsoft\_sql.servers.databases.blocked\_by\_firewall |
| Failed connections | builtin:cloud.azure.sqlDatabase.connections.failed | Failed connections - system errors Failed connections - user errors | ext:cloud.azure.microsoft\_sql.servers.databases.connection\_failed ext:cloud.azure.microsoft\_sql.servers.databases.connection\_failed\_user\_error |
| Successful connections | builtin:cloud.azure.sqlDatabase.connections.successful | Successful connections | ext:cloud.azure.microsoft\_sql.servers.databases.connection\_successful |
| DTU limit | builtin:cloud.azure.sqlDatabase.dtu.limit.count | DTU limit | ext:cloud.azure.microsoft\_sql.servers.databases.dtu\_limit |
| DTU used | builtin:cloud.azure.sqlDatabase.dtu.limit.used | DTU used | ext:cloud.azure.microsoft\_sql.servers.databases.dtu\_used |
| DTU percentage | builtin:cloud.azure.sqlDatabase.dtu.consumptionPerc | DTU percentage | ext:cloud.azure.microsoft\_sql.servers.databases.dtu\_consumption\_percent |
| Data I/O percentage | builtin:cloud.azure.sqlDatabase.io.dataRead | Data IO percentage | ext:cloud.azure.microsoft\_sql.servers.databases.physical\_data\_read\_percent |
| Log I/O percentage | builtin:cloud.azure.sqlDatabase.io.logWrite | Log IO percentage | ext:cloud.azure.microsoft\_sql.servers.databases.log\_write\_percent |
| Database size percentage | builtin:cloud.azure.sqlDatabase.storage.percent | Data space used percent | ext:cloud.azure.microsoft\_sql.servers.databases.storage\_percent |
| Total database size | builtin:cloud.azure.sqlDatabase.storage.totalBytes | Data space used | ext:cloud.azure.microsoft\_sql.servers.databases.storage |
| In-Memory OLTP storage percent | builtin:cloud.azure.sqlDatabase.storage.xtpPercent | ext:cloud.azure.microsoft\_sql.servers.databases.xtp\_storage\_percent | ext:cloud.azure.microsoft\_sql.servers.databases.xtp\_storage\_percent |
| CPU percentage | builtin:cloud.azure.sqlDatabase.cpuPercent | CPU percentage | ext:cloud.azure.microsoft\_sql.servers.databases.cpu\_percent |
| Deadlocks | builtin:cloud.azure.sqlDatabase.deadlocks | Deadlocks | ext:cloud.azure.microsoft\_sql.servers.databases.deadlock |
| Sessions percentage | builtin:cloud.azure.sqlDatabase.sessions | Sessions percentage | ext:cloud.azure.microsoft\_sql.servers.databases.sessions\_percent |
| Workers percentage | builtin:cloud.azure.sqlDatabase.workers | Workers percentage | ext:cloud.azure.microsoft\_sql.servers.databases.workers\_percent |

#### Azure SQL Database elastic pools

| Classic service metric name | Classic service metric key | Cloud service metric name | Cloud service metric key |
| --- | --- | --- | --- |
| Storage limit | builtin:cloud.azure.sqlElasticPool.dtu.storage.limitBytes | Data max size | ext:cloud.azure.microsoft\_sql.servers.elasticpools.storage\_limit |
| Database size percentage | builtin:cloud.azure.sqlElasticPool.dtu.storage.percent | Data space used percent | ext:cloud.azure.microsoft\_sql.servers.elasticpools.storage\_percent |
| Storage used | builtin:cloud.azure.sqlElasticPool.dtu.storage.usedBytes | Data space used | ext:cloud.azure.microsoft\_sql.servers.elasticpools.storage\_used |
| In-memory OLTP storage percent | builtin:cloud.azure.sqlElasticPool.dtu.storage.xtpPercent | In - memory OLTP storage percent | ext:cloud.azure.microsoft\_sql.servers.elasticpools.xtp\_storage\_percent |
| DTU percentage | builtin:cloud.azure.sqlElasticPool.dtu.consumption | DTU percentage | ext:cloud.azure.microsoft\_sql.servers.elasticpools.dtu\_consumption\_percent |
| eDTU limit | builtin:cloud.azure.sqlElasticPool.edtu.limit | EDTU limit | ext:cloud.azure.microsoft\_sql.servers.elasticpools.edtu\_limit |
| eDTU used | builtin:cloud.azure.sqlElasticPool.edtu.used | EDTU used | ext:cloud.azure.microsoft\_sql.servers.elasticpools.edtu\_used |
| Data I/O percentage | builtin:cloud.azure.sqlElasticPool.io.dataRead | Data IO percentage | ext:cloud.azure.microsoft\_sql.servers.elasticpools.physical\_data\_read\_percent |
| Log I/O percentage | builtin:cloud.azure.sqlElasticPool.io.logWrite | Log IO percentage | ext:cloud.azure.microsoft\_sql.servers.elasticpools.log\_write\_percent |
| CPU percentage | builtin:cloud.azure.sqlElasticPool.cpuPercent | CPU percentage | ext:cloud.azure.microsoft\_sql.servers.elasticpools.cpu\_percent |
| Sessions percentage | builtin:cloud.azure.sqlElasticPool.sessions | Sessions percentage | ext:cloud.azure.microsoft\_sql.servers.elasticpools.sessions\_percent |
| Workers percentage | builtin:cloud.azure.sqlElasticPool.workers | Workers percentage | ext:cloud.azure.microsoft\_sql.servers.elasticpools.workers\_percent |

### Azure Storage Account

| Classic service metric name | Classic service metric key | Cloud service metric name | Cloud service metric key |
| --- | --- | --- | --- |
| Transactions count | builtin:cloud.azure.storage.blob.transactions | Transactions | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.transactions |
| E2E success latency | builtin:cloud.azure.storage.blob.transactions.network.latency.success.e2e | Success E2E latency | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.transactions |
| Server success latency | builtin:cloud.azure.storage.blob.transactions.network.latency.success.server | Success server latency | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.successserverlatency |
| Egress bytes | builtin:cloud.azure.storage.blob.transactions.network.egress | Egress | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.egress |
| Ingress bytes | builtin:cloud.azure.storage.blob.transactions.network.ingress | Ingress | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.ingress |
| Blob capacity | builtin:cloud.azure.storage.blob.capacity | Blob capacity | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.blobcapacity |
| Blob container count | builtin:cloud.azure.storage.blob.containers | Blob container count | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.containercount |
| Blob count | builtin:cloud.azure.storage.blob.entities | Blob count | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.blobcount |
| Transactions count | builtin:cloud.azure.storage.file.transactions | Transactions | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.transactions |
| E2E success latency | builtin:cloud.azure.storage.file.transactions.network.latency.success.e2e | Success E2E latency | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.successe2elatency |
| Server success latency | builtin:cloud.azure.storage.file.transactions.network.latency.success.server | Success server latency | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.successserverlatency |
| Egress bytes | builtin:cloud.azure.storage.file.transactions.network.egress | Egress | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.egress |
| Ingress bytes | builtin:cloud.azure.storage.file.transactions.network.ingress | Ingress | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.ingress |
| File capacity | builtin:cloud.azure.storage.file.capacity | File capacity | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.filecapacity |
| File share count | builtin:cloud.azure.storage.file.containers | File share count | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.filesharecount |
| File count | builtin:cloud.azure.storage.file.entities | File count | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.filecount |
| Transactions count | builtin:cloud.azure.storage.queue.transactions | Transactions | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.transactions |
| E2E success latency | builtin:cloud.azure.storage.queue.transactions.network.latency.success.e2e | Success E2E latency | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.successe2elatency |
| Server success latency | builtin:cloud.azure.storage.queue.transactions.network.latency.success.server | Success server latency | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.successserverlatency |
| Egress bytes | builtin:cloud.azure.storage.queue.transactions.network.egress | Egress | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.egress |
| Ingress bytes | builtin:cloud.azure.storage.queue.transactions.network.ingress | Ingress | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.ingress |
| Queue capacity | builtin:cloud.azure.storage.queue.capacity | Queue capacity | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.queuecapacity |
| Queue count | builtin:cloud.azure.storage.queue.containers | Queue count | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.queuecount |
| Queue message count | builtin:cloud.azure.storage.queue.entities | Queue message count | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.queuemessagecount |
| Transactions count | builtin:cloud.azure.storage.table.transactions | Transactions | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.transactions |
| Server success latency | builtin:cloud.azure.storage.table.transactions.network.latency.success.server | Success server latency | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.successserverlatency |
| E2E success latency | builtin:cloud.azure.storage.table.transactions.network.latency.success.server.e2e | Success E2E latency | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.successe2elatency |
| Egress bytes | builtin:cloud.azure.storage.table.transactions.network.egress | Egress | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.egress |
| Ingress bytes | builtin:cloud.azure.storage.table.transactions.network.ingress | Ingress | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.ingress |
| Table capacity | builtin:cloud.azure.storage.table.capacity | Table capacity | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.tablecapacity |
| Table count | builtin:cloud.azure.storage.table.containers | Table count | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.tablecount |
| Table entity count | builtin:cloud.azure.storage.table.entities | Table entity count | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.tableentitycount |