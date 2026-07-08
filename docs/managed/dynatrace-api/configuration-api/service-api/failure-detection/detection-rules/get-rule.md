---
title: Failure detection API - GET a detection rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/failure-detection/detection-rules/get-rule
---

# Failure detection API - GET a detection rule

# Failure detection API - GET a detection rule

* Reference
* Published Jan 11, 2021

Gets the specified failure detection rule.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/rules/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/rules/{id}` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required failure detection rule. Needs to be a valid RFC 4122 UUID. | path | Required |

## Response

To find all model variations that depend on the type of the model, see [JSON models](/managed/dynatrace-api/configuration-api/service-api/failure-detection/json-models "Learn the variations of JSON models in the Dynatrace failure detection API.").

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [FailureDetectionRule](#openapi-definition-FailureDetectionRule) | Success |
| **404** | - | Failed. The specified entity doesn't exist. |

### Response body objects

#### The `FailureDetectionRule` object

Configuration of the failure detection rule.

| Element | Type | Description |
| --- | --- | --- |
| conditions | [FailureDetectionCondition](#openapi-definition-FailureDetectionCondition)[] | A list of conditions of the rule.  The rule applies when **all** conditions are fulfilled. |
| description | string | A short description of the rule. |
| enabled | boolean | The rule is enabled (`true`) or disabled (`false`). |
| fdpId | string | The failure detection parameter (FDP) set of the rule.  Specify the ID of the set here. The FDP set must exist at the time of rule creation. |
| id | string | The ID of the rule. |
| name | string | The display name of the rule.  The length of the name is limited to 150 characters. |

#### The `FailureDetectionCondition` object

The condition of the failure detection rule.

| Element | Type | Description |
| --- | --- | --- |
| attribute | string | The attribute to be checked. The element can hold these values * `PG_NAME` * `PG_TAG` * `SERVICE_MANAGEMENT_ZONES` * `SERVICE_NAME` * `SERVICE_SERVICE_TYPE` * `SERVICE_TAG` |
| predicate | [FdcPredicate](#openapi-definition-FdcPredicate) | The predicate that tests the value of the attribute.  The actual set of fields depends on the type of the predicate. Find the list of actual objects in the description of the **type** field or see [Failure detection API - JSON models﻿](https://dt-url.net/9sg3swf). |

#### The `FdcPredicate` object

The predicate that tests the value of the attribute.

The actual set of fields depends on the type of the predicate. Find the list of actual objects in the description of the **type** field or see [Failure detection API - JSON models﻿](https://dt-url.net/9sg3swf).

| Element | Type | Description |
| --- | --- | --- |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `STRING_EQUALS` -> FdcPredicateStringEquals * `STRING_STARTS_WITH` -> FdcPredicateStringStartsWith * `STRING_ENDS_WITH` -> FdcPredicateStringEndsWith * `STRING_CONTAINS_SUBSTRING` -> FdcPredicateStringContains * `INTEGER_EQUALS` -> FdcPredicateIntegerEquals * `INTEGER_LESS_THAN` -> FdcPredicateIntegerLessThan * `INTEGER_LESS_THAN_OR_EQUAL` -> FdcPredicateIntegerLessThanOrEqual * `INTEGER_GREATER_THAN` -> FdcPredicateIntegerGreaterThan * `INTEGER_GREATER_THAN_OR_EQUAL` -> FdcPredicateIntegerGreaterThanOrEqual * `LONG_EQUALS` -> FdcPredicateLongEquals * `LONG_LESS_THAN` -> FdcPredicateLongLessThan * `LONG_LESS_THAN_OR_EQUAL` -> FdcPredicateLongLessThanOrEqual * `LONG_GREATER_THAN` -> FdcPredicateLongGreaterThan * `LONG_GREATER_THAN_OR_EQUAL` -> FdcPredicateLongGreaterThanOrEqual * `TAG_KEY_EQUALS` -> FdcPredicateTagKeyEquals * `TAG_EQUALS` -> FdcPredicateTagEquals * `SERVICE_TYPE_EQUALS` -> FdcPredicateServiceTypeEquals * `MANAGEMENT_ZONES_CONTAINS_ALL` -> FdcPredicateManagementZonesContainsAll * `SET_OF_INTEGERS_CONTAINS_ANY` -> FdcPredicateSetOfIntegersContainsAny * `SET_OF_INTEGERS_CONTAINS_ALL` -> FdcPredicateSetOfIntegersContainsAll The element can hold these values * `INTEGER_EQUALS` * `INTEGER_GREATER_THAN` * `INTEGER_GREATER_THAN_OR_EQUAL` * `INTEGER_LESS_THAN` * `INTEGER_LESS_THAN_OR_EQUAL` * `LONG_EQUALS` * `LONG_GREATER_THAN` * `LONG_GREATER_THAN_OR_EQUAL` * `LONG_LESS_THAN` * `LONG_LESS_THAN_OR_EQUAL` * `MANAGEMENT_ZONES_CONTAINS_ALL` * `SERVICE_TYPE_EQUALS` * `SET_OF_INTEGERS_CONTAINS_ALL` * `SET_OF_INTEGERS_CONTAINS_ANY` * `STRING_CONTAINS_SUBSTRING` * `STRING_ENDS_WITH` * `STRING_EQUALS` * `STRING_STARTS_WITH` * `TAG_EQUALS` * `TAG_KEY_EQUALS` |

### Response body JSON models

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