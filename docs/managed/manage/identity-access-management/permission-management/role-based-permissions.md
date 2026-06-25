---
title: Role-based permissions
source: https://docs.dynatrace.com/managed/manage/identity-access-management/permission-management/role-based-permissions
scraped: 2026-05-12T11:08:46.345863
---

# Role-based permissions

# Role-based permissions

* Reference
* 2-min read
* Published Jul 01, 2024

Migrate roles to policies

Recommended

Dynatrace version 1.252+

Starting with Dynatrace version 1.252, you can manage role-based access using policies. For more information, see [Upgrade role-based permissions to Dynatrace IAM policies](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/migrate-roles "Manage access to a Dynatrace environment using security policies.").

Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/)âsee [Account Management](/managed/manage/account-management "Manage your Dynatrace license, accounts, platform adoption, and environment health.") for more information.

## Account permissions

Dynatrace provides the following account-level permissions.

* **View account**: Allows access to the account to view environment data (host hours, sessions, synthetic monitors) and Dynatrace Documentation (documentation) links. Also allows access to view and create support tickets and the Dynatrace Community user forum. There is no access to billing or user/group management.
* **View and manage account and billing information**: Allows access to payment data (credit card details), billing data (invoices), and contact information (company contact data).
* **View and manage users and groups**: Allows access to user management (add, edit, remove user group membership) and group management (create, edit, delete groups).

## Environment permissions

Dynatrace provides the following environment-level permissions. Select all that apply:

* **View environment:** Allows read-only access to the environment. You cannot change settings or install OneAgent with this permission alone.

  **View environment** permission is required for any of the other environment permissions, so **View environment** is automatically selected for the environment when you select any other environment permission.

* **View sensitive request data:** Allows viewing of potentially [personal data captured by Dynatrace](/managed/manage/data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace "Find out what types of end-user data may be captured during Dynatrace monitoring and the methods that are available for masking personal end-user data."), including downloading memory dumps. Users who do not have this permission see that the data point exists but the personal data is masked by asterisks (`*****`). Also allows manually triggering [memory dumps](/managed/observe/application-observability/profiling-and-optimization/memory-dump-analysis "Learn how Dynatrace enables you to trigger, download and analyze memory dumps for Java and Node.js.").

