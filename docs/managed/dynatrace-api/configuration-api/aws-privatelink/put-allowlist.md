---
title: AWS PrivateLink API - PUT allowlist
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/aws-privatelink/put-allowlist
---

# AWS PrivateLink API - PUT allowlist

# AWS PrivateLink API - PUT allowlist

* Reference
* Published Nov 19, 2020

Adds an AWS account to the allowlist of AWS PrivateLink.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/privateLink/allowlistedAccounts/{id}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/privateLink/allowlistedAccounts/{id}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The AWS account id to be updated in the AWS PrivateLink allowlist, has to match the id in the provided payload. | path | Required |
| body | [AllowlistedAwsAccount](#openapi-definition-AllowlistedAwsAccount) | The AWS account id to be updated in the AWS PrivateLink allowlist, has to match the id in the path. | body | Required |

### Request body objects

#### The `AllowlistedAwsAccount` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| id | string | The AWS account id to allowlist | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"id": "string"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [AllowlistedAwsAccount](#openapi-definition-AllowlistedAwsAccount) | Success. The account id has been added to the PrivateLink allowlist. |
| **204** | - | Success. The account id already exists in the PrivateLink allowlist. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Error. Wrong format of the provided AWS account id (length = 12 characters, only digits). |

### Response body objects

#### The `AllowlistedAwsAccount` object

| Element | Type | Description |
| --- | --- | --- |
| id | string | The AWS account id to allowlist |

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



"id": "string"



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