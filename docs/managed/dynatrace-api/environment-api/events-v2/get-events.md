---
title: "Events API v2 - GET list events"
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/events-v2/get-events
updated: 2026-02-09
---

# Events API v2 - GET list events

# Events API v2 - GET list events

* Reference
* Published Aug 06, 2021

Lists events that happened within the specified timeframe along with their properties.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/events` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/events` |

## Authentication

To execute this request, you need an access token with `events.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **nextPageKey** field of the previous response.  The first page is always returned if you don't specify the **nextPageKey** query parameter.  When the **nextPageKey** is set to obtain subsequent pages, you must omit all other query parameters. | query | Optional |
| pageSize | integer | The amount of events in a single response payload.  The maximal allowed page size is 1000.  If not set, 100 is used. | query | Optional |
| from | string | The start of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the relative timeframe of two hours is used (`now-2h`). | query | Optional |
| to | string | The end of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the current timestamp is used. | query | Optional |
| eventSelector | string | Defines the scope of the query. Only events matching the specified criteria are included in the response.  You can add one or several of the criteria listed below. For each criterion you can specify multiple comma-separated values, unless stated otherwise. If several values are specified, the **OR** logic applies.  * Event ID: `eventId("id-1", "id-2")`. * ID of related entity: `entityId("id-1", "id-2")`. * Event status: `status("OPEN")` or `status("CLOSED")`. You can specify only one status. * Management zone ID: `managementZoneId("123", "321")`. * Event type: `eventType("event-type")`. You can specify only one event type. You can fetch the list of possible event types with the [GET event typesï»¿](https://dt-url.net/qc03u6w) call. * Correlation ID: `correlationId("id-1", "id-2")`. * Happened during maintenance (true, false): `underMaintenance(true)`. * Notifications are suppressed (true, false): `suppressAlert(true)`. * Problem creation is suppressed (true, false): `suppressProblem(true)`. * Frequent event (true, false): `frequentEvent(true)`. * Event property: `property.<key>("value-1", "value-2")`. Only properties with the **filterable** property set to `true` can be used. You can check event properties via the [GET event propertiesï»¿](https://dt-url.net/es03nwo) call.  To set several criteria, separate them with commas (`,`). Only results matching **all** criteria are included in the response. | query | Optional |
| entitySelector | string | The entity scope of the query. You must set one of these criteria:  * Entity type: `type("TYPE")` * Dynatrace entity ID: `entityId("id")`. You can specify several IDs, separated by a comma (`entityId("id-1","id-2")`). All requested entities must be of the same type.  You can add one or more of the following criteria. Values are case-sensitive and the `EQUALS` operator is used unless otherwise specified.  * Tag: `tag("value")`. Tags in `[context]key:value`, `key:value`, and `value` formats are detected and parsed automatically. Any colons (`:`) that are part of the key or value must be escaped with a backslash(`\`). Otherwise, it will be interpreted as the separator between the key and the value. All tag values are case-sensitive. * Management zone ID: `mzId(123)` * Management zone name: `mzName("value")` * Entity name: + `entityName.equals`: performs a non-casesensitive `EQUALS` query.   + `entityName.startsWith`: changes the operator to `BEGINS WITH`.   + `entityName.in`: enables you to provide multiple values. The `EQUALS` operator applies.   + `caseSensitive(entityName.equals("value"))`: takes any entity name criterion as an argument and makes the value case-sensitive. * Health state (HEALTHY,UNHEALTHY): `healthState("HEALTHY")` * First seen timestamp: `firstSeenTms.<operator>(now-3h)`. Use any timestamp format from the **from**/**to** parameters.   The following operators are available: + `lte`: earlier than or at the specified time   + `lt`: earlier than the specified time   + `gte`: later than or at the specified time   + `gt`: later than the specified time * Entity attribute: `<attribute>("value1","value2")` and `<attribute>.exists()`. To fetch the list of available attributes, execute the [GET entity typeï»¿](https://dt-url.net/2ka3ivt) request and check the **properties** field of the response. * Relationships: `fromRelationships.<relationshipName>()` and `toRelationships.<relationshipName>()`. This criterion takes an entity selector as an attribute. To fetch the list of available relationships, execute the [GET entity typeï»¿](https://dt-url.net/2ka3ivt) request and check the **fromRelationships** and **toRelationships** fields. * Negation: `not(<criterion>)`. Inverts any criterion except for **type**.  For more information, see [Entity selectorï»¿](https://dt-url.net/apientityselector) in Dynatrace Documentation.  To set several criteria, separate them with a comma (`,`). For example, `type("HOST"),healthState("HEALTHY")`. Only results matching **all** criteria are included in the response.  The maximum string length is 2,000 characters.  The number of entities that can be selected is limited to 10000. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [EventList](#openapi-definition-EventList) | Success. The response contains the list of events. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `EventList` object

A list of events.

| Element | Type | Description |
| --- | --- | --- |
| events | [Event[]](#openapi-definition-Event) | A list of events. |
| nextPageKey | string | The cursor for the next page of results. Has the value of `null` on the last page.  Use it in the **nextPageKey** query parameter to obtain subsequent pages of the result. |
| pageSize | integer | The number of entries per page. |
| totalCount | integer | The total number of entries in the result. |
| warnings | string[] | A list of warnings. |

#### The `Event` object

Configuration of an event.

| Element | Type | Description |
| --- | --- | --- |
| correlationId | string | The correlation ID of the event. |
| endTime | integer | The timestamp when the event was closed, in UTC milliseconds.  Has the value of `null` if the event is still active. |
| entityId | [EntityStub](#openapi-definition-EntityStub) | A short representation of a monitored entity. |
| entityTags | [METag[]](#openapi-definition-METag) | A list of tags of the related entity. |
| eventId | string | The ID of the event. |
| eventType | string | The type of the event. |
| frequentEvent | boolean | If `true`, the event happens [frequentlyï»¿](https://dt-url.net/4da3kdg).  A frequent event doesn't raise a problem. |
| managementZones | [ManagementZone[]](#openapi-definition-ManagementZone) | A list of all management zones that the event belongs to. |
| properties | [EventProperty[]](#openapi-definition-EventProperty) | A list of event properties. |
| startTime | integer | The timestamp when the event was raised, in UTC milliseconds. |
| status | string | The status of the event. The element can hold these values * `CLOSED` * `OPEN` |
| suppressAlert | boolean | The alerting status during a [maintenanceï»¿](https://dt-url.net/b2123rg0):  * `false`: Alerting works as usual. * `true`: Alerting is disabled. |
| suppressProblem | boolean | The problem detection status during a [maintenanceï»¿](https://dt-url.net/b2123rg0):  * `false`: Problem detection works as usual. * `true`: Problem detection is disabled. |
| title | string | The title of the event. |
| underMaintenance | boolean | If `true`, the event happened while the monitored system was under maintenance. |

#### The `EntityStub` object

A short representation of a monitored entity.

| Element | Type | Description |
| --- | --- | --- |
| entityId | [EntityId](#openapi-definition-EntityId) | A short representation of a monitored entity. |
| name | string | The name of the entity.  Not included in the response in case no entity with the relevant ID was found. |

#### The `EntityId` object

A short representation of a monitored entity.

| Element | Type | Description |
| --- | --- | --- |
| id | string | The ID of the entity. |
| type | string | The type of the entity. |

#### The `METag` object

The tag of a monitored entity.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. |
| key | string | The key of the tag. |
| stringRepresentation | string | The string representation of the tag. |
| value | string | The value of the tag. |

#### The `ManagementZone` object

A short representation of a management zone.

| Element | Type | Description |
| --- | --- | --- |
| id | string | The ID of the management zone. |
| name | string | The name of the management zone. |

#### The `EventProperty` object

A property of an event.

| Element | Type | Description |
| --- | --- | --- |
| key | string | The key of the event property. |
| value | string | The value of the event property. |

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



"events": [



{



"correlationId": "933613657e1c8fcf",



"endTime": 1564039524182,



"entityId": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"entityTags": [



{



"context": "string",



"key": "string",



"stringRepresentation": "string",



"value": "string"



}



],



"eventId": "4293884258445543163_1564039524182",



"eventType": "LOW_DISK_SPACE",



"frequentEvent": true,



"managementZones": [



{



"id": "string",



"name": "string"



}



],



"properties": [



{



"key": "string",



"value": "string"



}



],



"startTime": 1564039524182,



"status": "OPEN",



"suppressAlert": true,



"suppressProblem": true,



"title": "High CPU load on host X",



"underMaintenance": true



}



],



"nextPageKey": "AQAAABQBAAAABQ==",



"pageSize": 1,



"totalCount": 1,



"warnings": [



"string"



]



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

In this example, the request lists all events of the **PROCESS\_RESTART** (`eventSelector=eventType("PROCESS_RESTART")`) that happened within the last **2 hours** (`from=now-2h`) while a maintenance window was active (`eventSelector=underMaintenance(true)`). The result is truncated to two events.

The API token is passed in the **Authorization** header.

#### Curl

```
curl --request GET \



