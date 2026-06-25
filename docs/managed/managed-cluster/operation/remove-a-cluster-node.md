---
title: Remove a cluster node
source: https://docs.dynatrace.com/managed/managed-cluster/operation/remove-a-cluster-node
scraped: 2026-05-12T11:53:22.332566
---

# Remove a cluster node

# Remove a cluster node

* Updated on May 24, 2024

You can easily remove a cluster node using the Dynatrace Managed Cluster Management Console. However, as removing a cluster node essentially means uninstalling Dynatrace Managed, you can alternatively use the command prompt to remove a cluster node. Both approaches are described below.

## Remove a cluster node using the Cluster Management Console

Recommended

Before you can remove a node from a Dynatrace Managed cluster, you must first disable OneAgent traffic to prevent data flow to the node while it is being removed.

### Disable OneAgent traffic

To disable a cluster node

1. Log in as an administrator. Use your Dynatrace Managed URL or a cluster node that you want to keep (you can't remove a node while you're logged into the node).
2. Go to **Deployment Status**.
3. Select **Cluster nodes** and, from the nodes list, select the node on which you want to disable OneAgent traffic.
4. Select **Configure** to view the node configuration page.
5. Select the browse button (**â¦**) in the upper-right corner.
6. Select **Disable OneAgent traffic** to stop monitoring data processing on the node. If you want to temporarily exclude the node from a cluster, stop here and enable the node later. Dynatrace Managed will keep running on the machine but it won't process monitoring data.

### Remove a disabled cluster node

Before proceeding with node removal, it's recommended that you wait for at least the duration of the transaction storage data retention period (up to 35 days). This is because while all metrics are replicated in the cluster, the raw transaction data isn't stored redundantly. Removing a node before its transaction storage data retention period expires may impact code-level and user-session data analysis.

Remove no more than one node at a time. To avoid data loss, allow 24 hours before removing any subsequent nodes. This is because it takes up to 24 hours for the long-term metrics replicas to be automatically redistributed on the remaining nodes.

If you have cluster backup enabled, and you remove a node, the backup files for that node will remain in your backup space. If you want to delete the backup specifically for the removed node, delete the `<path-to-backup>/<UUID>/node_<node_id>` folder.

Remove specific node backup example

In this example path:

```
rmdir -r /mnt/backup/bckp/c9dd47f0-87d7-445e-bbeb-26429fac06c6/node_3/
```

the parts of the path are as follows:

* `/mnt/backup/bckp/` = `<path-to-backup>`
* `c9dd47f0-87d7-445e-bbeb-26429fac06c6` = `<UUID>`
* `3` = `<node_id>`

Following the removal of an existing cluster node, you must wait 72 hours before installing a new node on a host that shares the same IP (that is when re-installing on the same host).

To remove a disabled cluster node

1. Log in as an administrator. Use your Dynatrace Managed URL or a cluster node that you want to keep (you can't remove a node while you're logged into the node).
2. Go to **Home** to navigate to the Dynatrace Managed cluster nodes page.
3. Select the cluster node you want to remove to access the node's overview page.
4. Select the browse button (**â¦**) in the top right corner.
5. Select **Remove node**. The node will then stop and be completely uninstalled from your server instance.

Dead nodes

Dynatrace Managed shows dead and removed nodes for 7 days. However even once a dead node is no longer displayed on the clusters page, the node is still registered. To remove a node entirely, use the Dynatrace API call. You can execute the Cluster Management API call to the following endpoint: `onpremise/nodeManagement/deadNodeCleaning`.

See the Dynatrace API explorer in CMC for details.

1. In the upper-right corner of the CMC, open the User menu and select **Cluster Management API**.
2. Expand the **Cluster node** and **DELETE** the `/nodeManagement/deadNodeCleaning` section to try it out.

## Remove a cluster node via REST API

Recommended

We recommend removing a cluster node using the Cluster Management Console. However, there's also an alternative option, via public API: `/api/v1.0/onpremise/nodeManagement/triggerRemoveNode`.

How to remove nodes if the cluster is down

If our recommended methods for removing cluster nodes ([Cluster Management Console](#remove-node-cmc) and [API call](#remove-node-api)) are not enough, and you're still facing issues, try using the following command prompt.

1. Log in to the Linux machine where Dynatrace Managed is installed.
2. Navigate to the `PRODUCT_PATH` main directory for Dynatrace Managed binaries (default: `/opt/dynatrace-managed`).
3. Using root rights, execute the following command:

   `/bin/sh uninstall-dynatrace.sh`

All Dynatrace Managed data will be deleted from the machine once the script is successfully executed.