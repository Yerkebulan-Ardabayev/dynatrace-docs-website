---
title: Remove a cluster
source: https://docs.dynatrace.com/managed/managed-cluster/operation/remove-a-cluster
---

# Remove a cluster

# Remove a cluster

* Published Feb 01, 2018

To remove a cluster you need to remove all nodes of the cluster. In other words, you must [uninstall Dynatrace Server from each node](/managed/managed-cluster/operation/remove-a-cluster-node "Learn how to remove a new cluster node using either the command prompt or the Cluster Management Console."). To release the license as well, use the `--unregister` parameter at least once when uninstalling the cluster nodes.

When using the `--unregister` parameter, the license is released but the cluster is still set up and can potentially be associated with a new license.