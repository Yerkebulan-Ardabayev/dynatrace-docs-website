---
title: Set up permissions for Live Debugging
source: https://www.dynatrace.com/docs/observe/application-observability/live-debugger/setup
scraped: 2026-02-18T05:49:48.129645
---

# Set up permissions for Live Debugging

# Set up permissions for Live Debugging

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Nov 22, 2025

## User permissions

All supported values for each IAM permission and condition are listed below. Use them to define access policies based on a fine-grained set of permissions and conditions that can be enforced per service. For more information, see [Working with policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies").

Permission

Description

state:user-app-states:read

Allows write required user settings

state:user-app-states:write

Allows write required user settings

settings:objects:read

Allows reading required client settings

app-settings:objects:read

Allows reading required settings, such as On-Prem Git servers

dev-obs:breakpoints:set

See Observability for Developers agents and place breakpoints.

dev-obs:breakpoints:manage

Manage Observability for Developers breakpoints.

10

rows per page

Page

1

of 1

## Set breakpoints

Grants permission to set user-level Live Debugging breakpoints.

**Conditions**:

* `dev-obs:k8s.namespace.name` - the name of the namespace that the pod is running in.

  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`
* `dev-obs:dt.entity.process_group` - the process group your application is a part of.

  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`
* `dev-obs:dt.process_group.detected_name` â the detected name of the process group your application is a part of.

  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

**Example policies**:

* Allow setting breakpoints for all instances:

  ```
  ALLOW dev-obs:breakpoints:set;
  ```
* Allow setting breakpoints for a particular host group:

  ```
  ALLOW dev-obs:breakpoints:set WHERE dev-obs:dt.process_group.detected_name = "my_process_group";
  ```

## Read snapshots

Grants permission to read user-level Live Debugging snapshots.

**Example policies**:

* Allow read snapshots:

  ```
  ALLOW storage:application.snapshots:read;



  ALLOW storage:buckets:read WHERE storage:table-name = "application.snapshots";
  ```