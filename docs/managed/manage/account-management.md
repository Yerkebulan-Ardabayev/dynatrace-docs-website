---
title: Account Management
source: https://docs.dynatrace.com/managed/manage/account-management
---

# Account Management

# Account Management

* Explanation
* 5-min read
* Updated on Oct 08, 2026

Dynatrace Account Management provides a single place to:

* Manage Dynatrace license and subscriptions.
* Monitor Dynatrace platform adoption and environment health.

## Access

### Web UI

To open **Account Management** through the web UI, select the user icon in the upper-right corner, and then select **Account settings**.

![Display the user menu](https://dt-cdn.net/images/user-menu-86-9ab2cd2961.png)

Display the user menu

### Browser address

To access Account Management directly from your browser address line, go to [https://myaccount.dynatrace.com/﻿](https://myaccount.dynatrace.com/).

### Permissions

For information on the permissions needed to access Account Management, see [Account Management permissions (Dynatrace Classic)](/managed/manage/identity-access-management-classic/permission-management/account-management-permissions-classic "Dynatrace permissions required to access Account Management").

## Top-level navigation

The uppermost level of Account Management has three tabs to manage your information.

### My accounts

![Account Management: My accounts](https://dt-cdn.net/images/account-management-my-accounts-569-b7d835311e.png)

Account Management: My accounts

The **My accounts** tab displays your accounts.

* Select the account you want to manage.
* After you select the account you want to manage, you can bookmark the account-specific page for direct access the next time.

To return to the **My accounts** tab later, open  in the upper-right corner and select **My accounts**.

### My profile

![Account Management: My profile](https://dt-cdn.net/images/account-management-my-profile-571-20958f7605.png)

Account Management: My profile

Use the **My profile** tab to update your user profile and notification options.

* **My profile**—information about you, such as your name, job title, and location.

  The time zone setting here is informational and does not affect any Dynatrace functionality other than report generation for [dashboard subscriptions in Dashboards Classic](/managed/analyze-explore-automate/dashboards/share-a-dashboard "Share a dashboard with specific users, groups, anyone with the link, or anonymous viewers, and subscribe people to weekly or monthly email reports.").
* **Environment notifications**—lists environments for which you can enable email-based notification for outages.

To return to the **My profile** tab later, open  in the upper-right corner and select you account name.

## Account-level navigation

After you select an account on the **My accounts** tab, **Account Management** shows a menu bar on a large display.

* On a small display, the menu bar collapses to a smaller  menu with the same options.
* The menu options available to you depend on your deployment type, user permissions, and license model.

![Account Management menu bar example: License](https://dt-cdn.net/images/account-management-header-license-736-374ccfea23.png)

Account Management menu bar example: License

![Account Management menu bar example: Subscription](https://dt-cdn.net/images/account-management-header-subscription-870-da77a8f47b.png)

Account Management menu bar example: Subscription

### Home

Select **Home** from anywhere in **Account Management** to return to the main page for the selected account.

### License / Subscription

* **License** is displayed for classic contracts
* **Subscription** is displayed for DPS

Open the **License** or **Subscription** menu to:

* View license/subscription usage and consumption history
* View a forecast of future usage
* View all license quota notifications

#### Overview

* **License** > **Overview**

  Consumption is based on various types of monitoring units that are consumed by your Dynatrace environments during the monitoring of your applications and related services.
* **Subscription** > **Overview**

  Dynatrace Platform Subscription: Consumption is based on various types of monitoring units that are consumed by your Dynatrace environments during the monitoring of your applications and related services. Values shown represent deduction from your annual commit.

### Identity & access management

IAM for Dynatrace Managed deployments is managed within each cluster. For details, see [User groups, permissions, and policies](/managed/manage/identity-access-management/user-and-group-management/user-groups-and-permissions "Learn about the supported permissions and policies, how you can assign them to groups, and how you can manage your users and groups.").

### Lens

The **Lens** feature of Account Management provides you with insights into platform adoption and health, helping you to understand how Dynatrace is used within your organization and recommend areas for optimization.

For details on Lens, see [Lens](/managed/manage/account-management/lens "Get insights Dynatrace adoption and health.").

#### Adoption

The **Lens** > **Adoption** page gives you insight into platform adoption and health:

* User activity
* Which technologies are being monitored across Dynatrace
* How monitored hosts are deployed (license type, platform type)
* How many synthetic tests are running
* How many problem notification integrations are defined

For details, see [Adoption](/managed/manage/account-management/lens#adoption "Get insights Dynatrace adoption and health.").

#### Environments

**Lens** > **Environments** offers:

* An overview of how many technologies are detected and monitored by Dynatrace over time.
* A host-centric summary of the environments in your Dynatrace deployment.
* A summary of how many monitored hosts are deployed across the cloud.
* A summary of how many public and private synthetic tests have been running across your environments.
* A high-level summary of how many API tokens are defined, how many problem notification integrations are defined, how many PaaS integrations are in use, and how many session exports are defined.

For details, see [Environments](/managed/manage/account-management/lens#environments "Get insights Dynatrace adoption and health.").

### Settings

Use **Settings** to specify general account information.

For details, see [Settings](/managed/manage/account-management/settings "Configure account contact, billing, and shipping information.").

### Contact information

Use **Settings** > **Contact information** to specify account contact, billing, and shipping information.

### Environments

Use **Settings** > **Environments** to list environments and, with **Action** > **Edit environment**, change the selected environment's name or time zone.

The time zone setting here is informational and does not affect any Dynatrace functionality other than report generation for [dashboard subscriptions in Dashboards Classic](/managed/analyze-explore-automate/dashboards/share-a-dashboard "Share a dashboard with specific users, groups, anyone with the link, or anonymous viewers, and subscribe people to weekly or monthly email reports.").

## Back to Account Settings

Select **Back to Account Settings** to purchase or extend a Dynatrace account.

## Notifications

Select  **Notifications** to view the notification history for your budgets and cost monitors.

For more information, see [Notification center](/managed/manage/account-management/notifications "Learn about Account Management notifications, for example budget alerts and cost monitor events.").

## Support resources

Select  **Support** to go to a support resource:

* Support Center
* Documentation
* Community
* University
* Support tickets

## Chat

Select  **Chat** to contact a product specialist.

## Profile

Select  **Profile** to verify the account you're signed in under, list your accounts, or sign out.