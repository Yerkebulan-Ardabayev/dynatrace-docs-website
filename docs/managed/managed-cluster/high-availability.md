---
title: High availability
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability
---

# High availability

# High availability

* 1-min read
* Updated on Jul 07, 2026

Dynatrace Managed high availability protects against different scopes of failure. A single Managed Cluster tolerates the loss of individual nodes. Premium High Availability (PHA) adds a second data center, so monitoring continues even if an entire data center fails. On top of either topology, rack-aware deployment groups nodes into fault domains, so a Managed Cluster also survives the outage of an entire rack. First choose a base topology, either a single Managed Cluster or PHA, then optionally layer on rack-aware deployment. The following pages help you compare these options, add a data center, convert an existing Managed Cluster, and recover after an outage.

## Single-cluster high availability

[### Single-cluster high availability

Learn how a single Managed Cluster tolerates node failures through data replication, node redundancy, and automatic OneAgent traffic failover.](/managed/managed-cluster/high-availability/single-cluster-high-availability "Understand how a single Dynatrace Managed Cluster tolerates node failures through data replication, node redundancy, and automatic OneAgent traffic failover.")

## Premium High Availability

[### Multi-data center high availability

Understand how Premium High Availability (PHA) uses redundancy, hardware placement, capacity planning, data replication, and automatic failover across data centers.](/managed/managed-cluster/high-availability/multi-data-centers "Understand how Dynatrace Managed Premium High Availability provides failover, data resilience, and data routing across data centers.")[### Add a data center

Replicate Managed Cluster nodes across two data centers and prepare Cassandra, Elasticsearch, and server components for PHA.](/managed/managed-cluster/high-availability/add-data-center "Learn how to replicate Managed Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")[### Multi-data center failover

Review how PHA detects Elasticsearch and Cassandra node outages, routes failover decisions, and restores service after recovery.](/managed/managed-cluster/high-availability/failover "Learn how the Premium High Availability multi-data center failover mechanism detects node outages and transfers responsibility to a healthy data center.")[### Recover a data center from another data center

Recover a data center in a PHA deployment by using another data center as the recovery source.](/managed/managed-cluster/high-availability/recover-from-data-center "Recover a data center when Premium High Availability can't repair it within 72 hours by restoring or recreating it from another data center.")[### Recover a data center from backup

Recover a lost data center from backup and restore the data center topology in a multi-data center deployment.](/managed/managed-cluster/high-availability/recover-from-backup "Learn how to restore a Premium High Availability data center from backup in a Dynatrace Managed multi-DC deployment after a data center loss.")[### Rebuild a data center

Rebuild a lost data center, reinstall nodes, migrate data stores, and restore replication across both data centers.](/managed/managed-cluster/high-availability/rebuild-data-center "Learn how to rebuild a lost data center in a Dynatrace Managed Premium High Availability deployment and restore replication across both data centers.")

## Rack-aware deployment

[### Rack-aware deployment

Learn how rack-aware deployments group nodes into fault domains to survive a rack outage, on a single Managed Cluster or a PHA deployment.](/managed/managed-cluster/high-availability/rack-awareness "Learn how rack-aware deployment groups Dynatrace Managed Cluster nodes into three fault domains to ensure resilience against a full rack outage and data loss.")[### Rack-aware conversion using replication

Convert a Managed Cluster to a rack-aware deployment using the expansion method when you can add capacity before migration.](/managed/managed-cluster/high-availability/rack-aware-replication "Learn how to convert a Dynatrace Managed Cluster to a rack-aware deployment using the replication method, including preparation and node migration steps.")[### Rack-aware conversion using restore

Convert a Managed Cluster to a rack-aware deployment using the restore method when you need to rebuild from restored data.](/managed/managed-cluster/high-availability/rack-aware-restore "Learn how to convert a Dynatrace Managed Cluster to rack-aware topology using the backup and restore method, including preparation and installer parameters.")