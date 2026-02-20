---
title: Query monitored entities in Grail
source: https://www.dynatrace.com/docs/platform/grail/querying-monitored-entities
scraped: 2026-02-20T21:27:06.485732
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

`entity.name`

`id`

HOST-1

HOST-123

HOST-2

HOST-456

HOST-3

HOST-789

HOST-4

HOST-101

HOST-5

HOST-111

HOST-6

HOST-131

HOST-7

HOST-141

To include additional details, you can use the `fieldsAdd` command. As you start typing, the auto-complete feature suggests available fields for the entity type.

Another way to get started is to use one of the built-in topology query snippets.

![Example of how to get started by using built-in topology query snippets.](https://dt-cdn.net/images/topology-1447-687b6417ca.png)

## Query relationships

Relationships are exposed as fields and can be added similarly to other fields. For instance, you can add the `runs` relationship to your host records to obtain a list of all entities running on the host.

```
fetch dt.entity.host



| fieldsAdd runs
```

`entity.name`

`id`

`runs`

HOST-1

HOST-123

runs: Complex record

HOST-2

HOST-456

runs: Complex record

HOST-3

HOST-789

runs: Complex record

The `runs` field is a nested record that contains a field for each entity type running on a specific host. Depending on the cardinality, these fields are either strings representing a single entity ID or arrays of strings representing a list of entity IDs. In notebooks, select a nested record in the results list to see its contents.

If you only want to see process groups running on that host, you can specify this in the `fieldsAdd` command. The auto-complete feature will provide a list of possible identifier types.

Selecting a type refines the query to only return an array containing the process group IDs.

```
fetch dt.entity.host



| fieldsAdd runs[dt.entity.process_group]
```

`entity.name`

`id`

`runs[dt.entity.process_group]`

HOST-1

HOST-123

runs: PROCESS\_GROUP-D123, PROCESS\_GROUP-567, PROCESS\_GROUP-012

HOST-2

HOST-456

runs: PROCESS\_GROUP-D234, PROCESS\_GROUP-234, PROCESS\_GROUP-F10

HOST-3

HOST-789

runs: PROCESS\_GROUP-D567, PROCESS\_GROUP-789, PROCESS\_GROUP-123

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

`entity.name`

`id`

`runs_on[dt.entity.host]`

Mapped Instance for answer\_queue on ActiveMQ Artemis

SERVICE\_INSTANCE-1AB2

HOST-1

Mapped Instance for Requests executed in the background threads of eT-demo-1-BussinessBackend

SERVICE\_INSTANCE-A123

HOST-2

It's important to note that service instances always run on a single host, which means that you obtain a single host ID per service instance record. This allows you to use the `lookup` command to add the hostname to your records. The hostname is added as the `lookup.entity.name` field.

```
fetch dt.entity.service_instance



| fieldsAdd runs_on[dt.entity.host]



| lookup sourceField:`runs_on[dt.entity.host]`, lookupField:id, [ fetch dt.entity.host ]
```

`entity.name`

`id`

`runs_on[dt.entity.host]`

`lookup.entity.name`

`lookup.id`

Mapped Instance for answer\_queue on ActiveMQ Artemis

SERVICE\_INSTANCE-2AB1

HOST-1

AB1-abc

HOST-1

Mapped Instance for Requests executed in the background threads of eT-demo-1-BussinessBackend

SERVICE\_INSTANCE-B123

HOST-2

BA1-cba

HOST-2

Mapped Instance for :80

SERVICE\_INSTANCE-C321

HOST-3

BA1-cba

HOST-2

## Expand relationships

Hosts can run multiple service instances, so the `runs[dt.entity.service_instance]` field is an array of entity IDs.

```
fetch dt.entity.host



| fieldsAdd runs[dt.entity.service_instance]
```

`entity.name`

`id`

`runs[dt.entity.service_instance]`

dw123

HOST-1

SERVICE\_INSTANCE-AB123

dw123

HOST-1

SERVICE\_INSTANCE-CB123

dw123

HOST-1

SERVICE\_INSTANCE-DB123

abc/123

HOST-2

SERVICE\_INSTANCE-AB902

The `lookup` command doesn't apply to arrays of IDs, so you need to use the `expand` command first to retrieve individual records per service instance ID.

```
fetch dt.entity.host



| fieldsAdd runs[dt.entity.service_instance]



| expand runs[dt.entity.service_instance]
```

`entity.name`

`id`

`runs[dt.entity.service_instance]`

dw123

HOST-1

SERVICE\_INSTANCE-DB123

dw456

HOST-2

SERVICE\_INSTANCE-BA987

dw789

HOST-3

SERVICE\_INSTANCE-CA687

dw652

HOST-4

SERVICE\_INSTANCE-1AB2

In this example, the first record expands into three. Now you can use the `lookup` command to get the service instance details that you include in the `lookup` field.

```
fetch dt.entity.host



| fieldsAdd runs[dt.entity.service_instance]



| expand runs[dt.entity.service_instance]



| lookup sourceField:`runs[dt.entity.service_instance]`, lookupField:id, [ fetch dt.entity.service_instance]
```

`entity.name`

`id`

`runs[dt.entity.service_instance]`

`lookup.entity.name`

`lookup.id`

dw123

HOST-1

SERVICE\_INSTANCE-AB123

Mapped instance for easytravelazure-weather-service

SERVICE\_INSTANCE-AB123

dw123

HOST-1

SERVICE\_INSTANCE-CB123

Mapped Instance for weather-service-restify

SERVICE\_INSTANCE-CB123

dw123

HOST-1

SERVICE\_INSTANCE-DB123

Mapped Instance for easytravelazure-weather-express

SERVICE\_INSTANCE-DB123

abc/123

HOST-2

SERVICE\_INSTANCE-AB902

Mapped Instance for easytravel-frontend

SERVICE\_INSTANCE-AB902

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

`tag`

AppSec:Node.js

[Azure]tenant:CustomerA

HostName:dw123

AppSec:.NET

[AWS]created\_at:2023-07-07T12:20:10Z

[Environment]tema:cpn

You can use the `expand` command to optimize tag filtering. This example filters hosts based on a specific cluster name.

```
fetch dt.entity.host



| expand tags



| filter contains(tags, "[Environment]Cluster.Name:prod-eu-west-6-ireland")
```

`entity.name`

`id`

`tags`

HOST-1

HOST-C2

tags:[Environment]Cluster.Name:prod-eu-west-6-ireland

HOST-2

HOST-C3

tags:[Environment]Cluster.Name:prod-eu-west-6-ireland

HOST-3

HOST-C4

tags:[Environment]Cluster.Name:prod-eu-west-6-ireland

HOST-4

HOST-C5

tags:[Environment]Cluster.Name:prod-eu-west-6-ireland

HOST-5

HOST-C6

tags:[Environment]Cluster.Name:prod-eu-west-6-ireland

If you need structured access to the key, context, or value, you can use the following DPL parse expression to split the string representation into individual fields.

```
fetch dt.entity.host



| expand tags, alias:tag_string



| parse tag_string, """(('['LD:tag_context ']' LD:tag_key (!<<'\\' ':') LD:tag_value)|(LD:tag_key (!<<'\\' ':') LD:tag_value)|LD:tag_key)"""
```

`entity.name`

`id`

`tag_string`

`tag_context`

`tag_key`

`tag_value`

HOST-1

HOST-73

Maxk:WebService2-ABC

undefined

Maxk:WebService2-ABC

undefined

HOST-1

HOST-73

testtests:testspreiser

undefined

testtests:testspreiser

undefined

HOST-1

HOST-73

Maxk:WebService3-ABC

undefined

Maxk:WebService3-ABC

undefined

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

`field`

`data_types`

belongs\_to

record

runs\_on

record

sends\_to

record

icon

record

receives\_from

record

instance\_of

record

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

`entity.name`

`id`

123

123

123

123

123

123

123

123

123

123

You can also obtain this result using native DQL with the following query.

```
fetch dt.entity.service



| fieldsAdd host.id = runs_on[dt.entity.host]



| expand host.id



| lookup sourceField:host.id, lookupField: id, fields:host.tags=tags, [ fetch dt.entity.host]



| expand host.tags



| filter host.tags == "[AWS]Category:ABC"
```

`entity.name`

`id`

`host.id`

`host.tags`

123

123

123

123

123

123

123

123

123

123

123

123

123

123

123

123

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

Relationship name

From > To

To > From

belongsTo

belongs\_to

contains

calls

calls

called\_by

candidateTalksWith

called\_by

calls

hostsComputeNode

hosts

hosted\_by

indirectlySendsToQueue

indirectly\_sends\_to

indirectly\_receives\_from

isAccessibleBy

accessible\_by

can\_access

isApplicationMethodOf

belongs\_to

contains

isApplicationMethodOfGroup

belongs\_to

contains

isApplicationOfSyntheticTest

monitored\_by

monitors

isAzrAppServicePlanOf

contains

belongs\_to

isAzrEventHubNamespaceOfEventHub

contains

belongs\_to

isAzrMgmtGroupOfAzrTenant

belongs\_to

contains

isAzrServiceBusNamespaceOfQueue

contains

belongs\_to

isAzrServiceBusNamespaceOfTopic

contains

belongs\_to

isAzrSQLDatabaseOfElasticPool

belongs\_to

contains

isAzrSqlServerOfDatabase

contains

belongs\_to

isAzrSqlServerOfElasticPool

belongs\_to

contains

isAzrStorageAccountOfAzrEventHub

contains

belongs\_to

isAzrSubscriptionOfAzrMgmtGroup

belongs\_to

contains

isAzrSubscriptionOfAzrTenant

belongs\_to

contains

isAzrSubscriptionOfCredentials

contains

belongs\_to

isBalancedBy

balanced\_by

balances

isBoshDeploymentOfHost

contains

belongs\_to

isCfFoundationOfHost

contains

belongs\_to

isCgiOfCa

belongs\_to

contains

isCgiOfCai

belongs\_to

contains

isCgiOfCluster

belongs\_to

contains

isCgiOfHost

belongs\_to

contains

isCgiOfNamespace

belongs\_to

contains

isChildOf

child\_of

parent\_of

isClusterOfCa

cluster\_of

clustered\_by

isClusterOfCai

cluster\_of

clustered\_by

isClusterOfCni

cluster\_of

clustered\_by

isClusterOfHost

cluster\_of

clustered\_by

isClusterOfKubernetesSvc

cluster\_of

clustered\_by

isClusterOfNamespace

cluster\_of

clustered\_by

isClusterOfNode

cluster\_of

isClusterOfPg

clustered\_by

cluster\_of

clustered\_by

isCnpOfCai

belongs\_to

contains

isDatastoreOf

belongs\_to

contains

isDeviceApplicationMethodOf

belongs\_to

contains

isDeviceApplicationMethodOfGroup

belongs\_to

contains

isDiskOf

belongs\_to

contains

isDockerContainerOf

contains

belongs\_to

isDockerContainerOfPg

contains

belongs\_to

isEbsVolumeOf

belongs\_to

contains

isGroupOf

group\_of

groups

isHostGroupOf

group\_of

groups

isHostOfContainer

hosts

hosted\_by

isInstanceOf

instance\_of

instantiates

isKubernetesSvcOfCa

balances

balanced\_by

isKubernetesSvcOfCai

balances

balanced\_by

isLocatedIn

belongs\_to

contains

isMainPgiOfCgi

belongs\_to

contains

isMemberOf

belongs\_to

contains

isMemberOfScalingGroup

belongs\_to

contains

isNamespaceOfCa

contains

belongs\_to

isNamespaceOfCai

contains

belongs\_to

isNamespaceOfCni

contains

belongs\_to

isNamespaceOfCnp

contains

belongs\_to

isNamespaceOfKubernetesSvc

contains

belongs\_to

isNamespaceOfPg

contains

belongs\_to

isNamespaceOfService

contains

belongs\_to

isNetworkClientOf

calls

called\_by

isNetworkClientOfHost

calls

called\_by

isNetworkClientOfProcessGroup

calls

called\_by

isNetworkInterfaceOf

belongs\_to

contains

isNodeOfHost

belongs\_to

contains

isOpenstackAvZoneOf

belongs\_to

contains

isPartOf

belongs\_to

contains

isPgAppOf

belongs\_to

contains

isPgiOfCgi

belongs\_to

contains

isPgOfCa

belongs\_to

contains

isPgOfCai

belongs\_to

contains

isPgOfCg

belongs\_to

contains

isProcessOf

belongs\_to

contains

isProcessRunningOpenstackVm

belongs\_to

contains

isRuntimeComponentOf

belongs\_to

contains

isSameAs

same\_as

same\_as

isServedByDcrumService

served\_by

serves

isServiceMethodOf

belongs\_to

contains

isServiceMethodOfService

belongs\_to

contains

isServiceOf

belongs\_to

contains

isServiceOfProcessGroup

belongs\_to

contains

isSiteOf

contains

belongs\_to

isSoftwareComponentOfPgi

belongs\_to

contains

isStepOf

belongs\_to

contains

isUserActionOf

belongs\_to

contains

listensOnQueue

belongs\_to

contains

manages

manages

managed\_by

monitors

monitors

monitored\_by

propagatesTo

propagates\_to

propagated\_from

receivesFromQueue

receives\_from

sends\_to

runsOn

runs\_on

runs

runsOnHost

runs\_on

runs

runsOnProcessGroupInstance

runs\_on

runs

runsOnResource

runs\_on

runs

sendsToQueue

sends\_to

receives\_from

talksWithCandidate

calls

called\_by

affects

affects

affected\_by

isRelatedTo

related\_to

related\_to

## Troubleshooting

* **The DQL query returns different or fewer entities than API v2 environment**
  Verify that you are using the same query timeframe `fetch dt.entity.*`. The `classicEntitySelector()` function only returns entities that have a lifetime that overlaps with the query timeframe. By default, DQL queries are executed for the last 2 hours, whereas the default timeframe in the API environment is 72 hours.

## Related topics



* [What is Dynatrace Grail?](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more.")
* [DQL commands](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.")
* [IAM policy reference](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.")
* [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.")
* [Environment API v2 - Entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.")