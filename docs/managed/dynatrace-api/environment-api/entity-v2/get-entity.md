---
title: Monitored entities API - GET an entity
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/entity-v2/get-entity
---

# Monitored entities API - GET an entity

# Monitored entities API - GET an entity

* Reference
* Published May 28, 2020

Gets the full list of properties of the specified entity. The actual list depends on the entity type.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/entities/{entityId}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/entities/{entityId}` |

## Authentication

To execute this request, you need an access token with `entities.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| entityId | string | The ID of the required entity. | path | Required |
| from | string | The start of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the relative timeframe of three days is used (`now-3d`). | query | Optional |
| to | string | The end of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the current timestamp is used. | query | Optional |
| fields | string | Defines the list of entity properties included in the response. The ID and the name of an entity are **always** included to the response.  To add properties, list them with leading plus `+`. You can specify several properties, separated by a comma (for example `fields=+lastSeenTms,+properties.BITNESS`).  Use the [GET entity type﻿](https://dt-url.net/2ka3ivt?dt=m) request to fetch the list of properties available for your entity type. Fields from the **properties** object must be specified in the `properties.FIELD` format (for example, `properties.BITNESS`).  When requesting large amounts of relationship fields, throttling can apply. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [Entity](#openapi-definition-Entity) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `Entity` object

The properties of a monitored entity.

| Element | Type | Description |
| --- | --- | --- |
| displayName | string | The name of the entity, displayed in the UI. |
| entityId | string | The ID of the entity. |
| firstSeenTms | integer | The timestamp at which the entity was first seen, in UTC milliseconds. |
| fromRelationships | object | A list of relationships where the entity occupies the FROM position. |
| icon | [EntityIcon](#openapi-definition-EntityIcon) | The icon of a monitored entity. |
| lastSeenTms | integer | The timestamp at which the entity was last seen, in UTC milliseconds. |
| managementZones | [EnrichedManagementZoneDto](#openapi-definition-EnrichedManagementZoneDto)[] | A set of management zones to which the entity belongs. |
| properties | object | A list of additional properties of the entity. |
| tags | [EnrichedTagDto](#openapi-definition-EnrichedTagDto)[] | A set of tags assigned to the entity. |
| toRelationships | object | A list of relationships where the entity occupies the TO position. |
| type | string | The type of the entity. |

#### The `EntityId` object

A short representation of a monitored entity.

| Element | Type | Description |
| --- | --- | --- |
| id | string | The ID of the entity. |
| type | string | The type of the entity. |

#### The `EntityIcon` object

The icon of a monitored entity.

| Element | Type | Description |
| --- | --- | --- |
| customIconPath | string | The user-defined icon of the entity.  Specify the [barista﻿](https://dt-url.net/u403suy?dt=m) ID of the icon or a URL of your own icon. |
| primaryIconType | string | The primary icon of the entity.  Specified by the [barista﻿](https://dt-url.net/u403suy?dt=m) ID of the icon. |
| secondaryIconType | string | The secondary icon of the entity.  Specified by the [barista﻿](https://dt-url.net/u403suy?dt=m) ID of the icon. |

#### The `EnrichedManagementZoneDto` object

| Element | Type | Description |
| --- | --- | --- |
| id | string | The ID of the management zone. |
| name | string | The name of the management zone. |
| sourceSetting | string | The path to the settings object in the Settings API. |

#### The `EnrichedTagDto` object

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. |
| key | string | The key of the tag. |
| source | string | The source where the tag comes from. Possible values are:  * Auto tags * Environment tags * User provided tags |
| sourceSetting | string | The path to the settings object in the Settings API. Only available for tags with the Auto tags source. |
| stringRepresentation | string | The string representation of the tag. |
| value | string | The value of the tag. |

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | A list of constraint violations |
| message | string | The error message |

#### The `ConstraintViolation` object

A list of constraint violations

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -The element can hold these values * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Response body JSON models

```
{



"displayName": "my host",



"entityId": "HOST-06F288EE2A930951",



"firstSeenTms": 1574697667547,



"fromRelationships": {



"isInstanceOf": [



{



"id": "HOST_GROUP-0E489369D663A4BF",



"type": "HOST_GROUP"



}



]



},



"icon": {



"customIconPath": "host",



"primaryIconType": "linux",



"secondaryIconType": "microsoft-azure-signet"



},



"lastSeenTms": 1588242361417,



"managementZones": [



{



"id": "6239538939987181652",



"name": "main app"



}



],



"properties": {



"bitness": 64,



"cpuCores": 8,



"monitoringMode": "FULL_STACK",



"networkZoneId": "aws.us.east01",



"osArchitecture": "X86",



"osType": "LINUX"



},



"tags": [



{



"context": "CONTEXTLESS",



"key": "architecture",



"stringRepresentation": "architecture:x86",



"value": "x86"



},



{



"context": "ENVIRONMENT",



"key": "Infrastructure",



"stringRepresentation": "[ENVIRONMENT]Infrastructure:Linux",



"value": "Linux"



}



],



"toRelationships": {



"isDiskOf": [



{



"id": "DISK-0393340DCA3853B0",



"type": "DISK"



}



]



},



"type": "HOST"



}
```

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Example

In this example, the request lists the properties of the **dotNetBackend\_easyTravel\_x64** service, which has the ID of **SERVICE-1125C375A187D27A**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/entities/SERVICE-1125C375A187D27A' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/entities/SERVICE-1125C375A187D27A
```

#### Response body

```
{



"entityId": "SERVICE-1125C375A187D27A",



"displayName": "dotNetBackend_easyTravel_x64",



"firstSeenTms": 1424310498896,



"lastSeenTms": 1590609632865,



"properties": {



"serviceType": "WEB_REQUEST_SERVICE",



"internalName": "dotNetBackend_easyTravel_x64",



"webServerName": "dotNetBackend_easyTravel_x64",



"softwareTechnologies": [



{



"edition": "FullCLR",



"version": "2.0.50727"



},



{



"type": "DOTNET",



"edition": ".NET Framework",



"version": "3.5.1.0"



},



{



"type": "ADO_NET",



"edition": "System.Data",



"version": "2.0.50727.8751"



},



{



"type": "ASP_DOTNET",



"version": "3.5.1.0"



},



{



"type": "IIS_APP_POOL",



"version": "10.0.14393.0"



},



{



"type": "DOTNET_REMOTING",



"version": "2.0.50727.8771"



}



],



"serviceTechnologyTypes": [



"IIS app pool",



"ASP.NET",



"DotNet"



],



"mainServiceSoftwareTech": {



"type": "ASP_DOTNET"



},



"contextRoot": "/",



"agentTechnologyType": "DOTNET"



},



"tags": [



{



"context": "CONTEXTLESS",



"key": "customService",



"stringRepresentation": "customService"



},



{



"context": "CONTEXTLESS",



"key": "easytravel",



"value": "backend",



"stringRepresentation": "easytravel:backend",



"source": "Auto tags",



"sourceSetting": "api/v2/settings/objects/vu9U3hXa3q0AAAABABlidWlsdGluOnRhZ3MuYXV0by10YWdnaW5nAAZ0ZW5hbnQABnRlbmFudAAkNGQ5YTFhMTUtZmY1ZS0zNDE5LWE2MDUtOTlmOWJkZTFhODNmvu9U3hXa3q0"



}



],



"mangementZones": [



{



"id": "2827032493241090264",



"name": "allServices"



},



{



"id": "9130632296508575249",



"name": "Easytravel",



"sourceSetting": "api/v2/settings/objects/vu9U3hXa3q0AAAABABhidWlsdGluOm1hbmFnZW1lbnQtem9uZXMABnRlbmFudAAGdGVuYW50ACQ1MTNkNWNkMC0zZjEyLTNiOTUtODZlMi05YjU4ODk0ODM4MWO-71TeFdrerQ"



}



],



"fromRelationships": {



"calls": [



{



"id": "SERVICE-775060208AAA1058",



"type": "SERVICE"



},



{



"id": "SERVICE-6737CDED8F9BF969",



"type": "SERVICE"



}



],



"runsOn": [



{



"id": "PROCESS_GROUP-0A9A52EA262BC039",



"type": "PROCESS_GROUP"



}



],



"runsOnHost": [



{



"id": "HOST-B64B6B9CB11E2244",



"type": "HOST"



},



{



"id": "HOST-CF61BC45E6282234",



"type": "HOST"



}



],



"runsOnProcessGroupInstance": [



{



"id": "PROCESS_GROUP_INSTANCE-DE765F657721AF59",



"type": "PROCESS_GROUP_INSTANCE"



}



]



},



"toRelationships": {



"calls": [



{



"id": "SERVICE-D20E300A0A6814EF",



"type": "SERVICE"



},



{



"id": "SERVICE-7675DAA7464128F8",



"type": "SERVICE"



}



]



}



}
```

#### Response code

200

## Related topics

* [Custom tags API](/managed/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.")