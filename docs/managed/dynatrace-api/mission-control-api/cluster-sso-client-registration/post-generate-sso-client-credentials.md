---
title: Generate SSO client credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/mission-control-api/cluster-sso-client-registration/post-generate-sso-client-credentials
---

# Generate SSO client credentials

# Generate SSO client credentials

* Published Mar 12, 2021

This API call generates an `OAuth API client`.

You can create up to `100` OAuth API clients per account. We recommend that you reuse once created OAuth API client.

## Endpoint

`/public/v1.0/oauth/registration/withLicenseKey`

## Parameter

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| clientType | string | - | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ClientCredentialsDto](#openapi-definition-ClientCredentialsDto) | Cluster credentials generated successfully |
| **401** | - | Invalid cluster credentials |

### Response body objects

#### The `ClientCredentialsDto` object

| Element | Type | Description |
| --- | --- | --- |
| clientId | string | - |
| clientSecret | string | - |
| scopes | string[] | - |

### Response body JSON models

```
{



"clientId": "string",



"clientSecret": "string",



"scopes": [



"string"



]



}
```

## Example

In this example, you generate an `OAuth API client` execute following REST call.

where :

* `<cluster-identifier>` is a cluster identifier (in Dynatrace, go to **Licensing**). For example, `0a00a0a0-92ec-11e7-b1e6-12fbd1fb3732`
* `<license-key>` is a license key provided to you in welcome email and visible in **Licensing**. For example, `0a0aAAAA0jeUv6N`.

#### Curl

```
curl -X POST "https://mcsvc.dynatrace.com/rest/public/v1.0/oauth/registration/withLicenseKey"



-H "accept: application/json"



-u "<cluster-identifier>:<license-key>"
```

#### Request URL

```
https://mcsvc.dynatrace.com/rest/public/v1.0/oauth/registration/withLicenseKey
```

#### Response body

```
{



"clientId": "dt0s04.AAAAAAAA",



"clientSecret": "dt0s04.AAAAAAAA.AAAA00AAAAAAAAAA0OBA6AVNCQVQAGSO25VM5KDFBIKEZ7HVG6THKTHGWAY5ACCL",



"scopes": [



"sso20-managed-cluster-offline-bundle",



"sso20-identity-linking"



]



}
```

#### Response code

`200`