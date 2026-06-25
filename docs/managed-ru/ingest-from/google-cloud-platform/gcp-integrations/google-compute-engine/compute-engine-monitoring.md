---
title: Мониторинг Google Compute Engine с метриками Operations suite
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine/compute-engine-monitoring
scraped: 2026-05-12T11:50:27.366091
---

# Мониторинг Google Compute Engine с метриками Operations suite

# Мониторинг Google Compute Engine с метриками Operations suite

* Практическое руководство
* Чтение: 18 мин
* Опубликовано 17 января 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные через Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все релевантные данные в дашбордах, она также обеспечивает оповещения и отслеживание событий.

## Предварительные условия

[Настройка интеграции](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически отслеживает ряд предустановленных сервисов и наборов функций (метрик) Google Cloud. Помимо них, в мониторинг можно добавить дополнительные сервисы или наборы функций. Подробнее см. [Добавление или удаление сервисов](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

Список наборов функций, доступных для этого сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции метрики отслеживаемых сервисов можно просматривать в [Браузере метрик](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Просматривайте метрики с помощью браузера метрик Dynatrace."), [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения нужных аналитических данных.") и на плитках ваших дашбордов.

## Таблица метрик

Для Google Compute Engine доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| gce\_instance/default\_metrics | Dropped bytes | Байт | compute.googleapis.com/firewall/dropped\_bytes\_count |
| gce\_instance/default\_metrics | Dropped packets | Количество | compute.googleapis.com/firewall/dropped\_packets\_count |
| gce\_instance/default\_metrics | Runnable task count. | Количество | compute.googleapis.com/guest/cpu/runnable\_task\_count |
| gce\_instance/default\_metrics | CPU usage | Секунда | compute.googleapis.com/guest/cpu/usage\_time |
| gce\_instance/default\_metrics | Disk usage in Bytes | Байт | compute.googleapis.com/guest/disk/bytes\_used |
| gce\_instance/default\_metrics | IO Time | Миллисекунда | compute.googleapis.com/guest/disk/io\_time |
| gce\_instance/default\_metrics | Merged disk operations | Количество | compute.googleapis.com/guest/disk/merged\_operation\_count |
| gce\_instance/default\_metrics | Disk bytes transferred | Байт | compute.googleapis.com/guest/disk/operation\_bytes\_count |
| gce\_instance/default\_metrics | Disk operations | Количество | compute.googleapis.com/guest/disk/operation\_count |
| gce\_instance/default\_metrics | Disk operation time | Миллисекунда | compute.googleapis.com/guest/disk/operation\_time |
| gce\_instance/default\_metrics | Queue Length | Количество | compute.googleapis.com/guest/disk/queue\_length |
| gce\_instance/default\_metrics | IO Time | Миллисекунда | compute.googleapis.com/guest/disk/weighted\_io\_time |
| gce\_instance/default\_metrics | Anonymous memory usage in Bytes | Байт | compute.googleapis.com/guest/memory/anonymous\_used |
| gce\_instance/default\_metrics | Memory usage in Bytes | Байт | compute.googleapis.com/guest/memory/bytes\_used |
| gce\_instance/default\_metrics | Dirty pages usage in Bytes. | Байт | compute.googleapis.com/guest/memory/dirty\_used |
| gce\_instance/default\_metrics | Page cache memory usage in Bytes | Байт | compute.googleapis.com/guest/memory/page\_cache\_used |
| gce\_instance/default\_metrics | Unevictable memory usage in Bytes | Байт | compute.googleapis.com/guest/memory/unevictable\_used |
| gce\_instance/default\_metrics | Problem Count | Количество | compute.googleapis.com/guest/system/problem\_count |
| gce\_instance/default\_metrics | Problem State | Количество | compute.googleapis.com/guest/system/problem\_state |
| gce\_instance/default\_metrics | Uptime | Секунда | compute.googleapis.com/guest/system/uptime |
| gce\_instance/default\_metrics | Reserved vCPUs | Количество | compute.googleapis.com/instance/cpu/reserved\_cores |
| gce\_instance/default\_metrics | Scheduler Wait Time | Секунда | compute.googleapis.com/instance/cpu/scheduler\_wait\_time |
| gce\_instance/default\_metrics | CPU usage | Секунда | compute.googleapis.com/instance/cpu/usage\_time |
| gce\_instance/default\_metrics | CPU utilization | Процент | compute.googleapis.com/instance/cpu/utilization |
| gce\_instance/default\_metrics | Peak disk read bytes | Байт | compute.googleapis.com/instance/disk/max\_read\_bytes\_count |
| gce\_instance/default\_metrics | Peak disk read ops | Количество | compute.googleapis.com/instance/disk/max\_read\_ops\_count |
| gce\_instance/default\_metrics | Peak disk write bytes | Байт | compute.googleapis.com/instance/disk/max\_write\_bytes\_count |
| gce\_instance/default\_metrics | Peak disk write ops | Количество | compute.googleapis.com/instance/disk/max\_write\_ops\_count |
| gce\_instance/default\_metrics | Disk read bytes | Байт | compute.googleapis.com/instance/disk/read\_bytes\_count |
| gce\_instance/default\_metrics | Disk read operations | Количество | compute.googleapis.com/instance/disk/read\_ops\_count |
| gce\_instance/default\_metrics | Throttled read bytes | Байт | compute.googleapis.com/instance/disk/throttled\_read\_bytes\_count |
| gce\_instance/default\_metrics | Throttled read operations | Количество | compute.googleapis.com/instance/disk/throttled\_read\_ops\_count |
| gce\_instance/default\_metrics | Throttled write bytes | Байт | compute.googleapis.com/instance/disk/throttled\_write\_bytes\_count |
| gce\_instance/default\_metrics | Throttled write operations | Количество | compute.googleapis.com/instance/disk/throttled\_write\_ops\_count |
| gce\_instance/default\_metrics | Disk write bytes | Байт | compute.googleapis.com/instance/disk/write\_bytes\_count |
| gce\_instance/default\_metrics | Disk write operations | Количество | compute.googleapis.com/instance/disk/write\_ops\_count |
| gce\_instance/default\_metrics | Early Boot Validation | Количество | compute.googleapis.com/instance/integrity/early\_boot\_validation\_status |
| gce\_instance/default\_metrics | Late Boot Validation | Количество | compute.googleapis.com/instance/integrity/late\_boot\_validation\_status |
| gce\_instance/default\_metrics | VM Memory Total | Байт | compute.googleapis.com/instance/memory/balloon/ram\_size |
| gce\_instance/default\_metrics | VM Memory Used | Байт | compute.googleapis.com/instance/memory/balloon/ram\_used |
| gce\_instance/default\_metrics | VM Swap In | Байт | compute.googleapis.com/instance/memory/balloon/swap\_in\_bytes\_count |
| gce\_instance/default\_metrics | VM Swap Out | Байт | compute.googleapis.com/instance/memory/balloon/swap\_out\_bytes\_count |
| gce\_instance/default\_metrics | Received bytes | Байт | compute.googleapis.com/instance/network/received\_bytes\_count |
| gce\_instance/default\_metrics | Received packets | Количество | compute.googleapis.com/instance/network/received\_packets\_count |
| gce\_instance/default\_metrics | Sent bytes | Байт | compute.googleapis.com/instance/network/sent\_bytes\_count |
| gce\_instance/default\_metrics | Sent packets | Количество | compute.googleapis.com/instance/network/sent\_packets\_count |
| gce\_instance/default\_metrics | Uptime | Секунда | compute.googleapis.com/instance/uptime |
| gce\_instance/default\_metrics | Uptime Total | Секунда | compute.googleapis.com/instance/uptime\_total |
| gce\_instance/default\_metrics | Dropped packets | Количество | compute.googleapis.com/mirroring/dropped\_packets\_count |
| gce\_instance/default\_metrics | Mirrored bytes | Байт | compute.googleapis.com/mirroring/mirrored\_bytes\_count |
| gce\_instance/default\_metrics | Mirrored packets | Количество | compute.googleapis.com/mirroring/mirrored\_packets\_count |
| gce\_instance/default\_metrics | Allocated ports | Не указано | compute.googleapis.com/nat/allocated\_ports |
| gce\_instance/default\_metrics | Closed connections count | Не указано | compute.googleapis.com/nat/closed\_connections\_count |
| gce\_instance/default\_metrics | Received packets dropped count | Не указано | compute.googleapis.com/nat/dropped\_received\_packets\_count |
| gce\_instance/default\_metrics | Sent packets dropped count | Не указано | compute.googleapis.com/nat/dropped\_sent\_packets\_count |
| gce\_instance/default\_metrics | New connections count | Не указано | compute.googleapis.com/nat/new\_connections\_count |
| gce\_instance/default\_metrics | Open connections | Не указано | compute.googleapis.com/nat/open\_connections |
| gce\_instance/default\_metrics | Port usage | Не указано | compute.googleapis.com/nat/port\_usage |
| gce\_instance/default\_metrics | Received bytes count | Байт | compute.googleapis.com/nat/received\_bytes\_count |
| gce\_instance/default\_metrics | Received packets count | Не указано | compute.googleapis.com/nat/received\_packets\_count |
| gce\_instance/default\_metrics | Sent bytes count | Байт | compute.googleapis.com/nat/sent\_bytes\_count |
| gce\_instance/default\_metrics | Sent packets count | Не указано | compute.googleapis.com/nat/sent\_packets\_count |
| gce\_instance/agent | Monitoring Agent API Request Count | Количество | agent.googleapis.com/agent/api\_request\_count |
| gce\_instance/agent | Logging Agent Log Entry Count | Количество | agent.googleapis.com/agent/log\_entry\_count |
| gce\_instance/agent | Logging Agent Retried Log Entry Writes Count | Количество | agent.googleapis.com/agent/log\_entry\_retry\_count |
| gce\_instance/agent | Monitoring Agent Memory Usage | Байт | agent.googleapis.com/agent/memory\_usage |
| gce\_instance/agent | Monitoring Agent Metric Point Count | Количество | agent.googleapis.com/agent/monitoring/point\_count |
| gce\_instance/agent | Logging Agent API Request Count | Количество | agent.googleapis.com/agent/request\_count |
| gce\_instance/agent | Monitoring Agent Process Labels Size | Байт | agent.googleapis.com/agent/streamspace\_size |
| gce\_instance/agent | Monitoring Agent is Throttling Processes | Количество | agent.googleapis.com/agent/streamspace\_size\_throttling |
| gce\_instance/agent | Monitoring/Logging Agent Uptime | Секунда | agent.googleapis.com/agent/uptime |
| gce\_instance/agent | Open connections | Количество | agent.googleapis.com/apache/connections |
| gce\_instance/agent | Idle workers | Количество | agent.googleapis.com/apache/idle\_workers |
| gce\_instance/agent | Requests | Количество | agent.googleapis.com/apache/request\_count |
| gce\_instance/agent | Scoreboard | Количество | agent.googleapis.com/apache/scoreboard |
| gce\_instance/agent | Traffic | Байт | agent.googleapis.com/apache/traffic |
| gce\_instance/agent | Hit count | Количество | agent.googleapis.com/cassandra/cache/hits |
| gce\_instance/agent | Read latency | Микросекунда | agent.googleapis.com/cassandra/client\_request/latency/50p |
| gce\_instance/agent | Read latency | Микросекунда | agent.googleapis.com/cassandra/client\_request/latency/95p |
| gce\_instance/agent | Read latency | Микросекунда | agent.googleapis.com/cassandra/client\_request/latency/99p |
| gce\_instance/agent | Read latency | Микросекунда | agent.googleapis.com/cassandra/client\_request/latency/max |
| gce\_instance/agent | Compression ratio | Количество | agent.googleapis.com/cassandra/column\_family/compression\_ratio |
| gce\_instance/agent | Max row size | Байт | agent.googleapis.com/cassandra/column\_family/max\_row\_size |
| gce\_instance/agent | Commit log size | Байт | agent.googleapis.com/cassandra/commitlog\_total\_size |
| gce\_instance/agent | Completed tasks | Количество | agent.googleapis.com/cassandra/completed\_tasks |
| gce\_instance/agent | Tasks | Количество | agent.googleapis.com/cassandra/current\_tasks |
| gce\_instance/agent | Dropped messages | Количество | agent.googleapis.com/cassandra/dropped\_message/dropped\_count |
| gce\_instance/agent | Exceptions | Количество | agent.googleapis.com/cassandra/storage\_service\_exception\_count |
| gce\_instance/agent | Storage load | Байт | agent.googleapis.com/cassandra/storage\_service\_load |
| gce\_instance/agent | Request latency | Миллисекунда | agent.googleapis.com/couchdb/average\_request\_time |
| gce\_instance/agent | Bulk requests | Количество | agent.googleapis.com/couchdb/httpd/bulk\_request\_count |
| gce\_instance/agent | Requests | Количество | agent.googleapis.com/couchdb/httpd/request\_count |
| gce\_instance/agent | Request methods | Количество | agent.googleapis.com/couchdb/httpd/request\_method\_count |
| gce\_instance/agent | Response codes | Количество | agent.googleapis.com/couchdb/httpd/response\_code\_count |
| gce\_instance/agent | Temp view reads | Количество | agent.googleapis.com/couchdb/httpd/temporary\_view\_read\_count |
| gce\_instance/agent | View reads | Количество | agent.googleapis.com/couchdb/httpd/view\_read\_count |
| gce\_instance/agent | Open databases | Количество | agent.googleapis.com/couchdb/open\_databases |
| gce\_instance/agent | Open files | Количество | agent.googleapis.com/couchdb/open\_files |
| gce\_instance/agent | Reads | Количество | agent.googleapis.com/couchdb/read\_count |
| gce\_instance/agent | Writes | Количество | agent.googleapis.com/couchdb/write\_count |
| gce\_instance/agent | CPU load (15m) | Количество | agent.googleapis.com/cpu/load\_15m |
| gce\_instance/agent | CPU load (1m) | Количество | agent.googleapis.com/cpu/load\_1m |
| gce\_instance/agent | CPU load (5m) | Количество | agent.googleapis.com/cpu/load\_5m |
| gce\_instance/agent | CPU usage | Секунда | agent.googleapis.com/cpu/usage\_time |
| gce\_instance/agent | CPU utilization | Процент | agent.googleapis.com/cpu/utilization |
| gce\_instance/agent | Disk usage | Байт | agent.googleapis.com/disk/bytes\_used |
| gce\_instance/agent | Disk I/O time | Миллисекунда | agent.googleapis.com/disk/io\_time |
| gce\_instance/agent | Disk merged operations | Количество | agent.googleapis.com/disk/merged\_operations |
| gce\_instance/agent | Disk operations | Количество | agent.googleapis.com/disk/operation\_count |
| gce\_instance/agent | Disk operation time | Миллисекунда | agent.googleapis.com/disk/operation\_time |
| gce\_instance/agent | Disk pending operations | Количество | agent.googleapis.com/disk/pending\_operations |
| gce\_instance/agent | Disk utilization | Процент | agent.googleapis.com/disk/percent\_used |
| gce\_instance/agent | Disk bytes read | Байт | agent.googleapis.com/disk/read\_bytes\_count |
| gce\_instance/agent | Disk weighted I/O time | Миллисекунда | agent.googleapis.com/disk/weighted\_io\_time |
| gce\_instance/agent | Disk bytes written | Байт | agent.googleapis.com/disk/write\_bytes\_count |
| gce\_instance/agent | Cache size | Байт | agent.googleapis.com/elasticsearch/cache\_memory\_usage |
| gce\_instance/agent | Field evictions | Количество | agent.googleapis.com/elasticsearch/field\_eviction\_count |
| gce\_instance/agent | Filter evictions | Количество | agent.googleapis.com/elasticsearch/filter\_cache\_eviction\_count |
| gce\_instance/agent | GC count | Количество | agent.googleapis.com/elasticsearch/gc\_collection\_count |
| gce\_instance/agent | Memory usage | Байт | agent.googleapis.com/elasticsearch/memory\_usage |
| gce\_instance/agent | Network traffic | Байт | agent.googleapis.com/elasticsearch/network |
| gce\_instance/agent | Documents | Количество | agent.googleapis.com/elasticsearch/num\_current\_documents |
| gce\_instance/agent | Data nodes | Количество | agent.googleapis.com/elasticsearch/num\_data\_nodes |
| gce\_instance/agent | Open connections | Количество | agent.googleapis.com/elasticsearch/num\_http\_connections |
| gce\_instance/agent | Nodes | Количество | agent.googleapis.com/elasticsearch/num\_nodes |
| gce\_instance/agent | Open files | Количество | agent.googleapis.com/elasticsearch/num\_open\_files |
| gce\_instance/agent | Open connections | Количество | agent.googleapis.com/elasticsearch/num\_server\_connections |
| gce\_instance/agent | Shards | Количество | agent.googleapis.com/elasticsearch/num\_shards |
| gce\_instance/agent | Completed operations | Количество | agent.googleapis.com/elasticsearch/operation\_count |
| gce\_instance/agent | Operation time | Миллисекунда | agent.googleapis.com/elasticsearch/operation\_time |
| gce\_instance/agent | Max threads | Количество | agent.googleapis.com/elasticsearch/peak\_threads |
| gce\_instance/agent | Storage size | Байт | agent.googleapis.com/elasticsearch/storage\_size |
| gce\_instance/agent | Threads | Количество | agent.googleapis.com/elasticsearch/threads |
| gce\_instance/agent | IPC connections | Количество | agent.googleapis.com/hbase/ipc/connections |
| gce\_instance/agent | IPC queue size | Количество | agent.googleapis.com/hbase/ipc/queue\_length |
| gce\_instance/agent | IPC traffic | Байт | agent.googleapis.com/hbase/ipc/traffic\_count |
| gce\_instance/agent | Load | Количество | agent.googleapis.com/hbase/master/average\_load |
| gce\_instance/agent | Dead region servers | Количество | agent.googleapis.com/hbase/master/dead\_region\_servers |
| gce\_instance/agent | Live region servers | Количество | agent.googleapis.com/hbase/master/live\_region\_servers |
| gce\_instance/agent | Block cache accesses | Количество | agent.googleapis.com/hbase/regionserver/block\_cache/access\_count |
| gce\_instance/agent | Evicted block count | Количество | agent.googleapis.com/hbase/regionserver/block\_cache/evicted\_blocks\_count |
| gce\_instance/agent | Block cache hit ratio | Процент | agent.googleapis.com/hbase/regionserver/block\_cache/hit\_ratio\_percent |
| gce\_instance/agent | Block cache size | Байт | agent.googleapis.com/hbase/regionserver/block\_cache/memory |
| gce\_instance/agent | Block count | Количество | agent.googleapis.com/hbase/regionserver/block\_cache/num\_items |
| gce\_instance/agent | Call queue size | Количество | agent.googleapis.com/hbase/regionserver/call\_queue/length |
| gce\_instance/agent | Compaction queue size | Количество | agent.googleapis.com/hbase/regionserver/compaction\_queue/length |
| gce\_instance/agent | Flush queue size | Количество | agent.googleapis.com/hbase/regionserver/flush\_queue/length |
| gce\_instance/agent | Heap usage | Байт | agent.googleapis.com/hbase/regionserver/memory/heap\_usage |
| gce\_instance/agent | Memstore files | Количество | agent.googleapis.com/hbase/regionserver/memstore/files |
| gce\_instance/agent | Memstore index size | Байт | agent.googleapis.com/hbase/regionserver/memstore/index\_size |
| gce\_instance/agent | Memstore open stores | Количество | agent.googleapis.com/hbase/regionserver/memstore/open\_stores |
| gce\_instance/agent | Memstore size | Байт | agent.googleapis.com/hbase/regionserver/memstore/size |
| gce\_instance/agent | Online regions | Количество | agent.googleapis.com/hbase/regionserver/online\_regions |
| gce\_instance/agent | Request count | Количество | agent.googleapis.com/hbase/regionserver/request\_count |
| gce\_instance/agent | RPC request rate | 1/с | agent.googleapis.com/hbase/regionserver/requests/total\_rate |
| gce\_instance/agent | Slow operations | Количество | agent.googleapis.com/hbase/regionserver/slow\_operation\_count |
| gce\_instance/agent | Thrift average batch latency | Наносекунда | agent.googleapis.com/hbase/thrift/batch\_latency/average |
| gce\_instance/agent | Thrift average call latency | Наносекунда | agent.googleapis.com/hbase/thrift/call\_latency/average |
| gce\_instance/agent | Thrift call queue size | Количество | agent.googleapis.com/hbase/thrift/call\_queue/length |
| gce\_instance/agent | Thrift average slow call latency | Наносекунда | agent.googleapis.com/hbase/thrift/slow\_call\_latency/average |
| gce\_instance/agent | Thrift average time in queue | Наносекунда | agent.googleapis.com/hbase/thrift/time\_in\_queue/average |
| gce\_instance/agent | IIS open connections | Количество | agent.googleapis.com/iis/current\_connections |
| gce\_instance/agent | IIS transferred bytes | Байт | agent.googleapis.com/iis/network/transferred\_bytes\_count |
| gce\_instance/agent | IIS connections | Количество | agent.googleapis.com/iis/new\_connection\_count |
| gce\_instance/agent | IIS requests | Количество | agent.googleapis.com/iis/request\_count |
| gce\_instance/agent | Network errors | Количество | agent.googleapis.com/interface/errors |
| gce\_instance/agent | Network packets | Количество | agent.googleapis.com/interface/packets |
| gce\_instance/agent | Network traffic | Байт | agent.googleapis.com/interface/traffic |
| gce\_instance/agent | GC count | Количество | agent.googleapis.com/jvm/gc/count |
| gce\_instance/agent | GC time | Миллисекунда | agent.googleapis.com/jvm/gc/time |
| gce\_instance/agent | Memory usage | Байт | agent.googleapis.com/jvm/memory/usage |
| gce\_instance/agent | CPU time | Наносекунда | agent.googleapis.com/jvm/os/cpu\_time |
| gce\_instance/agent | Open files | Количество | agent.googleapis.com/jvm/os/open\_files |
| gce\_instance/agent | Daemon threads | Количество | agent.googleapis.com/jvm/thread/num\_daemon |
| gce\_instance/agent | Threads | Количество | agent.googleapis.com/jvm/thread/num\_live |
| gce\_instance/agent | Max threads | Количество | agent.googleapis.com/jvm/thread/peak |
| gce\_instance/agent | Uptime | Миллисекунда | agent.googleapis.com/jvm/uptime |
| gce\_instance/agent | Failed requests | Количество | agent.googleapis.com/kafka/broker/topics/failed\_request\_count |
| gce\_instance/agent | Incoming messages | Количество | agent.googleapis.com/kafka/broker/topics/incoming\_message\_count |
| gce\_instance/agent | Traffic | Байт | agent.googleapis.com/kafka/broker/topics/traffic |
| gce\_instance/agent | Active controllers | Количество | agent.googleapis.com/kafka/controller/kafka/active |
| gce\_instance/agent | Offline partitions | Количество | agent.googleapis.com/kafka/controller/kafka/offline\_partitions |
| gce\_instance/agent | Leader elections | Количество | agent.googleapis.com/kafka/controller/leader\_elections/election\_count |
| gce\_instance/agent | Stale leader elections | Количество | agent.googleapis.com/kafka/controller/leader\_elections/unclean\_count |
| gce\_instance/agent | Flushes | Количество | agent.googleapis.com/kafka/log/flush\_count |
| gce\_instance/agent | Requests | Количество | agent.googleapis.com/kafka/network/request\_count |
| gce\_instance/agent | Delayed purgatory requests | Количество | agent.googleapis.com/kafka/purgatory/num\_delayed\_requests |
| gce\_instance/agent | Purgatory requests | Количество | agent.googleapis.com/kafka/purgatory/size |
| gce\_instance/agent | Maximum lag | Количество | agent.googleapis.com/kafka/replica\_fetcher/max\_lag |
| gce\_instance/agent | Minimum fetch rate | 1/с | agent.googleapis.com/kafka/replica\_fetcher/min\_fetch\_rate |
| gce\_instance/agent | Gaining replicas | Количество | agent.googleapis.com/kafka/replica\_manager/isr/expand\_count |
| gce\_instance/agent | Lagging replicas | Количество | agent.googleapis.com/kafka/replica\_manager/isr/shrink\_count |
| gce\_instance/agent | Leaders | Количество | agent.googleapis.com/kafka/replica\_manager/leaders |
| gce\_instance/agent | Partitions | Количество | agent.googleapis.com/kafka/replica\_manager/partitions |
| gce\_instance/agent | Unreliable partitions | Количество | agent.googleapis.com/kafka/replica\_manager/under\_replicated\_partitions |
| gce\_instance/agent | Commands | Количество | agent.googleapis.com/memcached/command\_count |
| gce\_instance/agent | Connections | Количество | agent.googleapis.com/memcached/current\_connections |
| gce\_instance/agent | Items | Количество | agent.googleapis.com/memcached/current\_items |
| gce\_instance/agent | Evictions | Количество | agent.googleapis.com/memcached/eviction\_count |
| gce\_instance/agent | Memory usage | Байт | agent.googleapis.com/memcached/memory |
| gce\_instance/agent | Traffic | Байт | agent.googleapis.com/memcached/network |
| gce\_instance/agent | Operations | Количество | agent.googleapis.com/memcached/operation\_count |
| gce\_instance/agent | Hit ratio | Процент | agent.googleapis.com/memcached/operation\_hitratio |
| gce\_instance/agent | CPU time | Секунда | agent.googleapis.com/memcached/rusage |
| gce\_instance/agent | Threads | Количество | agent.googleapis.com/memcached/threads |
| gce\_instance/agent | Memory usage | Байт | agent.googleapis.com/memory/bytes\_used |
| gce\_instance/agent | Memory utilization | Процент | agent.googleapis.com/memory/percent\_used |
| gce\_instance/agent | Cache hits | Количество | agent.googleapis.com/mongodb/cache/hits |
| gce\_instance/agent | Cache misses | Количество | agent.googleapis.com/mongodb/cache/misses |
| gce\_instance/agent | Collections | Количество | agent.googleapis.com/mongodb/collections |
| gce\_instance/agent | Connections | Количество | agent.googleapis.com/mongodb/connections |
| gce\_instance/agent | Data size | Байт | agent.googleapis.com/mongodb/data\_size |
| gce\_instance/agent | Extents | Количество | agent.googleapis.com/mongodb/extents |
| gce\_instance/agent | Global lock time | Миллисекунда | agent.googleapis.com/mongodb/global\_lock\_hold\_time |
| gce\_instance/agent | Index size | Байт | agent.googleapis.com/mongodb/index\_size |
| gce\_instance/agent | Indexes | Количество | agent.googleapis.com/mongodb/indexes |
| gce\_instance/agent | Memory usage | Мебибайт | agent.googleapis.com/mongodb/memory\_usage |
| gce\_instance/agent | Objects | Количество | agent.googleapis.com/mongodb/objects |
| gce\_instance/agent | Operations | Количество | agent.googleapis.com/mongodb/operation\_count |
| gce\_instance/agent | Storage size | Байт | agent.googleapis.com/mongodb/storage\_size |
| gce\_instance/agent | SQL Server open connections | Количество | agent.googleapis.com/mssql/connections/user |
| gce\_instance/agent | SQL Server transaction rate | 1/с | agent.googleapis.com/mssql/transaction\_rate |
| gce\_instance/agent | SQL Server write transaction rate | 1/с | agent.googleapis.com/mssql/write\_transaction\_rate |
| gce\_instance/agent | Buffer pool pages | Количество | agent.googleapis.com/mysql/buffer\_pool/num\_pages |
| gce\_instance/agent | Buffer pool operations | Количество | agent.googleapis.com/mysql/buffer\_pool/operation\_count |
| gce\_instance/agent | Buffer pool size | Байт | agent.googleapis.com/mysql/buffer\_pool\_size |
| gce\_instance/agent | Commands | Количество | agent.googleapis.com/mysql/command\_count |
| gce\_instance/agent | Handlers | Количество | agent.googleapis.com/mysql/handler\_count |
| gce\_instance/agent | InnoDB doublewrite buffers | Количество | agent.googleapis.com/mysql/innodb/doublewrite\_count |
| gce\_instance/agent | InnoDB log operations | Количество | agent.googleapis.com/mysql/innodb/log\_operation\_count |
| gce\_instance/agent | InnoDB operations | Количество | agent.googleapis.com/mysql/innodb/operation\_count |
| gce\_instance/agent | InnoDB page operations | Количество | agent.googleapis.com/mysql/innodb/page\_operation\_count |
| gce\_instance/agent | InnoDB locks | Количество | agent.googleapis.com/mysql/innodb/row\_lock\_count |
| gce\_instance/agent | InnoDB row operations | Количество | agent.googleapis.com/mysql/innodb/row\_operation\_count |
| gce\_instance/agent | Locks | Количество | agent.googleapis.com/mysql/lock\_count |
| gce\_instance/agent | QCache operations | Количество | agent.googleapis.com/mysql/qcache/operation\_count |
| gce\_instance/agent | QCache queries | Количество | agent.googleapis.com/mysql/qcache/query\_count |
| gce\_instance/agent | Replica lag | Секунда | agent.googleapis.com/mysql/slave\_replication\_lag |
| gce\_instance/agent | Sorts | Количество | agent.googleapis.com/mysql/sort\_count |
| gce\_instance/agent | Threads | Количество | agent.googleapis.com/mysql/thread\_count |
| gce\_instance/agent | TCP connections | Количество | agent.googleapis.com/network/tcp\_connections |
| gce\_instance/agent | Accepted connections | Количество | agent.googleapis.com/nginx/connections/accepted\_count |
| gce\_instance/agent | Active connections | Количество | agent.googleapis.com/nginx/connections/current |
| gce\_instance/agent | Handled connections | Количество | agent.googleapis.com/nginx/connections/handled\_count |
| gce\_instance/agent | Requests | Количество | agent.googleapis.com/nginx/request\_count |
| gce\_instance/agent | Pagefile utilization | Процент | agent.googleapis.com/pagefile/percent\_used |
| gce\_instance/agent | Blocks read | Количество | agent.googleapis.com/postgresql/blocks\_read\_count |
| gce\_instance/agent | Commits | Количество | agent.googleapis.com/postgresql/commit\_count |
| gce\_instance/agent | DB size | Байт | agent.googleapis.com/postgresql/db\_size |
| gce\_instance/agent | Backends | Количество | agent.googleapis.com/postgresql/num\_backends |
| gce\_instance/agent | DB rows | Количество | agent.googleapis.com/postgresql/num\_tuples |
| gce\_instance/agent | Operations | Количество | agent.googleapis.com/postgresql/operation\_count |
| gce\_instance/agent | Rollbacks | Количество | agent.googleapis.com/postgresql/rollback\_count |
| gce\_instance/agent | Processes | Количество | agent.googleapis.com/processes/count\_by\_state |
| gce\_instance/agent | Process CPU | Секунда | agent.googleapis.com/processes/cpu\_time |
| gce\_instance/agent | Process disk read I/O | Байт | agent.googleapis.com/processes/disk/read\_bytes\_count |
| gce\_instance/agent | Process disk write I/O | Байт | agent.googleapis.com/processes/disk/write\_bytes\_count |
| gce\_instance/agent | Fork count | Количество | agent.googleapis.com/processes/fork\_count |
| gce\_instance/agent | Process resident memory | Байт | agent.googleapis.com/processes/rss\_usage |
| gce\_instance/agent | Process virtual memory | Байт | agent.googleapis.com/processes/vm\_usage |
| gce\_instance/agent | Consumers | Количество | agent.googleapis.com/rabbitmq/consumers |
| gce\_instance/agent | Delivery rate | 1/с | agent.googleapis.com/rabbitmq/delivery\_rate |
| gce\_instance/agent | Messages | Количество | agent.googleapis.com/rabbitmq/num\_messages |
| gce\_instance/agent | Publish rate | 1/с | agent.googleapis.com/rabbitmq/publish\_rate |
| gce\_instance/agent | Unsaved changes | Количество | agent.googleapis.com/redis/changes\_since\_last\_save |
| gce\_instance/agent | Blocked clients | Количество | agent.googleapis.com/redis/clients/blocked |
| gce\_instance/agent | Connected clients | Количество | agent.googleapis.com/redis/clients/connected |
| gce\_instance/agent | Commands | Количество | agent.googleapis.com/redis/commands\_processed |
| gce\_instance/agent | Slave connections | Количество | agent.googleapis.com/redis/connections/slaves |
| gce\_instance/agent | Connections | Количество | agent.googleapis.com/redis/connections/total |
| gce\_instance/agent | Expired keys | Количество | agent.googleapis.com/redis/expired\_keys |
| gce\_instance/agent | Memory usage | Байт | agent.googleapis.com/redis/memory/usage |
| gce\_instance/agent | Lua memory usage | Байт | agent.googleapis.com/redis/memory/usage\_lua |
| gce\_instance/agent | PubSub channels | Количество | agent.googleapis.com/redis/pubsub/channels |
| gce\_instance/agent | PubSub patterns | Количество | agent.googleapis.com/redis/pubsub/patterns |
| gce\_instance/agent | Uptime | Секунда | agent.googleapis.com/redis/uptime |
| gce\_instance/agent | 95% latency (1m) | Микросекунда | agent.googleapis.com/riak/latency/95th\_percentile |
| gce\_instance/agent | Average latency (1m) | Микросекунда | agent.googleapis.com/riak/latency/average |
| gce\_instance/agent | Maximum latency (1m) | Микросекунда | agent.googleapis.com/riak/latency/maximum |
| gce\_instance/agent | Memory usage | Байт | agent.googleapis.com/riak/memory\_usage |
| gce\_instance/agent | 95% siblings (1m) | Количество | agent.googleapis.com/riak/num\_siblings/95th\_percentile |
| gce\_instance/agent | Average siblings (1m) | Количество | agent.googleapis.com/riak/num\_siblings/average |
| gce\_instance/agent | Maximum siblings (1m) | Количество | agent.googleapis.com/riak/num\_siblings/maximum |
| gce\_instance/agent | 95% object size (1m) | Байт | agent.googleapis.com/riak/object\_size/95th\_percentile |
| gce\_instance/agent | Average object size (1m) | Байт | agent.googleapis.com/riak/object\_size/average |
| gce\_instance/agent | Maximum object size (1m) | Байт | agent.googleapis.com/riak/object\_size/maximum |
| gce\_instance/agent | Operations | Количество | agent.googleapis.com/riak/operation\_count |
| gce\_instance/agent | Swap usage | Байт | agent.googleapis.com/swap/bytes\_used |
| gce\_instance/agent | Swap I/O operations | Количество | agent.googleapis.com/swap/io |
| gce\_instance/agent | Swap utilization | Процент | agent.googleapis.com/swap/percent\_used |
| gce\_instance/agent | Sessions | Количество | agent.googleapis.com/tomcat/manager/sessions |
| gce\_instance/agent | Errors | Количество | agent.googleapis.com/tomcat/request\_processor/error\_count |
| gce\_instance/agent | Processing time | Миллисекунда | agent.googleapis.com/tomcat/request\_processor/processing\_time |
| gce\_instance/agent | Requests | Количество | agent.googleapis.com/tomcat/request\_processor/request\_count |
| gce\_instance/agent | Traffic | Байт | agent.googleapis.com/tomcat/request\_processor/traffic\_count |
| gce\_instance/agent | Busy threads | Количество | agent.googleapis.com/tomcat/threads/busy |
| gce\_instance/agent | Current threads | Количество | agent.googleapis.com/tomcat/threads/current |
| gce\_instance/agent | Backend connection successes | Количество | agent.googleapis.com/varnish/backend\_connection\_count |
| gce\_instance/agent | Cache operations | Количество | agent.googleapis.com/varnish/cache\_operation\_count |
| gce\_instance/agent | Client connections | Количество | agent.googleapis.com/varnish/client\_connection\_count |
| gce\_instance/agent | Open connections | Количество | agent.googleapis.com/zookeeper/connections\_count |
| gce\_instance/agent | Data size | Байт | agent.googleapis.com/zookeeper/data\_size |
| gce\_instance/agent | Followers | Количество | agent.googleapis.com/zookeeper/followers/count |
| gce\_instance/agent | Synced followers | Количество | agent.googleapis.com/zookeeper/followers/synced\_count |
| gce\_instance/agent | Packets received | Количество | agent.googleapis.com/zookeeper/network/received\_packets\_count |
| gce\_instance/agent | Packets sent | Количество | agent.googleapis.com/zookeeper/network/sent\_packets\_count |
| gce\_instance/agent | Nodes | Количество | agent.googleapis.com/zookeeper/nodes/count |
| gce\_instance/agent | Ephemeral nodes | Количество | agent.googleapis.com/zookeeper/nodes/ephemeral\_count |
| gce\_instance/agent | Watches | Количество | agent.googleapis.com/zookeeper/nodes/watches\_count |
| gce\_instance/agent | Average request latency | Миллисекунда | agent.googleapis.com/zookeeper/requests/latency/average |
| gce\_instance/agent | Maximum request latency | Миллисекунда | agent.googleapis.com/zookeeper/requests/latency/maximum |
| gce\_instance/agent | Minimum request latency | Миллисекунда | agent.googleapis.com/zookeeper/requests/latency/minimum |
| gce\_instance/agent | Outstanding requests | Количество | agent.googleapis.com/zookeeper/requests/outstanding\_count |
| gce\_instance/agent | Pending syncs | Количество | agent.googleapis.com/zookeeper/sync\_operations/pending\_count |
| gce\_instance/firewallinsights | VM Firewall Hit Counts | Количество | firewallinsights.googleapis.com/vm/firewall\_hit\_count |
| gce\_instance/firewallinsights | VM Firewall Last Used Timestamp | Количество | firewallinsights.googleapis.com/vm/firewall\_last\_used\_timestamp |
| gce\_instance/istio | Client Connection Close Count | Байт | istio.io/service/client/connection\_close\_count |
| gce\_instance/istio | Client Connection Open Count | Байт | istio.io/service/client/connection\_open\_count |
| gce\_instance/istio | Client Received Bytes Count | Байт | istio.io/service/client/received\_bytes\_count |
| gce\_instance/istio | Client Request Bytes | Байт | istio.io/service/client/request\_bytes |
| gce\_instance/istio | Client Request Count | Количество | istio.io/service/client/request\_count |
| gce\_instance/istio | Client Response Bytes | Байт | istio.io/service/client/response\_bytes |
| gce\_instance/istio | Client Roundtrip Latencies | Миллисекунда | istio.io/service/client/roundtrip\_latencies |
| gce\_instance/istio | Client Sent Bytes Count | Байт | istio.io/service/client/sent\_bytes\_count |
| gce\_instance/istio | Server Connection Close Count | Байт | istio.io/service/server/connection\_close\_count |
| gce\_instance/istio | Server Connection Open Count | Байт | istio.io/service/server/connection\_open\_count |
| gce\_instance/istio | Server Received Bytes Count | Байт | istio.io/service/server/received\_bytes\_count |
| gce\_instance/istio | Server Request Bytes | Байт | istio.io/service/server/request\_bytes |
| gce\_instance/istio | Server Request Count | Количество | istio.io/service/server/request\_count |
| gce\_instance/istio | Server Response Bytes | Байт | istio.io/service/server/response\_bytes |
| gce\_instance/istio | Server Response Latencies | Миллисекунда | istio.io/service/server/response\_latencies |
| gce\_instance/istio | Server Sent Bytes Count | Байт | istio.io/service/server/sent\_bytes\_count |
| gce\_instance\_vm\_flow/default\_metrics | Egress bytes | Байт | networking.googleapis.com/vm\_flow/egress\_bytes\_count |
| gce\_instance\_vm\_flow/default\_metrics | Ingress bytes | Байт | networking.googleapis.com/vm\_flow/ingress\_bytes\_count |
| gce\_instance\_vm\_flow/default\_metrics | RTT latencies | Миллисекунда | networking.googleapis.com/vm\_flow/rtt |
| instance\_group/default\_metrics | Instance group size | Количество | compute.googleapis.com/instance\_group/size |
| autoscaler/default\_metrics | Serving capacity | Количество | autoscaler.googleapis.com/capacity |
| autoscaler/default\_metrics | Current Autoscaler utilization | Количество | autoscaler.googleapis.com/current\_utilization |
| tpu\_worker/default\_metrics | Container CPU utilization | Процент | tpu.googleapis.com/container/cpu/utilization |
| tpu\_worker/default\_metrics | Container memory usage | Байт | tpu.googleapis.com/container/memory/usage |
| tpu\_worker/default\_metrics | CPU utilization | Процент | tpu.googleapis.com/cpu/utilization |
| tpu\_worker/default\_metrics | Memory usage | Байт | tpu.googleapis.com/memory/usage |
| tpu\_worker/default\_metrics | Network bytes received | Байт | tpu.googleapis.com/network/received\_bytes\_count |
| tpu\_worker/default\_metrics | Network bytes sent | Байт | tpu.googleapis.com/network/sent\_bytes\_count |
| tpu\_worker/default\_metrics | MXU utilization | Процент | tpu.googleapis.com/tpu/mxu/utilization |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")