---
title: Custom tags API - POST tags
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/custom-tags/post-tags
---

# Custom tags API - POST tags

# Custom tags API - POST tags

* Reference
* Published May 29, 2020

Add custom tags to the specified monitored entities.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/tags` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/tags` |

## Authentication

To execute this request, you need an access token with `entities.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| entitySelector | string | Specifies the entities where you want to update tags.  You must set one of these criteria:  * Entity type: `type("TYPE")` * Dynatrace entity ID: `entityId("id")`. You can specify several IDs, separated by a comma (`entityId("id-1","id-2")`). All requested entities must be of the same type.  You can add one or more of the following criteria. Values are case-sensitive and the `EQUALS` operator is used unless otherwise specified.  * Tag: `tag("value")`. Tags in `[context]key:value`, `key:value`, and `value` formats are detected and parsed automatically. Any colons (`:`) that are part of the key or value must be escaped with a backslash(`\`). Otherwise, it will be interpreted as the separator between the key and the value. All tag values are case-sensitive. * Management zone ID: `mzId(123)` * Management zone name: `mzName("value")` * Entity name: + `entityName.equals`: performs a non-casesensitive `EQUALS` query.   + `entityName.startsWith`: changes the operator to `BEGINS WITH`.   + `entityName.in`: enables you to provide multiple values. The `EQUALS` operator applies.   + `caseSensitive(entityName.equals("value"))`: takes any entity name criterion as an argument and makes the value case-sensitive. * Health state (HEALTHY,UNHEALTHY): `healthState("HEALTHY")` * First seen timestamp: `firstSeenTms.<operator>(now-3h)`. Use any timestamp format from the **from**/**to** parameters.   The following operators are available: + `lte`: earlier than or at the specified time   + `lt`: earlier than the specified time   + `gte`: later than or at the specified time   + `gt`: later than the specified time * Entity attribute: `<attribute>("value1","value2")` and `<attribute>.exists()`. To fetch the list of available attributes, execute the [GET entity type﻿](https://dt-url.net/2ka3ivt) request and check the **properties** field of the response. * Relationships: `fromRelationships.<relationshipName>()` and `toRelationships.<relationshipName>()`. This criterion takes an entity selector as an attribute. To fetch the list of available relationships, execute the [GET entity type﻿](https://dt-url.net/2ka3ivt) request and check the **fromRelationships** and **toRelationships** fields. * Negation: `not(<criterion>)`. Inverts any criterion except for **type**.  For more information, see [Entity selector﻿](https://dt-url.net/apientityselector) in Dynatrace Documentation.  To set several criteria, separate them with a comma (`,`). For example, `type("HOST"),healthState("HEALTHY")`. Only results matching **all** criteria are included in the response.  The maximum string length is 2,000 characters. | query | Required |
| from | string | The start of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the relative timeframe of 24 hours is used (`now-24h`). | query | Optional |
| to | string | The end of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the current timestamp is used. | query | Optional |
| body | [AddEntityTags](#openapi-definition-AddEntityTags) | The JSON body of the request. Contains tags to be added to the matching entities. | body | Optional |

### Request body objects

#### The `AddEntityTags` object

A list of tags to be added to monitored entities.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| tags | [AddEntityTag](#openapi-definition-AddEntityTag)[] | A list of tags to be added to monitored entities. | Required |

#### The `AddEntityTag` object

The custom tag to be added to monitored entities.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| key | string | The key of the custom tag to be added to monitored entities. | Required |
| value | string | The value of the custom tag to be added to monitored entities. May be null | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"tags": [



{



"key": "mainApp"



},



{



"key": "bookings",



"value": "42"



}



]



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [AddedEntityTags](#openapi-definition-AddedEntityTags) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `AddedEntityTags` object

A list of custom tags added to monitored entities.

| Element | Type | Description |
| --- | --- | --- |
| appliedTags | [METag](#openapi-definition-METag)[] | A list of added custom tags. |
| matchedEntitiesCount | integer | The number of monitored entities where the tags have been added. |

#### The `METag` object

The tag of a monitored entity.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. |
| key | string | The key of the tag. |
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



"appliedTags": [



{



"context": "CONTEXTLESS",



"key": "mainApp",



"stringRepresentation": "mainApp"



},



{



"context": "CONTEXTLESS",



"key": "booking",



"stringRepresentation": "booking"



}



],



"matchedEntitiesCount": 2



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

In this example, the request adds the **REST-test** and **RESTexample** custom tags to hosts that already have the **easyTravel** tag. To achieve that, the **entitySelector** query parameter is set to `type("HOST"),tag("easyTravel")`.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -L -X POST 'https://mySampleEnv.live.dynatrace.com/api/v2/tags?entitySelector=type(%22HOST%22),tag(%22easyTravel%22)' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



--data-raw '{



"tags": [



{



"key": "REST-test"



},



{



"key": "RESTexample"



}



]



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/tags?entitySelector=type(%22HOST%22),tag(%22easyTravel%22)
```

#### Request body

```
{



"tags": [



{



"key": "REST-test"



},



{



"key": "RESTexample"



}



]



}
```

#### Response body

```
{



"matchedEntitiesCount": 3,



"appliedTags": [



{



"context": "CONTEXTLESS",



"key": "REST-test",



"stringRepresentation": "REST-test"



},



{



"context": "CONTEXTLESS",



"key": "RESTexample",



"stringRepresentation": "RESTexample"



}



]



}
```

#### Response code

200

## Related topics

* [Monitored entities API](/managed/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.")