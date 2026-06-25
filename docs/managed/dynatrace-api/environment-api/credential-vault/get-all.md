---
title: Credential vault API - GET all credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/credential-vault/get-all
scraped: 2026-05-12T11:54:23.968569
---

# Credential vault API - GET all credentials

# Credential vault API - GET all credentials

* Reference
* Published Oct 06, 2022

Lists all credentials for [synthetic monitors](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.") stored in your environment.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/credentials` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/credentials` |

## Authentication

To execute this request, you need an access token with `credentialVault.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| type | string | Filters the result by the specified credentials type. The element can hold these values * `CERTIFICATE` * `USERNAME_PASSWORD` * `TOKEN` * `SNMPV3` * `AWS_MONITORING_KEY_BASED` * `AWS_MONITORING_ROLE_BASED` | query | Optional |
| name | string | Filters the result by the name. When in quotation marks, whole phrase is taken. Case insensitive. | query | Optional |
| user | string | Filters credentials accessible to the user (owned by the user or the ones that are accessible for all). | query | Optional |
| scope | string | Filters credentials with specified scope. | query | Optional |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **nextPageKey** field of the previous response.  The first page is always returned if you don't specify the **nextPageKey** query parameter.  When the **nextPageKey** is set to obtain subsequent pages, you must omit all other query parameters. | query | Optional |
| pageSize | integer | The amount of credentials in a single response payload.  The maximal allowed page size is 500.  If not set, 100 is used. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [CredentialsList](#openapi-definition-CredentialsList) | Success |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `CredentialsList` object

A list of credentials sets for Synthetic monitors.

| Element | Type | Description |
| --- | --- | --- |
| credentials | [CredentialsResponseElement[]](#openapi-definition-CredentialsResponseElement) | A list of credentials sets for Synthetic monitors. |
| nextPageKey | string | - |
| pageSize | integer | - |
| totalCount | integer | - |

#### The `CredentialsResponseElement` object

Metadata of the credentials set.

| Element | Type | Description |
| --- | --- | --- |
| allowContextlessRequests | boolean | Allow access without app context, for example, from ad hoc functions in Workflows (requires the APP\_ENGINE scope). |
| allowedEntities | [CredentialAccessData[]](#openapi-definition-CredentialAccessData) | The set of entities allowed to use the credential. |
| credentialUsageSummary | [CredentialUsageHandler[]](#openapi-definition-CredentialUsageHandler) | The list contains summary data related to the use of credentials. |
| description | string | A short description of the credentials set. |
| externalVault | [ExternalVaultConfig](#openapi-definition-ExternalVaultConfig) | Configuration for external vault synchronization for username and password credentials. |
| id | string | The ID of the credentials set. |
| name | string | The name of the credentials set. |
| owner | string | The owner of the credential (user for which used API token was created). |
| ownerAccessOnly | boolean | Flag indicating that this credential is visible only to the owner. |
| scope | string | The scope of the credentials set. The element can hold these values * `APP_ENGINE` * `EXTENSION` * `SYNTHETIC` |
| scopes | string[] | The set of scopes of the credentials set. The element can hold these values * `APP_ENGINE` * `EXTENSION` * `SYNTHETIC` |
| type | string | The type of the credentials set. The element can hold these values * `AWS_MONITORING_KEY_BASED` * `AWS_MONITORING_ROLE_BASED` * `CERTIFICATE` * `PUBLIC_CERTIFICATE` * `SNMPV3` * `TOKEN` * `UNKNOWN` * `USERNAME_PASSWORD` |

#### The `CredentialAccessData` object

The set of entities allowed to use the credential.

| Element | Type | Description |
| --- | --- | --- |
| id | string | - |
| type | string | -The element can hold these values * `APPLICATION` * `UNKNOWN` * `USER` |

#### The `CredentialUsageHandler` object

Keeps information about credential's usage.

| Element | Type | Description |
| --- | --- | --- |
| count | integer | The number of uses. |
| type | string | Type of usage. |

#### The `ExternalVaultConfig` object

Configuration for external vault synchronization for username and password credentials.

| Element | Type | Description |
| --- | --- | --- |
| credentialsUsedForExternalSynchronization | string[] | - |
| passwordSecretName | string | - |
| sourceAuthMethod | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `HASHICORP_VAULT_APPROLE` -> HashicorpApproleConfig * `HASHICORP_VAULT_CERTIFICATE` -> HashicorpCertificateConfig * `AZURE_KEY_VAULT_CLIENT_SECRET` -> AzureClientSecretConfig * `CYBERARK_VAULT_USERNAME_PASSWORD` -> CyberArkUsernamePasswordConfig * `CYBERARK_VAULT_ALLOWED_LOCATION` -> CyberArkAllowedLocationConfig The element can hold these values * `AZURE_KEY_VAULT_CLIENT_SECRET` * `CYBERARK_VAULT_ALLOWED_LOCATION` * `CYBERARK_VAULT_USERNAME_PASSWORD` * `HASHICORP_VAULT_APPROLE` * `HASHICORP_VAULT_CERTIFICATE` |
| tokenSecretName | string | - |
| type | string | -The element can hold these values * `AZURE_CERTIFICATE_MODEL` * `AZURE_CLIENT_SECRET_MODEL` * `CYBERARK_VAULT_ALLOWED_LOCATION_MODEL` * `CYBERARK_VAULT_USERNAME_PASSWORD_MODEL` * `HASHICORP_APPROLE_MODEL` * `HASHICORP_CERTIFICATE_MODEL` |
| usernameSecretName | string | - |
| vaultUrl | string | - |

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



"credentials": [



{



"credentialUsageSummary": [



{



"HTTP_MONITOR": 4



}



],



"description": "Sample credentials for demo purposes",



"id": "CREDENTIALS_VAULT-E80203F993472E6D",



"name": "Sample username-password credentials",



"owner": "admin",



"ownerAccessOnly": true,



"scope": "SYNTHETIC",



"type": "USERNAME_PASSWORD"



},



{



"credentialUsageSummary": [],



"description": "Sample credentials for demo purposes",



"id": "CREDENTIALS_VAULT-842DEF439999E15B",



"name": "Sample certificate credentials",



"owner": "John.Doe@domain.com",



"ownerAccessOnly": true,



"scope": "EXTENSION",



"type": "CERTIFICATE"



},



{



"credentialUsageSummary": [



{



"BROWSER_MONITOR": 11,



"HTTP_MONITOR": 4



}



],



"description": "Sample token for demo purposes",



"id": "CREDENTIALS_VAULT-854345639999E15B",



"name": "Sample token credentials",



"owner": "John.Doe@domain.com",



"ownerAccessOnly": true,



"scope": "SYNTHETIC",



"type": "TOKEN"



},



{



"awsPartition": "CHINA",



"description": "Sample AWS credentials for demo purposes",



"id": "CREDENTIALS_VAULT-12ABB17F0D93F8AF",



"name": "Sample AWS key based credentials",



"owner": "John.Doe@domain.com",



"ownerAccessOnly": true,



"scopes": [



"CLOUDS_MONITORING_AUTHENTICATION"



],



"type": "AWS_MONITORING_KEY_BASED"



},



{



"accountID": "123456789012",



"description": "Sample AWS credentials for demo purposes",



"externalID": "21cf07eb-4812-4de7-d5b9-6189c5951ad4",



"iamRole": "Dynatrace_monitoring_role",



"id": "CREDENTIALS_VAULT-08D0C2A011411D64",



"name": "Sample AWS role based credentials",



"owner": "John.Doe@domain.com",



"ownerAccessOnly": true,



"scopes": [



"CLOUDS_MONITORING_AUTHENTICATION"



],



"type": "AWS_MONITORING_ROLE_BASED"



}



]



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

## Related topics

* [Configure browser monitors](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Learn about configuring browser monitors and clickpaths.")
* [Configure HTTP monitors](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Learn about configuring HTTP monitors.")