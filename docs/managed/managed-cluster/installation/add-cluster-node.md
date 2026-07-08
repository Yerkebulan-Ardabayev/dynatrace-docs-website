---
title: Add a Managed Cluster node
source: https://docs.dynatrace.com/managed/managed-cluster/installation/add-cluster-node
---

# Add a Managed Cluster node

# Add a Managed Cluster node

* How-to guide
* 3-min read
* Updated on May 08, 2026

You can scale your Managed Cluster by adding nodes through the Cluster Management Console. You need root access to the target host to run the installer.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Download installer**](/managed/managed-cluster/installation/add-cluster-node#download-installer "Add a node to your Managed Cluster by downloading the installer, running it on the target host, and monitoring synchronization progress.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Run installer**](/managed/managed-cluster/installation/add-cluster-node#run-installer "Add a node to your Managed Cluster by downloading the installer, running it on the target host, and monitoring synchronization progress.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Finalize**](/managed/managed-cluster/installation/add-cluster-node#finalize "Add a node to your Managed Cluster by downloading the installer, running it on the target host, and monitoring synchronization progress.")

* You can't add additional cluster nodes until synchronization completes.
* After removing a cluster node, wait 72 hours before installing a new node on a host with the same IP address (for example, when reinstalling on the same host).

## Step 1 Download installer

1. Log in to the **Cluster Management Console**.
2. Go to **Deployment Status** and select **Install cluster node**.
3. Copy the `wget` command line from the **Run this command on the target host** text field and paste it into your terminal window. Wait for the download to complete.

## Step 2 Run installer

1. Run one of the following commands from the directory where you downloaded the installation script. Root access is required.

   Replace `<version>` with your Dynatrace Managed version.

   * Ubuntu Server

     ```
     sudo /bin/sh dynatrace-managed-<version>.sh
     ```
   * Red Hat Enterprise Linux

     ```
     su -c '/bin/sh dynatrace-managed-<version>.sh'
     ```
   * Other Linux distributions with root session

     ```
     /bin/sh dynatrace-managed-<version>.sh
     ```
2. Type `Accept` to agree to the Dynatrace Managed [Terms of use﻿](https://www.dynatrace.com/eula/managed/). Installation won't continue until you complete this step. To quit installation, press `Ctrl+C`.
3. Accept the prompts for values such as installation path and user account by pressing `Enter`. To override a value, type your choice and press `Enter`.

## Step 3 Finalize

The newly added node appears in the Cluster Management Console with the status `joining` during installation. Full data synchronization can take a couple of hours. To monitor cluster node synchronization progress, run:

```
[root@host]# /opt/dynatrace-managed/utils/cassandra-nodetool.sh status
```

Example response:

```
Datacenter: datacenter-1



=====================



Status=Up/Down



|/ State=Normal/Leaving/Joining/Moving



--  Address         Load     Tokens       Owns (effective)  Host ID                               Rack



UN  1.6.1.6  349.88 GiB       256          100.0%           aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee  rack1



UN  1.6.2.2  358.2  GiB       256          100.0%           zzzzzzzz-xxxx-cccc-vvvv-ffffffffffff  rack1



UJ  1.6.3.9  278.75 GiB       256          ?                qqqqqqqq-wwww-eeee-rrrr-rrrrrrrrrrrr  rack1
```

Where `UJ` marks the node as `joining`.

How to read the response?

A value of `100.0%` in the `Owns (effective)` column is only visible for clusters that have up to three nodes.

If there are more than three nodes, the percentage is calculated as follows:

`(3/number_of_nodes)*100%`

While a node is joining, the `Owns (effective)` column shows a question mark (`?`). Once you scale out from two to three nodes, the value changes to `100.0%`. For additional nodes, the value is calculated per the formula above.

In a multi-rack setup, the formula for the `Owns (effective)` column changes to `(100 / number_of_nodes)%`. The first node in a rack shows `100.0%`. When you add a second node, it shows `50.0%`, and a third node shows `33.3%`.

Tips

* It's possible to see unequal values in the `Owns (effective)` column, such as `75.1%` instead of `75.0%`. This is normal, as data can't be divided into equal-sized parts between the nodes. As a result, the value for `Load` can slightly differ between the nodes.
* Cassandra doesn't automatically balance the data on disk in the entire cluster after a node is added. The value for `Owns (effective)` falls as more nodes are added to a cluster. This is expected and shows that the data responsibility per node is reduced.
* Relatedly, data on disk (`Load`) isn't automatically reduced on all cluster nodes. To instruct Cassandra to remove data from a local node for which it's no longer responsible, you can run a cleanup command.

  Before running the command, however, note the following:

  + This command can run for several hours, as Cassandra needs to rewrite all data on the local disk. During this process, CPU and disk utilization will increase locally on the node running the command, but it won't impact performance.
  + To avoid rewriting the data several times, run the cleanup only after you add all desired nodes. For example, if you plan to scale out your cluster from three to six nodes, run the cleanup only after the sixth node has been successfully added. You need to run the cleanup command on all five remaining nodes, as it's a node-local operation.

  **Cleanup command:**

  ```
  /opt/dynatrace-managed/utils/cassandra-nodetool.sh
  ```

## Frequently asked questions

### Adding a node using the Managed Cluster installation procedure

Yes, you can add a node using the same procedure as for [installing a Managed Cluster](/managed/managed-cluster/installation/install-managed-cluster "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration."). The difference is that the installer asks whether to add the node to an existing cluster (you must enter the IP address of an existing Managed Cluster node) or create a new cluster. Alternatively, use the `--seed-auth` parameter to skip this prompt and automatically add the node to the existing cluster.

### Using a privilege management system other than sudo

Yes, you can use `pbrun`, but you must grant the Dynatrace user permission to run `/opt/dtrun/dtrun *`. Specify the user who is installing Dynatrace Managed and the command that replaces `sudo`. `<version>` is the Dynatrace Managed version number.

```
/bin/sh dynatrace-managed-<version>.sh --system-user dynatrace:dynatrace --sudo-cmd  "/usr/bin/pbrun \$CMD"
```

For maintenance purposes, add the following script paths to your privilege management configuration:

* `/opt/dynatrace-managed/uninstall-dynatrace.sh`
* `/opt/dynatrace-managed/launcher/*`
* `/opt/dynatrace-managed/utils/*`

Run this command to stop all Dynatrace Managed processes on a node:

```
pbrun /opt/dynatrace-managed/launcher/dynatrace.sh stop
```

Don't remove or overwrite `dtrun`, as it's required by installation and update procedures. The installer calls `dtrun` without arguments to validate that the user has administrative privileges; during normal operation, Dynatrace calls `dtrun` with arguments to run commands.