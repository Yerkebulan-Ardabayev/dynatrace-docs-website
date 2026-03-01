---
title: Visual Resolution Path
source: https://www.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-modals/visual-resolution-path
scraped: 2026-03-01T21:23:36.258732
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