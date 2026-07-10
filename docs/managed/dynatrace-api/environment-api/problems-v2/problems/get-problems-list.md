---
title: Problems API v2 - GET problems list
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/problems-v2/problems/get-problems-list
---

# Problems API v2 - GET problems list

# Problems API v2 - GET problems list

* Reference
* Published Oct 12, 2020

Lists the problems (and their details) observed by Dynatrace during a relative period of time.

A problem is included in the response if either the start or end timestamp of the problem is within the defined timeframe.

You can narrow down the output by specifying filtering criteria—see the [**Parameters** section](#parameters).

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/problems` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/problems` |

## Authentication

To execute this request, you need an access token with `problems.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| fields | string | A list of additional problem properties you can add to the response.  The following properties are available (all other properties are always included and you can't remove them from the response):  * `evidenceDetails`: The details of the root cause. * `impactAnalysis`: The impact analysis of the problem on other entities/users. * `recentComments`: A list of the most recent comments to the problem.  To add properties, specify them as a comma-separated list (for example, `evidenceDetails,impactAnalysis`).  The field is valid only for the current page of results. You must set it for each page you're requesting. | query | Optional |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **nextPageKey** field of the previous response.  The first page is always returned if you don't specify the **nextPageKey** query parameter.  When the **nextPageKey** is set to obtain subsequent pages, you must omit all other query parameters except the optional **fields** parameter. | query | Optional |
| pageSize | integer | The amount of problems in a single response payload.  The maximal allowed page size is 500.  If not set, 50 is used. | query | Optional |
| from | string | The start of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the relative timeframe of two hours is used (`now-2h`). | query | Optional |
| to | string | The end of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the current timestamp is used. | query | Optional |
| problemSelector | string | Defines the scope of the query. Only problems matching the specified criteria are included into response.  You can add one or several of the criteria listed below. For each criterion you can specify multiple comma-separated values, unless stated otherwise. If several values are specified, the **OR** logic applies. All values must be quoted.  * Status: `status("open")` or `status("closed")`. You can specify only one status. * Severity level: `severityLevel("level-1","level-2")`. Find the possible values in the description of the **severityLevel** field of the response. * Impact level: `impactLevel("level-11","level-2")` Find the possible values in the description of the **impactLevel** field of the response. * Root cause entity: `rootCauseEntity("id-1", "id-2")`. * Management zone ID: `managementZoneIds("mZId-1", "mzId-2")`. * Management zone name: `managementZones("value-1","value-2")`. * Impacted entities: `impactedEntities("id-1", "id-2")`. * Affected entities: `affectedEntities("id-1", "id-2")`. * Type of affected entities: `affectedEntityTypes("value-1","value-2")`. * Problem ID: `problemId("id-1", "id-2")`. * Alerting profile ID: `problemFilterIds("id-1", "id-2")`. * Alerting profile name (contains, case-insensitive): `problemFilterNames("value-1","value-2")`. * Alerting profile name (exact match, case-insensitive): `problemFilterNames.equals("value-1","value-2")`. * Entity tags: `entityTags("[context]key:value","key:value")`. Tags in `[context]key:value`, `key:value`, and `value` formats are detected and parsed automatically. If a value-only tag has a colon (`:`) in it, you must escape the colon with a backslash(`\`). Otherwise, the tag will be parsed as a `key:value tag`. All tag values are case-sensitive. * Display ID of the problem: `displayId("id-1", "id-2")`. * Under maintenance: `underMaintenance(true|false)`. Shows (true) or hides (false) all problems created during maintenance mode. * Text search: `text("value")`. Text search on the following fields: problem title, event titles, displayId and the id of affected and impacted entities. The text search is case insensitive, partial matching and based on a relevance score. Therefore the `relevance` sort option should be used to get the most relevant problems first. The special characters `~` and `"` need to be escaped using a `~` (e.g. double quote search `text("~"")`). The search value is limited to 30 characters.  To set several criteria, separate them with a comma (`,`). Only results matching **all** criteria are included in the response. | query | Optional |
| entitySelector | string | The entity scope of the query. You must set one of these criteria:  * Entity type: `type("TYPE")` * Dynatrace entity ID: `entityId("id")`. You can specify several IDs, separated by a comma (`entityId("id-1","id-2")`). All requested entities must be of the same type.  You can add one or more of the following criteria. Values are case-sensitive and the `EQUALS` operator is used unless otherwise specified.  * Tag: `tag("value")`. Tags in `[context]key:value`, `key:value`, and `value` formats are detected and parsed automatically. Any colons (`:`) that are part of the key or value must be escaped with a backslash(`\`). Otherwise, it will be interpreted as the separator between the key and the value. All tag values are case-sensitive. * Management zone ID: `mzId(123)` * Management zone name: `mzName("value")` * Entity name: + `entityName.equals`: performs a non-casesensitive `EQUALS` query.   + `entityName.startsWith`: changes the operator to `BEGINS WITH`.   + `entityName.in`: enables you to provide multiple values. The `EQUALS` operator applies.   + `caseSensitive(entityName.equals("value"))`: takes any entity name criterion as an argument and makes the value case-sensitive. * Health state (HEALTHY,UNHEALTHY): `healthState("HEALTHY")` * First seen timestamp: `firstSeenTms.<operator>(now-3h)`. Use any timestamp format from the **from**/**to** parameters.   The following operators are available: + `lte`: earlier than or at the specified time   + `lt`: earlier than the specified time   + `gte`: later than or at the specified time   + `gt`: later than the specified time * Entity attribute: `<attribute>("value1","value2")` and `<attribute>.exists()`. To fetch the list of available attributes, execute the [GET entity type﻿](https://dt-url.net/2ka3ivt?dt=m) request and check the **properties** field of the response. * Relationships: `fromRelationships.<relationshipName>()` and `toRelationships.<relationshipName>()`. This criterion takes an entity selector as an attribute. To fetch the list of available relationships, execute the [GET entity type﻿](https://dt-url.net/2ka3ivt?dt=m) request and check the **fromRelationships** and **toRelationships** fields. * Negation: `not(<criterion>)`. Inverts any criterion except for **type**.  For more information, see [Entity selector﻿](https://dt-url.net/apientityselector?dt=m) in Dynatrace Documentation.  To set several criteria, separate them with a comma (`,`). For example, `type("HOST"),healthState("HEALTHY")`. Only results matching **all** criteria are included in the response.  The maximum string length is 2,000 characters.  The maximum number of entities that may be selected is limited to 10000. | query | Optional |
| sort | string | Specifies a set of comma-separated (`,`) fields for sorting in the problem list.  You can sort by the following properties with a sign prefix for the sorting order.  * `status`: problem status (`+` open problems first or `-` closed problems first) * `startTime`: problem start time (`+` old problems first or `-` new problems first) * `relevance`: problem relevance (`+` least relevant problems first or `-` most relevant problems first) - can be used only in combination with text search  If no prefix is set, `+` is used.  You can specify several levels of sorting. For example, `+status,-startTime` sorts problems by status, open problems first. Within the status, problems are sorted by start time, oldest first. | query | Optional |

## Response

Some JSON models vary depending on the **type** of the model. To find all the possible variations, refer to [JSON models](/managed/dynatrace-api/environment-api/problems-v2/models "Learn the variations of models in the Problems v2 API.").

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [Problems](#openapi-definition-Problems) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `Problems` object

A list of problems.

| Element | Type | Description |
| --- | --- | --- |
| nextPageKey | string | The cursor for the next page of results. Has the value of `null` on the last page.  Use it in the **nextPageKey** query parameter to obtain subsequent pages of the result. |
| pageSize | integer | The number of entries per page. |
| problems | [Problem](#openapi-definition-Problem)[] | The result entries. |
| totalCount | integer | The total number of entries in the result. |
| warnings | string[] | A list of warnings |

#### The `Problem` object

The properties of a problem.

| Element | Type | Description |
| --- | --- | --- |
| affectedEntities | [EntityStub](#openapi-definition-EntityStub)[] | A list of all entities that are affected by the problem. |
| displayId | string | The display ID of the problem. |
| endTime | integer | The end timestamp of the problem, in UTC milliseconds.  Has `-1` value, if the problem is still open. |
| entityTags | [METag](#openapi-definition-METag)[] | A list of all entity tags of the problem. |
| evidenceDetails | [EvidenceDetails](#openapi-definition-EvidenceDetails) | The evidence details of a problem. |
| impactAnalysis | [ImpactAnalysis](#openapi-definition-ImpactAnalysis) | A list of all impacts of the problem. |
| impactLevel | string | The impact level of the problem. It shows what is affected by the problem. The element can hold these values * `APPLICATION` * `ENVIRONMENT` * `INFRASTRUCTURE` * `SERVICES` |
| impactedEntities | [EntityStub](#openapi-definition-EntityStub)[] | A list of all entities that are impacted by the problem. |
| k8s.cluster.name | string[] | The related Kubernetes cluster names. |
| k8s.cluster.uid | string[] | The related Kubernetes cluster UIDs. |
| k8s.namespace.name | string[] | The related Kubernetes namespace names. |
| linkedProblemInfo | [LinkedProblem](#openapi-definition-LinkedProblem) | The properties of the linked problem. |
| managementZones | [ManagementZone](#openapi-definition-ManagementZone)[] | A list of all management zones that the problem belongs to. |
| problemFilters | [AlertingProfileStub](#openapi-definition-AlertingProfileStub)[] | A list of alerting profiles that match the problem. |
| problemId | string | The ID of the problem. |
| recentComments | [CommentsList](#openapi-definition-CommentsList) | A list of comments. |
| rootCauseEntity | [EntityStub](#openapi-definition-EntityStub) | A short representation of a monitored entity. |
| severityLevel | string | The severity of the problem. The element can hold these values * `AVAILABILITY` * `CUSTOM_ALERT` * `ERROR` * `INFO` * `MONITORING_UNAVAILABLE` * `PERFORMANCE` * `RESOURCE_CONTENTION` |
| startTime | integer | The start timestamp of the problem, in UTC milliseconds. |
| status | string | The status of the problem. The element can hold these values * `CLOSED` * `OPEN` |
| title | string | The name of the problem, displayed in the UI. |

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

#### The `EvidenceDetails` object

The evidence details of a problem.

| Element | Type | Description |
| --- | --- | --- |
| details | [Evidence](#openapi-definition-Evidence)[] | A list of all evidence. |
| totalCount | integer | The total number of evidence of a problem. |

#### The `Evidence` object

An evidence of a root cause.

The actual set of fields depends on the type of the evidence. Find the list of actual objects in the description of the **evidenceType** field or see [Problems API v2 - JSON models﻿](https://dt-url.net/we03sp2?dt=m).

| Element | Type | Description |
| --- | --- | --- |
| displayName | string | The display name of the evidence. |
| entity | [EntityStub](#openapi-definition-EntityStub) | A short representation of a monitored entity. |
| evidenceType | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `EVENT` -> EventEvidence * `METRIC` -> MetricEvidence * `TRANSACTIONAL` -> TransactionalEvidence * `MAINTENANCE_WINDOW` -> MaintenanceWindowEvidence * `AVAILABILITY_EVIDENCE` -> AvailabilityEvidence The element can hold these values * `AVAILABILITY_EVIDENCE` * `EVENT` * `MAINTENANCE_WINDOW` * `METRIC` * `TRANSACTIONAL` |
| groupingEntity | [EntityStub](#openapi-definition-EntityStub) | A short representation of a monitored entity. |
| rootCauseRelevant | boolean | The evidence is (`true`) or is not (`false`) a part of the root cause. |
| startTime | integer | The start time of the evidence, in UTC milliseconds. |

#### The `ImpactAnalysis` object

A list of all impacts of the problem.

| Element | Type | Description |
| --- | --- | --- |
| impacts | [Impact](#openapi-definition-Impact)[] | A list of all impacts of the problem. |

#### The `Impact` object

The impact analysis of the problem on other entities/users.

The actual set of fields depends on the type of the impact. Find the list of actual objects in the description of the **impactType** field or see [Problems API v2 - JSON models﻿](https://dt-url.net/we03sp2?dt=m).

| Element | Type | Description |
| --- | --- | --- |
| estimatedAffectedUsers | integer | The estimated number of affected users. |
| impactType | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `SERVICE` -> ServiceImpact * `APPLICATION` -> ApplicationImpact * `MOBILE` -> MobileImpact * `CUSTOM_APPLICATION` -> CustomApplicationImpact The element can hold these values * `APPLICATION` * `CUSTOM_APPLICATION` * `MOBILE` * `SERVICE` |
| impactedEntity | [EntityStub](#openapi-definition-EntityStub) | A short representation of a monitored entity. |

#### The `LinkedProblem` object

The properties of the linked problem.

| Element | Type | Description |
| --- | --- | --- |
| displayId | string | The display ID of the problem. |
| problemId | string | The ID of the problem. |

#### The `ManagementZone` object

A short representation of a management zone.

| Element | Type | Description |
| --- | --- | --- |
| id | string | The ID of the management zone. |
| name | string | The name of the management zone. |

#### The `AlertingProfileStub` object

Short representation of the alerting profile.

| Element | Type | Description |
| --- | --- | --- |
| id | string | The ID of the alerting profile. |
| name | string | The name of the alerting profile. |

#### The `CommentsList` object

A list of comments.

| Element | Type | Description |
| --- | --- | --- |
| comments | [Comment](#openapi-definition-Comment)[] | The result entries. |
| nextPageKey | string | The cursor for the next page of results. Has the value of `null` on the last page.  Use it in the **nextPageKey** query parameter to obtain subsequent pages of the result. |
| pageSize | integer | The number of entries per page. |
| totalCount | integer | The total number of entries in the result. |

#### The `Comment` object

The comment to a problem.

| Element | Type | Description |
| --- | --- | --- |
| authorName | string | The user who wrote the comment. |
| content | string | The text of the comment. |
| context | string | The context of the comment. |
| createdAtTimestamp | integer | The timestamp of comment creation, in UTC milliseconds. |
| id | string | The ID of the comment. |

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



"nextPageKey": "AQAAABQBAAAABQ==",



"pageSize": 1,



"problems": [



{



"affectedEntities": [



{



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



}



],



"displayId": "string",



"endTime": 1,



"entityTags": [



{



"context": "string",



"key": "string",



"stringRepresentation": "string",



"value": "string"



}



],



"evidenceDetails": {



"details": [



{



"displayName": "string",



"entity": {},



"evidenceType": "AVAILABILITY_EVIDENCE",



"groupingEntity": {},



"rootCauseRelevant": true,



"startTime": 1



}



],



"totalCount": 1



},



"impactAnalysis": {



"impacts": [



{



"estimatedAffectedUsers": 1,



"impactType": "APPLICATION",



"impactedEntity": {}



}



]



},



"impactLevel": "APPLICATION",



"impactedEntities": [



{}



],



"k8s.cluster.name": [



"string"



],



"k8s.cluster.uid": [



"string"



],



"k8s.namespace.name": [



"string"



],



"linkedProblemInfo": {



"displayId": "string",



"problemId": "string"



},



"managementZones": [



{



"id": "string",



"name": "string"



}



],



"problemFilters": [



{



"id": "string",



"name": "string"



}



],



"problemId": "string",



"recentComments": {



"comments": [



{



"authorName": "string",



"content": "string",



"context": "string",



"createdAtTimestamp": 1,



"id": "string"



}



],



"nextPageKey": "AQAAABQBAAAABQ==",



"pageSize": 1,



"totalCount": 1



},



"rootCauseEntity": {},



"severityLevel": "AVAILABILITY",



"startTime": 1,



"status": "CLOSED",



"title": "string"



}



],



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

## Related topics

* [Davis® AI](/managed/dynatrace-intelligence "Learn how Davis® AI detects performance anomalies, identifies root causes, and uses AI models for adaptive thresholds across your environment.")