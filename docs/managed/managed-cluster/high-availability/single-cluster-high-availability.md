---
title: Single-cluster high availability
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability/single-cluster-high-availability
---

# Single-cluster high availability

# Single-cluster high availability

* Explanation
* 3-min read
* Updated on Jul 03, 2026

Dynatrace Managed provides high availability within a single Managed Cluster. A Managed Cluster runs on three or more peer nodes that share the same services and replicate data to each other. As a result, the Managed Cluster keeps running when a node fails, and you only need to replace the failed node.

A single Managed Cluster tolerates the loss of individual nodes, but not the loss of an entire location. To achieve regional fault tolerance, where all Managed Cluster nodes in one location can fail without downtime, use Premium High Availability (PHA) across data centers. For details, go to [Multi-data center high availability](/managed/managed-cluster/high-availability/multi-data-centers "Understand how Dynatrace Managed Premium High Availability provides failover, data resilience, and data routing across data centers.").

## Node redundancy

Deploy a minimum of three Managed Cluster nodes. All nodes replicate data across the Managed Cluster, so there are typically two replicas in addition to the primary shard. Keep the latency between nodes at around 10 ms or less.

Dynatrace Managed distributes the entire configuration of the Managed Cluster and its environments across all nodes, including all events, user sessions, and metrics. The Managed Cluster maintains two copies of this data, so Dynatrace Managed continues to operate after the loss of one node. The loss of two or more nodes might affect Managed Cluster performance and availability, depending on the data distribution and the consistency level required for the data.

[Log Monitoring](/managed/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.") event data replicates in the Elasticsearch store to achieve high availability and optimize storage cost. As a result, if a node goes down, another node holds a copy. However, the failure of two nodes makes some log events unavailable. If the nodes come back up, the data becomes available again. Otherwise, Dynatrace Managed loses the data.

Dynatrace Managed doesn't replicate raw transaction data, such as call stacks, database statements, and code-level visibility, across nodes. Instead, it distributes this data evenly across all nodes. As a result, when a node fails, Dynatrace Managed can estimate the missing data. The estimate is reliable because raw transaction data is typically short-lived. Dynatrace Managed also collects a high volume of it, so each node retains a large enough data set even when another node is unavailable.

## Node failover

If a node fails, the NGINX load balancer automatically redirects all OneAgent traffic to the remaining working nodes. You only need to replace the failed node.

## Hardware placement

To prevent loss of configuration, metrics, and log data, deploy each node on a separate host. Deploy nodes on hardware with the same characteristics, especially disk, processor, and memory, to minimize performance degradation when some nodes are unavailable.

A hardware failure affects only the data on the failed machine. The failure doesn't affect metrics data or configuration, because all nodes replicate them. Dynatrace Managed loses only the data stored on that node, such as distributed traces and session replays. However, other nodes retain a representative set of similar data.

## Capacity planning

Build your Managed Cluster with additional capacity and possible node failure in mind. A Managed Cluster that operates at 100% of its processing capacity has no capacity to compensate for a lost node and can drop data during a node failure. Plan for a processing capacity one-third higher than typical utilization.