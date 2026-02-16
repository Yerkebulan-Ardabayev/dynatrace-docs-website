---
title: Permissions in Grail
source: https://www.dynatrace.com/docs/platform/grail/organize-data/assign-permissions-in-grail
scraped: 2026-02-16T21:13:07.098589
---

# Permissions in Grail

# Permissions in Grail

* Latest Dynatrace
* How-to guide
* 10-min read
* Updated on Jan 26, 2026

Permissions can be assigned at the bucket, table, record, and field level. Without permissions, your users can't query data from Grail.

![Bucket and table permissions logic ](https://dt-cdn.net/images/new-bucket-and-table-permissions-diagram-1991-07901aebd8.png)

## Set up permissions

To set up the bucket and table-level permissions

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/). If you have more than one account, select the account you want to manage.
2. Go to **Identity & access management** > **Policy management**.
3. Select **Create policy**.
4. Add the policy details:

   * **Name**
   * **Description**
   * **Policy statement**âuse the following format:

     ```
     ALLOW storage:buckets:read WHERE <conditions>;



     ALLOW <table permission> WHERE <conditions>;
     ```

   See below for supported bucket and table permissions.
5. Select **Create policy**.

## Bucket permissions

All bucket permissions need to start with `storage:buckets:read`. Their scope can be limited by a `WHERE` clause that includes one of the following operators:

* `=`, tests for equality.
* `STARTSWITH`, tests for a prefix.
* `IN`, tests for equality for any value of a list.
* `MATCH`, tests for pattern matching for any pattern of a list. It generalizes and expands both `STARTSWITH` and `IN` operators.

After the `WHERE` clause, you can filter your results by specifying buckets or tables:

* WHERE storage:bucket-name
* WHERE storage:table-name

The example below shows how to include only buckets prefixed with `default_` or the `common_logs` bucket.

```
ALLOW storage:buckets:read WHERE storage:bucket-name MATCH ("default_*", "common_logs");
```

For more information, see [IAM policy reference](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#storage "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

### Included queries

Logs only

This only applies if `Log Management & Analytics - Retain with Included Queries` is on your rate card.

Included queries

For more information about retained log data and included query log data, see [Retain with Included Queries](/docs/license/capabilities/log-analytics#log-retain-included-queries "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.").

Bucket permissions let you define user group access to

* All retained log data.
  Queries may generate `Log Management & Analytics - Query` consumption.
* Only included query log data.
  Queries will not generate additional `Log Management & Analytics - Query` consumption.

To define access, you use the `storage:query-consumption` condition.
This condition has two possible values.

* `ON_DEMAND`: Queries can scan all retained data.
  This is the default value: if not specified, users have access to all retained data.
* `INCLUDED`: Queries can scan only included query data.

This can be combined with the `storage:bucket-name` condition to restrict access on a per-bucket level.

Example use cases

The following examples describe how to use bucket permissions to grant access to

* Included query data in all buckets.

  ```
  ALLOW storage:buckets:read WHERE storage:query-consumption="INCLUDED";
  ```
* Included query data in a specific bucket (`common_logs`).

  ```
  ALLOW storage:buckets:read WHERE storage:bucket-name="common_logs" AND storage:query-consumption="INCLUDED";
  ```
* Included query data in all buckets, and additionally all retained data in a specific bucket (`common_logs`).

  ```
  ALLOW storage:buckets:read WHERE storage:query-consumption="INCLUDED";



  ALLOW storage:buckets:read WHERE storage:bucket-name="common_logs" AND storage:query-consumption="ON_DEMAND";
  ```
* All retained data in all buckets.

  ```
  ALLOW storage:buckets:read WHERE storage:query-consumption="ON_DEMAND";
  ```

  or

  ```
  ALLOW storage:buckets:read;
  ```

## Table permissions

Besides granting access to buckets, you also need to configure table permissions.

Table name

Permission

Affected DQL functions/commands

logs

storage:logs:read

[fetch](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#fetch "DQL data source commands")

events

storage:events:read

[fetch](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#fetch "DQL data source commands")

security.events

storage:security.events:read

[fetch](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#fetch "DQL data source commands")

metrics

storage:metrics:read

[timeseries](/docs/platform/grail/dynatrace-query-language/commands/metric-commands#timeseries "DQL metric commands")

bizevents

storage:bizevents:read

[fetch](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#fetch "DQL data source commands")

spans

storage:spans:read

[fetch](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#fetch "DQL data source commands")

entities

storage:entities:read

[fetch](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#fetch "DQL data source commands"), [classicEntitySelector](/docs/platform/grail/dynatrace-query-language/functions/general-functions#classic-entity-selector "A list of DQL general functions."), [entityAttr](/docs/platform/grail/dynatrace-query-language/functions/general-functions#entity-attr "A list of DQL general functions."), [entityName](/docs/platform/grail/dynatrace-query-language/functions/general-functions#entity-name "A list of DQL general functions.")

smartscape

storage:smartscape:read

[smartscapeNodes](/docs/platform/grail/dynatrace-query-language/commands/smartscape-commands#smartscapeNodes "DQL Smartscape commands"), [smartscapeEdges](/docs/platform/grail/dynatrace-query-language/commands/smartscape-commands#smartscapeEdges "DQL Smartscape commands"), [getNodeName()](/docs/platform/grail/dynatrace-query-language/functions/join-functions#getNodeName "A list of DQL join functions."), [getNodeField()](/docs/platform/grail/dynatrace-query-language/functions/join-functions#getNodeField "A list of DQL join functions.")

dt.system.events

storage:system:read

[fetch](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#fetch "DQL data source commands")

user.events

storage:user.events:read

[fetch](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#fetch "DQL data source commands")

user.sessions

storage:user.sessions:read

[fetch](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#fetch "DQL data source commands")

For more information, see [IAM policy reference](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#storage "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

### Bucket level permissions

You can restrict table permissions to certain buckets using the `WHERE` clause. For example:

```
ALLOW storage:logs:read WHERE storage:bucket-name="default_logs";
```

### Record level permissions

You can define fine-grained permissions for records that are stored in Grail. The permissions are added to the existing table permissions by adding the `WHERE` clause. For example:

```
ALLOW storage:logs:read WHERE storage:dt.security_context="TeamA";
```

Supported fields:

Field name

IAM condition

Supported IAM tables

`event.kind`

`storage:event.kind`

`events`, `security.events`, `bizevents`, `system`

`event.type`

`storage:event.type`

`events`, `security.events`, `bizevents`, `system`

`event.provider`

`storage:event.provider`

`events`, `security.events`, `bizevents`, `system`

`k8s.namespace.name`

`storage:k8s.namespace.name`

`events`, `security.events`, `bizevents`, `logs`, `metrics`, `spans`, `smartscape`

`k8s.cluster.name`

`storage:k8s.cluster.name`

`events`, `security.events`, `bizevents`, `logs`, `metrics`, `spans`, `smartscape`

`host.name`

`storage:host.name`

`events`, `security.events`, `bizevents`, `logs`, `metrics`, `spans`, `smartscape`

`dt.host_group.id`

`storage:dt.host_group.id`

`events`, `security.events`, `bizevents`, `logs`, `metrics`, `spans`, `smartscape`

`metric.key`

`storage:metric.key`

`metrics`

`log.source`

`storage:log.source`

`logs`

`dt.security_context`

`storage:dt.security_context`

`events`, `security.events`, `bizevents`, `system`, `logs`, `metrics`, `spans`, `entities`, `smartscape`, `user.events`, `user.sessions`

`gcp.project.id`

`storage:gcp.project.id`

`events`, `security.events`, `bizevents`, `logs`, `metrics`, `spans`, `smartscape`

`aws.account.id`

`storage:aws.account.id`

`events`, `security.events`, `bizevents`, `logs`, `metrics`, `spans`, `smartscape`

`azure.subscription`

`storage:azure.subscription`

`events`, `security.events`, `bizevents`, `logs`, `metrics`, `spans`, `smartscape`

`azure.resource.group`

`storage:azure.resource.group`

`events`, `security.events`, `bizevents`, `logs`, `metrics`, `spans`, `smartscape`

`frontend.name`

`storage:frontend.name`

`user.events`, `user.sessions`, `metrics`, `smartscape`

For details that are not available as a dedicated field, set the `dt.security_context` field either at the data source or in the processing pipeline.

### Combining bucket and record level permissions

You can combine both bucket and record level in your table permissions. For example this statement will provide access to all logs in the `unrestricted_logs` bucket and only specific records in the `default_logs` bucket:

```
ALLOW storage:logs:read WHERE storage:bucket-name="unrestricted_logs";



ALLOW storage:logs:read WHERE storage:bucket-name="default_logs" AND storage:dt.security_context="TeamA";
```

### Support for multiple values with MATCH operator

For efficiency reasons, record filters using the `=`, `IN` or `STARTSWITH` operators apply to fields holding a single string. You might have cases where the fields you want to use for filtering contain multiple values, in conjunction with a "for any value" set semantic. Such case is possible with the `MATCH` operator.

For example, the following statement will return results for records with `dt.security_context` holding either a `crn-70400-` prefixed string, or an array with a `crn-70400-` prefixed string as one of its elements.

```
// will match both "crn-70400-alpha" and ["crn-70131", "crn-70400-beta", "crn-70500"]



ALLOW storage:logs:read WHERE storage:dt.security_context MATCH ("crn-70400-*");
```

Note that you must use the `MATCH` operator to get "for any value" set semantic. Using `=`, `STARTSWITH` or `IN` when the field holds an array will always return `false`. If you expect your record filters might contain an array, use the `MATCH` operator in your IAM statements.

Example 1 - Grant team access to logs

As a Dynatrace administrator, I would like to ensure that each of my application teams can only access logs from their own Kubernetes namespace (records identifiable through `k8s.namespace.name`) and logs that belong to the basic infrastructure (records identifiable through `dt.host_group.id`).

Solution:

Create a policy for each team that grants them access to their logs.

Make sure that the user has access to all relevant buckets.

```
ALLOW storage:buckets:read WHERE â¦ // Ensure that the user has access to all relevant buckets



ALLOW storage:logs:read WHERE storage:k8s.namespace.name="namespace1";



ALLOW storage:logs:read WHERE storage:dt.host_group.id MATCH ("shared_host_*");
```

Example 2 - Grant team access to logs from lambda functions

As a Dynatrace administrator, I would like to set up access for my application teams to access logs from lambda functions based on the team tag. For example `team` = `A`.

Solution:

1. Define the log processing rule with a security context that adds the `dt.security_context` field based on the lambda tag.
2. Create a policy for each team that grants them access based on the security context field.

   Make sure that the user has access to all relevant buckets.

   ```
   ALLOW storage:buckets:read WHERE â¦ // Ensure that the user has access to all relevant buckets



   ALLOW storage:logs:read WHERE storage:dt.security_context MATCH ("TeamA");
   ```

Example 3 - Business analytics

As an administrator, I want to control access to business events that contain financial data. They can be identified using the `event.kind` field.

Solution:

Create a policy to grant access for specific users to records in `bizevents` for the specific `event.kind` (`Opportunity Field History`).

Make sure that the user has access to all relevant buckets.

```
ALLOW storage:buckets:read WHERE â¦ // Ensure that the user has access to all relevant buckets



ALLOW storage:bizevents:read WHERE storage:event.kind="Opportunity Field History";
```

Example 4 - System events

As an administrator, I want to provide selected users access to billing events but not to any other system events.

Solution:

Create a policy to grant access to records in `dt_system_events` for the specific `event.type` with the value `BILLING_EVENT`.

```
ALLOW storage:buckets:read WHERE storage:bucket-name="dt_system_events"



ALLOW storage:system:read WHERE storage:event.kind="BILLING_EVENT"
```

### Record permission limits

The following configuration limitations apply to record permissions:

* Number of statements per policy (100)
* Number of policies per account (200)

### Permissions for entities

Permissions for entities allow you to define IAM policies that control data access on entities.

In contrast to monitoring data, entity permissions only allow filtering for the `dt.security_context` field.

For more information, see [Grant access to entities with security context](/docs/manage/identity-access-management/use-cases/access-security-context "Grant access to entities with security context").

## Field permissions

You can use field permissions to hide fields that might contain sensitive data. For this purpose, we provide fieldsets. A field is considered sensitive when it's part of a fieldset. Once a field is part of a fieldset, only users with the right permissions can use it in DQL queries for filtering and grouping. For other users, it won't show up in the query results.

You require permission to access fieldsets in order to use sensitive fields. For example, if you want to use `builtin-sensitive-spans` fields in DQL queries, you need the following permission:

```
ALLOW storage:fieldsets:read WHERE storage:fieldset-name="builtin-sensitive-spans"
```

The three predefined fieldsets are:

* `builtin-sensitive-spans` - drops all fields on `spans` that are considered sensitive
* `builtin-request-attributes-spans` - drops all fields on `spans` that contain request attribute data that was marked sensitive
* `builtin-sensitive-user-events-and-sessions` - drops all fields in `user.events` and `user.sessions` that are considered sensitive

* The predefined fieldsets apply to `spans`, `user.events` and `user.sessions` only. They don't apply to `logs` or `events`.
* You can define your custom fieldsets, and to which scope they apply (either buckets, or tables, otherwise all buckets and tables).
* If you don't have sufficient permissions, sensitive fields won't be shown in the result.
* You can use the field permissions with `smartscape`, but not with `entities`.

### Define custom fieldsets via API

You can manage your custom fieldsets via REST API

1. In Dynatrace, search for and select **Dynatrace API**.
2. In the **Select a definition** field, select **Grail - Fieldsets**.
3. Authenticate with your API token.  
   For details, see [Authentication](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Create personalised platform tokens to access Dynatrace services via the API in your user context.").
4. Perform one of the following actions.

To do this

Go to **Fieldsets** and select this

Get all fieldsets

**GET /fieldsets**

Create a new fieldset

**POST /fieldsets**

Get fieldsets by UID

**GET /fieldsets/{fieldsetUid}**

Update a fieldset. All fields will be overwritten.

**PUT /fieldsets/{fieldsetUid}**

Delete a fieldset

**DELETE /fieldsets/{fieldsetUid}**

#### Example

This call creates the fieldset `sensitive-fields-retail`, removing the `credit_card` and `DOB` fields from DQL query results in the `logs_retail` bucket.

##### Request URL

```
POST https://myapps.mydomain.com/platform/storage/fieldsets/v1/fieldsets
```

##### Request body

```
{



"name": "sensitive-fields-retail",



"description": "Sensitive fields retail",



"enabled": true,



"scope": "BUCKET",



"fields": [



"credit_card",



"DOB"



],



"buckets": [



"logs_retail"



]



}
```

To unmask the `credit_card` and `DOB` fields, you need the following permission:

```
ALLOW storage:fieldsets:read WHERE storage:fieldset-name="sensitive-fields-retail"
```

## File permissions

Preview

To manage your lookup data stored in Grail, you require the following permissions:

* `storage:files:read` - to read lookup data data via DQL.
* `storage:files:write` - to upload lookup data via REST API.
* `storage:files:delete` - to delete lookup data via REST API.

All of these permissions support the `storage:file-path` condition using one of the following operators:

* `=` (equals) - indicating an exact match.
* `IN` - indicating a range.
* `startsWith` - with an expression put in quotation marks.

The following example shows how to provide full access to lookup data stored in `/lookups/`.

```
ALLOW storage:files:read WHERE storage:file-path startsWith "/lookups/";



ALLOW storage:files:write WHERE storage:file-path startsWith "/lookups/";



ALLOW storage:files:delete WHERE storage:file-path startsWith "/lookups/";
```

You can use the folder-like structure to manage access to different subsets of your lookup files with permissions, as in the following example.

```
ALLOW storage:files:read WHERE storage:file-path startsWith "/lookups/public/";
```

To give read-only access to a specific file, you could also use a permission similar to the following.

```
ALLOW storage:files:read WHERE storage:file-path startsWith "/lookups/http_status_codes";
```

For more information, see [IAM policy reference](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#storage "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

## Predefined global policies

There are several predefined global policies, each set per table (logs, events, bizevents, security events, metrics, entities, spans), and three additional, general policies:

* Read all data
* Read default monitoring data
* Read all system data

### Access to all logs

This policy provides access to all logs from Grail, and narrows the bucket permission with a `WHERE` condition that limits the results to the log table.

This statement provides access to all built-in and custom buckets.

```
ALLOW storage:buckets:read WHERE storage:table-name= "logs";



ALLOW storage:logs:read;
```

### Read all data

This permission statement gives you access to all tables and all buckets, therefore it needs to be used only in justified cases.

```
ALLOW storage:buckets:read;



ALLOW storage:system:read,



storage:events:read,



storage:security.events:read,



storage:logs:read,



storage:metrics:read,



storage:entities:read,



storage:bizevents:read,



storage:spans:read,



storage:smartscape:read;
```

### Read all default monitoring data

This policy retrieves all default monitoring data.

In the first line, this policy statement gives access to all default buckets. The `WHERE` condition narrows the search to buckets whose name starts with `default`. Subsequently, the next lines list all the needed table permissions.

This statement does not give access to custom buckets.

```
ALLOW storage:buckets:read WHERE storage:bucket-name MATCH ("default_*");



ALLOW storage:events:read,



storage:logs:read,



storage:metrics:read,



storage:entities:read,



storage:bizevents:read,



storage:spans:read,



storage:smartscape:read;
```

### Read all system data

This permission statement first narrows the results to system buckets, whose name starts with `dt`. Then, it gives you access to all tables that contain system data, for example audit `events`, billing `events`, and query execution events. It can be useful for system admins.

```
ALLOW storage:buckets:read WHERE storage:bucket-name MATCH ("dt_*");



ALLOW storage:system:read;
```

## Best practices

* Ensure that you also have bucket permissions.
* If there is an unconditional table permission in any other policy available for a user, the `WHERE` clause is irrelevant and the user will always be able to view all records from that table.
* Use the `MATCH` operator to simplify your statements instead of combination of `=`, `IN` and `STARTSWITH`, as there is a 100-statement limit per policy.
* When using the `MATCH` operator with wildcards (`*`) in record filters, it's best to place wildcards before or after word separators such as: `-`, `_`, `.`, or `/`. This is because `matchesValue` used in DQL queries, performs better when word separators are present. For example, `... WHERE storage:dt.host_group.id MATCH ("db-tech-*")` is more efficient than `... WHERE storage:dt.host_group.id MATCH ("db-tech*")`.
* Make sure to combine logs, events and metrics where applicable (to further save on the 100 statement policy [IAM policy statement syntax and examples](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policystatement-syntax#iam-example-statements-combined "IAM policy statement syntax."))
* When you create custom fieldsets, make sure to avoid including any essential fields in your fieldset (such as `timestamp`, `id`, `content`).

## Related topics

* [Working with policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies")
* [DQL best practices](/docs/platform/grail/dynatrace-query-language/dql-best-practices "Best practices for using Dynatrace Query Language.")