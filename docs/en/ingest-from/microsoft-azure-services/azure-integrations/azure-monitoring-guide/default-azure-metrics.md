---
title: Classic (formerly 'built-in') Azure metrics
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/default-azure-metrics
scraped: 2026-03-01T21:20:47.773550
---

# Classic (formerly 'built-in') Azure metrics

# Classic (formerly 'built-in') Azure metrics

* Latest Dynatrace
* Reference
* 1-min read
* Updated on Jan 29, 2024

For information about differences between classic services and other services, see [Migrate from Azure classic (formerly 'built-in') services to cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Migrate Azure classic services to their new versions.").

The table below lists all Azure metrics that Dynatrace collects by default when you enable [Microsoft Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace.") monitoring.

For all other metrics collected by Dynatrace per configurable Azure service, see [cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics "Monitor Azure services with Dynatrace and view available metrics.") pages.

| Metric key | Name | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:cloud.azure.apiMgmt.requests.failed | Failed requests | Count | autoavgcountmaxminsum |
| builtin:cloud.azure.apiMgmt.requests.other | Other requests | Count | autoavgcountmaxminsum |
| builtin:cloud.azure.apiMgmt.requests.successful | Successful requests | Count | autoavgcountmaxminsum |
| builtin:cloud.azure.apiMgmt.requests.total | Total requests | Count | autoavgcountmaxminsum |
| builtin:cloud.azure.apiMgmt.requests.unauth | Unauthorized requests | Count | autoavgcountmaxminsum |
| builtin:cloud.azure.apiMgmt.capacity | Capacity | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.apiMgmt.duration | Duration | Millisecond | autoavgmaxmin |
| builtin:cloud.azure.appGateway.backend.settings.pool.host.healthy | Healthy host count | Count | autoavgmaxmin |
| builtin:cloud.azure.appGateway.backend.settings.pool.host.unhealthy | Unhealthy host count | Count | autoavgmaxmin |
| builtin:cloud.azure.appGateway.backend.settings.traffic.requests.failed | Requests failed | Count | autovalue |
| builtin:cloud.azure.appGateway.backend.settings.traffic.requests.total | Requests total | Count | autovalue |
| builtin:cloud.azure.appGateway.http.status.response | Response status | Count | autovalue |
| builtin:cloud.azure.appGateway.network.connections.count | Current connections count | Count | autoavgmaxmin |
| builtin:cloud.azure.appGateway.network.throughput | Network throughput | Byte/second | autoavgmaxmin |
| builtin:cloud.azure.appService.applicationQueue.requests | Requests in application queue | Count | autoavgmaxmin |
| builtin:cloud.azure.appService.functions.applicationQueue.requests | Requests in application queue | Count | autoavgmaxmin |
| builtin:cloud.azure.appService.functions.execution.count | Function execution count | Count | autovalue |
| builtin:cloud.azure.appService.functions.execution.unitsCount | Function execution units count | Count | autovalue |
| builtin:cloud.azure.appService.functions.http.status.http5xx | HTTP 5xx | Count | autovalue |
| builtin:cloud.azure.appService.functions.io.operations.other | IO other operations/s | Per second | autoavgmaxmin |
| builtin:cloud.azure.appService.functions.io.operations.read | IO read operations/s | Per second | autoavgmaxmin |
| builtin:cloud.azure.appService.functions.io.operations.write | IO write operations/s | Per second | autoavgmaxmin |
| builtin:cloud.azure.appService.functions.io.other | IO other bytes/s | Byte/second | autoavgmaxmin |
| builtin:cloud.azure.appService.functions.io.read | IO read bytes/s | Byte/second | autoavgmaxmin |
| builtin:cloud.azure.appService.functions.io.write | IO write bytes/s | Byte/second | autoavgmaxmin |
| builtin:cloud.azure.appService.functions.traffic.bytesReceived | Received bytes | Byte | autovalue |
| builtin:cloud.azure.appService.functions.traffic.bytesSent | Sent bytes | Byte | autovalue |
| builtin:cloud.azure.appService.http.status.http2xx | HTTP 2xx | Count | autovalue |
| builtin:cloud.azure.appService.http.status.http403 | HTTP 403 | Count | autovalue |
| builtin:cloud.azure.appService.http.status.http5xx | HTTP 5xx | Count | autovalue |
| builtin:cloud.azure.appService.io.operations.other | IO other operations/s | Per second | autoavgmaxmin |
| builtin:cloud.azure.appService.io.operations.read | IO read operations/s | Per second | autoavgmaxmin |
| builtin:cloud.azure.appService.io.operations.write | IO write operations/s | Per second | autoavgmaxmin |
| builtin:cloud.azure.appService.io.other | IO other bytes/s | Byte/second | autoavgmaxmin |
| builtin:cloud.azure.appService.io.read | IO read bytes/s | Byte/second | autoavgmaxmin |
| builtin:cloud.azure.appService.io.write | IO write bytes/s | Byte/second | autoavgmaxmin |
| builtin:cloud.azure.appService.response.avg | Response time avg | Second | autoavgmaxmin |
| builtin:cloud.azure.appService.traffic.bytesReceived | Received bytes | Byte | autovalue |
| builtin:cloud.azure.appService.traffic.bytesSent | Sent bytes | Byte | autovalue |
| builtin:cloud.azure.appService.traffic.requests | Requests count | Count | autovalue |
| builtin:cloud.azure.cosmos.availableStorage | Available Storage | Byte | autoavgmaxmin |
| builtin:cloud.azure.cosmos.dataUsage | Data Usage | Byte | autoavgmaxmin |
| builtin:cloud.azure.cosmos.documentCount | Document Count | Count | autoavgmaxmin |
| builtin:cloud.azure.cosmos.documentQuota | Document Quota | Byte | autoavgmaxmin |
| builtin:cloud.azure.cosmos.indexUsage | Index Usage | Byte | autoavgmaxmin |
| builtin:cloud.azure.cosmos.metadataRequests | Metadata Requests | Count | autoavgmaxmin |
| builtin:cloud.azure.cosmos.normalizedRUConsumption | Normalized request units consumption | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.cosmos.provisionedThroughput | Provisioned Throughput | Count | autoavgmaxmin |
| builtin:cloud.azure.cosmos.replicationLatency | Replication Latency | Millisecond | autoavgmaxmin |
| builtin:cloud.azure.cosmos.requestUnits | Total number of request units | Count | autoavgmaxmin |
| builtin:cloud.azure.cosmos.requests | Total number of requests | Count | autoavgmaxmin |
| builtin:cloud.azure.cosmos.serviceAvailability | Service Availability | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.eventHub.capture.backlog | Capture backlog | Count | autovalue |
| builtin:cloud.azure.eventHub.capture.bytes | Captured bytes | Byte | autovalue |
| builtin:cloud.azure.eventHub.capture.msg | Captured messages | Count | autovalue |
| builtin:cloud.azure.eventHub.errors.quotaExceeded | Quota exceeded errors | Count | autovalue |
| builtin:cloud.azure.eventHub.errors.server | Server errors | Count | autovalue |
| builtin:cloud.azure.eventHub.errors.user | User errors | Count | autovalue |
| builtin:cloud.azure.eventHub.requests.incoming | Incoming requests | Count | autovalue |
| builtin:cloud.azure.eventHub.requests.successful | Successful requests | Count | autovalue |
| builtin:cloud.azure.eventHub.requests.throttled | Throttled requests | Count | autovalue |
| builtin:cloud.azure.eventHub.traffic.bytesIn | Incoming bytes | Byte/minute | autovalue |
| builtin:cloud.azure.eventHub.traffic.bytesOut | Outgoing bytes | Byte | autovalue |
| builtin:cloud.azure.eventHub.traffic.msgIn | Incoming messages | Count | autovalue |
| builtin:cloud.azure.eventHub.traffic.msgOut | Outgoing messages | Count | autovalue |
| builtin:cloud.azure.eventHubNamespace.connections.active | Active connections | Count | autoavgmaxmin |
| builtin:cloud.azure.eventHubNamespace.connections.closed | Closed connections | Count | autoavgmaxmin |
| builtin:cloud.azure.eventHubNamespace.connections.opened | Opened connections | Count | autoavgmaxmin |
| builtin:cloud.azure.iotHub.command.abandoned | Commands abandoned | Count | autovalue |
| builtin:cloud.azure.iotHub.command.completed | Commands completed | Count | autovalue |
| builtin:cloud.azure.iotHub.command.rejected | Commands rejected | Count | autovalue |
| builtin:cloud.azure.iotHub.device.connected | Connected devices | Count | autoavgmaxmin |
| builtin:cloud.azure.iotHub.device.dailyThroughputThrottling | Number of throttling errors | Count | autovalue |
| builtin:cloud.azure.iotHub.device.dataUsage | Total device data usage | Byte | autoavgmaxmin |
| builtin:cloud.azure.iotHub.device.registered | Total devices | Count | autoavgmaxmin |
| builtin:cloud.azure.iotHub.eventHub.builtInEventHub.messages.delivered | Messages delivered to the built-in endpoint (messages/events) | Count | autovalue |
| builtin:cloud.azure.iotHub.eventHub.builtInEventHub.averageLatencyMs | Message latency for the built-in endpoint (messages/events) | Millisecond | autoavgmaxmin |
| builtin:cloud.azure.iotHub.eventHub.messages.delivered | Messages delivered to Event Hub endpoints | Count | autovalue |
| builtin:cloud.azure.iotHub.eventHub.averageLatencyMs | Message latency for event hub endpoints | Millisecond | autoavgmaxmin |
| builtin:cloud.azure.iotHub.messages.dropped | Dropped messages | Count | autovalue |
| builtin:cloud.azure.iotHub.messages.invalidForAllEndpoints | Invalid messages | Count | autovalue |
| builtin:cloud.azure.iotHub.messages.orphaned | Orphaned messages | Count | autovalue |
| builtin:cloud.azure.iotHub.messages.sendAttempts | Telemetry message send attempts | Count | autovalue |
| builtin:cloud.azure.iotHub.messages.sent | Telemetry messages sent | Count | autovalue |
| builtin:cloud.azure.iotHub.messages.sentToFallback | Messages matching fallback condition | Count | autovalue |
| builtin:cloud.azure.iotHub.serviceBus.queues.averageLatencyMs | Message latency for service bus queue endpoints | Millisecond | autoavgmaxmin |
| builtin:cloud.azure.iotHub.serviceBus.queues.messagesDelivered | Messages delivered to service bus queue endpoints | Count | autovalue |
| builtin:cloud.azure.iotHub.serviceBus.topics.averageLatencyMs | Message latency for service bus topic endpoints | Millisecond | autoavgmaxmin |
| builtin:cloud.azure.iotHub.serviceBus.topics.messagesDelivered | Messages delivered to service bus topic endpoints | Count | autovalue |
| builtin:cloud.azure.iotHub.storageEndpoints.avgLatencyMs | Message latency for storage endpoints | Millisecond | autoavgmaxmin |
| builtin:cloud.azure.iotHub.storageEndpoints.blobsWritten | Blobs written to storage | Count | autovalue |
| builtin:cloud.azure.iotHub.storageEndpoints.bytesWritten | Data written to storage | Byte | autoavgmaxmin |
| builtin:cloud.azure.iotHub.storageEndpoints.messageDelivered | Messages delivered to storage endpoints | Count | autovalue |
| builtin:cloud.azure.loadbalancer.availability.dipTcp | Load balancer DIP TCP availability | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.loadbalancer.availability.dipUdp | Load balancer DIP UDP availability | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.loadbalancer.availability.vip | Load Balancer VIP availability | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.loadbalancer.snatConnection.est | SNAT connections successful | Count | autovalue |
| builtin:cloud.azure.loadbalancer.snatConnection.pending | SNAT connections pending | Count | autovalue |
| builtin:cloud.azure.loadbalancer.snatConnection.rej | SNAT connections failed | Count | autovalue |
| builtin:cloud.azure.loadbalancer.traffic.byteIn | Bytes received | Byte | autovalue |
| builtin:cloud.azure.loadbalancer.traffic.byteOut | Bytes sent | Byte | autovalue |
| builtin:cloud.azure.loadbalancer.traffic.packetIn | Packets received | Count | autovalue |
| builtin:cloud.azure.loadbalancer.traffic.packetOut | Packets sent | Count | autovalue |
| builtin:cloud.azure.loadbalancer.traffic.packetSynIn | SYN packets received | Count | autovalue |
| builtin:cloud.azure.loadbalancer.traffic.packetSynOut | SYN packets sent | Count | autovalue |
| builtin:cloud.azure.redis.cache.hits | Cache hits | Count | autovalue |
| builtin:cloud.azure.redis.cache.misses | Cache misses | Count | autovalue |
| builtin:cloud.azure.redis.cache.read | Read bytes/s | Byte/second | autoavgmaxmin |
| builtin:cloud.azure.redis.cache.write | Write bytes/s | Byte/second | autoavgmaxmin |
| builtin:cloud.azure.redis.commands.get | Get commands | Count | autovalue |
| builtin:cloud.azure.redis.commands.set | Set commands | Count | autovalue |
| builtin:cloud.azure.redis.commands.total | Total no. of processed commands | Count | autovalue |
| builtin:cloud.azure.redis.keys.evicted | No. of evicted keys | Count | autovalue |
| builtin:cloud.azure.redis.keys.expired | No. of expired keys | Count | autovalue |
| builtin:cloud.azure.redis.keys.total | Total no. of keys | Count | autoavgmaxmin |
| builtin:cloud.azure.redis.memory.used | Used memory | Byte | autoavgmaxmin |
| builtin:cloud.azure.redis.memory.usedRss | Used memory RSS | Byte | autoavgmaxmin |
| builtin:cloud.azure.redis.connected | Connected clients | Count | autoavgmaxmin |
| builtin:cloud.azure.redis.load | Server load | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.redis.processorTime | Processor time | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.region.vms.initializing | Number of starting VMs in region | Count | autoavgmaxmin |
| builtin:cloud.azure.region.vms.running | Number of active VMs in region | Count | autoavgmaxmin |
| builtin:cloud.azure.region.vms.stopped | Number of stopped VMs in region | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.namespace.connections.active | Total active connections | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.namespace.errors.server | Server errors | Count | autovalue |
| builtin:cloud.azure.serviceBus.namespace.errors.user | User errors | Count | autovalue |
| builtin:cloud.azure.serviceBus.namespace.messages.count | Count of messages | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.namespace.messages.countActive | Count of active messages | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.namespace.messages.countDeadLettered | Count of dead-lettered messages | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.namespace.messages.countScheduled | Count of scheduled messages | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.namespace.messages.incoming | Incoming messages | Count | autovalue |
| builtin:cloud.azure.serviceBus.namespace.messages.outgoing | Outgoing messages | Count | autovalue |
| builtin:cloud.azure.serviceBus.namespace.requests.incoming | Incoming requests | Count | autovalue |
| builtin:cloud.azure.serviceBus.namespace.requests.successful | Total successful requests | Count | autovalue |
| builtin:cloud.azure.serviceBus.namespace.requests.throttled | Throttled requests | Count | autovalue |
| builtin:cloud.azure.serviceBus.namespace.cpu | Service bus premium namespace CPU usage metric | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.namespace.memory | Service bus premium namespace memory usage metric | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.namespace.size | Service bus size | Byte | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.queue.errors.server | Server errors | Count | autovalue |
| builtin:cloud.azure.serviceBus.queue.errors.user | User errors | Count | autovalue |
| builtin:cloud.azure.serviceBus.queue.messages.count | Count of messages in queue | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.queue.messages.countActive | Count of active messages in a queue | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.queue.messages.countDeadLettered | Count of dead-lettered messages in a queue | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.queue.messages.countScheduled | Count of scheduled messages in a queue | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.queue.messages.incoming | Incoming messages | Count | autovalue |
| builtin:cloud.azure.serviceBus.queue.messages.outgoing | Outgoing messages | Count | autovalue |
| builtin:cloud.azure.serviceBus.queue.requests.incoming | Incoming requests | Count | autovalue |
| builtin:cloud.azure.serviceBus.queue.requests.successful | Total successful requests | Count | autovalue |
| builtin:cloud.azure.serviceBus.queue.requests.throttled | Throttled requests | Count | autovalue |
| builtin:cloud.azure.serviceBus.queue.size | Size of an queue | Byte | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.topic.errors.server | Server errors | Count | autovalue |
| builtin:cloud.azure.serviceBus.topic.errors.user | User errors | Count | autovalue |
| builtin:cloud.azure.serviceBus.topic.messages.count | Count of messages in topic | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.topic.messages.countActive | Count of active messages in a topic | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.topic.messages.countDeadLettered | Count of dead-lettered messages in a topic | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.topic.messages.countScheduled | Count of scheduled messages in a topic | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.topic.messages.incoming | Incoming messages | Count | autovalue |
| builtin:cloud.azure.serviceBus.topic.messages.outgoing | Outgoing messages | Count | autovalue |
| builtin:cloud.azure.serviceBus.topic.requests.incoming | Incoming requests | Count | autovalue |
| builtin:cloud.azure.serviceBus.topic.requests.successful | Total successful requests | Count | autovalue |
| builtin:cloud.azure.serviceBus.topic.requests.throttled | Throttled requests | Count | autovalue |
| builtin:cloud.azure.serviceBus.topic.size | Size of a topic | Byte | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.connections.blockedByFirewall | Blocked by firewall | Count | autovalue |
| builtin:cloud.azure.sqlDatabase.connections.failed | Failed connections | Count | autovalue |
| builtin:cloud.azure.sqlDatabase.connections.successful | Successful connections | Count | autovalue |
| builtin:cloud.azure.sqlDatabase.dtu.limit.count | DTU limit | Count | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.dtu.limit.used | DTU used | Count | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.dtu.consumptionPerc | DTU percentage | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.io.dataRead | Data I/O percentage | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.io.logWrite | Log I/O percentage | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.storage.percent | Database size percentage | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.storage.totalBytes | Total database size | Byte | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.storage.xtpPercent | In-Memory OLTP storage percent | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.cpuPercent | CPU percentage | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.deadlocks | Deadlocks | Count | autovalue |
| builtin:cloud.azure.sqlDatabase.sessions | Sessions percentage | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.workers | Workers percentage | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.dtu.storage.limitBytes | Storage limit | Byte | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.dtu.storage.percent | Database size percentage | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.dtu.storage.usedBytes | Storage used | Byte | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.dtu.storage.xtpPercent | In-memory OLTP storage percent | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.dtu.consumption | DTU percentage | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.edtu.limit | eDTU limit | Count | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.edtu.used | eDTU used | Count | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.io.dataRead | Data I/O percentage | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.io.logWrite | Log I/O percentage | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.cpuPercent | CPU percentage | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.sessions | Sessions percentage | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.workers | Workers percentage | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.vm.disk.read | Disk read bytes | Byte | autovalue |
| builtin:cloud.azure.vm.disk.readOps | Disk read operations per sec | Per second | autoavgmaxmin |
| builtin:cloud.azure.vm.disk.write | Disk write bytes | Byte | autovalue |
| builtin:cloud.azure.vm.disk.writeOps | Disk write operations per sec | Per second | autoavgmaxmin |
| builtin:cloud.azure.vm.network.bytesIn | Network in bytes | Byte | autovalue |
| builtin:cloud.azure.vm.network.bytesOut | Network out bytes | Byte | autovalue |
| builtin:cloud.azure.vm.cpuUsage | Percentage CPU | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.vmScaleSet.disk.read | Disk read bytes | Byte | autovalue |
| builtin:cloud.azure.vmScaleSet.disk.readOps | Disk read operations per sec | Per second | autoavgmaxmin |
| builtin:cloud.azure.vmScaleSet.disk.write | Disk write bytes | Byte | autovalue |
| builtin:cloud.azure.vmScaleSet.disk.writeOps | Disk write operations per sec | Per second | autoavgmaxmin |
| builtin:cloud.azure.vmScaleSet.network.bytesIn | Network in bytes | Byte | autovalue |
| builtin:cloud.azure.vmScaleSet.network.bytesOut | Network out bytes | Byte | autovalue |
| builtin:cloud.azure.vmScaleSet.vms.initializing | Number of starting VMs in scale set | Count | autoavgmaxmin |
| builtin:cloud.azure.vmScaleSet.vms.running | Number of active VMs in scale set | Count | autoavgmaxmin |
| builtin:cloud.azure.vmScaleSet.vms.stopped | Number of stopped VMs in scale set | Count | autoavgmaxmin |
| builtin:cloud.azure.vmScaleSet.cpuUsage | Percentage CPU | Percent (%) | autoavgmaxmin |