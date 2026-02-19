---
title: Anomaly detection configuration
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration
scraped: 2026-02-19T21:15:53.752950
---

# Anomaly detection configuration

# Anomaly detection configuration

* Latest Dynatrace
* Explanation
* 7-min read
* Updated on Feb 04, 2026

An anomaly detection configuration relies on several components:

* Data sourceâa time series that is evaluated. It can be a DQL query, fetching data from Grail or a specific metric.
* Analyzer type and parameters: how the data is evaluated.
* Sliding window: a period over which the data is evaluated.
* Event template: what kind of template is triggered by the configuration.

Once configured and activated, the configuration observes the data and triggers an event when conditions are met. To ensure the configuration works as expected and alerts you about the right events, you can preview the results of its work:

* Previous Dynatrace The preview of a metric event visually represents your event's behavior. You can adjust the settings to see how they affect the configuration.

## Data source

Data source provides a time series that is evaluated by Davis:

* Previous Dynatrace A metric defines the time series. It can be a single metric defined by a metric key or a [metric expression](/docs/dynatrace-api/environment-api/metric-v2/metric-expressions "Use metric expressions to apply arithmetic operations in a data points query via the Metrics API v2.").

If your data has a latency, you need to offset it in your configuration via the **Query offset** parameter. Specify the value in minutes.

## Delay

The **Delay** parameter allows users to reduce the frequency of DQL query executions performed by a custom alert in an hour, helping to lower query costs and minimize system load.

While the default delay period between custom alert executions is `1 Minute`, you can configure the query execution to longer intervalsâfor example, every five minutesâwithout losing the ability to perform retroactive evaluations for each minute within the selected time window.

You can configure the **Delay** parameter using **Minutes** or **Seconds**, but the delay can't be longer than `60 Minutes`.

## Analyzer type and parameters

Analyzer parameters define how Dynatrace Intelligence evaluates the data provided by the data source. The exact set of parameters depends on the type of the analysis:

* [Auto-adaptive threshold](/docs/dynatrace-intelligence/anomaly-detection/auto-adaptive-threshold "How Dynatrace adapts thresholds for multiple entities within the scope of an anomaly detection configuration.")âDynatrace calculates the threshold automatically and adapts it dynamically to your data's behavior.
* [Seasonal baseline](/docs/dynatrace-intelligence/reference/ai-models/seasonal-baseline "How Dynatrace Intelligence suggests seasonal baseline thresholds for a scope of entities.")âDynatrace creates a confidence band for data with seasonal patterns.
* [Static threshold](/docs/dynatrace-intelligence/anomaly-detection/static-thresholds "When to use a static threshold for your anomaly detection.")âthe threshold that doesn't change over time.

