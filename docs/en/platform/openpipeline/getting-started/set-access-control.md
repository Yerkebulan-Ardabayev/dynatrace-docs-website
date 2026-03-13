---
title: Set access control in OpenPipeline
source: https://www.dynatrace.com/docs/platform/openpipeline/getting-started/set-access-control
scraped: 2026-03-06T21:37:26.951279
---

# Set access control in OpenPipeline

# Set access control in OpenPipeline

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Jan 09, 2026

This guide explains how pipeline and custom ingest source owners, as well as administrators, can configure and manage access through the web UI or API.

## Prerequistes

* Dynatrace version 1.322 and earlierYou [migrated your OpenPipeline configurations to the Settings API](../migration-settings.md "Understand how to migrate your OpenPipeline configurations to new Settings API.").
* Verify that the user or user group permissions are sufficient for the access type you want to grant.
* To carry out the procedures via API, ensure `ownerBasedAccessControl` property is set to `true` for the OpenPipeline Settings API schema you intend to use.

  Access control default API values

  When you set the property for the first time, the following default values are added automatically.

  | Property | Description | Supported values | Default value |
  | --- | --- | --- | --- |
  | `owner` | The user who first changed the settings object. | A user, a user group, or `all-users`. | `all-users` |
  | `accessor` | The users who can access the object, depending on their permissions. | One or multiple users or user groups, or `all-users` | `all-users` |

  Available Settings API schemas

  + [builtin:openpipeline.bizevents.ingest-sources](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-bizevents-ingest-sources.md "View builtin:openpipeline.bizevents.ingest-sources settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.bizevents.pipelines](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-bizevents-pipelines.md "View builtin:openpipeline.bizevents.pipelines settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.bizevents.routing](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-bizevents-routing.md "View builtin:openpipeline.bizevents.routing settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.davis.events.ingest-sources](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-davis-events-ingest-sources.md "View builtin:openpipeline.davis.events.ingest-sources settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.davis.events.pipelines](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-davis-events-pipelines.md "View builtin:openpipeline.davis.events.pipelines settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.davis.events.routing](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-davis-events-routing.md "View builtin:openpipeline.davis.events.routing settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.davis.problems.ingest-sources](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-davis-problems-ingest-sources.md "View builtin:openpipeline.davis.problems.ingest-sources settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.davis.problems.pipelines](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-davis-problems-pipelines.md "View builtin:openpipeline.davis.problems.pipelines settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.davis.problems.routing](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-davis-problems-routing.md "View builtin:openpipeline.davis.problems.routing settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.events.ingest-sources](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-ingest-sources.md "View builtin:openpipeline.events.ingest-sources settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.events.pipelines](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-pipelines.md "View builtin:openpipeline.events.pipelines settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.events.routing](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-routing.md "View builtin:openpipeline.events.routing settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.events.sdlc.ingest-sources](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-sdlc-ingest-sources.md "View builtin:openpipeline.events.sdlc.ingest-sources settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.events.sdlc.pipelines](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-sdlc-pipelines.md "View builtin:openpipeline.events.sdlc.pipelines settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.events.sdlc.routing](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-sdlc-routing.md "View builtin:openpipeline.events.sdlc.routing settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.events.security.ingest-sources](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-security-ingest-sources.md "View builtin:openpipeline.events.security.ingest-sources settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.events.security.pipelines](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-security-pipelines.md "View builtin:openpipeline.events.security.pipelines settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.events.security.routing](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-security-routing.md "View builtin:openpipeline.events.security.routing settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.logs.ingest-sources](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-logs-ingest-sources.md "View builtin:openpipeline.logs.ingest-sources settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.logs.pipelines](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-logs-pipelines.md "View builtin:openpipeline.logs.pipelines settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.logs.routing](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-logs-routing.md "View builtin:openpipeline.logs.routing settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.metrics.ingest-sources](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-metrics-ingest-sources.md "View builtin:openpipeline.metrics.ingest-sources settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.metrics.pipelines](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-metrics-pipelines.md "View builtin:openpipeline.metrics.pipelines settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.metrics.routing](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-metrics-routing.md "View builtin:openpipeline.metrics.routing settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.security.events.ingest-sources](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-security-events-ingest-sources.md "View builtin:openpipeline.security.events.ingest-sources settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.security.events.pipelines](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-security-events-pipelines.md "View builtin:openpipeline.security.events.pipelines settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.security.events.routing](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-security-events-routing.md "View builtin:openpipeline.security.events.routing settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.spans.ingest-sources](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-spans-ingest-sources.md "View builtin:openpipeline.spans.ingest-sources settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.spans.pipelines](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-spans-pipelines.md "View builtin:openpipeline.spans.pipelines settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.spans.routing](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-spans-routing.md "View builtin:openpipeline.spans.routing settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.system.events.ingest-sources](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-system-events-ingest-sources.md "View builtin:openpipeline.system.events.ingest-sources settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.system.events.pipelines](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-system-events-pipelines.md "View builtin:openpipeline.system.events.pipelines settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.system.events.routing](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-system-events-routing.md "View builtin:openpipeline.system.events.routing settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.user.events.ingest-sources](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-user-events-ingest-sources.md "View builtin:openpipeline.user.events.ingest-sources settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.user.events.pipelines](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-user-events-pipelines.md "View builtin:openpipeline.user.events.pipelines settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.user.events.routing](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-user-events-routing.md "View builtin:openpipeline.user.events.routing settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.user.sessions.ingest-sources](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-usersessions-ingest-sources.md "View builtin:openpipeline.usersessions.ingest-sources settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.user.sessions.pipelines](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-usersessions-pipelines.md "View builtin:openpipeline.usersessions.pipelines settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.user.sessions.routing](../../../dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-usersessions-routing.md "View builtin:openpipeline.usersessions.routing settings schema table of your monitoring environment via the Dynatrace API.")

