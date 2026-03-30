---
title: Log alerts
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/alerting-on-logs
scraped: 2026-03-06T21:15:23.570408
---

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

Use custom alerts with metrics based on logs when you need to:

* Set thresholds.
* Employ statistical analyzers to trigger alerts.

Metrics based on logs are particularly useful for detecting anomalies in the number of occurrences of log records, or of values that are derived from log fields, such as `http.response_time`.

Keep in mind that metric analyzers are triggered every minute, which means they are not suitable for real-time alerting.

For detailed instructions, see Set up custom alerts based on metrics extracted from logs.

### Use alerting with events based on logs

For simple alerting scenarios where setting thresholds is not necessary, use Davis events extracted from logs.

This method is ideal in cases of very sparse occurrences of log pattern (once a week, once per month) when metrics wouldnât be useful.
It also provides near real-time alerting and instant notifications without the need for an additional overview of matching data over time.

It is particularly useful when you require prompt responses to specific log events without the complexity of statistical analysis.

For detailed instructions, see Set up alerts based on events extracted from logs.

### Use DQL queries in custom alerts

Use DQL queries in custom alerts when you need to define custom alert conditions based on specific log data patterns, and metric or event extraction is not possible.
This approach allows for flexible and precise querying to identify events or trends within your logs.

Keep in mind that these queries are executed every minute, which can increase license consumption.
Therefore, make sure you use only optimized queries.

This method is not typically recommended as the primary alerting strategy.
However, it can serve as a fallback when alerting with metrics or events is not possible.

For detailed instructions, see Create log alerts for a log event or summary of log data.

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

* OpenPipeline
* Anomaly detection
* Event analysis and correlation
* Anomaly detection configuration
* Detect problems with Logs