---
title: Smartscape on Grail
source: https://www.dynatrace.com/docs/platform/grail/smartscape-on-grail
scraped: 2026-02-28T21:19:38.405376
---

# Smartscape on Grail

# Smartscape on Grail

* Latest Dynatrace
* Explanation
* Updated on Jan 16, 2026
* Preview

Smartscape on Grail is a Grail-native storage that automatically records topological data, such as monitored entities and relationships.

Smartscape on Grail uses the power of DQL queries to:

* Represent entities as nodes.
* Represent relationships as edges.
* Traverse from one node to another.

This gives you deeper insight into your data records and allows you to manipulate and extract necessary information for further analysis.

## Access Smartscape on Grail

Smartscape on Grail is fully integrated into DQL and introduces new commands and functions that you can use to:

* Query nodes and edges.
* Enrich monitoring data, such as logs and spans, with entity details.
* Navigate the topology.
* Filter your topology based on complex relations.

Costs and DPS license

Smartscape on Grail is included in the DPS license. This means that data returned from Smartscape queries doesn't incur any additional cost.

## Smartscape on Grail features

### Mutable data

The data stored in traditional bucketsâsuch as logs, events, spans, or metric data pointsâis ingested for a particular timestamp and never changes. In comparison, Smartscape nodes and edges are mutable and can change over time.

### Smartscape IDs

Smartscape nodes are identified via an ID, represented by a Grail datatype `Smartscape ID`. Smartscape IDs are updated regularly through the upsert events.

A Smartscape ID consists of the entity type and a 16-symbol long number. It can be represented by a following string:

* `ENTITY_TYPE-000000000000007B`

The Smartscape type is fully compatible with its string representation, meaning that you can compare a string to Smartscape ID.

### Type

Every node has a type field that describes the entity type and determines the schema of the entity. The Semantic Dictionary contains the schema for each of the types. By convention, node types are always formatted in uppercase, like `HOST`, `K8S_NAMESPACE`, and `AWS_EC2_INSTANCE`.

### Lifetime

Because nodes are updated regularly, they don't have a single timestamp field. Instead, nodes have two timeframe fields that represent the node's lifetime:

* `lifetime.start`: the first time when the node was discovered.
* `lifetime.end`: the time when the node was last observed.

While the `lifetime.start` field will remain unchanged, the `lifetime.end` field will be continuously updated with every incoming upsert event as long as the node is still being observed.

Based on the query timeframe, you will see only those nodes that have a lifetime overlapping with the query timeframe. For example, a node with a `lifetime.end` field containing yesterday's data won't be included in a query result for the last 2 hours.

### Edges

Edges are relationships that connect two nodes to each other. An edge always stores an edge type (such as `runs_on`, `calls` or `relates_to`), and two IDs of two different nodes.

How an edge is stored on a node depends on whether the edge is static or dynamic:

* Static: the edge inherits the node's lifetime.
* Dynamic: the edge is recorded for a specific point in time.

Edges stored statically are included in results where the query timeframe overlaps with the node's lifetime, whereas dynamic edges are included in query results based on a timeframe when the edge was recorded.

Static edges are mostly based on configuration, such as when a disk is configured to be attached to a specific host. Dynamic edges are typically based on monitoring signals that reveal a specific relationship between nodes, such as when a service based on traces calls another service.

### Node references

All static edges can be accessed through the source node via the `references` field. While this field is hidden by default, you can display it and use it in queries with the help of the `fieldsAdd` command.

You can see the examples of using the `references` field below:

Display the references field by using fieldsAdd for all nodes

```
smartscapeNodes "*"



| fieldsAdd references
```

Summarize containers by the host ID they're running on

```
smartscapeNodes CONTAINER



| summarize by:references[runs_on.host], count()
```

### Data retention

Data retention is fixed at 35 days. This means that nodes whose `lifetime.end` is older than 35 days will be deleted, including all static edges. Dynamic edges will be cleaned up after 35 days as well.

### Signal's connection to Smartscape nodes

A signal's fields that start with `dt.smartscape.__type__` and contain Smartscape IDs indicate that the signal has originated within a given node. A single signal can have multiple `dt.smartscape.__type__` fields.

Optionally, a signal can also have:

* A `dt.smartscape_source.id` field that points to the exact source that produced the signal.
* A `dt.smartscape_source.type` field that describes the type of the entity that produced the signal.

### Tags

Each node has a special field called `tags` that contains different nested fields recognized as tags.

Currently, tags can only be set at the data source. That means that, for example:

* Kubernetes monitoring adds labels and annotations as tags.
* Cloud monitoring adds AWS tags.
* OneAgent adds agent tags.

### Security context

Similar to other data stored in Grail, Smartscape nodes have a `dt.security_context` field that can contain multiple values.

The `dt.security_context` field is an optional node field and is empty by default, since the regular permission fields are fully supported and often sufficient.

### Field permissions

You can configure and use [fieldsets](/docs/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-fields "Find out how to assign permissions to buckets and tables in Grail.") with the `smartscape` table to apply filters to all data returned by Smartscape commands (`smartscapeNodes` and `smartscapeEdges`). Be aware that only certain fields can be filtered out for all entity types simultaneously.

See the example of a field set configuration below:

Define a new fieldset to filter Kubernetes configuration details

To define a new fieldset that filters the Kubernetes configuration details that are stored in the `k8s.object` field, you can use the API with the following request:

```
POST /fieldsets



{



"name": "sensitive-field-k8s-object",



"description": "Make k8s.object sensitive",



"enabled": true,



"scope": "TABLE",



"fields": [



"k8s.object"



],



"tables": [



"smartscape"



]



}
```

Now only users that have the permission `ALLOW storage:fieldsets:read WHERE storage:fieldset-name="sensitive-field-k8s-object"` will be able to read the details of this field.

### Classic entity IDs

Node types used by Smartscape on Grail might be different from classic entity types. This means that the entity or node ID might also be different (for example, `CLOUD_APPLICATION_INSTANCE` is called `K8S_POD` in Smartscape on Grail). To avoid confusion, Smartscape nodes include an `id_classic` field that contains the entity ID of the corresponding classic entity. Classic entity IDs are available for K8s entities, core entities, and services.

If there are no corresponding classic entities (for example, with [Clouds](/docs/observe/infrastructure-observability/cloud-platform-monitoring "The cloud platforms Dynatrace can monitor")), there are no `id_classic` fields on those nodes.

## Differences between classic entities and Smartscape on Grail

## Smartscape segments

Smartscape nodes can be filtered with the help of

* "All data" segment
* "Entity" segment rules

Only Smartscape nodes can be filtered using segments, meaning that Smartscape edges can't be filtered.

## Extract via OpenPipeline

[OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.") offers dedicated stages for node and edge extraction and processing. Use OpenPipeline to extract topological data from any signal for the following purposes:

* Custom entity type definition, such as extensions
* Additional information on Dynatrace built-in types

## Related topics

* [DQL Smartscape commands](/docs/platform/grail/dynatrace-query-language/commands/smartscape-commands "DQL Smartscape commands")
* [Join functions](/docs/platform/grail/dynatrace-query-language/functions/join-functions "A list of DQL join functions.")
* [Conversion and casting functions](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions "A list of DQL conversion and casting functions.")
* [DPL Smartscape ID](/docs/platform/grail/dynatrace-pattern-language/log-processing-smartscape "Explore DPL syntax for parsing out Smartscape ID from strings.")
* [DPL Grammar](/docs/platform/grail/dynatrace-pattern-language/log-processing-grammar "Complete grammar list of Dynatrace Pattern Language (DPL) syntax.")