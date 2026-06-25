---
title: Access your DPS cost overview
source: https://docs.dynatrace.com/managed/license/cost-overview
scraped: 2026-05-12T11:09:13.536886
---

# Access your DPS cost overview

# Access your DPS cost overview

* How-to guide
* 6-min read
* Updated on Mar 10, 2026

Hourly reporting on DPS usage and daily updates on your current budget provide you with all the transparency you expect.

## Cost overviews

You can get an overview of your Dynatrace Platform Subscription consumption in **Account Management** > **Subscription**.

* Budget summary: A summary of total subscription period costs and forecast, with a breakdown by environment.
* Cost and usage breakdown: A detailed cost and usage breakdown for the last 30 days.
* Cost and usage analysis: A drilldown view with flexible filtering to view and compare costs and usage.

For more information, see [Subscription overview (Dynatrace Platform Subscription)](/managed/manage/account-management/license-subscription/subscription-overview-dps "View your Dynatrace Platform Subscription budget summary and cost analysis.").

Costs are calculated daily at 02:00:00 UTC based upon the availability of on-premise clusters and an active connection to Dynatrace.
When clusters are unavailable, this results in late delivery of usage data for cost calculations and delays budget notifications.
When the cluster becomes available and usage data uploads to Dynatrace, costs will be calculated at the next 02:00:00 UTC interval and processed several hours later.
This can impact the timeliness of budget notifications.

## Billing report

Your billing report provides details about accrued costs per booking date.
Use this view to determine which Dynatrace monitoring costs were recognized and booked on which day.

Billing reports are available in **Account Management** > **Subscription** > **Billing report**.

For more information, see [Billing report](/managed/license/billing-reports "View your billing to see details about accrued costs per booking date. Use this view to determine which Dynatrace monitoring costs were recognized and booked on which day.").

## Billing period

A Dynatrace Platform Subscription agreement has a minimum commitment of 1 year.
Typically, a DPS agreement is signed for 1â3 years.

Your organization's consumption of each Dynatrace capability accrues costs towards your annual commitment as specified on the rate card.
Each platform capability has a price point defined in the rate card as included with your agreement.

Once you reach your annual commitment, you can continue to use Dynatrace while incurring on-demand usage.
Dynatrace applies the same rate card for on-demand usage without additional fees or premium pricing.
You receive monthly invoices for on-demand costs until the next annual commitment period begins.

Dynatrace Platform Subscription works best when you have permanent usage upload configured between your Dynatrace Managed cluster and Dynatrace Mission Control.
This ensures your costs are booked on the same day the corresponding monitoring is consumed, which leads to more accurate cost and forecast calculations.

## FAQ

### In what timezone are daily usage and cost analysis calculated?

Dynatrace meters usage based on Coordinated Universal Time (UTC).
All references to time and date are therefore to be understood as UTC+00:00.

Daily usage and costs are based on UTC and run from `00:00:00` on the start date of your agreement to `23:59:59` on the end date.

### Is the annual commitment period always 12 months? What if I have a three-year subscription?

Multi-year subscriptions are broken down into annual (12-month) subscription periods.

Dynatrace may adjust the subscription period for your agreement to accommodate your needs.
For example, the first period of a multi-year agreement might actually be just a six-month subscription period, which is then followed by two 12-month subscription periods.

### What currency is used for Dynatrace Platform Subscription?

Your subscription agreement determines the currency that is used for billing.
The currency code is shown on all Account Management cost views as a three-digit abbreviation (for example, USD, GBP, or EUR).
The applied currency code might not be displayed until after the first cost metrics are calculated.

### How can I view my usage from a previous license?

The [View your previous DPS periods via subscription history](/managed/license/subscription-history "View the subscription history of your Dynatrace environment, including usage and cumulative costs for each subscription.") page shows active and expired licenses and subscriptions, including POCs.

## Related topics

* [Account Management](/managed/manage/account-management "Manage your Dynatrace license, accounts, platform adoption, and environment health.")
* [Unavailable in Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)