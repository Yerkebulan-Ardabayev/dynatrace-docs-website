---
title: Service dependency graph
source: https://www.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-views/service-dependency-graph
scraped: 2026-03-01T21:24:52.318381
---

# Service dependency graph

# Service dependency graph

* Latest Dynatrace
* Explanation
* 5-min read
* Published Jan 28, 2026

The **Service dependency graph** view provides a comprehensive visualization of the relationships between all services in your environment. This view focuses on the logical layer of your digital system, allowing you to explore how services interact with one another and uncover critical dependency chains.

By visualizing the interconnections, the **Service dependency graph** view helps you understand how services influence each other, detect bottlenecks, and assess the potential impact of changes across your entire service landscape.

![And example of Smartscape Service dependency graph starting view](https://dt-cdn.net/images/service-dependency-graph-smartscape-1920-1c512764c7.png)

## Constituent entities overview

### Nodes

The nodes in the **Service dependency graph** view represent all services detected within your environment.

### Edges

The edges shown between service nodes in this view visualize the `_calls_` relationships between services in your environment.

## Use cases

You can use **Service dependency graph** to:

* Identify dependency chains by examining both upstream services that your service depends on, as well as downstream services that rely on your service.
* Analyze the impact of changes by visualizing how updates to one service may ripple across dependent services within the environment.
* Collaborate across teams by sharing a filtered view of the graph, helping other teams understand how their services interact with yours and fostering better communication.

## Best practice tips

To use **Service dependency graph** effectively, we recommend that you:

* Focus on what matters by selecting a segment that defines your area of responsibility, such as specific clusters, namespaces, or workloads relevant to your team.
* Optimize the view's layout and the understanding of dependency chains by making use of the **Service dependency graph** layout options to either **Vertical** or **Horizontal**.

  These layout options are only available on filtered-down views with fewer nodes.
* Actively use the pin the tooltip functionality on your service nodes to reveal key metrics such as throughput, error rates, or response times in context.
* Drill down into details of your service in the dedicated ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** app to access health-relevant signals, metrics, events, and logs.

## Related topics

* [Smartscape](/docs/analyze-explore-automate/smartscape "Visualize the structure of your environments and understand relationships and dependencies between your service entities.")