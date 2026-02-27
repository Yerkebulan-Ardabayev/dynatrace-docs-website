---
title: Monitor Kubernetes/OpenShift metrics
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-metrics-kubernetes
scraped: 2026-02-27T21:19:48.242528
---

# Monitor Kubernetes/OpenShift metrics

# Monitor Kubernetes/OpenShift metrics

* 2-min read
* Updated on Mar 14, 2023

Dynatrace version 1.232+

## Prerequisites

* In Dynatrace, go to your Kubernetes cluster settings page and make sure that **Monitor Kubernetes namespaces, services, workloads, and pods** is turned on.

## View Kubernetes metrics

* For details on container metrics, see [Built-in metrics - Containers/CPU](/docs/analyze-explore-automate/metrics-classic/built-in-metrics#containers-cpu "Explore the complete list of built-in Dynatrace metrics.") and [Built-in metrics - Containers/Memory](/docs/analyze-explore-automate/metrics-classic/built-in-metrics#containers-memory "Explore the complete list of built-in Dynatrace metrics.").

* For details on Kubernetes metrics, see [Built-in metrics - Cloud/Kubernetes](/docs/analyze-explore-automate/metrics-classic/built-in-metrics#cloud-kubernetes "Explore the complete list of built-in Dynatrace metrics.").

![K8 dash](https://dt-cdn.net/images/2021-03-12-08-54-46-1668-d24182ddd2.png)

### Workload resource metrics

Dynatrace version 1.264+ ActiveGate version 1.263+

Workload resource metrics rely on cAdvisor, which is only available on POSIX-based Kubernetes nodes. These metrics are not available on Windows.

For clusters with more than 50 nodes or 5,000 pods, resource consumption of the ActiveGate is considerably increased.

The workload and node resource metrics feature aggregates container resource metrics (CPU usage, CPU throttling, and memory consumption) to the workload and node level. Workload and node resource metrics are based on the container metrics exposed by the Kubernetes cAdvisor. This feature does not require OneAgentâan ActiveGate with Kubernetes API monitoring turned on is sufficient.

To enable monitoring of workload and node resource metrics

1. Go to ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic** and select the cluster name to open the Kubernetes cluster overview page.
2. In the upper-right corner, select **More** (**â¦**) > **Settings**, select **Monitoring settings**, and turn on **Monitor workload and node resource metrics**.

   Monitoring **node resource metrics** requires ActiveGate version 1.271+.
3. Optional Select **Test connection** to verify that the feature has been successfully activated.

For a list of all available metrics, see [Workload metrics](/docs/analyze-explore-automate/metrics-classic/all-metrics#workload "Explore the complete list of Dynatrace metrics.") or [Node](/docs/analyze-explore-automate/metrics-classic/all-metrics#node "Explore the complete list of Dynatrace metrics.") for node resource metrics.

## Related topics

* [Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")