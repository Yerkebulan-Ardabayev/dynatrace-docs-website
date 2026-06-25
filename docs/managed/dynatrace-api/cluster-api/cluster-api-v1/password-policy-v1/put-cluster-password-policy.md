---
title: Update cluster password policy
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/password-policy-v1/put-cluster-password-policy
scraped: 2026-05-12T12:12:13.307907
---

# Update cluster password policy

# Update cluster password policy

* Published Nov 18, 2020

This API call updates a cluster password policy.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/passwordPolicy`

## Parameter

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [PasswordPolicy](#openapi-definition-PasswordPolicy) | The JSON body of the request. Contains parameters of password policy configuration. | body | Optional |

### Request body objects

#### The `PasswordPolicy` object

Password policy configuration.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| minNumberOfDigits | integer | Minimum number of digits | Required |
| minNumberOfLowercaseChars | integer | Minimum number of lowercase characters | Required |
| minNumberOfNonAlphanumericChars | integer | Minimum number of non-alphanumeric characters | Required |
| minNumberOfUppercaseChars | integer | Minimum number of uppercase characters | Required |
| minPasswordLength | integer | Minimum password length | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"minNumberOfDigits": 1,



"minNumberOfLowercaseChars": 1,



"minNumberOfNonAlphanumericChars": 1,



"minNumberOfUppercaseChars": 1,



"minPasswordLength": 1



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Successfully updated. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **404** | - | Realm not found |

### Response body objects

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

In this example, you update the password policy for your managed deployment (`myManaged.cluster.com`). You define:

* Minimum password length
* Minimum number of uppercase characters
* Minimum number of lowercase characters
* Minimum number of digits
* Minimum number of non-alphanumeric characters

In return you receive a response code `204` indicating that the password policy was updated successfully.

#### Curl

```
curl -X PUT "https://myManaged.cluster.com/api/v1.0/onpremise/passwordPolicy" -H  "accept: */*" -H  "Content-Type: application/json" -d "{\"realmId\":\"string\",\"minPasswordLength\":16,\"minNumberOfUppercaseChars\":2,\"minNumberOfLowercaseChars\":4,\"minNumberOfDigits\":2,\"minNumberOfNonAlphanumericChars\":4}"
```

#### Request URL

```
https://myManaged.cluster.com/api/v1.0/onpremise/passwordPolicy
```

#### Response body

Successfully updated. Response doesn't have a body.

#### Response code

`204`