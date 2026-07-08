---
title: Generate SSO token
source: https://docs.dynatrace.com/managed/dynatrace-api/mission-control-api/cluster-sso-token-generation/post-generate-sso-token
---

# Generate SSO token

# Generate SSO token

* Published Mar 12, 2021

This API call generates a token that allows you to execute update package download URLs.

## Endpoint

`/public/v1.0/oauth/api-token`

## Parameter

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [TokenGrantCredentialsDto](#openapi-definition-TokenGrantCredentialsDto) | - | body | Optional |

### Request body objects

#### The `TokenGrantCredentialsDto` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| clientId | string | - | Optional |
| clientSecret | string | - | Optional |
| scope | string | - | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"clientId": "string",



"clientSecret": "string",



"scope": "string"



}
```

## Response

### Response codes

| Code | Description |
| --- | --- |
| **200** | Token generated successfully |
| **401** | Invalid credentials |
| **404** | Cluster not found |

## Example

In this example, you generate a token execute following REST call:

#### Curl

```
curl -X POST "https://mcsvc.dynatrace.com/rest/public/v1.0/oauth/api-token"



-H "accept: application/json"



-H "Content-Type: application/json"



-d "{ \"clientId\": \"dt0s04.AAAAAAAA\", \"clientSecret\": \"dt0s04.AAAAAAAA.AAAA00AAAAAAAAAA0OBA6AVNCQVQAGSO25VM5KDFBIKEZ7HVG6THKTHGWAY5ACCL\", \"scope\": \"sso20-managed-cluster-offline-bundle\"}"
```

#### Request URL

```
https://mcsvc.dynatrace.com/rest/public/v1.0/oauth/api-token
```

#### Response body

```
{



"token": "aaA0aAAaAaAAA0AaAAAaaAaaAaAAAaA0AaA0.eyJzdWIiOiJjbHVzdGVyLTBhMDBhMGEwLTkyZWMtMTFlNy1iMWU2LTEyZmJkMWZiMzczMkBkeW5hdHJhY2UtbWFuYWdlZC5jb20iLCJhdWQiOiJkdDBzMDQuTFFWT1FQQVMiLCJ1aWQiOiI5N2Y0OGFhMy1jYmRiLTRkMzEtOGE2YS02NjUyNTQxMzY5MTIiLCJzY29wZSI6InNzbzIwLW1hbmFnZWQtY2x1c3Rlci1vZmZsaW5lLWJ1bmRsZSIsImlzcyI6Imh0dHBzOi8vc3NvLXNwcmludC5keW5hdHJhY2VsYWJzLmNvbTo0NDMiLCJleHAiOjE2MTU0NzcxNTIsImdyYW50VHlwZSI6ImNsaWVudF9jcmVkZW50aWFscyIsImlhdCI6MTYxNTQ2OTk1Mn0.svn34bJEZbziHVyV7cKW9OWwvBwakzH0Ke_Iu19GV743zrC4zHuX4YQFts-JkEHRYmnVvnQRwPPCakuq0LHVjA",



"scopes": [



"sso20-managed-cluster-offline-bundle"



],



"expiresAt": 1615477153001



}
```

#### Response code

`200`