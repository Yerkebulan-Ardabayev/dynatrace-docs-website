---
title: Premium High Availability
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability
scraped: 2026-05-12T11:11:12.647346
---

# Premium High Availability

# Premium High Availability

* Explanation
* 3-min read
* Published Mar 23, 2022

Dynatrace Managed allows for high-availability deployments across single or multiple data centers that consist of multiple, equally important nodes that run the same services.

To achieve optimal failover deployments, follow these guidelines.

## Redundancy

Plan to deploy a minimum of three Managed Cluster nodes. All nodes automatically replicate data across nodes, so there are typically two replicas in addition to the primary shard. The latency between nodes should be around 10 ms or less.

The entire configuration of the Managed Cluster and its environments (including all events, user sessions, and metrics) is distributed across all nodes in the Managed Cluster, with two copies of the data maintained. This ensures that Dynatrace can continue to operate fully even after a node's loss. The Managed Cluster's performance and availability might be impacted by the loss of two or more nodes, depending on the data distribution and the consistency level required for the data.

[Log Monitoring](/managed/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.") event data is replicated in the Elasticsearch store to achieve high availability and optimize storage cost. As a result, if a node goes down, Dynatrace has a copy stored on the other node. However, the failure of two nodes makes some log events unavailable. If the nodes go back up, the data will be available again. Otherwise, the data is lost.

Raw transaction data (call stacks, database statements, code-level visibility, and so on) isn't replicated across nodes. It's evenly distributed across all nodes. As a result, in the event of a node failure, Dynatrace can accurately estimate the missing data. This is possible because this data is typically short-lived, and the high volume of raw data that Dynatrace collects ensures that each node still has a large enough data set even if a node isn't available for some time.

If you plan to achieve regional fault-tolerance (where all Managed Cluster nodes in one location domain can fail), distribute Managed Cluster nodes across separate physical locations using one of the following options:

* Two locations can only be implemented with [High availability for multi-data centers](/managed/managed-cluster/high-availability/premium-high-availability "Learn how Dynatrace Premium High Availability provides near-zero downtime and data resilience through multi-data-center deployments for Managed Clusters.").
* Three low-latency locations can be implemented with [Rack-aware Managed deployment](/managed/managed-cluster/high-availability/rack-awareness "Understand the steps required to create a rack-aware Dynatrace Managed deployment.").
* Six locations can be implemented with High availability for multi-data centers and rack-aware Managed deployment in each data center.

The replication factor of three ensures that each location has all the metric and event data.

For Dynatrace Managed installations that are deployed across globally distributed data centers (with latency higher than 10 ms), you need Premium High Availability, which provides fully automatic failover capabilities in cases where an entire data center experiences an outage. This extends the existing high availability capabilities of Dynatrace Managed to provide geographic redundancy for globally distributed enterprises that need to run critically important services in a turnkey manner without depending on external replication or load balancing solutions.  
See [High availability for multi-data centers](/managed/managed-cluster/high-availability/premium-high-availability "Learn how Dynatrace Premium High Availability provides near-zero downtime and data resilience through multi-data-center deployments for Managed Clusters.").

## Hardware

To prevent configuration, metrics, and logs data loss, deploy each node on a separate host. Deploy nodes on hardware with the same characteristics â especially disk, CPU, and RAM â to minimize performance degradation when some nodes are unavailable. Only the data on the failed machine is affected by a hardware failure. Metrics data and configuration are not affected because all nodes replicate them. The data stored on that node only â distributed traces and session replays â is lost. However, a representative count is available on other nodes. Performance degradation is minimized because all nodes operate on the same hardware type with an evenly distributed workload.

## Processing capacity

Build your Managed Cluster with additional capacity and possible node failure in mind. Managed Clusters that operate at 100% of their processing capacity have no capacity to compensate for a lost node and are susceptible to dropping data in the event of a node failure. Deployments planned for node failure should have a processing capacity one-third higher than their typical utilization.

If a node fails, the NGINX that is load-balancing the system automatically redirects all OneAgent traffic to the remaining working nodes, and there is no need for user action other than replacing the failed node.