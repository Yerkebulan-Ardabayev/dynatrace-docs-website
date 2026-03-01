---
title: Subscription and license management (DPS pre-April 2023)
source: https://www.dynatrace.com/docs/license/subscription-and-license/subscription-and-license-dps
scraped: 2026-03-01T21:14:33.218592
---

# Subscription and license management (DPS pre-April 2023)

# Subscription and license management (DPS pre-April 2023)

* Latest Dynatrace
* Explanation
* 2-min read
* Published Feb 01, 2022

This documentation is valid for Dynatrace Platform Subscription licenses that were signed prior to April 26, 2023.
For information about all other Dynatrace Platform Subscription licenses, see [License Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.").

This page is provided for informational purposes only.
The terms of the Dynatrace free trial offer and/or your Dynatrace license will be applied to any use of Dynatrace products or services.

The Dynatrace platform subscription model (DPS) simplifies how you consume monitoring on the Dynatrace platform by basing all your consumption of Dynatrace monitoring functionality on a standard unit of currency: the DPS unit.
This approach consolidates the consumption of all Dynatrace monitoring units (Host units, Davis data units, DEM units, Mainframe units, and Application security units) into a single unit of consumption.

## Dynatrace Platform Subscription (DPS)

A Dynatrace SaaS deployment has one active license that controls the products you can use.
Products' capabilities include

* host units[1](#fn-1-1-def)
* host unit hours[2](#fn-1-2-def)
* Digital Experience Monitoring
* Davis data units
* Application security units

1

The size of a host for licensing purposes (based on the amount of RAM provided by a host).
For full details, see [Application and Infrastructure Monitoring (Host Units)](/docs/license/monitoring-consumption-classic/application-and-infrastructure-monitoring "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.").

2

Represents the consumption of a host unit over a time period. One unit hour equates to one unit consumed for one hour.
A host with 16 GB of RAM (one unit) running for a full day consumes 24 host unit hours.
The Dynatrace Platform Subscription model is based on the same monitoring units used across all Dynatrace capabilities.

Your Dynatrace Platform Subscription volume is based on the amount of your annual licensing commitments.
These platform subscription commitments, collectively referred to as your annual commit, are assigned to your account and can be used within the subscription year.
Past consumption is archived at the beginning of each new subscription year, and your full annual commit volume is reset.
Note that any portion of your annual commit that isn't used by the end of the subscription year isn't carried over to the new subscription year.

## How DPS units are consumed

Each hour, Dynatrace collects all usage statistics from your environments, calculates the consumption, and applies the monitoring unit costs defined for your subscription.
The total consumption is then deducted from your DPS annual commit. The remaining balance is the amount you have available for the rest of the subscription year.

## Track consumption

You can view your license consumption in:

* Account Management, see [Subscription overview (Dynatrace Platform Subscription pre-2023)](/docs/manage/account-management/license-subscription/subscription-overview-dps-la "View your Dynatrace Platform Subscription budget summary and cost analysis.").
* The Account Management API, see [Dynatrace Platform Subscription API](/docs/dynatrace-api/account-management-api/dynatrace-platform-subscription-api "Query the data about your Dynatrace Platform Subscription via the Account Management API.").

Information includes:

* Account usage: A summary of how much of your annual commit has been used.
* Environment usage: A breakdown of how the annual commit has been used across your environments and capabilities.
* Usage details: Historical chart and tabular view of usage by environment and capability.