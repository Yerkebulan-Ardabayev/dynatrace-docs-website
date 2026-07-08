---
title: Apply operating system patches to a node
source: https://docs.dynatrace.com/managed/managed-cluster/operation/apply-operating-system-patches-to-a-node
---

# Apply operating system patches to a node

# Apply operating system patches to a node

* Updated on Oct 17, 2025

We recommend that you perform the node operating system update or patch application one node at a time. The Dynatrace Managed node software consists of a number of Dynatrace services that are dependent on each other and should be stopped or started in a particular order. Use the official `dynatrace.sh` command with a parameter to properly start, stop, or restart Dynatrace services.

To apply the operating system patch to a Dynatrace node

1. As a root user, log into the Linux machine where the Dynatrace Managed node is installed.
2. Execute the `dynatrace.sh` command with the appropriate parameter (`start`, `stop`, or `restart`).  
   By default, the script is located at `/opt/dynatrace-managed/launcher`.

   ```
   [root@localhost]# ./dynatrace.sh stop
   ```
3. Apply all required patches to the operating system of the node.

   System restart

   Some operating system patches may require a system restart. After the restart, Dynatrace services will automatically resume unless explicitly stopped. If you plan to install additional patches post-restart, you must stop the Dynatrace services again before proceeding.  
   Failing to do so can result in the node accepting observability data inconsistently, leading to data gaps and misleading alerts. Always ensure Dynatrace is fully stopped before applying any OS-level changes to cluster nodes.
4. If no system restart occurred, restart the Dynatrace services.

   ```
   [root@localhost]# ./dynatrace.sh start
   ```