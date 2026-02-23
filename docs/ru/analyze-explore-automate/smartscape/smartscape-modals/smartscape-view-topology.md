---
title: View topology
source: https://www.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-modals/smartscape-view-topology
scraped: 2026-02-23T21:35:58.657793
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