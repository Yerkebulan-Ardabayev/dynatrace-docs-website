---
title: Create calculated metrics for web applications
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/rum-calculated-metrics-web
scraped: 2026-05-12T11:07:09.084282
---

# Create calculated metrics for web applications

# Create calculated metrics for web applications

* How-to guide
* 2-min read
* Updated on May 10, 2024

In Dynatrace, you can create calculated metrics to make your current analysis available for [charting](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") and [API usage](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API."). You can also leverage calculated metrics to add custom alerts.

Once you select the application you're interested in, you can use **Multidimensional Analysis** to select aspects of your user actions and create a calculated metric. You can choose if you want to split your selected performance metrics by another dimension, such as geolocation, browser, and error type, or only use single dimensions, such as [user action properties](/managed/observe/digital-experience/web-applications/additional-configuration/define-user-action-and-session-properties "Define custom string, numeric, and date properties for your monitored web applications.").

![Dashboard with custom charts based on calculated metrics](https://dt-cdn.net/images/image-19-1916-a1098d2ab4.png)

Dashboard with custom charts based on calculated metrics

## Create a metric

To create a calculated metrics from your application

1. Go to **Web** and select the application for which you want to create a metric.
2. Scroll down to **Impact of user actions on performance** and select **Analyze performance**.
3. On the **User action analysis** page, select the desired timeframe, options, and filters.
4. Select one of the **Analyze by** options and a performance metric that you want to create the metric for.
5. Optional Use the filter bar to add filters for geolocations, browser versions, user action properties, and more to focus the resulting metric on what you're interested in.
6. Select **Create metric**.

   ![Creating a metric on the Multidimensional analysis page](https://dt-cdn.net/images/createmetric-1896-0987193fdb.png)

   Creating a metric on the Multidimensional analysis page
7. Optional Change the metric name and key and turn on **Split by <dimension name>**.
8. Optional Select **Advanced options** if you want to additionally specify or change the following parameters.

   * Metric
   * Metric name
   * Metric key for API usage
   * Filters
   * Split-by parameters
9. Select **Create metric**.

Use the metric to create a custom chart or alert.

Only new data is written to calculated metrics; retrospective data is not included.

You can have up to 500 enabled calculated metrics per environment across all applications and up to 100 enabled calculated metrics per application.

### Example

In this example, let's analyze `Price`, which is a [user action property](/managed/observe/digital-experience/web-applications/additional-configuration/define-user-action-and-session-properties#custom-properties "Define custom string, numeric, and date properties for your monitored web applications."), and filter it by `Loyalty status`, which is another user action property.

On the **Multidimensional analysis** page, select the timeframe for the analysis. To filter out prices paid by platinum customers only, we select `Price` in the **Analyze by** list box and then set additional filters by selecting `String property`, `Loyalty status`, and `Platinum`.

![Example - Revenue by platinum customers](https://dt-cdn.net/images/loyalty-status-example-1385-0549af2191.png)

Example - Revenue by platinum customers

We can also create a metric and generate a custom chart.

![Example - Create a metric](https://dt-cdn.net/images/example-create-metric-320-b73577057f.png)

Example - Create a metric

## Create custom charts based on calculated metrics

Creating charts can help you to analyze combinations of application metrics directly on your dashboard. You can split and filter available entities to fine-tune the metric dimensions that appear in your charts and filter out entities that are relevant to you.

For details on creating charts and pinning them to your dashboards, see [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

## Manage metrics

After you've created a calculated metric, you can view its properties, delete it, temporarily disable it, or create a chart or a metric event for it.

Once a metric has been created, you can't change its properties.

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Metrics**.
5. Select the metric you want to manage and check its properties or perform one of the following actions.

   * **Enable or disable** ![Toggle icon](https://dt-cdn.net/images/icon-toggle-barista-701-35879d6adf.png "Toggle icon") the metric
   * **Copy** the API URL for the metric
   * **Create a chart** with [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.")
   * **Create alert** to create a [metric event](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace")
   * **Analyze** to open the [multidimensional analysis](/managed/observe/digital-experience/web-applications/analyze-and-use/multi-dimensional-analysis "Find out how Dynatrace Real User Monitoring enables you to dig deep into your user actions and perform analysis across numerous dimensions.") view for the metric
   * **Delete metric**

## Related topics

* [Web application metrics API](/managed/dynatrace-api/configuration-api/calculated-metrics/rum-metrics "Manage calculated web application metrics via the Dynatrace configuration API.")