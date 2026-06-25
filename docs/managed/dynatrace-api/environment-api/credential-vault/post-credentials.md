---
title: Credential vault API - POST a set of credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/credential-vault/post-credentials
scraped: 2026-05-12T11:54:25.960676
---

# Credential vault API - POST a set of credentials

# Credential vault API - POST a set of credentials

* Reference
* Published Oct 14, 2019

Creates a new set of credentials for [synthetic monitors](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.").

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/credentials` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/credentials` |

## Authentication

To execute this request, you need an access token with `credentialVault.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

Refer to [JSON models](/managed/dynatrace-api/environment-api/credential-vault/models "Learn the variations of credential set JSON models in the Dynatrace API.") to find all JSON models that depend on the type of the model.

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [Credentials](#openapi-definition-Credentials) | The JSON body of the request. Contains parameters of the new credentials set. | body | Required |

### Request body objects

#### The `Credentials` object

A set of credentials for synthetic monitors.

The actual set of fields depends on the type of credentials. Find the list of actual objects in the description of the **type** field or see [Credential vault API - JSON modelsï»¿](https://dt-url.net/2sa3sen).

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| allowContextlessRequests | boolean | Allow ad-hoc functions to access the credential details (requires the APP\_ENGINE scope). | Optional |
| allowedEntities | [CredentialAccessData[]](#openapi-definition-CredentialAccessData) | The set of entities allowed to use the credential. | Optional |
| description | string | A short description of the credentials set. | Optional |
| id | string | The ID of the credentials set. | Optional |
| name | string | The name of the credentials set. | Required |
| ownerAccessOnly | boolean | The credentials set is available to every user (`false`) or to owner only (`true`). | Optional |
| ~~scope~~ | string | DEPRECATED  The scope of the credentials set. The element can hold these values * `APP_ENGINE` * `EXTENSION` * `SYNTHETIC` | Optional |
| scopes | string[] | The set of scopes of the credentials set.  Limitations: `CredentialsScope.APP_ENGINE` is only available on the new Dynatrace SaaS platform - it's not available on managed or non-Grail SaaS environments. The element can hold these values * `APP_ENGINE` * `EXTENSION` * `SYNTHETIC` | Required |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `CERTIFICATE` -> CertificateCredentials * `PUBLIC_CERTIFICATE` -> PublicCertificateCredentials * `USERNAME_PASSWORD` -> UserPasswordCredentials * `TOKEN` -> TokenCredentials * `SNMPV3` -> SNMPV3Credentials * `AWS_MONITORING_KEY_BASED` -> AWSKeyBasedCredentialsDto * `AWS_MONITORING_ROLE_BASED` -> AWSRoleBasedCredentials The element can hold these values * `AWS_MONITORING_KEY_BASED` * `AWS_MONITORING_ROLE_BASED` * `CERTIFICATE` * `PUBLIC_CERTIFICATE` * `SNMPV3` * `TOKEN` * `USERNAME_PASSWORD` | Required |

#### The `CredentialAccessData` object

The set of entities allowed to use the credential.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| id | string | - | Optional |
| type | string | -The element can hold these values * `APPLICATION` * `UNKNOWN` * `USER` | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"allowContextlessRequests": "false",



"allowedEntities": [



{



"id": "jane.doe@example.com",



"type": "USER"



},



{



"id": "john.smith@example.com",



"type": "USER"



},



{



"id": "my.with.credentials",



"type": "APPLICATION"



}



],



"description": "Sample set of credentials for API documentation",



"name": "Sample credentials",



"ownerAccessOnly": false,



"password": "1234abcd",



"scope": "SYNTHETIC",



"scopes": [



"SYNTHETIC",



"EXTENSION_AUTHENTICATION"



],



"type": "USERNAME_PASSWORD",



"user": "john.smith@example.com"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [CredentialsId](#openapi-definition-CredentialsId) | Success. The new credentials set has been created. The response contains the ID of the set. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `CredentialsId` object

A short representation of the credentials set.

| Element | Type | Description |
| --- | --- | --- |
| id | string | The ID of the credentials set. |

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



"id": "CREDENTIALS_VAULT-C43F2C2E6395AD23"



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

## Example

In this example, the request creates a new set of credentials of the **USERNAME\_PASSWORD** type. The username of the credentials set is **john.smith** and the password is **abcd1234**.

The API token is passed in the **Authorization** header.

You can download or copy the example request body to try it out on your own.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/config/v1/credentials/ \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"name": "RESTtest",



"description": "Test credentials",



"password": "abcd1234",



"ownerAccessOnly": true,



"type": "USERNAME_PASSWORD",



"certificate": "john.smith"



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/credentials/
```

#### Request body

```
{



"name": "RESTtest",



"description": "Test credentials",



"password": "abcd1234",



"ownerAccessOnly": true,



"type": "USERNAME_PASSWORD",



"user": "john.smith"



}
```

#### Response body

```
{



"id": "CREDENTIALS_VAULT-1E6EA5075AF7E85D"



}
```

#### Response code

200

## Related topics

* [Configure browser monitors](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Learn about configuring browser monitors and clickpaths.")
* [Configure HTTP monitors](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Learn about configuring HTTP monitors.")