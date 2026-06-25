---
title: Premium HA for multi-data centers
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability/premium-high-availability
scraped: 2026-05-12T11:53:26.046843
---

# Premium HA for multi-data centers

# Premium HA for multi-data centers

* Explanation
* Updated on Apr 30, 2026

Dynatrace Premium High Availability (Premium HA) is a self-contained out-of-the-box solution that provides near-zero downtime and allows monitoring to continue without data loss in failover scenarios. This solution reduces compute and storage costs by eliminating the need for separate standby disaster recovery hosts and the associated infrastructure to store and transfer backup data.

While additional nodes in the peered data center (DC) increase the total computing capacity available to the cluster, the impact is non-linear. For capacity planning, treat the nodes in the additional DC as redundant rather than as expanded capacity, because the additional DC holds a copy of all Cassandra and Elasticsearch data from the initial DC.

Important notes

* Premium HA is available for customers with either the [Dynatrace classic licensing](/managed/license/monitoring-consumption-classic "Understand how Dynatrace monitoring consumption is calculated for classic licensing.") or [Dynatrace Platform Subscription](/managed/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") license model.
* Premium HA cluster requires a connection to [Dynatrace Mission Control](/managed/managed-cluster/basics/mission-control-proactive-support "Mission Control proactively monitors your Managed Cluster, provides software updates, and keeps your installation secure and reliable.") and is therefore only available for Managed online clusters.
* The minimum number of nodes required for a Premium HA cluster is 6 (3 nodes per DC).
* The maximum number of nodes supported for a Premium HA cluster is 30 (15 nodes per DC).
* Migration to Premium HA cannot be reversed.
* Both DCs within a Premium HA cluster must be symmetrically sized.

## Recover from a segmented cluster

If one part of a cluster loses connection with another part, this does not necessarily mean that part of the cluster is unavailable. The problem may simply be a connectivity issue. You need to determine which part of the cluster will act as the surviving one. Network disconnections of up to three hours between data centers are repaired automatically. To avoid data inconsistency during longer outages, we recommend shutting down the server service in all nodes at the affected data center. You can start services when network connectivity is stable again.

To handle the situation when one part of the cluster is unavailable, [Dynatrace Mission Control](/managed/managed-cluster/basics/mission-control-proactive-support "Mission Control proactively monitors your Managed Cluster, provides software updates, and keeps your installation secure and reliable.") tracks the health of all nodes and automatically designates one part of the cluster as primary (surviving). During the recovery, this designation determines how to re-sync all parts of the cluster.

## Data sharding and replication

Using virtual racks, Dynatrace High Availability stores three copies of all configuration data, metrics, and user sessions in each DC. This provides optimal performance and reliability in failover scenarios.

Raw transaction data (such as distributed traces, call stacks, and database statements) is distributed randomly across all DCs so that a statistically representative data set is always available on each DC.

Data is synchronized asynchronously between DCs. This eliminates the 10-ms latency requirement that applies to all cross-DC clusters. Data synchronization minimizes bandwidth consumption between DCs and prevents data loss in case of a DC outage.

During outages of less than three hours, Premium HA automatically re-synchronizes the data across DCs.

## Telemetry data routing

You can use network zones to control the flow of telemetry data to the cluster nodes in the various DCs. While Premium HA implements various optimizations to reduce cross-DC traffic, for data redundancy we recommend allowing ActiveGates to send data to both DCs. OneAgents and ActiveGates can be configured to prefer certain network zones while preserving their ability to fail over to another part of the cluster in case of a DC outage. Load balancers can also be used for this purpose.

For active-passive deployments of applications, do not disable ActiveGates in the passive portions of the deployment. This ensures all parts of the Dynatrace infrastructure remain active in disaster recovery scenarios and enables failover without reconfiguration or rediscovery.

## Technical details

Premium HA requires an OS that supports cgroups version 1.0 and systemd version 219 or later (for example, RHEL/CentOS 7+).

The various nodes continue to communicate with each other over the usual ports as described earlier. The ports that need to be open between nodes in a single DC are the same ports that need to be open within the cluster if the cluster spans two DCs.

The connections between nodes in different DCs must be encrypted. Dynatrace does not create or install the required certificates for this â you need to do that manually. Round-trip network latency of up to 100 ms is supported. Bandwidth consumption depends on a variety of factors. For more information, contact a Dynatrace product specialist.

You can migrate a single-DC cluster (or a DC-agnostic cross-DC cluster) to a dual-DC Premium HA cluster. For more information, contact a Dynatrace product specialist.