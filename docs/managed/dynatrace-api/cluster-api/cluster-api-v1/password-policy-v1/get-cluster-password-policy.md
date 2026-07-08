---
title: Get cluster password policy
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/password-policy-v1/get-cluster-password-policy
---

# Get cluster password policy

# Get cluster password policy

* Published Nov 18, 2020

This API call retrieves a cluster password policy.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/passwordPolicy`

## Parameter

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [PasswordPolicy](#openapi-definition-PasswordPolicy) | Success |
| **404** | - | Realm not found |

### Response body objects

#### The `PasswordPolicy` object

Password policy configuration.

| Element | Type | Description |
| --- | --- | --- |
| minNumberOfDigits | integer | Minimum number of digits |
| minNumberOfLowercaseChars | integer | Minimum number of lowercase characters |
| minNumberOfNonAlphanumericChars | integer | Minimum number of non-alphanumeric characters |
| minNumberOfUppercaseChars | integer | Minimum number of uppercase characters |
| minPasswordLength | integer | Minimum password length |

### Response body JSON models

```
{



"minNumberOfDigits": 1,



"minNumberOfLowercaseChars": 1,



"minNumberOfNonAlphanumericChars": 1,



"minNumberOfUppercaseChars": 1,



"minPasswordLength": 1



}
```

## Example

In this example, you query your managed deployment (`myManaged.cluster.com`) for its password policy. In return you receive information on current password policy settings.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/v1.0/onpremise/passwordPolicy" -H  "accept: application/json"
```

#### Request URL

```
https://myManaged.cluster.com/api/v1.0/onpremise/passwordPolicy
```

#### Response body

```
{



"realmId": "string",



"minPasswordLength": 12,



"minNumberOfUppercaseChars": 1,



"minNumberOfLowercaseChars": 1,



"minNumberOfDigits": 1,



"minNumberOfNonAlphanumericChars": 10



}
```

#### Response code

`200`