---
title: Start/stop/restart a cluster
source: https://docs.dynatrace.com/managed/managed-cluster/operation/start-stop-restart-cluster
scraped: 2026-05-12T11:53:24.883782
---

# Start/stop/restart a cluster

# Start/stop/restart a cluster

* Updated on Dec 03, 2025

Dynatrace Managed software consists of a number of Dynatrace services that are dependent on each other and should be stopped or started in a particular order. Use this procedure for Dynatrace Managed deployments containing three or more nodes.

* For Dynatrace Managed deployments containing less than three (3) nodes, you can use the official `dynatrace.sh` script with additional parameters to properly start, stop, or restart Dynatrace services on each node individually within the cluster ([Start/stop/restart a node](/managed/managed-cluster/operation/start-stop-restart-node "Properly shut down and restart Dynatrace Managed nodes using command line parameters.")).
* For Dynatrace Managed deployments containing three (3) or more nodes, use the following cluster procedures:

## Shut down cluster

1. Run the following command on each existing node:

   ```
   sudo nohup ./opt/dynatrace-managed/launcher/server.sh stop
   ```
2. Run the following command to check the status:

   ```
   sudo nohup ./opt/dynatrace-managed/launcher/server.sh status
   ```

   When all server processes are fully shut down and a status check shows them as not running, issue the following command on each existing node, one node at a time:

   ```
   sudo nohup ../launcher/dynatrace.sh stop
   ```

## Start up cluster

1. Run `/opt/dynatrace-managed/launcher/firewall.sh start` on each node.
2. Run the following command on each existing node as simultaneously as possible:

   ```
   sudo nohup ./opt/dynatrace-managed/launcher/elasticsearch.sh start
   ```

   Run the following command to check the status:

   ```
   curl -X GET "localhost:9200/_cluster/health?wait_for_status=yellow&timeout=50s&pretty"
   ```

   Check status

   Make sure `active_shards_percent_as_number` is 100% and `number_of_nodes` is equal to the number of nodes in the cluster.
3. Run the following command on each existing node as simultaneously as possible:

   ```
   sudo nohup ./opt/dynatrace-managed/launcher/cassandra.sh start
   ```

   Run the following command to check the status:

   ```
   sudo nohup ./opt/dynatrace-managed/utils/cassandra-nodetool.sh status
   ```

   Check status

   Make sure that all nodes display `UN` before proceeding to the next step.
4. Run the following command on each existing node as simultaneously as possible. It can take up to ~10 minutes to fully start a node.

   ```
   sudo nohup ./opt/dynatrace-managed/launcher/server.sh start
   ```
5. Once all server processes are up and running, start the rest of the processes. Run the following command on each existing node:

   ```
   sudo nohup ./opt/dynatrace-managed/launcher/dynatrace.sh start
   ```