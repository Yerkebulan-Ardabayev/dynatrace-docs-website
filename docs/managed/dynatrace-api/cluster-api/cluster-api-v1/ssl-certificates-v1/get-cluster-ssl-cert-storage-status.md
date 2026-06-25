---
title: Get cluster SSL certificate storage status
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/ssl-certificates-v1/get-cluster-ssl-cert-storage-status
scraped: 2026-05-12T12:12:54.022593
---

# Get cluster SSL certificate storage status

# Get cluster SSL certificate storage status

* Published Dec 29, 2020

This API call retrieves the cluster SSL certificate storage status.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

BAD\_REQUEST

The certificate storage status is only available in runtime during the certificate update or upload. Once the certificate is uploaded and the node restarted, this API call will return `BAD_REQUEST` because no storage status is availabile.

## Endpoint

`/api/v1.0/onpremise/sslCertificate/store`

## Parameter

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| entityType | string | entity type, possible values = "COLLECTOR" The element can hold these values * `COLLECTOR` * `SERVER` | path | Required |
| entityId | integer | Node ID, which can be extracted from the URL in 'Node details' view. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [CertificateStoreStatus](#openapi-definition-CertificateStoreStatus) | Successful or in progress |
| **400** | [CertificateStoreStatus](#openapi-definition-CertificateStoreStatus) | Incorrect entity type |
| **404** | [CertificateStoreStatus](#openapi-definition-CertificateStoreStatus) | Status not found |
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

In this example, you check the SSL certificate storage status on `32` node of the `myManaged.cluster.com` cluster. In return you receive information on SSL certificate storage status indicating that the SSL certificate has been successfully stored.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/v1.0/onpremise/sslCertificate/store/SERVER/32" -H  "accept: application/json" -H  "Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890"
```

#### Request URL

```
https://myManaged.cluster.com/api/v1.0/onpremise/sslCertificate/store/SERVER/32
```

#### Response body

```
{



"certificateStoreStatus": "Successful",



"detailedError": null



}
```

#### Response code

`200`