--url 'https://mySampleEnv.live.dynatrace.com/api/v2/events?eventSelector=eventType(%22PROCESS_RESTART%22)%2CunderMaintenance(true)&from=now-2h' \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/events?eventSelector=eventType(%22PROCESS_RESTART%22)%2CunderMaintenance(true)&from=now-2h
```

#### Response body

```
{



"totalCount": 43,



"pageSize": 100,



"events": [



{



"eventId": "-6475311485380369979_1628500180000",



"startTime": 1628500180000,



"endTime": 1628500240000,



"eventType": "PROCESS_RESTART",



"title": "Process restart",



"entityId": {



"entityId": {



"id": "PROCESS_GROUP_INSTANCE-03F98EA8639FD052",



"type": "PROCESS_GROUP_INSTANCE"



},



"name": "IIS app pool dotNetFrontend_easyTravel_x64"



},



"properties": [



{



"key": "dt.event.group_label",



"value": "Process restart"



}



],



"status": "OPEN",



"entityTags": [



{



"context": "CONTEXTLESS",



"key": "easyTravel",



"stringRepresentation": "easyTravel"



},



{



"context": "CONTEXTLESS",



"key": "tech",



"value": "IIS",



"stringRepresentation": "tech:IIS"



},



{



"context": "CONTEXTLESS",



"key": "tech",



"value": ".NET",



"stringRepresentation": "tech:.NET"



},



{



"context": "CONTEXTLESS",



"key": "hosts",



"value": "w-077",



"stringRepresentation": "hosts:w-077"



},



{



"context": "CONTEXTLESS",



"key": "Infrastructure",



"value": "Windows",



"stringRepresentation": "Infrastructure:Windows"



},



{



"context": "CONTEXTLESS",



"key": "dotNetFrontend",



"stringRepresentation": "dotNetFrontend"



},



],



"managementZones": [



{



"id": "9130632296508575249",



"name": "Easytravel"



},



{



"id": "-6239538939987181652",



"name": "frontend"



},



{



"id": "5130731705740636866",



"name": "Windows"



}



],



"underMaintenance": true,



"suppressAlert": true,



"suppressProblem": true,



"frequentEvent": false



},



{



"eventId": "-231290298591263162_1628500000000",



"startTime": 1628500000000,



"endTime": 1628500060000,



"eventType": "PROCESS_RESTART",



"title": "Process restart",



"entityId": {



"entityId": {



"id": "PROCESS_GROUP_INSTANCE-00CA9B0F1AE9BAF8",



"type": "PROCESS_GROUP_INSTANCE"



},



"name": "chromedriver_linux64"



},



"properties": [



{



"key": "dt.event.group_label",



"value": "Process restart"



}



],



"status": "CLOSED",



"entityTags": [



{



"context": "CONTEXTLESS",



"key": "Infrastructure",



"value": "Linux",



"stringRepresentation": "Infrastructure:Linux"



},



{



"context": "CONTEXTLESS",



"key": "hosts",



"value": "l-008",



"stringRepresentation": "hosts:l-008"



}



],



"managementZones": [



{



"id": "2631544906797876001",



"name": "Linux"



}



],



"underMaintenance": true,



"suppressAlert": false,



"suppressProblem": false,



"frequentEvent": false



}



],



"warnings": []



}
```

#### Response code

200

## Related topics

* [Event categories](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Learn about different categories of events and supported event types, along with their severity levels, and the logic behind raising them.")
* [Event analysis and correlation](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Gain an understanding of the Events section on each host, process, and service overview page.")
