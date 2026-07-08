---
title: License overview (Dynatrace classic licensing)
source: https://docs.dynatrace.com/managed/manage/account-management/license-subscription/license-overview-classic
---

# License overview (Dynatrace classic licensing)

# License overview (Dynatrace classic licensing)

* Explanation
* 3-min read
* Published Nov 24, 2025

The Account Management **License** view provides a real-time view of your Dynatrace classic licensing product consumption.
Dynatrace classic licensing covers usage of products such as host units, host unit hours, Digital Experience Monitoring, Davis data units (DDUs), and Application Security units (ASUs).
Historical analysis is available at the daily or hourly level.

You can access this information at **Account Management** > **License**.

If you see **Account Management** > **Subscription**, please refer to our [Dynatrace Platform Subscription documentation](/managed/manage/account-management/license-subscription/subscription-overview-dps "View your Dynatrace Platform Subscription budget summary and cost analysis.") instead.

## Total license usage

The **Total license usage** section displays real-time information about your licensing consumption.

![Account Management License view for Dynatrace classic licensing model, with total license usage highlighted.](https://dt-cdn.net/images/account-management-classic-total-license-usage-1857-f5c4b93a02.png)

Account Management License view for Dynatrace classic licensing model, with total license usage highlighted.

Each licensed product is displayed in a separate infographic that indicates how much of each product you have used.
The colored bars indicate if you're under or over your quota:

* Blue: Your usage is below your quota.
* Brown: You have exceeded your quota, and your usage incurs overage charges (if this is allowed for your license).
* Red: Your maximum quota is reached, and monitoring is deactivated.

Hover over a product infographic to display a detailed breakdown of usage.

## Usage details

The **Usage details** section displays historical license consumption.

![Account Management License view for Dynatrace classic license model, with Usage details highlighted.](https://dt-cdn.net/images/account-management-classic-usage-details-1857-acaa5cff26.png)

Account Management License view for Dynatrace classic license model, with Usage details highlighted.

You can filter this information according to **Cluster**, **Product**, **Resolution**, and **Timeframe**.

You can export this data in CSV format.
To do this, select ![Export](https://dt-cdn.net/images/dashboards-app-dashboard-export-5ed2168e10.svg "Export") **Export data**.

Use **Resolution** to choose the granularity:

* **Daily**: Day-by-day total usage.
* **Hourly**: Hourly cumulative totals for a selected day.
* **Total**: Cumulative usage for consumption-based licenses (includes host unit hours, Digital Experience Monitoring, Davis data units, and Application Security units).
* **Linear forecast**: Forecast usage based on linear extrapolation from the last 30 days of usage data (limited to Digital Experience Monitoring and Davis data units only).
* **Seasonal forecast**: Forecast usage based on a seasonal forecast from the last 365 days of data (limited to Digital Experience Monitoring and Davis data units only).

## Environment usage breakdown

The **Environment usage breakdown** section shows how individual environments contribute to license consumption, including a breakdown of product consumption within each environment.

![Account Management License view for Dynatrace classic license model, with Environment usage breakdown highlighted.](https://dt-cdn.net/images/account-management-classic-environment-usage-breakdown-1857-73ccab1183.png)

Account Management License view for Dynatrace classic license model, with Environment usage breakdown highlighted.

## FAQ

### Why does the license consumption in **Usage details** not match the information in **Total license usage**?

* **Total license usage** provides an accurate and real-time measurement of your license consumption.
  These measurements differentiate between free, paid, and overage usage.
* **Usage details** provides a historic breakdown of total consumption.
  This breakdown includes all units, and does not differentiate between paid, free, and overage usage.

### When should I use linear forecasts and seasonal forecasts?

* Linear model:

  + If you're a new customer, the linear model offers more accurate predictions during the first year of consumption.
  + The linear model is also accurate if your consumption in the previous 30 days is indicative of your future usage.
* Seasonal model: If your business is more seasonal (for example, retail usage spikes during holiday periods) and you have a year or more of consumption data, the seasonal model can provide a more accurate estimate of future usage.

### Why does the forecast show that I have consumed more DDUs than my current license is for?

Forecasts show the total consumption that has accrued from the first day your first Dynatrace license was active.
Total consumption may include consumption from a license that has since expired.

Therefore, even if the forecast shows that you have consumed more DDUs than your current license, this does not automatically mean that you have already consumed the DDUs in your current license.