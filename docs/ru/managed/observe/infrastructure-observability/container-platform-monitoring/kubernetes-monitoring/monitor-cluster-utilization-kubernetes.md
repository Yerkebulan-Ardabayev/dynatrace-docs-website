---
title: Monitor Kubernetes/OpenShift cluster utilization
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-cluster-utilization-kubernetes
scraped: 2026-02-18T21:26:46.039249
---

# Monitor Kubernetes/OpenShift cluster utilization

# Monitor Kubernetes/OpenShift cluster utilization

* 2-min read
* Updated on Apr 29, 2024

Dynatrace version 1.232+

## Prerequisites

* In Dynatrace, go to your Kubernetes cluster settings page and make sure that **Monitor Kubernetes namespaces, services, workloads, and pods** is turned on.

## Kubernetes page

After enabling access to the Kubernetes overview page for a specific Kubernetes cluster, the specific cluster will appear on the **Kubernetes** page. The Kubernetes page provides an overview of all Kubernetes clusters showing monitoring data like the clustersâ sizing and utilization.  
To access this page, go to ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic**.

![Cluster utilization](https://dt-cdn.net/images/cluster-list-3710-4c21475cfb.png)

## Utilization of cluster resources over time

As Kubernetes can run any containerized workloads and allow for horizontal pod autoscaling, the actual utilization of cluster resources will likely be very volatile. That is why Dynatrace offers a single pane of glass for the most important utilization and performance metrics on a cluster level. These metrics are:

* Percentage of CPU resources used out of the total allocatable CPU resources.
* Percentage of CPU resources requested/limited out of the total allocatable CPU resources.
* Percentage of memory resources requested/used out of the total allocatable memory resources.
* Percentage of memory resources limited out of the total allocatable memory resources.
* Total CPU/Memory usage.
* CPU/Memory resources requested/limited.
* CPU/Memory resources allocatable to pods.
* Total number of pods running/allocatable on cluster nodes.
* Number of times containers have been restarted.

![Monitor k8](https://dt-cdn.net/images/cluster-1-3700-55f0edc5fe.png)

## View available resources on your Kubernetes nodes

You can get detailed insights of the Kubernetes node metrics on a per-node level to understand how individual nodes are utilized. The **Node analysis** page also provides information about how much workload can still be deployed on nodes.

![View resource k8](https://dt-cdn.net/images/cluster-2-3700-209833d1e0.png)

By selecting a specific node, you can access the host details at the top of the node overview page. From there, you can delve into code-level insights on currently deployed containers, along with relevant cloud-specific host properties and Kubernetes node labels.

![View host k8](https://dt-cdn.net/images/cluster-3-3700-0d7e54a3e8.png)

## Related topics

* [Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")