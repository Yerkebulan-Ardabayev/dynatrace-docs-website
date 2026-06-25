---
title: Estimate cluster backup size
source: https://docs.dynatrace.com/managed/managed-cluster/operation/estimating-cluster-backup-size
scraped: 2026-05-12T11:53:13.467444
---

# Estimate cluster backup size

# Estimate cluster backup size

* Published Aug 05, 2019

Follow the instructions below to estimate the cluster backup size for metrics storage and Elasticsearch storage. The overall size of a cluster backup can be roughly estimated as the sum of your backup estimates for metrics storage and Elasticsearch storage.

### General formula

1. Estimate the metrics storage backup size.

   Typically, it's 20% of the sum of the metrics storage on all nodes. The number of nodes doesn't affect the formula.

   Available storage space for backup

   The current metrics storage backup is retained until the next backup completes and a new backup is created. Until the first backup is removed, the storage space required by the metrics storage backup therefore is double the size of your actual backup. For this reason, we recommend that you double the estimated space you need for metrics storage backup.
2. Estimate the Elasticsearch storage backup size.

   The estimated required backup size for Elasticsearch is based on the ElasticSearch storage size. Typically, it's less than the sum of the ElasticSearch storage on all nodes. While Elasticsearch backup doesn't contain data replicas, because of incremental snapshots, we use total storage for the estimation.
3. Estimate the cluster backup size.

   Based on the preceding estimates, calculate the estimated backup size as 20% of metrics storage + Elasticsearch storage.

### Example estimate

For example, assume that you want to estimate the backup size for a three-node cluster:

1. Calculate the metrics storage for the whole cluster.  
   Check the size of metrics storage on disk on **each node**. The size should vary only slightly between nodes.

   ```
   du -sh /var/opt/dynatrace-managed/cassandra/



   885GB
   ```

   In our example, the cluster has three nodes, and one node has 885 GB of metrics storage, so we can estimate the metrics storage as: `3 * 885 GB = 2.6 TB`.
2. Calculate the Elasticsearch storage for the whole cluster.  
   Check the size of Elasticsearch storage on disk on **each node**. The size should vary only slightly between nodes.

   ```
   du -sh /var/opt/dynatrace-managed/elasticsearch/



   1.5TB
   ```

   In our example, the cluster has three nodes, and one node has 1.5 TB of Elasticsearch storage, so we can estimate the Elasticsearch storage as: `3 * 1.5 TB = 4.5 TB`.
3. Now that we have estimates for metrics storage and Elasticsearch, we can estimate the backup size as the 20% of the metrics storage + Elasticsearch storage estimate estimate: `(2.6 TB * 0.2) + 4.5 TB = 5.02 TB`.

   Single **backup size** was estimated to 5.02 TB. To estimate the **minimum size you should provision** for this backup, you need to double the metric storage backup. In total, it is `4.5 TB + ((2.6 TB * 0.2) * 2) = 5.54 TB`.

Estimate accuracy

This estimate won't be accurate if it was calculated on a new cluster that just started storing data. As the storage on disk grows, so will the size of the backup.

### Configuration-only backup

Takes up to 10% of metrics storage instead of 20% (it is 50% less of metrics storage).

### Excluding user sessions

In highly intensive RUM environments (50k user sessions per minute), user sessions might take up to 99% of total Elasticsearch storage. Therefore, excluding them might eliminate Elasticsearch backup estimation from the overall formula. In other environments it's hard to estimate the reduction of backup size. You can contact a Dynatrace product expert via live chat within your Dynatrace environment for help.