## Share access

When you create a pipeline or custom ingest source, you're the owner, and only you and the administrator have access to it. To share access with another Dynatrace user or user group

Via UI

Via API

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** and select a configuration scope.
2. Find the custom ingest source or pipeline in the table.
3. Open the  menu and select  **Share**.
4. Find and select the new accessor.
5. Select the access type:  **View** or  **Edit**.
6. Select **Save**.

To modify or revoke access,

1. Go to  (**Manage access**).
2. Expand the access type for the user to modify it or **Remove** it.

Set the `accessor` property value to the users or user groups that you want to share access with.

## Make public (or private)

When you create a pipeline or custom ingest source, you're the owner, and can share access with all users. To go public

Via UI

Via API

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** and select a configuration scope.
2. Find the custom ingest source or pipeline in the table.
3. Open  and select  **Share**.
4. Go to  (**Manage access**) and turn on **Visible to anyone in your environment (Read only)**.

To return to private, do one of the following

* Turn on **Visible to anyone in your environment (Read only)** to maintain specific accessors.
* Select  **Remove all access** to remove all access types for all users and user groups.

Set the `accessor` property value to `all-users`.

## Transfer ownership

When you create a pipeline or custom ingest source, you're the owner. To transfer ownership to another Dynatrace user or user group

Via UI

Via API

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** and select a configuration scope.
2. Find the custom ingest source or pipeline in the table.

1. Open the  menu and select  **Change owner**.
2. Find and select a new owner, and then select **Change owner**.

   Be aware that you'll lose all access unless the new owner gives you permission.
3. After the transfer is complete, the new owner will receive an email about the ownership transfer.

Set the `owner` property value to the user or user group that you want to share access with.

Be aware that you will lose all access unless the new owner gives you permission.

## Next steps

Once administrators set permissions and owners set access, users can manage and access items accordingly. Development teams can start configuring processing for their use cases. To learn more about processing, see [Configure a processing pipeline](tutorial-configure-processing.md "Configure ingest sources, routes, and processing for your data in OpenPipeline.").

## Related topics

* [Developer - Owner-based access controlï»¿](https://developer.dynatrace.com/develop/data/store-app-settings/#owner-based-access-control)