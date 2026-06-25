---
title: Create calculated metrics for mobile applications
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/additional-configuration/rum-calculated-metrics-mobile
scraped: 2026-05-12T11:07:00.377874
---

# Create calculated metrics for mobile applications

# Create calculated metrics for mobile applications

* How-to guide
* 1-min read
* Updated on May 10, 2024

In Dynatrace, you can create calculated metrics to make your current analysis available for [charting](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") and [API usage](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API."). You can also leverage calculated metrics to add custom alerts.

Once you select the application you're interested in, you can use **Multidimensional Analysis** to select aspects of your user actions and create a calculated metric. You can choose if you want to split your selected performance metrics by another dimension, such as geolocation, browser, and error type, or only use single dimensions, such as [user action properties](/managed/observe/digital-experience/web-applications/additional-configuration/define-user-action-and-session-properties "Define custom string, numeric, and date properties for your monitored web applications.").

![Dashboard with custom charts based on calculated metrics](https://dt-cdn.net/images/image-19-1916-a1098d2ab4.png)

Dashboard with custom charts based on calculated metrics

## Create a calculated metric

To create a calculated metrics from your application

1. Go to **Frontend** and select the application for which you want to create a metric.
2. Under **Top 3 actions**, select **Analyze performance**.
3. Select the desired **OS family**, **Contribution**, timeframe, and **Analyze by** options.
4. Optional Use the filter bar to add filters for geolocation, manufacturer, Apdex, and more to focus the resulting metric on what you're interested in.
5. Select **Create metric**.

   ![Creating a metric on the Multidimensional analysis page](https://dt-cdn.net/images/mobile-metric-create-metric-mda-1758-a913b7f692.png)

   Creating a metric on the Multidimensional analysis page
6. Optional Change the metric name and key, and turn on **Split by <dimension name>**.

   For [mobile](/managed/observe/digital-experience/mobile-applications/analyze-and-use/action-and-session-properties-mobile "User action and session properties, which are metadata key-value pairs, provide added visibility and deeper analysis of your end users' experience. Using these properties for your applications, you can filter user sessions, add calculated metrics, create charts, and more.") and [custom applications](/managed/observe/digital-experience/custom-applications/analyze-and-use/action-and-session-properties-custom "User action and session properties, which are metadata key-value pairs, provide added visibility and deeper analysis of your end users' experience. Using these properties for your applications, you can filter user sessions, add calculated metrics, create charts, and more."), you cannot split a metric by user action property. Splitting by user action property is available only for web applications.
7. Select **Create metric**.

   ![Overlay for creating a metric](https://dt-cdn.net/images/mobile-metric-create-metric-overlay-330-88ec98fac1.png)

   Overlay for creating a metric

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

1. Go to **Frontend**.
2. Select the application that you want to configure.
3. Select **More** (**â¦**) > **Edit** in the upper-right corner of the tile with your application name.
4. From the application settings, select **Metrics**.
5. Select the metric you want to manage and check its properties or perform one of the following actions.

   * **Enable or disable** ![Toggle icon](https://dt-cdn.net/images/icon-toggle-barista-701-35879d6adf.png "Toggle icon") the metric
   * **Copy** the API URL for the metric
   * **Create a chart** with [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.")
   * **Create alert** to create a [metric event](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace")
   * **Delete metric**

## Related topics

* [Mobile app metrics API](/managed/dynatrace-api/configuration-api/calculated-metrics/mobile-app-metrics "Manage calculated metrics for mobile and custom apps via the Dynatrace configuration API.")