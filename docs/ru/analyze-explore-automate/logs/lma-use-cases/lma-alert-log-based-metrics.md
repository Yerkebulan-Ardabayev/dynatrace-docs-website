---
title: Set up custom alerts based on metrics extracted from logs
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-metrics
scraped: 2026-02-23T21:37:47.009318
---

# Set up custom alerts based on metrics extracted from logs

# Set up custom alerts based on metrics extracted from logs

* Latest Dynatrace
* Tutorial
* 4-min read
* Updated on Jan 28, 2026

Ingested logs can be triggers for opening new Davis problems.

Using a combination of metrics based on logs and [custom alerts](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app."), you can use the power of different Dynatrace Intelligence data analyzers to address use cases from simple threshold-based alerting to seasonal baselines, for example:

* Alert when the average count of matching records exceeds a specific number within a defined time period.
* Alert when the value of a metric is abnormal, without setting a static threshold.

Follow this guide to learn more about alerting with metrics based on logs.

If you don't need to set thresholds, you should follow the instructions in [Set up alerts based on events extracted from logs](/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-events "How to create and configure Davis problems and alerts with events based on logs.").

## Prerequisites

* You have set up [log ingestion](/docs/analyze-explore-automate/logs/lma-log-ingestion "Stream log data to Dynatrace.").
* You are using OpenPipeline.
* You have the necessary permissions to configure the custom alert, within [Anomaly Detection app](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.").

## Steps

In this example we will open a new Davis Problem when certain records, which contain a specific phrase, are ingested and exceed a static threshold.

1. Find logs you want to trigger alerts

You can find alerts by opening ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs** and using the following DQL query.

```
fetch logs



| filter matchesPhrase(content, "Dropping data because sending_queue is full")



| sort timestamp desc
```

If your DQL query uses `parse`, `fieldAdd`, or other transformations, you should add a processing rule to set those fields on ingest.

2. Extract metric in OpenPipeline

Add metric extraction configuration in OpenPipeline.

1. Open ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Logs** and select the **Pipelines** tab.
2. Find the pipeline you want to modify, or add a new pipeline.
3. Select  >  **Edit**.
   The pipeline configuration page appears.
4. Select **Metric extraction** tab.
5. Set

   * The metric name and ID.
   * The [DQL matcher](/docs/platform/openpipeline/reference/dql-matcher-in-openpipeline "Examine specific DQL functions and logical operators for log processing.").
     A matcher sets the condition for the event that is to be extracted.
     It is a subset of filtering conditions in a single DQL statement.

     In **Matching condition**, use the matcher as shown below.

     ```
     matchesPhrase(content, "Dropping data because sending_queue is full")
     ```

If you use Segments or your permissions are set at the record level, you should include those conditions in the matcher.

There are situations when a matcher can't be easily extracted from a DQL statement.
In these cases, you can [create log alerts for a log event or summary of log data](/docs/dynatrace-intelligence/use-cases/create-alert-in-logs "Create log alerts for a specific log event or summary of log data").

3. Add dimensions.
   For most logs, you can add automated correlation to entities in Dynatrace Intelligence root cause analysis.
   To do this, add a `dt.source_entity` dimension or any other field that contains an entity identifier.

3. Configure a custom alert

Go to ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** and create a new custom alert.

This section describes how to create a simple custom alert.

If you need to set additional advanced properties and fine-tune your alert, use the **Advanced** mode.

1. Set the scope for your alert.
2. Use DQL syntax to point the metric you created.
   To have your alert connected to monitored entity make sure to add `by: {dt.source_entity}`.
3. Define the alerting conditions under which a new Davis event will be generated.
   You can pick different ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** analyzers.

   * Use **Suggest values** to find the right threshold.
   * Use **Preview** to get an estimation of how many alerts would have been generated in the last two hours.
4. Finally set the event details like title and description.

4. Open problem

When the alerting conditions are met you will see a new problem in ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**.

## Conclusion

Here's when to use a custom alert with metrics based on logs:

* You need to set thresholds or use other machine learning analyzers to trigger alerts.
* When you want to alert on anomalies in value coming from a log field like `http.response_time`.
* Metric analyzers are triggered every minute so itâs not a real-time alerting method.
* Metric dimensions have low cardinality.

Detected anomalies can trigger automations using simple workflows as described in [Create a simple workflow in Dynatrace Workflows](/docs/analyze-explore-automate/workflows/simple-workflow "Build and run a simple workflow.").

## Related topics

* [Set up alerts based on events extracted from logs](/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-events "How to create and configure Davis problems and alerts with events based on logs.")
* [Log metrics (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics "Learn how to create and use Dynatrace log metrics to analyze log data.")
* [Log events (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-events "Learn how to create and use Dynatrace log events to analyze log data.")
* [Alerting and notifications](/docs/analyze-explore-automate/alerting-and-notifications "Utilize anomaly detection, problem detection, and workflows for external notifications to ensure that critical problems never go unnoticed.")