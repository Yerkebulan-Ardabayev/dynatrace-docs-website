---
title: Monitored entities API - GET entity type
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/entity-v2/get-entity-type
---

# Monitored entities API - GET entity type

# Monitored entities API - GET entity type

* Reference
* Published Apr 24, 2020

Lists possible properties of an entity of the specified type. Note that these are placeholders showing what properties an entity can possibly have, not actual properties. To view actual properties of an entity, use the [GET an entity](/managed/dynatrace-api/environment-api/entity-v2/get-entity "View parameters of a monitored entity via Dynatrace API.") request.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/entityTypes/{type}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/entityTypes/{type}` |

## Authentication

To execute this request, you need an access token with `entities.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| type | string | The required entity type. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [EntityType](#openapi-definition-EntityType) | Success |
| **400** | - | Failed. The requested monitored entity type is not exportable or doesn't exist. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `EntityType` object

A list of properties of the monitored entity type.

| Element | Type | Description |
| --- | --- | --- |
| dimensionKey | string | The dimension key used within metrics for this monitored entity. |
| displayName | string | The display name of the monitored entity. |
| entityLimitExceeded | boolean | Indicates whether the entity creation limit for this type has been exceeded. When true, Dynatrace automatically triggers a cleanup process for this entity type. New entities will still be created, and no action is required. This applies only for builtin-types. For generic types creation and update gets blocked. You can recognize a generic type by containing ':' in the name for example my:type. |
| fromRelationships | [ToPosition](#openapi-definition-ToPosition)[] | A list of possible relationships where the monitored entity type occupies the FROM position |
| managementZones | string | The placeholder for the list of management zones of an actual entity. |
| properties | [EntityTypePropertyDto](#openapi-definition-EntityTypePropertyDto)[] | A list of additional properties of the monitored entity type. |
| tags | string | The placeholder for the list of tags of an actual entity. |
| toRelationships | [FromPosition](#openapi-definition-FromPosition)[] | A list of possible relationships where the monitored entity type occupies the TO position. |
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
```

## Example

In this example, the request lists all possible properties of entities of the **PROCESS\_GROUP\_INSTANCE** type.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/entityTypes/PROCESS_GROUP_INSTANCE' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/entityTypes/PROCESS_GROUP_INSTANCE
```

#### Response body

```
{



"type": "PROCESS_GROUP_INSTANCE",



"properties": [



{



"id": "appVersion",



"type": "String"



},



{



"id": "awsNameTag",



"type": "String"



},



{



"id": "azureHostName",



"type": "String"



},



{



"id": "azureSiteName",



"type": "String"



},



{



"id": "bitness",



"type": "Enum"



},



{



"id": "boshName",



"type": "String"



},



{



"id": "conditionalName",



"type": "String"



},



{



"id": "customPgMetadata",



"type": "Map"



},



{



"id": "customizedName",



"type": "String"



},



{



"id": "gardenApplicationNames",



"type": "List"



},



{



"id": "gcpZone",



"type": "String"



},



{



"id": "internalName",



"type": "String"



},



{



"id": "isDockerized",



"type": "Boolean"



},



{



"id": "jvmClrVersion",



"type": "String"



},



{



"id": "jvmVendor",



"type": "String"



},



{



"id": "listenPorts",



"type": "List"



},



{



"id": "metadata",



"type": "List"



},



{



"id": "modules",



"type": "List"



},



{



"id": "oneAgentCustomHostName",



"type": "String"



},



{



"id": "processType",



"type": "Enum"



},



{



"id": "softwareTechnologies",



"type": "List"



},



{



"id": "versionedModules",



"type": "List"



}



],



"tags": "List",



"managementZones": "List",



"fromRelationships": [



{



"id": "isProcessOf",



"toTypes": [



"HOST"



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



"PROCESS_GROUP"



]



},



{



"id": "talksWithCandidate",



"toTypes": [



"HOST"



]



},



{



"id": "isNetworkClientOf",



"toTypes": [



"CUSTOM_DEVICE",



"PROCESS_GROUP_INSTANCE"



]



}



],



"toRelationships": [



{



"id": "runsOnProcessGroupInstance",



"fromTypes": [



"SERVICE"



]



},



{



"id": "isHostGroupOf",



"fromTypes": [



"HOST_GROUP"



]



},



{



"id": "isNetworkClientOf",



"fromTypes": [



"CUSTOM_DEVICE",



"PROCESS_GROUP_INSTANCE"



]



},



{



"id": "candidateTalksWith",



"fromTypes": [



"HOST"



]



}



]



}
```

#### Response code

200

## Related topics

* [Custom tags API](/managed/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.")