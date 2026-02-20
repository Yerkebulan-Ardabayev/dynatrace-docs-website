---
title: Environment API v2 - Entity selector
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/entity-v2/entity-selector
scraped: 2026-02-20T21:22:00.097540
---

# Environment API v2 - Entity selector

# Environment API v2 - Entity selector

* Reference
* Updated on Jan 27, 2026

The entity selector is a powerful instrument for specifying which entities you want to include to the scope of your Environment v2 API calls. It is used in several APIs, so you only have to learn the syntax once and then reuse it for multiple use cases.

You must specify one of following criteria:

* [Entity type](#type)
* [Entity ID](#id)

Additionally you can provide the following criteria in any combination:

* [Entity name](#name)
* [Entity attribute](#attribute)
* [Tag](#tag)
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

You can fetch the list of available entity types with the [GET all entity types](/docs/dynatrace-api/environment-api/entity-v2/get-all-entity-types "View all types of monitored entities in your environment via Dynatrace API.") call.

|  |  |
| --- | --- |
| Syntax | `type("value")` |
| Multiple values | Not applicable |
| Value operator | `EQUALS` |
| Case-sensitive value | Not applicable |

## Dynatrace entity ID

The Dynatrace entity ID of the requested entity.

To specify several IDs, separate them by a comma (`,`). All requested entities must be of the same type.

You can fetch the list of available entities with the [GET entities list](/docs/dynatrace-api/environment-api/entity-v2/get-entities-list "View a list of monitored entities via Dynatrace API.") call.

|  |  |
| --- | --- |
| Syntax | `entityId("id-1","id-2")` |
| Multiple values | Applicable |
| Value operator | `EQUALS` |
| Case-sensitive value | Not applicable |

## Entity name

The name of the requested entity.

You can fetch the list of available entities with the [GET entities list](/docs/dynatrace-api/environment-api/entity-v2/get-entities-list "View a list of monitored entities via Dynatrace API.") call.

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

The attribute nameâattribute value pair that the requested entity should have.

To fetch the list of available attributes, execute the [GET entity type](/docs/dynatrace-api/environment-api/entity-v2/get-entity-type "View the details of a monitored entity type via Dynatrace API.") call and check the **properties** field. You can use attributes with values that can be represented by a string.

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

To specify several tags, separate them by a comma (`,`). An entity with **any** of the specified tags is included to the response.

You can fetch the list of available tags with the [GET custom tags](/docs/dynatrace-api/environment-api/custom-tags/get-tags "View custom tags of monitored entities via Dynatrace API.") and the [GET auto-tags](/docs/dynatrace-api/configuration-api/automatically-applied-tags-api/get-all "View all automatically applied tags of your environment via the Dynatrace API.") calls.

|  |  |
| --- | --- |
| Syntax | `tag("[context]key1:value-1","key2:value-2","value-3")` |
| Multiple values | Applicable |
| Value operator | `EQUALS` |
| Case-sensitive value | Applicable |

## Management zone ID

The ID of the management zone to which the requested entities belong.

To specify several IDs, separate them by a comma (`,`).

You can fetch the list of available management zones with the [GET all management zones](/docs/dynatrace-api/configuration-api/management-zones-api/get-all "View all management zones of your environment via the Dynatrace API.") call.

|  |  |
| --- | --- |
| Syntax | `mzId("123456789","987654321")` |
| Multiple values | Applicable |
| Value operator | `EQUALS` |
| Case-sensitive value | n/a |

## Management zone name

The name of the management zone to which the requested entities belong.

To specify several names, separate them by a comma (`,`).

You can fetch the list of available management zones with the [GET all management zones](/docs/dynatrace-api/configuration-api/management-zones-api/get-all "View all management zones of your environment via the Dynatrace API.") call.

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

Syntax

`firstSeenTms.<operator>(timestamp)`

Multiple values

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

Value operator

* `lte`: earlier than or at the specified time
* `lt`: earlier than the specified time
* `gte`: later than or at the specified time
* `gt`: later than the specified time

Case-sensitive value

n/a

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

Syntax

`deletedEntities.<operator>()`

Operator

* `include`: include deleted entities
* `exclude`: exclude deleted entities

Values

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

Example

`type(HTTP_CHECK), deletedEntities.include()`: Select all entities of type `HTTP_CHECK` and include the ones marked as deleted.

Note

* By default, deleted entities are excluded from all results.
* This is not supported in [management zone rules](/docs/manage/identity-access-management/permission-management/management-zones/management-zone-rules#text "Define rules to limit the entities accessible within a management zone.") and [automatic tagging](/docs/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Find out how to define and apply tags manually and automatically.").

## Relationships

Relationships that the requested entity should have.

To fetch the list of available relationships, issue the [GET entity type](/docs/dynatrace-api/environment-api/entity-v2/get-entity-type "View the details of a monitored entity type via Dynatrace API.") call and check the **fromRelationships** and **toRelationships** fields.

Syntax

* `fromRelationships.<relationship>(<entitySelector>)`
* `toRelationships.<relationship>(<entitySelector>)`

Multiple arguments

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

Note

Takes an entity selector as an attribute.

## Negate criterion



You can use the `not` modification to invert any criterion except for **type**. It takes a criterion as an argument and inverts the condition. For example, the `not(tag("Infrastructure:Linux"))` criterion selects entities that do *not* have the **Infrastructure:Linux** tag.

You can use the negated criteria as part of complicated selectors, just like any other criteria.

|  |  |
| --- | --- |
| Syntax | `not (<criterion>)` |
| Multiple arguments | Not applicable |
| Note | Doesn't support [**type** criteria](#type). |

## Related topics

* [Custom tags API](/docs/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.")
* [Metrics API v2](/docs/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.")
* [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.")
* [Problems API v2](/docs/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers.")