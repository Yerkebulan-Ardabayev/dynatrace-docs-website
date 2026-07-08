---
title: Multi-data center high availability
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability/multi-data-centers
---

# Multi-data center high availability

# Multi-data center high availability

* Explanation
* 5-min read
* Updated on Jul 07, 2026

Premium High Availability (PHA) extends Dynatrace Managed high availability across two data centers (DC). PHA is a self-contained solution that keeps monitoring running with no data loss and minimal downtime when a DC fails.

PHA keeps a full, active copy of your data in the second DC. The active copy removes the need for separate standby disaster recovery hosts and backup transfer infrastructure, reducing both compute and storage costs.

## Requirements and limitations

Before you plan a PHA deployment, review the following requirements and limitations:

* Use a license model that supports PHA, either [Dynatrace Classic](/managed/license/monitoring-consumption-classic "Understand how Dynatrace classic monitoring consumption is calculated, including host units, DDUs, DEM units, and Application Security units.") or [Dynatrace Platform Subscription](/managed/license "Dynatrace Platform Subscription, capability rate cards, hybrid licensing, and previous license models.").
* Connect the Managed Cluster to [Dynatrace Mission Control (MC)](/managed/managed-cluster/basics/mission-control-proactive-support "Mission Control proactively monitors your Managed Cluster, provides software updates, and keeps your installation secure and reliable."). PHA is available only for Managed online clusters.
* Deploy at least 6 nodes, with 3 nodes per DC.
* Deploy no more than 30 nodes, with no more than 15 nodes per DC.
* Size both DCs symmetrically.
* Plan the migration. You can't reverse a migration to PHA.
* Use an operating system that supports `cgroups` version 1.0 and `systemd` version 219 or later, for example Red Hat Enterprise Linux 7 or CentOS 7.
* Open the same ports between nodes in one DC and in a Managed Cluster that spans two DCs.
* Encrypt the connections between nodes in different DCs. Dynatrace Managed doesn't create or install the required certificates.
* Keep round-trip network latency at 100 ms or less.

## Regional fault tolerance

Regional fault tolerance means that all Managed Cluster nodes in one location can fail without downtime. To achieve it, distribute Managed Cluster nodes across separate physical locations using one of the following options:

* Use PHA for two locations that need geographic redundancy and automatic failover.
* Use [rack-aware deployment](/managed/managed-cluster/high-availability/rack-awareness "Learn how rack-aware deployment groups Dynatrace Managed Cluster nodes into three fault domains to ensure resilience against a full rack outage and data loss.") for three low-latency locations.
* Combine PHA with [rack-aware deployment](/managed/managed-cluster/high-availability/rack-awareness "Learn how rack-aware deployment groups Dynatrace Managed Cluster nodes into three fault domains to ensure resilience against a full rack outage and data loss.") in each DC for six locations.

The replication factor of three ensures that each location has all the metric and event data.

## Capacity planning

Build your Managed Cluster with additional capacity and possible node failure in mind. Managed Clusters that operate at 100 percent of their processing capacity have no capacity to compensate for a lost node. Deployments operating at full capacity can drop data during a node failure.

Deployments planned for node failure should have a processing capacity one-third higher than their typical utilization.

For capacity planning in a PHA deployment, treat the nodes in the additional DC as redundant rather than as expanded capacity. The additional DC holds a copy of all Cassandra and Elasticsearch data from the initial DC.

If a node fails, NGINX automatically redirects all OneAgent traffic to the remaining working nodes. You only need to replace the failed node.

## Data replication across data centers

Dynatrace Managed distributes the entire configuration of the Managed Cluster and its environments across all nodes. The replicated data includes all events, user sessions, and metrics. The Managed Cluster maintains two copies of this data, so Dynatrace Managed can continue to operate after the loss of one node.

The loss of two or more nodes might affect Managed Cluster performance and availability. The impact depends on data distribution and the consistency level required for the data.

[Log Monitoring](/managed/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.") event data replicates in the Elasticsearch store to achieve high availability and optimize storage cost. As a result, if a node goes down, another node has a copy. However, the failure of two nodes makes some log events unavailable. If the nodes go back up, the data becomes available again. Otherwise, Dynatrace Managed loses the data.

Dynatrace Managed doesn't replicate raw transaction data, such as call stacks, database statements, and code-level visibility, across nodes. Dynatrace Managed evenly distributes this data across all nodes.

As a result, when a node fails, Dynatrace Managed can estimate the missing data. The estimate is possible because raw transaction data is typically short-lived. Dynatrace Managed also collects a high volume of raw data, so each node still has a large enough data set even if another node isn't available for some time.

### Data sharding and replication

Using virtual racks, PHA stores three copies of all configuration data, metrics, and user sessions in each DC. Three-copy storage provides optimal performance and reliability in failover scenarios.

PHA distributes raw transaction data, such as distributed traces, call stacks, and database statements, across all DCs. Cross-DC distribution makes a statistically representative data set available in each DC.

PHA synchronizes data asynchronously between DCs. Asynchronous synchronization eliminates the 10 ms latency requirement that applies to Managed Clusters that span DCs. Data synchronization minimizes bandwidth consumption between DCs and prevents data loss during a DC outage.

During outages of up to 72 hours, PHA automatically re-synchronizes data across DCs.

## Telemetry routing

PHA uses network zones to route telemetry to Managed Cluster nodes in different DCs. Network zones let OneAgents and ActiveGates prefer local routes while retaining the ability to fail over to another DC during an outage. For setup guidance, go to [Replicate nodes across data centers for PHA](/managed/managed-cluster/high-availability/add-data-center#review-network-zone-setup "Learn how to replicate Managed Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.").

## Failover and recovery

PHA handles DC outages of up to 72 hours automatically and uses Mission Control to designate the surviving part of the Managed Cluster during recovery. For failover behavior, go to [Multi-data center failover](/managed/managed-cluster/high-availability/failover "Learn how the Premium High Availability multi-data center failover mechanism detects node outages and transfers responsibility to a healthy data center."). For recovery after longer outages, go to [Data center disaster recovery from data center](/managed/managed-cluster/high-availability/recover-from-data-center "Recover a data center when Premium High Availability can't repair it within 72 hours by restoring or recreating it from another data center.").

You can migrate a Managed Cluster from a single DC, or a Managed Cluster that already spans DCs, to a dual-DC PHA deployment. For migration steps, go to [Replicate nodes across data centers for PHA](/managed/managed-cluster/high-availability/add-data-center "Learn how to replicate Managed Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.").

## Hardware placement

To prevent configuration, metrics, and logs data loss, deploy each node on a separate host. Deploy nodes on hardware with the same characteristics, especially disk, processor, and memory. Identical hardware minimizes performance degradation when some nodes are unavailable.

A hardware failure affects only the data on the failed machine. The failure doesn't affect metrics data or configuration because all nodes replicate them. Dynatrace Managed loses only the data stored on that node, such as distributed traces and session replays. However, other nodes still contain enough similar data for estimates.

Matching hardware and balanced workloads reduce performance degradation when nodes are unavailable.