---
title: Hardware requirements
source: https://docs.dynatrace.com/managed/managed-cluster/installation/managed-hardware-requirements
---

# Hardware requirements

# Hardware requirements

* Reference
* 6-min read
* Updated on Sep 30, 2026

Review the hardware requirements before installing Dynatrace Managed. Exact sizing of a Managed Cluster isn't always possible, especially in environments with growing traffic. While upfront analysis is useful, it's more important to be able to add capacity as your monitoring needs increase. Plan to scale along these dimensions:

* **Horizontal scaling**: Add more nodes. Dynatrace Managed supports up to 42 Managed Cluster nodes.
* **Vertical scaling**: Add more RAM or CPU per node.
* **Storage scaling**: Use resizable disk volumes. For details, see [Storage requirements](#storage).

Adding nodes increases how much your Managed Cluster can monitor. Keep in mind that a larger Managed Cluster also holds and processes more data. Cluster updates and other maintenance operations need more time to complete, and backups grow along with it. Plan for somewhat longer maintenance windows as your Managed Cluster grows, and scale out to gain monitoring capacity rather than to speed up existing operations.

Production environments require a minimum 3-node Managed Cluster for reliability and data redundancy. For details, see [Multi-node installations](#multi-node-install).

## Hardware requirements

The hardware requirements in the following tables are estimates based on typical environments and load patterns. Individual environments may vary. All values are per node. The storage columns show the disk space to provision: Transaction Storage covers 10 days of code visibility, and Elasticsearch covers 35 days of retention. Column definitions:

* **Max host units**: The host units that one node serves. Multiply this figure by the number of nodes to get an initial estimate for your Managed Cluster.
* **Max Full-Stack OneAgents**: The Full-Stack OneAgents that one node serves. Both columns are limits, so check which one your environment reaches first. Hosts with a lot of memory usually reach the host units limit first, while many small hosts usually reach the OneAgent limit first.
* **Minimum node specifications**: CPU and RAM must be exclusively available for Dynatrace. Turn off CPU power-saving mode. CPUs must run at 2 GHz or faster. Hosts must have at least 32 GB RAM.
* **Transaction Storage**: Dynatrace Managed distributes transaction storage across all nodes and doesn't store it redundantly. In multi-node Managed Clusters, Dynatrace Managed divides the total transaction storage by the number of nodes.
* **Long-term Metrics Store**: In multi-node installations, Dynatrace Managed stores three copies of the metrics store. For four or more nodes, the per-node storage requirement decreases.

  Keep the Long-term Metrics Store data below 2 TB per node. The disk sizes in the following tables include free space that Cassandra needs for compaction. Dynatrace Managed raises a warning cluster event when the data on a node exceeds 2 TB, and a severe cluster event when it exceeds 4 TB. Persistent storage growth degrades Managed Cluster performance, resilience, and availability, and causes issues when adding nodes. If you need more storage, add another node to reduce the per-node requirement.

Host units measure the RAM of your monitored hosts, not the amount of data those hosts produce. Two hosts of the same size can place different loads on your Managed Cluster, depending on how many processes, services, and requests run on them. Use the following tables for your initial sizing, then monitor your Managed Cluster and add nodes as your load grows.

A node can reach the recommended 2 TB of Long-term Metrics Store data before it reaches the host units listed here, so check both.

### Dynatrace Managed

| **Node size** | **Max host units[1](#fn-1-1-def)** | **Max Full-Stack OneAgents** | **Peak user actions/min** | **Min node specifications** | **Disk IOPS** | **Transaction Storage** | **Long-term Metrics Store** | **Elasticsearch** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Micro | 50 | 25 | 1000 | 4 vCPUs, 32 GB RAM[2](#fn-1-2-def) | 500 | 50 GB | 100 GB | 50 GB |
| Small | 300 | 100 | 10000 | 8 vCPUs, 64 GB RAM | 3000 | 300 GB | 500 GB | 500 GB |
| Medium | 600 | 250 | 25000 | 16 vCPUs, 128 GB RAM | 5000 | 600 GB | 1 TB | 1.5 TB |
| Large | 1250 | 500 | 50000 | 32 vCPUs, 256 GB RAM | 7500 | 1 TB | 2 TB | 1.5 TB |
| XLarge[3](#fn-1-3-def) | 2500 | 800 | 100000 | 64 vCPUs, 512 GB RAM | 10000 | 2 TB | 4 TB | 3 TB |

1

The number of **host units** a monitored host consumes depends on the amount of RAM available on that host. A host with 16 GiB RAM consumes 1 host unit in Full-Stack mode, and a host with 64 GiB RAM consumes 4 host units. Because RAM is the only factor, a host unit doesn't tell you how much monitoring data a host produces. For full details, see [Application and Infrastructure Monitoring](/managed/license/classic-licensing/application-and-infrastructure-monitoring "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units."). If you license Dynatrace through the Dynatrace Platform Subscription (DPS), Full-Stack Monitoring consumption is also based on host memory, measured in [GiB-hours](/managed/license/capabilities/app-infra-observability/full-stack-monitoring#gib-hour "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged."). To estimate host units, divide the total memory of all Full-Stack monitored hosts by 16 GiB. For example, 100 hosts with 32 GiB RAM each, monitored around the clock, consume about 28 million GiB-hours per year and correspond to about 200 host units.

2

See RAM requirements in [Log Monitoring recommendations](/managed/managed-cluster/installation/managed-hardware-requirements#log-mon "Review the hardware sizing, storage, and multi-node cluster requirements before installing Dynatrace Managed on your infrastructure.").

3

Dynatrace Managed runs resiliently on instances with 1 TB+ RAM/128 cores (2XLarge) and lets you monitor more entities, but this setup doesn't use the hardware optimally. Instead, consider using smaller instances (Large or XLarge).

#### Examples

* To monitor up to 7,500 host units and up to 2,400 Full-Stack OneAgents with a peak load of 300,000 user actions per minute, you need 3 XLarge nodes with 9 TB storage each, split across storage types.
* To monitor 500 host units and up to 300 Full-Stack OneAgents with a peak load of 25,000 user actions per minute, you need 3 Small nodes with 1.3 TB storage each, split across storage types.
* To monitor 900 hosts with 8 GiB RAM each (450 host units, 900 Full-Stack OneAgents) with a peak load of 25,000 user actions per minute, you need 4 Medium nodes with 3.1 TB storage each, split across storage types. Based on host units alone, 3 Small nodes would be enough, but they serve only 300 Full-Stack OneAgents.

### Dynatrace Managed Premium High Availability

In a Premium High Availability deployment, the node limit counts all nodes across both data centers: a 42-node Managed Cluster runs 21 nodes in each data center. Size both data centers symmetrically, with the same number of nodes and the same hardware, including disk storage, in each. For details, see [Premium High Availability](/managed/managed-cluster/high-availability/multi-data-centers "Understand how Dynatrace Managed Premium High Availability provides failover, data resilience, and data routing across data centers."). The second data center holds a copy of the data. As a result, a node of a given size serves fewer host units than the same node size in a Managed Cluster with one data center. The following table accounts for this, which is why its figures are lower than in the Dynatrace Managed table. Multiply them by the total number of nodes, not by the nodes in one data center.

| **Node size** | **Max host units** | **Max Full-Stack OneAgents** | **Peak user actions/min** | **Min node specifications** | **Disk IOPS** | **Transaction Storage** | **Long-term Metrics Store** | **Elasticsearch** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Large | 600 | 350 | 25000 | 32 vCPUs, 256 GB RAM | 7500 | 1 TB | 2 TB | 1.5 TB |
| XLarge[1](#fn-2-1-def) | 1250 | 700 | 50000 | 64 vCPUs, 512 GB RAM | 10000 | 2 TB | 4 TB | 3 TB |

1

While Dynatrace Managed runs resiliently on instances with 1 TB+ RAM/128 cores (2XLarge) and allows you to monitor more entities, it's not the optimal way of utilizing the hardware. Instead, consider using smaller instances (Large or XLarge).

#### Example

To monitor 7,500 host units and up to 4,200 Full-Stack OneAgents with a peak load of 300,000 user actions per minute in a Premium High Availability deployment, you need 6 XLarge nodes. Place 3 nodes in one data center and 3 nodes in a second data center, each with 9 TB storage split across storage types.

## Storage requirements

Dynatrace Managed stores multiple types of monitoring data. Follow these recommendations:

* Store Dynatrace binaries and the data store on separate mount points so you can resize the data store independently.
* Don't store Dynatrace data on the root volume to avoid complexity when resizing later.
* Exclude data storage paths from antivirus scanning to prevent data consistency issues.
* Mount different types of data storage on separate disk volumes for maximum flexibility and performance.
* Use resizable disk partitions, for example with Logical Volume Manager (LVM).
* Use the same partition size on all Managed Cluster nodes.
* For details, see [Default directory paths and required free disk space for installing and upgrading](/managed/managed-cluster/operation/change-storage-location#default-directory-paths-disk-space "Learn how to change the location of datastores defined during the install of Dynatrace Managed.").

Disk size can vary depending on usage. For example, in a 2-node Managed Cluster where each node has 10 TB and transaction storage on both nodes is only 1.5 TB, a third node needs a minimum of 1 TB: (1.5 TB + 1.5 TB) / 3 = 1 TB.

In a similar Managed Cluster where disks are 9 TB full, a third node needs a minimum of 6 TB: (9 TB + 9 TB) / 3 = 6 TB.

Anything below the calculated minimum is a misconfiguration. Multiple data sources, such as Session Replay, contribute to disk usage and can also trigger a misconfiguration.

### File system requirements

Dynatrace Managed works with all common file systems. Use fast local storage suitable for database workloads. Dynatrace Managed also supports encrypted file systems when disk IOPS meet the requirements and encryption is transparent at the operating system level. Examples include Amazon EBS and Azure Storage encryption.

* High-latency remote volumes such as NFS or CIFS aren't supported for primary storage; NFS is sufficient for backups only.
* Amazon Elastic File System (EFS) isn't supported as primary storage for Elasticsearch, because it may lead to index corruption.

## Log Monitoring requirements

Requirements for [Log Monitoring](/managed/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more."):

* All Managed Cluster nodes must have at least 64 GB total RAM.

Additional recommendations:

* Add more Managed Cluster nodes rather than increasing hardware per node for a more resilient configuration.
* Distribute additional Elasticsearch storage equally across all Managed Cluster nodes.
* Plan custom log retention for environments according to the available hardware. Depending on the number and size of Managed Cluster nodes and the selected retention times, only a limited number of environments can use longer custom log retention.
* When adding CPUs or RAM, keep all nodes equally sized.
* Update the Managed Cluster ingest limit via Cluster Management Console or [REST API](/managed/dynatrace-api/cluster-api/cluster-api-v2/log-monitoring/post-update-log-events-per-cluster-for-log-monitoring "Learn how to update the total log events per cluster limit based on the cluster resources size using API.") whenever hardware changes.

  1. Sign in to the **Cluster Management Console**.
  2. Go to **Environments**, select your environment, and adjust the limit in **Cluster overload prevention settings**.

## Multi-node installations

Production environments require a minimum 3-node Managed Cluster for reliability and data redundancy. All nodes in a multi-node Managed Cluster must:

* Have the same hardware configuration
* Synchronize with NTP
* Be in the same time zone
* Communicate over a private network on the [required ports](/managed/managed-cluster/installation/cluster-node-ports "Review the network ports required by Dynatrace Managed and configure your firewall for inbound and outbound communication.")
* Have a network latency between nodes of 10 ms or less
* Have matching Dynatrace Managed system user and group identifiers on all nodes