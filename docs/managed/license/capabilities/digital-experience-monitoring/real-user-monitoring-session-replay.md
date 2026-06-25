---
title: Calculate your consumption of Real User Monitoring with Session Replay (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/digital-experience-monitoring/real-user-monitoring-session-replay
scraped: 2026-05-12T12:11:40.975616
---

# Calculate your consumption of Real User Monitoring with Session Replay (DPS)

# Calculate your consumption of Real User Monitoring with Session Replay (DPS)

* Explanation
* 5-min read
* Published Aug 12, 2025

Real User Monitoring with Session Replay feature overview

This page describes how the Real User Monitoring with Session Replay DPS capability is consumed and billed.
For an overview of the capability, including its main features, see [Real User Monitoring with Session Replay](/managed/license/capabilities/digital-experience-monitoring#rum-sr "Learn how Dynatrace Digital Experience Monitoring (DEM) consumption is calculated using the Dynatrace Platform Subscription model.").

## How consumption is calculated: sessions per application per hour

When Session Replay is activated for a given RUM session, the unit of measure is one session per application (web and mobile) per hour with Session Replay activated (also referred to as "Session Replay Capture" in your rate card).

Depending on the session, you are billed for a RUM session or a RUM session with Session Replay, but not both.
If a session is longer than one hour, the session is counted multiple times (once per hour).

## Track your consumption

This section describes the different Dynatrace tools that you can use to track consumption and costs.

### Track your consumption with Metrics

Dynatrace provides built-in usage metrics that help you understand and analyze your organization's consumption of Real User Monitoring with Session Replay.

For details about the respective monitoring-consumption metrics, see [Built-in Real User Monitoring metrics](/managed/analyze-explore-automate/metrics-classic/built-in-metrics#real-user-monitoring "Explore the complete list of built-in Dynatrace metrics.").

### Track your consumption and costs in Account Management

You can also view your usage in Account Management.
Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **Subscription** > **Overview** > **Cost and usage details** > **Usage summary** and select the **Real User Monitoring with Session Replay** capability.

### View consumption and costs via API

You can query metrics via the [Environment API - Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

## Related topics

* [Digital Experience Monitoring (DEM) overview (DPS)](/managed/license/capabilities/digital-experience-monitoring "Learn how Dynatrace Digital Experience Monitoring (DEM) consumption is calculated using the Dynatrace Platform Subscription model.")
* [Session Replay](/managed/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.")
* [License Dynatrace](/managed/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)