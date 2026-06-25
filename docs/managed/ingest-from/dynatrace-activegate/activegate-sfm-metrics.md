---
title: ActiveGate self-monitoring metrics
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/activegate-sfm-metrics
scraped: 2026-05-12T12:13:50.279924
---

# ActiveGate self-monitoring metrics

# ActiveGate self-monitoring metrics

* 1-min read
* Published Dec 03, 2021

Dynatrace offers a special self-monitoring category of metrics to provide observability into the operation and health of Dynatrace components and features. These metrics are available in every Dynatrace Managed and SaaS environment and can be identified by the `dsfm:` metric prefix.

For more information, see [Self-monitoring metrics](/managed/analyze-explore-automate/metrics-classic/self-monitoring-metrics "Explore the complete list of self-monitoring Dynatrace metrics.").

Following is the list of self-monitoring metrics that can be used to get insights into the operation of an ActiveGate.

## Active gate

### AWS

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| dsfm:active\_gate.aws.elements.bad | Active Gate - Aws - Elements - Bad  Count of elements that were successfully retrieved from AWS, but failed later on (e.g., due to parsing errors). Elements are e.g., number of metrics for metric query, number of instances for instances query etc. | Count | autovalue |
| dsfm:active\_gate.aws.elements.reported | Active Gate - Aws - Elements - Reported  Count of elements that were successfully reported (sent) to the server by ActiveGate. Elements are e.g., number of metrics for metric query, number of instances for instances query etc. | Count | autovalue |
| dsfm:active\_gate.aws.elements.total | Active Gate - Aws - Elements - Total  Count of all elements retrieved in the given timeframe. Elements are e.g., number of metrics for metric query, number of instances for instances query etc. | Count | autovalue |
| dsfm:active\_gate.aws.data\_delay | Active Gate - Aws - Data Delay  Sum of data delay (difference between expected last timestamp and actual last timestamp) for all entity and metric combinations | Millisecond | autovalue |
| dsfm:active\_gate.aws.data\_lost | Active Gate - Aws - Data Lost  Flag indicating whether we failed to obtain some of the data. 0 - all data obtained, 1 - some data lost. | Count | autovalue |
| dsfm:active\_gate.aws.data\_lost\_monitoring\_status | Active Gate - Aws - Data Lost Monitoring Status  Flag indicating whether we failed to obtain some of the data. 0 - all data obtained, 1 - some data lost. | Count | autoavgcountmaxminsum |
| dsfm:active\_gate.aws.empty\_responses | Active Gate - Aws - Empty Responses  Count of requests whose responses were empty even though we expected some data. | Count | autovalue |
| dsfm:active\_gate.aws.missing\_permissions | Active Gate - Aws - Missing Permissions  Missing Permissions in AWS monitoring | Count | autoavgcountmaxminsum |
| dsfm:active\_gate.aws.monitored\_entities | Active Gate - Aws - Monitored Entities  Number of monitored entities per AWS Credentials | Count | autovalue |
| dsfm:active\_gate.aws.monitored\_entities\_infrastructure\_size | Active Gate - Aws - Monitored Entities Infrastructure Size  Current number of monitored entities per AWS Credentials. | Count | autoavgcountmaxminsum |
| dsfm:active\_gate.aws.query\_time | Active Gate - Aws - Query Time  Summed time in milliseconds of all queries in the given timeframe. | Millisecond | autovalue |
| dsfm:active\_gate.aws.requests | Active Gate - Aws - Requests  Count of performed HTTP requests. | Count | autovalue |

