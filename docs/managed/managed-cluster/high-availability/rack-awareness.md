---
title: Rack-aware deployment
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability/rack-awareness
---

# Rack-aware deployment

# Rack-aware deployment

* Explanation
* 3-min read
* Updated on Jun 16, 2026

In a standard high-availability Dynatrace Managed deployment, you are protected against data loss if one node fails in either small or large deployment.

Dynatrace Managed rack-aware deployment allows you to group Managed Cluster nodes into three fault domains (racks). A rack-aware deployment is resilient to an outage of all nodes in a rack.

## Prerequisites

Use rack awareness only if:

* The final number of racks is three, corresponding to the replication factor of Dynatrace data storage.
* Racks reflect the underlying physical deployment location of nodes.
* Racks are in the same low-latency network. Typically, this means the same local area network. If racks are in separate sites connected over a wide area network, network latency between sites need to stay below 10 ms.

Otherwise, you may lose data and have issues with Managed Cluster availability.

## Rack-aware deployment

Rack-aware deployment ensures that no replica is stored redundantly inside a single rack, so replicas are spread across all racks. In case one rack goes down, the other two full replicas are available, ensuring data consistency and availability. For example, in the deployment below, the Managed Cluster can handle up to three node failures in a rack before data loss.

![Large rack-aware Managed Cluster with no data loss](https://cdn.bfldr.com/B686QPH3/as/ngjgbptj3nb5jm7g7pqxf23/Premium_high_availability_rack_aware_Managed_deployment_with_no_data_loss-Light_Mode?auto=webp&format=png&position=1)

Large rack-aware Managed Cluster with no data loss

In a standard Dynatrace Managed high availability deployment, you need at least three Managed Cluster nodes to prevent data loss.
Similarly, in rack-aware deployments, you must have three racks (fault domains) to prevent data loss. In an event where the rack fails, the surviving two racks maintain the data. Given that the rack contains at least three nodes, in rack-aware deployments, you can afford a failure of the entire rack and still maintain data integrity.

The same concept applies to Premium High Availability (PHA) Managed deployments. Using rack-aware Managed Cluster deployments in separate data centers increases your resilience to data loss.

![Diagram - Premium High Availability Managed deployment with no data loss](https://dt-cdn.net/images/4man-ha-no-data-loss-54863cd646.svg)

Diagram - Premium High Availability Managed deployment with no data loss

PHA Managed deployment.

![Premium High Availability rack-aware Managed deployment with no data loss](https://cdn.bfldr.com/B686QPH3/as/ngjgbptj3nb5jm7g7pqxf23/Premium_high_availability_rack_aware_Managed_deployment_with_no_data_loss-Light_Mode?auto=webp&format=png&position=1)

Premium High Availability rack-aware Managed deployment with no data loss

PHA rack-aware Managed deployment.

For the ultimate high availability and redundancy, use the PHA deployment that is rack-aware.

To create a rack-aware deployment during the initial Managed deployment, use the installation parameters to indicate the data center and the rack to which to add the node. See [Install a Managed Cluster](/managed/managed-cluster/installation/install-managed-cluster "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration.") and [Customize installation for Dynatrace Managed](/managed/managed-cluster/installation/customize-managed-cluster-install#install-managed-cluster "Use command line parameters to customize or automate a Managed Cluster installation, with options for datastores, system users, and SSL certificates.") for example:

```
dynatrace-managed.sh --rack-name az-1 --rack-dc datacenter1
```

## Convert to rack-aware

Use either the Cluster expansion or Cluster restore method to convert the existing Managed deployment.

### Cluster expansion (no Managed Cluster downtime)

You can scale nodes vertically in two locations, so they can handle additional load when you terminate the third location, and reinstall with rack-aware settings. See [Rack-aware conversion using replication](/managed/managed-cluster/high-availability/rack-aware-replication "Learn how to convert a Dynatrace Managed Cluster to a rack-aware deployment using the replication method, including preparation and node migration steps.").

Metric storage size

If your current metric storage (Cassandra database) per node is more than 1 TB, use the cluster restore method. While the cluster expansion method will work, the Cassandra bootstrapping required in this method takes an unreasonably long time.

### Cluster restore (Managed Cluster downtime during the restore)

You can backup and restore with rack-aware settings. See [Rack-aware conversion using restore](/managed/managed-cluster/high-availability/rack-aware-restore "Learn how to convert a Dynatrace Managed Cluster to rack-aware topology using the backup and restore method, including preparation and installer parameters.").

## Related topics

* [Rack-aware conversion using replication](/managed/managed-cluster/high-availability/rack-aware-replication "Learn how to convert a Dynatrace Managed Cluster to a rack-aware deployment using the replication method, including preparation and node migration steps.")
* [Rack-aware conversion using restore](/managed/managed-cluster/high-availability/rack-aware-restore "Learn how to convert a Dynatrace Managed Cluster to rack-aware topology using the backup and restore method, including preparation and installer parameters.")