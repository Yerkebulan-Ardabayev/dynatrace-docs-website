---
title: Calculate your consumption of Browser Monitor or Clickpath (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/digital-experience-monitoring/browser-monitor-clickpath
scraped: 2026-05-12T12:11:44.694339
---

# Calculate your consumption of Browser Monitor or Clickpath (DPS)

# Calculate your consumption of Browser Monitor or Clickpath (DPS)

* Explanation
* 5-min read
* Published Aug 12, 2025

Browser Monitor or Clickpath feature overview

This page describes how the Browser Monitor or Clickpath DPS capability is consumed and billed.
For an overview of the capability, including its main features, see [Browser Monitor or Clickpath](/managed/license/capabilities/digital-experience-monitoring#browser-monitor "Learn how Dynatrace Digital Experience Monitoring (DEM) consumption is calculated using the Dynatrace Platform Subscription model.").

## How consumption is calculated: Synthetic action

The unit of measure for browser monitors is a synthetic action.
A synthetic action is an interaction with a synthetic browser that triggers a web request that includes a page load, navigation event, or action that triggers an XHR or Fetch request performed during private and public executions of Synthetic Browser Monitors.

The following interactions are not counted:

* Scroll downs, keystrokes, or clicks that don't trigger web requests aren't counted as actions.
* XHR or Fetch requests that are made by a synthetic browser as the result of a user action like a page load, which isn't directly triggered by user input, don't result in user actions and therefore aren't counted.

A synthetic action is charged as soon as the action is made, no matter if it is successful or fails.
If an action fails and therefore subsequent actions are not executed, these subsequent actions are not charged.

## Track your consumption

This section describes the different Dynatrace tools that you can use to track consumption and costs.

Example scenario: Estimate possible consumption

The following calculation gives you an estimate of the maximum possible consumption, assuming that all Synthetic actions were executed.
Actual consumption may vary depending on if some actions failed subsequent actions were not executed.

`# Synthetic actions consumed per monitor = (# Synthetic actions included in monitor) Ã (# Executions per hour) Ã (# Locations) Ã # Hours`

### Track your consumption with Metrics

Dynatrace provides built-in usage metrics that help you understand and analyze your organization's consumption of Browser Monitor and Clickpath.

For details about the respective monitoring-consumption metrics, see [Built-in Real User Monitoring metrics](/managed/analyze-explore-automate/metrics-classic/built-in-metrics#synthetic "Explore the complete list of built-in Dynatrace metrics.").

### Track your consumption and costs in Account Management

You can also track your usage in Account Management.
Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **Subscription** > **Overview** > **Cost and usage details** > **Usage summary** and select the **Browser Monitor and Clickpath** capability.

### Track your consumption and costs via API

You can query metrics via the [Environment API - Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

## Related topics

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")
* [Digital Experience Monitoring (DEM) overview (DPS)](/managed/license/capabilities/digital-experience-monitoring "Learn how Dynatrace Digital Experience Monitoring (DEM) consumption is calculated using the Dynatrace Platform Subscription model.")
* [License Dynatrace](/managed/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)