### Communication

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| dsfm:active\_gate.communication.agent\_modules.connected | Active Gate - Communication - Agent Modules - Connected  Number of OneAgent modules connected. | Count | autoavgcountmaxminsum |
| dsfm:active\_gate.communication.messages.dropped | Active Gate - Communication - Messages - Dropped  Number of messages dropped due to timeouts. Non-zero value may indicate data loss. | Count | autovalue |
| dsfm:active\_gate.communication.messages.rejected | Active Gate - Communication - Messages - Rejected  Number of messages rejected due to authorization issues. Non-zero value indicates data loss. | Count | autovalue |
| dsfm:active\_gate.communication.messages.resent | Active Gate - Communication - Messages - Resent  Number of messages resent by ActiveGate. Indicates communication issue that may eventually result in `dsfm:active_gate.communication.messages.dropped` | Count | autovalue |
| dsfm:active\_gate.communication.queue.outgoing.usage | Active Gate - Communication - Queue - Outgoing - Usage  Number of messages queued. Growing value indicates messages are being received at a faster pace than sent out. Network performance is often a common root cause of this issue. | Count | autoavgcountmaxminsum |
| dsfm:active\_gate.communication.dropped\_messages | Active Gate - Communication - Dropped Messages  Deprecated. To be removed. Use: `dsfm:active_gate.communication.messages.dropped`. | Count | autovalue |
| dsfm:active\_gate.communication.incoming\_traffic | Active Gate - Communication - Incoming Traffic  Deprecated. To be removed. Use: `dsfm:active_gate.traffic.server.received` and `dsfm:active_gate.traffic.client.received` respectively. | Kibibyte | autovalue |
| dsfm:active\_gate.communication.outgoing\_traffic | Active Gate - Communication - Outgoing Traffic  Deprecated. To be removed. Use: `dsfm:active_gate.traffic.server.sent` and `dsfm:active_gate.traffic.client.sent` respectively. | Kibibyte | autovalue |
| dsfm:active\_gate.communication.resent\_messages | Active Gate - Communication - Resent Messages  Deprecated. To be removed. Use: `dsfm:active_gate.communication.messages.resent`. | Count | autovalue |
| dsfm:active\_gate.communication.traffic\_in | Active Gate - Communication - Traffic In  Deprecated. To be removed. Use: `dsfm:active_gate.traffic.server.received` and `dsfm:active_gate.traffic.client.received` respectively. | Kibibyte | autovalue |
| dsfm:active\_gate.communication.traffic\_out | Active Gate - Communication - Traffic Out  Deprecated. To be removed. Use: `dsfm:active_gate.traffic.server.sent` and `dsfm:active_gate.traffic.client.sent` respectively. | Kibibyte | autovalue |

### Event ingest

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| dsfm:active\_gate.event\_ingest.drop\_count | Active Gate - Event Ingest - Drop Count  Number of dropped messages | Count | autovalue |
| dsfm:active\_gate.event\_ingest.event\_attribute\_semantic\_count | Active Gate - Event Ingest - Event Attribute Semantic Count  Semantic Attribute Count per Event | Count | autoavgcountmaxminsum |
| dsfm:active\_gate.event\_ingest.event\_attribute\_unknown\_count | Active Gate - Event Ingest - Event Attribute Unknown Count  Unknown Attribute Count per Event | Count | autoavgcountmaxminsum |
| dsfm:active\_gate.event\_ingest.event\_incoming\_count | Active Gate - Event Ingest - Event Incoming Count  Incoming Log Event Count | Count | autovalue |
| dsfm:active\_gate.event\_ingest.event\_json\_size | Active Gate - Event Ingest - Event Json Size  JSON Event Size Bytes | Byte | autoavgcountmaxminsum |
| dsfm:active\_gate.event\_ingest.event\_otlp\_size | Active Gate - Event Ingest - Event Otlp Size  OTLP Event Size Bytes | Byte | autoavgcountmaxminsum |
| dsfm:active\_gate.event\_ingest.event\_plain\_size | Active Gate - Event Ingest - Event Plain Size  Plain Event Size Bytes | Byte | autoavgcountmaxminsum |

### Filecache

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| dsfm:active\_gate.filecache.data\_added\_count | Active Gate - Filecache - Data Added Count  Size of files added to cache (in kiB) | Kibibyte | autovalue |
| dsfm:active\_gate.filecache.data\_removed\_count | Active Gate - Filecache - Data Removed Count  Size of files removed from cache (in kiB) | Kibibyte | autovalue |
| dsfm:active\_gate.filecache.data\_requested\_count | Active Gate - Filecache - Data Requested Count  Counts the amount of data requested from cache (in kiB) | Kibibyte | autovalue |
| dsfm:active\_gate.filecache.data\_served\_count | Active Gate - Filecache - Data Served Count  Counts the amount of data served out of the cache (in kiB) | Kibibyte | autovalue |
| dsfm:active\_gate.filecache.size\_limit | Active Gate - Filecache - Size Limit  Configured limit of cache (in kiB) | Kibibyte | autoavgcountmaxminsum |

