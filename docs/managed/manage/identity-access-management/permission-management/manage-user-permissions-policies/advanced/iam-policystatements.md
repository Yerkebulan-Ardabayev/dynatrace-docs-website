---
title: IAM policy reference
source: https://docs.dynatrace.com/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements
---

# IAM policy reference

# IAM policy reference

* Reference
* 1-min read
* Published Mar 25, 2021

The following is a complete reference of IAM permissions and corresponding conditions applicable to Dynatrace services. Refer to it when you need to define access policies based on a fine-grained set of permissions and conditions that can be enforced per service.

## environment

Environment and management zone user permissions. See [Migrate role-based permissions to Dynatrace IAM﻿](https://dt-url.net/3s23539) for more information.

Role IAM permissions work the same way as classic roles do, which means that the `environment:roles:viewer` permission is a part of any other role permission. For example, a policy granting `environment:roles:manage-settings` permission also allows a user to access the web UI.

### environment:roles:viewer

Grants user the **Access environment** permission.

#### conditions:

* `environment:management-zone` - A string that uniquely identifies a management zone. Applies the permission on the management zone level for the specified management zone.
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

### environment:roles:manage-settings

Grants user the **Change monitoring settings** permission.

#### conditions:

* `environment:management-zone` - A string that uniquely identifies a management zone. Applies the permission on management zone level for the specified management zone.
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

### environment:roles:agent-install

Grants user the **Download/install OneAgent** permission. Users who have this permission assigned are also able to view monitoring data for all management zones.

### environment:roles:view-sensitive-request-data

Grants user the **View sensitive request data** permission.

#### conditions:

* `environment:management-zone` - A string that uniquely identifies a management zone. Applies the permission on management zone level for the specified management zone.
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

### environment:roles:configure-request-capture-data

Grants user the **Configure capture of sensitive data** permission. Users who have this permission assigned are also able to view monitoring data for all management zones.

### environment:roles:replay-sessions-without-masking

Grants user the **Replay session data without masking** permission.

#### conditions:

* `environment:management-zone` - A string that uniquely identifies a management zone. Applies the permission on management zone level for the specified management zone.
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

### environment:roles:replay-sessions-with-masking

Grants user the **Replay session data** permission.

#### conditions:

* `environment:management-zone` - A string that uniquely identifies a management zone. Applies the permission on management zone level for the specified management zone.
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

### environment:roles:manage-security-problems

Grants user the **Manage security problems** permission.

#### conditions:

* `environment:management-zone` - A string that uniquely identifies a management zone. Applies the permission on management zone level for the specified management zone.
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

### environment:roles:view-security-problems

Grants user the **View security problems** permission.

#### conditions:

* `environment:management-zone` - A string that uniquely identifies a management zone. Applies the permission on management zone level for the specified management zone.
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

### environment:roles:logviewer

Grants user the **View logs** permission.

#### conditions:

* `environment:management-zone` - A string that uniquely identifies a management zone. Applies the permission on management zone level for the specified management zone.
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

## extensions

Extensions service

### extensions:definitions:read

Grants permission to read extension and environment configurations

#### conditions:

* `extensions:extension-name` - A string that uniquely identifies a single extension
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `!=`, `=`

### extensions:definitions:write

Grants permission to write (update/create/delete) extension and environment configurations

#### conditions:

* `extensions:extension-name` - A string that uniquely identifies a single extension
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `!=`, `=`

### extensions:configurations:read

Grants permission to read extension monitoring configurations

#### conditions:

* `extensions:host` - A string that uniquely identifies a single host for monitoring configuration assignment
  operators: `IN`, `=`
* `extensions:host-group` - A string that uniquely identifies a single host group for monitoring configuration assignment
  operators: `IN`, `=`
* `extensions:ag-group` - A string that uniquely identifies a single ActiveGate group for monitoring configuration assignment
  operators: `IN`, `=`
* `extensions:management-zone` - A string that uniquely identifies a single management zone for monitoring configuration assignment
  operators: `IN`, `=`
* `extensions:extension-name` - A string that uniquely identifies a single extension
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `!=`, `=`

### extensions:configurations:write

Grants permission to write (update/create/delete) extension monitoring configurations

#### conditions:

* `extensions:host` - A string that uniquely identifies a single host for monitoring configuration assignment
  operators: `IN`, `=`
* `extensions:host-group` - A string that uniquely identifies a single host group for monitoring configuration assignment
  operators: `IN`, `=`
* `extensions:ag-group` - A string that uniquely identifies a single ActiveGate group for monitoring configuration assignment
  operators: `IN`, `=`
* `extensions:management-zone` - A string that uniquely identifies a single management zone for monitoring configuration assignment
  operators: `IN`, `=`
* `extensions:extension-name` - A string that uniquely identifies a single extension
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `!=`, `=`

### extensions:configuration.actions:write

Grants permission to execute actions for extension

#### conditions:

* `extensions:host` - A string that uniquely identifies a single host for monitoring configuration assignment
  operators: `IN`, `=`
* `extensions:host-group` - A string that uniquely identifies a single host group for monitoring configuration assignment
  operators: `IN`, `=`
* `extensions:ag-group` - A string that uniquely identifies a single ActiveGate group for monitoring configuration assignment
  operators: `IN`, `=`
* `extensions:management-zone` - A string that uniquely identifies a single management zone for monitoring configuration assignment
  operators: `IN`, `=`
* `extensions:extension-name` - A string that uniquely identifies a single extension
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `!=`, `=`

## settings

Settings service

### settings:objects:read

Enables reading of settings objects belonging to the schema

#### conditions:

* `settings:schemaId` - A string that uniquely identifies a single settings schema. The identifier of a schema can either be found via the dedicated schema endpoint in the Dynatrace Environment API or in the info box of a settings screen. The condition will match if the object's schemaId property matches.
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `settings:schemaGroup` - A schema group that allows to address multiple individual schemas at once. The group of a schema can either be found via the dedicated schema endpoint in the Dynatrace Environment API or in the info box of a settings screen. The condition will match if the schema of the object has a schemaGroup property that matches.
  operators: `IN`, `=`
* `settings:entity.hostGroup` - The host group attribute of an entity for which a setting is stored. This is e.g. useful to grant access to settings scopes of all hosts which belong to the same host group.
  operators: `IN`, `=`, `!=`
* `settings:scope` - The exact scope identifier a setting object has or will have. This condition allows to grant access to the scope of e.g., an individual host. In this case the scope equals the entity identifier, e.g. HOST-48B8F52F33098830.
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `environment:management-zone` - The name of a management zone. This condition is applicable to either: any settings object that is allowed on the scope of an entity that can be matched into a management zone or settings objects of the schemas builtin:alerting.maintenance-window, builtin:alerting.profile, builtin:anomaly-detection.metric-events, builtin:monitoring.slo and builtin:problem.notifications.
  operators: `IN`, `=`, `startsWith`, `MATCH`

### settings:objects:write

Enables writing of settings objects belonging to the schema

#### conditions:

* `settings:schemaId` - A string that uniquely identifies a single settings schema. The identifier of a schema can either be found via the dedicated schema endpoint in the Dynatrace Environment API or in the info box of a settings screen. The condition will match if the object's schemaId property matches.
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `settings:schemaGroup` - A schema group that allows to address multiple individual schemas at once. The group of a schema can either be found via the dedicated schema endpoint in the Dynatrace Environment API or in the info box of a settings screen. The condition will match if the schema of the object has a schemaGroup property that matches.
  operators: `IN`, `=`
* `settings:entity.hostGroup` - The host group attribute of an entity for which a setting is stored. This is e.g. useful to grant access to settings scopes of all hosts which belong to the same host group.
  operators: `IN`, `=`, `!=`
* `settings:scope` - The exact scope identifier a setting object has or will have. This condition allows to grant access to the scope of e.g., an individual host. In this case the scope equals the entity identifier, e.g. HOST-48B8F52F33098830.
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `environment:management-zone` - The name of a management zone. This condition is applicable to either: any settings object that is allowed on the scope of an entity that can be matched into a management zone or settings objects of the schemas builtin:alerting.maintenance-window, builtin:alerting.profile, builtin:anomaly-detection.metric-events, builtin:monitoring.slo and builtin:problem.notifications.
  operators: `IN`, `=`, `startsWith`, `MATCH`

### settings:schemas:read

Enables reading settings schemas

#### conditions:

* `settings:schemaId` - A string that uniquely identifies a single settings schema. The identifier of a schema can either be found via the dedicated schema endpoint in the Dynatrace Environment API or in the info box of a settings screen. The condition will match if the schema's schemaId property of the schema matches.
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `settings:schemaGroup` - A schema group that allows to address multiple individual schemas at once. The group of a schema can either be found via the dedicated schema endpoint in the Dynatrace Environment API or in the info box of a settings screen. The condition will match if the schema's schemaId property of the schema matches.
  operators: `IN`, `=`

## Related topics

* [Working with policies](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies")
* [IAM policy statement syntax and examples](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policystatement-syntax "IAM policy statement syntax.")
* [Grant access to Settings](/managed/manage/identity-access-management/use-cases/access-settings "Grant access to Settings")
* [Account Management API](/managed/dynatrace-api/account-management-api "Explore endpoints of the Account Management API.")