# Dynatrace Documentation: license/license-lifecycle.md

Generated: 2026-02-16

Files combined: 1

---


## Source: license-lifecycle.md


---
title: Your license lifecycle
source: https://www.dynatrace.com/docs/license/license-lifecycle
scraped: 2026-02-16T09:23:34.241579
---

# Your license lifecycle

# Your license lifecycle

* Latest Dynatrace
* Explanation
* 3-min read
* Updated on Oct 19, 2025

This page describes the lifecycle of Dynatrace SaaS licenses.
It explains how licenses affect your consumption of Dynatrace services.

On this page, the term "license" is synonymous with "contract."

For questions about your license, contact a Dynatrace product expert via live chat within your Dynatrace environment.

## License notifications

You're notified of all updates to your Dynatrace license via

* email notifications.
* notifications in the Dynatrace web UI.

This includes license activation notifications, upcoming license expiration notifications, and license deactivation notifications.

To view your notifications, go to **Account Management** > **Notifications**.

## New licenses

When you sign up for a free trial or subscribe to Dynatrace services, a new license is created and associated with your account.
You will receive a notification email that explains the details of your license and all contained subscriptions.

## Active licenses

Your license becomes active at its start date.

With an active Dynatrace license, you can consume Dynatrace services according to the [monitoring consumption rules](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") and the terms and conditions of your contract.

You can view your consumption and the remaining quotas of your license in [Account Management](/docs/manage/account-management "Manage your Dynatrace license, subscriptions, and platform adoption and environment health.") or via the [Dynatrace Platform Subscription API](/docs/dynatrace-api/account-management-api/dynatrace-platform-subscription-api "Query the data about your Dynatrace Platform Subscription via the Account Management API.").

## Expired licenses

Dynatrace licenses expire when (whichever come first):

* The license end date is reached.
* All subscribed services have been consumed.
* The subscription is otherwise terminated according to the terms of your contract.

When a license expires:

* Access to the Dynatrace web UI and API is blocked.
* No more data is ingested.

All ingested data is saved for 30 days after the expiration of your license.
If you extend your license during this period, data ingest will restart and you will regain access to your saved data.
However, there will be no data for the time between license expiration and license extension.

## Deleted license

All data is deleted 30 days following the date of expiration of your license:

* Your Dynatrace environment is shut down.
* All data, configurations, and settings related to your environment(s) are permanently deleted and cannot be restored.

## Data retention

Different types of monitored data are stored for different periods of time.
For more information, see [Data retention periods](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods "Check retention times for various data types.").


---
