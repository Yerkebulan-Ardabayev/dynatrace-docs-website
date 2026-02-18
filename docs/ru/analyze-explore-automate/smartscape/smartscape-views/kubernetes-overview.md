---
title: Kubernetes overview
source: https://www.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-views/kubernetes-overview
scraped: 2026-02-18T21:36:25.678011
---

# Kubernetes overview

# Kubernetes overview

* Latest Dynatrace
* Explanation
* 5-min read
* Published Jan 28, 2026

**Kubernetes overview** provides a clear visualization of your Kubernetes environment, from clusters to their components, by leveraging rich topological data in ![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape**. A high-level overview helps you to understand relationships, identify misconfigurations, and navigate dependencies with ease and context.

**Kubernetes overview** acts as a good starting point for exploring and understanding containerized workloads.

![An example of Smartscape Kubernetes overview starting view](https://dt-cdn.net/images/kubernetes-overview-smartscape-1918-369d0a086d.png)

## Constituent entities overview

**Kubernetes overview** breaks down your environment into clear, hierarchical layers to help you visualize its structure. The layers consist of:

* Nodes
* Groups

### Nodes and groups

Nodes and groups at the highest level of the view showcase Kubernetes clusters. Each cluster can contain namespaces, followed by various types of workloads. The structure can be visualized as follows:

* Kubernetes clusters

  + Kubernetes namespaces

    - Kubernetes workloads

Groups, found within the clusters, can contain entities of the same type or level. You can expand or collapse any group to improve the visibility and focus on the relevant entities.

## Use cases

You can use **Kubernetes overview** to:

* Spot misconfigurations and validate your setup by analyzing the structure of the Kubernetes topology graph.
* Clearly visualize the layout of clusters, namespaces, and workloads to facilitate cross-team collaboration or onboarding, aiding in explaining environment ownership and responsibilities.

## Best practice tips

To use **Kubernetes overview** effectively, we recommend that you:

* Focus on specific areas by selecting a segment that defines your area of responsibility, such as specific clusters, namespaces, or workloads relevant to your team.
* Use Kubernetes topology graph to ensure that configured clusters, namespaces, and workloads exist and are correctly associated with their intended clusters and namespaces.
* Drill down into any cluster, namespace, or workload in the ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** to continue your exploration or investigation and access detailed health-relevant signals, metrics, events, and logs.

## Related topics

* [Smartscape](/docs/analyze-explore-automate/smartscape "Visualize the structure of your environments and understand relationships and dependencies between your service entities.")