### JVM

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| dsfm:active\_gate.jvm.gc.major\_collection\_time | Active Gate - Jvm - Gc - Major Collection Time  ActiveGate java process major garbage collection time. | Millisecond | autovalue |
| dsfm:active\_gate.jvm.cpu\_usage | Active Gate - Jvm - Cpu Usage  ActiveGate java process CPU usage. | Percent (%) | autoavgcountmaxminsum |
| dsfm:active\_gate.jvm.heap\_memory\_available | Active Gate - Jvm - Heap Memory Available  ActiveGate java process heap memory size. | Byte | autoavgcountmaxminsum |
| dsfm:active\_gate.jvm.heap\_memory\_used | Active Gate - Jvm - Heap Memory Used  ActiveGate java process heap memory used. Compare with heap memory size reported by `dsfm:active_gate.jvm.heap_memory_available` metric. | Byte | autoavgcountmaxminsum |

### Kubernetes

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| dsfm:active\_gate.kubernetes.api.connections.pool.available | Active Gate - Kubernetes - Api - Connections - Pool - Available  Number of idle persistent connections | Count | autoavgcountmaxminsum |
| dsfm:active\_gate.kubernetes.api.query\_count | Active Gate - Kubernetes - Api - Query Count  Number of api queries sent to monitored Kubernetes clusters | Count | autovalue |
| dsfm:active\_gate.kubernetes.api.query\_duration | Active Gate - Kubernetes - Api - Query Duration  Duration of api queries sent to monitored Kubernetes clusters | Millisecond | autoavgcountmaxminsum |
| dsfm:active\_gate.kubernetes.cache.eviction\_count | Active Gate - Kubernetes - Cache - Eviction Count  Number of cache evictions | Count | autovalue |
| dsfm:active\_gate.kubernetes.cache.size\_available | Active Gate - Kubernetes - Cache - Size Available  Number of available elements until the cache limit is reached | Count | autoavgcountmaxminsum |
| dsfm:active\_gate.kubernetes.events.observed | Active Gate - Kubernetes - Events - Observed  ActiveGate observed Kubernetes Events | Count | autoavgcountmaxminsum |
| dsfm:active\_gate.kubernetes.events.processed | Active Gate - Kubernetes - Events - Processed  ActiveGate Processed Kubernetes Events | Count | autoavgcountmaxminsum |
| dsfm:active\_gate.kubernetes.spm.configuration\_dataset.dropped | Active Gate - Kubernetes - Spm - Configuration Dataset - Dropped  The number of Security Posture Management (SPM) configuration datasets dropped due to environment size limits | Count | autovalue |
| dsfm:active\_gate.kubernetes.pipeline\_duration | Active Gate - Kubernetes - Pipeline Duration  The execution time and completion state of a particular Kubernetes Platform Monitoring pipeline in the ActiveGate. | Millisecond | autoavgcountmaxminsum |

