---
title: Query monitored entities in Grail
source: https://www.dynatrace.com/docs/platform/grail/querying-monitored-entities
scraped: 2026-02-24T21:33:46.572131
---

# Query monitored entities in Grail

# Query monitored entities in Grail

* Latest Dynatrace
* Reference
* 13-min read
* Updated on Oct 13, 2025

This is a guide to effectively using Dynatrace Query Language (DQL) to query monitored entities. This involves using generic DQL features such as expanding arrays, joining data using the `lookup` command, and using the built-in parse functionality.

## Query entity types

To query monitored entities by their respective type, you can use the `dt.entity.*` views.

To initiate the query, start with a blank query in your notebooks and enter `fetch dt.entity`. This triggers an auto-complete dialog where you can select the desired entity type.

![Example of auto-complete for entity types.](https://dt-cdn.net/images/ft-entity-2-1439-af70ed8841.png)

For example, executing the `fetch dt.entity.host` query retrieves all host entities. By default, entity records include the ID and entity name.

```
fetch dt.entity.host
```

To include additional details, you can use the `fieldsAdd` command. As you start typing, the auto-complete feature suggests available fields for the entity type.

Another way to get started is to use one of the built-in topology query snippets.

![Example of how to get started by using built-in topology query snippets.](https://dt-cdn.net/images/topology-1447-687b6417ca.png)

## Query relationships

Relationships are exposed as fields and can be added similarly to other fields. For instance, you can add the `runs` relationship to your host records to obtain a list of all entities running on the host.

```
fetch dt.entity.host



| fieldsAdd runs
```

The `runs` field is a nested record that contains a field for each entity type running on a specific host. Depending on the cardinality, these fields are either strings representing a single entity ID or arrays of strings representing a list of entity IDs. In notebooks, select a nested record in the results list to see its contents.

If you only want to see process groups running on that host, you can specify this in the `fieldsAdd` command. The auto-complete feature will provide a list of possible identifier types.

Selecting a type refines the query to only return an array containing the process group IDs.

```
fetch dt.entity.host



| fieldsAdd runs[dt.entity.process_group]
```

The field names for relationships differ from the original relationship names in the previous Dynatrace. Instead of using a single name prefixed with `fromRelationship` and `toRelationship`, the fields have different names on both sides.

See the [relationship mapping table](#relationship-mapping-table) below to understand how second-generation relationships are represented as DQL fields.

Note that 1:n relationships only return 100 entity IDs per type, per record. In such cases, we recommend using `classicEntitySelector()` instead.

## Entity lookups

You can use the `lookup` command to join data from related entities.

For example, to include the host tags with your service instances, you can access the host from a service instance by following the `runs_on` relationship.

```
fetch dt.entity.service_instance



| fieldsAdd runs_on[dt.entity.host]
```

It's important to note that service instances always run on a single host, which means that you obtain a single host ID per service instance record. This allows you to use the `lookup` command to add the hostname to your records. The hostname is added as the `lookup.entity.name` field.

```
fetch dt.entity.service_instance



| fieldsAdd runs_on[dt.entity.host]



| lookup sourceField:`runs_on[dt.entity.host]`, lookupField:id, [ fetch dt.entity.host ]
```

## Expand relationships

Hosts can run multiple service instances, so the `runs[dt.entity.service_instance]` field is an array of entity IDs.

```
fetch dt.entity.host



| fieldsAdd runs[dt.entity.service_instance]
```

The `lookup` command doesn't apply to arrays of IDs, so you need to use the `expand` command first to retrieve individual records per service instance ID.

```
fetch dt.entity.host



| fieldsAdd runs[dt.entity.service_instance]



| expand runs[dt.entity.service_instance]
```

In this example, the first record expands into three. Now you can use the `lookup` command to get the service instance details that you include in the `lookup` field.

```
fetch dt.entity.host



| fieldsAdd runs[dt.entity.service_instance]



| expand runs[dt.entity.service_instance]



| lookup sourceField:`runs[dt.entity.service_instance]`, lookupField:id, [ fetch dt.entity.service_instance]
```

## Entity tags

Entity tags consist of up to three values: context, key, and value. Dynatrace creates a string representation of these values in the following format:

`[<context>]<key>:<value>`

* All occurrences of the `[`, `]`, and `:` characters need to be escaped using the `\` character.
* The `tags` field returns the string representations of these fields.

The following query example retrieves a list of host entity tags.

```
fetch dt.entity.host



| expand tags, alias:tag



| fields tag
```

You can use the `expand` command to optimize tag filtering. This example filters hosts based on a specific cluster name.

```
fetch dt.entity.host



| expand tags



| filter contains(tags, "[Environment]Cluster.Name:prod-eu-west-6-ireland")
```

If you need structured access to the key, context, or value, you can use the following DPL parse expression to split the string representation into individual fields.

```
fetch dt.entity.host



| expand tags, alias:tag_string



| parse tag_string, """(('['LD:tag_context ']' LD:tag_key (!<<'\\' ':') LD:tag_value)|(LD:tag_key (!<<'\\' ':') LD:tag_value)|LD:tag_key)"""
```

## List fields and relationships

Use the `describe` command to obtain a list of fields and relationships for each entity view.

For example, to retrieve a list of all fields and relationships for the `service_instance` entity view, enter `describe dt.entity.service_instance`:

```
describe dt.entity.service_instance
```

Take this information into account when working with different fields:

* Most entity fields have the same names as in the API v2 environment (for example, gcpZone and oneAgentCustomName).
* The first and last observation timestamp of an entity is stored in the lifetime field, represented as a timeframe type comprising a start and end timestamp. The lifetime of an entity needs to overlap with the query timeframe for the entity to be included in the query.
* Several entity names are prefixed with 'entity.' (for example, `entity.conditional_name`)
* Relationships are returned as records, to learn more about them, see [entity relationships](/docs/semantic-dictionary/model/dt-entities#entity-relationships "Get to know the Semantic Dictionary models related to topology.").

The `describe` command is a valuable tool to explore the Grail data schema.

```
describe dt.entity.service_instance



| filter in(data_types, "record")
```

## Permissions

You need the `storage:entities:read` permission to query entities.

Grail doesn't apply management zone filters. Users having the `storage:entities:read` permission can query all entities.

## Entity selectors

You can use the `classicEntitySelector()` function to simplify starting DQL entity queries. This command takes an entity selector as a string argument and provides a list of entity IDs in return. You can use this list to filter entities based on ID.

For example, you can filter service instances running on hosts with a specific tag.

```
fetch dt.entity.service



| filter in(id, classicEntitySelector("type(service), fromRelationship.runsOnHost(type(host), tag([AWS]Category:ABC))"))
```

You can also obtain this result using native DQL with the following query.

```
fetch dt.entity.service



| fieldsAdd host.id = runs_on[dt.entity.host]



| expand host.id



| lookup sourceField:host.id, lookupField: id, fields:host.tags=tags, [ fetch dt.entity.host]



| expand host.tags



| filter host.tags == "[AWS]Category:ABC"
```

This query has limitations, such as returning only 100 hosts per service entity, and is generally more complex than the previous example using the `classicEntitySelector` function.

### Filtering along relationships

When your query evaluates relationships, we recommend using the [`classicEntitySelector`](/docs/platform/grail/dynatrace-query-language/functions/general-functions#classic-entity-selector "A list of DQL general functions.") function instead of native DQL queries.

In the following examples, the native DQL query will be slower and might yield incomplete results compared to the `classicEntitySelector` query:

```
// fetch all hosts that run Java processes



// using native DQL



fetch dt.entity.host



| expand pgi=contains[dt.entity.process_group_instance]



| filter pgi in [



fetch dt.entity.process_group_instance



| filter matchesValue(softwareTechnologies, "*JAVA*")



| fields id



]
```

```
// fetch all hosts that run Java processes



// using classicEntitySelector()



fetch dt.entity.host



| filter in (id, classicEntitySelector("type(host),toRelationship.isProcessOf(type(PROCESS_GROUP_INSTANCE),softwareTechnologies(JAVA))"))
```

### Combine `classicEntitySelector` with native DQL filters

If you already use the `classicEntitySelector` function, it is better to add all filter criteria into the function call rather than add additional native filter statements. The mixed query is slower than the query that contains all filter conditions in the entity selector.

```
// fetch all LINUX hosts that run Java processes



// using a mix of classicEntitySelector and native DQL filters



fetch dt.entity.host



| filter in (id, classicEntitySelector("type(host),toRelationship.isProcessOf(type(PROCESS_GROUP_INSTANCE),softwareTechnologies(JAVA))"))



| fieldsAdd osType



| filter osType == "LINUX"
```

```
// fetch all LINUX hosts that run Java processes



// using only classicEntitySelector



fetch dt.entity.host



| filter in (id, classicEntitySelector("type(host),osType(LINUX),toRelationship.isProcessOf(type(PROCESS_GROUP_INSTANCE),softwareTechnologies(JAVA))"))



| fieldsAdd osType
```

## Relationship mapping table

Entity relationships in the previous Dynatrace (for example, the environment API v2) are mapped to the new names in DQL records according to the following table.

## Troubleshooting

* **The DQL query returns different or fewer entities than API v2 environment**
  Verify that you are using the same query timeframe `fetch dt.entity.*`. The `classicEntitySelector()` function only returns entities that have a lifetime that overlaps with the query timeframe. By default, DQL queries are executed for the last 2 hours, whereas the default timeframe in the API environment is 72 hours.

## Related topics

* [What is Dynatrace Grail?](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more.")
* [DQL commands](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.")
* [IAM policy reference](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.")
* [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.")
* [Environment API v2 - Entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.")