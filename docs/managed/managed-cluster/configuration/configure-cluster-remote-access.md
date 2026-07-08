---
title: Configure Cluster remote access
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/configure-cluster-remote-access
---

# Configure Cluster remote access

# Configure Cluster remote access

* How-to guide
* 4-min read
* Updated on Jun 18, 2026

Dynatrace product experts can assist you remotely with Dynatrace Managed Cluster upgrades and troubleshooting when you run into problems. The prerequisite is that Dynatrace product experts need to have permission to remotely access your Managed Cluster. You can configure remote access permissions for your Managed Cluster to authorize Dynatrace product experts to provide you with updates and proactive support.

Admin required

You must have cluster administrator privileges for **Cluster Management Console (CMC)**.

## UI workflows

Use the CMC to configure remote access permissions for Dynatrace product experts.

### Configure remote access permissions

To configure the level of permissions within your Managed Cluster, in the **CMC**, go to **Settings** > **Remote access permissions**.

On this page, you can allow Dynatrace product experts remote access to your Managed Cluster. If this setting is enabled and events are detected, Dynatrace product experts can remotely adjust your Managed Cluster settings to ensure optimum performance and stability.

Security

All communication with Mission Control is secure and performed via HTTPS with browser-like certificate checks. All Dynatrace Managed configuration changes are fully audit-logged and each remote access is logged as a separate event (open **Events** to view the list of recorded events). The Mission Control team can't access certificates or user credentials. The Mission Control team also can't gain root access to any servers.

## API workflows

Use the Remote Access REST API to adjust remote access settings and permissions. For details, see [Dynatrace Cluster API](/managed/dynatrace-api/cluster-api/cluster-api-v2#remote-access "Find out about managing environments, network zones, Synthetic locations, nodes, and tokens in Dynatrace Managed using the Cluster API v2.").

## Remote access reference

Use this reference to compare remote access scopes and role permissions before you assign access to Dynatrace product experts.

### Remote access scopes

After you turn on Dynatrace remote access, you can set remote access permissions for Dynatrace product experts with one of the following scopes.

* **All**

  The entire Dynatrace product expert team can access your Managed Cluster to provide you with the full power of proactive support and optimize your Managed Cluster settings.
* **Read-only access to all**

  The entire Dynatrace product expert team can access your Managed Cluster but they can't edit any Managed Cluster settings. The read-only access option significantly limits the level of proactive support. With this option, only the **Viewer** role is available for a remote-access user. Dynatrace product experts will contact you to make required changes if necessary.
* **Approved**

  Only approved Dynatrace product experts can access your Managed Cluster. Your cluster administrators receive email notifications about pending remote access requests. The cluster administrator needs to approve each request to grant permissions. You can adjust the duration and role you grant. You can also grant permissions to known Dynatrace product experts up front.

  The Approved scope gives you maximum control over who can access your Managed Cluster, but it significantly impacts the Dynatrace product expert team's ability to provide you with proactive support.

### Remote access role permissions

You can assign the **Admin**, **User**, or **Viewer** role for a remote-access user. See the following table for details on the permissions each role is assigned.

| Permissions | Admin | User | Viewer | Description |
| --- | --- | --- | --- | --- |
| Environment | Applicable | Applicable | Applicable | Allows read-only access to an environment. Specifically, Dynatrace employees have access to:  * User-related settings—Signed-in user profile and signed-in user settings (for example, scheduled reports, favorite dashboards, and menu entries). * Dynatrace Hub pages - Installation pages for OneAgent or ActiveGate. * Settings in read-only mode. * Reports. * **CMC** in read-only mode. * Request data capture rules configuration in read-only mode. * Internal-only diagnostic data. * Audit log reading. * Support archive access. * Synthetic credential vault access and update/delete actions for credentials owned by the user.  Dynatrace employees can't change settings or install OneAgent with this permission alone. |
| Settings write | Applicable | Not applicable | Not applicable | Allows the user to change monitoring settings of an environment. |
| Download OneAgent and ActiveGate | Applicable | Not applicable | Not applicable | Allows the user to download OneAgent and ActiveGate from Hub and install on hosts. |
| **CMC** configuration change | Applicable | Not applicable | Not applicable | Allows the user to change cluster-related settings in **CMC**. |
| Logs | Applicable | Not applicable | Not applicable | Allows the user to access the Logs page and log content of your applications. Logs may have sensitive information. |
| Configure capture of sensitive data | Applicable | Not applicable | Not applicable | Allows the user to configure request-attribute capture rules. These can be used to capture elements such as HTTP headers or Post parameters for storage, filtering, and search. Also allows the user to manually trigger memory dumps. |
| View sensitive request data | Not applicable | Not applicable | Not applicable | Allows the user to view personal data captured by Dynatrace, including permission to download memory dumps. Users who don't have this permission see that the data point exists, but the personal data is masked by asterisks (\*\*\*\*\*). Also allows the user to manually trigger memory dumps. |
| Enable OneAgent debug flags | Applicable | Applicable | Not applicable | Allows the user to run read-only diagnostic operations and set OneAgent debug flags. |
| Run diagnostic operations | Applicable | Not applicable | Not applicable | Allows the user to run diagnostic operations such as service restarts, run diagnostic scripts on Managed Cluster node hosts, and access the database. |
| Replay session data with masking | Applicable | Applicable | Applicable | Allows the user to replay [recorded user sessions](/managed/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.") with [playback masking rules](/managed/observe/digital-experience/session-replay/configure-session-replay-web#masking-preset-options "Configure monitoring consumption and data privacy settings for Session Replay Classic.") applied at the time of replay. Note that data masked during recording is never captured and therefore is always masked during replay. |
| Replay session data without masking | Not applicable | Not applicable | Not applicable | Allows the user to replay recorded user sessions without playback masking rules applied. Note that any data masked during recording is always masked during replay. |
| Manage security problem | Not applicable | Not applicable | Not applicable | Allows the user to manage problems reported by Dynatrace Application Security. |
| View security problems | Applicable | Not applicable | Not applicable | Allows the user to view security problems. |