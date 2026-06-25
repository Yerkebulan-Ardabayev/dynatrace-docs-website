---
title: Rack-aware Managed deployment
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability/rack-awareness
scraped: 2026-05-12T11:53:27.988786
---

# Rack-aware Managed deployment

# Rack-aware Managed deployment

* Updated on May 04, 2026

In a standard high-availability Dynatrace Managed deployment, you're protected against data loss if one node fails in either small or large deployment.

Dynatrace Managed rack-aware deployment allows you to group cluster nodes into three fault domains (racks). Such deployment is resilient to an outage of all nodes in a rack.

## Prerequisites

You should use rack awareness only if:

* The final number of racks is three, corresponding to the replication factor of Dynatrace data storage.
* Racks reflect the underlying physical deployment location of nodes.

Otherwise, you may lose data and have issues with cluster availability.

## Rack-aware deployment

Rack-aware deployment ensures that no replica is stored redundantly inside a singular rack, so that replicas are spread around through racks. In case one rack goes down, the other two full replicas are available, ensuring data consistency and availability. For example, in the deployment below, the Dynatrace Managed cluster can handle up to three node failures in a rack before data loss.

![Large Managed rack-aware cluster no data loss](https://dt-cdn.net/images/3l-ra-man-cluster-no-data-loss-4eb930ca7f.svg)

Large Managed rack-aware cluster no data loss

In a standard Dynatrace Managed high availability deployment, you need at least three cluster nodes in order to prevent data loss.
Similarly, in rack-aware deployments, you must have three racks (fault domains) to prevent data loss. In an event where the rack fails, the surviving two racks maintain the data. Given that the rack contains at least three nodes, in rack-aware deployments, you can afford a failure of the entire rack and still maintain data integrity.

The same concept applies to Premium High Availability Managed deployments. Using rack-aware Managed clusters in separate data centers increases your resilience to data loss.

![Diagram - Premium high availability Managed deployment with no data loss](https://dt-cdn.net/images/4man-ha-no-data-loss-54863cd646.svg)

Diagram - Premium high availability Managed deployment with no data loss

Premium high availability Managed deployment.

![Premium high availability rack-aware Managed deployment with no data loss](https://dt-cdn.net/images/5man-ha-ra-no-data-loss-5f9393973b.svg)

Premium high availability rack-aware Managed deployment with no data loss

Premium high availability rack-aware Managed deployment.

For the ultimate high availability and redundancy, use the Premium high availably deployment that is rack-aware.

To create a rack-aware deployment during the initial Managed deployment, use the installation parameters to indicate the data center and the rack to which to add the node. See [Set up a cluster](/managed/managed-cluster/installation/install-managed-cluster "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration.") and [Customize installation for Dynatrace Managed](/managed/managed-cluster/installation/customize-managed-cluster-install#install-managed-cluster "Use command line parameters to customize or automate a Managed Cluster installation, with options for datastores, system users, and SSL certificates.") for example:

```
dynatrace-managed.sh --rack-name az-1 --rack-dc datacenter1
```

## Convert to rack-aware

Use either the Cluster expansion or Cluster restore method to convert the existing Managed deployment.

### Cluster expansion (no cluster down time)

You can scale nodes vertically in two locations, so they can handle additional load when you terminate the third location, and reinstall with rack-aware settings. See [Rack-aware conversion using replication](/managed/managed-cluster/high-availability/rack-aware-conversion-using-replication "Learn how to download and convert Dynatrace Managed cluster to rack-aware using the expansion method.").

Metric storage size

If your current metric storage (Cassandra database) per node is more than 1TB, use the cluster restore method. While the cluster expansion method will work, the Cassandra bootstrapping required in this method may take unreasonably long time.

### Cluster restore (cluster down time during the restore)

You can backup and restore with rack-aware settings. See [Rack-aware conversion using restore](/managed/managed-cluster/high-availability/rack-aware-conversion-using-restore "Learn how to download and convert a Dynatrace Managed cluster to rack-aware using the restore method.").

## Related topics

* [Rack-aware conversion using replication](/managed/managed-cluster/high-availability/rack-aware-conversion-using-replication "Learn how to download and convert Dynatrace Managed cluster to rack-aware using the expansion method.")
* [Rack-aware conversion using restore](/managed/managed-cluster/high-availability/rack-aware-conversion-using-restore "Learn how to download and convert a Dynatrace Managed cluster to rack-aware using the restore method.")