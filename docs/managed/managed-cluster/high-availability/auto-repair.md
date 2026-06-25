---
title: Premium HA multi-datacenter failover
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability/auto-repair
scraped: 2026-05-12T11:36:01.455149
---

# Premium HA multi-datacenter failover

# Premium HA multi-datacenter failover

* Reference
* Updated on Apr 10, 2026

Dynatrace Managed version 1.302

The Premium HA multi-datacenter failover mechanism detects Elasticsearch or Cassandra node outages longer than 15 minutes and shorter than 72 hours. If Mission Control detects that two or more Elasticsearch or Cassandra nodes in a data center (DC) are down for 15 minutes, it automatically stops the server processes in that DC and marks it as unhealthy.

* The Premium HA multi-datacenter failover mechanism is triggered only when two or more nodes in the same DC are down.
* To transfer responsibility to another DC, it must be healthy at the time of failover.

The Premium HA multi-datacenter failover mechanism is controlled by Mission Control, which instructs Nodekeepers on what to do. Every minute, each Nodekeeper sends a health check to Mission Control. In the response, each Nodekeeper receives information about the health state of other nodes collected by Mission Control, along with some instructions. These instructions can include stopping/starting the server or starting Cassandra repair. However, Nodekeepers donât receive the instructions simultaneously. They should receive them within a minute (if there are no connection problems).

The graphics in the following sections illustrate the Premium HA failover mechanism in case of Elasticsearch or Cassandra node outages.

## Premium HA failover triggered by Elasticsearch downtime

The following graphic illustrates the Premium HA failover mechanism when two or more Elasticsearch nodes in a DC are down.

![Elasticsearch failover mechanism](https://cdn.bfldr.com/B686QPH3/as/gjsqbvfmg2zpp9p7n679bfr/Elasticsearch_failover_mechanism_-_Light_Mode?auto=webp&format=png&position=1)

Elasticsearch failover mechanism

1. Mission Control detects that two or more Elasticsearch nodes in a DC are down (this is later referred to as an unhealthy DC).
2. After 15 minutes, Mission Control informs all Nodekeepers that one DC is unhealthy, requests to change the responsibility override (to the healthy DC), and requests Nodekeepers to stop all server processes in the unhealthy DC.
3. Nodekeepers stop server processes in the unhealthy DC, switch responsibility override, and ask a healthy server to generate an event and an email.
4. After you start the Elasticsearch processes on the nodes that were down, Mission Control requests that Nodekeepers start all server processes.
5. All servers are up and running.
6. After 30 minutes, Mission Control requests the Nodekeepers to change the responsibility overrideâthe cluster is fully operational.

## Premium HA failover triggered by Cassandra downtime

The following graphic illustrates the Premium HA failover mechanism when two or more Cassandra nodes in a DC are down.

![Cassandra failover mechanism](https://cdn.bfldr.com/B686QPH3/as/9q4bp3sfbm6989r5vbz6fg4/Cassandra_failover_mechanism_-_Light_Mode?auto=webp&format=png&position=1)

Cassandra failover mechanism

1. Mission Control detects that two or more Cassandra nodes in a DC are down (this is later referred to as an unhealthy DC).
2. After 15 minutes, Mission Control informs all Nodekeepers that one DC is unhealthy, requests to change the responsibility override (to the healthy DC), and requests Nodekeepers to stop all server processes in the unhealthy DC.
3. Nodekeepers stop server processes in the unhealthy DC, switch responsibility override, and ask a healthy server to generate an event and an email.
4. After you start the Cassandra processes on the nodes that were down, Mission Control requests that Nodekeepers start all server processes.
5. Nodekeepers run Cassandra repairs, one by one, on all nodes in the unhealthy DC. At the same time server start up is initiated (MC sends desired server state to RUNNING).
6. 30 minutes after all Cassandra nodes are repaired, Mission Control requests the Nodekeepers to change the responsibility overrideâthe cluster is fully operational.

## Rack awareness

Racks will be ignored if there are only one or two racks in a DC.

When you configure rack awareness for a cluster, make sure to account for it during unhealthy data center detection.

The following five rules apply when evaluating DC health:

* If two or more Cassandra nodes fail in different racks, Dynatrace marks the DC as unhealthy.
* If two or more Elasticsearch nodes fail in different racks, Dynatrace marks the DC as unhealthy.
* If two or more Cassandra nodes fail in the same rack, Dynatrace considers the DC healthy.
* If two or more Elasticsearch nodes fail in the same rack, Dynatrace considers the DC healthy.
* If one Cassandra and one Elasticsearch node fail (regardless of rack), Dynatrace considers the DC healthy.

## FAQ

What triggers the Premium HA failover mechanism?

The Premium HA failover mechanism is triggered when at least two Elasticsearch or Cassandra nodes are down. When a node is not reachable by other nodes, it is automatically added to the list of Elasticsearch/Cassandra down nodes.

Does Elasticsearch in RED status trigger the Premium HA failover mechanism?

No. We react only to Elasticsearch down status.

Does Dynatrace run a repair on all nodes in the broken DC or only on the one down?

Dynatrace repairs only the nodes that were down.

Can the minimum node downtime and Mission Control health assessment intervals be changed?

No. The Elasticsearch or Cassandra nodes must be down for 15 minutes for the failover mechanism to start. Mission Control needs 30 minutes to consider the cluster fully recovered.

What happens after 72 hours have passed?

The cluster will be marked in Mission Control as not repaired in 72 hours from the failover. Such a cluster is not reliable and you should replicate it from a healthy DC.

What events will be generated during the failover?

* Step 2âstart of the failover recovery.
* Between the steps 5 and 6âstart and end of each Cassandra repair.
* Step 8âend of the failover recovery.

What emails will be generated during the failover?

* Step 2âstart of the failover.
* Step 6âfailed Cassandra repairs (if not all finished successfully).
* Step 8âend of the failover.

I got an email titled "Automatic failover of datacenter2 has been started." How can I fix the data center?

In the message, we specify what components are down (Elasticsearch, Cassandra, or both). First check if the machine is up and running. Then try to start Elasticsearch and Cassandra using the following commands:

```
/opt/dynatrace-managed/launcher/Elasticsearch.sh start



/opt/dynatrace-managed/launcher/cassandra.sh start
```

If you notice any issues with the start process, check the following logs:

```
/var/opt/dynatrace-managed/log/Elasticsearch/\*



/var/opt/dynatrace-managed/log/cassandra/\*
```

What is required by Mission Control to mark a node as healthy after failover?

* Nodekeeper sends a healthcheck to Mission Control.
* Cassandra, Elasticsearch, and server processes are up and running.
* Any needed Cassandra repair is complete.

What happens if the repair fails?

The repair process runs only once, even if it fails. You should manually run the repair process on nodes where it automatically triggered repair failure. Dynatrace continues repairs on other nodes. Only when all repairs are done will Dynatrace inform you where the operation failed and consider the repair complete.

What logs are crucial for troubleshooting?

In an unhealthy DC, check `nodekeeper.0.0.log`, `nodekeeper-healthcheck.0.log`, and `repair-cassandra-data.log`.

In a healthy DC, only `server.log` and `audit.cluster.event.0.0.log` are important.