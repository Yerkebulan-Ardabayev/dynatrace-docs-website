---
title: Метрики самомониторинга ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/activegate-sfm-metrics
scraped: 2026-05-12T12:13:50.279924
---

# Метрики самомониторинга ActiveGate

# Метрики самомониторинга ActiveGate

* 1-min read
* Published Dec 03, 2021

Dynatrace предлагает специальную категорию метрик самомониторинга для обеспечения наблюдаемости за работой и работоспособностью компонентов и функций Dynatrace. Эти метрики доступны в каждом окружении Dynatrace Managed и SaaS и идентифицируются по префиксу метрики `dsfm:`.

Подробнее смотрите в разделе [Метрики самомониторинга](/managed/analyze-explore-automate/metrics-classic/self-monitoring-metrics "Изучите полный список метрик самомониторинга Dynatrace.").

Ниже приведён список метрик самомониторинга, позволяющих получить информацию о работе ActiveGate.

> _Reference-таблица ниже на английском._

## Active gate

### AWS

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| dsfm:active\_gate.aws.elements.bad | Active Gate - Aws - Elements - Bad  Count of elements that were successfully retrieved from AWS, but failed later on (e.g., due to parsing errors). | Count | autovalue |
| dsfm:active\_gate.aws.elements.reported | Active Gate - Aws - Elements - Reported  Count of elements that were successfully reported (sent) to the server by ActiveGate. | Count | autovalue |
| dsfm:active\_gate.aws.elements.total | Active Gate - Aws - Elements - Total  Count of all elements retrieved in the given timeframe. | Count | autovalue |
| dsfm:active\_gate.aws.data\_delay | Active Gate - Aws - Data Delay  Sum of data delay for all entity and metric combinations | Millisecond | autovalue |
| dsfm:active\_gate.aws.data\_lost | Active Gate - Aws - Data Lost  Flag indicating whether we failed to obtain some of the data. 0 - all data obtained, 1 - some data lost. | Count | autovalue |
| dsfm:active\_gate.aws.monitored\_entities | Active Gate - Aws - Monitored Entities  Number of monitored entities per AWS Credentials | Count | autovalue |
| dsfm:active\_gate.aws.query\_time | Active Gate - Aws - Query Time  Summed time in milliseconds of all queries in the given timeframe. | Millisecond | autovalue |
| dsfm:active\_gate.aws.requests | Active Gate - Aws - Requests  Count of performed HTTP requests. | Count | autovalue |

### Communication

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| dsfm:active\_gate.communication.agent\_modules.connected | Active Gate - Communication - Agent Modules - Connected  Number of OneAgent modules connected. | Count | autoavgcountmaxminsum |
| dsfm:active\_gate.communication.messages.dropped | Active Gate - Communication - Messages - Dropped  Number of messages dropped due to timeouts. | Count | autovalue |
| dsfm:active\_gate.communication.messages.rejected | Active Gate - Communication - Messages - Rejected  Number of messages rejected due to authorization issues. | Count | autovalue |
| dsfm:active\_gate.communication.messages.resent | Active Gate - Communication - Messages - Resent  Number of messages resent by ActiveGate. | Count | autovalue |
| dsfm:active\_gate.communication.queue.outgoing.usage | Active Gate - Communication - Queue - Outgoing - Usage  Number of messages queued. | Count | autoavgcountmaxminsum |

### JVM

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| dsfm:active\_gate.jvm.gc.major\_collection\_time | Active Gate - Jvm - Gc - Major Collection Time  ActiveGate java process major garbage collection time. | Millisecond | autovalue |
| dsfm:active\_gate.jvm.cpu\_usage | Active Gate - Jvm - Cpu Usage  ActiveGate java process CPU usage. | Percent (%) | autoavgcountmaxminsum |
| dsfm:active\_gate.jvm.heap\_memory\_available | Active Gate - Jvm - Heap Memory Available  ActiveGate java process heap memory size. | Byte | autoavgcountmaxminsum |
| dsfm:active\_gate.jvm.heap\_memory\_used | Active Gate - Jvm - Heap Memory Used  ActiveGate java process heap memory used. | Byte | autoavgcountmaxminsum |

### Storage

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| dsfm:active\_gate.storage.directory.limit | Active Gate - Storage - Directory - Limit  Maximum allowed directory size. | MebiByte | autoavgcountmaxminsum |
| dsfm:active\_gate.storage.directory.size | Active Gate - Storage - Directory - Size  Directory size. | MebiByte | autoavgcountmaxminsum |
| dsfm:active\_gate.storage.volume.free | Active Gate - Storage - Volume - Free  Storage volume free space left. | MebiByte | autoavgcountmaxminsum |
| dsfm:active\_gate.storage.volume.total | Active Gate - Storage - Volume - Total  Storage volume size. | MebiByte | autoavgcountmaxminsum |

### System

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| dsfm:active\_gate.system.cpu\_usage | Active Gate - System - Cpu Usage  Operating system CPU usage. | Percent (%) | autoavgcountmaxminsum |
| dsfm:active\_gate.system.free\_memory | Active Gate - System - Free Memory  Operating system free memory. | MebiByte | autoavgcountmaxminsum |
| dsfm:active\_gate.system.total\_memory | Active Gate - System - Total Memory  Operating system total memory. | MebiByte | autoavgcountmaxminsum |

### Traffic

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| dsfm:active\_gate.traffic.client.received | Active Gate - Traffic - Client - Received  Ingress traffic from Dynatrace environment | Byte | autovalue |
| dsfm:active\_gate.traffic.client.sent | Active Gate - Traffic - Client - Sent  Egress traffic to Dynatrace environment | Byte | autovalue |
| dsfm:active\_gate.traffic.server.received | Active Gate - Traffic - Server - Received  Ingress traffic from clients | Byte | autovalue |
| dsfm:active\_gate.traffic.server.sent | Active Gate - Traffic - Server - Sent  Egress traffic to clients | Byte | autovalue |