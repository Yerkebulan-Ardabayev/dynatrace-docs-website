---
title: View your previous DPS periods via subscription history
source: https://www.dynatrace.com/docs/license/subscription-history
scraped: 2026-02-20T21:11:42.075383
---

# View your previous DPS periods via subscription history

# View your previous DPS periods via subscription history

* Latest Dynatrace
* Tutorial
* 4-min read
* Updated on Jul 16, 2025

The **Subscription history** page lists your expired, active, and pending Dynatrace subscriptions and licenses.
You can view details for all Dynatrace subscriptions that have been active in the last three years.

## Requirements

To view subscription history, you need:

* An active Dynatrace Platform Subscription that was signed after April 26, 2023.
* A Dynatrace user account with one or both of these [Account Management permissions](/docs/manage/identity-access-management/permission-management/account-management-permissions "Dynatrace permissions required to access Account Management"):

  + **View account**
  + **View and manage account and billing information**

## View subscription history

To view **Subscription history**

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/).
2. Select **Subscription** > **History**.

This page provides easy access to details of your Dynatrace usage and the costs associated with each subscription and license.

Cost information for POC subscriptions (identified with the type `DPS:POC`) is provided for informational purposes only.
You are not actually charged any of these costs, as POCs are free of charge according to your POC license.

For more information about POCs, see [Proof of Concept for existing DPS subscriptions](/docs/license/proof-of-concept "Use Account Management tools to view consumption during your DPS Proof of Concept period.").

![Account Management: Subscription history](https://dt-cdn.net/images/history-list-1600-dcce197542.png)

## View details

To display subscription details, find the relevant subscription and select **View details**.
The **History** window opens with information about **Budget summary** and **Cost and usage details**.

* The **Budget summary** shows:

  + The total used budget, as a percentage of the annual budget.
  + The budget forecast: the actual costs, projected costs, and the annual budget.
* Cost and usage details are provided in two tabs.

  + The **Cost summary** tab shows the actual costs (in local currency) based on your consumption during the subscription period.
  + The **Usage summary** tab shows the environment usage according to the capability's unit of measure.

Cost and usage details are available for all environments and capabilities provided with the subscription.
You can drill down to focus on individual environments and capabilities.

## FAQ

### My Dynatrace Platform Subscription started before April 26, 2023. Can I access subscription history?

The **Subscription history** page is available for

* Customers with a Dynatrace Platform Subscription that started on or after April 26, 2023.
* Customers who have migrated from a Dynatrace classic license to a Dynatrace Platform Subscription (DPS) license can view their subscriptions.
  Any previous DPS and quota-based licenses will also be displayed.

### Why can't I see host unit hours, user sessions, or custom metrics and log details for my Dynatrace SaaS subscription?

Only contracts with Host Unit, DEM, and DDU features are shown. If you were licensed using the older feature capabilities, details are not displayed.

## Related topics

* [License Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")