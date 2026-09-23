---
title: Rack awareness
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability/rack-awareness
---

# Rack awareness

# Rack awareness

* Explanation
* 3-min read
* Updated on Sep 18, 2026

Dynatrace Managed rack awareness groups Cluster nodes into three fault domains (racks). A rack-aware deployment is resilient to an outage of all nodes in a rack. You can make a single Managed Cluster rack-aware, or apply rack awareness to each data center in a Premium High Availability (PHA) deployment.

## How rack awareness works

Rack awareness ensures that no replica is stored redundantly inside a single rack, so replicas are spread across all racks. If one rack goes down, the other two full replicas remain available, which keeps data consistent and accessible. For example, in the deployment below, the Managed Cluster survives the loss of all three nodes in Rack 1 without data loss.

| Data center | Rack | Nodes | Status |
| --- | --- | --- | --- |
| Data center 1 | Rack 1 | Node 1, Node 2, Node 3 | Down |
| Data center 1 | Rack 2 | Node 4, Node 5, Node 6 | Up |
| Data center 1 | Rack 3 | Node 7, Node 8, Node 9 | Up |

A standard Dynatrace Managed high-availability deployment needs at least three Cluster nodes to prevent data loss. A rack-aware deployment needs three racks (fault domains) for the same reason: if one rack fails, the surviving two racks still hold a complete copy of the data. Because each rack holds at least three nodes, a rack-aware deployment tolerates the loss of an entire rack.

## Rack awareness in a PHA deployment

The same concept applies to PHA deployments. Rack-aware Managed Clusters in separate data centers increase your resilience to data loss.

### PHA deployment without rack awareness

Without rack awareness, the nodes in a data center aren't grouped into fault domains. In the following example, Data center 1 is offline and one node in Data center 2 is also down. The remaining eight nodes in Data center 2 still hold a full replica set, so no data is lost.

| Data center | Nodes | Status |
| --- | --- | --- |
| Data center 1 | Node 1 to Node 9 | Down |
| Data center 2 | Node 1 | Down |
| Data center 2 | Node 2 to Node 9 | Up |

### PHA deployment with rack awareness

With rack awareness, the same PHA deployment tolerates the loss of a whole rack in the surviving data center. In the following example, Data center 1 is offline and Rack 1 in Data center 2 also fails. The two remaining racks in Data center 2 each hold a complete replica, so no data is lost.

| Data center | Rack | Nodes | Status |
| --- | --- | --- | --- |
| Data center 1 | Rack 1 | Node 1, Node 2, Node 3 | Down |
| Data center 1 | Rack 2 | Node 4, Node 5, Node 6 | Down |
| Data center 1 | Rack 3 | Node 7, Node 8, Node 9 | Down |
| Data center 2 | Rack 1 | Node 1, Node 2, Node 3 | Down |
| Data center 2 | Rack 2 | Node 4, Node 5, Node 6 | Up |
| Data center 2 | Rack 3 | Node 7, Node 8, Node 9 | Up |

For the highest resilience, make every data center in a PHA deployment rack-aware.

## Rack awareness requirements

Use rack awareness only if:

* The final number of racks is three, corresponding to the replication factor of Dynatrace data storage.
* Racks reflect the underlying physical deployment location of nodes.
* Racks are in the same low-latency network. Typically, this means the same local area network. If racks are in separate sites connected over a wide area network, network latency between sites needs to stay below 10 ms.
* Each rack holds at least three nodes. Dynatrace doesn't enforce this, but fewer nodes per rack reduce the protection rack awareness provides.

Otherwise, you might lose data and encounter Managed Cluster availability issues.

## Rack awareness methods

A deployment becomes rack-aware either at installation time or through a conversion. During the initial Managed installation, the `--rack-dc` and `--rack-name` parameters assign each node to a data center and a rack. For the parameter descriptions, go to [Customize installation for Dynatrace Managed](/managed/managed-cluster/installation/customize-managed-cluster-install#install-managed-cluster "Use command line parameters to customize or automate a Managed Cluster installation, with options for datastores, system users, and SSL certificates.").

An existing Managed Cluster converts to rack-aware in one of two ways, and the size of your metric storage decides which one fits:

* [Rack-aware conversion using replication](/managed/managed-cluster/high-availability/rack-aware-replication "Learn how to convert a Dynatrace Managed Cluster to a rack-aware deployment using the replication method, including preparation and node migration steps.") suits small Managed Clusters where one node can contain a full replica, and it doesn't cause Managed Cluster downtime.
* [Rack-aware conversion using restore](/managed/managed-cluster/high-availability/rack-aware-restore "Learn how to convert a Managed Cluster to a rack-aware deployment using the restore method, including preparation and installer parameters.") suits a metric storage (Cassandra database) per node of more than 1 TB. The replication method also works at that size, but the required Cassandra bootstrapping takes considerably longer.

To run rack awareness together with Premium High Availability, go to [Combine Premium High Availability with rack awareness](/managed/managed-cluster/high-availability/pha-rack-aware "Combine Premium High Availability with rack awareness so each data center holds three racks and the cluster spans six independent fault domains.").

## Related topics

* [Convert a Managed Cluster to a rack-aware deployment using replication](/managed/managed-cluster/high-availability/rack-aware-replication "Learn how to convert a Dynatrace Managed Cluster to a rack-aware deployment using the replication method, including preparation and node migration steps.")
* [Convert a Managed Cluster to a rack-aware deployment using restore](/managed/managed-cluster/high-availability/rack-aware-restore "Learn how to convert a Managed Cluster to a rack-aware deployment using the restore method, including preparation and installer parameters.")
* [Customize Managed Cluster installation](/managed/managed-cluster/installation/customize-managed-cluster-install "Use command line parameters to customize or automate a Managed Cluster installation, with options for datastores, system users, and SSL certificates.")
* [Single-cluster high availability](/managed/managed-cluster/high-availability/single-cluster-high-availability "Understand how a single Managed Cluster tolerates node failures through data replication, node redundancy, and automatic OneAgent traffic failover.")
* [Multi-data center high availability](/managed/managed-cluster/high-availability/multi-data-centers "Understand how Dynatrace Managed Premium High Availability provides failover, data resilience, and data routing across data centers.")
* [Combine Premium High Availability with rack awareness](/managed/managed-cluster/high-availability/pha-rack-aware "Combine Premium High Availability with rack awareness so each data center holds three racks and the cluster spans six independent fault domains.")