### Metrics

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| dsfm:active\_gate.metrics.ingest.grail.datapoints.accepted | Active Gate - Metrics - Ingest - Grail - Datapoints - Accepted  Number of accepted datapoints | Count | autoavgcountmaxminsum |
| dsfm:active\_gate.metrics.ingest.grail.datapoints.rejected | Active Gate - Metrics - Ingest - Grail - Datapoints - Rejected  Number of rejected datapoints, split by reason of rejection | Count | autoavgcountmaxminsum |
| dsfm:active\_gate.metrics.ingest.otlp.datapoints.accepted | Active Gate - Metrics - Ingest - Otlp - Datapoints - Accepted  Number of accepted datapoints | Count | autoavgcountmaxminsum |
| dsfm:active\_gate.metrics.ingest.otlp.datapoints.accepted.count | Active Gate - Metrics - Ingest - Otlp - Datapoints - Accepted - Count  Number of accepted datapoints | Count | autovalue |
| dsfm:active\_gate.metrics.ingest.otlp.datapoints.received.total | Active Gate - Metrics - Ingest - Otlp - Datapoints - Received - Total  Total number of datapoints that arrived at the API. | Count | autoavgcountmaxminsum |
| dsfm:active\_gate.metrics.ingest.otlp.datapoints.rejected | Active Gate - Metrics - Ingest - Otlp - Datapoints - Rejected  Number of rejected datapoints, split by reason of rejection | Count | autoavgcountmaxminsum |
| dsfm:active\_gate.metrics.ingest.otlp.datapoints.rejected.count | Active Gate - Metrics - Ingest - Otlp - Datapoints - Rejected - Count  Number of rejected datapoints, split by reason of rejection | Count | autovalue |

### Rest

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| dsfm:active\_gate.rest.request\_count | Active Gate - Rest - Request Count  ActiveGate number of incoming REST API calls | Count | autovalue |
| dsfm:active\_gate.rest.request\_size | Active Gate - Rest - Request Size  ActiveGate REST API request size | Byte | autoavgcountmaxminsum |
| dsfm:active\_gate.rest.response\_size | Active Gate - Rest - Response Size  ActiveGate REST API response size | Byte | autoavgcountmaxminsum |
| dsfm:active\_gate.rest.response\_time | Active Gate - Rest - Response Time  ActiveGate REST API response time | Millisecond | autoavgcountmaxminsum |

### Rum

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| dsfm:active\_gate.rum.beacon\_forwarded\_count | Active Gate - Rum - Beacon Forwarded Count  Counts the number of beacons forwarded to the server by the Active gate | Count | autovalue |

### Storage

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| dsfm:active\_gate.storage.directory.limit | Active Gate - Storage - Directory - Limit  Maximum allowed directory size. | MebiByte | autoavgcountmaxminsum |
| dsfm:active\_gate.storage.directory.size | Active Gate - Storage - Directory - Size  Directory size. Compare to limit reported by `dsfm:active_gate.storage.directory.limit`. | MebiByte | autoavgcountmaxminsum |
| dsfm:active\_gate.storage.volume.free | Active Gate - Storage - Volume - Free  Storage volume free space left. | MebiByte | autoavgcountmaxminsum |
| dsfm:active\_gate.storage.volume.total | Active Gate - Storage - Volume - Total  Storage volume size. | MebiByte | autoavgcountmaxminsum |

### System

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| dsfm:active\_gate.system.cpu\_usage | Active Gate - System - Cpu Usage  Operating system CPU usage. | Percent (%) | autoavgcountmaxminsum |
| dsfm:active\_gate.system.free\_memory | Active Gate - System - Free Memory  Operating system free memory. Compare with total memory reported by `dsfm:active_gate.system.total_memory` metric. | MebiByte | autoavgcountmaxminsum |
| dsfm:active\_gate.system.total\_memory | Active Gate - System - Total Memory  Operating system total memory. | MebiByte | autoavgcountmaxminsum |

### Thread pool

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| dsfm:active\_gate.thread\_pool.busy\_threads | Active Gate - Thread Pool - Busy Threads  Number of thread pool busy threads. | Count | autoavgcountmaxminsum |
| dsfm:active\_gate.thread\_pool.queue\_size | Active Gate - Thread Pool - Queue Size  Thread pool queue size. | Count | autoavgcountmaxminsum |

### Traffic

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| dsfm:active\_gate.traffic.client.received | Active Gate - Traffic - Client - Received  Ingress traffic from Dynatrace environment | Byte | autovalue |
| dsfm:active\_gate.traffic.client.sent | Active Gate - Traffic - Client - Sent  Egress traffic to Dynatrace environment | Byte | autovalue |
| dsfm:active\_gate.traffic.server.received | Active Gate - Traffic - Server - Received  Ingress traffic from clients | Byte | autovalue |
| dsfm:active\_gate.traffic.server.sent | Active Gate - Traffic - Server - Sent  Egress traffic to clients | Byte | autovalue |