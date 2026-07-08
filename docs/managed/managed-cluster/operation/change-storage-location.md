---
title: Change storage location
source: https://docs.dynatrace.com/managed/managed-cluster/operation/change-storage-location
---

# Change storage location

# Change storage location

* Updated on May 20, 2026

Dynatrace Managed stores multiple types of monitoring data that vary depending on the use case. There are default storage locations, as listed in [Dynatrace Managed hardware and system requirements](/managed/managed-cluster/installation/managed-hardware-requirements#storage "Review the hardware sizing, storage, and multi-node cluster requirements before installing Dynatrace Managed on your infrastructure.").

You may need to change existing paths for the storage locations if:

* The volume storage is full and you must migrate to a larger volume.
* Current storage location is on a temporary volume and you must migrate it to another volume.
* Current storage location is on a shared volume and you want to move the data to a dedicated volume.

To change the paths to these storage locations

1. Back up your data.

   An error in this procedure can result in data loss. We advise you to back up all of the storage files to a safe location before proceeding. If possible, execute this procedure first on a test deployment.
2. Stop all Dynatrace services on the node.  
   By default, the script is located at `<PRODUCT_PATH>/launcher/`. Make sure the `dynatrace.sh` script has executable permissions. Once executed, wait for the script to finish and make sure that no Dynatrace services are running.

   ```
   [root@host]# <PRODUCT_PATH>/launcher/dynatrace.sh stop
   ```
3. Move the data store to the new location.  
   Keep in mind that you can't nest datastores within each other. For example, Cassandra storage can't be a subdirectory of session storage.

   ```
   [root@host]# cp -pR /old_location/cassandra/* /new_location/cassandra
   ```
4. Ensure that the user `dynatrace:dynatrace` is the owner of this new directory.

   ```
   [root@host]# chown -R dynatrace:dynatrace /new_location
   ```
5. Update the new data location in `/etc/dynatrace.conf`.  
   The location must be either an absolute path or a value based on predefined variables. It must be a directory, and it can't be a symlink.  
   Update the following section:

   ```
   # Paths to directories with component's data



   DATASTORE_PATH = /var/opt/dynatrace-managed



   CASSANDRA_DATASTORE_PATH = DATASTORE_PATH/CASSANDRA_DIR



   ELASTICSEARCH_DATASTORE_PATH = DATASTORE_PATH/ELASTICSEARCH_DIR



   SERVER_DATASTORE_PATH = DATASTORE_PATH/SERVER_DIR



   SERVER_REPLAY_DATASTORE_PATH = SERVER_DATASTORE_PATH/replayData



   NODEKEEPER_DATASTORE_PATH = DATASTORE_PATH/NODEKEEPER_DIR
   ```
6. Run the reconfigure via the installer. Use the `nohup` command to prevent interruption of script execution (such as session disconnect) during important operations.

   ```
   [root@host]# nohup <PRODUCT_PATH>/installer/reconfigure.sh --no-start &
   ```

   This step is crucial to propagating the changes from `/etc/dynatrace.conf` to all relevant configuration files. The `--no-start` flag will allow you to make a final verification of the changes before starting any of the Dynatrace services.

   The script output should look similar to the following:

   ```
   Reconfiguration completed successfully after 1 minute 9 seconds.



   Dynatrace binaries are located in directory /opt/dynatrace-managed



   Dynatrace data is located in directory /new_location



   Dynatrace metrics repository is located in directory /new_location/cassandra



   Dynatrace Elasticsearch store is located in directory /new_location/elasticsearch



   Dynatrace server store is located in directory /new_location/sessionstorage



   Dynatrace session replay store is located in directory /new_location/replayData



   Don't forget to start Dynatrace Server and log in at https://<your_ip>
   ```
7. Start all Dynatrace services.

   ```
   [root@host]# <PRODUCT_PATH>/launcher/dynatrace.sh start
   ```
8. Check the logs to make sure all services started without issues.

## Default directory paths and required free disk space for installing and upgrading

The directory paths included in the following table are the default paths. Actual paths may vary if you've installed to a custom directory.

Custom directories

If you customized the storage locations, `SERVER_DATASTORE_PATH`, `CASSANDRA_DATASTORE_PATH`, `ELASTICSEARCH_DATASTORE_PATH` should be placed in separate directories and they should not be a sub-directory of the other.

| **Directory symbol** | **Directory path** | **Description** | **Required free disk space for installing** | **Required free disk space for upgrading** |
| --- | --- | --- | --- | --- |
| `SELFMON_AGENT_INSTALL_PATH`  Also see, [Disk space for OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/disk-space-requirements-for-oneagent-installation-and-update-on-linux "Learn the OneAgent directory structure and disk space requirements for OneAgent installation on Linux.") | `/opt/dynatrace` | Main directory for self-monitoring OneAgent binaries. | 3 GB [1](#fn-1-1-def) | 1.8 GB [1](#fn-1-1-def) |
| `PRODUCT_PATH` | `/opt/dynatrace-managed` | Main directory for Dynatrace Managed binaries | 12 GB [1](#fn-1-1-def) | 10 GB [1](#fn-1-1-def) |
| `DATASTORE_PATH` | `/var/opt/dynatrace-managed` | Main directory for Dynatrace Managed data | 24 GB | 3 GB |
| `LOG_PATH` | `DATASTORE_PATH` `/log` | Logs of all Dynatrace Managed components, services, and tools | 2 GB | 1 GB |
| `CASSANDRA_DATASTORE_PATH` | `DATASTORE_PATH` `/cassandra` | Metrics repository | 25 GB | 1 GB |
| `ELASTICSEARCH_DATASTORE_PATH` | `DATASTORE_PATH` `/elasticsearch` | Elasticsearch store | 3 GB | 1 GB |
| `SERVER_DATASTORE_PATH` | `DATASTORE_PATH` `/server/tenantData` | Transactions store | 14 GB | 1 GB |
| `SERVER_REPLAY_DATASTORE_PATH` | `DATASTORE_PATH` `/server/replayData` | Session replay store | 14 GB | 1 GB |
| `AGENT_BUILD_UNITS_PATH` | `DATASTORE_PATH` `/agents` | OneAgent and ActiveGate installation packages (if downloaded by Dynatrace Server or installed from a standalone packages) | 20 GB | 1 GB |
| `SERVER_BUILD_UNITS_PATH` | `DATASTORE_PATH` `/installer` | Dynatrace Managed installer for adding nodes to a cluster, prepared during installation/upgrade | 2 GB | 1 GB |

1

This value is part of a total value required for the `/opt` directory. Total required free disk space is the sum of the required disk space for `/opt/dynatrace-managed` and `/opt/dynatrace`.

Not supported

Please be advised that we don't support nested mount points in the `DATASTORE_PATH/server` location for `/tenantData` and/or `/replayData`.

## Extend the size of the storage volume

To extend the size of the storage volume, you need to follow the disk extension procedure from your storage provider. If you use dynamic storage, you most likely can adjust the disk parameters (size, bandwidth, type) and the host will automatically apply it. Otherwise, a disk re-mounting may be necessary. If you've increased the size of your volume, then you must also extend the volume's partition to make use of the additional storage capacity. Dynatrace Managed services should automatically discover any changes to this.

## Dynatrace Managed cluster is out of free disk space

If there's insufficient disk space on any of your used mount points, a cluster generates a cluster event like this:

Insufficient disk space on <mountPoint> on <path>

You need at least <required MB> free for <storage type>. Currently, only <current free disk space> of a total of <disk size> is available. Providing enough disk space is vital to the health of your cluster and ensures your monitoring data is safe, consistent, and available. Ignoring that message may cause data loss.

If the transaction data storage is affected, you'll see an additional cluster event that automatically truncates the data and adapts the data retention period. To read more, see [Adaptive data retention](/managed/manage/data-privacy-and-security/data-privacy/adaptive-data-retention "Learn how Dynatrace Managed adapts transaction, Session Replay, and Log Monitoring retention when environments exceed quota or disk limits.").