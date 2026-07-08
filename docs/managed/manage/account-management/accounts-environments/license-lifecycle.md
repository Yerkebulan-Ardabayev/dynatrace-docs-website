---
title: Your license lifecycle
source: https://docs.dynatrace.com/managed/manage/account-management/accounts-environments/license-lifecycle
---

# Your license lifecycle

# Your license lifecycle

* Explanation
* 3-min read
* Updated on Oct 19, 2025

This page describes the lifecycle of Dynatrace Managed licenses.
It explains how licenses affect your consumption of Dynatrace services.

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

With an active Dynatrace license, you can consume Dynatrace services according to the [monitoring consumption rules](/managed/license/monitoring-consumption-classic "Understand how Dynatrace classic monitoring consumption is calculated, including host units, DDUs, DEM units, and Application Security units.") and the terms and conditions of your contract.

You can view your consumption and the remaining quotas of your license in [Account Management](/managed/manage/account-management "Manage your Dynatrace license, accounts, platform adoption, and environment health.") or via the [Dynatrace Platform Subscription API](/managed/dynatrace-api/account-management-api/dynatrace-platform-subscription-api "Query the data about your Dynatrace Platform Subscription via the Account Management API.").
Additionally, you can download consumption details via the [Cluster API](/managed/dynatrace-api/cluster-api/cluster-api-v2/export-license-data/get-export-license-data-hour "Learn how to export aggregated hourly license usage as a ZIP file for an hour.").

## Expired licenses

Dynatrace licenses expire when (whichever come first):

* The license end date is reached.
* All subscribed services have been consumed.
* The subscription is otherwise terminated according to the terms of your contract.

When a license expires:

* Access to the Dynatrace web UI and API is blocked.
* No more data is ingested.
* You can still access the Cluster Management Console to see license details or manage cluster settings.
* Your Dynatrace Cluster administrator can perform specific REST API management actions via the management console.  
  This includes, for example, managing license deployment, switching a license key, or [retrieving monitoring consumption data](/managed/dynatrace-api/cluster-api/cluster-api-v2/export-license-data/get-export-license-data-hour "Learn how to export aggregated hourly license usage as a ZIP file for an hour.").

All ingested data is saved for 30 days after the expiration of your license.
If you extend your license during this period, data ingest will restart and you will regain access to your saved data.
However, there will be no data for the time between license expiration and license extension.

## Deleted license

After 30 days, maintenance operations and updates become unavailable.
Your monitoring data will still be stored on-premises, that is within your physical data storage system according to your storage and data retention policies.
You are responsible for deleting your captured Dynatrace monitoring data.

## Data retention

Different types of monitored data are stored for different periods of time.
For more information, see [Data retention periods](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods "Review default and configurable retention periods for service, RUM Classic, synthetic, Log Monitoring, metric, diagnostic, and security data in Dynatrace Managed.").