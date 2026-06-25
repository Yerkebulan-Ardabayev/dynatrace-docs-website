---
title: Reconfigure the IP address of a cluster node
source: https://docs.dynatrace.com/managed/managed-cluster/operation/ip-reconfiguration
scraped: 2026-05-12T11:35:57.645496
---

# Reconfigure the IP address of a cluster node

# Reconfigure the IP address of a cluster node

* Updated on Nov 03, 2025

Cluster version 1.320+

As you develop your infrastructure, we aim to adapt the Dynatrace Managed deployment to the dynamic nature of cloud-based data centers.

Dynatrace Managed relies on static IP addresses, but the IP reconfiguration feature allows you to dynamically reconfigure the IP address on a node without the need to remove the node and then install a new one.

For a successful IP address reconfiguration, your cluster **must** have at least three nodes.

If both the old and new IP addresses are assigned to the same machine, ensure that the routing table is configured to route all outgoing traffic to other cluster nodes exclusively through the new IP address.

The IP address reconfiguration can also serve as an alternative to:

* [Migrate a cluster](/managed/managed-cluster/operation/migrate-a-cluster "Learn how to migrate a cluster from one data center to another.")
* [Apply operating system patches to a node](/managed/managed-cluster/operation/apply-operating-system-patches-to-a-node "Find out how to perform a graceful server shut down and apply OS patches to a node.")

## Steps

### Generate a token

1. Go to the Cluster Management Console (CMC) > **Settings** > **API tokens**.
2. Scroll down and select **Cluster tokens**.
3. Select **Generate token** and put in the **Token name**.
4. Turn on the **Service Provider API** toggle.
5. Copy the token and save it somewhere safe, because you will not be able to access it again.

### Check the node data

Make sure all node data is available on the node you want to reconfigure. You can do it:

* By copying the data to the node.
* By mounting the disks.

### Run the script

Run the script below on the node you want to reconfigure:

```
/opt/dynatrace-managed/installer/migrate-ip-local.sh --seed-auth <cluster-token>
```

The script takes some time, even up to one hour. When it finishes, the node should be visible in the cluster under the new IP address.

Additionally, the cluster administrator gets notified that IP reconfiguration is in progress by the cluster event.

### FAQ

Where is the log of reconfiguration process located?

You can find the main log in `/var/log/dynatrace/install.log` on the reconfigured machine. Many components on all nodes take part in this process, so details of each step can be found in the relevant logs.

Can I run the script more than once?

Yes, you can run the script multiple times, but one at a time.

What if I have more than one network interface?

You need to specify the IP address you want to use for Dynatrace using the `--cluster-ip <ip-for-dynatrace>` parameter.

Can I change the IP address of more than one node simultaneously?

No, you can change only one node at a time.

What if any of the steps fail?

Check the log and try to fix the issue. Then, you can run the script again.

## Related topics

* [Migrate a cluster](/managed/managed-cluster/operation/migrate-a-cluster "Learn how to migrate a cluster from one data center to another.")
* [Apply operating system patches to a node](/managed/managed-cluster/operation/apply-operating-system-patches-to-a-node "Find out how to perform a graceful server shut down and apply OS patches to a node.")