---
title: Data Explorer quick start
source: https://docs.dynatrace.com/managed/analyze-explore-automate/explorer/explorer-quick-start
scraped: 2026-05-12T11:12:56.792181
---

# Data Explorer quick start

# Data Explorer quick start

* 6-min read
* Published Oct 28, 2021

You're in the right place if you want to see what Data Explorer can do and learn a little about writing your own queries.

You have two options here:

* [Start with a template](#templates)âAn easy intro
* [Start from scratch](#from-scratch)âA little harder

## Start with a template

Starting with Dynatrace version 1.251, Data Explorer opens with a **Start with a template** section. This is the fastest and easiest way to get up and running with Data Explorer.

Don't be afraid to experiment. You can't break anything.

If you need to start again, navigate away from Data Explorer (select another app) and then go back to display the **Start with a template** section again.

To get started with a template

1. Go to **Data Explorer**.
2. In the **Start with a template** section, select a template.

   When you select a template, Dynatrace automatically fills in the query definition, configures the visualization settings, and runs the query.
3. Hover over visualization elements to see tooltips.
4. Select visualization elements to access drilldown actions.
5. Experiment with the query definition. After you make a change, select **Run query** to see what happens.
6. Experiment with the **Settings** panel on the right. Tweak some settings and see what happens.
7. Optional [Dashboards Classic](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic."): When you come up with something you like, select **Pin to dashboard** to add the query to a dashboard. The list of dashboards is searchable: select in the list and start typing to filter the list, and then select the dashboard from the filtered list.

   * If you don't have a dashboard, just select **Create new dashboard** when the **Where do you want to pin to?** message pops up.
   * You can pin multiple versions of your work to your dashboard so you can see them side by side.

![Data Explorer - templates](https://dt-cdn.net/images/sample-templates-section-1285-7b25cb25e5.png)

Data Explorer - templates

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

     How to select a metric

     When you browse the list of metrics

     + You can type or paste a metric name directly into the box to find all matching metrics. In this example, there are multiple matches. We select the metric in the Host category to add it to our query.

       ![Data Explorer: metric selector: type and select](https://dt-cdn.net/images/metric-selector-metric-type-471-10a8a83a2e.png)

       Data Explorer: metric selector: type and select

     + If you have favorited any metrics in the [Metrics browser](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser.") browser, those metrics are displayed at the top of the list in the metric selector.

       ![Data Explorer: metric selector: favorites](https://dt-cdn.net/images/metric-selector-favorites-475-665c98b195.png)

       Data Explorer: metric selector: favorites
     + You can select a metric category to focus the list of metrics.

       ![Data Explorer: metric selector: categories](https://dt-cdn.net/images/metric-selector-categories-476-5cbd27551a.png)

       Data Explorer: metric selector: categories

     + When you hover over any metric in the list, a side panel displays details about that metric.

       ![Data Explorer: metric selector: metric details](https://dt-cdn.net/images/metric-selector-metric-details-964-cd2f59a371.png)

       Data Explorer: metric selector: metric details

       To see more information about that metric, select **View all metric information**. This opens the [Metrics browser](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser.") in a new tab (so you don't lose your work in Data Explorer) with lots of useful details about the selected metric.
   * Choose an aggregation (for example, `Average`, `Minimum`, or `Maximum`)
   * Select **Split by** dimensions. In this example (`CPU usage %`), we split by host to see CPU usage per host.
   * Specify **Filter by** criteria as needed. In this example, we leave it empty.

   For details on building a query, see [Query components and concepts](/managed/analyze-explore-automate/explorer#query-components-and-concepts "Query for metrics and transform results to gain desired insights.") and [Examples](/managed/analyze-explore-automate/explorer#examples "Query for metrics and transform results to gain desired insights.").
3. Optional To review or edit the code for your query, turn on **Advanced mode**, which is the [advanced query editor](/managed/analyze-explore-automate/explorer/explorer-advanced-query-editor "Build advanced queries using the Data Explorer advanced mode.").
4. Add and delete metrics as needed.

   * A query can have up to 10 rows.
   * To add a new empty row, select **Add metric** and then repeat the previous step to define that row.
   * To reorder metrics, select and drag the metric to a new position in the list of metrics.

     ![Drag metric to reorder list](https://dt-cdn.net/images/data-explorer-drag-metric-69-84144c5cd2.png)

     Drag metric to reorder list

     + A query's metrics are rendered in order from top to bottom, so the last one is rendered on top of the others.
     + Note that the order of the metrics is also updated in the **Settings** section in the side panel.
     + Rerun the query to see your changes.
   * To make a copy of a metric that you have already added to the query, select  > **Duplicate** and then edit the copy as needed.

     ![Metric More menu ](https://dt-cdn.net/images/data-explorer-metric-more-menu-74-1b3f17af8b.png)

     Metric More menu
   * To enable or disable a metric, select the eye button .

     ![Data Explorer: enable or disable a metric](https://dt-cdn.net/images/data-explorer-metric-enable-disable-80-d4980f418d.png)

     Data Explorer: enable or disable a metric
   * To delete a metric, select  > **Delete**.
5. Optional To add or remove metric transformations for a row, select the transformations (**+**) button and then select or clear checkboxes as needed.

   ![Metric Plus button](https://dt-cdn.net/images/data-explorer-metric-plus-button-46-3104fd992d.png)

   Metric Plus button
6. Select **Run query** to take a first look at the visualization. The **Run query** button displays the status of the displayed results:

   ![Data Explorer: Run query button: last run time](https://dt-cdn.net/images/data-explorer-run-button-last-run-293-a37ea8a71f.png)

   Data Explorer: Run query button: last run time

   ![Data Explorer: Run query button: unapplied changes](https://dt-cdn.net/images/data-explorer-run-button-unapplied-472-7f10360ebb.png)

   Data Explorer: Run query button: unapplied changes
7. Use the **Settings** panel to configure your visualization.

   * The visualization is updated with each change.
   * Choose from several visualization types:

     + [Graph](/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-graph "Configure and use a graph visualization in Data Explorer and pin it to your dashboards as a graph tile.")
     + [Stacked column](/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-stacked-column "Configure and use a stacked column visualization in Data Explorer and display it on your dashboards.")
     + [Stacked area](/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-stacked-area "Configure and use a stacked area visualization in Data Explorer and display it on your dashboards.")
     + [Pie](/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-pie "Configure and use a pie/doughnut visualization in Data Explorer and display it on your dashboards.")
     + [Single value](/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-single-value "Configure and use a single-value visualization in Data Explorer and display it on your dashboards.")
     + [Table](/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-table "Configure and use a table visualization in Data Explorer and display it on your dashboards.")
     + [Top list](/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-top-list "Configure a top-list visualization in Data Explorer and display it on your dashboards.")
     + [Heatmap](/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-heatmap "Configure and use a heatmap visualization in Data Explorer and pin it to your dashboards as a heatmap tile.")
     + [Honeycomb](/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-honeycomb "Configure and use a honeycomb visualization in Data Explorer and display it on your dashboards.")

When you are satisfied with your visualization, you can use it within Data Explorer immediately or pin it to a dashboard for future use.

### Use the visualization in Data Explorer

Visualization elements are active. For example:

* To see details in tooltips, hover over visualization elements
* To drill down from a problematic (red) element, select it.
* To hide or show a visualization element, select the corresponding label in the visualization legend

When you're done using your visualization (for now, anyway), you need to decide whether to discard it or save it.

* To discard your visualization (and the query that generated it), just navigate away from Data Explorer.
* To save your visualization and query for future use, you need to pin the visualization to a dashboard. See below.

### Pin the visualization to a dashboard

To save the visualization as a dashboard tile, select **Pin to dashboard**.

To return from the dashboard to Data Explorer with the visualization open for viewing and editing, open the menu in the upper-right corner of the tile and select **Configure tile in Data Explorer**. Now two buttons are displayed in the **Results** section of Data Explorer:

* **Save changes to dashboard**âsaves the visualization to the same tile and dashboard you used to open Data Explorer. If you have made any changes, they will update the tile on your dashboard.
* **Pin to dashboard**âsaves the visualization as a tile on a different dashboard. You might want to pin the same visualization (perhaps with filtering differences) to various dashboards.

For details about pinning tiles to dashboards, see [Pin tiles to your dashboard](/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Learn to pin tiles to your dashboards.").

## What's next?

If you're ready for the technical details, see:

* [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.")âlearn the details of query construction
* [Data Explorer Advanced mode query editor](/managed/analyze-explore-automate/explorer/explorer-advanced-query-editor "Build advanced queries using the Data Explorer advanced mode.")âlearn how to edit queries om **Advanced mode**