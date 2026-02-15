---
title: Working with policies
source: https://www.dynatrace.com/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies
scraped: 2026-02-15T21:20:10.171652
---

# Working with policies

# Working with policies

* Latest Dynatrace
* Explanation
* 9-min read
* Updated on Aug 20, 2025

Use Dynatrace identity and access management (IAM) to manage user access to Dynatrace features.

With the IAM framework, you can define policies that clearly specify whether an action in Dynatrace is allowed. When policies are bound to user groups, they describe an access pattern for the group that is enforced at runtime. This gives you much more fine-grained control over how your users interact with Dynatrace.

## Basic

[### Manage IAM policies

List, create, delete, and copy policies using the Account Management.](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt "Create, edit, copy, and delete IAM policies for managing Dynatrace user permissions.")[### Create your policies

Learn the policy statement syntax and see the example custom policies.](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policystatement-syntax "IAM policy statement syntax.")[### Policy boundaries

Boundaries allow you to further restrict policies.](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-boundaries "Restrict security policies with policy boundaries to provide tailored access to your users.")

## Advanced

[### Global conditions

You can apply global conditions to any policy statement because they are not service-specific.](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-global-conditions "Policy global conditions")[### Global attributes

Apply attributes to certain global conditions, usable in the policy syntax without extra configuration.](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-global-attributes "Policy global attributes")[### Migrate role-based permissions

Dynatrace security policies now support the classic role-based permissions, learn how to migrate them.](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/migrate-roles "Manage access to a Dynatrace environment using security policies.")

## Reference

[### IAM permissions reference

A complete list of all supported IAM permissions across all Dynatrace services.](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.")[### Policy management API

Manage the policies at scale using the policy management API.](/docs/dynatrace-api/account-management-api/policy-management-api/policies "Manage access policies in your Dynatrace account via the Policy management API.")