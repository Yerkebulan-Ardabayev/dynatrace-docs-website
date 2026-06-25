---
title: Custom tags API - GET tags
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/custom-tags/get-tags
scraped: 2026-05-12T11:58:01.434499
---

# Custom tags API - GET tags

# Custom tags API - GET tags

* Reference
* Published May 29, 2020

Lists all custom tags assigned to the specified monitored entities. Automatically applied tags and imported tags are not included.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/tags` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/tags` |

## Authentication

To execute this request, you need an access token with `entities.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| entitySelector | string | Specifies the entities where you want to read tags.  You must set one of these criteria:  * Entity type: `type("TYPE")` * Dynatrace entity ID: `entityId("id")`. You can specify several IDs, separated by a comma (`entityId("id-1","id-2")`). All requested entities must be of the same type.  You can add one or more of the following criteria. Values are case-sensitive and the `EQUALS` operator is used unless otherwise specified.  * Tag: `tag("value")`. Tags in `[context]key:value`, `key:value`, and `value` formats are detected and parsed automatically. Any colons (`:`) that are part of the key or value must be escaped with a backslash(`\`). Otherwise, it will be interpreted as the separator between the key and the value. All tag values are case-sensitive. * Management zone ID: `mzId(123)` * Management zone name: `mzName("value")` * Entity name: + `entityName.equals`: performs a non-casesensitive `EQUALS` query.   + `entityName.startsWith`: changes the operator to `BEGINS WITH`.   + `entityName.in`: enables you to provide multiple values. The `EQUALS` operator applies.   + `caseSensitive(entityName.equals("value"))`: takes any entity name criterion as an argument and makes the value case-sensitive. * Health state (HEALTHY,UNHEALTHY): `healthState("HEALTHY")` * First seen timestamp: `firstSeenTms.<operator>(now-3h)`. Use any timestamp format from the **from**/**to** parameters.   The following operators are available: + `lte`: earlier than or at the specified time   + `lt`: earlier than the specified time   + `gte`: later than or at the specified time   + `gt`: later than the specified time * Entity attribute: `<attribute>("value1","value2")` and `<attribute>.exists()`. To fetch the list of available attributes, execute the [GET entity typeï»¿](https://dt-url.net/2ka3ivt) request and check the **properties** field of the response. * Relationships: `fromRelationships.<relationshipName>()` and `toRelationships.<relationshipName>()`. This criterion takes an entity selector as an attribute. To fetch the list of available relationships, execute the [GET entity typeï»¿](https://dt-url.net/2ka3ivt) request and check the **fromRelationships** and **toRelationships** fields. * Negation: `not(<criterion>)`. Inverts any criterion except for **type**.  For more information, see [Entity selectorï»¿](https://dt-url.net/apientityselector) in Dynatrace Documentation.  To set several criteria, separate them with a comma (`,`). For example, `type("HOST"),healthState("HEALTHY")`. Only results matching **all** criteria are included in the response.  The maximum string length is 2,000 characters. | query | Required |
| from | string | The start of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the relative timeframe of 24 hours is used (`now-24h`). | query | Optional |
| to | string | The end of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the current timestamp is used. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [CustomEntityTags](#openapi-definition-CustomEntityTags) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `CustomEntityTags` object

A list of custom tags.

| Element | Type | Description |
| --- | --- | --- |
| tags | [METag[]](#openapi-definition-METag) | A list of custom tags. |
| totalCount | integer | The total number of tags in the response. |

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



"tags": [



{



"context": "CONTEXTLESS",



"key": "mainApp",



"stringRepresentation": "mainApp"



},



{



"context": "CONTEXTLESS",



"key": "bookings",



"stringRepresentation": "bookings"



}



],



"totalCount": 2



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

In this example, the request lists custom tags that are applied to services that belong to the management zones with the ID of **229130632296508575249**. To achieve that, the **entitySelector** query parameter is set to `type("SERVICE"),mzId("9130632296508575249")`.

The API token is passed in the **Authorization** header.

Because the full result is rather lengthy, it is truncated to three entries.

#### Curl

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/tags?entitySelector=type(%22SERVICE%22),mzId(%229130632296508575249%22)' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/tags?entitySelector=type(%22SERVICE%22),mzId(%229130632296508575249%22)
```

#### Response body

```
{



"totalCount": 31,



"tags": [



{



"context": "CONTEXTLESS",



"key": "Billing",



"stringRepresentation": "Billing"



},



{



"context": "CONTEXTLESS",



"key": "Booking",



"stringRepresentation": "Booking"



},



{



"context": "CONTEXTLESS",



"key": "easytravel",



"value": "backend",



"stringRepresentation": "easytravel:backend"



}



]



}
```

#### Response code

200

## Related topics

* [Monitored entities API](/managed/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.")