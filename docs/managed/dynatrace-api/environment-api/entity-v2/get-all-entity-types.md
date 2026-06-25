---
title: Monitored entities API - GET all entity types
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/entity-v2/get-all-entity-types
scraped: 2026-05-12T11:57:10.598292
---

# Monitored entities API - GET all entity types

# Monitored entities API - GET all entity types

* Reference
* Published Apr 24, 2020

Lists all types of monitored entities observed in your environment.

Additionally, every entity type lists the possible properties of an entity of that type. Note that these are placeholders showing what properties an entity can possibly have, not actual properties. To view actual properties of an entity, use the [GET an entity](/managed/dynatrace-api/environment-api/entity-v2/get-entity "View parameters of a monitored entity via Dynatrace API.") request.

You can limit the output by using the pagination:

1. Specify the number of results per page in the **pageSize** query parameter.
2. Then use the cursor from the **nextPageKey** field of the previous response in the **nextPageKey** query parameter to obtain subsequent pages.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/entityTypes` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/entityTypes` |

## Authentication

To execute this request, you need an access token with `entities.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **nextPageKey** field of the previous response.  The first page is always returned if you don't specify the **nextPageKey** query parameter.  When the **nextPageKey** is set to obtain subsequent pages, you must omit all other query parameters. | query | Optional |
| pageSize | integer | The amount of entity types in a single response payload.  The maximal allowed page size is 500.  If not set, 50 is used. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [EntityTypeList](#openapi-definition-EntityTypeList) | Success |
| **400** | - | Failed. There are no more entity types to export. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `EntityTypeList` object

A list of properties of all available entity types.

| Element | Type | Description |
| --- | --- | --- |
| nextPageKey | string | The cursor for the next page of results. Has the value of `null` on the last page.  Use it in the **nextPageKey** query parameter to obtain subsequent pages of the result. |
| pageSize | integer | The number of entries per page. |
| totalCount | integer | The total number of entries in the result. |
| types | [EntityType[]](#openapi-definition-EntityType) | The list of meta information for all available entity-types |

#### The `EntityType` object

A list of properties of the monitored entity type.

| Element | Type | Description |
| --- | --- | --- |
| dimensionKey | string | The dimension key used within metrics for this monitored entity. |
| displayName | string | The display name of the monitored entity. |
| entityLimitExceeded | boolean | Indicates whether the entity creation limit for this type has been exceeded. When true, Dynatrace automatically triggers a cleanup process for this entity type. New entities will still be created, and no action is required. This applies only for builtin-types. For generic types creation and update gets blocked. You can recognize a generic type by containing ':' in the name for example my:type. |
| fromRelationships | [ToPosition[]](#openapi-definition-ToPosition) | A list of possible relationships where the monitored entity type occupies the FROM position |
| managementZones | string | The placeholder for the list of management zones of an actual entity. |
| properties | [EntityTypePropertyDto[]](#openapi-definition-EntityTypePropertyDto) | A list of additional properties of the monitored entity type. |
| tags | string | The placeholder for the list of tags of an actual entity. |
| toRelationships | [FromPosition[]](#openapi-definition-FromPosition) | A list of possible relationships where the monitored entity type occupies the TO position. |
| type | string | The type of the monitored entity. |

#### The `ToPosition` object

The TO position of a relationship.

| Element | Type | Description |
| --- | --- | --- |
| id | string | The ID of the relationship. |
| toTypes | string[] | A list of monitored entity types that can occupy the TO position. |

#### The `EntityTypePropertyDto` object

The property of a monitored entity.

| Element | Type | Description |
| --- | --- | --- |
| displayName | string | The display-name of the property. |
| id | string | The ID of the property. |
| type | string | The type of the property. |

#### The `FromPosition` object

The FROM position of a relationship.

| Element | Type | Description |
| --- | --- | --- |
| fromTypes | string[] | A list of monitored entity types that can occupy the FROM position. |
| id | string | The ID of the relationship. |

### Response body JSON models

```
{



"nextPageKey": "AQAAABQBAAAABQ==",



"pageSize": 1,



"totalCount": 1,



"types": [



{



"entityLimitExceeded": "false",



"fromRelationships": [



{



"id": "RUNS_ON_RESOURCE",



"toTypes": [



"CUSTOM_DEVICE"



]



},



{



"id": "IS_NETWORK_CLIENT_OF_HOST",



"toTypes": [



"HOST",



"CUSTOM_DEVICE"



]



}



],



"managementZones": "placeholder for management zones",



"properties": [



{



"id": "BITNESS",



"type": "Enum"



},



{



"id": "CPU_CORES",



"type": "Number"



}



],



"tags": "placeholder for tags",



"toRelationships": [



{



"fromTypes": [



"DISK"



],



"id": "IS_DISK_OF"



},



{



"fromTypes": [



"VMWARE_DATACENTER",



"GEOLOC_SITE"



],



"id": "IS_SITE_OF"



}



],



"type": "HOST"



}



]



}
```

## Example

In this example, the request lists all entity types observed in the **mySampleEnv** environment.

The API token is passed in the **Authorization** header.

Because the full result is rather lengthy, it is truncated to three entries. Subsequently, the **properties** array of each entity is also truncated to three entries.

#### Curl

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/entityTypes' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/entityTypes
```

