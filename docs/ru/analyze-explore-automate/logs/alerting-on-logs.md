---
title: Log alerts
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/alerting-on-logs
scraped: 2026-02-25T21:18:23.418441
---

# Log alerts

# Log alerts

* Latest Dynatrace
* Explanation
* 3-min read
* Updated on Oct 15, 2025

Effective alerting is essential for maintaining optimal performance and quickly addressing issues.
Various strategies for alerting with logs provide timely notifications based on log data.
Each strategy offers unique benefits and configurations, catering to different use cases and requirements.

Understanding these approaches will help you choose the most suitable alerting method to ensure your applications and systems run smoothly.

## Explore different methods

### Use alerting with metrics based on logs

Use [custom alerts](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.") with metrics based on logs when you need to:

* Set thresholds.
* Employ statistical analyzers to trigger alerts.

Metrics based on logs are particularly useful for detecting anomalies in the number of occurrences of log records, or of values that are derived from log fields, such as `http.response_time`.

Keep in mind that metric analyzers are triggered every minute, which means they are not suitable for real-time alerting.

For detailed instructions, see [Set up custom alerts based on metrics extracted from logs](/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-metrics "How to create and configure Davis problems and custom alerts with metrics based on logs.").

### Use alerting with events based on logs

For simple alerting scenarios where setting thresholds is not necessary, use Davis events extracted from logs.

This method is ideal in cases of very sparse occurrences of log pattern (once a week, once per month) when metrics wouldnât be useful.
It also provides near real-time alerting and instant notifications without the need for an additional overview of matching data over time.

It is particularly useful when you require prompt responses to specific log events without the complexity of statistical analysis.

For detailed instructions, see [Set up alerts based on events extracted from logs](/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-events "How to create and configure Davis problems and alerts with events based on logs.").

### Use DQL queries in custom alerts

Use DQL queries in [custom alerts](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.") when you need to define custom alert conditions based on specific log data patterns, and metric or event extraction is not possible.
This approach allows for flexible and precise querying to identify events or trends within your logs.

Keep in mind that these queries are executed every minute, which can increase license consumption.
Therefore, make sure you use only optimized queries.

This method is not typically recommended as the primary alerting strategy.
However, it can serve as a fallback when alerting with metrics or events is not possible.

For detailed instructions, see [Create log alerts for a log event or summary of log data](/docs/dynatrace-intelligence/use-cases/create-alert-in-logs "Create log alerts for a specific log event or summary of log data").

## Comparison of Alerting Methods

| Aspect | Log-Based Events | Log-Based Metrics (recommended) | Log Queries in custom alerts |
| --- | --- | --- | --- |
| Alerting Type | Simple alerting without thresholds | Threshold-based alerting using statistical analyzers | Custom queries to define alert conditions |
| Response Time | Fastest | Triggered every minute | Triggered every minute |
| Configuration Complexity | Low (only Event Extraction) | High (requires setting Metric Extraction and Anomaly Detection - new **Anomaly Detection** custom alert configuration) | Medium (requires a custom alert configuration) |
| Use Case | Prompt responses to specific log events when ingested | Detecting anomalies in record occurrences or values derived from log fields | Custom alert conditions based on log data |
| Example | Instant alert for a specific log entry | Alert for anomalies in `http.response_time` field values; alert when matching record occurred 10 times | Alert for specific log query results and apply statistical analyzers |
| Cost | Depends on the number of generated events and event size | Depends on the number of data points and metric size | Depends on query complexity and scanned volumes |

## Related topics

* [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.")
* [Anomaly detection](/docs/dynatrace-intelligence/anomaly-detection "How Dynatrace detects anomalies in your environment.")
* [Event analysis and correlation](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Gain an understanding of the Events section on each host, process, and service overview page.")
* [Anomaly detection configuration](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration "How to set up an alert for missing measurements.")
* [Detect problems with Logs](/docs/analyze-explore-automate/logs/lma-use-cases/lma-detect-problems-with-logs "Use the Problems app and Logs to quickly detect and analyze arising problems.")