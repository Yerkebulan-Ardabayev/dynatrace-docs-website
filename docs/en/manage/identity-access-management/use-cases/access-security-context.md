---
title: Grant access to entities with security context
source: https://www.dynatrace.com/docs/manage/identity-access-management/use-cases/access-security-context
scraped: 2026-02-21T21:24:12.972808
---

# Grant access to entities with security context

# Grant access to entities with security context

* Latest Dynatrace
* Tutorial
* 4-min read
* Updated on Sep 17, 2025

This article shows you how to set the security context and grant access to the monitored entities using policies.

Don't mistake IAM policies with management zones. Unlike management zones, an IAM policy that is set up to filter entities (`allow storage:entities:read`) will not filter related metrics, logs, or traces.
These entity filters only control which entities can be queried via DQL.
To control access to logs, metrics, and spans, you need to use the corresponding permissions, such as `allow storage:logs:read`.

## Who this is for

This is for Dynatrace account administrators who are responsible for creating policies to grant users access to monitored entities such as hosts, through [DQL](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.").

## What you'll learn

In this article, you'll learn:

* How to set the security context on monitored entities.
* How to create policies to grant access to monitoring data stored in Grail in the context of monitored entities.
* How to use the security context in combination with IAM security policies to provide granular access to your entities.

## Before you begin

Prior knowledge

* [Identity and access management (IAM)](/docs/manage/identity-access-management "Configure users, groups and permissions.")
* [Grant access to Dynatrace](/docs/manage/identity-access-management/use-cases/access-platform "Grant access to Dynatrace")
* [User permissions in default groups](/docs/manage/identity-access-management/user-and-group-management/default-groups "Dynatrace default groups reference")

Prerequisites

* A Dynatrace account with administrative privileges.
* Set up the required users, federations, and user groups in advance.

Key terms

Security context
:   Defines the scope of access for a user or group

Management zone
:   Information-partitioning mechanism that promotes collaboration and the sharing of relevant data in your Dynatrace environment

## Steps

Letâs start by setting up the security context, then learn how to create the policies to grant access to data on entities.

1. Set the security context for monitored entities

To set the security context for entities, you can choose one of the following options,

#### Option 1: Use an already existing property of the entity

If you have already set up management zones, it's possible to map the management zones into the security context, depending on its type.

1. Go to **Settings** > **Topology model** > **Grail Security Context**.
2. Expand the relevant entity type
3. In the **Destination property** section, choose the field that should map into the security context. It can be either `managementZones`, `entity.detected_name`, or `dt.security_context` itself.

   ![Grail Security Context ](https://dt-cdn.net/images/123-1532-c8aa238683.webp)

`managementZones` is the default value for the majority of entity types. With this option, the security context of entities is mapped from classic management zones.
Logs, spans, metrics, and events powered by Grail that are sent from an entity do not inherit the management zones of that entity.
This means [access controls](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.") on logs, spans, metrics and events powered by Grail must be handled separately.
This option is useful if you have management zones already in place and you want to re-use those to control access on entities.

#### Option 2: Host tags and properties

You can set the security context using the `dt.security_context` host property set using automated rules or host properties set using [OneAgent configuration via command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

After you set the security context on a host, it will be used to automatically determine the security context for all logs, spans, metrics, and events that are sent from this host.

Additionally, it will set the security context for host-related entities reported from this host, such as process group instances and disks.

With this option, ensure the security context is mapped using the `dt.security_context` field for the entity types of interest, as described in Option 1 above.

To set a security context using `oneagentctl`:

```
./oneagentctl --set-host-property=dt.security_context=my-security-context
```

#### Option 3: Define an extraction rule for generic types

For [generic entity types](/docs/ingest-from/extend-dynatrace/extend-topology/events-entity-extraction#extract-map "Extract generic entities from event metadata and map events to them."), you can add an extraction rule for `dt.security_context` and derive the security context from any detail on the data source.
This is particularly useful for extensions where you can set the `dt.security_context` per extension configuration.

Let's use the PostgreSQL extension with a simplified example, assuming a configuration with `dt.security_context` set to `TeamA`.
For that configuration, the extension sends metric data points using the Metrics API such as:

```
postgres.activity.idle,port=5432,dt.security_context="TeamA",dt.entity.sql:postgres_instance="CUSTOM_DEVICE-..." 42



postgres.activity.idle,port=5432,dt.security_context="TeamA",dt.entity.sql:postgres_instance="CUSTOM_DEVICE-..." 45



postgres.activity.idle,port=5432,dt.security_context="TeamA",dt.entity.sql:postgres_instance="CUSTOM_DEVICE-..." 43
```

Based on this, you can add an extraction rule to the existing PostgreSQL extension extraction rules that sets the `dt.security_context`
to the value of the `dt.security_context` dimension in the metric data points (`TeamA`).

As with option 2, ensure the security context is mapped using the `dt.security_context` field for the entity types of interest.
If the entity types are not listed, we recommend creating those entity types.

#### Option 4: Dynatrace API

This API is deprecated.

Set the security context via the [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2/security-context "Create or delete security context via Dynatrace API.").

2. Create the policy

Entity permissions allow you to define policies that control data access on entities. In contrast to monitoring data, entity permissions only allow filtering for the `dt.security_context` field.

Access to all entities is configured via the `storage:entities:read` permission, which supports the following conditions

* `storage:entity.type`

  the entity type in upper snake case (for example `PROCESS_GROUP_INSTANCE`)
* `storage:dt.security_context`

  the security context of this entity. Can be a multi-value field and `startsWith` will evaluate for any matching value.

For example, the following policy grants access to data with the security context set to `mySecurityContext`.

```
ALLOW



storage:entities:read



WHERE



storage:dt.security_context = "mySecurityContext";
```

## Related topics

* [Monitored entities API - security context](/docs/dynatrace-api/environment-api/entity-v2/security-context "Create or delete security context via Dynatrace API.")
* [IAM policy reference](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.")
* [Working with policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies")