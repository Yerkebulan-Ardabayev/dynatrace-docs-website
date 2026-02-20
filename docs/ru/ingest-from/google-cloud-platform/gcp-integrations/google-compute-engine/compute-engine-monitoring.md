---
title: Google Compute Engine with Operations suite metrics monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine/compute-engine-monitoring
scraped: 2026-02-20T21:24:25.290160
---

# Google Compute Engine with Operations suite metrics monitoring

# Google Compute Engine with Operations suite metrics monitoring

* Latest Dynatrace
* How-to guide
* 18-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Compute Engine.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| gce\_instance/default\_metrics | Dropped bytes | Byte | compute.googleapis.com/firewall/dropped\_bytes\_count |
| gce\_instance/default\_metrics | Dropped packets | Count | compute.googleapis.com/firewall/dropped\_packets\_count |
| gce\_instance/default\_metrics | Runnable task count. | Count | compute.googleapis.com/guest/cpu/runnable\_task\_count |
| gce\_instance/default\_metrics | CPU usage | Second | compute.googleapis.com/guest/cpu/usage\_time |
| gce\_instance/default\_metrics | Disk usage in Bytes | Byte | compute.googleapis.com/guest/disk/bytes\_used |
| gce\_instance/default\_metrics | IO Time | MilliSecond | compute.googleapis.com/guest/disk/io\_time |
| gce\_instance/default\_metrics | Merged disk operations | Count | compute.googleapis.com/guest/disk/merged\_operation\_count |
| gce\_instance/default\_metrics | Disk bytes transferred | Byte | compute.googleapis.com/guest/disk/operation\_bytes\_count |
| gce\_instance/default\_metrics | Disk operations | Count | compute.googleapis.com/guest/disk/operation\_count |
| gce\_instance/default\_metrics | Disk operation time | MilliSecond | compute.googleapis.com/guest/disk/operation\_time |
| gce\_instance/default\_metrics | Queue Length | Count | compute.googleapis.com/guest/disk/queue\_length |
| gce\_instance/default\_metrics | IO Time | MilliSecond | compute.googleapis.com/guest/disk/weighted\_io\_time |
| gce\_instance/default\_metrics | Anonymous memory usage in Bytes | Byte | compute.googleapis.com/guest/memory/anonymous\_used |
| gce\_instance/default\_metrics | Memory usage in Bytes | Byte | compute.googleapis.com/guest/memory/bytes\_used |
| gce\_instance/default\_metrics | Dirty pages usage in Bytes. | Byte | compute.googleapis.com/guest/memory/dirty\_used |
| gce\_instance/default\_metrics | Page cache memory usage in Bytes | Byte | compute.googleapis.com/guest/memory/page\_cache\_used |
| gce\_instance/default\_metrics | Unevictable memory usage in Bytes | Byte | compute.googleapis.com/guest/memory/unevictable\_used |
| gce\_instance/default\_metrics | Problem Count | Count | compute.googleapis.com/guest/system/problem\_count |
| gce\_instance/default\_metrics | Problem State | Count | compute.googleapis.com/guest/system/problem\_state |
| gce\_instance/default\_metrics | Uptime | Second | compute.googleapis.com/guest/system/uptime |
| gce\_instance/default\_metrics | Reserved vCPUs | Count | compute.googleapis.com/instance/cpu/reserved\_cores |
| gce\_instance/default\_metrics | Scheduler Wait Time | Second | compute.googleapis.com/instance/cpu/scheduler\_wait\_time |
| gce\_instance/default\_metrics | CPU usage | Second | compute.googleapis.com/instance/cpu/usage\_time |
| gce\_instance/default\_metrics | CPU utilization | Percent | compute.googleapis.com/instance/cpu/utilization |
| gce\_instance/default\_metrics | Peak disk read bytes | Byte | compute.googleapis.com/instance/disk/max\_read\_bytes\_count |
| gce\_instance/default\_metrics | Peak disk read ops | Count | compute.googleapis.com/instance/disk/max\_read\_ops\_count |
| gce\_instance/default\_metrics | Peak disk write bytes | Byte | compute.googleapis.com/instance/disk/max\_write\_bytes\_count |
| gce\_instance/default\_metrics | Peak disk write ops | Count | compute.googleapis.com/instance/disk/max\_write\_ops\_count |
| gce\_instance/default\_metrics | Disk read bytes | Byte | compute.googleapis.com/instance/disk/read\_bytes\_count |
| gce\_instance/default\_metrics | Disk read operations | Count | compute.googleapis.com/instance/disk/read\_ops\_count |
| gce\_instance/default\_metrics | Throttled read bytes | Byte | compute.googleapis.com/instance/disk/throttled\_read\_bytes\_count |
| gce\_instance/default\_metrics | Throttled read operations | Count | compute.googleapis.com/instance/disk/throttled\_read\_ops\_count |
| gce\_instance/default\_metrics | Throttled write bytes | Byte | compute.googleapis.com/instance/disk/throttled\_write\_bytes\_count |
| gce\_instance/default\_metrics | Throttled write operations | Count | compute.googleapis.com/instance/disk/throttled\_write\_ops\_count |
| gce\_instance/default\_metrics | Disk write bytes | Byte | compute.googleapis.com/instance/disk/write\_bytes\_count |
| gce\_instance/default\_metrics | Disk write operations | Count | compute.googleapis.com/instance/disk/write\_ops\_count |
| gce\_instance/default\_metrics | Early Boot Validation | Count | compute.googleapis.com/instance/integrity/early\_boot\_validation\_status |
| gce\_instance/default\_metrics | Late Boot Validation | Count | compute.googleapis.com/instance/integrity/late\_boot\_validation\_status |
| gce\_instance/default\_metrics | VM Memory Total | Byte | compute.googleapis.com/instance/memory/balloon/ram\_size |
| gce\_instance/default\_metrics | VM Memory Used | Byte | compute.googleapis.com/instance/memory/balloon/ram\_used |
| gce\_instance/default\_metrics | VM Swap In | Byte | compute.googleapis.com/instance/memory/balloon/swap\_in\_bytes\_count |
| gce\_instance/default\_metrics | VM Swap Out | Byte | compute.googleapis.com/instance/memory/balloon/swap\_out\_bytes\_count |
| gce\_instance/default\_metrics | Received bytes | Byte | compute.googleapis.com/instance/network/received\_bytes\_count |
| gce\_instance/default\_metrics | Received packets | Count | compute.googleapis.com/instance/network/received\_packets\_count |
| gce\_instance/default\_metrics | Sent bytes | Byte | compute.googleapis.com/instance/network/sent\_bytes\_count |
| gce\_instance/default\_metrics | Sent packets | Count | compute.googleapis.com/instance/network/sent\_packets\_count |
| gce\_instance/default\_metrics | Uptime | Second | compute.googleapis.com/instance/uptime |
| gce\_instance/default\_metrics | Uptime Total | Second | compute.googleapis.com/instance/uptime\_total |
| gce\_instance/default\_metrics | Dropped packets | Count | compute.googleapis.com/mirroring/dropped\_packets\_count |
| gce\_instance/default\_metrics | Mirrored bytes | Byte | compute.googleapis.com/mirroring/mirrored\_bytes\_count |
| gce\_instance/default\_metrics | Mirrored packets | Count | compute.googleapis.com/mirroring/mirrored\_packets\_count |
| gce\_instance/default\_metrics | Allocated ports | Unspecified | compute.googleapis.com/nat/allocated\_ports |
| gce\_instance/default\_metrics | Closed connections count | Unspecified | compute.googleapis.com/nat/closed\_connections\_count |
| gce\_instance/default\_metrics | Received packets dropped count | Unspecified | compute.googleapis.com/nat/dropped\_received\_packets\_count |
| gce\_instance/default\_metrics | Sent packets dropped count | Unspecified | compute.googleapis.com/nat/dropped\_sent\_packets\_count |
| gce\_instance/default\_metrics | New connections count | Unspecified | compute.googleapis.com/nat/new\_connections\_count |
| gce\_instance/default\_metrics | Open connections | Unspecified | compute.googleapis.com/nat/open\_connections |
| gce\_instance/default\_metrics | Port usage | Unspecified | compute.googleapis.com/nat/port\_usage |
| gce\_instance/default\_metrics | Received bytes count | Byte | compute.googleapis.com/nat/received\_bytes\_count |
| gce\_instance/default\_metrics | Received packets count | Unspecified | compute.googleapis.com/nat/received\_packets\_count |
| gce\_instance/default\_metrics | Sent bytes count | Byte | compute.googleapis.com/nat/sent\_bytes\_count |
| gce\_instance/default\_metrics | Sent packets count | Unspecified | compute.googleapis.com/nat/sent\_packets\_count |
| gce\_instance/agent | Monitoring Agent API Request Count | Count | agent.googleapis.com/agent/api\_request\_count |
| gce\_instance/agent | Logging Agent Log Entry Count | Count | agent.googleapis.com/agent/log\_entry\_count |
| gce\_instance/agent | Logging Agent Retried Log Entry Writes Count | Count | agent.googleapis.com/agent/log\_entry\_retry\_count |
| gce\_instance/agent | Monitoring Agent Memory Usage | Byte | agent.googleapis.com/agent/memory\_usage |
| gce\_instance/agent | Monitoring Agent Metric Point Count | Count | agent.googleapis.com/agent/monitoring/point\_count |
| gce\_instance/agent | Logging Agent API Request Count | Count | agent.googleapis.com/agent/request\_count |
| gce\_instance/agent | Monitoring Agent Process Labels Size | Byte | agent.googleapis.com/agent/streamspace\_size |
| gce\_instance/agent | Monitoring Agent is Throttling Processes | Count | agent.googleapis.com/agent/streamspace\_size\_throttling |
| gce\_instance/agent | Monitoring/Logging Agent Uptime | Second | agent.googleapis.com/agent/uptime |
| gce\_instance/agent | Open connections | Count | agent.googleapis.com/apache/connections |
| gce\_instance/agent | Idle workers | Count | agent.googleapis.com/apache/idle\_workers |
| gce\_instance/agent | Requests | Count | agent.googleapis.com/apache/request\_count |
| gce\_instance/agent | Scoreboard | Count | agent.googleapis.com/apache/scoreboard |
| gce\_instance/agent | Traffic | Byte | agent.googleapis.com/apache/traffic |
| gce\_instance/agent | Hit count | Count | agent.googleapis.com/cassandra/cache/hits |
| gce\_instance/agent | Read latency | MicroSecond | agent.googleapis.com/cassandra/client\_request/latency/50p |
| gce\_instance/agent | Read latency | MicroSecond | agent.googleapis.com/cassandra/client\_request/latency/95p |
| gce\_instance/agent | Read latency | MicroSecond | agent.googleapis.com/cassandra/client\_request/latency/99p |
| gce\_instance/agent | Read latency | MicroSecond | agent.googleapis.com/cassandra/client\_request/latency/max |
| gce\_instance/agent | Compression ratio | Count | agent.googleapis.com/cassandra/column\_family/compression\_ratio |
| gce\_instance/agent | Max row size | Byte | agent.googleapis.com/cassandra/column\_family/max\_row\_size |
| gce\_instance/agent | Commit log size | Byte | agent.googleapis.com/cassandra/commitlog\_total\_size |
| gce\_instance/agent | Completed tasks | Count | agent.googleapis.com/cassandra/completed\_tasks |
| gce\_instance/agent | Tasks | Count | agent.googleapis.com/cassandra/current\_tasks |
| gce\_instance/agent | Dropped messages | Count | agent.googleapis.com/cassandra/dropped\_message/dropped\_count |
| gce\_instance/agent | Exceptions | Count | agent.googleapis.com/cassandra/storage\_service\_exception\_count |
| gce\_instance/agent | Storage load | Byte | agent.googleapis.com/cassandra/storage\_service\_load |
| gce\_instance/agent | Request latency | MilliSecond | agent.googleapis.com/couchdb/average\_request\_time |
| gce\_instance/agent | Bulk requests | Count | agent.googleapis.com/couchdb/httpd/bulk\_request\_count |
| gce\_instance/agent | Requests | Count | agent.googleapis.com/couchdb/httpd/request\_count |
| gce\_instance/agent | Request methods | Count | agent.googleapis.com/couchdb/httpd/request\_method\_count |
| gce\_instance/agent | Response codes | Count | agent.googleapis.com/couchdb/httpd/response\_code\_count |
| gce\_instance/agent | Temp view reads | Count | agent.googleapis.com/couchdb/httpd/temporary\_view\_read\_count |
| gce\_instance/agent | View reads | Count | agent.googleapis.com/couchdb/httpd/view\_read\_count |
| gce\_instance/agent | Open databases | Count | agent.googleapis.com/couchdb/open\_databases |
| gce\_instance/agent | Open files | Count | agent.googleapis.com/couchdb/open\_files |
| gce\_instance/agent | Reads | Count | agent.googleapis.com/couchdb/read\_count |
| gce\_instance/agent | Writes | Count | agent.googleapis.com/couchdb/write\_count |
| gce\_instance/agent | CPU load (15m) | Count | agent.googleapis.com/cpu/load\_15m |
| gce\_instance/agent | CPU load (1m) | Count | agent.googleapis.com/cpu/load\_1m |
| gce\_instance/agent | CPU load (5m) | Count | agent.googleapis.com/cpu/load\_5m |
| gce\_instance/agent | CPU usage | Second | agent.googleapis.com/cpu/usage\_time |
| gce\_instance/agent | CPU utilization | Percent | agent.googleapis.com/cpu/utilization |
| gce\_instance/agent | Disk usage | Byte | agent.googleapis.com/disk/bytes\_used |
| gce\_instance/agent | Disk I/O time | MilliSecond | agent.googleapis.com/disk/io\_time |
| gce\_instance/agent | Disk merged operations | Count | agent.googleapis.com/disk/merged\_operations |
| gce\_instance/agent | Disk operations | Count | agent.googleapis.com/disk/operation\_count |
| gce\_instance/agent | Disk operation time | MilliSecond | agent.googleapis.com/disk/operation\_time |
| gce\_instance/agent | Disk pending operations | Count | agent.googleapis.com/disk/pending\_operations |
| gce\_instance/agent | Disk utilization | Percent | agent.googleapis.com/disk/percent\_used |
| gce\_instance/agent | Disk bytes read | Byte | agent.googleapis.com/disk/read\_bytes\_count |
| gce\_instance/agent | Disk weighted I/O time | MilliSecond | agent.googleapis.com/disk/weighted\_io\_time |
| gce\_instance/agent | Disk bytes written | Byte | agent.googleapis.com/disk/write\_bytes\_count |
| gce\_instance/agent | Cache size | Byte | agent.googleapis.com/elasticsearch/cache\_memory\_usage |
| gce\_instance/agent | Field evictions | Count | agent.googleapis.com/elasticsearch/field\_eviction\_count |
| gce\_instance/agent | Filter evictions | Count | agent.googleapis.com/elasticsearch/filter\_cache\_eviction\_count |
| gce\_instance/agent | GC count | Count | agent.googleapis.com/elasticsearch/gc\_collection\_count |
| gce\_instance/agent | Memory usage | Byte | agent.googleapis.com/elasticsearch/memory\_usage |
| gce\_instance/agent | Network traffic | Byte | agent.googleapis.com/elasticsearch/network |
| gce\_instance/agent | Documents | Count | agent.googleapis.com/elasticsearch/num\_current\_documents |
| gce\_instance/agent | Data nodes | Count | agent.googleapis.com/elasticsearch/num\_data\_nodes |
| gce\_instance/agent | Open connections | Count | agent.googleapis.com/elasticsearch/num\_http\_connections |
| gce\_instance/agent | Nodes | Count | agent.googleapis.com/elasticsearch/num\_nodes |
| gce\_instance/agent | Open files | Count | agent.googleapis.com/elasticsearch/num\_open\_files |
| gce\_instance/agent | Open connections | Count | agent.googleapis.com/elasticsearch/num\_server\_connections |
| gce\_instance/agent | Shards | Count | agent.googleapis.com/elasticsearch/num\_shards |
| gce\_instance/agent | Completed operations | Count | agent.googleapis.com/elasticsearch/operation\_count |
| gce\_instance/agent | Operation time | MilliSecond | agent.googleapis.com/elasticsearch/operation\_time |
| gce\_instance/agent | Max threads | Count | agent.googleapis.com/elasticsearch/peak\_threads |
| gce\_instance/agent | Storage size | Byte | agent.googleapis.com/elasticsearch/storage\_size |
| gce\_instance/agent | Threads | Count | agent.googleapis.com/elasticsearch/threads |
| gce\_instance/agent | IPC connections | Count | agent.googleapis.com/hbase/ipc/connections |
| gce\_instance/agent | IPC queue size | Count | agent.googleapis.com/hbase/ipc/queue\_length |
| gce\_instance/agent | IPC traffic | Byte | agent.googleapis.com/hbase/ipc/traffic\_count |
| gce\_instance/agent | Load | Count | agent.googleapis.com/hbase/master/average\_load |
| gce\_instance/agent | Dead region servers | Count | agent.googleapis.com/hbase/master/dead\_region\_servers |
| gce\_instance/agent | Live region servers | Count | agent.googleapis.com/hbase/master/live\_region\_servers |
| gce\_instance/agent | Block cache accesses | Count | agent.googleapis.com/hbase/regionserver/block\_cache/access\_count |
| gce\_instance/agent | Evicted block count | Count | agent.googleapis.com/hbase/regionserver/block\_cache/evicted\_blocks\_count |
| gce\_instance/agent | Block cache hit ratio | Percent | agent.googleapis.com/hbase/regionserver/block\_cache/hit\_ratio\_percent |
| gce\_instance/agent | Block cache size | Byte | agent.googleapis.com/hbase/regionserver/block\_cache/memory |
| gce\_instance/agent | Block count | Count | agent.googleapis.com/hbase/regionserver/block\_cache/num\_items |
| gce\_instance/agent | Call queue size | Count | agent.googleapis.com/hbase/regionserver/call\_queue/length |
| gce\_instance/agent | Compaction queue size | Count | agent.googleapis.com/hbase/regionserver/compaction\_queue/length |
| gce\_instance/agent | Flush queue size | Count | agent.googleapis.com/hbase/regionserver/flush\_queue/length |
| gce\_instance/agent | Heap usage | Byte | agent.googleapis.com/hbase/regionserver/memory/heap\_usage |
| gce\_instance/agent | Memstore files | Count | agent.googleapis.com/hbase/regionserver/memstore/files |
| gce\_instance/agent | Memstore index size | Byte | agent.googleapis.com/hbase/regionserver/memstore/index\_size |
| gce\_instance/agent | Memstore open stores | Count | agent.googleapis.com/hbase/regionserver/memstore/open\_stores |
| gce\_instance/agent | Memstore size | Byte | agent.googleapis.com/hbase/regionserver/memstore/size |
| gce\_instance/agent | Online regions | Count | agent.googleapis.com/hbase/regionserver/online\_regions |
| gce\_instance/agent | Request count | Count | agent.googleapis.com/hbase/regionserver/request\_count |
| gce\_instance/agent | RPC request rate | PerSecond | agent.googleapis.com/hbase/regionserver/requests/total\_rate |
| gce\_instance/agent | Slow operations | Count | agent.googleapis.com/hbase/regionserver/slow\_operation\_count |
| gce\_instance/agent | Thrift average batch latency | NanoSecond | agent.googleapis.com/hbase/thrift/batch\_latency/average |
| gce\_instance/agent | Thrift average call latency | NanoSecond | agent.googleapis.com/hbase/thrift/call\_latency/average |
| gce\_instance/agent | Thrift call queue size | Count | agent.googleapis.com/hbase/thrift/call\_queue/length |
| gce\_instance/agent | Thrift average slow call latency | NanoSecond | agent.googleapis.com/hbase/thrift/slow\_call\_latency/average |
| gce\_instance/agent | Thrift average time in queue | NanoSecond | agent.googleapis.com/hbase/thrift/time\_in\_queue/average |
| gce\_instance/agent | IIS open connections | Count | agent.googleapis.com/iis/current\_connections |
| gce\_instance/agent | IIS transferred bytes | Byte | agent.googleapis.com/iis/network/transferred\_bytes\_count |
| gce\_instance/agent | IIS connections | Count | agent.googleapis.com/iis/new\_connection\_count |
| gce\_instance/agent | IIS requests | Count | agent.googleapis.com/iis/request\_count |
| gce\_instance/agent | Network errors | Count | agent.googleapis.com/interface/errors |
| gce\_instance/agent | Network packets | Count | agent.googleapis.com/interface/packets |
| gce\_instance/agent | Network traffic | Byte | agent.googleapis.com/interface/traffic |
| gce\_instance/agent | GC count | Count | agent.googleapis.com/jvm/gc/count |
| gce\_instance/agent | GC time | MilliSecond | agent.googleapis.com/jvm/gc/time |
| gce\_instance/agent | Memory usage | Byte | agent.googleapis.com/jvm/memory/usage |
| gce\_instance/agent | CPU time | NanoSecond | agent.googleapis.com/jvm/os/cpu\_time |
| gce\_instance/agent | Open files | Count | agent.googleapis.com/jvm/os/open\_files |
| gce\_instance/agent | Daemon threads | Count | agent.googleapis.com/jvm/thread/num\_daemon |
| gce\_instance/agent | Threads | Count | agent.googleapis.com/jvm/thread/num\_live |
| gce\_instance/agent | Max threads | Count | agent.googleapis.com/jvm/thread/peak |
| gce\_instance/agent | Uptime | MilliSecond | agent.googleapis.com/jvm/uptime |
| gce\_instance/agent | Failed requests | Count | agent.googleapis.com/kafka/broker/topics/failed\_request\_count |
| gce\_instance/agent | Incoming messages | Count | agent.googleapis.com/kafka/broker/topics/incoming\_message\_count |
| gce\_instance/agent | Traffic | Byte | agent.googleapis.com/kafka/broker/topics/traffic |
| gce\_instance/agent | Active controllers | Count | agent.googleapis.com/kafka/controller/kafka/active |
| gce\_instance/agent | Offline partitions | Count | agent.googleapis.com/kafka/controller/kafka/offline\_partitions |
| gce\_instance/agent | Leader elections | Count | agent.googleapis.com/kafka/controller/leader\_elections/election\_count |
| gce\_instance/agent | Stale leader elections | Count | agent.googleapis.com/kafka/controller/leader\_elections/unclean\_count |
| gce\_instance/agent | Flushes | Count | agent.googleapis.com/kafka/log/flush\_count |
| gce\_instance/agent | Requests | Count | agent.googleapis.com/kafka/network/request\_count |
| gce\_instance/agent | Delayed purgatory requests | Count | agent.googleapis.com/kafka/purgatory/num\_delayed\_requests |
| gce\_instance/agent | Purgatory requests | Count | agent.googleapis.com/kafka/purgatory/size |
| gce\_instance/agent | Maximum lag | Count | agent.googleapis.com/kafka/replica\_fetcher/max\_lag |
| gce\_instance/agent | Minimum fetch rate | PerSecond | agent.googleapis.com/kafka/replica\_fetcher/min\_fetch\_rate |
| gce\_instance/agent | Gaining replicas | Count | agent.googleapis.com/kafka/replica\_manager/isr/expand\_count |
| gce\_instance/agent | Lagging replicas | Count | agent.googleapis.com/kafka/replica\_manager/isr/shrink\_count |
| gce\_instance/agent | Leaders | Count | agent.googleapis.com/kafka/replica\_manager/leaders |
| gce\_instance/agent | Partitions | Count | agent.googleapis.com/kafka/replica\_manager/partitions |
| gce\_instance/agent | Unreliable partitions | Count | agent.googleapis.com/kafka/replica\_manager/under\_replicated\_partitions |
| gce\_instance/agent | Commands | Count | agent.googleapis.com/memcached/command\_count |
| gce\_instance/agent | Connections | Count | agent.googleapis.com/memcached/current\_connections |
| gce\_instance/agent | Items | Count | agent.googleapis.com/memcached/current\_items |
| gce\_instance/agent | Evictions | Count | agent.googleapis.com/memcached/eviction\_count |
| gce\_instance/agent | Memory usage | Byte | agent.googleapis.com/memcached/memory |
| gce\_instance/agent | Traffic | Byte | agent.googleapis.com/memcached/network |
| gce\_instance/agent | Operations | Count | agent.googleapis.com/memcached/operation\_count |
| gce\_instance/agent | Hit ratio | Percent | agent.googleapis.com/memcached/operation\_hitratio |
| gce\_instance/agent | CPU time | Second | agent.googleapis.com/memcached/rusage |
| gce\_instance/agent | Threads | Count | agent.googleapis.com/memcached/threads |
| gce\_instance/agent | Memory usage | Byte | agent.googleapis.com/memory/bytes\_used |
| gce\_instance/agent | Memory utilization | Percent | agent.googleapis.com/memory/percent\_used |
| gce\_instance/agent | Cache hits | Count | agent.googleapis.com/mongodb/cache/hits |
| gce\_instance/agent | Cache misses | Count | agent.googleapis.com/mongodb/cache/misses |
| gce\_instance/agent | Collections | Count | agent.googleapis.com/mongodb/collections |
| gce\_instance/agent | Connections | Count | agent.googleapis.com/mongodb/connections |
| gce\_instance/agent | Data size | Byte | agent.googleapis.com/mongodb/data\_size |
| gce\_instance/agent | Extents | Count | agent.googleapis.com/mongodb/extents |
| gce\_instance/agent | Global lock time | MilliSecond | agent.googleapis.com/mongodb/global\_lock\_hold\_time |
| gce\_instance/agent | Index size | Byte | agent.googleapis.com/mongodb/index\_size |
| gce\_instance/agent | Indexes | Count | agent.googleapis.com/mongodb/indexes |
| gce\_instance/agent | Memory usage | MebiByte | agent.googleapis.com/mongodb/memory\_usage |
| gce\_instance/agent | Objects | Count | agent.googleapis.com/mongodb/objects |
| gce\_instance/agent | Operations | Count | agent.googleapis.com/mongodb/operation\_count |
| gce\_instance/agent | Storage size | Byte | agent.googleapis.com/mongodb/storage\_size |
| gce\_instance/agent | SQL Server open connections | Count | agent.googleapis.com/mssql/connections/user |
| gce\_instance/agent | SQL Server transaction rate | PerSecond | agent.googleapis.com/mssql/transaction\_rate |
| gce\_instance/agent | SQL Server write transaction rate | PerSecond | agent.googleapis.com/mssql/write\_transaction\_rate |
| gce\_instance/agent | Buffer pool pages | Count | agent.googleapis.com/mysql/buffer\_pool/num\_pages |
| gce\_instance/agent | Buffer pool operations | Count | agent.googleapis.com/mysql/buffer\_pool/operation\_count |
| gce\_instance/agent | Buffer pool size | Byte | agent.googleapis.com/mysql/buffer\_pool\_size |
| gce\_instance/agent | Commands | Count | agent.googleapis.com/mysql/command\_count |
| gce\_instance/agent | Handlers | Count | agent.googleapis.com/mysql/handler\_count |
| gce\_instance/agent | InnoDB doublewrite buffers | Count | agent.googleapis.com/mysql/innodb/doublewrite\_count |
| gce\_instance/agent | InnoDB log operations | Count | agent.googleapis.com/mysql/innodb/log\_operation\_count |
| gce\_instance/agent | InnoDB operations | Count | agent.googleapis.com/mysql/innodb/operation\_count |
| gce\_instance/agent | InnoDB page operations | Count | agent.googleapis.com/mysql/innodb/page\_operation\_count |
| gce\_instance/agent | InnoDB locks | Count | agent.googleapis.com/mysql/innodb/row\_lock\_count |
| gce\_instance/agent | InnoDB row operations | Count | agent.googleapis.com/mysql/innodb/row\_operation\_count |
| gce\_instance/agent | Locks | Count | agent.googleapis.com/mysql/lock\_count |
| gce\_instance/agent | QCache operations | Count | agent.googleapis.com/mysql/qcache/operation\_count |
| gce\_instance/agent | QCache queries | Count | agent.googleapis.com/mysql/qcache/query\_count |
| gce\_instance/agent | Replica lag | Second | agent.googleapis.com/mysql/slave\_replication\_lag |
| gce\_instance/agent | Sorts | Count | agent.googleapis.com/mysql/sort\_count |
| gce\_instance/agent | Threads | Count | agent.googleapis.com/mysql/thread\_count |
| gce\_instance/agent | TCP connections | Count | agent.googleapis.com/network/tcp\_connections |
| gce\_instance/agent | Accepted connections | Count | agent.googleapis.com/nginx/connections/accepted\_count |
| gce\_instance/agent | Active connections | Count | agent.googleapis.com/nginx/connections/current |
| gce\_instance/agent | Handled connections | Count | agent.googleapis.com/nginx/connections/handled\_count |
| gce\_instance/agent | Requests | Count | agent.googleapis.com/nginx/request\_count |
| gce\_instance/agent | Pagefile utilization | Percent | agent.googleapis.com/pagefile/percent\_used |
| gce\_instance/agent | Blocks read | Count | agent.googleapis.com/postgresql/blocks\_read\_count |
| gce\_instance/agent | Commits | Count | agent.googleapis.com/postgresql/commit\_count |
| gce\_instance/agent | DB size | Byte | agent.googleapis.com/postgresql/db\_size |
| gce\_instance/agent | Backends | Count | agent.googleapis.com/postgresql/num\_backends |
| gce\_instance/agent | DB rows | Count | agent.googleapis.com/postgresql/num\_tuples |
| gce\_instance/agent | Operations | Count | agent.googleapis.com/postgresql/operation\_count |
| gce\_instance/agent | Rollbacks | Count | agent.googleapis.com/postgresql/rollback\_count |
| gce\_instance/agent | Processes | Count | agent.googleapis.com/processes/count\_by\_state |
| gce\_instance/agent | Process CPU | Second | agent.googleapis.com/processes/cpu\_time |
| gce\_instance/agent | Process disk read I/O | Byte | agent.googleapis.com/processes/disk/read\_bytes\_count |
| gce\_instance/agent | Process disk write I/O | Byte | agent.googleapis.com/processes/disk/write\_bytes\_count |
| gce\_instance/agent | Fork count | Count | agent.googleapis.com/processes/fork\_count |
| gce\_instance/agent | Process resident memory | Byte | agent.googleapis.com/processes/rss\_usage |
| gce\_instance/agent | Process virtual memory | Byte | agent.googleapis.com/processes/vm\_usage |
| gce\_instance/agent | Consumers | Count | agent.googleapis.com/rabbitmq/consumers |
| gce\_instance/agent | Delivery rate | PerSecond | agent.googleapis.com/rabbitmq/delivery\_rate |
| gce\_instance/agent | Messages | Count | agent.googleapis.com/rabbitmq/num\_messages |
| gce\_instance/agent | Publish rate | PerSecond | agent.googleapis.com/rabbitmq/publish\_rate |
| gce\_instance/agent | Unsaved changes | Count | agent.googleapis.com/redis/changes\_since\_last\_save |
| gce\_instance/agent | Blocked clients | Count | agent.googleapis.com/redis/clients/blocked |
| gce\_instance/agent | Connected clients | Count | agent.googleapis.com/redis/clients/connected |
| gce\_instance/agent | Commands | Count | agent.googleapis.com/redis/commands\_processed |
| gce\_instance/agent | Slave connections | Count | agent.googleapis.com/redis/connections/slaves |
| gce\_instance/agent | Connections | Count | agent.googleapis.com/redis/connections/total |
| gce\_instance/agent | Expired keys | Count | agent.googleapis.com/redis/expired\_keys |
| gce\_instance/agent | Memory usage | Byte | agent.googleapis.com/redis/memory/usage |
| gce\_instance/agent | Lua memory usage | Byte | agent.googleapis.com/redis/memory/usage\_lua |
| gce\_instance/agent | PubSub channels | Count | agent.googleapis.com/redis/pubsub/channels |
| gce\_instance/agent | PubSub patterns | Count | agent.googleapis.com/redis/pubsub/patterns |
| gce\_instance/agent | Uptime | Second | agent.googleapis.com/redis/uptime |
| gce\_instance/agent | 95% latency (1m) | MicroSecond | agent.googleapis.com/riak/latency/95th\_percentile |
| gce\_instance/agent | Average latency (1m) | MicroSecond | agent.googleapis.com/riak/latency/average |
| gce\_instance/agent | Maximum latency (1m) | MicroSecond | agent.googleapis.com/riak/latency/maximum |
| gce\_instance/agent | Memory usage | Byte | agent.googleapis.com/riak/memory\_usage |
| gce\_instance/agent | 95% siblings (1m) | Count | agent.googleapis.com/riak/num\_siblings/95th\_percentile |
| gce\_instance/agent | Average siblings (1m) | Count | agent.googleapis.com/riak/num\_siblings/average |
| gce\_instance/agent | Maximum siblings (1m) | Count | agent.googleapis.com/riak/num\_siblings/maximum |
| gce\_instance/agent | 95% object size (1m) | Byte | agent.googleapis.com/riak/object\_size/95th\_percentile |
| gce\_instance/agent | Average object size (1m) | Byte | agent.googleapis.com/riak/object\_size/average |
| gce\_instance/agent | Maximum object size (1m) | Byte | agent.googleapis.com/riak/object\_size/maximum |
| gce\_instance/agent | Operations | Count | agent.googleapis.com/riak/operation\_count |
| gce\_instance/agent | Swap usage | Byte | agent.googleapis.com/swap/bytes\_used |
| gce\_instance/agent | Swap I/O operations | Count | agent.googleapis.com/swap/io |
| gce\_instance/agent | Swap utilization | Percent | agent.googleapis.com/swap/percent\_used |
| gce\_instance/agent | Sessions | Count | agent.googleapis.com/tomcat/manager/sessions |
| gce\_instance/agent | Errors | Count | agent.googleapis.com/tomcat/request\_processor/error\_count |
| gce\_instance/agent | Processing time | MilliSecond | agent.googleapis.com/tomcat/request\_processor/processing\_time |
| gce\_instance/agent | Requests | Count | agent.googleapis.com/tomcat/request\_processor/request\_count |
| gce\_instance/agent | Traffic | Byte | agent.googleapis.com/tomcat/request\_processor/traffic\_count |
| gce\_instance/agent | Busy threads | Count | agent.googleapis.com/tomcat/threads/busy |
| gce\_instance/agent | Current threads | Count | agent.googleapis.com/tomcat/threads/current |
| gce\_instance/agent | Backend connection successes | Count | agent.googleapis.com/varnish/backend\_connection\_count |
| gce\_instance/agent | Cache operations | Count | agent.googleapis.com/varnish/cache\_operation\_count |
| gce\_instance/agent | Client connections | Count | agent.googleapis.com/varnish/client\_connection\_count |
| gce\_instance/agent | Open connections | Count | agent.googleapis.com/zookeeper/connections\_count |
| gce\_instance/agent | Data size | Byte | agent.googleapis.com/zookeeper/data\_size |
| gce\_instance/agent | Followers | Count | agent.googleapis.com/zookeeper/followers/count |
| gce\_instance/agent | Synced followers | Count | agent.googleapis.com/zookeeper/followers/synced\_count |
| gce\_instance/agent | Packets received | Count | agent.googleapis.com/zookeeper/network/received\_packets\_count |
| gce\_instance/agent | Packets sent | Count | agent.googleapis.com/zookeeper/network/sent\_packets\_count |
| gce\_instance/agent | Nodes | Count | agent.googleapis.com/zookeeper/nodes/count |
| gce\_instance/agent | Ephemeral nodes | Count | agent.googleapis.com/zookeeper/nodes/ephemeral\_count |
| gce\_instance/agent | Watches | Count | agent.googleapis.com/zookeeper/nodes/watches\_count |
| gce\_instance/agent | Average request latency | MilliSecond | agent.googleapis.com/zookeeper/requests/latency/average |
| gce\_instance/agent | Maximum request latency | MilliSecond | agent.googleapis.com/zookeeper/requests/latency/maximum |
| gce\_instance/agent | Minimum request latency | MilliSecond | agent.googleapis.com/zookeeper/requests/latency/minimum |
| gce\_instance/agent | Outstanding requests | Count | agent.googleapis.com/zookeeper/requests/outstanding\_count |
| gce\_instance/agent | Pending syncs | Count | agent.googleapis.com/zookeeper/sync\_operations/pending\_count |
| gce\_instance/firewallinsights | VM Firewall Hit Counts | Count | firewallinsights.googleapis.com/vm/firewall\_hit\_count |
| gce\_instance/firewallinsights | VM Firewall Last Used Timestamp | Count | firewallinsights.googleapis.com/vm/firewall\_last\_used\_timestamp |
| gce\_instance/istio | Client Connection Close Count | Byte | istio.io/service/client/connection\_close\_count |
| gce\_instance/istio | Client Connection Open Count | Byte | istio.io/service/client/connection\_open\_count |
| gce\_instance/istio | Client Received Bytes Count | Byte | istio.io/service/client/received\_bytes\_count |
| gce\_instance/istio | Client Request Bytes | Byte | istio.io/service/client/request\_bytes |
| gce\_instance/istio | Client Request Count | Count | istio.io/service/client/request\_count |
| gce\_instance/istio | Client Response Bytes | Byte | istio.io/service/client/response\_bytes |
| gce\_instance/istio | Client Roundtrip Latencies | MilliSecond | istio.io/service/client/roundtrip\_latencies |
| gce\_instance/istio | Client Sent Bytes Count | Byte | istio.io/service/client/sent\_bytes\_count |
| gce\_instance/istio | Server Connection Close Count | Byte | istio.io/service/server/connection\_close\_count |
| gce\_instance/istio | Server Connection Open Count | Byte | istio.io/service/server/connection\_open\_count |
| gce\_instance/istio | Server Received Bytes Count | Byte | istio.io/service/server/received\_bytes\_count |
| gce\_instance/istio | Server Request Bytes | Byte | istio.io/service/server/request\_bytes |
| gce\_instance/istio | Server Request Count | Count | istio.io/service/server/request\_count |
| gce\_instance/istio | Server Response Bytes | Byte | istio.io/service/server/response\_bytes |
| gce\_instance/istio | Server Response Latencies | MilliSecond | istio.io/service/server/response\_latencies |
| gce\_instance/istio | Server Sent Bytes Count | Byte | istio.io/service/server/sent\_bytes\_count |
| gce\_instance\_vm\_flow/default\_metrics | Egress bytes | Byte | networking.googleapis.com/vm\_flow/egress\_bytes\_count |
| gce\_instance\_vm\_flow/default\_metrics | Ingress bytes | Byte | networking.googleapis.com/vm\_flow/ingress\_bytes\_count |
| gce\_instance\_vm\_flow/default\_metrics | RTT latencies | MilliSecond | networking.googleapis.com/vm\_flow/rtt |
| instance\_group/default\_metrics | Instance group size | Count | compute.googleapis.com/instance\_group/size |
| autoscaler/default\_metrics | Serving capacity | Count | autoscaler.googleapis.com/capacity |
| autoscaler/default\_metrics | Current Autoscaler utilization | Count | autoscaler.googleapis.com/current\_utilization |
| tpu\_worker/default\_metrics | Container CPU utilization | Percent | tpu.googleapis.com/container/cpu/utilization |
| tpu\_worker/default\_metrics | Container memory usage | Byte | tpu.googleapis.com/container/memory/usage |
| tpu\_worker/default\_metrics | CPU utilization | Percent | tpu.googleapis.com/cpu/utilization |
| tpu\_worker/default\_metrics | Memory usage | Byte | tpu.googleapis.com/memory/usage |
| tpu\_worker/default\_metrics | Network bytes received | Byte | tpu.googleapis.com/network/received\_bytes\_count |
| tpu\_worker/default\_metrics | Network bytes sent | Byte | tpu.googleapis.com/network/sent\_bytes\_count |
| tpu\_worker/default\_metrics | MXU utilization | Percent | tpu.googleapis.com/tpu/mxu/utilization |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")