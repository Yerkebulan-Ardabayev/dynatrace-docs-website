---
title: Dynatrace Intelligence for Notebooks
source: https://www.dynatrace.com/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/davis-for-notebooks
scraped: 2026-02-28T21:21:21.236879
---

# Dynatrace Intelligence for Notebooks

# Dynatrace Intelligence for Notebooks

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Jan 28, 2026

Dynatrace Intelligence for Notebooks runs a range of analyzers directly in Notebooks, providing on-spot results and enabling you to fine-tune your custom alert configurations.

## Anomaly Detection

With ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** combined with the power of [DQL](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language."), you can custom-build powerful configurations to detect anomalies in metrics, logs, business data, or a combination of them. To preview and fine-tune your Anomaly Detection configuration before deploying it to action, use a Dynatrace Intelligence for Notebooks analysis option:

* [Auto-adaptive threshold](/docs/dynatrace-intelligence/anomaly-detection/auto-adaptive-threshold "How Dynatrace adapts thresholds for multiple entities within the scope of an anomaly detection configuration.")âDynatrace calculates the threshold automatically and adapts it dynamically to your data's behavior.
* [Seasonal baseline](/docs/dynatrace-intelligence/reference/ai-models/seasonal-baseline "How Dynatrace Intelligence suggests seasonal baseline thresholds for a scope of entities.")âDynatrace creates a confidence band for data with seasonal patterns
* [Static threshold](/docs/dynatrace-intelligence/anomaly-detection/static-thresholds "When to use a static threshold for your anomaly detection.")âthe threshold that doesn't change over time.

For each of these options, you can configure a [missing data alert](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#missing-data "How to set up an alert for missing measurements."). Missing data and threshold conditions are combined by the **OR** logic.

To run an anomaly detection analysis in Notebooks

1. Go to **Notebooks** ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks").
2. Open your notebook or create a new one.
3. Add a **Query Grail** section and [query](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks#query-grail "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") the data you're interested in, or add a **Metrics** section and select the required metric.

   For a DQL query, use the `interval: 1m` parameter to ensure proper data resolution for the analysis.
4. Select **Options**.
5. In the **Options** panel, select **Analyze and alert** and activate the analyzer.
6. Select the required anomaly detection analyzer and configure its parameters.
7. Select **Run analysis**.

Dynatrace Intelligence analyses the data and shows potential alerts. Note that these are just indicative simulationsâno real alerts are triggered based on this analysis.

![An example of anomaly detection on seasonal data in the Notebooks app.](https://dt-cdn.net/images/notebooks-seasonal-anomaly-detection-1920-dbbd5f3499.png)

## Forecast analysis

Dynatrace Intelligence predictive AI analysis foresees future values of any time series of numeric values based on the accumulated data. To trigger a [forecast analysis](/docs/dynatrace-intelligence/reference/ai-models/forecast-analysis "Learn how Dynatrace Intelligence predictive AI generates forecasts.")

1. Go to **Notebooks** ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks").
2. Open your notebook or create a new one.
3. Add a **Query Grail** section and [query](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks#query-grail "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") the data you're interested in, or add a **Metrics** section and select the required metric.
4. Select **Options**.
5. In the **Options** panel, select **Analyze and alert** and activate the analyzer.
6. Select the **Forecast** analyzer and configure its parameters.
7. Select **Run analysis**.

Dynatrace Intelligence calculates the forecast and shows it, extending your visualization.

![An example of a forecast for seasonal data in the Notebooks app.](https://dt-cdn.net/images/notebooks-seasonal-prediction-1920-0137a2c619.png)

## Related topics

* [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.")
* [[Video] Introduction to Anomaly Detection based on DQLï»¿](https://www.youtube.com/watch?v=-GxLlr9oGGA)