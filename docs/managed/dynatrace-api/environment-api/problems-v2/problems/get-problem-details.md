---
title: Problems API v2 - GET problems details
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/problems-v2/problems/get-problem-details
scraped: 2026-05-12T11:57:21.415895
---

# Problems API v2 - GET problems details

# Problems API v2 - GET problems details

* Reference
* Published Oct 12, 2020

Lists all details of the specified problem.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/problems/{problemId}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/problems/{problemId}` |

## Authentication

To execute this request, you need an access token with `problems.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| problemId | string | The ID of the required problem. | path | Required |
| fields | string | A list of additional problem properties you can add to the response.  The following properties are available (all other properties are always included and you can't remove them from the response):  * `evidenceDetails`: The details of the root cause. * `impactAnalysis`: The impact analysis of the problem on other entities/users. * `recentComments`: A list of the most recent comments to the problem.  To add properties, specify them as a comma-separated list (for example, `evidenceDetails,impactAnalysis`). | query | Optional |

## Response

Some JSON models vary depending on the **type** of the model. To find all the possible variations, refer to [JSON models](/managed/dynatrace-api/environment-api/problems-v2/models "Learn the variations of models in the Problems v2 API.").

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [Problem](#openapi-definition-Problem) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `Problem` object

The properties of a problem.

| Element | Type | Description |
| --- | --- | --- |
| affectedEntities | [EntityStub[]](#openapi-definition-EntityStub) | A list of all entities that are affected by the problem. |
| displayId | string | The display ID of the problem. |
| endTime | integer | The end timestamp of the problem, in UTC milliseconds.  Has `-1` value, if the problem is still open. |
| entityTags | [METag[]](#openapi-definition-METag) | A list of all entity tags of the problem. |
| evidenceDetails | [EvidenceDetails](#openapi-definition-EvidenceDetails) | The evidence details of a problem. |
| impactAnalysis | [ImpactAnalysis](#openapi-definition-ImpactAnalysis) | A list of all impacts of the problem. |
| impactLevel | string | The impact level of the problem. It shows what is affected by the problem. The element can hold these values * `APPLICATION` * `ENVIRONMENT` * `INFRASTRUCTURE` * `SERVICES` |
| impactedEntities | [EntityStub[]](#openapi-definition-EntityStub) | A list of all entities that are impacted by the problem. |
| k8s.cluster.name | string[] | The related Kubernetes cluster names. |
| k8s.cluster.uid | string[] | The related Kubernetes cluster UIDs. |
| k8s.namespace.name | string[] | The related Kubernetes namespace names. |
| linkedProblemInfo | [LinkedProblem](#openapi-definition-LinkedProblem) | The properties of the linked problem. |
| managementZones | [ManagementZone[]](#openapi-definition-ManagementZone) | A list of all management zones that the problem belongs to. |
| problemFilters | [AlertingProfileStub[]](#openapi-definition-AlertingProfileStub) | A list of alerting profiles that match the problem. |
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
| details | [Evidence[]](#openapi-definition-Evidence) | A list of all evidence. |
| totalCount | integer | The total number of evidence of a problem. |

#### The `Evidence` object

An evidence of a root cause.

The actual set of fields depends on the type of the evidence. Find the list of actual objects in the description of the **evidenceType** field or see [Problems API v2 - JSON modelsï»¿](https://dt-url.net/we03sp2).

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
| impacts | [Impact[]](#openapi-definition-Impact) | A list of all impacts of the problem. |

#### The `Impact` object

The impact analysis of the problem on other entities/users.

The actual set of fields depends on the type of the impact. Find the list of actual objects in the description of the **impactType** field or see [Problems API v2 - JSON modelsï»¿](https://dt-url.net/we03sp2).

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
| comments | [Comment[]](#openapi-definition-Comment) | The result entries. |
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

* [DavisÂ® AI](/managed/dynatrace-intelligence "Get familiar with the capabilities of Davis AI.")