* **View logs:** Allows access to sensitive log file data in the **Logs** tab.

  The **View logs** role bypasses any existing conditional access you may have defined in policy boundaries through the [storage logs permission](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#storage-logs-read "Complete reference of IAM policies and corresponding conditions across all Dynatrace services."). To have those conditions adhered to, consider expressing the same **View logs** permissions within a policy statement leveraging the equivalent [environment log viewer permission](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#environment-roles-logviewer "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

* **Replay session data with masking:** Allows replay of [recorded user sessions](/managed/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.") with [playback masking rules](/managed/observe/digital-experience/session-replay/configure-session-replay-web#masking-preset-options "Configure monitoring consumption and data privacy settings for Session Replay.") applied at the time of replay. Note that any data masked during recording is never captured and, therefore, always masked during replay.
* **Replay session data without masking:** Allows replay of recorded user sessions without playback masking rules applied. Note that any data masked during recording is always masked during replay.

* **Install OneAgent**: Allows download of OneAgent and installation on hosts. To change/edit settings, you must provide the **Manage monitoring settings** permission.
* **Manage monitoring settings**: Allows changing of all environment settings. To install OneAgent, you must provide the **Install OneAgent** permission.
* **Manage capturing of sensitive request data**: Allows configuration of request-attribute capture rules. These can be used to capture elements such as HTTP headers or Post parameters for storage, filtering, and search. Also allows manually triggering memory dumps.

* **Manage support tickets:** Allows access to all support tickets that have been created for this environment.

* **Manage security problems:** Allows viewing and management of vulnerabilities reported by Dynatrace Application Security.
* **View security problems:** Allows viewing (but not management) of vulnerabilities reported by Dynatrace Application Security.

For details on Application Security permissions, see [Fine-tune permissions](/managed/secure/application-security#restrict-permissions-managed "Access the Dynatrace Application Security functionalities.").

## Management zone permissions

Dynatrace provides the following management-zone-level permissions. Select all that apply:

* **View environment:** Allows read-only access to the entities within the management zone. To change/edit settings, you must provide the **Change monitoring settings** permission.

  **View environment** permission is required for any of the other management zone permissions, so **View environment** is automatically selected for the management zone when you select any other management zone permission.

* **View sensitive request data:** Allows viewing of potentially [personal data captured by Dynatrace](/managed/manage/data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace "Find out what types of end-user data may be captured during Dynatrace monitoring and the methods that are available for masking personal end-user data.") for the entities within the management zone. Users who do not have this permission see that the data point exists but the personal data is masked by asterisks (`*****`)âsee also [**Environment permissions**](#environment) above.

* **View logs:** Allows access to sensitive log file data in the **Logs** tab for hosts explicitly included within the management zone. Note that it is not sufficient to provide management-zone-level access to the host groups that the hosts belong toâsee [Management zone rules](/managed/manage/identity-access-management/permission-management/management-zones/management-zone-rules "Define rules to limit the entities accessible within a management zone.") for details.

* **Replay session data with masking:** Allows replay of [recorded user sessions](/managed/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.") with [playback masking rules](/managed/observe/digital-experience/session-replay/configure-session-replay-web#masking-preset-options "Configure monitoring consumption and data privacy settings for Session Replay.") applied at the time of replay. Note that any data masked during recording is never captured and, therefore, always masked during replay.
* **Replay session data without masking:** Allows replay of recorded user sessions without playback masking rules applied. Note that any data masked during recording is always masked during replay.

  For Session Replay permissions to work within a management zone, the user also needs to have access to the requisite applications.

  + If a user session spans multiple applications that are not all assigned to the management zone, users can see still see and replay the session. However, user actions associated with the application to which you do not have access are masked and the corresponding part of the replay is not shown.
  + Playback buttons are grayed out for users who have access to applications but do not have permission to replay sessions.

  Example Session Details page: settings

  ![Session replay in a management zone](https://dt-cdn.net/images/sessionreplaymzmultipleapps1-1574-1ef406ad09.png)

  Session replay in a management zone

  Example Session Details page: notifications

  ![Session replay in a management zone](https://dt-cdn.net/images/sessionreplaymzmultipleapps2-2335-554ce06cae.png)

  Session replay in a management zone

  For details on management zones, see [Management zones](/managed/manage/identity-access-management/permission-management/management-zones "Learn about management zones concepts, how to define management zones, and how to make the most of them.").

* **Manage monitoring settings:** Allows the changing of entity settings within a management zone, for example, the ability to record or edit synthetic monitors. It also grants access to some items in the global settings menu but only allows making modifications to assigned management zones. For example, problem alerting profiles can only be created and changed for a specific management zone.

* **Manage security problems:** Allows viewing and management of vulnerabilities reported by Dynatrace Application Security.
* **View security problems:** Allows viewing (but not management) of vulnerabilities reported by Dynatrace Application Security.

For details on Application Security permissions, see [Fine-tune permissions](/managed/secure/application-security#restrict-permissions-managed "Access the Dynatrace Application Security functionalities.").

## Relationship between environment and management zone permissions

When you provide any permission other than **View environment** at the environment level, **View environment** is automatically enabled as well for the environment. Likewise, when you provide any permission other than **View environment** at the management-zone level, **View environment** is automatically enabled for the management zone.

[Management zones](/managed/manage/identity-access-management/permission-management/management-zones "Learn about management zones concepts, how to define management zones, and how to make the most of them.") are designed to provide targeted and limited access to certain entities within an environment. If you wish to provide a permission to users accessing a management zone, we recommend that you use the [management-zone-level permissions](#mz). Any permission you provide at the environment level supersedes and adds to those at the management-zone level. In other words, management-zone permissions cannot be used to limit permissions already provided at the environment level.

Take the example of a management zone containing three hosts out of five total hosts in an environment. If you grant the **View logs** permission to the management zone, viewers can see the **Logs** tab with information for the three hosts in the management zone. However, if you remove the same permission at the management-zone level and provide it at the environment level, users will be able to:

* Access **All** management zones from the management zones filter on the menu bar.
* See the **Logs** tab for all five hosts in the environment when viewing **All** management zones.
* See the **Logs** tab for the three hosts in the assigned management zone when they switch to it.