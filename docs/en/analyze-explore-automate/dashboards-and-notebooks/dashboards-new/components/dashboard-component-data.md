---
title: Add data to a dashboard
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-data
scraped: 2026-02-15T08:55:00.736729
---

# Add data to a dashboard

# Add data to a dashboard

* Latest Dynatrace
* How-to guide
* 10-min read
* Updated on May 27, 2025

This page describes how to add data with a Grail query, and how to specify a custom timeframe and a segment.

The fastest and easiest way to explore your data is with our new [Explore](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data "Explore your data with our point-and-click interface.") tiles and sections. In a few seconds, you can find and analyze your logs, metrics, or business events. No DQL required!

Deprecated: `dt.entity.*` fields

If you see the following message:

`The dt.entity.* fields are deprecated. Please use dt.smartscape.* fields instead.`

we recommend that you use an equivalent `dt.smartscape.*` field instead.

The deprecated `dt.entity.*` fields will eventually be removed.

## Add data

To Query Grail

1. In the upper-right of the dashboard, select  **Add** >  **DQL**.

   Keyboard shortcut: **Shift**+**D**

   ![Dashboards: Add tile button (Plus)](https://dt-cdn.net/images/updated-dashboards-add-tile-button-481-c21ba8f200.png)

   A configuration side panel opens on the right to display two tabs:

   * **Data**
   * **Visual**
2. On the **Data** tab, use the [Dynatrace Query Language (DQL)](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") to define your query.
3. Select **Run** to execute the query.
4. On the **Visual** tab, choose a [visualization](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.") format for your results.

   * means the visualization type is unavailable for your query.
5. Under the **Visualization** selector, expand the options sections to adjust visualization settings as needed.
6. Close the side panel when you're done.

   If you want to return to these settings, select your tile to display them.

## Specify a custom timeframe

To specify a custom timeframe in a dashboard tile

1. Edit the tile.
2. In the edit panel, turn on **Custom timeframe**.
3. Select the timeframe to apply to the selected tile.

   This timeframe overrides the dashboard timeframe set in the upper-right corner of the dashboard. Using this method, a dashboard can have multiple tiles, where each tile has its own timeframe.

You can also specify a custom timeframe in a data tile's DQL query. If you use this method (with a timeframe specified in the query), the above UI setting is disabled and the timeframe specified in the query is used.

Example timeframe specification in DQL:

```
fetch [recordtype], from:now() - 2h



| ....
```

For details on specifying a timeframe in DQL, see [Specify timeframe](/docs/platform/grail/dynatrace-query-language/dql-guide#specifytimeframe "Find out how DQL works and what are DQL key concepts.") in the DQL documentation.

## Select segments

To filter data, you can specify segments at two levels: dashboard and tile. Tile-level segment selections override dashboard-level segment selections.

Should I use segments or variables?

#### Segments

Use segments when you want to reuse them across dashboards. For example, use segments for recurring filters such as for your Kubernetes clusters, namespaces, workloads, or pods. Segments automatically apply on top of the queries of your tiles/sections, so you donât need to reference them within.

#### Variables

If you need more control over how a filter is applied, however, you might want to use variables.

* Variables allow you to fully control the underlying query or within your Explore section or tile, determining where and how they are applied. For example, you can specify how they connect with other filters applied (**AND**, **OR**) and you can control which operator is used for your filter (such as `equals`, `contains`, `startsWith`, and `endsWith`).
* Additionally, use variables when you need fine-grained control over how filters are interdependent.

* For details on segments, see [Segments](/docs/manage/segments "Segments logically structure monitoring data in Grail and function as convenient filters for data that users are allowed to access based on permissions.")
* For a ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**-specific segments use case, see [Analyze monitoring data with segments](/docs/manage/segments/getting-started/segments-getting-started-analyze-monitoring-data "Learn how to analyze monitoring data more efficiently by using segments in Dashboards.")

To select tile-level segments

1. Display the dashboard.
2. Select the tile and then select  in the tile controls to edit the tile.
3. In the edit panel, turn on **Custom segments**.
4. In the **Custom segments** list, select a segment.  
   If the segment requires an additional value selection, select it now.
5. To add another segment, select  **Segment**. Repeat this step for each segment you want to add for the selected tile.
6. Select **Apply** to apply the selection and filter data on the tile.

   * The segment selector  now displays the name of the selected segment or, if you select more than one segment, the number of selected segments.
   * To change your segment selection, select  again, make your changes, and select **Apply**.
   * To manage segments in general (list, create, view, edit, delete), select  and then select the **Manage segments** link.

## Data example 1

```
fetch logs



| summarize loglines = count(), by:{`1m interval` = bin(timestamp, 1m), status}
```

## Data example 2

### Create two variables

In case you haven't created a variable yet, first see [Add a variable to a dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-variable#add-a-variable "Add variables to your Dynatrace dashboards.").

1. Select **Add variable** and define the first variable.

   * **Name:** `Hosts`
   * **Type:** `Query`
   * **Query:**

     ```
     fetch logs



     | summarize count(), by:{`dt.entity.host`}



     | limit 100



     | sort `count()`, direction:"descending"



     | fields `dt.entity.host`
     ```
   * **Multi-select:** turned on
2. Select **Add variable** and define the second variable.

   * **Name:** `Loglevel`
   * **Type:** `Query`
   * **Query:**

     ```
     fetch logs, from:now() - 2h



     | summarize  count(), by:{loglevel}



     | sort `count()`, direction:"descending"



     | fields loglevel
     ```
   * **Multi-select:** turned on

### Add data

Now add data while referencing your previously created variables `$LogLevel` and `$Hosts` so that you can later use the variable filters on top of your dashboard to filter the tile according to your selections.

```
fetch logs



| filter in (loglevel, {$Loglevel})



| limit 10
```

Select **Run query**.