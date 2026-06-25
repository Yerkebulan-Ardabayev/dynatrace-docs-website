---
title: IAM policy statement syntax and examples
source: https://docs.dynatrace.com/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policystatement-syntax
scraped: 2026-05-12T11:49:51.029568
---

# IAM policy statement syntax and examples

# IAM policy statement syntax and examples

* Reference
* 6-min read
* Updated on Feb 10, 2026

This page describes the structure and syntax of the IAM policy statement and provides examples of how to work with IAM policy statements.

* For a list of all supported values for each IAM service, permission, and condition, see [IAM policy reference](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

## ALLOW statement

A policy statement typically starts with the `ALLOW` keyword, which is followed by `permissions` and then `conditions`.

```
ALLOW `<permissions>` WHERE `<conditions>`;
```

* `ALLOW`: To enable permission.
* `permissions` : A specific action a user or a group is allowed to perform on a resource within a Dynatrace service (For example, `settings:objects:read`).

Statement details

A single statement can contain multiple `permission` and `condition` clauses. It may also include an optional condition. A policy may include a maximum of 100 statements.

You can further break it down as:

```
ALLOW <service:resource:action> WHERE <service:attribute> = 'value' AND <service:attribute> = "value";
```

* `service`: Dynatrace service name (for example, `settings`, `storage`, or `metrics`).
* `resource`: Type of object or capability within the service (for example, `objects`, `logs`, or `apps`).
* `action`: Specific operation the user is allowed to perform on that resource (for example, `read`, `write`, or `create`).

Resource actions

Each resource offers a specific set of actions, and not all actions are available on all resources.

* `condition`: Allows you to restrict access on resource or record level. This is optional in a statement (for example, `storage:table-name = "application.snapshots"`). `condition` consists of three parts:

  + `service`: Dynatrace service that provides the attribute used in the condition (for example, `storage`, `settings`, or `metrics`).
  + `attribute`: Specific property of that service checked in the condition (for example, `table-name`, `dt.security_context`, or `builtin:container.monitoring-rule`).
  + `value`: Literal (or parameter) to compare with the attribute (for example, `application.snapshots`, `default_security_events`, or `builtin:container.monitoring-rule`).

## DENY statement

A `DENY` statement always overrules an `ALLOW` statement.

Example:

```
DENY storage:logs:read;
```

If there is any `DENY` statement assigned and it matches a given request, all subsequent `ALLOW` statements are ignored.

Instead of using `DENY`, you can grant users only the access they need via dedicated `ALLOW` statements with conditions or by leveraging policy boundaries.

It is recommended to avoid using `DENY` statements without a condition, as they would block the whole API for the users. It can create complex policy situations that are hard to resolve.

Dynatrace evaluates the order for `DENY` as follows:

1. Check for an unconditional `DENY` on a service request and reject if it matches.
2. Check for a conditional `DENY` on a service request that matches the request, and reject if it matches.
3. Check for an unconditional `ALLOW` on a service request, and grant access if it matches.
4. Check for a conditional `ALLOW` on a service request that matches the request, and grant access if it
   matches.
5. If nothing matches, reject access.

## Policy statement syntax

The table below provides descriptions and examples for each policy syntax component.

Example:

```
ALLOW settings:objects:read, settings:schemas:read WHERE settings:schemaId = "123" AND storage:table-name = "events";
```

| Component | Description | Examples |
| --- | --- | --- |
| `<permission>` | A specific action a user or group is allowed to perform on a resource within a Dynatrace service. | * `storage:logs:read` * `storage:buckets:write` * `environment:roles:viewer` * `openpipeline:configurations:write` * `storage:system:read (used with condition like storage:table-name = "dt.system.events")`  For more permissions, see [IAM policy reference](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services."). |
| `<service>` | Dynatrace service name. | * `settings` * `cloudautomation` * `environment` * `automation` * `openpipeline` * `business-analytics`  For more services, see [IAM policy reference](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services."). |
| `<resource>` | A specific type of object or capability within the service. | * `logs` * `bucket-definitions` * `configurations` * `apps`  For more resources, see [IAM policy reference](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services."). |
| `<action>` | A specific operation the user is allowed to perform on that resource. | * `read` * `run` * `set` * `manage` * `execute`  For more actions, see [IAM policy reference](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services."). |
| `<condition>` | Add a restriction to the permission based on a particular attribute or context. | * `WHERE` `<condition name>` `<condition operator>` = "`<condition value>`". + Example: `WHERE settings:schemaId = "builtin:container.monitoring-rule" AND storage:table-name = "events"` * To add multiple conditions to a `statement`, use `AND`. * Conditions are optional. You can use the `null` value to indicate no condition. + Example: `ALLOW settings:schemas:read WHERE null;` |
| `<condition name>` | The specific property of a service to check in the condition. | * `table-name` * `dt.security_context` * `schemaId`  Every permission in an IAM policy contains conditions.  * Some conditions are permission-specific and apply only to a defined set of permissions within a service, while [global conditions](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-global-conditions "Policy global conditions") apply across all permissions.  For conditions supported by permissions, see [IAM policy reference](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services."). |
| `<condition operator>` | The operator used to check the condition. | * `=` * `!=` * `<` * `>` * `IN` (applies only to lists) * `startsWith` * `NOT IN` * `NOT startsWith`  Not every operator applies to every service attribute. For a list of supported options, see [IAM policy reference](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services."). |
| `<condition value>` | The literal (or parameter) to compare with the attribute. | Examples for each operators:  * **=** or **!=** : `WHERE settings:schemaId = "builtin:container.monitoring-rule"` * **IN** : `WHERE settings:schemaId IN ("builtin:container.monitoring-rule", "builtin:container.built-in-monitoring-rule")` * **NOT IN** : `WHERE storage:table-name = "events" NOT IN ("default_security_events", "default_security_custom_events")` * **NOT startsWith** : `WHERE storage:table-name NOT startsWith "application."` * **>** : `WHERE global:date-time > "2022-05-03T05:00:00+01:00"` * **<** : `WHERE global:time-of-day < "17:00+01:00"` * **startsWith** : `WHERE settings:schemaId startsWith "app:"` |
| `<comment>` | A comment explaining the policy. Everything between a double slash (`//`) and the end of the line is comment text. | * Example: `// Vulnerability service ALLOW vulnerability-service:vulnerabilities:read;` |

## Example policy statements

These examples show common IAM policy patterns for granting, restricting, or conditioning access in different scenarios.

* These examples use the Dynatrace Settings service (`settings`), which enables you to manage the following permissions:

  + `schemas:read`
  + `objects:read`
  + `objects:write`

  Settings service supports the `settings:schemaId` condition, which supports the following operators:

  + `IN`
  + `=`
  + `!=`
  + `startsWith`
  + `NOT startsWith`.

### Example 1: simple ALLOW statement

In this example, a user that belongs to a group to which this policy is assigned has read access to all schemas in the Dynatrace `settings` service.

```
ALLOW settings:schemas:read;
```

### Example 2: condition - single value

This example modifies example 1 by adding a condition to limit read access to just one specific schema in the Dynatrace `settings` service.

```
ALLOW settings:schemas:read WHERE settings:schemaId = "builtin:container.monitoring-rule";
```

The condition is added to this example statement by adding the `WHERE` keyword followed by the condition, which consists of three parts:

* condition name (`settings:schemaId`)
* condition operator (`=`)
* condition value (`"builtin:container.monitoring-rule"`)

So this statement says a user that belongs to a group to which this policy is assigned can read schemas in the `settings` service, but only if the schema is equal to `builtin:container.monitoring-rule`.

If you instead used the condition operator `!=`, it would mean that a user that belongs to a group to which this policy is assigned can read schemas in the `settings` service, but only if the schema is NOT equal to `builtin:container.monitoring-rule`.

### Example 3: condition - list of values

This example modifies example 2 to show how to use the `IN` operator with a list of values.

```
ALLOW settings:schemas:read WHERE settings:schemaId IN ("builtin:container.monitoring-rule", "builtin:container.built-in-monitoring-rule");
```

The condition value in this case takes the form of a list of schema IDs enclosed with parentheses and delimited with commas.

So this statement says a user that belongs to a group to which this policy is assigned can read schemas in the `settings` service, but only if the schema ID is in this list, and then it defines a comma-separated list of two schema IDs:
`("builtin:container.monitoring-rule", "builtin:container.built-in-monitoring-rule")`

### Example 4: statements on separate lines

Each policy can have multiple statements.

Example policy with two statements:

```
ALLOW settings:objects:read;



ALLOW settings:objects:write WHERE settings:schemaId = "builtin:container.monitoring-rule";
```

In this example, a user that belongs to a group to which this policy is assigned can:

* read all `objects` in the `settings` service (there is no condition in the first statement)
* write `objects` in the `settings` service only where `settings:schemaId` is equal to `builtin:container.monitoring-rule`

### Example 5: statements combined

Instead of listing permission statements on separate lines, you can combine statements into one line:

```
ALLOW settings:objects:read, settings:objects:write WHERE settings:schemaId = "builtin:container.monitoring-rule";
```

A policy with this statement grants read and write access to `builtin:container.monitoring-rule`, with the WHERE condition applying to both.

### Example 6: statement with comments

To explain a policy or statements in it, you can add one or more standalone comment lines:

```
// Read and Write access to monitoring-rule



ALLOW settings:objects:read, settings:objects:write WHERE settings:schemaId = "builtin:container.monitoring-rule";
```

You can also add a comment to a statement line:

```
ALLOW settings:objects:read;  // Allows the user to read all `objects` in the `settings` service
```