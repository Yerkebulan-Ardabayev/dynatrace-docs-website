---
title: "Working with policies"
source: https://docs.dynatrace.com/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies
updated: 2026-02-09
---

# Working with policies


* Latest Dynatrace
* Explanation
* 9-min read
* Updated on Aug 20, 2025

Use Dynatrace identity and access management (IAM) to manage user access to Dynatrace features.

With the IAM framework, you can define policies that clearly specify whether an action in Dynatrace is allowed. When policies are bound to user groups, they describe an access pattern for the group that is enforced at runtime. This gives you much more fine-grained control over how your users interact with Dynatrace.

## Basic

[### Manage IAM policies

List, create, delete, and copy policies using the Account Management.](../../../../ru/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt.md "Create, edit, copy, and delete IAM policies for managing Dynatrace user permissions.")[### Create your policies

Learn the policy statement syntax and see the example custom policies.](manage-user-permissions-policies/iam-policystatement-syntax.md "IAM policy statement syntax.")[### Policy boundaries

Boundaries allow you to further restrict policies.](../../../../ru/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-boundaries.md "Restrict security policies with policy boundaries to provide tailored access to your users.")

## Advanced

[### Global conditions

You can apply global conditions to any policy statement because they are not service-specific.](manage-user-permissions-policies/advanced/iam-global-conditions.md "Policy global conditions")[### Global attributes

Apply attributes to certain global conditions, usable in the policy syntax without extra configuration.](manage-user-permissions-policies/advanced/iam-global-attributes.md "Policy global attributes")[### Migrate role-based permissions

Dynatrace security policies now support the classic role-based permissions, learn how to migrate them.](../../../../ru/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/migrate-roles.md "Manage access to a Dynatrace environment using security policies.")

## Reference

[### IAM permissions reference

A complete list of all supported IAM permissions across all Dynatrace services.](../../../../ru/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements.md "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.")[### Policy management API

Manage the policies at scale using the policy management API.](../../../dynatrace-api/account-management-api/policy-management-api/policies.md "Manage access policies in your Dynatrace account via the Policy management API.")
