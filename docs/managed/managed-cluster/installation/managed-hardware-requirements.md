---
title: Hardware requirements
source: https://docs.dynatrace.com/managed/managed-cluster/installation/managed-hardware-requirements
---

# Hardware requirements

# Hardware requirements

* Reference
* 6-min read
* Updated on Jun 16, 2026

Review the hardware requirements before installing Dynatrace Managed. Exact sizing of a Managed Cluster isn't always possible, especially in environments with growing traffic. While upfront analysis is useful, it's more important to be able to add capacity as your monitoring needs increase. Plan to scale along these dimensions:

* **Horizontal scaling**: Add more nodes. Dynatrace Managed supports up to 30 Managed Cluster nodes.
* **Vertical scaling**: Add more RAM or CPU per node.
* **Storage scaling**: Use resizable disk volumes. For details, see [Storage requirements](#storage).

Production environments require a minimum 3-node Managed Cluster for reliability and data redundancy. For details, see [Multi-node installations](#multi-node-install).

## Hardware requirements

The hardware requirements in the following tables are estimates based on typical environments and load patterns. Individual environments may vary. Column definitions:

* **Minimum node specifications**: CPU and RAM must be exclusively available for Dynatrace. Turn off CPU power-saving mode. CPUs must run at 2 GHz or faster. Hosts must have at least 32 GB RAM.
* **Transaction Storage**: Dynatrace Managed distributes transaction storage across all nodes and doesn't store it redundantly. In multi-node Managed Clusters, Dynatrace Managed divides the total transaction storage by the number of nodes.
* **Long-term Metrics Store**: In multi-node installations, Dynatrace Managed stores three copies of the metrics store. For four or more nodes, the per-node storage requirement decreases.

  Keep the Long-term Metrics Store below 2 TB per node. Dynatrace supports stability and operational resilience up to 4 TB per node. Persistent storage growth degrades Managed Cluster performance, resilience, and availability, and causes issues when adding nodes. If you need more storage, add another node to reduce the per-node requirement.

### Dynatrace Managed

| **Node size** | **Max host units[1](#fn-1-1-def) monitored** (per node) | **Peak user** **actions/min** (per node) | **Min node specifications** | **Disk IOPS** (per node) | **Transaction Storage** (10 days code visibility) | **Long-term Metrics Store** (per node) | **Elasticsearch** (per node) (35 days retention) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Micro | 50 | 1000 | 4 vCPUs, 32 GB RAM[2](#fn-1-2-def) | 500 | 50 GB | 100 GB | 50 GB |
| Small | 300 | 10000 | 8 vCPUs, 64 GB RAM | 3000 | 300 GB | 500 GB | 500 GB |
| Medium | 600 | 25000 | 16 vCPUs, 128 GB RAM | 5000 | 600 GB | 1 TB | 1.5 TB |
| Large | 1250 | 50000 | 32 vCPUs, 256 GB RAM | 7500 | 1 TB | 2 TB | 1.5 TB |
| XLarge[3](#fn-1-3-def) | 2500 | 100000 | 64 vCPUs, 512 GB RAM | 10000 | 2 TB | 4 TB | 3 TB |

1

The host size for licensing purposes depends on the amount of RAM provided by a host. The number of **host units** that a host uses for consumption calculations depends on the number of GBs of RAM available on the host server. This approach is simple because technology-specific factors don't affect the calculation. For example, the number of JVMs or microservices hosted on a server doesn't affect the amount of monitoring that an environment consumes. For full details, see [Application and Infrastructure Monitoring](/managed/license/classic-licensing/application-and-infrastructure-monitoring "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.").

2

See RAM requirements in [Log Monitoring recommendations](/managed/managed-cluster/installation/managed-hardware-requirements#log-mon "Review the hardware sizing, storage, and multi-node cluster requirements before installing Dynatrace Managed on your infrastructure.").

3

Dynatrace Managed runs resiliently on instances with 1 TB+ RAM/128 cores (2XLarge) and lets you monitor more entities, but this setup doesn't use the hardware optimally. Instead, consider using smaller instances (Large or XLarge).

#### Examples

* To monitor up to 7,500 host units with a peak load of 300,000 user actions per minute, you need 3 XLarge nodes with 9 TB storage each, split across storage types.
* To monitor 500 host units with a peak load of 25,000 user actions per minute, you need 3 Small nodes with 1.3 TB storage each, split across storage types.

### Dynatrace Managed Premium High Availability

| **Node size** | **Max host units** **monitored** (per node) | **Peak user** **actions/min** (per node) | **Min node specifications** | **Disk IOPS** (per node) | **Transaction Storage** (10 days code visibility) | **Long-term Metrics Store** (per node) | **Elasticsearch** (per node) (35 days retention) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Large | 600 | 25000 | 32 vCPUs, 256 GB RAM | 7500 | 1 TB | 2 TB | 1.5 TB |
| XLarge[1](#fn-2-1-def) | 1250 | 50000 | 64 vCPUs, 512 GB RAM | 10000 | 2 TB | 4 TB | 3 TB |

1

While Dynatrace Managed runs resiliently on instances with 1 TB+ RAM/128 cores (2XLarge) and allows you to monitor more entities, it's not the optimal way of utilizing the hardware. Instead, consider using smaller instances (Large or XLarge).

#### Example

To monitor 7,500 host units with a peak load of 300,000 user actions per minute in a Premium High Availability deployment, you need 6 XLarge nodes. Place 3 nodes in one data center and 3 nodes in a second data center, each with 9 TB storage split across storage types.

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