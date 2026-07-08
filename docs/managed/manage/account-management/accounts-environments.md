---
title: About Dynatrace licenses, accounts, environments, and users
source: https://docs.dynatrace.com/managed/manage/account-management/accounts-environments
---

# About Dynatrace licenses, accounts, environments, and users

# About Dynatrace licenses, accounts, environments, and users

* Explanation
* 2-min read
* Published Mar 16, 2026

This page describes how Dynatrace handles various administrative concepts, which are organized in hierarchical levels.
These are, from the most general to the most specific:

* License: One license can be used by one or more accounts.
* Account: Each account can have one or more environments.
* Environment: Each environment can be accessed by one or more users.
* User: You log into a Dynatrace environment as a user.

The access to each of these layers is handled via permissions.
Each Dynatrace user has specific permissions: some users may access only data within specific environments, while others may access account-level data.

Usage is calculated at the environment level.

## What is a Dynatrace license?

A Dynatrace Platform Subscription license lets your environment consume Dynatrace monitoring features.

In most cases, exactly one account (through its associated environments) consumes from a single subscription.
With [DPS for Hybrid](/managed/license/dps-for-hybrid "DPS for Hybrid lets you share one subscription across multiple accounts."), it's also possible in certain cases to have multiple accounts consume from a single subscription.

Account administrators can use **Account Management** to view information about licenses or subscriptions.
For more information, see [Subscription or license overview](/managed/manage/account-management/license-subscription "View your Dynatrace license information, including budgets, cost analysis, and historical usage, for all license models.").
Usage is continuously metered, and you can monitor consumption, forecast costs, and manage budgets across environments and accounts.

## What is a Dynatrace account?

A Dynatrace account provides a single place to manage licenses and subscriptions, users, and SSO access.

An account can contain one or more environments, such as `test`, `pre-prod`, and `production`.

## What is a Dynatrace environment?

A Dynatrace environment is how you interact with Dynatrace monitoring features.

* You log into an environment.
* Within the environment, you can view your monitoring data and alerts.
* Queries are run against data that resides in the environment.

Each environment is identified by a unique ID, which you can find in both the Dynatrace UI and in the URL.
For more information, see [Environment ID](/managed/discover-dynatrace/get-started/monitoring-environment#environment-id "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.").
An example environment ID is `abc12345`.

In Dynatrace, usage is calculated at the environment level.

For more information about how an environment works technically, see [What's a monitoring environment?](/managed/discover-dynatrace/get-started/monitoring-environment "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.").

## What is a Dynatrace user?

You log into a Dynatrace environment as a Dynatrace user.

Permissions are granted to Dynatrace users.
Permissions let users, for example, administer Dynatrace accounts, configure Dynatrace deployments, or query Grail data.

Permissions are granted at either the account level or the environment level.
Account-level permissions apply to all environments in that account, while environment-level permissions apply only to that environment.

For more about permissions, see [Identity and access management (IAM)](/managed/manage/identity-access-management "Configure users, groups and permissions.").

## Related topics

* [License Dynatrace](/managed/license "Dynatrace Platform Subscription, capability rate cards, hybrid licensing, and previous license models.")
* [Account Management](/managed/manage/account-management "Manage your Dynatrace license, accounts, platform adoption, and environment health.")
* [Your license lifecycle](/managed/manage/account-management/accounts-environments/license-lifecycle "Understand your Dynatrace DPS or Classic license lifecycle, and how it affects your consumption of Dynatrace services.")
* [Access management](/managed/manage/identity-access-management/permission-management "Permission management")
* [User and group management](/managed/manage/identity-access-management/user-and-group-management "User and group management")