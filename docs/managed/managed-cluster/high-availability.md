---
title: Premium High Availability
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability
---

# Premium High Availability

# Premium High Availability

* 1-min read
* Updated on Jun 15, 2026

Review Dynatrace Managed high availability options and choose between Premium High Availability across data centers and rack-aware deployment across fault domains. Use the following pages to compare topologies, add data centers, convert deployments, and recover from outages.

## Premium High Availability

[### Multi-data centers

Understand how Premium High Availability (PHA) uses redundancy, hardware placement, capacity planning, data replication, and automatic failover across data centers.](/managed/managed-cluster/high-availability/multi-data-centers "Understand how Dynatrace Managed Premium High Availability provides failover, data resilience, and data routing across data centers.")[### Add a data center

Replicate Managed Cluster nodes across two data centers and prepare Cassandra, Elasticsearch, and server components for PHA.](/managed/managed-cluster/high-availability/add-data-center "Learn how to replicate Managed Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")[### Multi-data center failover

Review how PHA detects Elasticsearch and Cassandra node outages, routes failover decisions, and restores service after recovery.](/managed/managed-cluster/high-availability/failover "Learn how the Premium High Availability multi-data center failover mechanism detects node outages and transfers responsibility to a healthy data center.")[### Recover a data center from another data center

Recover a data center in a PHA deployment by using another data center as the recovery source.](/managed/managed-cluster/high-availability/recover-from-data-center "Recover a data center when Premium High Availability can't repair it within 72 hours by restoring or recreating it from another data center.")[### Recover a data center from backup

Recover a lost data center from backup and restore the data center topology in a multi-data center deployment.](/managed/managed-cluster/high-availability/recover-from-backup "Learn how to restore a Premium High Availability data center from backup in a Dynatrace Managed multi-DC deployment after a data center loss.")[### Rebuild a data center

Rebuild a lost data center, reinstall nodes, migrate data stores, and restore replication across both data centers.](/managed/managed-cluster/high-availability/rebuild-data-center "Learn how to rebuild a lost data center in a Dynatrace Managed Premium High Availability deployment and restore replication across both data centers.")

## Rack-aware deployment

[### Rack-aware deployment

Learn how rack-aware deployments distribute nodes across fault domains, reduce data loss risk, and complement PHA topologies.](/managed/managed-cluster/high-availability/rack-awareness "Learn how rack-aware deployment groups Dynatrace Managed Cluster nodes into three fault domains to ensure resilience against a full rack outage and data loss.")[### Rack-aware conversion using replication

Convert a Managed Cluster to a rack-aware deployment using the expansion method when you can add capacity before migration.](/managed/managed-cluster/high-availability/rack-aware-replication "Learn how to convert a Dynatrace Managed Cluster to a rack-aware deployment using the replication method, including preparation and node migration steps.")[### Rack-aware conversion using restore

Convert a Managed Cluster to a rack-aware deployment using the restore method when you need to rebuild from restored data.](/managed/managed-cluster/high-availability/rack-aware-restore "Learn how to convert a Dynatrace Managed Cluster to rack-aware topology using the backup and restore method, including preparation and installer parameters.")