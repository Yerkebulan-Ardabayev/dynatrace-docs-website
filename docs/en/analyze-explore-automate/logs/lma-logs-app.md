---
title: Logs app
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-logs-app
scraped: 2026-03-01T21:07:11.102208
---

# Logs app

# Logs app

* Latest Dynatrace
* App
* 4-min read
* Updated on Jul 01, 2025

Prerequisites

### Permissions

The following table describes the required permissions.

storage:spans:read

allow to read spans, Segments Variables (Optional)

storage:bizevents:read

allow to read biz events, Segments Variables (Optional)

storage:metrics:read

allow to read metrics, Segments Variables (Optional)

storage:events:read

allow to read events, Segments Variables (Optional)

storage:security.events:read

allow to read security events, Segments Variables (Optional)

storage:logs:read

allow to read logs

storage:user.sessions:read

allow to read user sessions, Segments Variables (Optional)

storage:user.events:read

allow to read user events

storage:buckets:read

allow to read logs

storage:files:read

allow to do joins on the lookup tables

## Installation

Make sure the app is [installed in your environment](/docs/manage/hub#install "See the information about Dynatrace Hub.").

Get started

Concepts

![The dynamic histogram chart with intuitive point-and-click filter provide unique experience for simplified and timely exploration of logs.](https://cdn.hub.central.dynatrace.com/hub/console/drafts/85/media/3.png)![The "Explain Logs" feature provides actionable steps and insights to cut your root cause analysis and time to action, enabling you to resolve faster.](https://cdn.hub.central.dynatrace.com/hub/console/drafts/85/media/2.png)![Clear, stacked severity trends with swift and intuitive filtering options help to explore JSON-structured and other logs easily.](https://cdn.hub.central.dynatrace.com/hub/console/drafts/85/media/1.png)![Cut MTTR by turning raw logs into guided insights - In context of your trace, or surrounding topology entities.](https://dt-cdn.net/hub/logs-hub-4.png)![Log details surface rich context in one click - access to linked traces, topology, and more. Instant filters turn insights into precise searches.](https://cdn.hub.central.dynatrace.com/hub/console/drafts/85/media/4.png)

1 of 5The dynamic histogram chart with intuitive point-and-click filter provide unique experience for simplified and timely exploration of logs.

[01Query and filter logs

* How-to guide
* Explore logs with DQL queries and filter statements in the Dynatrace Logs app.](/docs/analyze-explore-automate/logs/lma-logs-app/query-and-filter)[02Spot trends with the log distribution chart

* How-to guide
* Get a visual overview of log entries grouped by status to spot trends, identify anomalies, and perform targeted queries without leaving the visualization.](/docs/analyze-explore-automate/logs/lma-logs-app/log-distribution-chart)[03View surrounding logs

* How-to guide
* Use surrounding logs to understand log data in context in the Dynatrace Logs app.](/docs/analyze-explore-automate/logs/lma-logs-app/surrounding-logs)[04Filter with facets

* How-to guide
* Filter with facets in the Dynatrace Logs app.](/docs/analyze-explore-automate/logs/lma-logs-app/facets)[05Adjust the log message

* How-to guide
* Adjust the log message in the Dynatrace Logs app.](/docs/analyze-explore-automate/logs/lma-logs-app/message)[06Limits in Logs

* Reference
* Learn about the limits that apply to the Logs app and how to modify these limits.](/docs/analyze-explore-automate/logs/lma-logs-app/limits)

## About Logs

![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs** is your starting point to finding relevant log records without writing queries.

* Find the logs youâre looking for.
  Easily filter your logs without writing DQL, and find the logs you need.
* Proactive investigation.
  Uncover problems and insights by investigating log distribution chart over time.
* Discover the root cause of issues from context.
  Investigate the surrounding logs of interest to understand the context and root cause of errors:

  + Find the root cause & check if a log is only a symptom of issues.
  + Based on traces: show transaction details in a distributed environment.
  + Based on source: analyze the selected record in the context of a single component.
* Expand your analysis.
  Quickly navigate between log details and related hosts, Kubernetes clusters, traces, or other entities.
  This helps you understand the impact of a single record in the context of related metrics and traces.
* Share your findings.
  Continue your journey with logs in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**, or automate with ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**.

## FAQ

Can I edit the DQL query?

Select **Edit DQL query** from the menu, besides the **Run query** button.

How are logs licensed?

Querying logs works based on the same licensing as other Log Management and Analytics feature.

* If you have **Retain** and **Query** as separate rate-card items, you only consume the license for queried log volume in bytes.
  For more info, see [Calculate your consumption of Log Management & Analytics - Query (DPS)](/docs/license/capabilities/log-analytics/dps-log-query "Learn how your consumption of the Log Management & Analytics - Query DPS capability is billed and charged.").
* If you have **Retain with Included Queries** on your rate card, there is no cost to for included queries.
  For more info, see [Log Analytics (DPS)](/docs/license/capabilities/log-analytics#log-retain-included-queries "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.").

The following actions are free of charge:

* Facets and Filter field suggestions.
* Generating the log distribution chart.
* Searching for previously returned results (using the searchbox above the table).

The license is consumed only when you click the **Run query** button or when you use **Surrounding logs**.

How to configure access to Logs?

The users must have access to the Dynatrace Platform and logs stored in Grail ([see the built-in access policies](/docs/platform/upgrade#built-in-policies "Use the power of Grail, AppEngine, and AutomationEngine to take advantage of improvements in storing and analyzing observability and security data.") for log data). The application replaces the **Logs and Events** screen, so users who accessed logs previously can use ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**.

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Find relevant log records without writing DQL queries.](https://www.dynatrace.com/hub/detail/logs/?internal_source=doc&internal_medium=link&internal_campaign=cross/)