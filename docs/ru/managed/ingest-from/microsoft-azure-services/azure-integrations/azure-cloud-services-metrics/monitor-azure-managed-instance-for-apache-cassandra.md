---
title: Azure Managed Instance for Apache Cassandra Monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-managed-instance-for-apache-cassandra
scraped: 2026-02-28T21:24:50.970245
---

# Azure Managed Instance for Apache Cassandra Monitoring

# Azure Managed Instance for Apache Cassandra Monitoring

* Latest Dynatrace
* How-to guide
* 11-min read
* Published Apr 18, 2022

From both a data and infrastructure perspective, this [Prometheus Extension 2.0](/docs/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions "Learn how to create a Prometheus extension using the Extensions framework.") allows you to monitors and analyze the activity of your Apache Cassandra clusters. It visualize your cluster's health and shows metrics like CPU, connectivity, request latency, suspension, and garbage collection time. Additionally, with [Davis](/docs/dynatrace-intelligence "Get familiar with the capabilities of Dynatrace Intelligence."), it automatically detects performance problems and provides precise root cause analysis.

## Prerequisites

* [Azure Managed Instance for Apache Cassandraï»¿](https://docs.microsoft.com/en-us/azure/managed-instance-apache-cassandra/) created and running.
* An Ubuntu virtual machine deployed inside the Azure Virtual Network where the managed instance is present.
* Prometheus server set up to scrape Cassandra nodes and with [relabelï»¿](https://github.com/datastax/metric-collector-for-apache-cassandra/blob/master/dashboards/prometheus/prometheus.yaml) config in place.
* [Environment ActiveGate version 1.231+](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-install-an-environment-activegate "Read the step-by-step procedure for installing an Environment ActiveGate on Linux.") with access to the Prometheus server

## Setup

1. Create an Ubuntu virtual machine in the same virtual network as your Azure Managed Instance for Apache Cassandra.
2. Ensure Docker is installed on your virtual machine.
3. Create a file named `prometheus.yml` on your virtual machine with the contents below.  
   Add every Cassandra Node IP address and port `9443` in the `static_configs` section. The IP addresses can be gathered from the Data Center section of the Azure Portal for your Cassandra Cluster.

   ```
   static_configs:



   - targets: ["<Node_IP_1>:9443", "<Node_IP_2>:9443", "<Node_IP_N>:9443"]
   ```

prometheus.yml

```
global:



scrape_interval: 15s



scrape_timeout: 10s



evaluation_interval: 15s



alerting:



alertmanagers:



- static_configs:



- targets: []



scheme: http



timeout: 10s



scrape_configs:



- job_name: prometheus



scrape_interval: 15s



scrape_timeout: 15s



metrics_path: /metrics



scheme: http



static_configs:



- targets:



- localhost:9090



- job_name: "mcac"



scrape_interval: 15s



scrape_timeout:  15s



static_configs:



- targets: ["<Node_IP_1>:9443", "<Node_IP_2>:9443", "<Node_IP_N>:9443"]



honor_labels: true



honor_timestamps: false



scheme: https



tls_config:



insecure_skip_verify: true



metric_relabel_configs:



#drop metrics we can calculate from prometheus directly



- source_labels: [__name__]



regex: .*rate_(mean|1m|5m|15m)



action: drop



#save the original name for all metrics



- source_labels: [__name__]



regex: (collectd_mcac_.+)



target_label: prom_name



replacement: ${1}



- source_labels: ["prom_name"]



regex: .+_bucket_(\d+)



target_label: le



replacement: ${1}



- source_labels: ["prom_name"]



regex: .+_bucket_inf



target_label: le



replacement: +Inf



- source_labels: ["prom_name"]



regex: .*_histogram_p(\d+)



target_label: quantile



replacement: .${1}



- source_labels: ["prom_name"]



regex: .*_histogram_min



target_label: quantile



replacement: "0"



- source_labels: ["prom_name"]



regex: .*_histogram_max



target_label: quantile



replacement: "1"



#Table Metrics *ALL* we can drop



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.table\.(\w+)



action: drop



#Table Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.table\.(\w+)\.(\w+)\.(\w+)



target_label: table



replacement: ${3}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.table\.(\w+)\.(\w+)\.(\w+)



target_label: keyspace



replacement: ${2}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.table\.(\w+)\.(\w+)\.(\w+)



target_label: __name__



replacement: mcac_table_${1}



#Keyspace Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.keyspace\.(\w+)\.(\w+)



target_label: keyspace



replacement: ${2}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.keyspace\.(\w+)\.(\w+)



target_label: __name__



replacement: mcac_keyspace_${1}



#ThreadPool Metrics (one type is repair.task so we just ignore the second part)



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.thread_pools\.(\w+)\.(\w+)\.(\w+).*



target_label: pool_type



replacement: ${2}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.thread_pools\.(\w+)\.(\w+)\.(\w+).*



target_label: pool_name



replacement: ${3}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.thread_pools\.(\w+)\.(\w+)\.(\w+).*



target_label: __name__



replacement: mcac_thread_pools_${1}



#ClientRequest Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.client_request\.(\w+)\.(\w+)$



target_label: request_type



replacement: ${2}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.client_request\.(\w+)\.(\w+)$



target_label: __name__



replacement: mcac_client_request_${1}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.client_request\.(\w+)\.(\w+)\.(\w+)$



target_label: cl



replacement: ${3}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.client_request\.(\w+)\.(\w+)\.(\w+)$



target_label: request_type



replacement: ${2}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.client_request\.(\w+)\.(\w+)\.(\w+)$



target_label: __name__



replacement: mcac_client_request_${1}_cl



#Cache Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.cache\.(\w+)\.(\w+)



target_label: cache_name



replacement: ${2}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.cache\.(\w+)\.(\w+)



target_label: __name__



replacement: mcac_cache_${1}



#CQL Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.cql\.(\w+)



target_label: __name__



replacement: mcac_cql_${1}



#Dropped Message Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.dropped_message\.(\w+)\.(\w+)



target_label: message_type



replacement: ${2}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.dropped_message\.(\w+)\.(\w+)



target_label: __name__



replacement: mcac_dropped_message_${1}



#Streaming Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.streaming\.(\w+)\.(.+)$



target_label: peer_ip



replacement: ${2}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.streaming\.(\w+)\.(.+)$



target_label: __name__



replacement: mcac_streaming_${1}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.streaming\.(\w+)$



target_label: __name__



replacement: mcac_streaming_${1}



#CommitLog Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.commit_log\.(\w+)



target_label: __name__



replacement: mcac_commit_log_${1}



#Compaction Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.compaction\.(\w+)



target_label: __name__



replacement: mcac_compaction_${1}



#Storage Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.storage\.(\w+)



target_label: __name__



replacement: mcac_storage_${1}



#Batch Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.batch\.(\w+)



target_label: __name__



replacement: mcac_batch_${1}



#Client Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.client\.(\w+)



target_label: __name__



replacement: mcac_client_${1}



#BufferPool Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.buffer_pool\.(\w+)



target_label: __name__



replacement: mcac_buffer_pool_${1}



#Index Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.index\.(\w+)



target_label: __name__



replacement: mcac_sstable_index_${1}



#HintService Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.hinted_hand_off_manager\.([^\-]+)-(\w+)



target_label: peer_ip



replacement: ${2}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.hinted_hand_off_manager\.([^\-]+)-(\w+)



target_label: __name__



replacement: mcac_hints_${1}



#HintService Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.hints_service\.hints_delays\-(\w+)



target_label: peer_ip



replacement: ${1}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.hints_service\.hints_delays\-(\w+)



target_label: __name__



replacement: mcac_hints_hints_delays



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.hints_service\.([^\-]+)



target_label: __name__



replacement: mcac_hints_${1}



# Misc





- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.memtable_pool\.(\w+)



target_label: __name__



replacement: mcac_memtable_pool_${1}



- source_labels: ["mcac"]



regex: com\.datastax\.bdp\.type\.performance_objects\.name\.cql_slow_log\.metrics\.queries_latency



target_label: __name__



replacement: mcac_cql_slow_log_query_latency



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.read_coordination\.(.*)



target_label: read_type



replacement: $1



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.read_coordination\.(.*)



target_label: __name__



replacement: mcac_read_coordination_requests



#GC Metrics



- source_labels: ["mcac"]



regex: jvm\.gc\.(\w+)\.(\w+)



target_label: collector_type



replacement: ${1}



- source_labels: ["mcac"]



regex: jvm\.gc\.(\w+)\.(\w+)



target_label: __name__



replacement: mcac_jvm_gc_${2}



#JVM Metrics



- source_labels: ["mcac"]



regex: jvm\.memory\.(\w+)\.(\w+)



target_label: memory_type



replacement: ${1}



- source_labels: ["mcac"]



regex: jvm\.memory\.(\w+)\.(\w+)



target_label: __name__



replacement: mcac_jvm_memory_${2}



- source_labels: ["mcac"]



regex: jvm\.memory\.pools\.(\w+)\.(\w+)



target_label: pool_name



replacement: ${2}



- source_labels: ["mcac"]



regex: jvm\.memory\.pools\.(\w+)\.(\w+)



target_label: __name__



replacement: mcac_jvm_memory_pool_${2}



- source_labels: ["mcac"]



regex: jvm\.fd\.usage



target_label: __name__



replacement: mcac_jvm_fd_usage



- source_labels: ["mcac"]



regex: jvm\.buffers\.(\w+)\.(\w+)



target_label: buffer_type



replacement: ${1}



- source_labels: ["mcac"]



regex: jvm\.buffers\.(\w+)\.(\w+)



target_label: __name__



replacement: mcac_jvm_buffer_${2}



#Append the prom types back to formatted names



- source_labels: [__name__, "prom_name"]



regex: (mcac_.*);.*(_micros_bucket|_bucket|_micros_count_total|_count_total|_total|_micros_sum|_sum|_stddev).*



separator: ;



target_label: __name__



replacement: ${1}${2}



- regex: prom_name



action: labeldrop
```

4. Start your Prometheus server Docker container.

   Be sure to change the path in the command below to point to the `prometheus.yml` file from above.

   ```
   docker run \



   -d \



   -p 9090:9090 \



   -v /path/to/prometheus.yml:/etc/prometheus/prometheus.yml \



   prom/prometheus
   ```
5. If your virtual machine is not available from the internet, install a [Dynatrace Environment ActiveGate](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-install-an-environment-activegate "Read the step-by-step procedure for installing an Environment ActiveGate on Linux.") on your Ubuntu VM.  
   **Recommended:** Set the `group` [property](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#group "Learn about the command-line parameters that you can use with ActiveGate on Linux.") on the installation.

## Enable and configure extension

1. In Dynatrace Hub, select **Azure Managed Instance for Apache Cassandra**.
2. Enable the extension.
3. Verify that the Prometheus endpoint publishes the Cassandra metrics. Use either of these queries:

   `{__name__=~"mcac.*"}`

   `http://<Prometheus Server URL>:9090/api/v1/query?query=%7B__name__%3D%7E%22mcac.*%22%7D`
4. Add the endpoint of your Prometheus server to the Extension Monitoring Configuration:

   `http://<Prometheus Server URL>:9090/api/v1`

   The `<Prometheus Server URL>` does not need to be public. If you install your ActiveGate on the same VM or same VNet as the Prometheus server, `localhost` or a private IP can be used.
5. Select the ActiveGate group on which to enable this extension.
6. Add a Monitoring Configuration description and select the Feature Sets of the metrics you'd like to collect.
7. A dashboard named **Azure Managed Instance for Apache Cassandra Overview** is provided with the extension.

## Metrics

Available metrics are listed below.

* Metric metadata and dimensions are available using [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") after the extension is enabled.
* See [Apache Cassandra Monitoring Documentationï»¿](https://cassandra.apache.org/doc/latest/cassandra/operating/metrics.html) for more information about collected metrics.

### Cluster node metrics

| Metric Name | Metric Key | Description |
| --- | --- | --- |
| Storage Load | com.dynatrace.extension.prometheus.azure\_cassandra\_storage\_load | Size, in bytes, of the on-disk data size this node manages. |
| Storage Exceptions | com.dynatrace.extension.prometheus.azure\_cassandra\_storage\_exceptions.count | Number of internal exceptions caught. In normal operation, this should be zero. |
| Commit Log Pending Tasks | com.dynatrace.extension.prometheus.azure\_cassandra\_commit\_log\_pending\_tasks | Number of commit log messages written but yet to be fsync'd. |
| Commit Log Completed Tasks Total | com.dynatrace.extension.prometheus.azure\_cassandra\_commit\_log\_completed\_tasks\_total.count | Total number of commit log messages written since start/restart. |
| Buffer Pool Size | com.dynatrace.extension.prometheus.azure\_cassandra\_buffer\_pool\_size | Size, in bytes, of the managed buffer pool. |
| Buffer Pool Misses Total | com.dynatrace.extension.prometheus.azure\_cassandra\_buffer\_pool\_misses\_total.count | The number of misses in the pool. The higher this is, the more allocations incurred. |
| Client Connected Native Clients | com.dynatrace.extension.prometheus.azure\_cassandra\_client\_connected\_native\_clients | Number of clients connected to this node's native protocol server. |
| Client Auth Failure Total | com.dynatrace.extension.prometheus.azure\_cassandra\_client\_auth\_failure\_total.count | Number of clients who experience authentication failures. |
| Client Auth Success Total | com.dynatrace.extension.prometheus.azure\_cassandra\_client\_auth\_success\_total.count | Number of clients who successfully authenticate. |
| Storage Total Hints Total | com.dynatrace.extension.prometheus.azure\_cassandra\_storage\_total\_hints\_total.count | Number of hint messages written to this node since start/restart. Includes one entry for each host to be hinted per hint. |
| CQL Prepared Statements Executed Total | com.dynatrace.extension.prometheus.azure\_cassandra\_cql\_prepared\_statements\_executed\_total.count | Number of prepared statements executed. |
| CQL Regular Statements Executed Total | com.dynatrace.extension.prometheus.azure\_cassandra\_cql\_regular\_statements\_executed\_total.count | Number of non-prepared statements executed. |
| Dropped Messages Total | com.dynatrace.extension.prometheus.azure\_cassandra\_dropped\_messages\_total.count | Number of dropped messages. |
| JVM GC Count | com.dynatrace.extension.prometheus.azure\_cassandra\_jvm\_gc\_count.count | Total number of collections that have occurred. |
| JVM GC Time | com.dynatrace.extension.prometheus.azure\_cassandra\_jvm\_gc\_time.count | Approximate accumulated collection elapsed time in milliseconds. |
| JVM Memory Used | com.dynatrace.extension.prometheus.azure\_cassandra\_jvm\_memory\_used | Amount of used memory in bytes. |
| JVM Memory Usage | func:com.dynatrace.extension.prometheus.azure\_cassandra\_jvm\_memory\_usage | Ratio of used memory to maximum memory. |
| Thread Pools Active Tasks | com.dynatrace.extension.prometheus.azure\_cassandra\_thread\_pools\_active\_tasks | Number of tasks being actively worked on by this pool. |
| Thread Pools Total Blocked Tasks Total | com.dynatrace.extension.prometheus.azure\_cassandra\_thread\_pools\_total\_blocked\_tasks\_total.count | Number of tasks that were blocked due to queue saturation. |
| Thread Pools Completed Tasks | com.dynatrace.extension.prometheus.azure\_cassandra\_thread\_pools\_completed\_tasks | Number of tasks completed. |
| Client Request Latency Total | com.dynatrace.extension.prometheus.azure\_cassandra\_client\_request\_latency\_total.count | Latency of client requests. |
| Client Request Failures Total | com.dynatrace.extension.prometheus.azure\_cassandra\_client\_request\_failures\_total.count | Number of transaction failures encountered. |
| Client Request Unavailables Total | com.dynatrace.extension.prometheus.azure\_cassandra\_client\_request\_unavailables\_total.count | Number of unavailable exceptions encountered. |
| Cache Hit Rate | func:com.dynatrace.extension.prometheus.azure\_cassandra\_cache\_hit\_rate | All-time cache hit rate. |
| Cache Capacity | com.dynatrace.extension.prometheus.azure\_cassandra\_cache\_capacity | Cache capacity in bytes. |
| Cache Misses Total | com.dynatrace.extension.prometheus.azure\_cassandra\_cache\_misses\_total.count | Total number of cache misses. |
| Cache Size | com.dynatrace.extension.prometheus.azure\_cassandra\_cache\_size | Total size of occupied cache, in bytes. |

### Keyspace metrics



| Metric Name | Metric Key | Description |
| --- | --- | --- |
| Keyspace All Memtables Live Data Size | com.dynatrace.extension.prometheus.azure\_cassandra\_keyspace\_all\_memtables\_live\_data\_size | Total amount of live data stored in the memtables (2i and pending flush memtables included) that resides off-heap, excluding any data structure overhead. |
| Keyspace Bloom Filter Disk Space Used | com.dynatrace.extension.prometheus.azure\_cassandra\_keyspace\_bloom\_filter\_disk\_space\_used | Disk space used by bloom filter (in bytes). |
| Keyspace Live Disk Space Used | com.dynatrace.extension.prometheus.azure\_cassandra\_keyspace\_live\_disk\_space\_used | Disk space used by SSTables belonging to this table (in bytes). |
| Keyspace Memtable Columns Count | com.dynatrace.extension.prometheus.azure\_cassandra\_keyspace\_memtable\_columns\_count.gauge | Total number of columns present in the memtable. |
| Keyspace Memtable Live Data Size | com.dynatrace.extension.prometheus.azure\_cassandra\_keyspace\_memtable\_live\_data\_size | Total amount of live data stored in the memtable, excluding any data structure overhead. |
| Keyspace Memtable Switch Count | com.dynatrace.extension.prometheus.azure\_cassandra\_keyspace\_memtable\_switch\_count.gauge | Number of times that flush has resulted in the memtable being switched out. |
| Keyspace Pending Compaction | com.dynatrace.extension.prometheus.azure\_cassandra\_keyspace\_pending\_compaction | Estimated number of compactions remaining to perform. |
| Keyspace Pending Flushes | com.dynatrace.extension.prometheus.azure\_cassandra\_keyspace\_pending\_flushes | Estimated number of flush tasks pending for this table. |
| Keyspace Read Total Latency Total | com.dynatrace.extension.prometheus.azure\_cassandra\_keyspace\_read\_total\_latency\_total.count | Read latency. |
| Keyspace Total Disk Space Used | com.dynatrace.extension.prometheus.azure\_cassandra\_keyspace\_total\_disk\_space\_used | Total disk space used by SSTables belonging to this table, including obsolete ones waiting for GC. |
| Keyspace Write Total Latency Total | com.dynatrace.extension.prometheus.azure\_cassandra\_keyspace\_write\_total\_latency\_total.count | Write Latency. |

### Table metrics

| Metric Name | Metric Key | Description |
| --- | --- | --- |
| Table Bloom Filter Disk Space Used | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_bloom\_filter\_disk\_space\_used | Disk space used by bloom filter (in bytes). |
| Table Bloom Filter False Positives | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_bloom\_filter\_false\_positives | Number of false positives on table's bloom filter. |
| Table Bloom Filter False Ratio | func:com.dynatrace.extension.prometheus.azure\_cassandra\_table\_bloom\_filter\_false\_ratio | False positive ratio of table's bloom filter. |
| Table Bytes Flushed Total | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_bytes\_flushed\_total.count | Total number of bytes flushed since server start/restart. |
| Table Compaction Bytes Written Total | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_compaction\_bytes\_written\_total.count | Total number of bytes compacted since server start/restart. |
| Table Compression Ratio | func:com.dynatrace.extension.prometheus.azure\_cassandra\_table\_compression\_ratio | Current compression ratio for all SSTables. |
| Table Dropped Mutations Total | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_dropped\_mutations\_total.count | Number of dropped mutations on this table. |
| Table Estimated Partition Count | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_estimated\_partition\_count.gauge | Approximate number of keys in table. |
| Table Key Cache Hit Rate | func:com.dynatrace.extension.prometheus.azure\_cassandra\_table\_key\_cache\_hit\_rate | Key cache hit rate for this table. |
| Table Live Disk Space Used Total | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_live\_disk\_space\_used\_total | Disk space used by SSTables belonging to this table (in bytes). |
| Table Live SSTable Count | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_live\_ss\_table\_count.gauge | Number of SSTables on disk for this table. |
| Table Memtable Columns Count | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_memtable\_columns\_count.gauge | Total number of columns present in the memtable. |
| Table Memtable Live Data Size | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_memtable\_live\_data\_size | Total amount of live data stored in the memtable, excluding any data structure overhead. |
| Table Memtable Switch Count Total | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_memtable\_switch\_count\_total.count | Number of times that flush has resulted in the memtable being switched out. |
| Table Pending Compactions | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_pending\_compactions | Estimate of number of pending compactions for this table. |
| Table Pending Flushes Total | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_pending\_flushes\_total.count | Estimate of number of pending flushes for this table. |
| Table Read Total Latency Total | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_read\_total\_latency\_total.count | Read latency for this table. |
| Table Row Cache Hit Total | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_row\_cache\_hit\_total.count | Number of table row cache hits. |
| Table Row Cache Miss Total | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_row\_cache\_miss\_total.count | Number of table row cache misses. |
| Table Total Disk Space Used Total | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_total\_disk\_space\_used\_total | Total disk space used by SSTables belonging to this table, including obsolete ones waiting to for GC. |
| Table Write Total Latency Total | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_write\_total\_latency\_total.count | Write latency for this table. |