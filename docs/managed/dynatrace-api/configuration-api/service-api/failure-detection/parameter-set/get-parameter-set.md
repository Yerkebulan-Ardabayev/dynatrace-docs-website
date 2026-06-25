---
title: Failure detection API - GET a parameter set
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/failure-detection/parameter-set/get-parameter-set
scraped: 2026-05-12T11:16:27.247447
---

# Failure detection API - GET a parameter set

# Failure detection API - GET a parameter set

* Reference
* Published Jan 11, 2021

Gets the specified failure detection parameter set.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/parameterSets/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/parameterSets/{id}` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required failure detection parameter set. Needs to be a valid RFC 4122 UUID. | path | Required |

## Response

To find all model variations that depend on the type of the model, see [JSON models](/managed/dynatrace-api/configuration-api/service-api/failure-detection/json-models "Learn the variations of JSON models in the Dynatrace failure detection API.").

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [FailureDetectionParameterSet](#openapi-definition-FailureDetectionParameterSet) | Success |
| **404** | - | Failed. The specified entity doesn't exist. |

### Response body objects

#### The `FailureDetectionParameterSet` object

A set of failure detection parameters (FDP).

These parameters define the conditions of failure and success.

| Element | Type | Description |
| --- | --- | --- |
| brokenLinkDomains | string[] | A list of domains for the special handling of the 404 HTTP response code.  If the top domain of the *Referer* is presented in the list OR equals the top domain of the request's host, the 404 code is considered a failure.  Only applicable when **isHttp404NotFoundFailureEnabled** is set to `true`. |
| clientSideMissingHttpCodeIsFailure | boolean | The missing HTTP response code on the client side is a failure (`true`) or a success (`false`).  If not set, `false` is used. |
| description | string | A short description of the FDP set. |
| exceptionOnAnyNodeExceptionPatterns | [ExceptionPattern[]](#openapi-definition-ExceptionPattern) | A list of faulty exceptions.  If an exception on *any* node of the service matches *any* of these patterns it is considered a failure. |
| failingHttpCodesClientSide | string | A list of client side HTTP response codes that are considered a failure.  The format is a list of ranges and individual values (for example, `500-599, 400-499, 1008`).  If not set, the range of `400-599` is used. |
| failingHttpCodesServerSide | string | A list of server side HTTP response codes that are considered a failure.  The format is a list of ranges and individual values (for example, `500-599, 400-499, 1008`).If not set, the range of `500-599` is used. |
| http404NotFoundFailureEnabled | boolean | Special handling of the 404 HTTP response code is enabled (`true`) or disabled (`false`). See **brokenLinkDomains** for special handling details.  Only applicable when 404 is NOT in the list of failing HTTP response codes and only for the server side.  If not set, `false` is used. |
| id | string | The ID of the parameter set. |
| ignoreAllExceptions | boolean | If set to true all exceptions will be ignored. Which means defined exception patterns will not have any effect. |
| ignoreSpanFailureDetection | boolean | If set to true span failure detection will be ignored. |
| ignoredExceptionPatterns | [ExceptionPattern[]](#openapi-definition-ExceptionPattern) | A list of ignored exceptions.  If an exception on the entry node of the service matches *any* of these patterns it is ignored by failure detection. |
| name | string | The display name of the FDP set.  The length of the name is limited to 150 characters. |
| serverSideMissingHttpCodeIsFailure | boolean | The missing HTTP response code on the server side is a failure (`true`) or a success (`false`).  If not set, `false` is used. |
| successForcingExceptionPatterns | [ExceptionPattern[]](#openapi-definition-ExceptionPattern) | A list of success exceptions.  If an exception on the entry node of the service matches *any* of these patterns it is considered a success. |
| tagConditions | [FdpTagCondition[]](#openapi-definition-FdpTagCondition) | A list of tag-based conditions.  If *any* condition is fulfilled the request is considered a failure. |

#### The `ExceptionPattern` object

A list of faulty exceptions.

If an exception on *any* node of the service matches *any* of these patterns it is considered a failure.

| Element | Type | Description |
| --- | --- | --- |
| classPattern | string | - |
| messagePattern | string | - |

#### The `FdpTagCondition` object

Configuration of the tag condition in the FDP set.

| Element | Type | Description |
| --- | --- | --- |
| predicate | [FdpTagPredicate](#openapi-definition-FdpTagPredicate) | The predicate that tests the value of the tag.  The actual set of fields depends on the type of the predicate. Find the list of actual objects in the description of the **type** field or see [Failure detection API - JSON modelsï»¿](https://dt-url.net/9sg3swf). |
| tagKey | string | The key of the tag to be checked. |

#### The `FdpTagPredicate` object

The predicate that tests the value of the tag.

The actual set of fields depends on the type of the predicate. Find the list of actual objects in the description of the **type** field or see [Failure detection API - JSON modelsï»¿](https://dt-url.net/9sg3swf).

| Element | Type | Description |
| --- | --- | --- |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `STRING_EXISTS` -> FdpTagStringExists * `STRING_EQUALS` -> FdpTagStringEquals * `STRING_STARTS_WITH` -> FdpTagStringStartsWith * `STRING_ENDS_WITH` -> FdpTagStringEndsWith * `STRING_CONTAINS_SUBSTRING` -> FdpTagStringContainsSubstring * `INTEGER_EXISTS` -> FdpTagIntegerExists * `INTEGER_EQUALS` -> FdpTagIntegerEquals * `INTEGER_LESS_THAN` -> FdpTagIntegerLessThan * `INTEGER_LESS_THAN_OR_EQUAL` -> FdpTagIntegerLessThanOrEqual * `INTEGER_GREATER_THAN` -> FdpTagIntegerGreaterThan * `INTEGER_GREATER_THAN_OR_EQUAL` -> FdpTagIntegerGreaterThanOrEqual * `DOUBLE_EXISTS` -> FdpTagDoubleExists * `DOUBLE_EQUALS` -> FdpTagDoubleEquals * `DOUBLE_LESS_THAN` -> FdpTagDoubleLessThan * `DOUBLE_LESS_THAN_OR_EQUAL` -> FdpTagDoubleLessThanOrEqual * `DOUBLE_GREATER_THAN` -> FdpTagDoubleGreaterThan * `DOUBLE_GREATER_THAN_OR_EQUAL` -> FdpTagDoubleGreaterThanOrEqual The element can hold these values * `DOUBLE_EQUALS` * `DOUBLE_EXISTS` * `DOUBLE_GREATER_THAN` * `DOUBLE_GREATER_THAN_OR_EQUAL` * `DOUBLE_LESS_THAN` * `DOUBLE_LESS_THAN_OR_EQUAL` * `INTEGER_EQUALS` * `INTEGER_EXISTS` * `INTEGER_GREATER_THAN` * `INTEGER_GREATER_THAN_OR_EQUAL` * `INTEGER_LESS_THAN` * `INTEGER_LESS_THAN_OR_EQUAL` * `STRING_CONTAINS_SUBSTRING` * `STRING_ENDS_WITH` * `STRING_EQUALS` * `STRING_EXISTS` * `STRING_STARTS_WITH` |

### Response body JSON models

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