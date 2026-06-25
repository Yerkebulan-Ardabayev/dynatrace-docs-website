---
title: Set budget alerts
source: https://docs.dynatrace.com/managed/license/budget-alerts
scraped: 2026-05-12T11:09:12.362166
---

# Set budget alerts

# Set budget alerts

* How-to guide
* 3-min read
* Updated on Mar 10, 2026

Use the Account Management **Budgets** tab to customize your Dynatrace Platform Subscription (DPS) budgets.
You can

* Define budgets at the account, environment, and capability level.
* Set up notifications to inform you when thresholds are exceeded.

Examples of supported use cases include:

* Receive notifications when your subscription reaches a given percentage of its annual commitment.
* Set a budget threshold of 10% of total subscription costs for a lower âsandboxâ environment.
* Set a fixed threshold for a new capability, and be notified when it reaches USD $1,000 in costs.

Budgets complement the existing [Customize cost alerts](/managed/license/cost-monitors "Learn how to use the Cost Monitors feature to make forecasts and cost events.") by allowing you to define custom thresholds at the environment and capability level.

To access **Budgets**, go to **Account Management** > **Subscription** > **Cost management** and select the **Budgets** tab.

Budget alerts are not available for trial licenses or Proofs-of-Concept.

![Budget Alerts overview page in Account Management](https://dt-cdn.net/images/budgets-overview-5760-88cc7aab8c.png)

Budget Alerts overview page in Account Management

## Best practices for budgets

A Dynatrace Platform Subscription automatically enables three initial budget thresholds that notify license administrators when total account level consumption reaches 75%, 90%, and 100% of the annual commitment.

By default, all users with the **View and manage account and billing information account permission** are notified when a budget is exceeded.
You can adjust these thresholds to suit your needs and add further recipients to ensure that the appropriate users are informed.

## Viewing your budgets

The **Budgets** tab shows all active budgets that are defined for your account.
Each budget is displayed as a card that shows:

* The total budget that has been consumed in the billing period.
* The cost threshold for the budget.
* A colored progress bar that compares the actual consumption against the cost threshold.

  + Blue: Less than 75% of the cost threshold has been consumed.
  + Brown: 75% or more of the cost threshold has been consumed.
  + Red: 100% or more of the cost threshold has been consumed.
* The number of configured environments.
* The number of configured capabilities.

## Create and edit budgets

Select a budget from the **Budgets** summary page to view and change its settings, or select **+ New budget** to create a new budget.
You can have up to 20 active budgets.

![Edit budget alerts in Account Management](https://dt-cdn.net/images/budgets-edit-5760-1e178f41f3.png)

Edit budget alerts in Account Management

Only users with the **View and manage account and billing information account** permission can create and change settings.

Each budget requires the following information:

* **Name**: Used to identify the budget in the Account Management portal and any notification email.
* **Monitored environment**: You can define a budget across all environments, or for specific environments.
  Select the environments that the budget applies to.
* **Monitored capabilities**: You can define a budget across all capabilities, or for one or more selected capabilities.
  Select the capabilities that the budget applies to.
* **Cost threshold type**: Whether a fixed value or a percentage of the annual DPS commitment.
* **Threshold amount**: The value, whether a fixed value or a percentage as defined in **Cost threshold type**.
* **Email notification details**: For each budget, you can define a list of email addresses to send notifications to when the budget is exceeded:

  + **Notify license administrators** sends notifications to all users with the permission: **View and manage account and billing information account permission.**
    To identify users with this permission, go to **Identity & access management** > **People**.
  + **Send to others** allows you to specify other email addresses of users that should receive budget notifications.
    Notification emails contain a link to Account Management, so recipients need the **View account access** permission.
  + **Subject**: Used in the email subject line (optional; if not defined, a default text will be used).
  + **Message**: Used in the email description (optional; if not defined, a default text will be used).

The new budget card will be visible within approximately 20 minutes.
Until then, it will display the message **Weâre creating your budget. Check back later to see cost data.**

Each budget card can be deleted.
Hover over the card, and then select  >  **Delete**.

## Budget notifications

When costs equal or exceed the defined threshold for the selected environments and capabilities, an email is sent to the users identified in the budget definition.

* Budget events and emails are only triggered when costs exceed a user-defined threshold.
* An email is sent only once on the day that the threshold is exceeded.
  If you define a threshold that is already exceeded, no email notification will be sent.
* When multiple budgets are exceeded simultaneously, a user will receive one email for each exceeded budget.
* Budget emails are sent from the email address `no-reply@dynatrace.com`.

Select **View your account** in any email notification to go to the Account Management **Notification Center**.

## Notification center

**Notification center** provides a history of all notifications sent from Account Management.
You can also view budget notifications.

To open **Notification center**, select  > **Notification center** in the Account Management toolbar.

## Related topics

* [Access your DPS cost overview](/managed/license/cost-overview "View license and subscription usage and consumption history for Dynatrace SaaS, Dynatrace Managed, and the Dynatrace platform subscription model.")
* [Account Management](/managed/manage/account-management "Manage your Dynatrace license, accounts, platform adoption, and environment health.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)