| Parameter | Description |
| --- | --- |
| Number of signal fluctuations | The auto-adaptive threshold consists of two components: a baseline and a signal fluctuation. This parameter defines how many times the signal fluctuation is added to the baseline. For more information, see [Threshold calculation](/docs/dynatrace-intelligence/anomaly-detection/auto-adaptive-threshold#calculation "How Dynatrace adapts thresholds for multiple entities within the scope of an anomaly detection configuration."). |
| Threshold | This parameter defines the value of a static threshold and, if applicable, its unit. Select **Suggest values** to use a value calculated by Dynatrace Intelligence based on the previous data. |
| Tolerance | This parameter defines the [tolerance](/docs/dynatrace-intelligence/reference/ai-models/seasonal-baseline#parameters "How Dynatrace Intelligence suggests seasonal baseline thresholds for a scope of entities.") of the seasonal model. The higher the tolerance, the broader the confidence band, leading to fewer triggered events. |
| Alert condition | This parameter defines when an event is triggered: if the metric is above, below, or outside of the threshold. |
| Missing data alert | This parameter defines whether the missing data alert is active for the configuration. If active, it's combined with the threshold condition by the **OR** logic. You can find it in the **Advanced properties** section of the configuration. |

## Missing data alert

Dynatrace provides you the ability to set an alert on missing data in a metric or a DQL query. If the alert is active, Dynatrace regularly checks whether the sliding window of the anomaly detection configuration contains any measurements. For example, if the sliding window is set to **3 violating samples during any 5 minutes**, Dynatrace triggers an alert if there's no data within a 3-minute period.

The missing data condition and threshold condition are combined by the **OR** logic.

We recommend disabling missing data alerts for sparse data streams, where measurements are not expected in regular intervals, as it will result in alert storms.

For expected late-incoming data (for example, cloud integration metrics with a 5-minute delay), use long sliding windows that cover delays. For a 5-minute delay, use a sliding window of at least 10 minutes.

The `{missing_data_samples}` event description placeholder resolves to the number of minutes without data received.

## Sliding window

The sliding window of an anomaly detection configuration defines how many one-minute samples must violate the threshold during a specific period. When the specified number of violations is reached, Dynatrace raises an event. The goal is to avoid overly aggressive alerting on single violations, when every measurement that violates the threshold triggers an event.

The event remains open until the metric stays within the threshold for a certain number of one-minute samples within the same sliding window, at which point Dynatrace closes the event. Keeping the event open helps to avoid over-alerting by adding new threshold violations to an existing problem instead of raising a new one.

You can find settings for the sliding window in the **Advanced properties** section of the configuration. By default:

* Any three one-minute samples out of five must violate your threshold to raise an event.
* Five one-minute samples must be back to normal to close this event.

You can set a sliding window of up to 60 minutes for each of the three analyzer types.

Let's consider a case of a static threshold of 90% CPU usage.

![Explanation of the sliding window and de-alerting ](https://dt-cdn.net/images/sliding-window-example-2026-39b1adf7bb.png)

The event analysis starts with the first violating sample in the sliding window. Once the number of violating samples reaches the defined threshold, the event analysis stops and a problem is raised. Even though event analysis is stopped, the event itself remains open until the de-alerting criteria are met:

* The number of violating samples must be lower than the threshold number to raise the problem.
* The number of "normal" samples must be greater than or equal to the number of de-alerting samples.

**Both** criteria must be met to close the event.

The default numbers (3 violating samples in the sliding window of 5 samples to trigger a problem, 5 de-alerting samples to close the event) are a good fit for most configurations. However, you might need to update them (for example, due to noise in measurements).

## Event template

The event template defines characteristics of an event triggered by threshold violation. You need to provide at least the name and the type of the event.

* For quick understanding of the event, the name should be a short, easy-to-read description of the situation, such as `High network activity` or `CPU saturation`.
* The name can include placeholders such as `{threshold}` or `{alert_condition}`. Placeholders are replaced with real values in the actual event. To see available placeholders, type `{` in the input field. There are several available thresholds:

  + `{alert_condition}` - the condition of the alert (above/below the threshold).

    If you set the **Alert condition** to `Alert if the metric is outside`, `{threshold}`, `{severity}` and `{baseline}` placeholders will not be available.
  + `{baseline}` - the violated value of the baseline.
  + `{dims}` - a list of all dimensions (and their values) of the metric that violated the threshold. You can also specify a particular dimension: `{dims:dt.entity.<entity>}`. To fetch the list of available dimensions for your metric, query it via the GET metric descriptor request.
  + `{entityname}` - the name of the affected entity.
  + `{metricname}` - the name of the metric that violated the threshold.
  + `{missing_data_samples}` - the number of samples with missing data. Only available if missing data alert is enabled.

    `{missing_data_samples}` in the event description

    We recommend including the `{missing_data_samples}` placeholder in the event description to see whether the problem is raised due to missing data samples or threshold violations.
  + `{severity}` - the severity of the event.
  + `{threshold}` - the violated value of the threshold.

You can provide additional parameters as key-value pairs. For a list of possible event properties, see [Semantic Dictionary](/docs/semantic-dictionary/model/davis#davis-ai-events "Get to know the Semantic Dictionary models related to Davis AI.").

## Related topics

* [Metric events](/docs/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace")