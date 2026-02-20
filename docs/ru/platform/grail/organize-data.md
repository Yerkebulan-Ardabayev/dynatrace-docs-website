---
title: Organize data
source: https://www.dynatrace.com/docs/platform/grail/organize-data
scraped: 2026-02-20T21:19:05.618208
---

# Organize data

# Organize data

* Latest Dynatrace
* Overview
* 4-min read
* Updated on Oct 02, 2025

## Grail data model

Dynatrace Grail organizes data in buckets, tables, and views to ensure efficient storage, flexible access, and scalable querying.

Buckets are the logical storage units where records are stored. Buckets are always associated with a specific record type, such as logs, events, or spans. Each record type has a predefined built-in bucket. Administrators can create custom buckets to optimize performance, apply different retention times, or meet specific compliance requirements.

Tables group records by type. Fetching a table retrieves records from all corresponding buckets. For example, the `logs` table includes all log records, regardless of whether they're stored in the default logs bucket or a custom one. This abstraction allows you to access data uniformly, independent of the underlying storage structure.

System tables such as `dt.system.buckets`, `dt.system.data_objects`, and `dt.system.files` represent information that is not stored in buckets.

Views are virtual tables defined by queries on existing tables. They provide a filtered or transformed perspective of the underlying records. For example, you can use `dt.entity.*` views to query classic entities.

## Built-in Grail buckets

There is a set of predefined built-in buckets that cannot be modified, including:

* Default buckets, whose name starts with `default_`
* System buckets, whose name starts with `dt_`

### Built-in buckets with corresponding retention periods

This section has been updated to align with the new Grail security events table. For the complete list of updates and actions needed to accomplish the migration, follow the steps in the [Grail security table migration guide](/docs/secure/threat-observability/migration "Understand the changes in the new Grail security table and learn how to migrate to it.").

These are examples of built-in buckets with corresponding retention periods.
For a full list of available built-in buckets, run this DQL query:

```
fetch dt.system.buckets



| filter startsWith(name, "default_") or startsWith(name, "dt_")
```

Run in Playground

Name

Table

Retention

`default_events`

events

35 days

`default_securityevents_builtin`

security.events

3 years

`default_securityevents`

security.events

1 year

`default_bizevents`

bizevents

35 days

`default_logs`

logs

35 days

`default_metrics`

metrics

15 months

`default_spans`

spans

10 days

`dt_system_events`

dt.system.events

1 year

`default_application_snapshots`

application.snapshots

10 days

## Custom Grail buckets

You can create a bucket tailored to your needs. Grail buckets behave like folders in a file system and are designed for records that should be handled together. For example, you might need to store together:

* Data with the same retention period
* Data that needs to be queried/analyzed together
* Data that needs to be deleted at the same time

Defining buckets can improve query performance by reducing query execution time and the scope of data read. Finally, having your data stored in a bucket streamlines your permission management because you can easily provide a user group or single users with access to needed data.

The default limit per environment is 80 buckets, typically satisfying ingestion volumes up to 5TB/day per table (e.g. logs). For larger ingestion volumes, more buckets can be requested in coordination with your Dynatrace account team.

For custom buckets, the possible retention periods range from 1 day to 10 years, with an additional week.

Shortening the retention period on update requests will delete the data that is over the new period.  
Any operation that deletes data is a long-running process. Deleting data can take up to a few days, depending on the amount of data you've deleted.

## Manage custom Grail buckets

To manage your buckets, ensure that you have configured the following permissions:

* `storage:bucket-definitions:read`
* `storage:bucket-definitions:write`
* `storage:bucket-definitions:delete`
* `storage:bucket-definitions:truncate`

With [**Storage Management**ï»¿](https://dt-url.net/s4038cj) you can:

* Create custom buckets for events, security events, bizevents, logs, and spans.
* Edit custom buckets.
* Delete custom buckets.

### Creating new buckets with Storage Management

To create a new custom Grail bucket with Storage Management you need to specify:

* Unique bucket name. It has to be between 3-100 characters long and has to start with a letter. The bucket name can only contain lowercase alphanumeric characters, underscores and hyphens. The bucket name can't be edited or changed at a later time.
* Display name. You can use this field to describe your bucket.
* Retention period between 1-3657 days.

### Manage custom Grail buckets via REST API

To manage your custom Grail buckets via REST API

1. Search for and select **Dynatrace API**.
2. In the **Select a definition** field, select **Grail Storage Management**.
3. Authenticate with your API token.

   For details, see [Authentication](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Create personalised platform tokens to access Dynatrace services via the API in your user context.").
4. Perform one of the following actions.

   | To do this | Go to **Bucket Definitions** and select this |
   | --- | --- |
   | List my buckets | **GET/bucket-definitions** |
   | Create buckets | **POST/bucket-definitions** |
   | Update buckets | **PATCH/bucket-definitions/{bucketName}**   or   **PUT/bucket-definitions/{bucketName}** |
   | Truncate buckets | **POST/bucket-definitions/{bucketName}:truncate** |
   | Delete buckets | **DELETE/bucket-definitions/{bucketName}** |

The delete buckets operation is irreversible. This operation will remove the content of a given bucket and then delete the bucket itself. Delete is an asynchronous task. Runtime will depend on the amount of data that has to be removed. The status of this operation can be tracked via the status field within `GET bucket definitions`.
Status will show **deleting** as long as data will be drained, and finally the bucket will be deleted. Afterwards, the bucket will cease to exist.
This operation can be executed on all types of buckets, except buckets where **bucketName** starts with `dt_` or `default_`. Before a bucket is deleted, checks are performed to verify that the bucket is not in use. To delete a bucket, you need the `storage:bucket-definitions:delete` permission.

See when to [create custom buckets and how to allow access to them](/docs/platform/upgrade#organize-your-data "Use the power of Grail, AppEngine, and AutomationEngine to take advantage of improvements in storing and analyzing observability and security data.").

## Related topics

* [What is Dynatrace Grail?](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more.")