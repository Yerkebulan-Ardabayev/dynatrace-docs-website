---
title: Multidimensional analysis for browser monitors in Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/multidimensional-analysis-for-browser-monitors
---

# Multidimensional analysis for browser monitors in Classic

# Multidimensional analysis for browser monitors in Classic

* Explanation
* 12-min read
* Updated on Feb 27, 2024

Dynatrace multidimensional analysis enables you to analyze browser monitor executions along multiple filtering dimensions.

The **Multidimensional analysis** page graphs [performance](#performance), [availability](#availability), and [error count](#errors) over the selected timeframe. You can select a [shorter analysis range](#analysis-range) and view individual data points in a scatter plot as well as in list format. The top of the page shows long-term (time series) data, followed by the [scatter plot](#scatter-plot) and individual [data points](#data-points) for up to 35 days from the current time. For data points, you can view [waterfall graphs](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/waterfall-graphs "How to analyze page resource downloads for browser monitors.") for actions and error details, if any.

From the scatter plot for performance values of individual data points, you can customize a wide range of page-level and resource-level performance metrics to create your own [calculated metrics](#calculated-metrics).

For each data point, you can see screenshots for all events; waterfall graphs are available for each action in the events that have timings.

You access the **Multidimensional analysis** page by drilling in from various points on the [Synthetic details page](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors "Analyze browser monitor and clickpath results on the Synthetic details page.").

![MDA for browser monitor performance](https://dt-cdn.net/images/syntheticmdaperformance1-1847-281a0cb232.png)

MDA for browser monitor performance

![MDA for browser monitor availability](https://dt-cdn.net/images/syntheticmdaavailability-1330-792a27f9a3.png)

MDA for browser monitor availability

![MDA for browser monitor errors](https://dt-cdn.net/images/syntheticmdaerrors-1316-a0e59c0e13.png)

MDA for browser monitor errors

## Analysis range

Whether you're looking at [availability](#availability), [performance](#performance), or [errors](#errors), the shaded area in the trend graph represents the analysis range, which is a subset of the global timeframe. Click elsewhere in the graph to move the analysis range; the [scatter plot](#scatter-plot) and list of [data points](#data-points) are filtered accordingly.

When you hover over the graph, you see arrow buttons ![Left and right arrows](https://dt-cdn.net/images/analysisarrowbuttons-49-c49391e1bc.png "Left and right arrows") that you can use to adjust the timeframe forward and backward in time, say from 10:30-12:30 to 08:30-10:30. Note that the size of the timeframe and analysis range remain the same.

Use the zoom buttons ![Zoom in and out](https://dt-cdn.net/images/analysiszoombuttons-49-744f9d7427.png "Zoom in and out") to adjust the timeframe by zooming in (**+** = shorter timeframe) or zooming out (**-** = longer timeframe). The size of the analysis range is correspondingly adjusted when you use the zoom buttons—you can also use the dropdown to change the analysis range.

![Analysis range](https://dt-cdn.net/images/analysisrange1-1666-a00a164538.png)

Analysis range

When there is a problem, solid red bars indicate the problem duration above the performance or availability graphs. Click a problem to select the problem duration as the analysis range. The [scatter plot](#scatter-plot) and [data points](#data-points) are filtered accordingly.

![Problem duration](https://dt-cdn.net/images/analysisrangeproblem-1688-38499191d4.png)

Problem duration

## Analyze availability

When you select **Analyze availability** on the [Synthetic details](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors#availability "Analyze browser monitor and clickpath results on the Synthetic details page.") page, you're directed to the **Multidimensional analysis** page, which shows an availability trend graph for all your monitoring locations.

![Analyze availability of all locations](https://dt-cdn.net/images/mdaavailabilityalllocations1-1663-add9daa0b0.png)

Analyze availability of all locations

When you select a specific location in the Synthetic details page, you're directed to the analysis page filtered by that location.

Multidimensional analysis for availability includes the option to filter the graph (and the corresponding [scatter plot](#scatter-plot) and [data points](#data-points)) to view information for **All locations** or a single monitoring location.

Hover over any point in the graph to see availability details for that point in time.

Red areas represent outages—the width of the area represents outage time while the height represents outage percentage. Outages are periods of time with error data points, or failures.

Solid red bars above the availability graph indicate the duration of availability problems (global outage or local outages). Click to select a problem bar and see the outage duration. [Data points](#data-points) for the problem duration are automatically displayed. Select the problem link to go to the problem details page.

![Availability problem in MDA](https://dt-cdn.net/images/mdaavailabilityproblem-329-39fe431e29.png)

Availability problem in MDA

* Monitor errors do not lead to [problems](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors#problems "Analyze browser monitor and clickpath results on the Synthetic details page.") if they don't violate your [availability thresholds](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors#outage-handling "Learn about configuring browser monitors and clickpaths.") or if you haven't enabled thresholds.
* Whether or not you see problems in the Dynatrace web UI and receive alert notifications during maintenance windows depends on how you [configure the maintenance windows](/managed/analyze-explore-automate/notifications-and-alerting/maintenance-windows/define-maintenance-window "Create maintenance windows and define their scope.").
* [Maintenance windows may be excluded from availability calculations](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations#m-windows-availability "Understand Synthetic Monitoring Classic metric calculations.") by applying a global setting.

## Analyze performance

You can access the **Multidimensional analysis** page for performance data from the [Synthetic details](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors "Analyze browser monitor and clickpath results on the Synthetic details page.") page in a few different ways. Your [default key performance metric selections](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors#kpm "Learn about configuring browser monitors and clickpaths.") carry over to the analysis page—you can, however, change them ([see below](#mda-performance)).

* Select [**Analyze performance**](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors#performance "Analyze browser monitor and clickpath results on the Synthetic details page.") to view the performance trend for all your monitoring locations. Your event-type selection from the details page (events with load actions, events with XHR actions, or all events) carries over to the **Multidimensional analysis** page. The resulting performance graph is split by event. The metric displayed depends on your event-type selection—**Total duration** for all events, and your selected key performance metrics for events with load or XHR actions.

  ![Analyze performance by event type](https://dt-cdn.net/images/mdaperformanceactiontype-1520-1916a1b752.png)

  Analyze performance by event type
* Select a specific location on the details page to view performance analysis filtered by that location.
* Select **Analyze** next to an event in the [Synthetic events and actions card](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors#events-actions "Analyze browser monitor and clickpath results on the Synthetic details page.") to see a graph for that particular event across all locations. The action type, for example, **Load actions**, is automatically selected. The performance graph is automatically split by metric.

  ![Analyze performance one event](https://dt-cdn.net/images/mdaperformanceoneevent-1512-9b501c5761.png)

  Analyze performance one event

Hover over any point in the graph to see the performance of the key performance metrics for that point in time.

Solid red bars above the performance graph indicate the duration of problems (threshold violations or availability outages). Click to select a problem bar and see its duration. [Data points](#data-points) for the problem duration are automatically displayed. Select the problem link to go to the problem details page.

![Performance problem in MDA](https://dt-cdn.net/images/mdaperformanceproblem1-404-4314be9617.png)

Performance problem in MDA

### Multidimensional analysis of performance

When you view performance over a selected [analysis range](#analysis-range), filters enable you to graph performance and filter the corresponding [scatter plot](#scatter-plot) and [data points](#data-points) along multiple dimensions:

![MDA filters for performance](https://dt-cdn.net/images/mdafiltersperformance-807-084f15bd3a.png)

MDA filters for performance

* **Location**—select all locations or an individual monitor location.
* **Action type**—view performance for load actions, XHR actions, custom actions, or all actions.
* **Performance metric**—this list shows the same [key performance metrics](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors#kpm "Learn about configuring browser monitors and clickpaths.") available in monitor settings, for which performance data is captured out of the box. While the [Synthetic details](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors "Analyze browser monitor and clickpath results on the Synthetic details page.") page graphs one key performance metric per action type, the **Multidimensional analysis** page offers all available metrics per action type.

  + When you filter for **All actions** in the trend, you only have the option of viewing **Total duration**.
  + When you filter for **Load actions** or **XHR actions** in the trend, **Total duration** is not available. This metric is only applicable to the performance of a monitor or events as a whole, not for action types within events.
* **Event**—select all or a specific Synthetic script event. You can only choose an event with timings from this list; events with no timing data are grayed out.
* **Split by**—select **Location**, **Action type**, **Metric**, or **Event**. When you choose a splitting criterion, the corresponding list is grayed out.

  ![Performance MDA splitting factor](https://dt-cdn.net/images/mdasplitby-811-2b18640f01.png)

  Performance MDA splitting factor

### Scatter plot

While the trend graph at the top of the page can show aggregated data, the scatter plot shows the performance for every data point in the analysis range. The scatter plot always plots performance, regardless of whether you opt to analyze [performance](#performance), [availability](#availability), or [errors](#errors) on the **Multidimensional analysis** page.

Your action-type selection (load, XHR, or all events) from the Synthetic details page carries over to the scatter plot. The scatter plot shows the default key performance metrics (specified in [monitor settings](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors#kpm "Learn about configuring browser monitors and clickpaths.")) for load and XHR actions; if you choose **All events** in the Synthetic details page, the scatter plot shows **Total duration**.

The filters you choose at the top of the page for multidimensional analysis of performance affect the scatter plot. For example, in the image below, the **Location**, **Action type**, **Performance metric**, and **Event** selections from the trend graph carry over to the scatter plot. (Choosing **All actions** in the trend graph defaults to **Load actions** in the scatter plot.)

![Scatter plot filters](https://dt-cdn.net/images/scatterplotfilters-1496-3bfad65ab4.png)

Scatter plot filters

The scatter plot also has its own independent filter for performance metrics, allowing you to view different metrics in the trend graph and scatter plot. The scatter plot metric filter offers more choices for page-level as well as resource-level metrics, which you can customize to create your own [**calculated metrics**](#calculated-metrics).

You can filter the scatter plot just for error data points (select **Error** > **Yes**), a specific error (**Error codes**), **Location**, Synthetic script **Event**, or **Request**. These filters are independent of the trend graph filters. The **Request** filter shows every request from every action and is meant to be used with the [waterfall graph](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/waterfall-graphs "How to analyze page resource downloads for browser monitors."). When analyzing an individual resource request in a waterfall, select **Analyze over time** to view the resource's performance across data points in the scatter plot.

![Scatter plot filters](https://dt-cdn.net/images/scatterplotfilters3-1499-a38e7e64f9.png)

Scatter plot filters

## Calculated metrics

Besides the [key performance metrics](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors#kpm "Learn about configuring browser monitors and clickpaths.") that you can select as the default display metrics for load and XHR actions, Dynatrace offers and plots several other page- and resource-level metrics (see also [Waterfall graphs](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/waterfall-graphs "How to analyze page resource downloads for browser monitors.")). These metrics are all listed in the **Analyze** list for [scatter plots](#scatter-plot).

While up to 35 days of historical data is always available for key performance metrics, you can also capture [long-term data](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods "Review default and configurable retention periods for service, RUM Classic, synthetic, Log Monitoring, metric, diagnostic, and security data in Dynatrace Managed.") for your customizations of any other metric by creating a calculated metric. Time series data for the calculated metric is available from the point of creation onward.

Select your metric and apply any desired filters in the scatter plot, then select **Create metric**. Optionally, enable the splitting factor in the metric creation dialog box. You can edit the **Metric name** and **Metric key**. By default, the metric key reflects the metric name and includes the monitor name. Once you create a calculated metric, the metric name, key, and configuration cannot be edited.

You can create up to 100 calculated metrics per monitor and up to 500 per monitoring environment. Note that calculated metrics are only available for the specific browser monitor for which they were created (for example, you cannot use a calculated metric created in one monitor for charting another monitor).

Notes on metrics

* **Total duration** is a monitor- or event-level metric and is not available for specific action types (load, XHR).
* The paint-focused **First paint**, **First contentful paint**, and **Largest contentful paint** metrics are applicable only to load actions.
* You can fine-tune **Visually complete calculation** by controlling various thresholds and timeouts as well as excluding specific elements from the calculation. You can set these properties in browser monitor settings: **Advanced setup** > **Enable custom RUM JavaScript settings** > **Configure parameters for Visually complete and Speed index calculation**.
* Some metrics or metric dimensions are not supported for creating calculated metrics. In such cases, you either see a message when you attempt to create a metric or the splitting factor is grayed out.

![Create a calculated metric](https://dt-cdn.net/images/createcalculatedmetric-1660-6bd30535bd.png)

Create a calculated metric

We recommend creating a calculated metric for those metrics that are not already offered as [key performance metrics](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors#kpm "Learn about configuring browser monitors and clickpaths.") in browser monitor settings.

We recommend that your metric name reflect any splits and filters so it's easy to differentiate from similar metrics.

You then have the option of configuring a chart with [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") or a [custom alert](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace") for the calculated metric. Select **Manage this metric** to go to the **Metrics** tab of monitor settings, from where you can disable/enable, delete, or create charts and alerts based on the calculated metrics for the given monitor.

![Calculated metric created](https://dt-cdn.net/images/calculatedmetriccreated-328-109d3aab05.png)

Calculated metric created

## Analyze errors

When you select **Analyze errors** on the [Errors card](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors#errors "Analyze browser monitor and clickpath results on the Synthetic details page.") on the Synthetic details page, you're directed to the **Multidimensional analysis** page showing a histogram for the error count per error code per unit of time for all locations in the timeframe. The height of each bar represents the frequency of the error codes. When you select **Analyze** ![Analyze](https://dt-cdn.net/images/analyze-icon-e97b8dab47.svg "Analyze") next to an individual error code, you're directed to the analysis page filtered by that error code. The [scatter plot](#scatter-plot) and [data points](#data-points) are automatically filtered to show only errors.

Hover over any bar in the graph to see the error count for that point in time.

![Analyze all errors](https://dt-cdn.net/images/mdaallerrors-1499-51f21b7a1d.png)

Analyze all errors

### Multidimensional analysis of errors

The following filters are available for multidimensional analysis of errors:

* **Location**—select all locations or an individual monitor location.
* **Error**—select all error codes or a single error code.
* **Event**—select all or an individual Synthetic script event. You can only choose an event with timings (an action) from this list; events with no timing data are grayed out.
* **Split by**—select **Location**, **Error code**, or **Event**.

## Data points

The **Multidimensional analysis** page gives you the ability to select a specific set of executions in an [analysis range](#analysis-range), filtered using multidimensional analysis, so you can focus on a particular action in a single data point to troubleshoot performance or availability.

The list of data points displayed corresponds to the combination of filters you've chosen for the [scatter plot](#scatter-plot) and the multidimensional analysis of [performance](#performance), [availability](#availability), or [errors](#errors).

By default, data points are listed most recent first. On-demand executions in the list are labeled **on-demand**. When you hover over a data point in the scatter plot. you can view its start timestamp, location, and key performance metric value. Error data points (availability failures) are marked in red and display the error code.

Select a data point to see event-level screenshots and analysis, including waterfall graphs for events with timings (actions).

Execution details include start and end timestamps and location. The **Execution type** is:

* **on-demand** for on-demand executions.
* **standard** for scheduled executions.
* **re-run** for executions that have been retried on error ([**Automatic retry on error** enabled](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors#outage-handling "Learn about configuring browser monitors and clickpaths.")).
* **on-update** for executions upon monitor script update.

You can switch between all events and only events with timings (that is, events with actions and waterfall graphs). **Close details** to return to the list of data points.

![Switch to view events with timings](https://dt-cdn.net/images/events-with-timings-1181-3cd5daebe7.png)

Switch to view events with timings

Successful data points display the reference screenshots captured for each event. (See the [Synthetic details](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors#screenshots "Analyze browser monitor and clickpath results on the Synthetic details page.") for more on how screenshots are captured.) Note that even successful data points can have actions with individual resource errors, shown in red in the waterfall graph.

![Successful data point](https://dt-cdn.net/images/bm-successful-data-point-1871-c7c20fc7b0.png)

Successful data point

Error data points display screenshots captured during that specific execution, enabling you to compare **Actual** and **Expected** (reference) screenshots. The failing data point and action are marked in red. Select **Show difference** to see the percentage and areas of mismatch highlighted in a superimposed image.

![Error data point](https://dt-cdn.net/images/bm-error-data-point-1879-3592365d74.png)

Error data point

## Related topics

* [Calculated metrics API - Synthetic](/managed/dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics "Manage calculated synthetic metrics via the Dynatrace configuration API.")