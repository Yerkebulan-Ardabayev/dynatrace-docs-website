---
title: Metric key events
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/metric-events/metric-key-events
scraped: 2026-02-27T21:29:13.040080
---

# Metric key events

# Metric key events

* Latest Dynatrace
* How-to guide
* 4-min read
* Updated on May 22, 2025

Metric key events are based on incoming raw measurements of a single metric. For this event type, only the static threshold monitoring strategy is available. You can monitor all metric dimensions within one configuration (for example, it is possible to create an alert for 20,000 CPUs in a single metric event configuration). As a safeguard, Dynatrace throttles these configurations with a limit of 200 simultaneous alerts. You can narrow down the scope of the event to particular dimensions.

Additionally, the limit of **10,000** configurations (both metric key and metric selector) per environment applies.

## Scope of metric key events

Many Dynatrace metrics are delivered by multiple entities; the count can easily reach thousands. You likely don't need your event to cover all these entities simultaneously. To narrow down the scope of the event, you can specify some rule-based filters.

Two types of filters are available:

* **Entity filters** narrow the scope based on the provided criteria (for example, entity name or tag). The actual set of available criteria depends on the metric. If multiple filters are specified, the **AND** logic applies.
* **Dimension filters** filter out entities based on provided tuples (unique combinations of metricâdimension keyâdimension value). If multiple filters are specified, the **AND** logic applies. For example, you can set a dimension filter that selects only user actions coming from iOS devices for your metric event based on the **Action count** metric.

![Metric key example](https://dt-cdn.net/images/metric-key-example-1309-8338cbabbd.png)

## Create a metric key event

1. Go to **Settings** > **Anomaly Detection** > **Metric events** and select **Add metric event**.
2. In the **Summary** field, provide a short meaningful description of the event.
3. In the **Query definition** section, configure the metric query:

   1. Select the **Metric key** type of the query.
   2. Select the metric for your metric event. You can provide the key or the display name of a metric. Start typing to see the list of suggestions.
   3. Select a type of aggregation for the metric (where applicable).
   4. Select a management zone. Only data coming from this zone is evaluated for the metric event. Omit this field to use all the data provided by the metric.
4. Optional In the **Advanced query definition** section, specify the query's offset (in minutes).  
   You need the offset for metrics with latency; otherwise, the metric event might produce false alerts.
5. Optional Add rule-based entity filters.
6. Optional Select the dimensions to be considered by the event.
7. Define the monitoring strategy. For metric key queries, only static thresholds are available.

   1. Specify the threshold value. Select **Use suggested threshold** to use a value based on the previous data.
   2. If applicable, select the threshold unit.
   3. Choose the [missing data alert](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#missing-data "How to set up an alert for missing measurements.") behavior.  
      If the missing data alert is enabled, it is combined with the threshold condition by the **OR** logic.
   4. Select the alert condition: alert if the metric is above or below the threshold.
   5. Optional In the **Advanced model properties** section, specify a sliding window for comparison.  
      The sliding window defines how often the threshold (whether automatically calculated or manually specified) must be violated within a sliding window of time to raise an event (violations don't have to be successive). It helps you to avoid overly aggressive alerting on single violations. You can set a sliding window of up to 60 minutes.
8. Check the preview for your alert and evaluate how effective your configuration is.

   1. Select the dimension values that you want to see on the preview.
   2. Select the timeframe of the preview. You can receive alerts for one, three, or seven days.
9. Provide a **title** for your event. The title should be a short, easy-to-read string describing the situation, such as `High network activity` or `CPU saturation`.
10. In the **Description** section, create a meaningful event message. Event messages help you understand the nature of the event. You can use the following placeholders:

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
11. Select the type for triggered events.
12. Define the **merge** strategy for triggered events.  
    If the merge is allowed, DavisÂ® AI will try to merge this event into existing problems; otherwise, a new problem is raised each time.
13. Optional Set additional key-value properties to be attached to the event.
14. Select **Save changes**.

## Related topics

* [Metrics Classic](/docs/analyze-explore-automate/metrics-classic "Learn about metrics classic that Dynatrace offers.")