#### Response body

```
{



"totalCount": 33,



"pageSize": 33,



"types": [



{



"type": "APPLICATION",



"properties": [



{



"id": "applicationType",



"type": "Enum"



},



{



"id": "conditionalName",



"type": "String"



},



{



"id": "customizedName",



"type": "String"



}



],



"tags": "List",



"managementZones": "List",



"fromRelationships": [



{



"id": "calls",



"toTypes": [



"SERVICE"



]



}



],



"toRelationships": []



},



{



"type": "HOST",



"properties": [



{



"id": "ipAddresses",



"type": "List"



},



{



"id": "osType",



"type": "Enum"



},



{



"id": "osVersion",



"type": "String"



}



],



"tags": "List",



"managementZones": "List",



"fromRelationships": [



{



"id": "runsOn",



"toTypes": [



"EC2_INSTANCE",



"VIRTUALMACHINE",



"AZURE_VM",



"OPENSTACK_VM",



"GOOGLE_COMPUTE_ENGINE",



"HYPERVISOR"



]



},



{



"id": "runsOnResource",



"toTypes": [



"CUSTOM_DEVICE"



]



},



{



"id": "isInstanceOf",



"toTypes": [



"HOST_GROUP"



]



},



{



"id": "isNetworkClientOfHost",



"toTypes": [



"HOST",



"CUSTOM_DEVICE"



]



},



{



"id": "candidateTalksWith",



"toTypes": [



"CUSTOM_DEVICE",



"PROCESS_GROUP_INSTANCE"



]



}



],



"toRelationships": [



{



"id": "isProcessOf",



"fromTypes": [



"PROCESS_GROUP_INSTANCE"



]



},



{



"id": "runsOn",



"fromTypes": [



"OPENSTACK_VM",



"PROCESS_GROUP"



]



},



{



"id": "isSiteOf",



"fromTypes": [



"GEOLOC_SITE",



"VMWARE_DATACENTER"



]



},



{



"id": "talksWithCandidate",



"fromTypes": [



"CUSTOM_DEVICE",



"PROCESS_GROUP_INSTANCE"



]



},



{



"id": "isNetworkClientOfHost",



"fromTypes": [



"CUSTOM_DEVICE",



"HOST"



]



},



{



"id": "isDiskOf",



"fromTypes": [



"DISK"



]



},



{



"id": "runsOnHost",



"fromTypes": [



"SERVICE"



]



},



{



"id": "isContainerGroupInstanceOfHost",



"fromTypes": [



"CONTAINER_GROUP_INSTANCE"



]



}



]



},



{



"type": "SERVICE",



"properties": [



{



"id": "mainServiceSoftwareTech",



"type": "Map"



},



{



"id": "port",



"type": "Number"



},



{



"id": "serviceType",



"type": "Enum"



}



],



"tags": "List",



"managementZones": "List",



"fromRelationships": [



{



"id": "runsOn",



"toTypes": [



"CUSTOM_DEVICE_GROUP",



"PROCESS_GROUP"



]



},



{



"id": "runsOnProcessGroupInstance",



"toTypes": [



"CUSTOM_DEVICE",



"PROCESS_GROUP_INSTANCE"



]



},



{



"id": "runsOnHost",



"toTypes": [



"CUSTOM_DEVICE",



"HOST"



]



},



{



"id": "calls",



"toTypes": [



"SERVICE"



]



}



],



"toRelationships": [



{



"id": "calls",



"fromTypes": [



"MOBILE_APPLICATION",



"CUSTOM_APPLICATION",



"HTTP_CHECK",



"APPLICATION",



"SERVICE"



]



}



]



}



]



}
```

#### Response code

200

## Related topics

* [Custom tags API](/managed/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.")