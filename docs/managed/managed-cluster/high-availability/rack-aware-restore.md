---
title: Convert a Managed Cluster to a rack-aware deployment using restore
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability/rack-aware-restore
---

# Convert a Managed Cluster to a rack-aware deployment using restore

# Convert a Managed Cluster to a rack-aware deployment using restore

* How-to guide
* 3-min read
* Updated on Sep 18, 2026

To convert a Managed Cluster to a rack-aware deployment using the backup and restore method, follow the steps below.

This method isn't supported on a Premium High Availability deployment, because it stops and reinstalls the whole Managed Cluster at once. See [Combine Premium High Availability with rack awareness](/managed/managed-cluster/high-availability/pha-rack-aware "Combine Premium High Availability with rack awareness so each data center holds three racks and the cluster spans six independent fault domains.") for the supported route.

The restore method is universal and works for larger Managed Clusters and more complex topology changes. However, the restoration process is time-consuming, and because backups run daily, the conversion involves some data loss. The backup doesn't include transaction storage ([distributed traces](/managed/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.")). For small Managed Clusters where one node can contain a full replica, use the [rack-aware conversion using replication](/managed/managed-cluster/high-availability/rack-aware-replication "Learn how to convert a Dynatrace Managed Cluster to a rack-aware deployment using the replication method, including preparation and node migration steps.") method instead.

![Process of converting Managed Cluster to rack-aware via backup and restore](https://cdn.bfldr.com/B686QPH3/as/spnxnjg7r477s8gb9qtctg/Rack_aware_conversion_using_restore-Light_Mode?auto=webp&format=png&position=1)

Process of converting Managed Cluster to rack-aware via backup and restore

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Prepare for the conversion**](/managed/managed-cluster/high-availability/rack-aware-restore#preparation "Learn how to convert a Managed Cluster to a rack-aware deployment using the restore method, including preparation and installer parameters.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Restore the Managed Cluster into new racks**](/managed/managed-cluster/high-availability/rack-aware-restore#restore "Learn how to convert a Managed Cluster to a rack-aware deployment using the restore method, including preparation and installer parameters.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Verify the conversion**](/managed/managed-cluster/high-availability/rack-aware-restore#verify "Learn how to convert a Managed Cluster to a rack-aware deployment using the restore method, including preparation and installer parameters.")

## Step 1 Prepare for the conversion

1. Verify that the Managed Cluster has a recent backup. See [Back up and restore a Managed Cluster](/managed/managed-cluster/operation/back-up-and-restore-a-cluster "Understand the steps and commands required to restore a Dynatrace Managed cluster.").
2. Prepare new nodes. Make sure the disk partition allocated for Cassandra storage on the new node is sufficient to contain the entire Cassandra database (with margin for compaction and new data). The disk must be at least twice the combined Cassandra storage of all existing Cluster nodes. Place Cassandra data on a separate volume to avoid disk-space issues from different data types.
3. Create your Managed Cluster inventory. You need the node IDs and the IPv4 addresses of the new machines during the restore. See [Back up and restore a Managed Cluster](/managed/managed-cluster/operation/back-up-and-restore-a-cluster "Understand the steps and commands required to restore a Dynatrace Managed cluster.").

## Step 2 Restore the Managed Cluster into new racks

1. Stop the existing Managed Cluster to prevent two Managed Clusters with the same ID from connecting to Dynatrace Mission Control.  
   See [Start/stop/restart a node](/managed/managed-cluster/operation/start-stop-restart-node "Properly shut down and restart Dynatrace Managed nodes using command line parameters.").
2. Run the Managed Cluster restore procedure ([Back up and restore a Managed Cluster](/managed/managed-cluster/operation/back-up-and-restore-a-cluster#cluster-restore "Understand the steps and commands required to restore a Dynatrace Managed cluster.")), with one modification: run the Dynatrace Managed installer on each node with the rack parameters.

   Run the installer in parallel on every node, using the following parameters:

   * `--rack-name`: rack this node belongs to
   * `--rack-dc`: data center this node belongs to
   * `--restore`: switches the installer into restore mode
   * `--cluster-ip`: IPv4 address of the node on which you run the installer
   * `--cluster-nodes`: comma-delimited list of IDs and IP addresses of all nodes in the Managed Cluster, including the one on which you run the installer, in the format `<node_id>:<node_ip>,<node_id>:<node_ip>`
   * `--seed-ip`: IPv4 address of the seed node
   * `--backup-file`: path to the backup `*.tar` file — the path combines the shared file storage mount, the Managed Cluster ID, the node ID, the backup version, and the filename, in the format  
     `<path-to-backup>/<UUID>/node_<node_id>/files/<backup_version_number>/<backup_file>`

   Backup path example

   Consider this example path:

   `/mnt/backup/bckp/c9dd47f0-87d7-445e-bbeb-26429fac06c6/node_1/files/19/backup-001.tar`

   The parts of the path are as follows:

   * `<path-to-backup>` = `/mnt/backup/bckp/`
   * `<UUID>` = `c9dd47f0-87d7-445e-bbeb-26429fac06c6`
   * `<node_id>` = `1`
   * `<backup_version_number>` = `19`

   While the backup is in progress, two backup directories might be present with different backup version numbers:

   * The directory with the lower version number contains the old backup. This directory is deleted after the backup completes.
   * The directory with the higher version number contains the backup that's in progress.

   The backup version number increments with each backup execution.

   Get the IDs and IP addresses from the inventory you created before you started. For example:

   * IP address of the node to restore: `10.176.41.168`
   * Node IDs and new IP addresses of all nodes in the Managed Cluster: `1: 10.176.41.168, 3: 10.176.41.169, 5: 10.176.41.170`

   ```
   sudo ./tmp/backup-001-dynatrace-managed-installer.sh \



   --rack-name rack2 \



   --rack-dc datacenter1 \



   --restore \



   --cluster-ip "10.176.41.168" \



   --cluster-nodes "1:10.176.41.168,3:10.176.41.169,5:10.176.41.170" \



   --seed-ip "10.176.41.169" \



   --backup-file /mnt/backup/bckp/c9dd47f0-87d7-445e-bbeb-26429fac06c6/node_1/files/19/backup-001.tar
   ```

## Step 3 Verify the conversion

The restore process places the loaded data directly in the target racks. After the conversion is complete, go to the **Deployment status** page in the Cluster Management Console and confirm that it lists the new racks:

![Cluster Management Console deployment status page of a Managed Cluster that's rack-aware](https://dt-cdn.net/images/cmcstatus-2263-58f0a8359d.png)

Cluster Management Console deployment status page of a Managed Cluster that's rack-aware

## Related topics

* [Combine Premium High Availability with rack awareness](/managed/managed-cluster/high-availability/pha-rack-aware "Combine Premium High Availability with rack awareness so each data center holds three racks and the cluster spans six independent fault domains.")