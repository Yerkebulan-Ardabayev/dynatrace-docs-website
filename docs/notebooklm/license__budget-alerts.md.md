# Dynatrace Documentation: license/budget-alerts.md

Generated: 2026-02-16

Files combined: 1

---


## Source: budget-alerts.md


---
title: Set budget alerts
source: https://www.dynatrace.com/docs/license/budget-alerts
scraped: 2026-02-16T09:23:31.075120
---

# Set budget alerts

# Set budget alerts

* Latest Dynatrace
* How-to guide
* 1-min read
* Updated on Nov 03, 2025

Use the Account Management **Budgets** tab to customize your Dynatrace Platform Subscription (DPS) budgets.
You can

* Define budgets at the account, environment, and capability level.
* Set budget thresholds.
* Set up notifications to inform you when thresholds are exceeded.

Examples of supported use cases include:

* Receive notifications when your subscription reaches 75%, 90%, and 100% of its annual commitment.
* Set a budget threshold of 10% of total subscription costs for a lower âsandboxâ environment.
* Set a fixed threshold for a new capability and be notified when it reaches USD 1,000 in costs.

Budgets complement the existing [Customize cost alerts](/docs/license/cost-monitors "Learn how to use the Cost Monitors feature to make forecasts and cost events.") by allowing you to define custom thresholds at the environment and capability level.

By default you have three budgets, which alert you when your consumption reaches 75%, 90%, and 100% of your license commitment.

To access **Budgets**, go to **Account Management** > **Subscription** > **Cost management** and select the **Budgets** tab.

Dynatrace license administrators can also access cost management information from the Account Management **Notification center** page.

## Best practices for budgets

A Dynatrace Platform Subscription automatically enables three initial budget thresholds that notify license administrators when total account level consumption reaches 75%, 90%, and 100% of the annual commitment.

By default, all users with the **View and manage account and billing information account permission** are notified when a budget is exceeded, ensuring that license administrators are notified without having to configure settings.
You can adjust these thresholds to suit your needs, and customize the email distribution list to ensure that the appropriate users are informed.

## Viewing your budgets

The **Budgets** tab shows all active budgets that are defined for your account.
Each budget is displayed as a card that shows

* The total budget that has been consumed in the billing period.
* The cost threshold for the budget.
* A colored progress bar that compares the actual consumption against the cost threshold.

  + Blue: Less than 75% of the cost threshold has been consumed.
  + Brown: 75% or more of the cost threshold has been consumed.
  + Red: 100% or more of the cost threshold has been consumed.
* The relevant environments.
* The relevant capabilities.

![Budget cards](https://dt-cdn.net/images/budget-screen-cards-1920-8c0134e0c1.png)

## Creating and editing budgets

Select a budget from the **Budgets** summary page to view and change its settings, or select **+ Budget** to create a new budget.
You can have up to 20 active budgets.

Only users with the **View and manage account and billing information account** permission can create and change settings.

Each budget requires the following information:

* **Name:** Used to identify the budget in the Account Management portal and any notification email.
* **Monitored environment:** You can define a budget across all environments or for specific environments.
  Select the environments that the budget applies to.
* **Monitored capabilities:** You can define a budget across all capabilities or for one or more selected capabilities.
  Select the capabilities that the budget applies to.
* **Threshold type:** Can be a fixed value or expressed as a % of the annual DPS commitment.
* **Email notification details:** Each budget defines a list of email addresses to send notifications to when the budget is exceeded:

  + **Notify license administrators** sends notifications to all users with the permission: **View and manage account and billing information account permission.**
  + To identify users with this permission, select **People** from the **Identity & Access Management** menu option, and select **Account level** scope and **View and manage account and billing information** to filter the list of users with this specific permission.
  + **Send email to additional users on this account** allows you to specify other email addresses of users that should receive budget notifications.
    Notification emails contain a link to Account Management, so recipients need the **View account access** permission.
  + **Subject:** Used in the email subject line.
  + **Message:** Used in the email description.

![Budgets](https://dt-cdn.net/images/budget-edit-75pct-1920-efc09bf9b7.png)

Each budget card can be deleted.
Hover over the card, and then select  >  **Delete**.

![Delete budget card](https://dt-cdn.net/images/screenshot-12-03-2025-11-04-31-555-f50546a78b.png)

## Budget notifications

Budgets are evaluated each day, always before 12:00:00 UTC.

When a new budget is initially created, the budget card displays the message: `Weâre creating your budget. Check back later to see cost data.` and a gray status bar.

![Budgets](https://dt-cdn.net/images/budget-creation-card-862-77b4cbab8d.png)

When costs equal or exceed the defined threshold for the selected environments and capabilities, an email is sent to the users identified in the budget definition.
An email is sent only once on the day that the threshold is exceeded.

When multiple budgets are exceeded simultaneously, a user will receive one email for each exceeded budget.

Budget emails are sent from the email address `no-reply@dynatrace.com`.

Select **View your account** in any email notification to go to the Account Management **Notification Center**.

![Budgets notification](https://dt-cdn.net/images/budget-email-example-1-1209-ca6f4b7b5c.png)

Budget events and emails are only triggered when costs exceed a user-defined threshold.
If you define a threshold that is already exceeded, no budget event will be triggered and no email notification will be sent.

## Notification center

**Notification center** provides a history of all budget events and other events tracked by Account Management.
To open **Notification center**, select  **Notifications** in the Account Management toolbar.

## Related topics

* [Account Management](/docs/manage/account-management "Manage your Dynatrace license, subscriptions, and platform adoption and environment health.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)


---
