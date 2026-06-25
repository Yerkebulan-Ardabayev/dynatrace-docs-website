---
title: Calculate your consumption of Real User Monitoring (RUM) (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/digital-experience-monitoring/real-user-monitoring
scraped: 2026-05-12T12:11:42.815615
---

# Calculate your consumption of Real User Monitoring (RUM) (DPS)

# Calculate your consumption of Real User Monitoring (RUM) (DPS)

* Explanation
* 5-min read
* Published Aug 12, 2025

Real User Monitoring feature overview

This page describes how the Real User Monitoring DPS capability is consumed and billed.
For an overview of the capability, including its main features, see [Real User Monitoring](/managed/license/capabilities/digital-experience-monitoring#rum "Learn how Dynatrace Digital Experience Monitoring (DEM) consumption is calculated using the Dynatrace Platform Subscription model.").

## How consumption is calculated: sessions per application per hour

The unit of measure for calculating your organization's consumption of RUM (web and mobile) is sessions per application per hour, excluding replay capture.

A user action is a mouse-click, finger tap, or app start that triggers a web request (for example, a page load or a page-view navigation).
A user who interacts with more than one web application or app during the same session consumes one session per hour for each application.
For sessions that last longer than one hour, one session is consumed per hour.

For complete details on when RUM user sessions start and end, see [User session timings](/managed/observe/digital-experience/rum-concepts/user-session#user-session-timings "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.").
RUM session consumption is not capped.

Sessions that include only one user action are considered "bounced" and aren't counted.
A user who interacts with more than one application at the same time consumes one session for each of those applications.

Interactions with hybrid mobile apps, that for technical reasons include a web application and a mobile app, will only be considered as a single session.

## Track your consumption

This section describes the different Dynatrace tools that you can use to track consumption and costs.

### Track your consumption with Metrics

Dynatrace provides built-in usage metrics that help you understand and analyze your organization's consumption of Real User Monitoring.

For details about the respective monitoring-consumption metrics, see [Built-in Real User Monitoring metrics](/managed/analyze-explore-automate/metrics-classic/built-in-metrics#real-user-monitoring "Explore the complete list of built-in Dynatrace metrics.").

### Track your consumption and costs in Account Management

You can also view your usage in Account Management.
Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **Subscription** > **Overview** > **Cost and usage details** > **Usage summary** and select the **Third-Party Synthetic API Ingestion** capability.

### Track your consumption and costs via API

You can query metrics via the [Environment API - Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

## Related topics

* [Digital Experience Monitoring (DEM) overview (DPS)](/managed/license/capabilities/digital-experience-monitoring "Learn how Dynatrace Digital Experience Monitoring (DEM) consumption is calculated using the Dynatrace Platform Subscription model.")
* [Real User Monitoring](/managed/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.")
* [License Dynatrace](/managed/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)