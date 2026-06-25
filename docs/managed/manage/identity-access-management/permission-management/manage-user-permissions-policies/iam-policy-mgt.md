---
title: Manage IAM policies
source: https://docs.dynatrace.com/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt
scraped: 2026-05-12T11:49:53.325675
---

# Manage IAM policies

# Manage IAM policies

* How-to guide
* 7-min read
* Updated on Aug 20, 2025

Use these procedures in the Dynatrace web UI to manage Dynatrace [IAM](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies") policies.

API alternative

To instead use the API to manage IAM policies, go to [Cluster API v2](/managed/dynatrace-api/cluster-api/cluster-api-v2 "Find out about managing environments, network zones, Synthetic locations, nodes, and tokens in Dynatrace Managed using the Cluster API v2.").

## List IAM policies

To list configured IAM policies

1. In the Cluster Management Console, go to **User authentication** > **Policy management**.
2. Review the table of all existing policies that you can bind to user groups.

   * **Policy**âthe name of the policy
   * **Policy description**âa brief description of the policy
   * **Organizational level**â`global`, `cluster`, or `environment`
   * **Actions**âview, edit, or delete that row's policy (actions available to you depend on your permission level)

### Default policies

To let you use policies right away, Dynatrace IAM is shipped with built-in global policies.

* On the **Policies** page, in the **Source** column, they're all set to `Dynatrace`
* They're predefined and managed by Dynatrace
* You can apply a built-in policy by [assigning it to a group](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies") for the whole account or to any environment.
* You can inspect themâselect **View policy** in the **Actions** columnâbut you can't edit them

## Create a policy

To create a policy

1. In the Cluster Management Console, go to **User authentication** > **Policy management**.
2. Select **Add policy**.
3. Enter the following information.

   | Element | Description |
   | --- | --- |
   | Policy name | The name of the policy. |
   | Policy description | A brief description of the policy. |
   | Available for organizational level | Each policy has a level that determines its scope:  * `global`: Global policies are predefined and managed by Dynatrace, and they apply to all accounts and environments. They cannot be edited. * `cluster`: Account policies apply to all environments under that account (customer). Use them to set company-wide policies. * `environment`: Environment policies apply only to a single customer environment.  Organization levels are now restricted in the UI to the `cluster` level (other levels are still available via API). Restriction in UI was provided to avoid confusion between *creating* and *binding*. Commonly creating multiple identical policies on the `environment` levels can be achieved in a more efficient way by defining one policy on the `cluster` level and binding it to `environment` levels. |
   | Policy statements | A statement specifying exactly what this policy allows.  Example: Policy for Settings 2.0 Write  ```  ALLOW settings:objects:read;  ALLOW settings:objects:write;  ALLOW settings:schemas:read; ```  You can combine multiple permissions in a single statement. Here is the same example combined into a single statement:  ```  ALLOW settings:objects:read, settings:objects:write, settings:schemas:read; ```  Combining statements is particularly useful for managing policies with complicated conditions. |

### Services

For a complete and up-to-date list of Dynatrace services that support permission management via IAM policies, see [IAM policy reference](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

## Edit a policy

To edit an existing policy

1. In the Cluster Management Console, go to **User authentication** > **Policy management**.
2. Find the policy you want to edit.  
   You can filter and sort the table.
3. Select **Actions** > **Edit policy**.
4. Make your changes and select **Save**.

## Delete a policy

To delete a policy

1. In the Cluster Management Console, go to **User authentication** > **Policy management**.
2. Find the policy you want to delete.  
   You can filter and sort the table.
3. Select the **Edit** button for the policy.
4. Select **Delete policy**.

   The change takes effect in a few minutes.

   To change the delay, modify property `policyRefreshIntervalSeconds` in the `iam` section of the config file.

## Copy a policy

To copy an existing policy

1. In the Cluster Management Console, go to **User authentication** > **Policy management**.
2. Open an existing policy for editing.
3. Copy the contents of **Policy statements** to the clipboard.
4. Go back to the **Policy management** page.
5. Select **Add policy**.
6. Paste the copied policy statements into **Policy statements**.
7. Fill in the **Name** and optional **Description**.
8. Select **Save**.

## Apply a policy to a group

To apply a policy to a group, you need to bind the policy to the group. For details on managing group permissions with IAM, see [Working with policies](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies").