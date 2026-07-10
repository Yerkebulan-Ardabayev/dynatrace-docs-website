---
title: Failure detection API - POST a parameter set
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/failure-detection/parameter-set/post-parameter-set
---

# Failure detection API - POST a parameter set

# Failure detection API - POST a parameter set

* Reference
* Published Jan 11, 2021

Creates a new failure detection parameter set.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/parameterSets` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/parameterSets` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The body must not provide an ID. An ID is assigned automatically by Dynatrace and returned as part of the response.

To find all model variations that depend on the type of the model, see [JSON models](/managed/dynatrace-api/configuration-api/service-api/failure-detection/json-models "Learn the variations of JSON models in the Dynatrace failure detection API.").

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [FailureDetectionParameterSet](#openapi-definition-FailureDetectionParameterSet) | The JSON body of the request. Contains the new failure detection parameter set.  Dynatrace will generate a random UUID for you, if you don't specify an ID. | body | Optional |

### Request body objects

#### The `FailureDetectionParameterSet` object

A set of failure detection parameters (FDP).

These parameters define the conditions of failure and success.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| brokenLinkDomains | string[] | A list of domains for the special handling of the 404 HTTP response code.  If the top domain of the *Referer* is presented in the list OR equals the top domain of the request's host, the 404 code is considered a failure.  Only applicable when **isHttp404NotFoundFailureEnabled** is set to `true`. | Optional |
| clientSideMissingHttpCodeIsFailure | boolean | The missing HTTP response code on the client side is a failure (`true`) or a success (`false`).  If not set, `false` is used. | Optional |
| description | string | A short description of the FDP set. | Optional |
| exceptionOnAnyNodeExceptionPatterns | [ExceptionPattern](#openapi-definition-ExceptionPattern)[] | A list of faulty exceptions.  If an exception on *any* node of the service matches *any* of these patterns it is considered a failure. | Optional |
| failingHttpCodesClientSide | string | A list of client side HTTP response codes that are considered a failure.  The format is a list of ranges and individual values (for example, `500-599, 400-499, 1008`).  If not set, the range of `400-599` is used. | Optional |
| failingHttpCodesServerSide | string | A list of server side HTTP response codes that are considered a failure.  The format is a list of ranges and individual values (for example, `500-599, 400-499, 1008`).If not set, the range of `500-599` is used. | Optional |
| http404NotFoundFailureEnabled | boolean | Special handling of the 404 HTTP response code is enabled (`true`) or disabled (`false`). See **brokenLinkDomains** for special handling details.  Only applicable when 404 is NOT in the list of failing HTTP response codes and only for the server side.  If not set, `false` is used. | Optional |
| id | string | The ID of the parameter set. | Optional |
| ignoreAllExceptions | boolean | If set to true all exceptions will be ignored. Which means defined exception patterns will not have any effect. | Optional |
| ignoreSpanFailureDetection | boolean | If set to true span failure detection will be ignored. | Optional |
| ignoredExceptionPatterns | [ExceptionPattern](#openapi-definition-ExceptionPattern)[] | A list of ignored exceptions.  If an exception on the entry node of the service matches *any* of these patterns it is ignored by failure detection. | Optional |
| name | string | The display name of the FDP set.  The length of the name is limited to 150 characters. | Optional |
| serverSideMissingHttpCodeIsFailure | boolean | The missing HTTP response code on the server side is a failure (`true`) or a success (`false`).  If not set, `false` is used. | Optional |
| successForcingExceptionPatterns | [ExceptionPattern](#openapi-definition-ExceptionPattern)[] | A list of success exceptions.  If an exception on the entry node of the service matches *any* of these patterns it is considered a success. | Optional |
| tagConditions | [FdpTagCondition](#openapi-definition-FdpTagCondition)[] | A list of tag-based conditions.  If *any* condition is fulfilled the request is considered a failure. | Optional |

#### The `ExceptionPattern` object

A list of faulty exceptions.

If an exception on *any* node of the service matches *any* of these patterns it is considered a failure.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| classPattern | string | - | Optional |
| messagePattern | string | - | Optional |

#### The `FdpTagCondition` object

Configuration of the tag condition in the FDP set.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| predicate | [FdpTagPredicate](#openapi-definition-FdpTagPredicate) | The predicate that tests the value of the tag.  The actual set of fields depends on the type of the predicate. Find the list of actual objects in the description of the **type** field or see [Failure detection API - JSON models﻿](https://dt-url.net/9sg3swf?dt=m). | Required |
| tagKey | string | The key of the tag to be checked. | Required |

#### The `FdpTagPredicate` object

The predicate that tests the value of the tag.

The actual set of fields depends on the type of the predicate. Find the list of actual objects in the description of the **type** field or see [Failure detection API - JSON models﻿](https://dt-url.net/9sg3swf?dt=m).

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `STRING_EXISTS` -> FdpTagStringExists * `STRING_EQUALS` -> FdpTagStringEquals * `STRING_STARTS_WITH` -> FdpTagStringStartsWith * `STRING_ENDS_WITH` -> FdpTagStringEndsWith * `STRING_CONTAINS_SUBSTRING` -> FdpTagStringContainsSubstring * `INTEGER_EXISTS` -> FdpTagIntegerExists * `INTEGER_EQUALS` -> FdpTagIntegerEquals * `INTEGER_LESS_THAN` -> FdpTagIntegerLessThan * `INTEGER_LESS_THAN_OR_EQUAL` -> FdpTagIntegerLessThanOrEqual * `INTEGER_GREATER_THAN` -> FdpTagIntegerGreaterThan * `INTEGER_GREATER_THAN_OR_EQUAL` -> FdpTagIntegerGreaterThanOrEqual * `DOUBLE_EXISTS` -> FdpTagDoubleExists * `DOUBLE_EQUALS` -> FdpTagDoubleEquals * `DOUBLE_LESS_THAN` -> FdpTagDoubleLessThan * `DOUBLE_LESS_THAN_OR_EQUAL` -> FdpTagDoubleLessThanOrEqual * `DOUBLE_GREATER_THAN` -> FdpTagDoubleGreaterThan * `DOUBLE_GREATER_THAN_OR_EQUAL` -> FdpTagDoubleGreaterThanOrEqual The element can hold these values * `DOUBLE_EQUALS` * `DOUBLE_EXISTS` * `DOUBLE_GREATER_THAN` * `DOUBLE_GREATER_THAN_OR_EQUAL` * `DOUBLE_LESS_THAN` * `DOUBLE_LESS_THAN_OR_EQUAL` * `INTEGER_EQUALS` * `INTEGER_EXISTS` * `INTEGER_GREATER_THAN` * `INTEGER_GREATER_THAN_OR_EQUAL` * `INTEGER_LESS_THAN` * `INTEGER_LESS_THAN_OR_EQUAL` * `STRING_CONTAINS_SUBSTRING` * `STRING_ENDS_WITH` * `STRING_EQUALS` * `STRING_EXISTS` * `STRING_STARTS_WITH` | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"brokenLinkDomains": [



"mydomain.com"



],



"clientSideMissingHttpCodeIsFailure": false,



"description": "for requests from shipping module",



"failingHttpCodesClientSide": "400-599",



"failingHttpCodesServerSide": "500-599",



"http404NotFoundFailureEnabled": false,



"id": "FDP_9",



"name": "shipping",



"serverSideMissingHttpCodeIsFailure": false,



"successForcingExceptionPatterns": [



{



"classPattern": "NullPointerException",



"messagePattern": ""



}



],



"tagConditions": [



{



"predicate": {



"ignoreCase": true,



"type": "STRING_EQUALS",



"value": "NG"



},



"tagKey": "myTag"



}



]



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Success. The new failure detection parameter set has been created. The response contains the ID of the new set. |
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
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/parameterSets/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/parameterSets/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The configuration has been updated. Response doesn't have a body. |
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