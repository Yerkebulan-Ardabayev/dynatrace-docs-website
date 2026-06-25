---
title: Credential vault API - GET all credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/credential-vault/get-all
scraped: 2026-05-12T12:05:34.398026
---

# Credential vault API - GET all credentials

# Credential vault API - GET all credentials

* Reference
* Published Oct 14, 2019

This API is deprecated. Use the [Credential vault API](/managed/dynatrace-api/environment-api/credential-vault "Learn what the Dynatrace API for credentials offers.") from the Environment API instead.

Lists all credentials for [synthetic monitors](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.") stored in your environment.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/credentials` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/credentials` |

## Authentication

To execute this request, you need an access token with `credentialVault.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| type | string | Filters the result by the specified credentials type. The element can hold these values * `CERTIFICATE` * `USERNAME_PASSWORD` * `TOKEN` * `SNMPV3` | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [CredentialsList](#openapi-definition-CredentialsList) | Success |

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

## Example

In this example, the request lists all credentials of the **USERNAME\_PASSWORD** type from the **mySampleEnv** environment.

The API token is passed in the **Authorization** header.

The result is truncated to two entries.

#### Curl

```
curl -X GET \



'https://mySampleEnv.live.dynatrace.com/api/config/v1/credentials/?type=USERNAME_PASSWORD' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/credentials/?type=USERNAME_PASSWORD
```

#### Response body

```
{



"credentials": [



{



"name": "easyTravel",



"id": "CREDENTIALS_VAULT-9415C41E3649FE3C",



"type": "USERNAME_PASSWORD",



"description": "Credentials for easyTravel test app"



},



{



"name": "google.com",



"id": "CREDENTIALS_VAULT-E6D8ED717C9689B2",



"type": "USERNAME_PASSWORD",



"description": "google.com"



}



]



}
```

#### Response code

200

## Related topics

* [Configure browser monitors](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Learn about configuring browser monitors and clickpaths.")
* [Configure HTTP monitors](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Learn about configuring HTTP monitors.")