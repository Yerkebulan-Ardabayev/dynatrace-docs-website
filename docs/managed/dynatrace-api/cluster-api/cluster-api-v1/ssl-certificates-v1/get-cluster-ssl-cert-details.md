---
title: Get cluster SSL certificate details
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/ssl-certificates-v1/get-cluster-ssl-cert-details
scraped: 2026-05-12T12:12:57.209191
---

# Get cluster SSL certificate details

# Get cluster SSL certificate details

* Published Dec 29, 2020

This API call retrieves cluster SSL certificate details.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/sslCertificate`

## Parameter

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| entityType | string | entity type, possible values = "SERVER, COLLECTOR" The element can hold these values * `COLLECTOR` * `SERVER` | path | Required |
| entityId | integer | Node ID, which can be extracted from the URL in 'Node details' view. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SSLDetails](#openapi-definition-SSLDetails) | Success |
| **500** | - | Internal server error. |

### Response body objects

#### The `SSLDetails` object

| Element | Type | Description |
| --- | --- | --- |
| customKeyStore | boolean | - |
| customKeyStoreWritable | boolean | - |
| default | boolean | - |
| expirationDate | string | - |
| inProgress | boolean | - |
| issuer | string | - |
| restartRequired | boolean | - |
| subject | string | - |

### Response body JSON models

```
{



"customKeyStore": true,



"customKeyStoreWritable": true,



"default": true,



"expirationDate": "string",



"inProgress": true,



"issuer": "string",



"restartRequired": true,



"subject": "string"



}
```

## Example

In this example, you check the SSL certificate details on `32` node of the `myManaged.cluster.com` cluster. In return you receive information on current SSL certificate.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/v1.0/onpremise/sslCertificate/SERVER/32" -H  "accept: application/json" -H  "Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890"
```

#### Request URL

```
https://myManaged.cluster.com/api/v1.0/onpremise/sslCertificate/SERVER/32
```

#### Response body

```
{



"issuer": "EV SSL Intermediate CA RSA",



"subject": "n32.myManaged.cluster.com",



"expirationDate": 1615956886000,



"customKeyStore": false,



"customKeyStoreWritable": true,



"inProgress": false,



"restartRequired": false,



"default": false



}
```

#### Response code

`200`