---
title: Rack-aware deployment
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability/rack-awareness
---

# Rack-aware deployment

# Rack-aware deployment

* Explanation
* 3-min read
* Updated on Jul 07, 2026

Dynatrace Managed rack-aware deployment allows you to group Managed Cluster nodes into three fault domains (racks). A rack-aware deployment is resilient to an outage of all nodes in a rack. You can make a single Managed Cluster rack-aware, or apply rack awareness to each data center in a Premium High Availability (PHA) deployment.

## How rack-aware deployment works

Rack-aware deployment ensures that no replica is stored redundantly inside a single rack, so replicas are spread across all racks. If one rack goes down, the other two full replicas are available, ensuring data consistency and availability. For example, in the deployment below, the Managed Cluster can handle up to three node failures in a rack before data loss.

![Large rack-aware Managed Cluster with no data loss](https://cdn.bfldr.com/B686QPH3/as/ngjgbptj3nb5jm7g7pqxf23/Premium_high_availability_rack_aware_Managed_deployment_with_no_data_loss-Light_Mode?auto=webp&format=png&position=1)

Large rack-aware Managed Cluster with no data loss

In a standard Dynatrace Managed high availability deployment, you need at least three Managed Cluster nodes to prevent data loss. Similarly, in rack-aware deployments, you must have three racks (fault domains) to prevent data loss. If a rack fails, the surviving two racks maintain the data. Given that the rack contains at least three nodes, in rack-aware deployments, you can afford a failure of the entire rack and still maintain data integrity.

The same concept applies to PHA Managed deployments. Using rack-aware Managed Cluster deployments in separate data centers increases your resilience to data loss.

![Premium High Availability Managed deployment with no data loss](https://cdn.bfldr.com/B686QPH3/as/kq99pm9bftxrgfbtp3s4rg6p/Premium_high_availability_Managed_deployment_with_no_data_loss-Light_Mode?auto=webp&format=png&position=1)

Premium High Availability Managed deployment with no data loss

![Premium High Availability rack-aware Managed deployment with no data loss](https://cdn.bfldr.com/B686QPH3/as/ngjgbptj3nb5jm7g7pqxf23/Premium_high_availability_rack_aware_Managed_deployment_with_no_data_loss-Light_Mode?auto=webp&format=png&position=1)

Premium High Availability rack-aware Managed deployment with no data loss

For the ultimate high availability and redundancy, use the PHA deployment that's rack-aware.

## Prerequisites

Use rack awareness only if:

* The final number of racks is three, corresponding to the replication factor of Dynatrace data storage.
* Racks reflect the underlying physical deployment location of nodes.
* Racks are in the same low-latency network. Typically, this means the same local area network. If racks are in separate sites connected over a wide area network, network latency between sites needs to stay below 10 ms.

Otherwise, you may lose data and have issues with Managed Cluster availability.

## Set up rack-aware deployment

To create a rack-aware deployment during the initial Managed deployment, use the installation parameters to indicate the data center and the rack for each node. See [Install a Managed Cluster](/managed/managed-cluster/installation/install-managed-cluster "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration.") and [Customize installation for Dynatrace Managed](/managed/managed-cluster/installation/customize-managed-cluster-install#install-managed-cluster "Use command line parameters to customize or automate a Managed Cluster installation, with options for datastores, system users, and SSL certificates."). For example:

```
dynatrace-managed.sh --rack-name az-1 --rack-dc datacenter1
```

To convert an existing Managed Cluster to rack-aware, choose a method based on your metric storage size:

* Use the [rack-aware conversion using replication](/managed/managed-cluster/high-availability/rack-aware-replication "Learn how to convert a Dynatrace Managed Cluster to a rack-aware deployment using the replication method, including preparation and node migration steps.") method for small Managed Clusters where one node can contain a full replica. This method doesn't cause Managed Cluster downtime.
* Use the [rack-aware conversion using restore](/managed/managed-cluster/high-availability/rack-aware-restore "Learn how to convert a Dynatrace Managed Cluster to rack-aware topology using the backup and restore method, including preparation and installer parameters.") method when your metric storage (Cassandra database) per node is more than 1 TB. The cluster expansion method also works, but the required Cassandra bootstrapping takes an unreasonably long time.

## Related topics

* [Rack-aware conversion using replication](/managed/managed-cluster/high-availability/rack-aware-replication "Learn how to convert a Dynatrace Managed Cluster to a rack-aware deployment using the replication method, including preparation and node migration steps.")
* [Rack-aware conversion using restore](/managed/managed-cluster/high-availability/rack-aware-restore "Learn how to convert a Dynatrace Managed Cluster to rack-aware topology using the backup and restore method, including preparation and installer parameters.")