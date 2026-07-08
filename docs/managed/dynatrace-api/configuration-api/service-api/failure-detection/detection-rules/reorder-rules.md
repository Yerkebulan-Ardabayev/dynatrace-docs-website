---
title: Failure detection API - PUT reorder rules
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/failure-detection/detection-rules/reorder-rules
---

# Failure detection API - PUT reorder rules

# Failure detection API - PUT reorder rules

* Reference
* Published Jan 11, 2021

Reorders the failure detection rules according to the order of the IDs in the body of the request.

Rules that are omitted from the body of the request retain their relative order but are placed after all those present in the request.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/rules/reorderRules` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/rules/reorderRules` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [FdpSelectionRuleOrder](#openapi-definition-FdpSelectionRuleOrder) | The JSON body of the request. Contains the failure detection rules in the required order. | body | Required |

### Request body objects

#### The `FdpSelectionRuleOrder` object

The order of the rules in the ruleset.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| ruleIds | string[] | A list of the rule IDs. The rules in the ruleset are arranged such that their IDs form the same sequence as this list. The ID of each rule in the ruleset must occur exactly once in the list. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"ruleIds": [



"R1",



"RZa",



"RZb"



]



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | - | Success |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

### Response body objects

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