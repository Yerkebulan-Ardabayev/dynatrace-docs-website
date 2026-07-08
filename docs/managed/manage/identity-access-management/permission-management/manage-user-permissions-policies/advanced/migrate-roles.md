---
title: Upgrade role-based permissions to Dynatrace IAM policies
source: https://docs.dynatrace.com/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/migrate-roles
---

# Upgrade role-based permissions to Dynatrace IAM policies

# Upgrade role-based permissions to Dynatrace IAM policies

* 11-min read
* Updated on Aug 20, 2025

Dynatrace version 1.252+

Starting with Dynatrace version 1.252+, Dynatrace supports defining user and group permissions using IAM policies alongside classic role-based access control. This page guides you through using environment-level permissions in policy statements, enabling fine-grained access control across management zones, host groups, and extensions. Dynatrace security policies support [role-based permissions](/managed/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions"), allowing you to control all access to your environment. You can use security policies to define user/group permissions in your environment via the Dynatrace web UI or the Dynatrace API.

Policies do not restrict classic role-based permissions

As you migrate your role-based permissions to IAM framework, note that role-based permissions and security policies are additive. For example, if an environment permission is assigned to a user, and then you assign this user to an IAM group with a policy-based role restricted to a management zone, the environment permission still grants access to a whole environment, including all management zones.

## Environment permissions

To ease migration to security policies, you can use existing [environment permissions](/managed/manage/identity-access-management/permission-management/role-based-permissions#environment "Role-based permissions") in your policy statements and bind them to groups.

### Example 1: Policy for an application developer

For example, to create a policy for a typical application developer, you'd want to provide them with a set of permissions as shown in the following code examples:

* Access to all settings in `dev` and `hardening`

  ```
  ALLOW environment:roles:manage-settings



  WHERE environment:management-zone IN ("dev", "hardening");
  ```
* Read access in `prod`

  ```
  ALLOW environment:roles:viewer



  WHERE environment:management-zone IN ("prod");
  ```

### Example 2: Monitoring parts of the environment

1. Create a policy granting full access to the environment.

   ```
   ALLOW environment:roles:viewer, environment:roles:manage-settings;
   ```

   A user from a group to which this policy is bound has full access to the environment.

   ![Full access](https://dt-cdn.net/images/roles-808-c081787446.png)

   Full access
2. Modify the policy to limit access to selected management zones based on name prefix (in this example, `“[Kubernetes]”`).

   ```
   ALLOW environment:roles:viewer, environment:roles:manage-settings



   WHERE environment:management-zone startsWith "[Kubernetes]";
   ```

   Now the user has access only to the management zones with names starting with `“[Kubernetes]”`.

   ![Roles limited access](https://dt-cdn.net/images/roles-limit-808-c095b9bcf9.png)

   Roles limited access

Learn how to [create policies](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt "Create, edit, copy, and delete IAM policies for managing Dynatrace user permissions.").

## Management zone permissions

To create policy limited to a specific management zone, use the `environment:management-zone` attribute in your policy statement. For example, to limit log viewing to a selected management zone, use the following statement:

```
ALLOW environment:roles:logviewer



WHERE environment:management-zone IN ("my-management-zone");
```

## Role names

Use the following role names in your policy statements.

| Current role name | IAM role name | Management zone condition |
| --- | --- | --- |
| View environment | `roles:viewer` | GA |
| Manage monitoring settings | `roles:manage-settings` | GA |
| Manage capturing of sensitive request data | `roles:configure-request-capture-data` |  |
| Install OneAgent | `roles:agent-install` |  |
| Manage security problems | `roles:manage-security-problems` | GA |
| View security problems | `roles:view-security-problems` | GA |
| Replay sessions without masking | `roles:replay-sessions-without-masking` | GA |
| Replay sessions with masking | `roles:replay-sessions-with-masking` | GA |
| View logs | `roles:logviewer` | GA |
| View sensitive request data | `roles:view-sensitive-request-data` | GA |

As with classic role-based permissions, the `viewer` role is implicitly included in all roles. For example, a policy with a `manage-settings` role also allows a user to access the web UI.

## Policy statement syntax

In its most basic form, a policy statement for environment permissions starts with the ALLOW keyword. Then it is followed by `environment:roles`, a role name, and a management zone name.

```
ALLOW environment:roles:<role name> WHERE environment:management-zone = "<name of management zone>";
```

A statement can include an optional management zone condition. This allows a role in a number of management zones.

```
ALLOW environment:roles:<role name> WHERE environment:management-zone IN ("<name of management zone 1>", "<name of management zone n>");
```

## Related topics

* [Working with policies](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies")
* [IAM policy statement syntax and examples](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policystatement-syntax "IAM policy statement syntax.")