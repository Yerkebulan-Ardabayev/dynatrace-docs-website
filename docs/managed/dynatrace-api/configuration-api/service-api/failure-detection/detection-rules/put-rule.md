---
title: Failure detection API - PUT a detection rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/failure-detection/detection-rules/put-rule
---

# Failure detection API - PUT a detection rule

# Failure detection API - PUT a detection rule

* Reference
* Published Jan 11, 2021

Updates the specified failure detection rule.

If a rule with the specified ID doesn't exist, a new one is created and appended to the end of the rule list. Rules are evaluated from top to bottom; the first matching rule applies. To enforce a particular order, use the [reorder request](/managed/dynatrace-api/configuration-api/service-api/failure-detection/detection-rules/reorder-rules "Change the order of failure detection rules via the Dynatrace API.").

The failure detection parameter set used by the rule must exist at the time of rule creation.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/rules/{id}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/rules/{id}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

To find all model variations that depend on the type of the model, see [JSON models](/managed/dynatrace-api/configuration-api/service-api/failure-detection/json-models "Learn the variations of JSON models in the Dynatrace failure detection API.").

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required failure detection rule. Needs to be a valid RFC 4122 UUID. | path | Required |
| body | [FailureDetectionRule](#openapi-definition-FailureDetectionRule) | The JSON body of the request. Contains the updated configuration of the failure detection rule.  You can't update the ID with this request. Use the change ID request instead. | body | Optional |

### Request body objects

#### The `FailureDetectionRule` object

Configuration of the failure detection rule.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| conditions | [FailureDetectionCondition](#openapi-definition-FailureDetectionCondition)[] | A list of conditions of the rule.  The rule applies when **all** conditions are fulfilled. | Required |
| description | string | A short description of the rule. | Optional |
| enabled | boolean | The rule is enabled (`true`) or disabled (`false`). | Required |
| fdpId | string | The failure detection parameter (FDP) set of the rule.  Specify the ID of the set here. The FDP set must exist at the time of rule creation. | Required |
| id | string | The ID of the rule. | Optional |
| name | string | The display name of the rule.  The length of the name is limited to 150 characters. | Optional |

#### The `FailureDetectionCondition` object

The condition of the failure detection rule.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| attribute | string | The attribute to be checked. The element can hold these values * `PG_NAME` * `PG_TAG` * `SERVICE_MANAGEMENT_ZONES` * `SERVICE_NAME` * `SERVICE_SERVICE_TYPE` * `SERVICE_TAG` | Optional |
| predicate | [FdcPredicate](#openapi-definition-FdcPredicate) | The predicate that tests the value of the attribute.  The actual set of fields depends on the type of the predicate. Find the list of actual objects in the description of the **type** field or see [Failure detection API - JSON models﻿](https://dt-url.net/9sg3swf). | Optional |

#### The `FdcPredicate` object

The predicate that tests the value of the attribute.

The actual set of fields depends on the type of the predicate. Find the list of actual objects in the description of the **type** field or see [Failure detection API - JSON models﻿](https://dt-url.net/9sg3swf).

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `STRING_EQUALS` -> FdcPredicateStringEquals * `STRING_STARTS_WITH` -> FdcPredicateStringStartsWith * `STRING_ENDS_WITH` -> FdcPredicateStringEndsWith * `STRING_CONTAINS_SUBSTRING` -> FdcPredicateStringContains * `INTEGER_EQUALS` -> FdcPredicateIntegerEquals * `INTEGER_LESS_THAN` -> FdcPredicateIntegerLessThan * `INTEGER_LESS_THAN_OR_EQUAL` -> FdcPredicateIntegerLessThanOrEqual * `INTEGER_GREATER_THAN` -> FdcPredicateIntegerGreaterThan * `INTEGER_GREATER_THAN_OR_EQUAL` -> FdcPredicateIntegerGreaterThanOrEqual * `LONG_EQUALS` -> FdcPredicateLongEquals * `LONG_LESS_THAN` -> FdcPredicateLongLessThan * `LONG_LESS_THAN_OR_EQUAL` -> FdcPredicateLongLessThanOrEqual * `LONG_GREATER_THAN` -> FdcPredicateLongGreaterThan * `LONG_GREATER_THAN_OR_EQUAL` -> FdcPredicateLongGreaterThanOrEqual * `TAG_KEY_EQUALS` -> FdcPredicateTagKeyEquals * `TAG_EQUALS` -> FdcPredicateTagEquals * `SERVICE_TYPE_EQUALS` -> FdcPredicateServiceTypeEquals * `MANAGEMENT_ZONES_CONTAINS_ALL` -> FdcPredicateManagementZonesContainsAll * `SET_OF_INTEGERS_CONTAINS_ANY` -> FdcPredicateSetOfIntegersContainsAny * `SET_OF_INTEGERS_CONTAINS_ALL` -> FdcPredicateSetOfIntegersContainsAll The element can hold these values * `INTEGER_EQUALS` * `INTEGER_GREATER_THAN` * `INTEGER_GREATER_THAN_OR_EQUAL` * `INTEGER_LESS_THAN` * `INTEGER_LESS_THAN_OR_EQUAL` * `LONG_EQUALS` * `LONG_GREATER_THAN` * `LONG_GREATER_THAN_OR_EQUAL` * `LONG_LESS_THAN` * `LONG_LESS_THAN_OR_EQUAL` * `MANAGEMENT_ZONES_CONTAINS_ALL` * `SERVICE_TYPE_EQUALS` * `SET_OF_INTEGERS_CONTAINS_ALL` * `SET_OF_INTEGERS_CONTAINS_ANY` * `STRING_CONTAINS_SUBSTRING` * `STRING_ENDS_WITH` * `STRING_EQUALS` * `STRING_STARTS_WITH` * `TAG_EQUALS` * `TAG_KEY_EQUALS` | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"conditions": [



{



"attribute": "SERVICE_NAME",



"predicate": {



"ignoreCase": false,



"type": "STRING_STARTS_WITH",



"values": [



"shp",



"stg_shp"



]



}



}



],



"description": "for requests from shipping module",



"enabled": true,



"fdpId": "FDP_9",



"id": "R_5",



"name": "shipping"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Success. The new failure detection rule has been created. The response contains the ID of the new rule. |
| **204** | - | Success. The failure detection rule has been updated. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

### Response body objects

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

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



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



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

## Validate payload

We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/rules/{id}/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/rules/{id}/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The submitted configuration is valid. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

#### Response body objects

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

#### Response body JSON models

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