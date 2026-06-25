---
title: Settings API - Generic relationships schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-monitoredentities-generic-relation
scraped: 2026-05-12T11:42:40.817185
---

# Settings API - Generic relationships schema table

# Settings API - Generic relationships schema table

* Published Dec 05, 2023

### Generic relationships (`builtin:monitoredentities.generic.relation)`

Looking for topology extraction support? Find the [topology modelï»¿](https://www.dynatrace.com/support/help/shortlink/topology-model#custom-topology-model "Visit Dynatrace support center") help page here.

Entity types can be related to each other. The relationship registry contains rules by which relationships between related entities are automatically established.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:monitoredentities.generic.relation` | * `group:topology-model` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitoredentities.generic.relation` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:monitoredentities.generic.relation` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitoredentities.generic.relation` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | Enables or disables the relationship | Required |
| Source filters `sources` | Set<[SourceFilter](#SourceFilter)> | Specify all sources which should be evaluated for this relationship rule. The relationship is only created when any of the filters match. | Required |
| Created by `createdBy` | text | The user or extension that created this relationship. | Required |
| Source type name `fromType` | text | Define an entity type as the source of the relationship. | Required |
| Role of source type `fromRole` | text | Specify a role for the source entity. If both source and destination type are the same, referring different roles will allow identification of a relationships direction. If role is left blank, any role of the source type is considered for the relationship. | Optional |
| Type of relationship `typeOfRelation` | enum | Type of the relationship between the Source Type and the Destination Type The element has these enums * `INSTANCE_OF` * `RUNS_ON` * `CHILD_OF` * `CALLS` * `PART_OF` * `SAME_AS` | Required |
| Destination type `toType` | text | Define an entity type as the destination of the relationship. You can choose the same type as the source type. In this case you also may assign different roles for source and destination for having directed relationships. | Required |
| Role of destination type `toRole` | text | Specify a role for the destination entity. If both source and destination type are the same, referring different roles will allow identification of a relationships direction. If role is left blank, any role of the destination type is considered for the relationship. | Optional |

##### The `SourceFilter` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Datasource type `sourceType` | enum | Specify the source type of the filter to identify which data source should be evaluated. The element has these enums * `Metrics` * `Logs` * `Spans` * `Entities` * `Topology` * `Events` * `Business Events` | Required |
| Condition `condition` | text | Specify a filter that needs to match in order for the extraction to happen.  Two different filters are supported: `$eq(value)` will ensure that the source matches exactly 'value', while `$prefix(value)` will ensure that the source begins with exactly 'value'. If your value contains the characters '(', ')' or '~', you need to escape them by adding a '~' in front of them. | Required |
| Mapping Rules `mappingRules` | Set<[MappingRule](#MappingRule)> | Specify all properties which should be compared. If all mapping rules match a relationship between entities will be created. | Required |

##### The `MappingRule` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Source property `sourceProperty` | text | The case-sensitive name of a property of the source type. | Required |
| Source Normalization `sourceTransformation` | enum | Normalize text or leave it as-is? The element has these enums * `Leave text as-is` * `To upper case` * `To lower case` | Required |
| Destination property `destinationProperty` | text | The case-sensitive name of a property of the destination type. | Required |
| Destination Normalization `destinationTransformation` | enum | Normalize text or leave it as-is? The element has these enums * `Leave text as-is` * `To upper case` * `To lower case` | Required |