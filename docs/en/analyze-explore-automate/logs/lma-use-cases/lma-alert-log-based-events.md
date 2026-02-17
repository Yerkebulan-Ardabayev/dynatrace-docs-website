---
title: Set up alerts based on events extracted from logs
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-events
scraped: 2026-02-17T05:01:25.768856
---

# Set up alerts based on events extracted from logs

# Set up alerts based on events extracted from logs

* Latest Dynatrace
* Tutorial
* 4-min read
* Updated on Jan 28, 2026

Ingested logs can be triggers for opening new Davis problems.

Using Davis events based on logs you will get immediate alerts once the log record you define is ingested.

Follow this guide to learn more about extracting events from logs.

If you need to set thresholds for your alerts, you should follow the instructions in [Set up custom alerts based on metrics extracted from logs](/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-metrics "How to create and configure Davis problems and custom alerts with metrics based on logs.").

## Prerequisites

Optional

* You have set up [log ingestion](/docs/analyze-explore-automate/logs/lma-log-ingestion "Stream log data to Dynatrace.").
* You have the necessary permissions to configure OpenPipeline. For example, the permissions granted with the default policy: [Data Processing and Storage](/docs/manage/identity-access-management/permission-management/default-policies#data-access "Dynatrace default policies reference").

## Steps

In this example we will open a new Davis problem when certain records, which contain a specific phrase, are ingested.

1. Find logs you want to trigger alerts

You can find alerts by opening ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs** and using the following DQL query.

```
fetch logs



| filter matchesPhrase(content, "Dropping data because sending_queue is full")



| sort timestamp desc
```

![Log results](https://dt-cdn.net/images/logs-1228-18a19d138d.png)

If your DQL query uses `parse`, `fieldAdd`, or other transformations, you should add a processing rule to set those fields on ingest.

2. Extract Davis event in OpenPipeline

1. Add Davis event data extraction configuration in OpenPipeline.

   1. Open ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Logs** and select the **Pipelines** tab.
   2. Find the pipeline you want to modify, or add a new pipeline.
   3. Select  >  **Edit**.
      The pipeline configuration page appears.
   4. Select **Data extraction** tab and add a **Davis event** processor.
2. Set the [DQL matcher](/docs/platform/openpipeline/reference/dql-matcher-in-openpipeline "Examine specific DQL functions and logical operators for log processing.").
   A matcher sets the condition for the event that is to be extracted.
   It is a subset of filtering conditions in a single DQL statement.

   In **Matching condition**, use the matcher as shown below.

   ```
   matchesPhrase(content, "Dropping data because sending_queue is full")
   ```

   If you use segments or your permissions are set at the record level, you should include those conditions in the matcher.

   There are situations when a matcher can't be easily extracted from a DQL statement.
   In these cases, you can [create log alerts for a log event or summary of log data](/docs/dynatrace-intelligence/use-cases/create-alert-in-logs "Create log alerts for a specific log event or summary of log data").
3. Set event properties.

   Event properties are metadata that your event will contain when it is triggered.
   You can remap any field from the log record.

   In our example, we will remap the `dt.source_entity` field to have the alerts connected to entities for [Dynatrace Intelligence root cause analysis](/docs/dynatrace-intelligence/root-cause-analysis "How Dynatrace analyzes problems to determine their root cause.").

   In **Event template**, set the following key/value pairs.

   * Set `event.type` to `CUSTOM_ALERT`.
   * Set `event.description` to `Dropping data because sending_queue is full. Try increasing queue_size.`.
   * Set `event.name` to `OpenTelemetry exporter failure`.
   * Set `dt.source_entity` to `{dt.source_entity}`.

   ![Pipeline data extraction](https://dt-cdn.net/images/pipeline-config-1190-5bd3924a5d.png)

3. Open problem in Problems

When the first Davis event is extracted, a new problem will be opened.
If there are no new events within the timeout period as defined in `dt.davis.event_timeout`, the problem will be closed automatically.

The default timeout is 15 minutes.

![Problem in Problems app](https://dt-cdn.net/images/problems-app-1048-6fd9c7e554.png)

## Conclusion

Extracting Davis events from logs is ideal for simple alerting when thresholds are not important.

* It provides immediate/real-time alerting.
* Additional overview of matching data overtime is not required.

Once you're extracting events, you can use these to trigger automations using simple workflows as described in [Create a simple workflow in Dynatrace Workflows](/docs/analyze-explore-automate/workflows/simple-workflow "Build and run a simple workflow.").

## Further reading

More information about event properties is available at:

* [Davis Event Reports](/docs/semantic-dictionary/model/davis#event "Get to know the Semantic Dictionary models related to Davis AI.")
* [Custom-defined event correlation](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation#custom-defined-event-correlation "Gain an understanding of the Events section on each host, process, and service overview page.")

## Related topics

* [Set up custom alerts based on metrics extracted from logs](/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-metrics "How to create and configure Davis problems and custom alerts with metrics based on logs.")
* [Log metrics (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics "Learn how to create and use Dynatrace log metrics to analyze log data.")
* [Log events (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-events "Learn how to create and use Dynatrace log events to analyze log data.")