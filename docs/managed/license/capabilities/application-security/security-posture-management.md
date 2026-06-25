---
title: Calculate your consumption of Security Posture Management (SPM) (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/application-security/security-posture-management
scraped: 2026-05-12T12:00:43.264559
---

# Calculate your consumption of Security Posture Management (SPM) (DPS)

# Calculate your consumption of Security Posture Management (SPM) (DPS)

* Explanation
* 5-min read
* Published Aug 12, 2025

Security Posture Management feature overview

This page describes how the Security Posture Management DPS capability is consumed and billed.
For an overview of the capability, including its main features, see [Security Posture Management (SPM)](/managed/license/capabilities/application-security#spm "Learn how Dynatrace Application Security monitoring consumption is calculated using the Dynatrace Platform Subscription model.").

## How consumption is calculated: host-hour

The unit of measure for Kubernetes Security Posture Management is a host-hour.

In Kubernetes environments, each node that is scanned during an hour is counted as a host-hour, regardless of how many times it was scanned.
You can enable Kubernetes Security Posture Management on a per-cluster basis.

Example scenario: Calculation example

* Kubernetes Security Posture Management is enabled for a Kubernetes cluster with 10 nodes.
* Kubernetes Security Posture Management analysis has been initiated and is ongoing.
* After five days, five nodes are added to the Kubernetes cluster so that there is now a total of 15 nodes on the Kubernetes cluster.
* After 10 days, the overall consumption is calculated as `(10 nodes x 5 days x 24 hours) + (15 nodes x 5 days x 24 hours) = 3000 host-hours`.

## Track your consumption

This section describes the different Dynatrace tools that you can use to track consumption and costs.

### Track your consumption and costs in Account Management

You can also track your usage in Account Management.

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **Subscription** > **Overview**.
2. In **Cost and usage details**, select **Usage summary**.
3. Search for `Security Posture Management` and select **View details**.

### Track your consumption and costs with Data Explorer

* In [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), enter `DPS` in the **Search** field).

### Track your consumption and costs via API

You can query metrics via the [Environment API - Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

## Related topics

* [Unavailable in Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.")
* [License Dynatrace](/managed/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Application Security overview (DPS)](/managed/license/capabilities/application-security "Learn how Dynatrace Application Security monitoring consumption is calculated using the Dynatrace Platform Subscription model.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)