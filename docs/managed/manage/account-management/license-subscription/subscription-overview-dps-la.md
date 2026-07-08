---
title: Subscription overview (Dynatrace Platform Subscription pre-2023)
source: https://docs.dynatrace.com/managed/manage/account-management/license-subscription/subscription-overview-dps-la
---

# Subscription overview (Dynatrace Platform Subscription pre-2023)

# Subscription overview (Dynatrace Platform Subscription pre-2023)

* Explanation
* 2-min read
* Published Nov 24, 2025

The Account Management **Overview** view provides three key analyses of your DPS subscription.

* Account usage: A summary of your usage, expressed as a proportion of your annual commit.
* Cluster usage breakdown: A breakdown of your annual commit usage across your clusters and capabilities.
* Usage details: Historical chart and tabular view of usage by environment and capability.

You can access this information at **Account Management** > **Subscription** > **Overview**.

![The Account Management Subscription screen for Dynatrace Platform Subscription (pre-April 2023) license models.](https://dt-cdn.net/images/account-management-dps-la-2-1857-f0546c9062.png)

The Account Management Subscription screen for Dynatrace Platform Subscription (pre-April 2023) license models.

All budget and cost information is also available via the [Dynatrace Platform Subscription API](/managed/dynatrace-api/account-management-api/dynatrace-platform-subscription-api "Query the data about your Dynatrace Platform Subscription via the Account Management API.").

This page is valid only for Dynatrace Platform Subscription licenses that were signed before April, 2023.
For all other Dynatrace Platform Subscription licenses, please see [Subscription overview (Dynatrace Platform Subscription)](/managed/manage/account-management/license-subscription/subscription-overview-dps "View your Dynatrace Platform Subscription budget summary and cost analysis.").

## Account usage

Account usage provides a summary of how much of your annual commit has been used.

* **Annual commit**: A textual summary of the current annual commit.
* **Commit period**: The subscription duration.

  A Dynatrace Platform Subscription can span multiple years, broken down into annual commit periods, with each period having an annual commit.

  + Dates are based on UTC and run from `0:00` on the start date shown to `23:59:59` on the end date indicated.
* The license bar: Your actual total consumption, expressed as a proportion of your annual commit.

  Hover over the license bar to get a breakdown of commit usage by capability.

## Environment usage breakdown

The **Environment usage breakdown** table provides a snapshot of cumulative usage by environment and platform feature.
The values represent totals for the current commit period, shown as a list of clusters with a drill-down into each environment. You can view DPS usage by feature and total DPS usage by cluster and environment.

Environments are displayed using their friendly name (if set) and environment identifier.

You can use this information to quickly determine which environments are using up most of the DPS annual commit.

## Usage details

Whereas the **Account usage** and **Cluster usage** sections provide a summary of costs to date, **Usage details** allow you to analyze DPS usage with different views and filters.

### Period

You may have a subscription that spans multiple annual periods.
By default, Account Management displays usage for your current subscription period.
To view usage for an earlier period, select a different **Period**.

### Products

The table shows the cumulative usage for the feature selected in the **Products** list.

* If you select `All`, the table reflects top-level feature usage, such as host unit hours and Davis data units.
* If you select a specific product, such as `Davis data units`, the table is updated to show the breakdown (metrics, logs, etc.) with the row total shown on the right. Selecting a time range also updates the table with cumulative usage for the user-defined period.

Select a **Product** to view subfeature usage. For example, select `Davis data units` to chart the usage of custom metrics, log analytics, serverless functions, events, and traces.

### Resolution

* By default, the chart displays the `Forecast` resolution.
  This sets the timeframe to the annual commit period, showing cumulative costs to date and projected costs through the end of the period.
  The forecast model is linear across all data points in the annual period.
* To filter by product, environment, or timeframe, select either the `Daily` or `Hourly` resolution.

### Filter

Use the **Filter** setting above the chart to view consumption information for selected environments.

### Legend

Each item in the chart legend is a toggle switch for that element: select it to hide or show the corresponding element on the chart.
This can be useful, for example, if you want to hide the annual commit level when viewing usage in a low-usage environment.

### Chart type

Use the chart buttons in the upper-right of the chart to switch chart types.

### Timeframe

To change the timeframe of the chart:

1. Expand the current timeframe setting.
2. Specify a new range.
3. Select **Apply**.