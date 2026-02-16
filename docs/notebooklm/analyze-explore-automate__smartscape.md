# Dynatrace Documentation: analyze-explore-automate/smartscape

Generated: 2026-02-16

Files combined: 3

---


## Source: visual-resolution-path.md


---
title: Visual Resolution Path
source: https://www.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-modals/visual-resolution-path
scraped: 2026-02-16T09:35:14.493846
---

# Visual Resolution Path

# Visual Resolution Path

* Latest Dynatrace
* Explanation
* 2-min read
* Published Jan 28, 2026

The Visual Resolution Path (VRP) is a ![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** modal that allows you to access the resolution path of a problem directly from any app on the Dynatrace platform. With the Visual Resolution Path view, you can see the problem's resolution path and gain immediate insights into the issue without leaving your current context and going to ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**.

From the Visual Resolution Path, you can trigger additional intents and drill-downs for deeper exploration. Alongside the visualized Visual Resolution Path entities, it includes a timeline of the underlying problem events. This provides a comprehensive, in-context view of the problem and its resolution journey.

For more details about problems and problem resolution, see [Root Cause Analysis](/docs/dynatrace-intelligence/root-cause-analysis "How Dynatrace analyzes problems to determine their root cause.").

## Visual Resolution Path support in Dynatrace apps

From the problem details in any Dynatrace application, you can drill down to the Visual Resolution Path.

Some problems don't have a detected root cause. If the problem's root cause wasn't detected, the Visual Resolution Path won't be displayed.

You can find some examples of triggering Visual Resolution Path below:

* [![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape**](/docs/analyze-explore-automate/smartscape "Visualize the structure of your environments and understand relationships and dependencies between your service entities."): you can trigger Visual Resolution Path directly from a problem node within the [Problem graph view](/docs/analyze-explore-automate/smartscape/smartscape-views/problem-graph "Use Problem graph to visualize and quickly identify problems and nodes that require immediate attention.").
* [![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**](/docs/dynatrace-intelligence/davis-problems-app "Use the Problems app to quickly get to the root cause of incidents in your environment."): you can trigger Visual Resolution Path by selecting  **Maximize** on the **Visual resolution path** in the overview tab.

  An example of triggering Visual Resolution Path from Problems app VRP overview tab

  Triggering Visual Resolution Path from Problems app VRP overview tab

## Overview

The Visual Resolution Path view consists of the selected problem entity represented by a group within the graph, the affected entities represented by nodes, and relationships between nodes represented by edges.

### Group

The problem in the Visual Resolution Path is represented as a group within the graph. The coloring of the group reflects the current state of the problem. You can also view additional details of problem itself in the tooltip overlay by hovering over the problem group's header.

### Nodes

In the Visual Resolution Path, entities involved in the problem are located within the problem group and displayed as nodes. The following entities can be found within the problem group:

* Frontends
* Services

### Edges

Edges in the Visual Resolution Path graph represent the dependency tree and relationships between the entities. These visual connections can help you understand how different components and services are interlinked.

For more information, see [Root Cause Analysis](/docs/dynatrace-intelligence/root-cause-analysis "How Dynatrace analyzes problems to determine their root cause.").

### Event Timeline

In addition to the node graph view, the Visual Resolution Path modal features an event timeline. The collapsed view of the timeline offers a high-level overview of the problem, including the start time of all associated events and the full problem timeframe.

By expanding the timeline, you can view the individual event timelines for each for each of the involved entities. This provides detailed insights into how events unfolded over time and helps you to understand the problem's progression better.

## Use cases

You can use ![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** Visual Resolution Path to:

* View key details about the problem, including its status, category, and duration.
* View the event timeline to gain a better understanding of the problem's progression over time.
* Identify cascading failures by analyzing how issues in one service propagate to other connected services or applications.

## Best practice tips

To maximize your efficiency when using ![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** Visual Resolution Path, you can:

* Hover over the problem group to view key details about the problem.
* Use the problem tooltip to:

  + Explain the problem using Dynatrace Intelligence.
  + Open the problem in the dedicated ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** app to perform advanced analysis and troubleshooting.
* Drill down into specific entities directly from the Visual Resolution Path to better understand performance bottlenecks, errors, or failures. This simplifies root cause analysis by guiding you to the affected systems and their dependencies.

## Related topics

* [Smartscape](/docs/analyze-explore-automate/smartscape "Visualize the structure of your environments and understand relationships and dependencies between your service entities.")
* [Smartscape views](/docs/analyze-explore-automate/smartscape/smartscape-views "Visualize your environment with customized Smartscape views to gain insight into relationships and dependencies between your services.")
* [Problem graph](/docs/analyze-explore-automate/smartscape/smartscape-views/problem-graph "Use Problem graph to visualize and quickly identify problems and nodes that require immediate attention.")
* [Root cause analysis](/docs/dynatrace-intelligence/root-cause-analysis "How Dynatrace analyzes problems to determine their root cause.")


---


## Source: kubernetes-overview.md


---
title: Kubernetes overview
source: https://www.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-views/kubernetes-overview
scraped: 2026-02-16T09:30:08.888443
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


---


## Source: smartscape-on-grail-view.md


---
title: Smartscape on Grail view
source: https://www.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-views/smartscape-on-grail-view
scraped: 2026-02-16T09:28:38.725447
---

# Smartscape on Grail view

# Smartscape on Grail view

* Latest Dynatrace
* Explanation
* 5-min read
* Published Jan 28, 2026

The **Smartscape on Grail** view delivers a comprehensive, real-time visualization of all detected Smartscape nodes and their interrelationships (edges) within your environment. This view provides a complete picture of your digital ecosystem's topology, enabling you to understand how entities are connected and interact across your landscape.

With the power of Grail primary fields, tags, and segments, you can customize the view to highlight the areas relevant to you and your team. Whether you're exploring your entire environment or narrowing in on a specific segment, **Smartscape on Grail** empowers you to gain deeper insights and context tailored to your needs.

![An example of Explore Smartscape on Grail home page](https://dt-cdn.net/images/smartscape-on-grail-explore-1920-f4d803dc97.png)

## Constituent entities overview

The **Smartscape on Grail** view visualizes entities as a flat structure consisting of nodes and edges. Nodes and edges can be represented by an entity of any type permitted by [**Smartscape on Grail**](/docs/platform/grail/smartscape-on-grail "Learn about Smartscape on Grail features and how Smartscape uses the power of DQL.").

### Nodes

The nodes in the **Smartscape on Grail** view represent all detected entities within your environment, including services, processes, hosts and hyperscaler resources (such as AWS EC2 instances, Azure VMs, and GCP resources). This real-time view displays all nodes active during the selected timeframe, ensuring an always up-to-date representation of your digital ecosystem.

### Edges

The edges in the **Smartscape on Grail** view represent all relationships and dependencies between nodes, such as communication flows, service calls, infrastructure connections, and more. Unlike other views, this graph is not limited to vertical (such as service-to-infrastructure) or horizontal (such as service-to-service) relationshipsâinstead, it displays all relationships comprehensively. This holistic approach ensures you gain a complete understanding of how entities interact across your environment.

## Use cases

You can use the **Smartscape on Grail** view to:

* Visualize the topology and dependencies within specific hyperscaler accounts or regions.
* Understand how the components your team owns interact, ensuring alignment and simplifying troubleshooting.
* See how services, processes, and infrastructure interact across on-premises, multi-cloud, and hybrid environments to identify potential bottlenecks or misconfigurations.
* Explore your digital ecosystemâs topology during a specific timeframe to analyze how changes or incidents impacted your environment.
* Display a dynamic graph of all nodes and relationships within an application perimeter to better understand its structure and dependencies.

## Best practice tips

To use the **Smartscape on Grail** view effectively, we recommend that you:

* Focus on relevant information by selecting a segment that defines your area of responsibility, such as specific hyperscaler accounts, regions, or workloads relevant to your team.
* Drill down into domain-specific apps (such as Services, Kubernetes, or Infrastructure & Operations) directly from nodes in the graph to access detailed metrics, events, and health signals for deeper analysis.
* Leverage the real-time nature of the graph to monitor changes in your environment as they happen, ensuring you always have up-to-date insights into your digital ecosystem.

## Related topics

* [Smartscape](/docs/analyze-explore-automate/smartscape "Visualize the structure of your environments and understand relationships and dependencies between your service entities.")


---
