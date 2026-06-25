---
title: Calculate your consumption of HTTP Monitor (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/digital-experience-monitoring/http-monitor
scraped: 2026-05-12T12:11:39.130999
---

# Calculate your consumption of HTTP Monitor (DPS)

# Calculate your consumption of HTTP Monitor (DPS)

* Explanation
* 5-min read
* Published Aug 12, 2025

HTTP Monitor feature overview

This page describes how the HTTP Monitor DPS capability is consumed and billed.
For an overview of the capability, including its main features, see [HTTP Monitor](/managed/license/capabilities/digital-experience-monitoring#http-monitor "Learn how Dynatrace Digital Experience Monitoring (DEM) consumption is calculated using the Dynatrace Platform Subscription model.").

## How consumption is calculated: synthetic request

An HTTP monitor consists of one or multiple HTTP(S) requests (for example, `GET`, `POST`, and `HEAD` requests).

The unit of measure for HTTP monitors is a synthetic request.
Each HTTP(S) request consumes one synthetic request.

A synthetic request is charged as soon as the request is made, no matter if it is successful or fails.
If a request fails and therefore subsequent requests are not executed, these subsequent requests are not charged.

Example scenario: Estimate consumption

The following calculation gives you an estimate of the maximum possible consumption, assuming that all Synthetic requests were executed.
Actual consumption may vary depending on if some requests failed subsequent requests were not executed.

`# Synthetic requests consumed per monitor = (# Synthetic requests included in monitor) Ã (# Executions per hour) Ã (# Locations) Ã # Hours`

## Track your consumption

This section describes the different Dynatrace tools that you can use to track consumption and costs.

### Track your consumption with Metrics

Dynatrace provides built-in usage metrics that help you understand and analyze your organization's consumption of Real User Monitoring.

For details about the respective monitoring consumption metrics, see [Built-in Real User Monitoring metrics](/managed/analyze-explore-automate/metrics-classic/built-in-metrics#synthetic "Explore the complete list of built-in Dynatrace metrics.").

### Track your consumption and costs in Account Management

You can also view your usage in Account Management.
Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **Subscription** > **Overview** > **Cost and usage details** > **Usage summary** and select the **HTTP Monitor** capability.

### View consumption and costs via API

You can query metrics via the [Environment API - Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

## Related topics

* [Digital Experience Monitoring (DEM) overview (DPS)](/managed/license/capabilities/digital-experience-monitoring "Learn how Dynatrace Digital Experience Monitoring (DEM) consumption is calculated using the Dynatrace Platform Subscription model.")
* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")
* [License Dynatrace](/managed/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)