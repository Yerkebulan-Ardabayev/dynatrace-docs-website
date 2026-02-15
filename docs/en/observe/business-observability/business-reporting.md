---
title: Business reporting
source: https://www.dynatrace.com/docs/observe/business-observability/business-reporting
scraped: 2026-02-15T21:25:29.850529
---

# Business reporting

# Business reporting

* Latest Dynatrace
* Tutorial
* 3-min read
* Published Feb 19, 2025

Track business metrics, KPIs, and SLOs in real time, automatically in context with IT infrastructure and services to promote collaboration between business and IT teams. Prioritize IT investments and automate remediation based on measurable business impact.

## Introduction

Use business events to capture key business metrics and transform these into business KPIs. Business events are a special class of data well-suited for demanding business use cases. Gain real-time visibility into business health and enable exploratory analytics to optimize business outcomes and understand business anomalies.

Business events can come from OneAgent, RUM, log files, and external systems via an API. Dynatrace automatically enriches business events with Smartscape topology context, connecting business metrics to their supporting IT systems. OneAgent can capture business events from in-flight application payloads without requiring code changes, prioritizing business data to ensure the lossless precision many business use cases demand.

## Target audience

This article is intended for business analysts and process managers who understand how their businesses are performing in real time and look for optimal execution of their business processes. You should have a basic knowledge of how business events are captured and some domain knowledge of the business area you are trying to analyze.

## Use cases

### Define the metrics and dimensions you want to report

Often, business KPIs are a function of multiple data points. For example, to report a supplier lead time KPI, you would subtract the order request date from the order delivery date. The dates are ingested as business events and then transformed by a processing rule into a lead time KPI. Youâll want to include relevant dimensions such as supplier name and product to add important granularity to your reports. These dimensions are derived from fields within the business event.

### Determine where to capture the business events

OneAgent makes it easy to capture business events through simple configuration steps, without any custom code. If your application can be instrumented with OneAgent, this should be your preferred option.

Log files are a commonly used source, especially if your application already writes relevant business data to log files.

You can ingest business events from external systems through an API.

You can use Dynatrace real user monitoring (RUM) to capture business events from user interactions.

### Define processing rules

Processing rules help you filter, parse, and transform business data. You can add new calculated fields, mask or drop sensitive data, define retention policies through bucket assignment, and much more.

Build and share your [dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.").

Once stored in Grail, you can query your business event data interactively and analyze it using [DQL](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language."). DQL is the starting point for analysis, whether you use Notebooks, Dashboards, or the DQL Query API. You can use query results interactively or pin them to a dashboard as charts, tiles, or tables.

### Measure and optimize the business value of aggregator sales channels

Capture business events from aggregator APIs to extract business KPIs such as quotes sent, bookings, and average revenue. Segment these business KPIs into relevant cohorts or dimensions; examples include partner, product, and geography. Add relevant IT metrics such as API response time and API errors.

### Recover lost business by automating customer outreach

Track critical errors near the bottom of your conversion funnel that frequently cause users to abandon their journey. Segment users by potential or real customer value; cart amount, purchase history, or loyalty status. Create a Workflow to automate an appropriate outreach response such as an incentive to return or credit towards a future purchase.

### Reduce call center costs by alerting on business exceptions

Extract business error messages such as out-of-stock, credit declined, unknown product SKU, invalid invoice number, etc. from in-flight application payload. Define alerting thresholds and profiles to notify IT and business teams as appropriate.

### Track long-term seasonal trends

To report on trends, capture the relevant business metrics as business events. Ensure your business event bucket assignments have the retention characteristics needed to meet your analysis and reporting goals.