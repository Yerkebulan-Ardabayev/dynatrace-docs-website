---
title: Problem graph
source: https://www.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-views/problem-graph
scraped: 2026-02-19T21:30:16.279344
---

# Problem graph

# Problem graph

* Latest Dynatrace
* Explanation
* 5-min read
* Published Jan 28, 2026

The **Problem graph** view provides a comprehensive visualization of all detected problems within your environment, including their affected nodes, related nodes, and root causes. By displaying the interrelationships between problems and nodes across your digital system, this view enables you to easily identify highly related or interconnected problems.

For example, you can quickly spot issues that affect a large number of entities or entities impacted by multiple problems.

![An example of Smartscape Problem graph home page](https://dt-cdn.net/images/problem-graph-smartscape-1920-1f8a7b5198.png)

## Constituent entities overview

### Nodes

The nodes in the **Problem graph** view represent all elements involved in a problem, as well as the problem itself. This includes:

* Problems: all detected problems in your environment.
* Affected nodes: any ![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** nodes impacted by a problem, such as hosts, processes, services, applications, or Kubernetes workloads.
* Related nodes: Any additional ![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** nodes indirectly connected to a problem, providing broader context for troubleshooting.

### Edges

The edges in the **Problem graph** view connect problems, affected nodes, and related nodes. They illustrate the inter-relationships between all elements involved in the problems across your environment and help you understand the scope and dependencies at a glance.

Edges link affected and related nodes together with problems to provide a visual representation of their relationships.

Edges in the ![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** **Problem graph** view are different from [**Smartscape on Grail**](/docs/platform/grail/smartscape-on-grail "Learn about Smartscape on Grail features and how Smartscape uses the power of DQL.") edges. For more details about Smartscape edges and how they differ, see [![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** concepts](/docs/analyze-explore-automate/smartscape "Visualize the structure of your environments and understand relationships and dependencies between your service entities.").

## Use cases

You can use ![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** **Problem graph** view to quickly identify:

* High-impact problems: quickly determine which problems have the largest impact or "blast radius" by identifying those that affect the largest number of entities.
* Problem-heavy nodes: identify nodes that are affected by multiple problems, helping you prioritize areas that require immediate attention.

## Best practice tips

To use ![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** **Problem graph** view effectively, we recommend that you:

* Focus on Relevant Areas: narrow down the ![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** **Problem graph** view by selecting one or more segments to display only the problems and nodes relevant to you or your team's area of responsibility.
* Analyze further with visual resolution paths: understand the resolution path for problems directly within the graph, without needing to leave the app.
* Drill down and open your problem in the dedicated ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** app to access detailed insights, root cause analysis, and resolution recommendations.
* Investigate specific entities (such as services or hosts) further by opening them in their respective domain applications, such as the ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations**, ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**, or ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** apps.

## Related topics

* [Smartscape](/docs/analyze-explore-automate/smartscape "Visualize the structure of your environments and understand relationships and dependencies between your service entities.")