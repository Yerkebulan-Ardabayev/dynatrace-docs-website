---
title: Manage user sessions
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/manage-user-sessions
---

# Manage user sessions

# Manage user sessions

* How-to guide
* 1-min read
* Updated on Jun 18, 2026

To manage access to Dynatrace Managed, review active user sessions, terminate sessions when needed, and configure session limits.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Review user sessions**](/managed/managed-cluster/configuration/manage-user-sessions#review-user-sessions "Learn how to define the maximum number of concurrent user sessions, terminate active sessions, and configure automatic sign-out in Dynatrace Managed.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Terminate a user session**](/managed/managed-cluster/configuration/manage-user-sessions#terminate-user-session "Learn how to define the maximum number of concurrent user sessions, terminate active sessions, and configure automatic sign-out in Dynatrace Managed.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Configure concurrent sessions**](/managed/managed-cluster/configuration/manage-user-sessions#configure-concurrent-sessions "Learn how to define the maximum number of concurrent user sessions, terminate active sessions, and configure automatic sign-out in Dynatrace Managed.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Update automatic sign-out**](/managed/managed-cluster/configuration/manage-user-sessions#update-automatic-sign-out "Learn how to define the maximum number of concurrent user sessions, terminate active sessions, and configure automatic sign-out in Dynatrace Managed.")

## Step 1 Review user sessions

In the Cluster Management Console, go to **User authentication** > **User sessions**.

The user sessions view shows the sign-in method, when the sign-in occurred, and the IP address or device from which the sign-in occurred.

Sign-in types:

* `LOCAL` - Users that exist only in the Managed Cluster database and are local to the Managed Cluster
* `LDAP` - LDAP users
* `SSO` - Sign-in from your identity provider
* `DEVOPSTOKEN` - Sign-in from Mission Control proactive support

## Step 2 Terminate a user session

To terminate a session, select ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove") and confirm the action.

The session immediately terminates and signs out the user.

## Step 3 Configure concurrent sessions

Limit concurrent sessions per user account to the minimum required to perform job duties.

To modify the number of concurrent user sessions permitted, select **Configure concurrent sessions**. You can set different limits for regular users and admin users. Admin accounts are users who belong to any group that has global cluster-admin permissions.

To remove all session limits for administrators and regular user accounts, turn on **Unlimited concurrent sessions**.

## Step 4 Update automatic sign-out

Use the REST API to update the automatic sign-out policy. By default, there's no automatic sign-out for users who stay on pages that automatically refresh. See [Update cluster user sessions configuration](/managed/dynatrace-api/cluster-api/cluster-api-v2/user-management/update-cluster-user-sessions-configuration "Learn how to update Dynatrace Cluster user sessions configuration using API.").