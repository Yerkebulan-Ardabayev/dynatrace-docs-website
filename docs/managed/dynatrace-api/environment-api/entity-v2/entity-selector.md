---
title: Environment API v2 - Entity selector
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/entity-v2/entity-selector
---

# Environment API v2 - Entity selector

# Environment API v2 - Entity selector

* Reference
* Updated on Oct 02, 2026

The entity selector is a powerful instrument for specifying which entities you want to include in the scope of your Environment API v2 calls. It is used in several APIs, so you only have to learn the syntax once and then reuse it for multiple use cases.

You must specify one of following criteria:

* [Entity type](#type)
* [Entity ID](#id)

Additionally you can provide the following criteria in any combination:

* [Entity name](#name)
* [Entity attribute](#attribute)
* [Tag](#tag)
* [Resource attributes](#resourceattributes)
* [Management zone ID](#mzid)
* [Management zone name](#mzname)
* [Health state](#health)
* [Inclusion of deleted entities](#deletedEntities)

If you provide several criteria, only results matching **all** criteria are included in the response.

* For example: `type(HOST),entityName.equals(Server)`

If the text input in the criteria contains certain symbols, such as parentheses or a comma, the text must be enclosed in quotation marks.

* For example: `type(HOST),entityName.equals("Server(prod),1")`

## Limitations

The total length of the **entitySelector** string is limited to 2,000 characters.

You can select only one type of entity per query.

## Entity type

The type of the entity you want to query.

You can fetch the list of available entity types with the [GET all entity types](/managed/dynatrace-api/environment-api/entity-v2/get-all-entity-types "View all types of monitored entities in your environment via Dynatrace API.") call.

|  |  |
| --- | --- |
| Syntax | `type("value")` |
| Multiple values | Not applicable |
| Value operator | `EQUALS` |
| Case-sensitive value | Not applicable |

## Dynatrace entity ID

The Dynatrace entity ID of the requested entity.

To specify several IDs, separate them by a comma (`,`). All requested entities must be of the same type.

You can fetch the list of available entities with the [GET entities list](/managed/dynatrace-api/environment-api/entity-v2/get-entities-list "View a list of monitored entities via Dynatrace API.") call.

|  |  |
| --- | --- |
| Syntax | `entityId("id-1","id-2")` |
| Multiple values | Applicable |
| Value operator | `EQUALS` |
| Case-sensitive value | Not applicable |

## Entity name

The name of the requested entity.

You can fetch the list of available entities with the [GET entities list](/managed/dynatrace-api/environment-api/entity-v2/get-entities-list "View a list of monitored entities via Dynatrace API.") call.

|  |  |
| --- | --- |
| Syntax | `entityName("name")` |
| Multiple values | Not applicable |
| Value operator | `CONTAINS` |
| Case-sensitive value | Not applicable |

### Starts with modification

Changes the value operator of the entity name criterion to `BEGINS WITH`.

|  |  |
| --- | --- |
| Syntax | `entityName.startsWith("name")` |
| Multiple values | Not applicable |
| Value operator | `BEGINS WITH` |
| Case-sensitive value | Not applicable |

### Equals modification

Changes the value operator of the entity name criterion to `EQUALS`.

|  |  |
| --- | --- |
| Syntax | `entityName.equals("name")` |
| Multiple values | Not applicable |
| Value operator | `EQUALS` |
| Case-sensitive value | Not applicable |

### One of values modification

Enables you to provide multiple values for the entity name criterion.

|  |  |
| --- | --- |
| Syntax | `entityName.in("name1","name2")` |
| Multiple values | Applicable |
| Value operator | `EQUALS` |
| Case-sensitive value | Not applicable |

### Case sensitive modification

By default entity names evaluation disregards the case. You can make the criterion stricter by using the `caseSensitive` modification. It takes any entity name criterion as an argument (including those already modified with `.startsWith` or `.equals` modifiers) and evaluates values as case-sensitive.

|  |  |
| --- | --- |
| Syntax | `caseSensitive(<entity name criterion>)` |
| Multiple arguments | Not applicable |

## Entity attribute

The attribute name—attribute value pair that the requested entity should have.

To fetch the list of available attributes, execute the [GET entity type](/managed/dynatrace-api/environment-api/entity-v2/get-entity-type "View the details of a monitored entity type via Dynatrace API.") call and check the **properties** field. You can use attributes with values that can be represented by a string.

|  |  |
| --- | --- |
| Syntax | `<attribute name>("attribute value")` |
| Multiple values | Applicable |
| Value operator | `EQUALS` |
| Case-sensitive attribute name | Not applicable |
| Case-sensitive attribute value | Applicable |

### Exists modification

Changes the operator of the entity attribute criterion to `EXISTS`. In this case, the condition selects the entities that have the attribute, regardless of the attribute's value.

|  |  |
| --- | --- |
| Syntax | `<attribute name>.exists()` |
| Operator | `EXISTS` |

## Tag

The tag of the requested entities. Tags in `[context]key:value`, `key:value`, and `value` formats are detected and parsed automatically. If a value-only tag has a colon (`:`) in it, you must escape the colon with a backslash(`\`). Otherwise, the tag will be parsed as a `key:value` tag.

To specify several tags, separate them by a comma (`,`). An entity with **any** of the specified tags is included in the response.

You can fetch the list of available tags with the [GET custom tags](/managed/dynatrace-api/environment-api/custom-tags/get-tags "View custom tags of monitored entities via Dynatrace API.") and the [GET auto-tags](/managed/dynatrace-api/configuration-api/automatically-applied-tags-api/get-all "View all automatically applied tags of your environment via the Dynatrace API.") calls.

|  |  |
| --- | --- |
| Syntax | `tag("[context]key1:value-1","key2:value-2","value-3")` |
| Multiple values | Applicable |
| Value operator | `EQUALS` |
| Case-sensitive value | Applicable |

## Resource attributes

The resource attributes of the requested entities. Use `resourceAttributes("<key>")` to select entities that report an attribute regardless of its value, or `resourceAttributes("<key>:<value>")` to select entities that report the attribute with a specific value.

To specify several attributes, separate them by a comma (`,`). An entity with **any** of the specified attributes is included in the response. You can specify up to 10 values in one `resourceAttributes` criterion, which is separate from the limit on how many resource attributes Dynatrace stores per entity—see [Resource attribute limits and excluded keys](/managed/ingest-from/dynatrace-oneagent/resource-attributes#ra-limits "Understand the resource attributes stored on Dynatrace Managed hosts, processes, and containers, including configuration, filtering, and storage limits.").

Resource attribute keys depend on what OneAgent, Dynatrace Operator, and your own configuration report for an entity, so they vary by environment. To read the keys and values of a specific entity, use the [GET an entity](/managed/dynatrace-api/environment-api/entity-v2/get-entity "View parameters of a monitored entity via Dynatrace API.") request; the [GET entity type](/managed/dynatrace-api/environment-api/entity-v2/get-entity-type "View the details of a monitored entity type via Dynatrace API.") request lists `resourceAttributes` among the properties an entity of that type can have, but not the keys themselves. You can also check the **Properties** section of the entity page, as described in [Where to see resource attributes](/managed/ingest-from/dynatrace-oneagent/resource-attributes#where-to-see "Understand the resource attributes stored on Dynatrace Managed hosts, processes, and containers, including configuration, filtering, and storage limits.").

|  |  |
| --- | --- |
| Syntax | `resourceAttributes("key-1","key-2:value-2")` |
| Multiple values | Applicable |
| Value operator | `EQUALS` |
| Case-sensitive value | Applicable |

A colon (`:`) separates the key from the value and can't be escaped inside a value. Only the text between the first and the second colon is matched, so you can't match a value that itself contains a colon—unlike the [Tag](#tag) criterion, where you escape a colon in a value with a backslash (`\`). To select entities by such an attribute, omit the value and match on the key alone.

## Management zone ID

The ID of the management zone to which the requested entities belong.

To specify several IDs, separate them by a comma (`,`).

You can fetch the list of available management zones with the [GET all management zones](/managed/dynatrace-api/configuration-api/management-zones-api/get-all "View all management zones of your environment via the Dynatrace API.") call.

|  |  |
| --- | --- |
| Syntax | `mzId("123456789","987654321")` |
| Multiple values | Applicable |
| Value operator | `EQUALS` |
| Case-sensitive value | n/a |

## Management zone name

The name of the management zone to which the requested entities belong.

To specify several names, separate them by a comma (`,`).

You can fetch the list of available management zones with the [GET all management zones](/managed/dynatrace-api/configuration-api/management-zones-api/get-all "View all management zones of your environment via the Dynatrace API.") call.

|  |  |
| --- | --- |
| Syntax | `mzName("name-1","name-2")` |
| Multiple values | Applicable |
| Value operator | `EQUALS` |
| Case-sensitive value | Applicable |

## Health state

The health state of the requested entities. Possible values are `HEALTHY` and `UNHEALTHY`.

|  |  |
| --- | --- |
| Syntax | `healthState("HEALTHY")` |
| Multiple values | Not applicable |
| Value operator | `EQUALS` |
| Case-sensitive value | Applicable |

## First seen

The timestamp (UTC milliseconds) when the entity was seen for the first time.

|  |  |
| --- | --- |
| Syntax | `firstSeenTms.<operator>(timestamp)` |
| Multiple values | Not applicable |
| Value operator | * `lte`: earlier than or at the specified time * `lt`: earlier than the specified time * `gte`: later than or at the specified time * `gt`: later than the specified time |
| Case-sensitive value | n/a |

## Inclusion of deleted entities

Include or exclude entities marked as deleted. Those are limited to the following entity types:

* `HTTP_CHECK`
* `SYNTHETIC_TEST`
* `EXTERNAL_SYNTHETIC_TEST`
* `MULTIPROTOCOL_MONITOR`
* `APPLICATION`
* `MOBILE_APPLICATION`
* `CUSTOM_APPLICATION`
* `DCRUM_APPLICATION`
* `CUSTOM_DEVICE`

|  |  |
| --- | --- |
| Syntax | `deletedEntities.<operator>()` |
| Operator | * `include`: include deleted entities * `exclude`: exclude deleted entities |
| Values | Not applicable |
| Example | `type(HTTP_CHECK), deletedEntities.include()`: Select all entities of type `HTTP_CHECK` and include the ones marked as deleted. |
| Note | * By default, deleted entities are excluded from all results. * This is not supported in [management zone rules](/managed/manage/identity-access-management-classic/permission-management/management-zones/management-zone-rules#text "Define management-zone rules to control access to monitored entities, logs, and metrics using entity conditions, dimensional data, and entity selectors.") and [automatic tagging](/managed/manage/tags-and-metadata-classic/setup/how-to-define-tags#automatic "Define and apply tags manually or automatically to organize Dynatrace entities, using rule conditions based on entity properties and regular expressions."). |

## Relationships

Relationships that the requested entity should have.

To fetch the list of available relationships, issue the [GET entity type](/managed/dynatrace-api/environment-api/entity-v2/get-entity-type "View the details of a monitored entity type via Dynatrace API.") call and check the **fromRelationships** and **toRelationships** fields.

|  |  |
| --- | --- |
| Syntax | * `fromRelationships.<relationship>(<entitySelector>)` * `toRelationships.<relationship>(<entitySelector>)` |
| Multiple arguments | Not applicable |
| Note | Takes an entity selector as an attribute. |

## Negate criterion

You can use the `not` modification to invert any criterion except for **type**. It takes a criterion as an argument and inverts the condition. For example, the `not(tag("Infrastructure:Linux"))` criterion selects entities that do *not* have the **Infrastructure:Linux** tag.

You can use the negated criteria as part of complicated selectors, just like any other criteria.

|  |  |
| --- | --- |
| Syntax | `not (<criterion>)` |
| Multiple arguments | Not applicable |
| Note | Doesn't support [**type** criteria](#type). |

## Related topics

* [Custom tags API](/managed/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.")
* [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.")
* [Monitored entities API](/managed/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.")
* [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers.")