---
title: Metrics browser
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-classic/metrics-browser
scraped: 2026-03-06T21:34:08.300543
---

# Metrics browser


* Classic
* How-to guide
* 5-min read
* Updated on Aug 01, 2022

Early Adopter

Go to **Metrics** to open the **Metrics** browser, which is a cool tool for browsing all metrics available in your monitoring environment and making a quick metric-specific visualization.

* Dashboards Classic: You can pin the visualization to a classic dashboard.

## Filter and sort the table

* By default, the table of metrics is filtered to show only those metrics that were last reported after the start of the selected timeframe (for example, `Last 2 hours`). Turn off **Only show metrics reported after the start of the selected timeframe** to see all metrics regardless of when they were last reported.
* Set **Favorites** to `Any`, `Yes`, or `No` to filter the table by metrics that you have favorited.

  + To favorite a metric, select the star in the **Favorite** column of the table. Favorited metrics sort to the top of the table by default.
  + To unfavorite a metric, select the star again.
* The filter bar (**Filtered by**) has the following options.

  + `Text`âSelect `Text`, enter a filter string, and then press **Enter** to list metrics that include the string in **Metric name**, **Metric key**, or **Description**.
  + `Tag`âSelect `Tag`, enter a filter string, and then select a matching tag to list metrics that include the tag in **Tags**.
  + `Unit`âSelect `Unit`, enter a filter string, and then select a matching metric unit (for example, `Percent`) to list metrics that have the selected **Unit**.
  + `Favorites`âSelect `Favorites` and then select `Yes` (to list only favorited metrics) or `No` (to list only metrics that are not favorited).
  + `Dimension`âSelect `Dimension`, enter a filter string, and then select a matching metric dimension (for example, `Host`) to list metrics that have the selected dimension.

    If you combine filters, they are ANDed together. For example, if you set `Dimension` to `Host` and set `Text` to `usage`, the metrics browser lists all metrics with the `Host` dimension that also include the string `usage` in the **Metric name**, **Metric key**, or **Description** field.
* Select column header **Favorite**, **Name**, or **Key** to sort by the selected column.
* Select ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") in the **Details** column to display metric details.

## Review metric details

Expand **Details** for any metric (row) in the table to see metric details and a visualization of the metric over the selected timeframe.

Metric details available in the 'Metrics browser'

## Order-of-magnitude notation

In this example, you can see values displayed in millions. This is order-of-magnitude notation (`7.5M` means "about 7.5 million" and not "exactly 7.5 million").

The order of magnitude here is selected automatically based on the size of the values. For example, the same metric measured over a shorter timeframe might be displayed in `k` values instead of `M`.

![Example order-of-magnitude values in the metrics browser.](https://dt-cdn.net/images/magnitude-metrics-browser-1284-02225955bf.png)

Examples of order-of-magnitude notation in Dynatrace:

For details, see Order-of-magnitude notation.

## Add metric to dashboard

Dashboards Classic

To add a metric to a classic dashboard

1. Select ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") in the **Details** column to display metric details.
2. Select **Create chart** to open the metric in Data Explorer.
3. Adjust the query and visualization settings as needed. For details, see Data Explorer or Data Explorer quick start.
4. Select **Pin to dashboard**.
5. Specify the target dashboard and metric title.
6. Select **Pin**.

## Metadata for custom metrics

To provide contextual information for custom metrics (for example, to define the unit of measurement, or to provide display names or descriptions or even information such as lower and upper value ranges or Davis-relevant information), you can create metric metadata per metric key.

Once this information is provided, it becomes part of the metrics descriptor and can be queried via the API and used in the Metrics Browser and Data Explorer.

* Providing metadata via Settings 2.0 is available only for custom/schemaless metrics, not for built-in/code-registered metrics.
* The metadata provided for a specific metric key exists side-by-side with the metric time series itself. You can even create the metric metadata before you ingest datapoints for the first time.

### Configuration via API

Metric metadata is fully configurable via API. For details, see Custom metric metadata.

### Configuration via web UI

To configure metric metadata for custom metrics via the web UI

1. Go to **Metrics**.
2. Select ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") in the **Details** column to display metric details.
3. Select **Edit metadata**.  
   If you don't see an **Edit metadata** button in the expanded row, you haven't selected a custom metric.
4. On the **Metric metadata** page, edit the metadata for the selected metric.  
   If the page displays a lock, you don't have the necessary write permissions to edit the selected metric's metadata.

   * **Display name**âEnter a human-friendly name for the metric.
   * **Description**âEnter a free-form description of the metric: how it is measured, etc.
   * **Unit**âSelect a unit from the list.
   * **Metric properties**

     + **Minimum value**âThe lower boundary of the metric.
     + **Maximum value**âThe upper boundary of the metric.
     + **Root cause relevant**âA root-cause relevant metric represents a strong indicator for a faulty component.
     + **Impact relevant**âAn impact-relevant metric is highly dependent on other metrics and changes because an underlying root-cause metric has changed.
     + **Value type**âThe type of the metric's value. You have these options:

       - `score`: A score metric is a metric where high values indicate a good situation, while low values indicate trouble. An example of such a metric is a success rate.
       - `error`: An error metric is a metric where high values indicate trouble, while low values indicate a good situation. An example of such a metric is an error count.
     + **Latency**âThe latency of the metric, in minutes. It indicates how long it takes before an ingested new metric data point is available in Dynatrace.
   * **Metric dimensions**âTo add a dimension, select **Add dimension** and enter the **Dimension key** and **Display name** for the dimension.
   * **Tags**âTo add a tag, select **Add tag** and enter the tag.
   * **Source entity type**âTo configure the entity type of the metric. Only editable if the metric is ingested via an API endpoint.
5. Select **Save changes** to save your edits.