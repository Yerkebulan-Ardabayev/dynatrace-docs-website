---
title: Smartscape concepts
source: https://www.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-concepts
scraped: 2026-02-20T21:13:53.721689
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