---
title: DPS permissions
source: https://docs.dynatrace.com/managed/license/dps-permissions
---

# DPS permissions

# DPS permissions

* Reference
* Published Jun 26, 2026

Dynatrace offers several features to help you understand your Dynatrace Platform Subscription costs . To be able to use some of these features, you'll need to have a user account with specific permissions to retrieve data at the account, environment, or subscription level.

This page describes the permissions that you need to understand your DPS consumption and costs.

## DPS permissions overview

The following table gives an overview of the different use cases and required permissions.
The sections on this page describe each use case in more detail, such as setup instructions.

| Use case | Method | Required permissions |
| --- | --- | --- |
| View DPS usage and cost in the UI | Account Management | Account Management permissions:  * **View account** (read only) * **View and manage account and billing information** (read/write) |
| Export usage data via API | Account Management API | OAuth client with `account-uac-read` scope and subject user with `account-viewer` or `account-company-info` permission. |

## How to configure permissions

### Account Management

License managers can view DPS consumption and cost directly in the Dynatrace UI under **Account Management** > **Subscription** > **Overview** > **Cost and usage details** > **Usage summary**.

To access this data, your user account must have one of the following Account Management permissions:

| Permission | What you can do |
| --- | --- |
| **View account** | View DPS consumption, usage, and subscription history. |
| **View and manage account and billing information** | All of the above, plus Cost Management features. |

These permissions are granted in Account Management by a license administrator with the **View and manage users and groups** permission. For more information, see [Account Management permissions](/managed/manage/identity-access-management/permission-management/account-management-permissions "Dynatrace permissions required to access Account Management").

### Account Management API

You can query DPS consumption programmatically via the Account Management API to integrate into external reporting.

To do this, create an OAuth client with the **Allow read access for usage and consumption resources** (`account-uac-read`) scope.

To create an OAuth client, go to **Account Management** > **Identity & access management** > **OAuth clients**.
For more information, see [Dynatrace Platform Subscription API - GET usage](/managed/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/usage/get-usage "Check how your Dynatrace Platform Subscription is used via the Account Management API.").

## Related topics

* [Account Management permissions](/managed/manage/identity-access-management/permission-management/account-management-permissions "Dynatrace permissions required to access Account Management")
* [About Dynatrace licenses, accounts, environments, and users](/managed/manage/account-management/accounts-environments "Key concepts to understand your Dynatrace user, account, its associated environments, and how it consumes from a Dynatrace subscription or license.")
* [Identity and access management (IAM)](/managed/manage/identity-access-management "Configure users, groups and permissions.")
* [Account Management](/managed/manage/account-management "Manage your Dynatrace license, accounts, platform adoption, and environment health.")