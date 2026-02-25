---
title: Include data in segments
source: https://www.dynatrace.com/docs/manage/segments/concepts/segments-concepts-includes
scraped: 2026-02-25T21:22:59.954917
---

# Include data in segments

# Include data in segments

* Latest Dynatrace
* Explanation
* 5-min read
* Updated on Nov 04, 2025

Segments can logically structure and serve as convenient filters when analyzing data in different apps. Segments are constructed based on rules, called **Includes**. Learn how data of different types can be included in segments.

## Key terms

Include
:   Single rule, referencing data to be included in segment. Querying for data not explicitly referenced by any include of the selected segment, will lead to empty results.

Signal
:   Observed data point, emmitted by a monitored entity. Available signal types in Dynatrace are `logs`, `metrics`, `events`, `spans`, and others.

Monitored entity
:   Logical component monitored by Dynatrace, persisted as Smartscape node and/or classic entity.

Smartscape node
:   Node topology objects, similar to entities on the Dynatrace cluster. Nodes are a collection of all kinds of entities, regardless of their type.

Classic entity
:   Application, service, process, host, or data center entity stored on the Dynatrace cluster (such as `dt.entity.host`, `dt.entity.service`, `dt.entity.kubernetes_cluster`). Classic entities are bound to a type.

## Includes

Segments are constructed incrementally through includes, step by step, extending the scope of the segment. Includes reference a certain data type and are defined by a filter condition for data of that type.

In its initial state, logically speaking, a segment can be considered empty. To use a segment for filtering, data needs to be included.

![An example of segments missing data](https://dt-cdn.net/images/segments-includes-new-2076-89db100a5d.png)

In the following example, two include blocks were added to include logs and metrics by the given conditions. This illustrates how includes incrementally extend the scope of a segment.

![segments query](https://dt-cdn.net/images/segments-4-1478-162bffb583.png)

Include block order doesn't matter

Include blocks are ORed together.

You can drag  include blocks up and down in the web UI, but this affects only the order in which they are displayed in the UI, and does not influence which data is included in the segment.

Logical conditions within a single include can of course be more complex than simple equals-matches conditions as shown above.

![segments query](https://dt-cdn.net/images/segments-5-1498-f099426644.png)

Conditions of segment includes are evaluated at query time, directly impacting query performance. Make sure to consider [![OpenPipeline](https://cdn.bfldr.com/B686QPH3/at/rp4vgwhpjx5rv6rm53mk88cc/OpenPipeline.svg?auto=webp&width=72&height=72 "OpenPipeline") OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.") to process fields and simplify complex conditions.

## Data types

### Signals

Collecting observability signals is at the core of Dynatrace, so you need to understand their schema and build segments around how those signals are shaped.

Signals can be included in segments in a number of ways. For the better efficiency of resulting filter expressions, always try to reference them directly.

![Segments: data types example: three include blocks added to include logs, metrics, and events](https://dt-cdn.net/images/data-types-1-2248-556d6370c4.png)

Configurations like the one above can also be expressed more elegantly using the **All data types** option:

![Segments: data types example: using the "All data types" option as a more elegant solution](https://dt-cdn.net/images/data-types-5-2248-9558f6aca9.png)

Since context matters, and the unique monitored entity model in Dynatrace provides an alternative way to work with observability signals, there is a second option to include signals through entity-to-signal relationships.

#### Entity-to-entity relationships

Entity relationships in segments are only supported for backward compatibility with classic entities.

A further benefit of segments in regards to monitored entities is being able to leverage relationships between them.

While working with entities stored as Smartscape nodes in Grail has multiple benefits, it's sometimes necessary to construct segments for classic entities. For instance, this enables having segments that include Kubernetes workloads or other monitored entities of higher cardinality, filtered by their related Kubernetes clusters.

![segments entity relationships](https://dt-cdn.net/images/segments-entities-relationships-2842-fb9d9bec55.png)

Segments allow a single relationship traversal step only. However, multiple parallel relationships of the same originating entity can be configured.