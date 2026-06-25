---
title: Monitored entities API - GET entities list
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/entity-v2/get-entities-list
scraped: 2026-05-12T11:57:12.938417
---

# Monitored entities API - GET entities list

# Monitored entities API - GET entities list

* Reference
* Published May 28, 2020

Lists entities observed within the specified timeframe along with their properties. When you query entities of the `SERVICE_METHOD` type, only the following requests are returned:

* [Key requests](/managed/observe/application-observability/services-classic/monitor-key-requests "Discover how to closely monitor requests that are critical to your business.").
* Top X requests that are used for [baselining](/managed/dynatrace-intelligence/anomaly-detection/automated-multidimensional-baselining "Learn how Dynatrace AI automatically calculates baselines based on a multi-dimensional baselining scheme.").
* Requests that have caused a [problem](/managed/dynatrace-intelligence "Get familiar with the capabilities of Davis AI.").

You can limit the output by using the pagination:

1. Specify the number of results per page in the **pageSize** query parameter.
2. Then use the cursor from the **nextPageKey** field of the previous response in the **nextPageKey** query parameter to obtain subsequent pages.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/entities` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/entities` |

## Authentication

To execute this request, you need an access token with `entities.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **nextPageKey** field of the previous response.  The first page is always returned if you don't specify the **nextPageKey** query parameter.  When the **nextPageKey** is set to obtain subsequent pages, you must omit all other query parameters. | query | Optional |
| pageSize | integer | The amount of entities.  If not set, 50 is used. | query | Optional |
| entitySelector | string | Defines the scope of the query. Only entities matching the specified criteria are included into response.  You must set one of these criteria:  * Entity type: `type("TYPE")` * Dynatrace entity ID: `entityId("id")`. You can specify several IDs, separated by a comma (`entityId("id-1","id-2")`). All requested entities must be of the same type.  You can add one or more of the following criteria. Values are case-sensitive and the `EQUALS` operator is used unless otherwise specified.  * Tag: `tag("value")`. Tags in `[context]key:value`, `key:value`, and `value` formats are detected and parsed automatically. Any colons (`:`) that are part of the key or value must be escaped with a backslash(`\`). Otherwise, it will be interpreted as the separator between the key and the value. All tag values are case-sensitive. * Management zone ID: `mzId(123)` * Management zone name: `mzName("value")` * Entity name: + `entityName.equals`: performs a non-casesensitive `EQUALS` query.   + `entityName.startsWith`: changes the operator to `BEGINS WITH`.   + `entityName.in`: enables you to provide multiple values. The `EQUALS` operator applies.   + `caseSensitive(entityName.equals("value"))`: takes any entity name criterion as an argument and makes the value case-sensitive. * Health state (HEALTHY,UNHEALTHY): `healthState("HEALTHY")` * First seen timestamp: `firstSeenTms.<operator>(now-3h)`. Use any timestamp format from the **from**/**to** parameters.   The following operators are available: + `lte`: earlier than or at the specified time   + `lt`: earlier than the specified time   + `gte`: later than or at the specified time   + `gt`: later than the specified time * Entity attribute: `<attribute>("value1","value2")` and `<attribute>.exists()`. To fetch the list of available attributes, execute the [GET entity typeï»¿](https://dt-url.net/2ka3ivt) request and check the **properties** field of the response. * Relationships: `fromRelationships.<relationshipName>()` and `toRelationships.<relationshipName>()`. This criterion takes an entity selector as an attribute. To fetch the list of available relationships, execute the [GET entity typeï»¿](https://dt-url.net/2ka3ivt) request and check the **fromRelationships** and **toRelationships** fields. * Negation: `not(<criterion>)`. Inverts any criterion except for **type**.  For more information, see [Entity selectorï»¿](https://dt-url.net/apientityselector) in Dynatrace Documentation.  To set several criteria, separate them with a comma (`,`). For example, `type("HOST"),healthState("HEALTHY")`. Only results matching **all** criteria are included in the response.  The maximum string length is 2,000 characters.  The field is **required** when you're querying the first page of results. | query | Optional |
| from | string | The start of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the relative timeframe of three days is used (`now-3d`). | query | Optional |
| to | string | The end of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the current timestamp is used. | query | Optional |
| fields | string | Defines the list of entity properties included in the response. The ID and the name of an entity are **always** included to the response.  To add properties, list them with leading plus `+`. You can specify several properties, separated by a comma (for example `fields=+lastSeenTms,+properties.BITNESS`).  Use the [GET entity typeï»¿](https://dt-url.net/2ka3ivt) request to fetch the list of properties available for your entity type. Fields from the **properties** object must be specified in the `properties.FIELD` format (for example, `properties.BITNESS`).  When requesting large amounts of relationship fields, throttling can apply. | query | Optional |
| sort | string | Defines the ordering of the entities returned.  This field is **optional**, each field has a sign prefix (+/-), which corresponds to sorting order ( + for ascending and - for descending). If no sign prefix is set, then default ascending sorting order will be applied.  Currently ordering is only available for the display name (for example `sort=name or sort =+name for ascending, sort=-name for descending`) | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [EntitiesList](#openapi-definition-EntitiesList) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `EntitiesList` object

A list of monitored entities along with their properties.

| Element | Type | Description |
| --- | --- | --- |
| entities | [Entity[]](#openapi-definition-Entity) | A list of monitored entities. |
| nextPageKey | string | The cursor for the next page of results. Has the value of `null` on the last page.  Use it in the **nextPageKey** query parameter to obtain subsequent pages of the result. |
| pageSize | integer | The number of entries per page. |
| totalCount | integer | The total number of entries in the result. |

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
| managementZones | [EnrichedManagementZoneDto[]](#openapi-definition-EnrichedManagementZoneDto) | A set of management zones to which the entity belongs. |
| properties | object | A list of additional properties of the entity. |
| tags | [EnrichedTagDto[]](#openapi-definition-EnrichedTagDto) | A set of tags assigned to the entity. |
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
| customIconPath | string | The user-defined icon of the entity.  Specify the [baristaï»¿](https://dt-url.net/u403suy) ID of the icon or a URL of your own icon. |
| primaryIconType | string | The primary icon of the entity.  Specified by the [baristaï»¿](https://dt-url.net/u403suy) ID of the icon. |
| secondaryIconType | string | The secondary icon of the entity.  Specified by the [baristaï»¿](https://dt-url.net/u403suy) ID of the icon. |

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
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | A list of constraint violations |
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



"entities": [



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



],



"nextPageKey": "AQAAABQBAAAABQ==",



"pageSize": 1,



"totalCount": 1



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

In this example, the request list services that belong to the management zones with the ID of **229130632296508575249**. To achieve that, the **entitySelector** query parameter is set to `type("SERVICE"),mzId("229130632296508575249")`.

Apart from default Dynatrace entity IDs and names of the entities, the request also returns the timestamp of when the service was last seen and the list of technology types that run in the service. To achieve that, the **fields** query parameter is set to `lastSeenTms,properties.serviceTechnologyTypes`.

The API token is passed in the **Authorization** header.

The result is truncated to three entries.

#### Curl

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/entities?entitySelector=type(%22SERVICE%22),mzId(%229130632296508575249%22)&fields=lastSeenTms,properties.serviceTechnologyTypes' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/entities?entitySelector=type(%22SERVICE%22),mzId(%229130632296508575249%22)&fields=lastSeenTms,properties.serviceTechnologyTypes
```

#### Response body

```
{



"totalCount": 52,



"pageSize": 50,



"nextPageKey": "AQArdHlwZSgiU0VSVklDRSIpL",



"entities": [



{



"entityId": "SERVICE-1125C375A187D27A",



"displayName": "dotNetBackend_easyTravel_x64",



"lastSeenTms": 1590609632865,



"properties": {



"serviceTechnologyTypes": [



"IIS app pool",



"ASP.NET",



"DotNet"



]



}



},



{



"entityId": "SERVICE-42C0B06C4DCFD0EF",



"displayName": "AuthenticationService",



"lastSeenTms": 1590747000977,



"properties": {



"serviceTechnologyTypes": [



"Java"



]



}



},



{



"entityId": "SERVICE-620517BB99A7ED9E",



"displayName": "BookingService",



"lastSeenTms": 1590747028702,



"properties": {



"serviceTechnologyTypes": [



"Java"



]



}



}



]



}
```

#### Response code

200

## Related topics

* [Custom tags API](/managed/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.")