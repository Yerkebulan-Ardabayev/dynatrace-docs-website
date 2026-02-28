---
title: Account Management
source: https://www.dynatrace.com/docs/manage/account-management
scraped: 2026-02-28T21:15:29.327441
---

# Account Management

# Account Management

* Latest Dynatrace
* Explanation
* 5-min read
* Updated on Jun 24, 2025

Dynatrace Account Management provides a single place to:

* Manage Dynatrace license and subscriptions
* Manage Dynatrace users and SSO access (for SaaS deployments only; for Managed accounts, this is done in Cluster settings)
* Monitor Dynatrace platform adoption and environment health

## Access

### Web UI

To open **Account Management** through the web UI:

* **Latest Dynatrace**: select your user name in the lower-left corner, and then select **Account Management**.
* **Previous Dynatrace**: select the user icon in the upper-right corner, and then select **Account settings**.

  ![Display the user menu](https://dt-cdn.net/images/user-menu-86-9ab2cd2961.png)

### Browser address

To access Account Management directly from your browser address line, go to [https://myaccount.dynatrace.com/ï»¿](https://myaccount.dynatrace.com/).

### Permissions

For information on the permissions needed to access Account Management, see [Account Management permissions](/docs/manage/identity-access-management/permission-management/account-management-permissions "Dynatrace permissions required to access Account Management").

## Top-level navigation

The uppermost level of Account Management has three tabs to manage your information.

### My accounts

![Account Management: My accounts](https://dt-cdn.net/images/account-management-my-accounts-569-b7d835311e.png)

The **My accounts** tab displays your accounts.

* Select the account you want to manage.
* After you select the account you want to manage, you can bookmark the account-specific page for direct access the next time.

To return to the **My accounts** tab later, open  in the upper-right corner and select **My accounts**.

### My profile

![Account Management: My profile](https://dt-cdn.net/images/account-management-my-profile-571-20958f7605.png)

Use the **My profile** tab to update your user profile and notification options.

* **My profile**âinformation about you, such as your name, job title, and location.

  The time zone setting here is informational and does not affect any Dynatrace functionality other than report generation for [dashboard subscriptions in Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic/dashboards/subscribe-to-dashboard-reports "Learn how to subscribe to reports generated from Dynatrace dashboards.").
* **Environment notifications**âlists environments for which you can enable email-based notification for outages.

To return to the **My profile** tab later, open  in the upper-right corner and select you account name.

### My platform tokens

![Account Management: My platform tokens](https://dt-cdn.net/images/account-management-my-platform-tokens-578-bcbc9af2e1.png)

Platform tokens allow to interact with the Dynatrace platform via API for external integrations or scripting. For details, see [Platform tokens](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Create personalised platform tokens to access Dynatrace services via the API in your user context.").

To return to the **My platform tokens** tab later, open  in the upper-right corner and select **Platform tokens**.

## Account-level navigation

After you select an account on the **My accounts** tab, **Account Management** shows a menu bar on a large display.

* On a small display, the menu bar collapses to a smaller ![Menu](https://dt-cdn.net/images/account-management-icon-hamburger-c275e8015b.svg "Menu") menu with the same options.
* The menu options available to you depend on your deployment type, user permissions, and license model.

#### Examples

![Account Management menu bar example: License](https://dt-cdn.net/images/account-management-header-license-736-374ccfea23.png)

![Account Management menu bar example: Subscription](https://dt-cdn.net/images/account-management-header-subscription-870-da77a8f47b.png)

### Home

Select **Home** from anywhere in **Application Management** to return to the main page for the selected account.

### License / Subscription

* **License** is displayed for classic contracts
* **Subscription** is displayed for DPS

Open the **License** or **Subscription** menu to:

* View license/subscription usage and consumption history
* View a forecast of future usage

* View all license quota notifications for SaaS and Managed licenses

#### Overview

* **License** > **Overview**

  Consumption is based on various types of monitoring units that are consumed by your Dynatrace environments during the monitoring of your applications and related services.
* **Subscription** > **Overview**

  Dynatrace Platform Subscription: Consumption is based on various types of monitoring units that are consumed by your Dynatrace environments during the monitoring of your applications and related services. Values shown represent deduction from your annual commit.

### Identity & access management

For Dynatrace SaaS customers, and for Dynatrace Platform Subscription deployments using the SaaS model, open the **Identity & access management** (IAM) menu to manage:

* User groups and permissions
* Users and groups with SAML in Dynatrace SaaS
* Users and groups with SCIM in Dynatrace SaaS
* API OAuth tokens for the Account Management API

IAM for Dynatrace Managed deployments is managed within each cluster. For details, see [Managed - managed-user-groupsï»¿](https://docs.dynatrace.com/managed/shortlink/managed-user-groups).

#### People

Use **Identity & access management** > **People** to invite and assign users to groups to manage Dynatrace permissions and access.

#### Groups

Use **Identity & access management** > **Group management** to create user groups to manage Dynatrace permissions and access for users assigned to those groups.

#### Policies

Use **Identity & access management** > **Policy management** to manage Dynatrace policies.

#### Domain verification

Use **Identity & access management** > **Domain verification** to create verify account domains for use in SSO configurations like SAML or SCIM.

#### SAML configuration

Use **Identity & access management** > **SAML configuration** to configure user authentication for multiple domains. If you want to use your corporate credentials for authentication in Dynatrace SaaS, you can set up SAML to delegate the authentication to your identity provider. As a prerequisite, you need to verify ownership of your domain by adding a resource record to your domain.

#### SCIM configuration

Use **Identity & access management** > **SCIM configuration** to manage user identities in cloud-based applications and services. SCIM is used to automate the exchange of user identities between different domains and systems. You need to add and verify ownership of the domain to which your users belong before generating tokens and completing SCIM configuration.

#### API OAuth clients

Use **Identity & access management** > **OAuth clients** to configure and manage account API OAuth clients. The Account Management API helps you manage your account and its users. For example, you can manage access to Dynatrace environments by creating groups with various access levels and then associating these groups with users.

### Lens

The **Lens** feature of Account Management provides you with insights into platform adoption and health, helping you to understand how Dynatrace is used within your organization and recommend areas for optimization.

For details on Lens, see [Lens](/docs/manage/account-management/lens "Get insights Dynatrace adoption and health.").

#### Adoption

The **Lens** > **Adoption** page gives you insight into platform adoption and health:

* User activity
* Which technologies are being monitored across Dynatrace
* How monitored hosts are deployed (license type, platform type)
* How many synthetic tests are running
* How many problem notification integrations are defined

For details, see [Adoption](/docs/manage/account-management/lens#adoption "Get insights Dynatrace adoption and health.").

#### Environments

**Lens** > **Environments** offers:

* An overview of how many technologies are detected and monitored by Dynatrace over time.
* A host-centric summary of the environments in your Dynatrace deployment.
* A summary of how many monitored hosts are deployed across the cloud.
* A summary of how many public and private synthetic tests have been running across your environments.
* A high-level summary of how many API tokens are defined, how many problem notification integrations are defined, how many PaaS integrations are in use, and how many session exports are defined.

For details, see [Environments](/docs/manage/account-management/lens#environments "Get insights Dynatrace adoption and health.").

### Settings

Use **Settings** to specify general account information.

For details, see [Settings](/docs/manage/account-management/settings "Configure account contact, billing, and shipping information.").

### Contact information

Use **Settings** > **Contact information** to specify account contact, billing, and shipping information.

### Environments

Use **Settings** > **Environments** to list environments and, with **Action** > **Edit environment**, change the selected environment's name or time zone.

The time zone setting here is informational and does not affect any Dynatrace functionality other than report generation for [dashboard subscriptions in Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic/dashboards/subscribe-to-dashboard-reports "Learn how to subscribe to reports generated from Dynatrace dashboards.").

## Back to Account Settings

Select **Back to Account Settings** to purchase or extend a Dynatrace account.

## Notifications



Select ![Notifications](https://dt-cdn.net/images/account-management-icon-notifications-8f074dc2ad.svg "Notifications") **Notifications** to view the notification history for your budget and cluster or environment limits.

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

Select  **Profile** to verify the account you're signed in under, list your accounts, list your platform tokens, or sign out.