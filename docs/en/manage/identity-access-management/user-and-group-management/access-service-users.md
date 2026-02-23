---
title: Service users
source: https://www.dynatrace.com/docs/manage/identity-access-management/user-and-group-management/access-service-users
scraped: 2026-02-23T21:27:58.430299
---

# Service users

# Service users

* Latest Dynatrace
* How-to guide
* 3-min read
* Updated on Dec 05, 2025

An administrator or a user belonging to a group with `View and manage users and groups` permission can perform the service user management activities listed here.

## What's a service user?

A service user is a non-interactive user: it can't sign in to Dynatrace and it isn't related to any real person. It has its own identity and access management permissions assigned directly.

You can select a service user as the actor of a [workflow](/docs/analyze-explore-automate/workflows/security#service-users "Guide on security aspects of workflow automation in Dynatrace Workflows") or [custom alert](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app#service-user "Explore anomaly detection configurations using the Anomaly Detection app.").

## Use case

When workflows and custom alerts are executed in the context of a service user, it makes them independent of the status of the user who maintains them. This makes it a good fit for a department or production use cases, or any collaborative efforts where a dependency on an actual user could hinder your work. Using a service user also strengthens the security of the actions executed by the actor.

## List and edit service users

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/). If you have more than one account, select the account you want to manage.
2. Go to **Identity & access management** > **Service users**.

   A table lists the defined service users.
3. In the **Actions** column for the user you want to edit, select  >  **Edit**.
4. In the **Edit service user** page, you can:

   * Change the **Name**
   * Change the **Description**

**Note**: You can't change the service user email address. It's the identifier used in policy statements. See [Create policies based on a service user](#policy).

5. On the **Select group** section, you can add or remove the selected groups. Service users get permissions via the selected groups.
6. Select **Save**.

## Create service user

1. On the **Service users** page, select  **Add service user**.
2. On the **Create service user** page, enter the following service user details.

   * **Name**
   * Optional **Description**

     **Tip**: Make sure they're both meaningful for environment admins so that they understand the purpose of the service user.
     The service user's email address is created automatically and can't be modified. It's the identifier used in the [policy statements](#policy).
3. In the **Assign permissions** section, select whether to assign permissions **Through existing groups** or **Directly**.

   * **Through existing groups**: Select one or more existing groups whose permissions you want to assign to this service user.
   * **Directly**: Make your own custom selection of permissions. A new group will be automatically created.

     1. On the **Assign permissions** tab, select a **Permission**, **Scope**, and **Boundaries** to assign to this service user.
     2. On the **View permissions** tab, verify the details of the selected permission.
4. Select **Create**.

## User permissions to use service users as actors

A user who wants to use a service user as an actor of a workflow or custom alert must be granted the `iam:service-users:use` permission.

That permission is granted with the following default policies:

* [Dynatrace Pro User](/docs/manage/identity-access-management/permission-management/default-policies#DynatraceAccessProUser "Dynatrace default policies reference")
* [Dynatrace Admin User](/docs/manage/identity-access-management/permission-management/default-policies#DynatraceAccessAdminUser "Dynatrace default policies reference")

## Create policies based on a service user

To control the use of service users even further, you can create a policy allowing users to use only specific service users as workflows or custom alerts actors.

To do that, create a policy with `iam:service-users:use` set to the `iam:service-user-email` condition

For example:

```
ALLOW iam:service-users:use



WHERE iam:service-user-email IN ("be820735-3114-4d40-9c44-dfa18fa62be9@service.sso.dynatrace.com");
```

Such policies are secure. You can't modify the service user identifier or assign a custom email address to a service user.