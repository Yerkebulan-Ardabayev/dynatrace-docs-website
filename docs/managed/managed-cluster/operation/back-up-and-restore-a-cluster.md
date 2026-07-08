---
title: Backup and restore a cluster
source: https://docs.dynatrace.com/managed/managed-cluster/operation/back-up-and-restore-a-cluster
---

# Backup and restore a cluster

# Backup and restore a cluster

* Published Mar 22, 2018

To configure automatic backup for a Dynatrace Managed cluster

1. Log in to **Cluster Management Console**.
2. Go to **Settings** > **Backup**.
3. Enable cluster backup and choose the scope:

   * User sessions may contain sensitive information.  
     **Exclude user sessions from the backup to remain compliant with GDPR**.
   * Exclude timeseries metric data from the backup if your historical data isn't relevant and you only want to retain configuration data.
   * Include backup of Log Monitoring events.
4. (Optional) Select data center. This step is required only if you have multiple data center deployment (Premium High Availability deployment). For more information on Premium High Availability deployments, see [Multi-data center high availability](/managed/managed-cluster/high-availability/multi-data-centers "Understand how Dynatrace Managed Premium High Availability provides failover, data resilience, and data routing across data centers.") and [Disaster recovery from backup](/managed/managed-cluster/high-availability/recover-from-backup "Learn how to restore a Premium High Availability data center from backup in a Dynatrace Managed multi-DC deployment after a data center loss.")
5. Provide a full path to the mounted network file storage where backup archives are stored.
6. Configure start time.

## Automatic cluster backup

You can automatically back up Dynatrace Managed configuration data (naming rules, tags, management zones, alerting profiles, and more), time series metric data, and user sessions. To maximize resilience, save your backup files to an off-site location.

* Each node needs to be connected to the shared file system—for example, Network File Sharing (NFS)—and the shared file system needs to be mounted **at the same shared directory on each node**.  
  To test your user permissions, run the following command on each node:

  ```
  su - dynatrace -s /bin/bash -c "touch /nfs/dynatrace/backup/$(uname -n)"



  ls -ltr /path/to/backup/
  ```
* The user running Dynatrace services needs read/write permissions for the shared file system.
* The shared file system mount must be available at system restart.
* You can add a mount point to `fstab` or use your disk management tool to make the shared file system mount persistent.
* The protocol used to transmit data depends on your configuration. We recommend NFSv4. Due to low performance and resilience, we don't recommend CIFS.

Shared file system mount point on system boot

If the shared file system mount point isn't available on system boot, Dynatrace won't start on that node. This may lead to the cluster becoming unavailable. You must disable backups manually to allow Dynatrace to start.

### Metrics and configuration storage

Dynatrace keeps the previous backup until a new one is completed.

#### Backup characteristics

* The snapshot is performed daily.
* Any data that's replicated between nodes is also stored in the backup (there is no deduplication).
* Dynatrace excludes the most frequently changing column families (excluded column families comprise about 80% of total storage) in addition to 1-minute and 5-minute resolution data.

### Elasticsearch

Elasticsearch files are stored in uncompressed binary format. While the data is replicated across nodes and there are two replicas in addition to the primary shard, the backup excludes the replicated data.

Don't remove Elasticsearch backups

Elasticsearch backs up incrementally, so it needs to be able to append recent changes to the previous backup. Don't remove Elasticsearch backup files.

#### Backup characteristics

* The snapshot is performed, by default, every 2 hours and it is incremental.  
  Initially, Dynatrace copies the entire data set and then creates snapshots of the differences. Older snapshots are removed gradually once they are five (5) days old.
* Since Dynatrace keeps some of the older snapshots, backup size grows regardless of the current size on disk. The snapshots are incremental, but Elasticsearch merges data segments over time, which results in certain duplicates in the backup.

No transaction storage backup

Transaction storage data isn't backed up, so when you restore backups you may see gaps in deep monitoring data (for example, distributed traces and code-level traces). By default, transaction storage data is only retained for 10 days. From a long-term perspective, it's not necessary to include transaction storage data in backups.

## Cluster restore

To restore a cluster, follow the steps below.

### Before you begin

* To restore a cluster on the same host as the source cluster, make sure to uninstall it first.
* Make sure the machines prepared for the cluster restore have a similar hardware and disk layout as the original cluster and sufficient capacity to handle the load after the restore.

  We recommend that you restore the cluster to the same number of nodes as the backed up cluster. In exceptional cases, it's possible to restore to a cluster with up to two nodes fewer than the backed up cluster. You risk losing the cluster configuration if you attempt to restore to a cluster that is more than two nodes short of the original backed up cluster.
