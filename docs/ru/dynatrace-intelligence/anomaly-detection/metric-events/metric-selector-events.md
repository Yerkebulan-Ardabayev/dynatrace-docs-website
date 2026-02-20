---
title: Metric selector events
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/metric-events/metric-selector-events
scraped: 2026-02-20T21:14:51.059204
---

# Metric selector events

# Metric selector events

* Latest Dynatrace
* How-to guide
* 4-min read
* Updated on May 22, 2025

The metric selector is a powerful instrument for specifying which data you want to read for the metric event evaluation. It provides you with two major possibilities:

* [Metric transformations](/docs/dynatrace-api/environment-api/metric-v2/metric-selector "Configure the metric selector for the Metric v2 API.") for transforming the data you're reading.
* [Metric expressions](/docs/dynatrace-api/environment-api/metric-v2/metric-expressions "Use metric expressions to apply arithmetic operations in a data points query via the Metrics API v2.") for combining one or more metrics into a different result using simple mathematics.

With the metric selector, Davis can access the historic data of the metric and can learn the normal behavior of your environment, enabling you to use auto-adaptive thresholds in your metric event. However, some limitations apply:

* **100,000** monitored metric dimensions per environment
* **10,000** metric events configurations (both metric key and metric selector) per environment
* **1,000** monitored dimensions per metric event configuration (static or auto-adaptive threshold)
* **500** monitored dimensions per metric event configuration (seasonal baseline)
* **100** metric selectors per monitoring strategy. You can have 100 configurations with an auto-adaptive threshold and 100 with a static threshold.

## Scope of metric selector events

The selector itself defines the scope of a metric selector event. It is important to understand the implications when configuring a selector consisting of measurements from thousands of individual sources. Dynatrace applies safety limits to anomaly detection in terms of the number of metric dimensions that can be observed within one monitoring environment to avoid any operational issues. To learn how to narrow down the scope of your configuration, see [**Filter transformation**](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#filter "Configure the metric selector for the Metric v2 API.").

![Metric selector example](https://dt-cdn.net/images/metric-selector-example-1296-84f54644de.png)

## Combining metrics

With the power of a metric expression, you can implement alerting with a top-down view of a situation rather than alerting on each component.

For example, you can observe log patterns across multiple hosts. By calculating the total count of observed log patterns across all relevant log files, Dynatrace can detect pattern anomalies on the accumulated log stream rather than on the individual counts per log file.
If there are sparse counts across many entities (for example, an error count across multiple processes of the same type), aggregated top-down anomaly detection is much more resilient against false-positive alerts than detection on an individual error count per process.

## Create a metric selector event

1. Go to **Settings** > **Anomaly Detection** > **Metric events** and select **Add metric event**.
2. In the **Summary** field, provide a short meaningful description of the event.
3. In the **Query definition** section, configure the metric query:

   1. Select the **Metric selector** type of the query.
   2. Specify the required metric selector.
4. Select a management zone. Only data coming from this zone is evaluated for the metric event. Omit this field to use all the data queried by the metric selector.
5. Optional In the **Advanced query definition** section, specify the query's offset (in minutes).  
   You need the offset for metrics with latency; otherwise, the metric event might produce false alerts.
6. Define the monitoring strategy

   1. Choose the model type:

      * Auto-adaptive thresholdâDynatrace calculates the threshold automatically and adapts it dynamically to your metric's behavior.
      * Static thresholdâthe threshold that doesn't change over time.
      * Seasonal BaselineâDynatrace creates a confidence band on a metric with seasonal patterns
   2. For the static threshold, specify the threshold. Select **Use suggested threshold** to use a value based on the previous data.
   3. Choose the [missing data alert](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#missing-data "How to set up an alert for missing measurements.") behavior.  
      If the missing data alert is enabled, it is combined with the threshold condition by the **OR** logic.
   4. Select the alert condition: alert if the metric is above, below, or outside of the threshold.
   5. Optional In the **Advanced model properties** section, specify a [sliding window](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#sliding-window "How to set up an alert for missing measurements.") for comparison.  
      The sliding window defines how often the thresholdâwhether it is automatically calculated or manually specifiedâmust be violated within a sliding window of time to raise an event (violations don't have to be successive). This helps you to avoid overly aggressive alerting on single violations. You can set a sliding window of up to 60 minutes.
7. Check the preview for your alert and evaluate the effectiveness of your configuration.

   1. Select the dimension values that you want to see on the preview.
   2. Select the timeframe of the preview. You can receive alerts for one, three, or seven days.
8. Provide a **Title** for your event. The title should be a short, easy-to-read string describing the situation, such as `High network activity` or `CPU saturation`.
9. In the **Description** section, create a meaningful event message. Event messages help you understand the nature of the event. You can use the following placeholders:

   * `{alert_condition}`âthe condition of the alert (above/below the threshold).
   * `{baseline}`âthe violated value of the baseline.
   * `{dims}`âa list of all dimensions (and their values) of the metric that violated the threshold. You can also specify a particular dimension: `{dims:dt.entity.<entity>}`. To fetch the list of available dimensions for your metric, query it via the [GET metric descriptor](/docs/dynatrace-api/environment-api/metric-v2/get-descriptor "View the descriptor of a metric via Metrics v2 API.") request.
   * `{entityname}`âthe name of the affected entity.
   * `{metricname}`âthe name of the metric that violated the threshold.
   * `{missing_data_samples}`âthe number of samples with missing data. Only available if missing data alert is enabled.

     `{missing_data_samples}` in the event description

     We recommend including the `{missing_data_samples}` placeholder in the event description to see whether the problem is raised due to missing data samples or threshold violations.
   * `{severity}`âthe severity of the event.
   * `{threshold}`âthe violated value of the threshold.
10. Select the **Event type** for triggered events.
11. Turn **Allow merge** on or off to define the merge strategy for triggered events.  
    If **Allow merge** is turned on, Davis AI will try to merge this event into existing problems; if it's turned off, a new problem is raised each time.
12. Optional Set additional key-value properties to be attached to the event.
13. Select **Save changes**.

## Related topics

* [Metrics API - Metric selector](/docs/dynatrace-api/environment-api/metric-v2/metric-selector "Configure the metric selector for the Metric v2 API.")
* [Metrics API - Metric expressions](/docs/dynatrace-api/environment-api/metric-v2/metric-expressions "Use metric expressions to apply arithmetic operations in a data points query via the Metrics API v2.")
* [Metrics Classic](/docs/analyze-explore-automate/metrics-classic "Learn about metrics classic that Dynatrace offers.")