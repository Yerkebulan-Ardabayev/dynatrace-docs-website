---
title: Working with policies
source: https://docs.dynatrace.com/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies
---

# Working with policies

# Working with policies

* Explanation
* 9-min read
* Updated on Aug 20, 2025

Use Dynatrace identity and access management (IAM) to manage user access to Dynatrace features.

With the IAM framework, you can define policies that clearly specify whether an action in Dynatrace is allowed. When policies are bound to user groups, they describe an access pattern for the group that is enforced at runtime. This gives you much more fine-grained control over how your users interact with Dynatrace.

## Basic

[### Manage IAM policies

List, create, delete, and copy policies using the Account Management.](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt "Create, edit, copy, and delete IAM policies for managing Dynatrace user permissions.")[### Create your policies

Learn the policy statement syntax and see the example custom policies.](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policystatement-syntax "IAM policy statement syntax.")

## Advanced

[### Global conditions

You can apply global conditions to any policy statement because they are not service-specific.](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-global-conditions "Policy global conditions")[### Global attributes

Apply attributes to certain global conditions, usable in the policy syntax without extra configuration.](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-global-attributes "Policy global attributes")[### Migrate role-based permissions

Dynatrace security policies now support the classic role-based permissions, learn how to migrate them.](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/migrate-roles "Manage access to a Dynatrace environment using security policies.")

## Reference

[### IAM permissions reference

A complete list of all supported IAM permissions across all Dynatrace services.](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.")