* Make sure the existing cluster is stopped to prevent two clusters with the same ID connecting to Dynatrace Mission Control. See [Start/stop/restart a cluster](/managed/managed-cluster/operation/start-stop-restart-node "Properly shut down and restart Dynatrace Managed nodes using command line parameters.").
* Make sure that system users created for Dynatrace Managed have the same UID:GID identifiers on all nodes.
* On each target node, mount the backup storage to, for example, `/mnt/backup`. This path is referred to as `<path-to-backup>` in the steps below.
* Ensure the installer has read permissions to the NFS. For example:
  `sudo adduser dynatrace && sudo chown -R dynatrace:dynatrace <path-to-backup>`
* Create your cluster inventory. You'll need this information during the restore.

  + IDs of nodes in the cluster. The backup of each node is stored in a dedicated directory whose name is based on the node identifier, in the format `node_<node-id>` (for example, `node_1`, `node_5`, etc).
  + IPv4 addresses of the new machines.
  + The IP address of the target machine for each node.
  + The node ID of the node that will become the seed node in the cluster.

### Restore from backup

To restore a cluster, follow the steps below:

1. **Copy the installer to target nodes**  
   To restore the cluster, you need to use the exact same installer version as in the original one. Copy the installer from `<path-to-backup>/<UUID>/node_<node-id>/` to a local disk on each target node.

   For example `cp <path-to-backup>/<UUID>/node_<node-id>/files/<backup-version-number>/backup-001-dynatrace-managed-installer.sh /tmp/`
2. **Launch Dynatrace restore on each node**  
   In parallel, on each node, run the Dynatrace Managed installer using the following parameters:

   * `--restore` - switches the installer into the restore mode.
   * `--cluster-ip` - IPv4 address of the node on which you run the installer.
   * `--cluster-nodes` - the comma-delimited list of IDs and IP addresses of all nodes in the cluster, including the one on which you run the installer, in the following format `<node-id>:<node-ip>,<node-id>:<node-ip>`.
   * `--seed-ip` - IPv4 address of the seed node.
   * `backup-file` - the path to the backup `*.tar` file, which includes the path to the shared file storage mount, the cluster ID, the node ID, the backup version, and the backup `*.tar` file in the following format:  
     `<path-to-backup>/<UUID>/node_<node-id>/files/<backup-version-number>/<backup-file>`

   Backup path example

   In this example path:

   `/mnt/backup/bckp/c9dd47f0-87d7-445e-bbeb-26429fac06c6/node_1/files/19/backup-001.tar`

   the parts of the path are as follows:

   * `<path-to-backup>` = `/mnt/backup/bckp/`
   * `<UUID>` = `c9dd47f0-87d7-445e-bbeb-26429fac06c6`
   * `<node-id>` = `1`
   * `<backup-version-number>` = `19`

   While the backup is in progress, two backup directories may be present with different backup version numbers:

   * The directory with the lower version number contains the old backup. It will be removed after the backup is completed.
   * The directory with the higher version number contains the backup that is in progress.

   The backup version number increments automatically with each backup run.

   Get the IDs and IP addresses from the inventory you created before you started.

   For example:  
   `10.176.41.168` - The IP address of the node to restore  
   `1: 10.176.41.168, 3: 10.176.41.169, 5: 10.176.41.170` - Node IDs and new IP addresses of all nodes in the cluster

   ```
   sudo /tmp/backup-001-dynatrace-managed-installer.sh



   --restore



   --cluster-ip "10.176.41.168"



   --cluster-nodes "1:10.176.41.168,3:10.176.41.169,5:10.176.41.170"



   --seed-ip "10.176.41.169"



   --backup-file /mnt/backup/bckp/c9dd47f0-87d7-445e-bbeb-26429fac06c6/node_1/files/19/backup-001.tar
   ```
3. **Start the firewall, Cassandra and Elasticsearch**  
   On each node successively, start the firewall, Cassandra and Elasticsearch using the launcher script:

   ```
   /opt/dynatrace-managed/launcher/firewall.sh start



   /opt/dynatrace-managed/launcher/cassandra.sh start



   /opt/dynatrace-managed/launcher/elasticsearch.sh start
   ```
4. **Verify Cassandra state**  
   On each node, check if Cassandra is running. Run the command:
   `<dynatrace-install-dir>/utils/cassandra-nodetool.sh status`

   All the nodes of the restored cluster should be listed in the response with the following values:  
   `Status = Up`
   `State = Normal`
5. **Verify Elasticsearch state**  
   On each node, check if Elasticsearch is running. Run the command:  
   `curl -s -N -XGET 'http://localhost:9200/_cluster/health?pretty' | grep status`

   You should get the following response:  
   `"status" : "green"`  
   or for one node setup:  
   `"status" : "yellow"`
6. **Restore the Elasticsearch database**  
   On the seed node, run the following command:
   `<dynatrace-install-dir>/utils/restore-elasticsearch-data.sh <path-to-backup>/<UUID>`
