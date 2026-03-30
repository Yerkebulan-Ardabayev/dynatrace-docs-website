---
title: Observe your logs in real time
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-use-cases/lma-e2e-real-time-observability-logs-dql
scraped: 2026-03-06T21:15:25.252177
---

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

For more details on supported log sources, see Log ingestion.

### 2. Explore log entries in Logs app

To quickly find and explore ingested logs, use ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**. It helps you find logs using quick filters and autocomplete. Moreover, it can also explain the meaning of a selected record.

For more details, see Logs app.

### 3. Share information via Notebooks app

In ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, create shareable documents for custom analytics. Create a new notebook and [add a Prompt section](../../dashboards-and-notebooks/notebooks.md#section-create-davis-copilot "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") for natural language queries.

For more details, see Notebooks.

### 4. Monitor with Dashboards app

In ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, use different tiles to visualize your log data and monitor them for your use cases.

For more details, see Dashboards.

## Next steps

To start observing your logs, no complex configuration or query language knowledge is required. Once you have data in, you can explore other use cases for analytics and observability with logs.

For more information, check the **Related topics** section and see Log Management and Analytics use cases.

## Related topics

* Log on Grail examples
* Log alerts
* Connect log data to traces
* Use logs in context to troubleshoot Kubernetes (K8s) issues
* Log ingestion
* Mask sensitive data in logs
* Configure data storage and retention for logs
* Set up Grail permissions for logs
* Log Management and Analytics best practices