---
title: Rack-aware conversion using restore
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability/rack-aware-restore
---

# Rack-aware conversion using restore

# Rack-aware conversion using restore

* How-to guide
* 3-min read
* Updated on Jun 15, 2026

The restore method is universal and can work for larger Managed Clusters and more complex topology changes. However, the restoration process is time-consuming, and due to daily frequency of backups, there is some loss of data involved. Transaction storage ([distributed traces](/managed/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.")) isn't contained in the backup.

![Process of converting Managed Cluster to rack-aware via backup and restore](https://cdn.bfldr.com/B686QPH3/as/spnxnjg7r477s8gb9qtctg/Rack_aware_conversion_using_restore-Light_Mode?auto=webp&format=png&position=1)

Process of converting Managed Cluster to rack-aware via backup and restore

## Preparation

* Verify that the Managed Cluster has a recent backup.  
  See [Back up and restore a Managed Cluster](/managed/managed-cluster/operation/back-up-and-restore-a-cluster "Understand the steps and commands required to restore a Dynatrace Managed cluster.").
* Prepare new nodes.  
  Make sure the disk partition allocated for Cassandra storage on the new node is sufficient to contain the entire Cassandra database (with margin for compaction and new data). The disk must be at least twice the combined Cassandra storage of all existing Managed Cluster nodes. Place Cassandra data on a separate volume to avoid disk-space issues from different data types.

## Restore the Managed Cluster into new racks

To restore the Managed Cluster into new racks:

1. Stop the existing Managed Cluster to prevent two Managed Clusters with the same ID from connecting to Dynatrace Mission Control.  
   See [Start/stop/restart a node](/managed/managed-cluster/operation/start-stop-restart-node "Properly shut down and restart Dynatrace Managed nodes using command line parameters.").
2. Run the cluster restore procedure ([Back up and restore a Managed Cluster](/managed/managed-cluster/operation/back-up-and-restore-a-cluster#cluster-restore "Understand the steps and commands required to restore a Dynatrace Managed cluster.")) using the following modified step:

   Run the Dynatrace restore on each node

   In parallel, on each node, run the Dynatrace Managed installer using the following parameters:

   * `--rack-name`: defines the rack to which this node will belong.
   * `--rack-dc`: defines the data center to which this node will belong.
   * `--restore`: switches the installer into the restore mode.
   * `--cluster-ip`: IPv4 address of the node on which you run the installer.
   * `--cluster-nodes`: the comma-delimited list of IDs and IP addresses of all nodes in the Managed Cluster, including the one on which you run the installer, in the following format `<node_id>:<node_ip>,<node_id>:<node_ip>`.
   * `--seed-ip`: IPv4 address of the seed node.
   * `backup-file`: the path to the backup `*.tar` file, which includes the path to the shared file storage mount, the cluster ID, the node ID, the backup version, and the backup `*.tar` file in the following format:  
     `<path-to-backup>/<UUID>/node_<node_id>/files/<backup_version_number>/<backup_file>`

   Backup path example

   In this example path:
   `/mnt/backup/bckp/c9dd47f0-87d7-445e-bbeb-26429fac06c6/node_1/files/19/backup-001.tar`
   the parts of the path are as follows:

   * `<path-to-backup>` = `/mnt/backup/bckp/`
   * `<UUID>` = `c9dd47f0-87d7-445e-bbeb-26429fac06c6`
   * `<node_id>` = `1`
   * `<backup_version_number>` = `19`

   While the backup is in progress, two backup directories may be present with different backup version numbers:

   * The directory with the lower version number contains the old backup. The directory with the lower version number will be deleted after the backup completes.
   * The directory with the higher version number contains the backup that's in progress.

   The backup version number is incremented with each backup execution.

   Get the IDs and IP addresses from the inventory you created before you started.

   For example:  
   `10.176.41.168` - The IP address of the node to restore  
   `1: 10.176.41.168, 3: 10.176.41.169, 5: 10.176.41.170` - Node IDs and new IP addresses of all nodes in the Managed Cluster

   ```
   sudo ./tmp/backup-001-dynatrace-managed-installer.sh



   --rack-name rack2



   --rack-dc datacenter1



   --restore



   --cluster-ip "10.176.41.168"



   --cluster-nodes "1:10.176.41.168,3:10.176.41.169,5:10.176.41.170"



   --seed-ip "10.176.41.169"



   --backup-file /mnt/backup/bckp/c9dd47f0-87d7-445e-bbeb-26429fac06c6/node_1/files/19/backup-001.tar
   ```
3. The restore process places the loaded data directly in the target racks.

After the conversion is complete, the **Deployment status** page in the Cluster Management Console shows the racks:

![Cluster Management Console deployment status page of a Managed Cluster that's rack-aware](https://dt-cdn.net/images/cmcstatus-2263-58f0a8359d.png)

Cluster Management Console deployment status page of a Managed Cluster that's rack-aware