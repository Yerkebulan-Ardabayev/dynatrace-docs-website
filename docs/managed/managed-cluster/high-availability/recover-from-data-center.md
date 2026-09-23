---
title: Recover from another data center
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability/recover-from-data-center
---

# Recover from another data center

# Recover from another data center

* How-to guide
* 1-min read
* Updated on Sep 11, 2026

To recover a failed data center from another data center, follow the steps below.

## Prerequisites

Outages of one data center (DC) that last up to 72 hours don't require this disaster recovery procedure. When the inaccessible DC becomes available again, Premium High Availability automatically repairs the affected DC and restores Managed Cluster operations. For details, go to [Multi-data center failover](/managed/managed-cluster/high-availability/failover "The Premium High Availability failover mechanism detects node outages exceeding 15 minutes and transfers server responsibility to a healthy data center.").

To avoid data inconsistency while a DC is unavailable, shut down the Dynatrace Server service on all Cluster nodes in the affected DC. Start the services only when network connectivity is stable again.

After 72 hours, Mission Control marks the Managed Cluster as not repaired after failover. Such a Managed Cluster is not reliable. As a result, you must restore or recreate the failed DC from either an operational DC or a backup.

## Recovery procedure

1. Remove unavailable nodes from the Managed Cluster.
2. Update the surviving DC configuration.
3. Reinstall nodes in the recovered DC.
4. Replicate Cassandra to the recovered DC.
5. Replicate Elasticsearch to the recovered DC.
6. Recreate the Dynatrace Server, start ActiveGate, and start NGINX in the recovered DC.
7. Enable the recovered DC.

For the detailed procedure, go to [Rebuild data center](/managed/managed-cluster/high-availability/rebuild-data-center "Learn how to rebuild a lost data center in a Dynatrace Managed Premium High Availability deployment and restore replication across both data centers.").

## Related topics

* [Multi-data center high availability](/managed/managed-cluster/high-availability/multi-data-centers "Understand how Dynatrace Managed Premium High Availability provides failover, data resilience, and data routing across data centers.")
* [Multi-data center failover](/managed/managed-cluster/high-availability/failover "The Premium High Availability failover mechanism detects node outages exceeding 15 minutes and transfers server responsibility to a healthy data center.")