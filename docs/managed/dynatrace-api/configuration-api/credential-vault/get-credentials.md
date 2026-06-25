---
title: Credential vault API - GET credentials metadata
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/credential-vault/get-credentials
scraped: 2026-05-12T12:05:32.384281
---

# Credential vault API - GET credentials metadata

# Credential vault API - GET credentials metadata

* Reference
* Published Oct 14, 2019

This API is deprecated. Use the [Credential vault API](/managed/dynatrace-api/environment-api/credential-vault "Learn what the Dynatrace API for credentials offers.") from the Environment API instead.

Gets the metadata of the specified set of credentials for [synthetic monitors](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor."). The credentials set itself (username/certificate and password) is not included in the response.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/credentials/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/credentials/{id}` |

## Authentication

To execute this request, you need an access token with `credentialVault.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The Dynatrace entity ID of the required credentials set. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [CredentialsResponseElement](#openapi-definition-CredentialsResponseElement) | Success. The response contains the metadata of the credentials set. |

### Response body objects

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



"allowContextlessRequests": "false",



"credentialUsageSummary": [



{



"BROWSER_MONITOR": 2,



"HTTP_MONITOR": 3



}



],



"description": "Sample credentials for demo purposes.",



"externalVault": {



"passwordSecretName": "password",



"pathToCredentials": "kv/credentials",



"roleId": "00e4858c-ec33-bc99-4e7e-34de6967de6c",



"secretId": "CREDENTIALS_VAULT-XXXXXXXXXXXXXXXX",



"sourceAuthMethod": "HASHICORP_VAULT_APPROLE",



"usernameSecretName": "username",



"vaultNamespace": "admin",



"vaultUrl": "https://vault-cluster.vault.fb17d2fc-be92-4230-afa2-91dbfda3cbad.aws.hashicorp.cloud:8200"



},



"id": "CREDENTIALS_VAULT-C43F2C2E6395AD23",



"name": "Sample username-password credentials",



"owner": "user@domain.com",



"ownerAccessOnly": true,



"scope": "SYNTHETIC",



"type": "USERNAME_PASSWORD"



}
```

## Example

In this example, the request fetches the metadata of the **easyTravel** credentials set with the ID of **CREDENTIALS\_VAULT-9415C41E3649FE3C**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X GET \



'https://mySampleEnv.live.dynatrace.com/api/config/v1/credentials/CREDENTIALS_VAULT-9415C41E3649FE3C' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/credentials/CREDENTIALS_VAULT-9415C41E3649FE3C
```

#### Response body

```
{



"name": "easyTravel",



"id": "CREDENTIALS_VAULT-9415C41E3649FE3C",



"type": "USERNAME_PASSWORD",



"description": "Credentials for easyTravel test app"



}
```

#### Response code

200

## Related topics

* [Configure browser monitors](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Learn about configuring browser monitors and clickpaths.")
* [Configure HTTP monitors](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Learn about configuring HTTP monitors.")