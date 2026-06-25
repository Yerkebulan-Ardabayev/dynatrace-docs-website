---
title: Log data analysis (Logs Classic)
source: https://docs.dynatrace.com/managed/analyze-explore-automate/log-monitoring/analyze-log-data
scraped: 2026-05-12T11:13:30.610368
---

# Log data analysis (Logs Classic)

# Log data analysis (Logs Classic)

* Overview
* 4-min read
* Updated on Jan 18, 2023

Log Monitoring Classic

Log Monitoring gives you direct access to the log content of all your system's mission-critical processes. Log data typically contain a lot of information. One way to handle a large amount of data is to narrow down the log records and parse them.

## Log viewer

The log viewer enables you to present log data in a filterable table that is easy to work with, and to browse log data within a certain timeframe using detected aspects of the log content. You can use **Available attributes** to narrow down your log view and to focus on a specific aspect of the log content.

* See [Log viewer (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer "Learn how to use Dynatrace log viewer to analyze log data.")

User rights for Log Monitoring

Logs often contain sensitive information that may not be appropriate for all users to see. For this reason, your Dynatrace administrator must add approved Log Monitoring users to the **Log viewer** group, which has the **View logs** account-security permission. Non-admin users are NOT part of this group by default. To access log contents, they must be explicitly added.

## Log events

Once you create log events based on your log content, Dynatrace artificial intelligence will automatically correlate relevant log events with any problems that it detects in your environment. Relevant log events that are associated with problems are then factored into problem root-cause analysis.

* See [Log events (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-events "Learn how to create and use Dynatrace log events to analyze log data.")

## Log metrics

Dynatrace Log Monitoring gives you the ability not only to view and analyze logs, but also to create metrics based on log data and use them throughout Dynatrace like any other metric. You can add them to your dashboard, include them in an analysis, and even create custom alerts.

* See [Log metrics (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics "Learn how to create and use Dynatrace log metrics to analyze log data.")

## Log custom attributes

In Dynatrace Log Monitoring, you can define your own custom log data attributes that suits your particular log data format. Similarly to the automatically detected log attributes, your custom log attributes are extracted from the log data during ingestion and become available within Dynatrace.

* See [Log custom attributes (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-custom-attributes "Learn how to create and use custom attributes during log data ingestion.")

## Enriched log data analysis

With enriched log data, you can check for the specific user inside your application. Use the log viewer and PurePathÂ® distributed traces link from a specific log record. You can view all logs for a particular user session to see how the user interacted with the application and, with the **Logs** tab in distributed traces, you can navigate through the trace and, based on logs associated with that trace, quickly see what happened.

* See [Leverage log enrichment for traces to resolve problems](/managed/observe/application-observability/distributed-traces/use-cases/problems-logs-traces "Use the log enrichment to view related log entries in the distributed traces view and enhance your analysis capabilities.")