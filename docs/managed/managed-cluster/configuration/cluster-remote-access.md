---
title: Cluster remote access
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/cluster-remote-access
scraped: 2026-05-12T11:36:54.659420
---

# Cluster remote access

# Cluster remote access

* Updated on Aug 11, 2022

Dynatrace product experts can assist you remotely with Dynatrace Managed cluster upgrades and troubleshooting when you run into problems. The prerequisite is that Dynatrace product experts need to have permission to remotely access your Dynatrace Managed cluster. You can configure remote access permissions for your Dynatrace Managed cluster to authorize Dynatrace product experts to provide you with updates and pro-active support.

Admin required

You must have cluster administrator privileges to access Cluster Management Console.

To configure the level of permissions within your cluster, in the **Cluster Management Console**, go to **Settings** > **Remote access permissions**.

On this page, you can allow Dynatrace product experts remote access to your cluster. If this setting is enabled and events are detected, Dynatrace product experts can remotely adjust your cluster settings to ensure optimum performance and stability.

Security

All communication with Mission Control is secure and performed via HTTPS with browser-like certificate checks. All Dynatrace Managed configuration changes are fully audit-logged and each remote access is logged as a separate event (go to **Events** to view the list of recorded events). The Mission Control team can't access certificates or user credentials. They also can't gain root access to any servers.

Once Dynatrace remote access is enabled, you can set remote access permissions for Dynatrace product experts with one of the following scopes.

* **All**

  The entire Dynatrace product expert team can access your cluster to provide you with the full power of pro-active support and optimize your cluster settings.
* **Read-only access to all**

  The entire Dynatrace product expert team can access your cluster but they can't edit any cluster settings. This option significantly limits the level of pro-active support. With this option, only the **Viewer** role is available for a remote-access user. Dynatrace product experts will contact you to make required changes if necessary.
* **Approved**

  Only approved Dynatrace product experts can access your cluster. Your cluster administrators receive an email notifications about pending remote access requests. The cluster administrator needs to approve each request to grant permissions. You can adjust the duration and role you grant. You can also grant permissions to known Dynatrace product experts up front.

  This scope gives you maximum control over who can access your cluster, but it significantly impacts the Dynatrace product expert team's ability to provide you with pro-active support.

  You can assign the **Admin**, **User**, or **Viewer** role for a remote-access user. Refer to the following table for details on the permissions each role is assigned.

  | Permissions | Admin | User | Viewer | Description |
  | --- | --- | --- | --- | --- |
  | Environment | Applicable | Applicable | Applicable | Allows read-only access to an environment. Specifically, Dynatrace employees have access to:  + User-related settings â Signed-in user profile and signed-in user settings (for example, scheduled reports, favorite dashboards, and menu entries). + Dynatrace Hub pages - Installation pages for OneAgent or ActiveGate. + Settings in read-only mode. + Reports. + Cluster Management Console in read-only mode. + Request data capture rules configuration in read-only mode. + Internal-only diagnostic data. + Audit log reading. + Support archive access. + Synthetic credential vault access and update/delete actions for credentials owned by the user.  Dynatrace employees cannot change settings or install OneAgent with this permission alone. |
  | Settings write | Applicable | Not applicable | Not applicable | Allows the user to change monitoring settings of an environment. |
  | Download OneAgent and ActiveGate | Applicable | Not applicable | Not applicable | Allows the user to download OneAgent and ActiveGate from Hub and install on hosts. |
  | Cluster Management Console configuration change | Applicable | Not applicable | Not applicable | Allows the user to change Cluster-related settings in Cluster Management Console. |
  | Logs | Applicable | Not applicable | Not applicable | Allows the user to access the Logs page and log content of your applications. Logs may have sensitive information. |
  | Configure capture of sensitive data | Applicable | Not applicable | Not applicable | Allows the user to configure request-attribute capture rules. These can be used to capture elements such as HTTP headers or Post parameters for storage, filtering, and search. Also allows the user to manually trigger memory dumps. |
  | View sensitive request data | Not applicable | Not applicable | Not applicable | Allows the user to view potentially personal data captured by Dynatrace, including permission to download memory dumps. Users who do not have this permission see that the data point exists, but the personal data is masked by asterisks (\*\*\*\*\*). Also allows the user to manually trigger memory dumps. |
  | Enable OneAgent debug flags | Applicable | Applicable | Not applicable | Allows the user to execute read-only diagnostic operations and set OneAgent debug flags. |
  | Execute diagnostic operations | Applicable | Not applicable | Not applicable | Allows the user to execute diagnostic operations such as service restarts, run diagnostic scripts on cluster node hosts, and access the database. |
  | Replay session data with masking | Applicable | Applicable | Applicable | Allows the user to replay [recorded user sessions](/managed/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.") with [playback masking rules](/managed/observe/digital-experience/session-replay/configure-session-replay-web#masking-preset-options "Configure monitoring consumption and data privacy settings for Session Replay.") applied at the time of replay. Note that data masked during recording is never captured and therefore is always masked during replay. |
  | Replay session data without masking | Not applicable | Not applicable | Not applicable | Allows the user to replay recorded user sessions without playback masking rules applied. Note that any data masked during recording is always masked during replay. |
  | Manage security problem | Not applicable | Not applicable | Not applicable | Allows the user to manage problems reported by Dynatrace Application Security. |
  | View security problems | Applicable | Not applicable | Not applicable | Allows the user to view security problems. |

## API

You can also use the Remote Access REST API to adjust settings and remote-access permissions. For details, see [Dynatrace Cluster API](/managed/dynatrace-api/cluster-api/cluster-api-v2#remote-access "Find out about managing environments, network zones, Synthetic locations, nodes, and tokens in Dynatrace Managed using the Cluster API v2.").