---
title: Recover from another data center
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability/recover-from-data-center
---

# Recover from another data center

# Recover from another data center

* How-to guide
* 1-min read
* Updated on Jul 07, 2026

Outages of one data center (DC) that last up to 72 hours don't require this disaster recovery procedure. When the inaccessible DC becomes available again, Premium High Availability (PHA) automatically repairs the affected DC and restores Managed Cluster operations. For details, go to [Multi-data center failover](/managed/managed-cluster/high-availability/failover "Learn how the Premium High Availability multi-data center failover mechanism detects node outages and transfers responsibility to a healthy data center.").

To avoid data inconsistency while a DC is unavailable, shut down the server service on all nodes in the affected DC. Start services only when network connectivity is stable again.

After 72 hours, Mission Control (MC) marks the Managed Cluster as not repaired after failover. Such a Managed Cluster isn't reliable. As a result, you must restore or recreate the failed DC from either an operational DC or a backup.

## Recovery procedure

To recover from another data center, complete the following steps:

1. Remove unavailable nodes from the Managed Cluster.
2. Update the surviving DC configuration.
3. Reinstall nodes in the recovered DC.
4. Replicate Cassandra to the recovered DC.
5. Replicate Elasticsearch to the recovered DC.
6. Recreate the server, start ActiveGate, and start NGINX in the recovered DC.
7. Enable the recovered DC.

For the detailed procedure, go to [Rebuild data center](/managed/managed-cluster/high-availability/rebuild-data-center "Learn how to rebuild a lost data center in a Dynatrace Managed Premium High Availability deployment and restore replication across both data centers.").