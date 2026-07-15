---
title: View your previous DPS periods via subscription history
source: https://docs.dynatrace.com/managed/manage-your-costs/reference/subscription-history
---

# View your previous DPS periods via subscription history

# View your previous DPS periods via subscription history

* Explanation
* 4-min read
* Updated on Jul 16, 2025

The **Subscription history** page lists your expired, active, and pending Dynatrace subscriptions and licenses.
You can view details for all Dynatrace subscriptions that have been active in the last three years.

## Overview

Subscription history lets you review consumption from previous DPS subscription periods after a renewal, when the live overview switches to the new period. Historical data covers cost, usage, and capability breakdowns for any prior period your account has been active.

## Use cases

* Compare actual end-of-period consumption against last year's commitment.
* Pull historical capability breakdowns for budgeting or renewal negotiations.
* Audit how cost allocation changed across periods.

## Requirements

To view subscription history, you need:

* An active Dynatrace Platform Subscription that was signed after April 26, 2023.
* A Dynatrace user account with one or both of these [Account Management permissions](/managed/manage/identity-access-management/permission-management/account-management-permissions "Dynatrace permissions required to access Account Management"):

  + **View account**
  + **View and manage account and billing information**

## View subscription history

To view **Subscription history**

1. Go to [**Account Management**﻿](https://myaccount.dynatrace.com/).
2. Select **Subscription** > **History**.

This page provides easy access to details of your Dynatrace usage and the costs associated with each subscription and license.

![Account Management: Subscription history](https://dt-cdn.net/images/history-list-1600-dcce197542.png)

Account Management: Subscription history

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

### Can I see my Dynatrace Managed license history?

The Account Management portal offers a view on all past, active, and pending subscriptions, including your previous quota-based licenses.

## Related topics

* [License Dynatrace](/managed/license "Dynatrace Platform Subscription, capability rate cards, hybrid licensing, and previous license models.")
* [Account Management](/managed/manage/account-management "Manage your Dynatrace license, accounts, platform adoption, and environment health.")
* [Where to view your costs](/managed/manage-your-costs/view/where-to-look "View Dynatrace consumption and costs in Account Management, query billing events directly with DQL, or ask Dynatrace Intelligence in natural language.")
* [Billing report](/managed/manage-your-costs/view/billing-report "View your billing to see details about accrued costs per booking date. Use this view to determine which Dynatrace monitoring costs were recognized and booked on which day.")