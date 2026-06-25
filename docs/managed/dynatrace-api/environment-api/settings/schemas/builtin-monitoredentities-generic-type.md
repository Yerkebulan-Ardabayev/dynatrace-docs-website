---
title: Settings API - Generic types schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-monitoredentities-generic-type
scraped: 2026-05-12T11:44:33.661297
---

# Settings API - Generic types schema table

# Settings API - Generic types schema table

* Published Dec 05, 2023

### Generic types (`builtin:monitoredentities.generic.type)`

Looking for topology extraction support? Find the [topology modelï»¿](https://www.dynatrace.com/support/help/shortlink/topology-model#custom-topology-model "Visit Dynatrace support center") help page here.

A generic type allows to define rules for creating custom monitored entities based on ingest data.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:monitoredentities.generic.type` | * `group:topology-model` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitoredentities.generic.type` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:monitoredentities.generic.type` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitoredentities.generic.type` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | Enables or disables the type | Required |
| Type name `name` | text | The entity type name. This type name must be unique and must not be changed after creation. | Required |
| Type display name `displayName` | text | The human readable type name for this entity type. | Required |
| Created by `createdBy` | text | The user or extension that created this type. | Required |
| List of rules `rules` | [ExtractionRule](#ExtractionRule)[] | Specify a list of rules which are evaluated in order. When **any** rule matches, the entity defined according to that rule will be extracted. Subsequent rules will not be evaluated.  Rules are evaluated in the order they appear in this list. Each rule defines how to create a single entity from ingested data. It defines properties like name, identifier and other attributes which are stored as part of that entity. A rule also describes filters which need to match the ingest data in order to create an entity.  Many properties of an extraction rule use *placeholders* to dynamically evaluate and transform ingest data. Such rule properties are called *patterns* and allow combining dimension values with static text. The evaluated result is then used when extracting an entity. Each pattern may use multiple placeholders, each referring a single dimension key. During entity extraction, placeholders are replaced with the respective dimension values.  Placeholders start with `{` and end with `}` (Those characters cannot be part of the static text of a pattern). It is not allowed to nest placeholders.  **Example:**  Ingest data line: `temperature,room=5.30 gauge,min=17.1,max=17.3,sum=34.4,count=2`  ID Pattern: `ROOM_{room}`  Would evaluate to the ID `ROOM_5.30`.  **Example:**  Ingest data line: `device.packets.received,device_number=123,if=eth0 1024`  Attribute Value Extraction Pattern: `192.168.1.{device_number}`  Would evaluate to a string `192.168.1.123` and could be stored as an IP address. | Required |

##### The `ExtractionRule` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Extracted ID pattern `idPattern` | text | ID patterns are comprised of static text and placeholders referring to dimensions in the ingest data. An ID pattern **must** contain at least one placeholder to ensure that different entities will be created.  Take care that the pattern results in the same ID for the same entity. For example, using timestamp or counter-like dimensions as part of the ID would lead to the creation of new entities for each ingest data and is strongly discouraged!  Each dimension key referred to by an identifier placeholder must be present in order to extract an entity. If any dimension key referred to in the identifier is missing, the rule will not be considered for evaluation. If you have cases where you still want to extract the same entity type but have differently named keys, consider creating multiple rules extracting the same entity type. In this case take care that each ID pattern evaluates to the same value if the same entity should be extracted. | Required |
| Instance name pattern `instanceNamePattern` | text | Define a pattern which is used to set the name attribute of the entity. You may define placeholders referencing data source dimensions. | Optional |
| Icon Pattern `iconPattern` | text | Define a pattern which is used to set the icon attribute of the entity. The extracted values must reference barista icon ids. You may define placeholders referencing data source dimensions. | Optional |
| Source filters `sources` | Set<[SourceFilter](#SourceFilter)> | Specify all sources which should be evaluated for this rule. A rule is evaluated if any of the specified source filters match. | Required |
| Additionally required dimensions `requiredDimensions` | Set<[DimensionFilter](#DimensionFilter)> | In addition to the dimensions already referred to in the ID pattern, you may specify additional dimensions which must be present in order to evaluate this rule. | Required |
| Attributes `attributes` | Set<[AttributeEntry](#AttributeEntry)> | All attribute extraction rules will be applied and found attributes will be added to the extracted type. | Required |
| Role `role` | text | If you want to extract multiple entities of the same type from a single ingest line you need to define multiple rules with different roles. | Optional |

##### The `SourceFilter` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Ingest datasource type `sourceType` | enum | Specify the source type of the filter to identify which data source should be evaluated for ingest. The element has these enums * `Metrics` * `Logs` * `Spans` * `Entities` * `Topology` * `Events` * `Business Events` | Required |
| Condition `condition` | text | Specify a filter that needs to match in order for the extraction to happen.  Three different filters are supported: `$eq(value)` will ensure that the source matches exactly 'value', `$prefix(value)` will ensure that the source begins with exactly 'value', '$exists()' will ensure that any source with matching dimension filter exists. If your value contains the characters '(', ')' or '~', you need to escape them by adding a '~' in front of them. | Required |

##### The `DimensionFilter` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Dimension key `key` | text | A dimension key which needs to exist in the ingest data to match this filter. | Required |
| Dimension value pattern `valuePattern` | text | A dimension value pattern which needs to exist in the ingest data to match this filter. | Optional |

##### The `AttributeEntry` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Attribute key `key` | text | The attribute key is the unique name of the attribute. | Required |
| Attribute display name `displayName` | text | The human readable attribute name for this extraction rule. Leave blank to use the key as the display name. | Optional |
| Attribute value extraction pattern `pattern` | text | Pattern for specifying the value for the extracted attribute. Can be a static value, placeholders or a combination of both. | Required |