7. **Restore metrics and configuration data files**  
   On each node successively, starting with the seed node, run the following command:
   `<dynatrace-install-dir>/utils/restore-cassandra-data.sh <path-to-backup>/<UUID>/node_<node-id>/files/<backup-version-number>/backup-001.tar`

   Wait until Cassandra has its cluster fully set. Use the command:
   `<dynatrace-install-dir>/utils/cassandra-nodetool.sh status`

   * You should get the following response:
     `Status = Up`
     `State = Normal`
8. Optional **Repair Cassandra**

   You can run the repair only on clusters with more than one node.

   Sequentially on all nodes, initiate the Cassandra repair:

   ```
   <dynatrace-install-dir>/utils/repair-cassandra-data.sh
   ```

   This is for ensuring data consistency between the nodes. **This step may take several hours to complete**.

   To restore just the configuration data without metric timeseries, run the following command:

   ```
   <dynatrace-install-dir>/utils/repair-cassandra-data.sh 1
   ```
9. **Start Dynatrace**

   On each node successively, starting with the seed node, run the following command:

   ```
   <dynatrace-install-dir>/launcher/dynatrace.sh start
   ```

   Wait until you can sign in to Cluster Management Console.
10. Optional **Remove remaining references to old nodes**  
    In case you decided to restore fewer nodes than in the original cluster, remove the nodes marked as `Offline` in the Cluster Management Console. For more information, see [Remove a cluster node](/managed/managed-cluster/operation/remove-a-cluster-node "Learn how to remove a new cluster node using either the command prompt or the Cluster Management Console.")
11. **Switch OneAgents to the new cluster address**  
    If you originally configured the cluster with the DNS for OneAgents, you only need to update the DNS records as explained in the next step.

    Otherwise, you need to configure Cluster ActiveGates (or OneAgents, if no ActiveGates are used) with the new target address and restart them. If there are no Cluster ActiveGates but there are Environment ActiveGates, this should be done on the Environment ActiveGates.

    Otherwise, you need to configure and restart Cluster ActiveGates (or OneAgents if no ActiveGates are used) with the new target address.

    To configure a new target address on ActiveGate

    1. Stop ActiveGgate service.
    2. Update the `seedServerUrl` parameter in `config.properties`.
    3. Update the `cluster.properties` with new URLs.
    4. Remove the `connectivity_history.properties` file.

    Run the following cluster API call for each node, replacing `<node-id>` with the node identifier, `<node-ip>` with the node IPV4 address, and `<api-token>` with a valid Cluster API token.

    ```
    curl -ikS -X PUT -d <node-ip> https://<node_ip>:8021/api/v1.0/onpremise/endpoint/publicIp/agents/<node-id>?Api-Token=<api-token> -H  "accept: application/json" -H  "Content-Type: application/json"
    ```

    You should receive the `200` response as in the example below:

    ```
    HTTP/1.1 200 OK



    Date: Tue, 19 Feb 2019 17:49:06 GMT



    X-Robots-Tag: noindex



    Server: ruxit server



    Content-Length: 0
    ```
12. Optional **Update cluster DNS records**  
    If the cluster restore resulted in changing the IP addresses, update the DNS records.

    * If you use automatic domain and certificate management, run to following cluster API call for each node, replacing `<node-id>` with the node identifier, `<node-ip>` with the node IPV4 address, and `<api-token>` with a valid [API token](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

    ```
    curl -ikS -X PUT -d <node-ip> https://<node-ip>:8021/api/v1.0/onpremise/endpoint/publicIp/domain/<node-id>?Api-Token=<api-token> -H  "accept: application/json" -H  "Content-Type: application/json"
    ```

    You should receive the `200` response as in the example below:

    ```
    HTTP/1.1 200 OK



    Date: Tue, 19 Feb 2019 17:49:06 GMT



    X-Robots-Tag: noindex



    Server: ruxit server



    Content-Length: 0
    ```

    * If you use your own DNS, update your cluster domain to a new IP address.
13. **Enable the backup**  
    To prevent overwriting the previous snapshot, the backup is automatically disabled after the restore. Once you have finished restoring, you should enable the backup again.

    1. Log in to **Cluster Management Console**.
    2. Go to **Settings** > **Backup**.
    3. Turn on **Enable cluster backup** and confirm the full path to the backup archive and schedule daily backup time.

### Disable backups manually

Certain situations require that you manually disable cluster backup. For example, if the shared file system mount point isn't available on system boot, Dynatrace won't start on that node. In this case, you need to disable backups manually to allow Dynatrace to start.

1. Edit the `<install-dir>/elasticsearch/config/elasticsearch.yml` file.
2. Remove the line with the `path.repo:` parameter.
   For example:

   ```
   network.host: [ _local_, "10.10.10.10" ]



   network.publish_host: 10.10.10.10



   path.data: /var/opt/dynatrace-managed/elasticsearch



   path.repo: <REMOVE THIS LINE>
   ```
3. Save the file and restart the system. See [Start/stop/restart a cluster](/managed/managed-cluster/operation/start-stop-restart-node "Properly shut down and restart Dynatrace Managed nodes using command line parameters.")