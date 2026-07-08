---
title: Cluster Management Console
source: https://docs.dynatrace.com/managed/managed-cluster/basics/cluster-management-console
---

# Cluster Management Console

# Cluster Management Console

* Explanation
* 5-min read
* Updated on May 08, 2026

The Cluster Management Console is the administration interface for the Managed Cluster. Use it to manage the Managed Cluster infrastructure and all environments hosted on it. The Cluster Management Console is separate from the monitoring environment UI. Only users with cluster admin permissions can access it.

![Cluster Management Console](https://dt-cdn.net/images/screenshot-2026-03-12-at-10-30-21-1837-e8bbf2f12e.png)

Cluster Management Console

## Home

**Home** displays the **Dynatrace Managed deployment overview**, with a graphical representation of your deployment at a glance.

* [Environments](#environments)—Displays the number of active environments. Links to [Environments](#environments).
* [ActiveGates](#deployment-status-ag)—Displays the number of Cluster ActiveGates and Environment ActiveGates. Links to [Deployment status](#deployment-status).
* [Cluster nodes](#deployment-status-cluster-nodes)—Displays the number of Cluster nodes.
* [Last backup](/managed/managed-cluster/operation/back-up-and-restore-a-cluster "Understand the steps and commands required to restore a Dynatrace Managed cluster.")—Displays the date and storage location of the last backup.
* [Events](#events)—Displays the number of log events.
* [Users](#user-authentication)—Displays the number of users and user groups.
* [Dynatrace Mission Control](/managed/managed-cluster/basics/mission-control-proactive-support "Mission Control proactively monitors your Managed Cluster, provides software updates, and keeps your installation secure and reliable.")—Provides access to Mission Control proactive support.

## Deployment status

**Deployment status** provides an overview of your Cluster infrastructure.

### Cluster nodes

* For details on a cluster node, expand its row.
* To install a cluster node, select **Install cluster node** in the upper-right corner.

### ActiveGates

* For details on an ActiveGate, expand its row.
* To install a cluster ActiveGate, select **Install Cluster ActiveGate** in the upper-right corner.

### Network zones

* For details on a network zone, select its name in the table.

## Environments

**Environments** displays a table of all Dynatrace environments you manage.

* To find an environment, use the filters on the left.
* To open an environment's details screen, select the environment name.

  + To change an environment-specific setting, select  for that setting.  
    Sections include:

    - Capability settings
    - Storage settings
    - Cluster overload prevention settings
    - Assign environment permissions to user groups
  + To go to the selected Dynatrace environment, select  **Go to environment** in the upper-right corner.
  + To disable the selected Dynatrace environment, select ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More") > **Disable environment** in the upper-right corner.
  + To export the configuration of the selected Dynatrace environment, select ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More") > **Export configuration** in the upper-right corner.

## Events

**Events** lists log events by message and timestamp.

* Filter the table by:

  + Severity level
  + Timeframe
  + String search
* Page through the table with the controls under the table.

## User authentication

**User authentication** links to user-related settings.

* **User accounts**—Lists user accounts. Select a user to view details and group assignments and permissions. For details, see [user and group management](/managed/manage/identity-access-management/user-and-group-management "User and group management").
* **User groups**—Lists user groups. Select  for a group to configure the group name, permissions, and policies. For details, see [user and group management](/managed/manage/identity-access-management/user-and-group-management "User and group management").
* **Policy management**—Lists policies. Select a policy in the **Actions** column to view or edit it.
* **User sessions**—Lists user sessions. For details, see [user sessions](/managed/managed-cluster/configuration/manage-user-sessions "Learn how to define the maximum number of concurrent user sessions, terminate active sessions, and configure automatic sign-out in Dynatrace Managed.").
* **Password policy**—For details, see [password complexity rules](/managed/managed-cluster/configuration/password-complexity-rules "Configure password complexity rules for Dynatrace Managed, including minimum length, character categories, default policy values, and best practices.").
* **User repository**—View and edit user repository settings. For details, see [LDAP](/managed/manage/identity-access-management/user-and-group-management/manage-users-and-groups-with-ldap "Learn how to connect your Dynatrace Server to an LDAP server to import user groups or accounts that need access to your Dynatrace Managed environment.").
* **Single sign-on settings**—For details, see [SAML settings](/managed/manage/identity-access-management/user-and-group-management/manage-users-and-groups-with-saml "Learn how to connect your Dynatrace Server to a SAML server to import user groups or accounts that need access to your Dynatrace Managed environment.") and [OpenID Connect settings](/managed/manage/identity-access-management/user-and-group-management/manage-users-and-groups-with-openid "Learn how to use OpenID as an SSO IdP for the management of users and groups.").
* **Login screen**—For details, see [sign-in customization](/managed/managed-cluster/configuration/customize-login-page "Learn how to customize the sign-in page in Dynatrace Managed to display system information, authentication details, legal notices, or an administrator contact.").

## Settings

**Settings** links to cluster-related settings.

* **Public endpoints**
* **Internet proxy**—For details, see [Configure internet proxy](/managed/managed-cluster/configuration/configure-internet-proxy "Configure a proxy connection for your Managed Cluster if you don't have direct internet access. Supported protocols include Basic and NTLMv1.").
* **Emails**

  + **SMTP server**—Configure how email notifications for the cluster are delivered. For details, see [Configure SMTP server connection](/managed/managed-cluster/configuration/configure-smtp-server-connection "Learn how to configure an SMTP server connection on your Managed Cluster, including connection security, mail server settings, and delivery method options.").
  + **Email notifications**—Configure email notification recipients.
* **Preferences**—For details, see [Configure Cluster preferences](/managed/managed-cluster/configuration/configure-cluster-preferences "Configure cluster preferences to manage proactive support reporting, remote access, data privacy, domain name, and community settings for your Managed Cluster.").
* **Remote access permissions**—For details, see [Configure Cluster remote access](/managed/managed-cluster/configuration/configure-cluster-remote-access "Configure remote access permissions for your Managed Cluster, including scope options and role assignments for Dynatrace product experts.").
* **API tokens**—For details, see [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").
* **Backup**—For details, see [Backup and restore a cluster](/managed/managed-cluster/operation/back-up-and-restore-a-cluster "Understand the steps and commands required to restore a Dynatrace Managed cluster.").
* **Service Providers**
* **Automatic update**—For details, see [Update a cluster](/managed/managed-cluster/operation/update-cluster "Learn how to update a Managed cluster and how to schedule an automatic update.").

## Licensing

**Licensing** displays account and licensing information.

To verify your connection to [Mission Control](/managed/managed-cluster/basics/mission-control-proactive-support "Mission Control proactively monitors your Managed Cluster, provides software updates, and keeps your installation secure and reliable."), select ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More") > **Check Mission Control connection** in the upper-right corner.

## Audit log

**Audit log** lists events triggered by the cluster and selected configuration changes for all environments.

This table shows only changes related to cluster-wide configuration, licensing, storage quota, and permissions. For all environment audit log entries, use the [Audit Logs API](/managed/dynatrace-api/environment-api/audit-logs/get-log "View full audit log via Dynatrace API.").