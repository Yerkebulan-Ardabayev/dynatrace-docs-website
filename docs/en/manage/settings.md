---
title: Settings
source: https://www.dynatrace.com/docs/manage/settings
scraped: 2026-02-20T21:26:07.391644
---

# Settings

# Settings

* Latest Dynatrace
* App
* 4-min read
* Published Sep 04, 2025

![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** is a preinstalled Dynatrace app that allows you to easily manage all the settings in your environment in a central place.

It serves as a central entry point to system-wide configurations. You can use it to control how your data is collected, processed, stored, and analyzed.

![The settings app structure reflects a top-down view of the settings that control how data is gathered and processed.](https://cdn.hub.central.dynatrace.com/hub/console/drafts/148/media/Settings_overview.png)![You can filter settings by title, description, or section.](https://cdn.hub.central.dynatrace.com/hub/console/drafts/148/media/Settings_search.png)

1 of 2The settings app structure reflects a top-down view of the settings that control how data is gathered and processed.

## Prerequisites

* To access ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings**:

  A user must belong to a group bound to the [Standard user](/docs/manage/identity-access-management/permission-management/default-policies#DynatraceAccessStandardUser "Dynatrace default policies reference") default policy.
* To modify ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings**:

  A user must belong to a group bound to the [Pro user](/docs/manage/identity-access-management/permission-management/default-policies#DynatraceAccessProUser "Dynatrace default policies reference") default policy.

See the minimum scope of permissions required to use ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** in case you want to create your own policy.

Permission

Description

settings:objects:read

Read a settings object

app-settings:objects:read

Read app settings

settings:schemas:read

Required for knowing which Settings Classic links to display

settings:objects:admin

Required for checking the admin access to the given settings object

settings:objects:write

Not used for writing, required for reading certain settings (e.g. GWT)

storage:entities:read

Required to fetch the list of entities in platform search

storage:fieldsets:read

Required to fetch the list of entities in platform search

storage:system:read

Required to fetch the recent modified entities from Grail

storage:buckets:read

Required to fetch the recent modified entities from Grail

10

rows per page

Page

1

of 1

Note that the access to selected settings can be further limited using tailored IAM policies, where users have access only to those settings where they have permissions assigned. For more information, see [Permissions](#permissions).

## Use cases

With ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings**, you can:

* Quickly find and discover all settings in the environment that are relevant to data gathering, processing, and analysis.
* Access a subset of this configuration or a read-only view, depending on the permissions of a user.

## Concepts

Get to know the following concepts to understand how Dynatrace settings work.

### Scope and hierarchy of settings

Many settings can be set for different scopes (for an entire monitoring environment or a specific entity). The default scope is global (the entire monitoring environment).

The most specific setting always takes precedence. For example, a configuration on the host level overrides a configuration on the host-group level, and in turn, a host-group level configuration overrides an environment-level configuration.

### Access to settings

Access to settings is controlled via [IAM policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies"). Policies enable you to create flexible and granular access to configurations, where users have access only to those settings where they have permissions assigned. No additional permissions are needed for policies to take effect. Policies grant access to configurations via both the ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** and the Settings API unless configured otherwise on the schema level.

If you need to configure fine-grained access to certain entities, you can do so via for example, a host group or security context.

To learn how to configure access policies for settings, see [IAM policy reference](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#settings "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

### Settings of individual Dynatrace Apps

![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** is extensible and it automatically displays the settings pages installed through other apps.

### Manage settings programmatically

You can manage Dynatrace settings centrally, with all the benefits of a version control system like change history, reviews, approval, generating the settings programmatically.

Dynatrace provides you with two options:

#### Dynatrace Settings API

You can manage Dynatrace settings programmatically using the Settings API. This API allows you to create, update, retrieve, and delete settings objects within Dynatrace. Here's how you can approach it.

The settings are passed to Dynatrace as the JSON payload for the settings object. The JSON structure depends on the particular feature and is determined by Settings schemas.

For more information, see [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

#### Monaco

The Dynatrace Monaco CLI provides general support for any Settings 2.0 schema available in your environment. Monaco is the Dynatrace approach to configuration as code. It enables you to manage your monitoring environment through configuration files, offering a range of features to streamline the process.

For more information, see [Configuration as Code via Monaco overview](/docs/deliver/configuration-as-code/monaco "Manage your Dynatrace environment using Dynatrace Configuration as Code via Monaco.").

## Related topics

* [Dynatrace settings framework](/docs/manage/settings/settings-20 "Introduction to the Settings 2.0 framework")
* [Settings 2.0 - Available schemas](/docs/dynatrace-api/environment-api/settings/schemas "View the entire settings schemas table of your monitoring environment via the Dynatrace API.")
* [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.")