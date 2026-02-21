---
title: Manage IAM policies
source: https://www.dynatrace.com/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt
scraped: 2026-02-21T21:15:45.990267
---

# Manage IAM policies

# Manage IAM policies

* Latest Dynatrace
* How-to guide
* 7-min read
* Updated on Aug 20, 2025

Use these procedures in the Dynatrace web UI to manage Dynatrace [IAM](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies") policies.

API alternative

To instead use the API to manage IAM policies, go to [Dynatrace Account Management API 1.0ï»¿](https://dt-url.net/vr03thr).

## List IAM policies

To list configured IAM policies

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **Identity & access management** > **Policy management**.
2. Review the table of all existing policies that you can bind to user groups.

   * **Name**âthe name of the policy
   * **Description**âa brief description of the policy
   * **Source**â`global`, `account`, or `environment`
   * **Actions**âview, edit, or delete that row's policy (actions available to you depend on your permission level)

### Default policies

To let you use policies right away, Dynatrace IAM is shipped with built-in global policies.

* On the **Policies** page, in the **Source** column, they're all set to `Dynatrace`
* They're predefined and managed by Dynatrace
* You can apply a built-in policy by [assigning it to a group](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies") for the whole account or to any environment.
* You can inspect themâselect **View policy** in the **Actions** columnâbut you can't edit them

## Create a policy

To create a policy

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **Identity & access management** > **Policy management**.
2. Select **Create policy**.
3. Enter the following information.

   Element

   Description

   Name

   The name of the policy.

   Description

   A brief description of the policy.

   Organization level

   Each policy has a level that determines its scope:

   * `global`: These policies are predefined and managed by Dynatrace, and they apply to all accounts and environments. They cannot be edited.
   * `account`: These policies apply to all environments under that account (customer). Use them to set company-wide policies.
   * `environment`: These policies apply only to a single customer environment.

   Organization levels are restricted in the UI to the `account` level (other levels are still available via API).
   Restriction in UI was provided to avoid confusion between *creating* and *binding*.
   Commonly creating multiple identical policies on the `environment` levels can be achieved in a more efficient way by defining one policy on the `account` level and binding it to `environment` levels.

   Policy statement

   A statement specifying exactly what this policy allows.

   Example: Policy for Settings 2.0 Write

   ```
   ALLOW settings:objects:read;



   ALLOW settings:objects:write;



   ALLOW settings:schemas:read;
   ```

   You can combine multiple permissions in a single statement. Here is the same example combined into a single statement:

   ```
   ALLOW settings:objects:read, settings:objects:write, settings:schemas:read;
   ```

   Combining statements is particularly useful for managing policies with complicated conditions.

### Services

For a complete and up-to-date list of Dynatrace services that support permission management via IAM policies, see [IAM policy reference](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

## Edit a policy

To edit an existing policy

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **Identity & access management** > **Policy management**.
2. Find the policy you want to edit.  
   You can filter and sort the table.
3. Select **Actions** > **Edit policy**.
4. Make your changes and select **Save**.

## Delete a policy

To delete a policy

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **Identity & access management** > **Policy management**.
2. Find the policy you want to delete.  
   You can filter and sort the table.
3. Select **Actions** > **Delete** for the policy.

## Copy a policy

To copy an existing policy

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **Identity & access management** > **Policy management**.
2. Find the policy you want to copy.  
   You can filter and sort the table.
3. Select the **Edit** button for the policy.
4. Copy the contents of **Policy statement** to the clipboard.
5. Go back to the **Policies** page.
6. Select **Create policy**.
7. Paste the copied policy statements into **Policy statement**.
8. Fill in the **Name** and optional **Description**.
9. Select **Create policy**.

## Apply a policy to a group

To apply a policy to a group, you need to bind the policy to the group. For details on managing group permissions with IAM, see [Working with policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies").