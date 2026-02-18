---
title: Log content analysis
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-analysis
scraped: 2026-02-18T05:39:25.205794
---

# Log content analysis

# Log content analysis

* Latest Dynatrace
* Overview
* 2-min read
* Updated on Oct 15, 2025

Log Management and Analytics gives you direct access to the log content of all your system's mission-critical processes. Log data typically contain a lot of information. One way to handle a large amount of data is to narrow down the log records and parse them.

## Logs and events viewer

The logs and events viewer enables you to present log data in a filterable table that is easy to work with and to browse log data within a certain timeframe using detected aspects of the log content. You can use **Available attributes** to narrow down your log view and focus on a specific aspect of the log content.

* See [Logs and events viewer](/docs/analyze-explore-automate/logs/lma-analysis/logs-and-events "Browse log data within a specified timeframe using DQL and elements that are automatically detected within the log content.")

User rights for log monitoring

Logs often contain sensitive information that may not be appropriate for all users to see. For this reason, your Dynatrace administrator must add approved Log Management and Analytics users to the **Log viewer** group, which has the **View logs** account-security permission. Non-admin users are NOT part of this group by default. To access log contents, they must be explicitly added.

## Log events

Once you create log events based on your log content, Dynatrace artificial intelligence will automatically correlate relevant log events with any problems that it detects in your environment. Relevant log events that are associated with problems are then factored into problem root-cause analysis.

* See [Log events](/docs/analyze-explore-automate/logs/lma-log-processing/lma-log-events "Create log events based on log data and use them in problem detection.")

## Log metrics

Dynatrace log monitoring gives you the ability not only to view and analyze logs but also to create metrics based on log data and use them throughout Dynatrace like any other metric. You can add them to your dashboard, include them in analysis, and even create custom alerts.

* See [Log metrics](/docs/analyze-explore-automate/logs/lma-log-processing/lma-log-metrics "Create metrics based on log data and use them throughout Dynatrace like any other metric.")

## Log custom attributes

In Dynatrace log monitoring, you can define your own custom log data attributes that suits your particular log data format. Similarly to the automatically detected log attributes, your custom log attributes are extracted from the log data during ingestion and become available within Dynatrace.

* See [Log custom attributes](/docs/analyze-explore-automate/logs/lma-analysis/logs-and-events/lma-log-custom-attributes "Create and use custom attributes during log data ingestion.")

## Enriched log data analysis

With enriched log data, you can check for the specific user inside your application. Use the log viewer and PurePathÂ® distributed traces link from a specific log record. You can view all logs for a particular user session to see how the user interacted with the application and, with the **Logs** tab in distributed traces, you can navigate through the trace and, based on logs associated with that trace, quickly see what happened.

* See [Leverage log enrichment for traces to resolve problems](/docs/observe/application-observability/distributed-traces/use-cases/problems-logs-traces "Use the log enrichment to view related log entries in the distributed traces view and enhance your analysis capabilities.")