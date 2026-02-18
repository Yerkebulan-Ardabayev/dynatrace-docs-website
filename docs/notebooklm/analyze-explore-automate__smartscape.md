# Документация Dynatrace: analyze-explore-automate/smartscape
Язык: Русский (RU)
Сгенерировано: 2026-02-18
Файлов в разделе: 12
---

## analyze-explore-automate/smartscape/smartscape-concepts.md

---
title: Smartscape concepts
source: https://www.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-concepts
scraped: 2026-02-18T05:45:05.733882
---

# Smartscape concepts

# Smartscape concepts

* Latest Dynatrace
* Explanation
* 8-min read
* Published Jan 28, 2026

This page is an introduction to Smartscape-specific concepts, as well as general concepts and their usage within ![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape**.

## Smartscape views

![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** provides multiple topology views, each offering a unique perspective on your digital system. For more information, see [![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** views](/docs/analyze-explore-automate/smartscape/smartscape-views "Visualize your environment with customized Smartscape views to gain insight into relationships and dependencies between your services.").

## Smartscape modals

![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** modals deliver in-context topological insights anywhere on the platform, seamlessly integrating analytics into your workflows. ![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** modals are displayed in an overlay on top of the existing app, which allows you to access topological insights and analytics without leaving your current app or context. For more information, see [![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** modals](/docs/analyze-explore-automate/smartscape/smartscape-modals "Use Smartscape modals to visualize your environment in any Dynatrace app and gain insights into problem resolution and service dependencies").

## Nodes, edges, and groups

In graph visualizations, a graph is a network of entities (nodes) and their relationships (edges). Here's how the key components work:

* Nodes: Represent entities or objects, such as people, devices, or systems. They are displayed as circles, dots, or vertices in the visualization.
* Edges: Represent relationships or connections between nodes, such as communication links, dependencies, or interactions. These are rendered as lines between nodes in the graph.
* Groups: Represent clusters or collections of nodes that share a common characteristic or context. In the visualization, groups encompass a set of nodes. Nodes and groups can also have multiple levels of nesting.

In **Smartscape on Grail**, nodes and edges are specifically designed to represent your digital ecosystem:

* Smartscape Nodes: Represent individual entities, such as services, processes, hosts, or data centers.
* Smartscape Edges: Represent the relationships or dependencies between nodes. For example, a `calls` relationship between services, or a `runs on` relationship between a process and a host.

The nodes and edges shown in the ![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** app don't always map 1:1 to **Smartscape on Grail** nodes and edges. Based on the specific view and use case, we may adjust how entities, properties, or relationships are represented to make the data more meaningful.

## Timeframe selector

The timeframe selector in the ![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** app works slightly different compared to the other areas of the platform. The timeframe selector lets you view nodes whose lifetime overlaps with the selected timeframe. This ensures that you only see nodes relevant to the period you're analyzing.

For more information about lifetime, see [**Smartscape on Grail**](/docs/platform/grail/smartscape-on-grail "Learn about Smartscape on Grail features and how Smartscape uses the power of DQL.").

## Segments

Segments allow you to logically structure and conveniently filter observability data across apps on the Dynatrace platform. Within the ![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** app, we recommend using segments as a best practice to filter your graph view down to a dataset that is relevant to you and your team.

Working with vast amounts of data such as thousands of nodes in a graph, and trying to analyze everything at once, can be overwhelming and counterproductive. By narrowing the scope to your area of responsibilityâwhether it's a specific application, environment, or infrastructureâyou can uncover actionable insights faster and make effective decisions. Filtering with segments allows you to enhance clarity and ensures that the data you're viewing is relevant to your goals.

### Segments in Smartscape **Smartscape**

In nested views, if your segment filters out a parent group, you won't be able to see the child nodes of that group even if those child nodes aren't directly affected by the segment filter.

For more information about Segments, see [Segments](/docs/manage/segments "Segments logically structure monitoring data in Grail and function as convenient filters for data that users are allowed to access based on permissions.").

## Tooltips

Tooltips, or overlays, provide in-context information about nodes, groups, or edges within a Smartscape view. You can perform the following actions to access tooltips:

* Hover for key metadata: Hovering over a node, group, or edge displays a tooltip with essential metadata.
* Select for more details: Selecting a node or group tooltip pins it in place, loads key metrics, and reveals further actions and intents you can perform:

  + Actions: Trigger actions directly within the ![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** app, such as isolating a node for deeper analysis.
  + Drilldowns: Navigate to other platform applications to continue your analysis in dedicated domain-specific tools.

Tooltips ensure you have quick access to relevant information and workflows, streamlining your analysis process.

## Toolbar

The toolbar in the Smartscape graph provides an intuitive way to navigate and interact with the visualization. The available tools include:

* **Move**: Move the toolbar across the Smartscape graph.
* **Download**: Export the Smartscape graph as a .png image. You can choose from the following options:

  + **Download full view as PNG**: Download the complete Smartscape graph.
  + **Download current view as PNG**: Download only the portion of the graph currently visible on your screen.
* **Zoom in** and  **Zoom out**: Adjust the zoom level to focus on specific areas or view a broader section of the graph.
* **Zoom to fit**: Automatically adjust the zoom to ensure the entire graph fits within your view.
* **Collapse all**: Collapse all open groups within the graph.
* **Reset**: Return the graph view to its original state.

## Badges

Badges appear on nodes, groups, and edges within ![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** views. Their meaning depends on the element they are attached to and the specific view being displayed.

In general, badges show the number of active problems on a given element, such as a group or a node (see below).

### Problem indicators

Problem indicators are a specialized type of badge that display the number of problems detected for a specific Smartscape node.

There are several types of problem indicators:

* Group-specific: For Smartscape groups (nodes with children), the problem count reflects only the issues associated with the group entity itself and doesn't include problems from child nodes. This means that problems on child nodes aren't aggregated or counted towards the problem count of the parent group.
* Affected nodes only: Problem indicators are shown only on Smartscape nodes directly affected by a problem.

  + Related nodes that are indirectly associated with a problem won't display a problem indicator.

## Optimized views

To ensure a seamless and responsive experience, the ![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** app dynamically optimizes your view by limiting the graph to display a maximum of 4,000 nodes and 10,000 edges. This allows you to explore your environment efficiently without compromising performance or usability.

If you need deeper insights into your data, you can fine-tune your view by:

* Using segments: to filter your graph view down to a dataset that is meaningful to you and your team. For more information, see the [Segments](#smartscape-segments) section.
* Adjusting the timeframe: Limit the view's timeframe to a shorter time period to capture the most relevant details. For more information, see the [Timeframe selector](#smartscape-timeframe-selector) section.

By optimizing the graph's size, you can ensure a stable and uninterrupted experience.

---

## analyze-explore-automate/smartscape/smartscape-modals/smartscape-view-topology.md

---
title: View topology
source: https://www.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-modals/smartscape-view-topology
scraped: 2026-02-18T21:31:54.957597
---

# View topology

# View topology

* Latest Dynatrace
* Explanation
* 2-min read
* Published Jan 28, 2026

View topology is an intuitive, in-context ![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** modal that allows you to visualize the topology of a selected entity across the platform. By integrating seamlessly into existing workflows, the modal helps you to get a deeper understanding of both vertical and horizontal relationships between entities in your environment.

By using the View topology ![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** modal, you can easily explore Smartscape's rich topological insights without leaving the current context, gaining access to drill-downs and actionable information for all displayed entities.

## View topology support in Dynatrace apps

You can trigger View topology modal from the entity details in any Dynatrace application, either via an explicit intent or through the **Open with** option after selecting the entity.

Some nodes might not have any edges to other nodes in your environment. If no edges exist in [**Smartscape on Grail**](/docs/platform/grail/smartscape-on-grail "Learn about Smartscape on Grail features and how Smartscape uses the power of DQL."), the topology view will only contain the selected node.

You can find some examples of triggering the View topology modal below:

* [![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape**](/docs/analyze-explore-automate/smartscape "Visualize the structure of your environments and understand relationships and dependencies between your service entities."): You can trigger the View topology modal directly from any entity in any [Smartscape view](/docs/analyze-explore-automate/smartscape/smartscape-views "Visualize your environment with customized Smartscape views to gain insight into relationships and dependencies between your services.").
* [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace."): You can trigger the View topology modal from a Smartscape node by selecting the **Show topology** action in the tooltip.
* [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](/docs/secure/threats-and-exploits "Understand, triage, and investigate detection findings and alerts."): You can trigger the View topology modal from the **Affected object** details within the app.

## Overview

The View topology modal offers two types of topology view:

* Vertical topology: provides a complete hierarchical visualization of all related entities for a selected node.
* Horizontal topology: focuses on directly connected upstream and downstream nodes.

The View topology modal allows you to seamlessly switch between both perspectives to gain a complete understanding of an entity's context. Both perspectives consist of the following components:

* Groups
* Nodes
* Edges

Components represent different relationships and node types depending on the view.

### Vertical topology

The vertical topology view shows a complete hierarchical visualization of all related entities for the focused node. It allows you to view relationships between the nodes, such as `runs_on` or `part_of`.

#### Group

In the vertical topology view, a group contains entities of the same type, such as Hosts and Kubernetes nodes.

#### Nodes

In the vertical topology, nodes can be divided into the following types:

* Focused node: your selected primary entity that's displayed at the center of the graph.
* Upstream nodes: entities the focused node is connected to by a `runs_on` or a `part_of` relationship. By default, these entities are displayed above the focused node.
* Downstream nodes: entities that are connected to the focused node by a `runs_on` or a `part_of` relationship. By default, these entities are displayed below the focused node.

#### Edges

Edges in vertical topology view represent relationships between nodes. The `runs_on` relationship is the most commonly displayed type, but other relationship types, such as `part_of` or `is_attached_to`, may also appear in this view.

### Horizontal topology

The horizontal topology view focuses on `calls` relationships between nodes, and showcases one level of connections in either direction.

#### Group

In the horizontal topology view, entities are divided into logical source and target groups:

* Source group: entities that call the focused node (`calls` relationship), displayed to the left.
* Target group: entities the focused node interacts with, displayed to the right.

#### Nodes

In horizontal topology, nodes can be divided into the following types:

* Focused node: your selected primary entity that's displayed at the center of the graph.
* Source nodes: entities calling the focused node, displayed to the left of the focused node.
* Target nodes: entities called by the focused node, displayed to the right of the focused node.

#### Edges

Edges represent the `calls` relationship between nodes and can provide clarity on communication pathways.

## Use cases

You can use ![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** View topology to:

* Understand the entity context and relationship between your services.
* Identify dependencies between entities in your environment.

## Best practice tips

To maximize your efficiency when using ![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** View topology, you can:

* Reference the legend to quickly view a summary of nodes and their types in the current topology.
* Drill down into any displayed entity directly from the topology view to analyze performance metrics, troubleshoot errors, or resolve failures.
* Use both vertical and horizontal topology views as a combined perspective to gain complete understanding of an entity's context and dependencies between your services.
* Trigger additional topology views from within the current view to continue exploring related entities and better understand the full scope of dependencies.

## Related topics

* [Smartscape](/docs/analyze-explore-automate/smartscape "Visualize the structure of your environments and understand relationships and dependencies between your service entities.")
* [Smartscape views](/docs/analyze-explore-automate/smartscape/smartscape-views "Visualize your environment with customized Smartscape views to gain insight into relationships and dependencies between your services.")

---

## analyze-explore-automate/smartscape/smartscape-modals/visual-resolution-path.md

---
title: Visual Resolution Path
source: https://www.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-modals/visual-resolution-path
scraped: 2026-02-17T05:05:45.502622
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

## analyze-explore-automate/smartscape/smartscape-modals.md

---
title: Smartscape modals
source: https://www.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-modals
scraped: 2026-02-18T05:57:37.979901
---

# Smartscape modals

# Smartscape modals

* Latest Dynatrace
* Overview
* 2-min read
* Published Jan 28, 2026

![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** modals extend the power of topological analytics beyond the ![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** app by providing intent add-on modals that deliver in-context insights regardless of which part of the Dynatrace platform you use. ![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** modals seamlessly integrate topological and relationship analytics into your workflows, ensuring you have the insights you need whenever you need them.

[### Visual Resolution Path

Use the Visual Resolution Path (VRP) add-on to access the problem resolution path directly from any Dynatrace app and gain insights into the problem and underlying problem event timeline without leaving your current context.](/docs/analyze-explore-automate/smartscape/smartscape-modals/visual-resolution-path "Access the problem resolution path directly from any Dynatrace app to gain insights into a problem and event timeline without leaving the current context.")[### View Topology

Visualize the topology around any selected entity to gain immediate insights on the relationships to other entities within your digital system.](/docs/analyze-explore-automate/smartscape/smartscape-modals/smartscape-view-topology "Visualize the topology around the selected entity to gain insights on service dependencies and relationships between the nodes.")

## Related topics

* [Smartscape](/docs/analyze-explore-automate/smartscape "Visualize the structure of your environments and understand relationships and dependencies between your service entities.")

---

## analyze-explore-automate/smartscape/smartscape-views/aws-ec2-ecosystem-overview.md

---
title: AWS EC2 ecosystem overview
source: https://www.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-views/aws-ec2-ecosystem-overview
scraped: 2026-02-18T05:56:49.796809
---

# AWS EC2 ecosystem overview

# AWS EC2 ecosystem overview

* Latest Dynatrace
* Explanation
* 5-min read
* Published Jan 28, 2026

**AWS EC2 Instance Ecosystem** provides a focused, hierarchical visualization of your EC2 instances and their surrounding resource ecosystem. This view enables you to understand how your EC2 instances are organized across regions, availability zones, and subnets, along with their relationships to attached EBS volumes, associated Lambda functions, and connected DynamoDB tables.

By presenting a clear structural hierarchy from region down to individual EC2 instances and their directly related resources, this view helps you quickly identify how your compute resources are distributed and connected, making it easier to troubleshoot issues, optimize instance placement, and ensure proper architectural design within your EC2 ecosystem.

![An example of Smartscape AWS EC2 ecosystem overview home page](https://dt-cdn.net/images/aws-ec2-ecosystem-overview-smartscape-1920-ba3b71044c.png)

## Constituent entities overview

**AWS EC2 Instance Ecosystem** breaks down your EC2 environment into clear, hierarchical layers to help you visualize its structure. The layers consist of:

* Nodes
* Groups

### Nodes and groups

Nodes, the highest level of the view, showcase AWS Regions. Each region contains Availability Zones, Lambda functions, and DynamoDB tables, with additional resources nested within the availability zones. The structure can be visualized as follows:

* AWS Region

  + AWS Availability Zone

    - AWS EC2 Subnet

      * AWS EC2 Instance

        + AWS Lambda Function
    - AWS EC2 Volume
  + AWS Lambda Function
  + AWS DynamoDB Table

Groups found on different hierarchy levels can contain entities of the same type or level. You can expand or collapse any group to improve visibility and focus on the relevant entities.

## Use cases

You can use the **AWS EC2 Instance Ecosystem** to:

* Visualize and understand the distribution of EC2 instances across regions, availability zones, and subnets to ensure proper high-availability configurations.
* Identify which resources are deployed in specific availability zones to assess potential single-point-of-failure risks.
* Review your subnet organization and EC2 placement to validate network segmentation and security zone configurations.
* Investigate infrastructure dependencies during troubleshooting to identify which resources might be affected by regional or zonal issues.
* Plan capacity and disaster recovery by understanding the full scope of resources within specific regions or availability zones.

## Best practice tips

To use the **AWS EC2 Instance Ecosystem** effectively, we recommend that you:

* Focus on specific areas by selecting a segment that defines your area of responsibility, such as specific regions, availability zones, or EC2 instances relevant to your team.
* Use the topology graph to verify that your EC2 instances, subnets, and availability zones are correctly organized and associated with their intended regions.
* Drill down into any region, availability zone, subnet, or EC2 instance to continue your exploration or investigation and access detailed health-relevant signals, metrics, events, and logs.
* Review the distribution of instances across availability zones to ensure your architecture maintains high availability and fault tolerance.

## Related topics

* [Smartscape](/docs/analyze-explore-automate/smartscape "Visualize the structure of your environments and understand relationships and dependencies between your service entities.")

---

## analyze-explore-automate/smartscape/smartscape-views/infrastructure-overview.md

---
title: Infrastructure overview
source: https://www.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-views/infrastructure-overview
scraped: 2026-02-17T21:25:37.776128
---

# Infrastructure overview

# Infrastructure overview

* Latest Dynatrace
* Explanation
* 5-min read
* Published Jan 28, 2026

**Infrastructure overview** provides a high-level visual representation of your physical infrastructure.

It focuses on the physical stack, showcasing key infrastructure entities such as hosts, processes, disks, and network interfaces. By visualizing the relationships and interdependencies between these entities, the **Infrastructure overview** delivers a comprehensive understanding of how the underlying components of your environment interact to support your workloads.

![An example of Smartscape Infrastructure overview](https://dt-cdn.net/images/infrastructure-overview-smartscape-1920-4dcf506dce.png)

## Constituent entities overview

### Nodes

In the **Infrastructure overview**, nodes represent physical components detected within your environment. These nodes are organized in a hierarchical structure that can be visualized as follows:

* Regions

  + Cloud regions / data centers

    - Hosts

      * Containers

        + Processes
      * Non-containerized processes
      * Disks
      * Network interfaces

Each level showcases specific infrastructure components and helps you traverse from the highest-level view of your environment, regions, down to individual processes within containers.

### Edges

In the **Infrastructure overview**, edges represent `calls` relationships between components. These connections can be visualized at varying levels of granularity:

* Host-to-Host calls: displays interactions between hosts in your environment.
* Process-to-Process calls: tracks communication at the most granular level and shows how individual processes interact across the infrastructure.

These relationships are aggregated, or "bubbled up", to higher levels in the hierarchy where possible. This provides a clearer, more concise visualization of the key dependencies within your infrastructure.

## Use cases

You can use **Infrastructure overview** to:

* Understand how your workloads are distributed by using the hierarchical structure of the view to drill down from regions to individual infrastructure components, such as containers and processes.
* Explore the relationships within containers to see how processes interact with each other by exploring the relationships within containers.
* Identify communication patterns, data flows, and potential bottlenecks at the infrastructure level by visualizing Host-to-Host calls.
* Identify problematic interactions or unexpected dependencies between processes, both within and across hosts by tracing process-level communication.
* Troubleshoot infrastructure issues.

## Best practice tips

To use **Infrastructure overview** effectively, we recommend that you:

* Focus on individual hosts or regions to identify performance bottlenecks, overloaded resources, or problematic dependencies that may impact your system.
* Thoroughly investigate non-containerized processes to pinpoint issues or dependencies that stem from processes running outside of containers, such as legacy applications or custom workloads.
* Actively use the pin the tooltip functionality on nodes for easy key metric access. Key metrics such as CPU, memory, or disk utilization, and can help you gain insights necessary to detect and resolve performance issues faster.
* Drill down into any nodes in the ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** app to continue your exploration of your infrastructure.

## Related topics

* [Smartscape](/docs/analyze-explore-automate/smartscape "Visualize the structure of your environments and understand relationships and dependencies between your service entities.")

---

## analyze-explore-automate/smartscape/smartscape-views/kubernetes-overview.md

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

---

## analyze-explore-automate/smartscape/smartscape-views/problem-graph.md

---
title: Problem graph
source: https://www.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-views/problem-graph
scraped: 2026-02-16T21:29:35.618649
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

---

## analyze-explore-automate/smartscape/smartscape-views/service-dependency-graph.md

---
title: Service dependency graph
source: https://www.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-views/service-dependency-graph
scraped: 2026-02-18T21:31:59.052070
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

---

## analyze-explore-automate/smartscape/smartscape-views/smartscape-on-grail-view.md

---
title: Smartscape on Grail view
source: https://www.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-views/smartscape-on-grail-view
scraped: 2026-02-18T05:49:44.693782
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

## analyze-explore-automate/smartscape/smartscape-views.md

---
title: Smartscape views
source: https://www.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-views
scraped: 2026-02-18T05:49:51.507984
---

# Smartscape views

# Smartscape views

* Latest Dynatrace
* Overview
* 2-min read
* Published Jan 28, 2026

![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** views enable you to visualize and analyze topology data with a range of ready-made, customized perspectives. Each view utilizes Dynatrace's comprehensive topological and relational data to deliver actionable insights into the complexities of contemporary digital systems, ensuring relevance to specific use cases.

Whether you're exploring service relationships, understanding infrastructure dependencies, or visualizing problem impact, ![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** ensures that you have the right lens to address your specific needs.

[### Smartscape on Grail view

Discover all entities and relationships in your environment and focus on what's relevant to you and your team.](/docs/analyze-explore-automate/smartscape/smartscape-views/smartscape-on-grail-view "Discover all entities and relationships in your environment and select relevant segments with the help of Grail.")[### Infrastructure overview

Gain insight into what components are running, how they're connected, and where the impact may spread.](/docs/analyze-explore-automate/smartscape/smartscape-views/infrastructure-overview "Visualize call-type relationships between components and gain insights into process dependencies and workload distribution.")[### Problem graph

Analyze problem impact and blast radius across your environment.](/docs/analyze-explore-automate/smartscape/smartscape-views/problem-graph "Use Problem graph to visualize and quickly identify problems and nodes that require immediate attention.")[### Service dependency graph

Discover how your services connect and communicate in real time.](/docs/analyze-explore-automate/smartscape/smartscape-views/service-dependency-graph "Visualize relationships between services in your environment to identify dependency chains and and uncover critical dependencies.")[### Kubernetes overview

Map your Kubernetes environments from clusters to components.](/docs/analyze-explore-automate/smartscape/smartscape-views/kubernetes-overview "Get a high-level overview of your Kubernetes environment to navigate dependencies and identify misconfigurations.")[### AWS EC2 ecosystem overview

Visualize your AWS EC2 ecosystem and resource relationships.](/docs/analyze-explore-automate/smartscape/smartscape-views/aws-ec2-ecosystem-overview "Visualize your AWS EC2 ecosystem and resource relationships.")

## Related topics

* [Smartscape](/docs/analyze-explore-automate/smartscape "Visualize the structure of your environments and understand relationships and dependencies between your service entities.")

---

## analyze-explore-automate/smartscape.md

---
title: Smartscape
source: https://www.dynatrace.com/docs/analyze-explore-automate/smartscape
scraped: 2026-02-18T21:35:49.841671
---

# Smartscape

# Smartscape

* Latest Dynatrace
* Overview
* 5-min read
* Published Jan 28, 2026

## Prerequisites

### Permissions

The following table describes the required permissions.

Permission

Description

storage:buckets:read

Necessary to read problems from 'dt.davis.problems'

storage:smartscape:read

Read data from Grail table "smartscape"

storage:events:read

Events permission is needed to query problems

storage:filter-segments:read

Permission to read filter segments

storage:metrics:read

Necessary to display entity metrics

storage:spans:read

Necessary to read segment variables

storage:logs:read

Necessary to read segment variables

storage:security.events:read

Necessary to read segment variables

storage:bizevents:read

Necessary to read segment variables

storage:entities:read

Necessary to read segment variables

10

rows per page

Page

1

of 1

## Get started

![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** is an interactive map of your digital ecosystem powered by [**Smartscape on Grail**](/docs/platform/grail/smartscape-on-grail "Learn about Smartscape on Grail features and how Smartscape uses the power of DQL."). Use it to visually analyze topology and relationships between all of your entities in real time with the help of customized ![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** views and modals.

![Get the full picture with a real-time representation of all your digital systems.](https://cdn.hub.central.dynatrace.com/hub/console/drafts/197/media/ScreenShot_Hub_-_Image_1.png)![Instant, domain-specific insights, with no configuration required.](https://cdn.hub.central.dynatrace.com/hub/console/drafts/114/media/Smartscape_Hub_-_Image_2.png)![Discover hidden patterns through multidimensional, visual analytics.](https://cdn.hub.central.dynatrace.com/hub/console/drafts/114/media/Smartscape_Hub_-_Image_3.png)![Assess and visualize impact and blast radius of problems.](https://cdn.hub.central.dynatrace.com/hub/console/drafts/114/media/Smartscape_Hub_-_Image_4.png)

1 of 4Get the full picture with a real-time representation of all your digital systems.

## Concepts

Go through the following topics to gain a better understanding of [Smartscape concepts](/docs/analyze-explore-automate/smartscape/smartscape-concepts "Learn about Smartscape-specific concepts and UI capabilities.") and ![Smartscape](https://dt-cdn.net/images/smartscapes-256-eb41c7cddc.png "Smartscape") **Smartscape** features.

[01Smartscape concepts

* Explanation
* Learn about Smartscape-specific concepts and UI capabilities.](/docs/analyze-explore-automate/smartscape/smartscape-concepts)[02Smartscape modals

* Overview
* Use Smartscape modals to visualize your environment in any Dynatrace app and gain insights into problem resolution and service dependencies](/docs/analyze-explore-automate/smartscape/smartscape-modals)[03Smartscape views

* Overview
* Visualize your environment with customized Smartscape views to gain insight into relationships and dependencies between your services.](/docs/analyze-explore-automate/smartscape/smartscape-views)

## Use cases

* **Smartscape on Grail:** Explore your entire digital ecosystem end-to-end with a unified model that connects everything from services to infrastructure for a complete architectural context.
* **Clouds overview:** Gain a unified, real-time topology of AWS EC2 instances and surrounding components to analyze security posture, optimize costs, and validate architecture.
* **Kubernetes:** Gain full-stack visibility by mapping clusters, namespaces, and components. Detect misconfigurations and troubleshoot issues across workloads.
* **Problems Graph:** Instantly understand root cause and blast radius by mapping anomalies to impacted entities and dependency chains.
* **Service Dependency Graph:** Trace call flows, isolate performance hotspots, and uncover unexpected communication paths for better service reliability.
* **Infrastructure:** Navigate a real-time map of hosts, VMs, and network relationships to validate architecture, diagnose infrastructure-driven issues, and spot bottlenecks or drift patterns.

---
