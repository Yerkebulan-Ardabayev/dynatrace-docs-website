---
title: Calculate your consumption of Real User Monitoring Property (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/digital-experience-monitoring/real-user-monitoring-property
scraped: 2026-05-12T12:11:46.536062
---

# Calculate your consumption of Real User Monitoring Property (DPS)

# Calculate your consumption of Real User Monitoring Property (DPS)

* Explanation
* 5-min read
* Published Aug 12, 2025

Real User Monitoring Property feature overview

This page describes how the Real User Monitoring Property DPS capability is consumed and billed.
For an overview of the capability, including its main features, see [Real User Monitoring Property](/managed/license/capabilities/digital-experience-monitoring#rum-property "Learn how Dynatrace Digital Experience Monitoring (DEM) consumption is calculated using the Dynatrace Platform Subscription model.").

## How consumption is calculated: individual user sessions

Dynatrace measures the consumption of RUM properties using defined properties within individual user sessions. Up to 20 properties per application are included in the volume. Any additional properties will be charged according to the total number of individual user sessions that use this property.

`((# billable properties) - (20 included properties)) * (# individual user sessions) = Consumption`

For details about the respective monitoring-consumption metrics, see [Built-in Real User Monitoring metrics](/managed/analyze-explore-automate/metrics-classic/built-in-metrics#real-user-monitoring "Explore the complete list of built-in Dynatrace metrics.").

## Track your consumption

This section describes the different Dynatrace tools that you can use to track consumption and costs.

### Track your consumption with Metrics

Dynatrace provides built-in usage metrics that help you understand and analyze your organization's consumption of Real User Monitoring Property.
To use these metrics, in Data Explorer, enter `DPS` in the **Search** field.

### Track your consumption and costs in Account Management

You can also view your usage in Account Management.
Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **Subscription** > **Overview** > **Cost and usage details** > **Usage summary** and select the **Real User Monitoring Property** capability.

### View consumption and costs via API

You can query metrics via the [Environment API - Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

## Related topics

* [Digital Experience Monitoring (DEM) overview (DPS)](/managed/license/capabilities/digital-experience-monitoring "Learn how Dynatrace Digital Experience Monitoring (DEM) consumption is calculated using the Dynatrace Platform Subscription model.")
* [Real User Monitoring](/managed/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.")
* [License Dynatrace](/managed/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)