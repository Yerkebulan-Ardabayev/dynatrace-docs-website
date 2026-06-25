---
title: Configure and manage user sessions
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/configure-manage-user-sessions
scraped: 2026-05-12T11:37:01.850150
---

# Configure and manage user sessions

# Configure and manage user sessions

* Published Apr 02, 2020

Dynatrace Managed can be accessed by numerous users belonging to various groups. The number of concurrent sessions per user account should be limited to the minimum required to perform job duties. Dynatrace Managed gives you the ability to control and limit the number of concurrent user sessions per user account.

Go to **User authentication** > **User sessions** to view or terminate any current user sessions. The user sessions view indicates the type of sign-in, when the sign-in occurred, and the IP address or device from which the sign-in occurred.

Sign-in types:

* `LOCAL` - Users that exist only in the cluster database and are local to the cluster
* `LDAP` - LDAP users
* `SSO` - Sign-in from your identity provider
* `DEVOPSTOKEN` - Sign-in from Mission Control pro-active support

To terminate a session, select ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove") and confirm the action. The session will immediately terminate and log out the user.

To modify the number of concurrent user sessions permitted, select **Configure concurrent sessions**. You can set different limits for regular users and admin users. Admin accounts are users who belong to any group that has global cluster-admin permissions.

To remove all session limits for administrators and regular user accounts, turn on **Unlimited concurrent sessions**.

Use the REST API to update automatic logout policy. By default, there's no auto logout of users who stay on auto-refreshable pages. See [Update cluster user sessions configuration](/managed/dynatrace-api/cluster-api/cluster-api-v2/user-management/update-cluster-user-sessions-configuration "Learn how to update Dynatrace Cluster user sessions configuration using API.")