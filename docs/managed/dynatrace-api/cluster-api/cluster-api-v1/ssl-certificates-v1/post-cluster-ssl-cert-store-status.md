---
title: Store cluster SSL certificate
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/ssl-certificates-v1/post-cluster-ssl-cert-store-status
scraped: 2026-05-12T12:01:04.935094
---

# Store cluster SSL certificate

# Store cluster SSL certificate

* Published Nov 18, 2020

This API call stores a cluster SSL certificate.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/sslCertificate/store`

## Parameter

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| entityType | string | entity type, possible values = "SERVER, COLLECTOR" The element can hold these values * `COLLECTOR` * `SERVER` | path | Required |
| entityId | integer | Node ID, which can be extracted from the URL in 'Node details' view. | path | Required |
| body | [sslCertDto](#openapi-definition-sslCertDto) | SSL certificate configuration. | body | Optional |

### Request body objects

#### The `sslCertDto` object

SSL certificate configuration.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| certificateChainEncoded | string | Certificate(s) X.509 standard, PEM base64-encoded format, intermediate and root certificates | Optional |
| privateKeyEncoded | string | Private key PKCS #8 standard, PEM base64-encoded format | Required |
| publicKeyCertificateEncoded | string | Certificate X.509 standard, PEM base64-encoded format, server certificate | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"certificateChainEncoded": "-----BEGIN CERTIFICATE-----\nMIIDKT...XbTK+M\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIDKT...bXTK+M\n-----END CERTIFICATE-----",



"privateKeyEncoded": "-----BEGIN RSA PRIVATE KEY-----\nMIIEow...aHzMvp\n-----END RSA PRIVATE KEY-----",



"publicKeyCertificateEncoded": "-----BEGIN CERTIFICATE-----\nMIIDKT...XbTK+M\n-----END CERTIFICATE-----"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [CertificateStoreStatus](#openapi-definition-CertificateStoreStatus) | Successful or in progress |
| **400** | [CertificateStoreStatus](#openapi-definition-CertificateStoreStatus) | Incorrect entity type |
| **500** | - | Internal error |
| **522** | [CertificateStoreStatus](#openapi-definition-CertificateStoreStatus) | Certificate chain is invalid |
| **523** | [CertificateStoreStatus](#openapi-definition-CertificateStoreStatus) | Private key does not match public key certificate |
| **525** | [CertificateStoreStatus](#openapi-definition-CertificateStoreStatus) | Public key certificate is invalid |
| **526** | [CertificateStoreStatus](#openapi-definition-CertificateStoreStatus) | Private key is invalid |
| **527** | [CertificateStoreStatus](#openapi-definition-CertificateStoreStatus) | Error while storing SSL certificate |
| **528** | [CertificateStoreStatus](#openapi-definition-CertificateStoreStatus) | Certificate has been stored but has not been refreshed |
| **529** | [CertificateStoreStatus](#openapi-definition-CertificateStoreStatus) | Internal error |

### Response body objects

#### The `CertificateStoreStatus` object

| Element | Type | Description |
| --- | --- | --- |
| certificateStoreStatus | string | -The element can hold these values * `BAD_REQUEST` * `CERTIFICATE_CHAIN_IS_INVALID` * `CERTIFICATE_IS_EXPIRED` * `CERTIFICATE_STORED_BUT_NOT_REFRESHED` * `ERROR` * `GENERAL_ERROR_WHILE_STORING_CERTIFICATE` * `IN_PROGRESS` * `NOT_FOUND` * `OK` * `PRIVATE_KEY_DOES_NOT_MATCH_PUBLIC_KEY_CERTIFICATE` * `PRIVATE_KEY_IS_INVALID` * `PUBLIC_KEY_CERTIFICATE_IS_INVALID` |
| detailedError | string | - |

#### The `CertificateStoreStatus` object

| Element | Type | Description |
| --- | --- | --- |
| certificateStoreStatus | string | -The element can hold these values * `BAD_REQUEST` * `CERTIFICATE_CHAIN_IS_INVALID` * `CERTIFICATE_IS_EXPIRED` * `CERTIFICATE_STORED_BUT_NOT_REFRESHED` * `ERROR` * `GENERAL_ERROR_WHILE_STORING_CERTIFICATE` * `IN_PROGRESS` * `NOT_FOUND` * `OK` * `PRIVATE_KEY_DOES_NOT_MATCH_PUBLIC_KEY_CERTIFICATE` * `PRIVATE_KEY_IS_INVALID` * `PUBLIC_KEY_CERTIFICATE_IS_INVALID` |
| detailedError | string | - |

### Response body JSON models

```
{



"certificateStoreStatus": "BAD_REQUEST",



"detailedError": "string"



}
```

```
{



"certificateStoreStatus": "BAD_REQUEST",



"detailedError": "string"



}
```

## Example

In this example, you store the SSL certificate on `32` node of the `myManaged.cluster.com` cluster. In return you receive information that the SSL certificate was successfully updated. Make sure that your request is in JSON format. This means that the `privateKeyEncoded`, `publicKeyCertificateEncoded` and `certificateChainEncoded` objects are in a single line.

#### Curl

```
curl -X POST "https://myManaged.cluster.com/api/v1.0/onpremise/sslCertificate/store/SERVER/32" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"privateKeyEncoded\":\"-----BEGIN RSA PRIVATE KEY-----\MIIEow...aHzMvp\-----END RSA PRIVATE KEY-----\",\"publicKeyCertificateEncoded\":\"-----BEGIN CERTIFICATE-----\MIIDKT...XbTK+M\-----END CERTIFICATE-----\",\"certificateChainEncoded\":\"-----BEGIN CERTIFICATE-----\MIIDKT...XbTK+M\-----END CERTIFICATE-----\-----BEGIN CERTIFICATE-----\MIIDKT...bXTK+M\-----END CERTIFICATE-----\"}"
```

#### Request URL

```
https://myManaged.cluster.com/api/v1.0/onpremise/sslCertificate/store/SERVER/32
```

#### Response body

Successfully updated. Response doesn't have a body.

#### Response code

`200`