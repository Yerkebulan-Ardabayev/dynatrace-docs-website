---
title: Observe your logs in real time
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-use-cases/lma-e2e-real-time-observability-logs-dql
scraped: 2026-03-06T21:15:25.252177
---

# Observe your logs in real time

# Observe your logs in real time

* Latest Dynatrace
* Tutorial
* 2-min read
* Updated on Jan 28, 2026

This tutorial outlines how to ingest, explore, and visualize log data without complex setup or query language expertise.

## Target audience

Developers or Site Reliability Engineers (SREs) who are starting to use Dynatrace for log analytics.

## Learning outcome

By leveraging platform apps, you'll gain immediate insights into application and infrastructure behavior based on logs.

With real-time and contextualized log analytics, you can detect issues faster, correlate events, collaborate effectively, and build custom analytics for your use casesâall within a unified observability platform.

## Prerequisites

* Permissions to install OneAgent
* Permissions to read logs

## Observe real-time log data

### 1. Ingest log data

The easiest way to start sending logs to Dynatrace is by using OneAgent.

1. Install OneAgent on a host.
2. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **Log monitoring** > **Log ingest rules**, and turn on **[Built-in] Ingest all logs**.

For more details on supported log sources, see [Log ingestion](../lma-log-ingestion.md "Stream log data to Dynatrace.").

### 2. Explore log entries in Logs app

To quickly find and explore ingested logs, use ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**. It helps you find logs using quick filters and autocomplete. Moreover, it can also explain the meaning of a selected record.

For more details, see [Logs app](../lma-logs-app.md "Search, filter, and analyze logs with Dynatrace Logs app to quickly investigate and share insights.").

### 3. Share information via Notebooks app

In ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, create shareable documents for custom analytics. Create a new notebook and [add a Prompt section](../../dashboards-and-notebooks/notebooks.md#section-create-davis-copilot "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") for natural language queries.

For more details, see [Notebooks](../../dashboards-and-notebooks/notebooks.md "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.").

### 4. Monitor with Dashboards app

In ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, use different tiles to visualize your log data and monitor them for your use cases.

For more details, see [Dashboards](../../dashboards-and-notebooks/dashboards-new.md "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.").

## Next steps

To start observing your logs, no complex configuration or query language knowledge is required. Once you have data in, you can explore other use cases for analytics and observability with logs.

For more information, check the **Related topics** section and see [Log Management and Analytics use cases](../lma-use-cases.md "Explore common Log Management and Analytics use cases in Dynatrace deployments.").

## Related topics

* [Log on Grail examples](../logs-on-grail-examples.md "Explore basic Log Management and Analytics examples of how to use log data in Dynatrace powered by Grail.")
* [Log alerts](../alerting-on-logs.md "Create, or let Dynatrace create, alerts-based log data in Dynatrace log monitoring")
* [Connect log data to traces](../lma-log-enrichment.md "Connect your incoming log data to traces for more precise Dynatrace analysis.")
* [Use logs in context to troubleshoot Kubernetes (K8s) issues](lma-e2e-troubleshooting.md "Faster troubleshooting with logs, metrics and traces on Kubernetes.")
* [Log ingestion](../lma-log-ingestion.md "Stream log data to Dynatrace.")
* [Mask sensitive data in logs](methods-of-masking-sensitive-data.md "Choose the optimal method to mask your sensitive data in logs.")
* [Configure data storage and retention for logs](../lma-bucket-assignment.md "Your log data can be stored in data retention buckets based on specific retention periods.")
* [Set up Grail permissions for logs](../lma-security-context.md "Use Dynatrace powered by Grail and DQL to reshape incoming log data for better understanding, analysis, or further processing.")
* [Log Management and Analytics best practices](../lma-best-practices.md "Best practices for setting up Log Management and Analytics with Dynatrace.")