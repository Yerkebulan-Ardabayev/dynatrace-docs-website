---
title: Set access control in OpenPipeline
source: https://www.dynatrace.com/docs/platform/openpipeline/getting-started/set-access-control
scraped: 2026-03-06T21:37:26.951279
---

# Set access control in OpenPipeline


* Latest Dynatrace
* How-to guide
* 3-min read
* Published Jan 09, 2026

This guide explains how pipeline and custom ingest source owners, as well as administrators, can configure and manage access through the web UI or API.

## Prerequistes

* Dynatrace version 1.322 and earlierYou migrated your OpenPipeline configurations to the Settings API.
* Verify that the user or user group permissions are sufficient for the access type you want to grant.
* To carry out the procedures via API, ensure `ownerBasedAccessControl` property is set to `true` for the OpenPipeline Settings API schema you intend to use.

  Access control default API values

  When you set the property for the first time, the following default values are added automatically.

  | Property | Description | Supported values | Default value |
  | --- | --- | --- | --- |
  | `owner` | The user who first changed the settings object. | A user, a user group, or `all-users`. | `all-users` |
  | `accessor` | The users who can access the object, depending on their permissions. | One or multiple users or user groups, or `all-users` | `all-users` |

  Available Settings API schemas

  + builtin:openpipeline.bizevents.ingest-sources
  + builtin:openpipeline.bizevents.pipelines
  + builtin:openpipeline.bizevents.routing
  + builtin:openpipeline.davis.events.ingest-sources
  + builtin:openpipeline.davis.events.pipelines
  + builtin:openpipeline.davis.events.routing
  + builtin:openpipeline.davis.problems.ingest-sources
  + builtin:openpipeline.davis.problems.pipelines
  + builtin:openpipeline.davis.problems.routing
  + builtin:openpipeline.events.ingest-sources
  + builtin:openpipeline.events.pipelines
  + builtin:openpipeline.events.routing
  + builtin:openpipeline.events.sdlc.ingest-sources
  + builtin:openpipeline.events.sdlc.pipelines
  + builtin:openpipeline.events.sdlc.routing
  + builtin:openpipeline.events.security.ingest-sources
  + builtin:openpipeline.events.security.pipelines
  + builtin:openpipeline.events.security.routing
  + builtin:openpipeline.logs.ingest-sources
  + builtin:openpipeline.logs.pipelines
  + builtin:openpipeline.logs.routing
  + builtin:openpipeline.metrics.ingest-sources
  + builtin:openpipeline.metrics.pipelines
  + builtin:openpipeline.metrics.routing
  + builtin:openpipeline.security.events.ingest-sources
  + builtin:openpipeline.security.events.pipelines
  + builtin:openpipeline.security.events.routing
  + builtin:openpipeline.spans.ingest-sources
  + builtin:openpipeline.spans.pipelines
  + builtin:openpipeline.spans.routing
  + builtin:openpipeline.system.events.ingest-sources
  + builtin:openpipeline.system.events.pipelines
  + builtin:openpipeline.system.events.routing
  + builtin:openpipeline.user.events.ingest-sources
  + builtin:openpipeline.user.events.pipelines
  + builtin:openpipeline.user.events.routing
  + builtin:openpipeline.user.sessions.ingest-sources
  + builtin:openpipeline.user.sessions.pipelines
  + builtin:openpipeline.user.sessions.routing

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

Once administrators set permissions and owners set access, users can manage and access items accordingly. Development teams can start configuring processing for their use cases. To learn more about processing, see Configure a processing pipeline.

## Related topics

* [Developer - Owner-based access controlï»¿](https://developer.dynatrace.com/develop/data/store-app-settings/#owner-based-access-control)