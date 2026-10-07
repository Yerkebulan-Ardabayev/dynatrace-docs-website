---
title: Get started with Data Explorer
source: https://docs.dynatrace.com/managed/analyze-explore-automate/explorer/explorer-quick-start
---

# Get started with Data Explorer

# Get started with Data Explorer

* Tutorial
* 6-min read
* Updated on Oct 01, 2026

In this tutorial, you build a metric visualization in Data Explorer and pin it to a dashboard, and you learn how to define, run, and save a query.

You have two options here:

* [Start with a template](#templates): Begin with a predefined query
* [Start from scratch](#from-scratch): Create a query without a template

## Start with a template

Data Explorer opens with a **Start with a template** section. Use this section to begin working with Data Explorer.

To start again, select another app, then reopen Data Explorer to display the **Start with a template** section.

To get started with a template, complete the following steps.

1. Go to **Data Explorer**.
2. In the **Start with a template** section, select a template.

   When you select a template, Dynatrace automatically fills in the query definition, configures the visualization settings, and runs the query.
3. Hover over visualization elements to see tooltips.
4. Select visualization elements to access drilldown actions.
5. Experiment with the query definition. After you make a change, select **Run query** to see what happens.
6. Experiment with the **Settings** panel on the right. Tweak some settings and see what happens.
7. Optional [Dashboards](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic."): When you come up with something you like, select **Pin to dashboard** to add the query to a dashboard. Select the list, enter text to filter it, and then select the dashboard from the filtered list.

   * If you don't have a dashboard, select **Create new dashboard** when the **Where do you want to pin to?** message appears.
   * You can pin multiple versions of your work to your dashboard so you can see them side by side.

![Data Explorer - templates](https://dt-cdn.net/images/sample-templates-section-1285-7b25cb25e5.png)

Data Explorer - templates

The **Start with a template** section lets you begin a query from a predefined template.

If you're ready to start exploring a little more, try starting from scratch.

## Start from scratch

Use this procedure to get hands-on experience with Data Explorer.

In this walkthrough, you'll:

* Create a simple metric visualization from scratch
* Use the visualization directly in Data Explorer
* Pin the visualization to a dashboard as a tile

### Create a visualization from scratch

1. Go to **Data Explorer**.
2. On the **Build** tab, add a metric to your query.

   * Select a metric such as `CPU usage %` (`builtin:host.cpu.usage`).

   When you browse the list of metrics:

   * Enter a metric name into the box to find matching metrics. When multiple matches appear, select the metric in the Host category to add it to your query.

     ![Data Explorer: metric selector: enter and select](https://dt-cdn.net/images/metric-selector-metric-type-471-10a8a83a2e.png)

     Data Explorer: metric selector: enter and select

     Enter a metric name and select the matching metric from the metric selector.
   * Find metrics that you favorited in [Metrics browser](/managed/analyze-explore-automate/metrics-browser "Find Metrics browser reference information for filters, metric details, and custom metric metadata, and configure metadata for custom metrics.") at the top of the metric-selector list.

     ![Data Explorer: metric selector: favorites](https://dt-cdn.net/images/metric-selector-favorites-475-665c98b195.png)

     Data Explorer: metric selector: favorites

     Favorited metrics appear at the top of the metric-selector list.
   * Select a metric category to focus the list of metrics.

     ![Data Explorer: metric selector: categories](https://dt-cdn.net/images/metric-selector-categories-476-5cbd27551a.png)

     Data Explorer: metric selector: categories

     Select a metric category to focus the list of available metrics.
   * When you hover over any metric in the list, a side panel displays details about that metric.

     ![Data Explorer: metric selector: metric details](https://dt-cdn.net/images/metric-selector-metric-details-964-cd2f59a371.png)

     Data Explorer: metric selector: metric details

     The metric-details panel shows information about the selected metric.

   To see more information about that metric, select **View all metric information**. Selecting **View all metric information** opens [Metrics browser](/managed/analyze-explore-automate/metrics-browser "Find Metrics browser reference information for filters, metric details, and custom metric metadata, and configure metadata for custom metrics.") in a new tab, where you can view details about the selected metric without losing your work in Data Explorer.

   * Choose an aggregation (for example, `Average`, `Minimum`, or `Maximum`)
   * Select **Split by** dimensions. For example, select host for `CPU usage %` to view CPU usage per host.
   * Select **Filter by** criteria as needed. Leave the criteria empty in this example.

   For details on building a query, see [Query components and concepts](/managed/analyze-explore-automate/explorer/metric-query-components#query-components-and-concepts "Look up Data Explorer query components, query editor commands, auto-extended filters, query examples, and query limits.") and [Examples](/managed/analyze-explore-automate/explorer/metric-query-components#examples "Look up Data Explorer query components, query editor commands, auto-extended filters, query examples, and query limits.").
3. Optional To review or edit the code for your query, turn on **Advanced mode**, which is the [advanced query editor](/managed/analyze-explore-automate/explorer/explorer-advanced-query-editor "Learn how to build and edit advanced Data Explorer queries, use metric transformations and expressions, and compare metrics across timeframes.").
4. Add and delete metrics as needed.

   * A query can have up to 10 rows.
   * To add a new empty row, select **Add metric** and then repeat the previous step to define that row.
   * To reorder metrics, select and drag the metric to a new position in the list of metrics.

     ![Drag metric to reorder list](https://dt-cdn.net/images/data-explorer-drag-metric-69-84144c5cd2.png)

     Drag metric to reorder list

     Drag a metric to change its position in the query.

     Metrics render from top to bottom, with the last metric on top. Rerun the query to view the reordered metrics.
   * To make a copy of a metric that you have already added to the query, select  > **Duplicate** and then edit the copy as needed.

     ![More menu for a metric, showing Duplicate and Delete actions](https://dt-cdn.net/images/data-explorer-metric-more-menu-74-1b3f17af8b.png)

     More menu for a metric, showing Duplicate and Delete actions

     Use the More menu to duplicate or delete a metric.
   * To enable or disable a metric, select the eye button .

     ![Data Explorer: enable or disable a metric](https://dt-cdn.net/images/data-explorer-metric-enable-disable-80-d4980f418d.png)

     Data Explorer: enable or disable a metric

     Select the eye button to enable or disable a metric.
   * To delete a metric, select  > **Delete**.
5. Optional To add or remove metric transformations for a row, select the transformations (**+**) button and then select or clear checkboxes as needed.

   ![Transformations button for a metric row](https://dt-cdn.net/images/data-explorer-metric-plus-button-46-3104fd992d.png)

   Transformations button for a metric row

   Select the transformations button to add or remove transformations for a metric row.
6. Select **Run query** to take a first look at the visualization. The **Run query** button displays the status of the displayed results:

   ![Data Explorer: Run query button: last run time](https://dt-cdn.net/images/data-explorer-run-button-last-run-293-a37ea8a71f.png)

   Data Explorer: Run query button: last run time

   The **Run query** button shows the time when the displayed results last ran.

   ![Data Explorer: Run query button: unapplied changes](https://dt-cdn.net/images/data-explorer-run-button-unapplied-472-7f10360ebb.png)

   Data Explorer: Run query button: unapplied changes

   The **Run query** button indicates when the query has unapplied changes.
7. Use the **Settings** panel to configure your visualization.

   * Each settings change updates the visualization.
   * For an overview of visualization types, see [Visualizations and tiles](/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles "Learn how to configure and use visualizations in Data Explorer and display them as tiles to your dashboards.").

After you finish the visualization, use it within Data Explorer or pin it to a dashboard for future use.

### Use the visualization in Data Explorer

Visualization elements are active. For example:

* To see details in tooltips, hover over visualization elements.
* To drill down from a problematic (red) element, select it.
* To hide or show a visualization element, select the corresponding label in the visualization legend.

When you're done using your visualization (for now, anyway), you need to decide whether to discard it or save it.

* To discard your visualization and its query, navigate away from Data Explorer.
* To save your visualization and query for future use, you need to pin the visualization to a dashboard. See below.

### Pin the visualization to a dashboard

To save the visualization as a dashboard tile, select **Pin to dashboard**.

To return to Data Explorer with the visualization open, open the tile menu and select **Configure tile in Data Explorer**. Two buttons then appear in the **Results** section.

* **Save changes to dashboard** saves the visualization to the same tile and dashboard you used to open Data Explorer. If you have made any changes, they will update the tile on your dashboard.
* **Pin to dashboard** saves the visualization as a tile on a different dashboard. You might want to pin the same visualization (perhaps with filtering differences) to various dashboards.

For instructions, go to [Pin a tile to a dashboard](/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Learn to pin tiles to your dashboards.").

## What's next

To write queries directly in the metric selector syntax, see [Write queries in advanced mode](/managed/analyze-explore-automate/explorer/explorer-advanced-query-editor "Learn how to build and edit advanced Data Explorer queries, use metric transformations and expressions, and compare metrics across timeframes.").

## Related topics

* [Data Explorer query reference](/managed/analyze-explore-automate/explorer/metric-query-components "Look up Data Explorer query components, query editor commands, auto-extended filters, query examples, and query limits.")