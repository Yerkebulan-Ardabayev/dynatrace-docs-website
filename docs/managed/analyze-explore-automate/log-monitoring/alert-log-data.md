---
title: Log data alerting
source: https://docs.dynatrace.com/managed/analyze-explore-automate/log-monitoring/alert-log-data
---

# Log data alerting

# Log data alerting

* Explanation
* 3-min read
* Published Jun 12, 2025

Log Monitoring Classic

Dynatrace Log Monitoring allows you to define patterns, events, and custom log metrics to receive proactive notifications.

## Log metrics

You can create a metric based on your monitored log data. With such a metric, you can have Dynatrace continuously scan your monitored log data and display a chart of that metric on your dashboard so that any pattern changes that occur in your custom metric will be clearly visible.

Check out how to use a log metric to save its chart to a dashboard, and then create an alert.

* See [Log metrics (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics "Learn how to create and use Dynatrace log metrics to analyze log data.") for general information about log metrics
* See [Example of creating an alert based on log metric](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics#log-monitoring-metric-alert-example "Learn how to create and use Dynatrace log metrics to analyze log data.")

## Log events

When Dynatrace ingests log data, it applies the query specified in the log event definition. Every matched occurrence triggers a log event that can be configured to individually create a problem for each triggered log event or can be merged into one problem.

Check out how to create a log event based on a Log Monitoring query to filter specific log content and properties from the ingested log data.

* See [Log events (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-events "Learn how to create and use Dynatrace log events to analyze log data.") for general information about log events
* See [Example of creating a log event based on ingested log data](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-events#log-monitoring-log-event-example "Learn how to create and use Dynatrace log events to analyze log data.")

## Related topics

* [Log metrics (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics "Learn how to create and use Dynatrace log metrics to analyze log data.")
* [Log events (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-events "Learn how to create and use Dynatrace log events to analyze log data.")