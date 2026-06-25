---
title: Credential vault API - JSON models
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/credential-vault/models
scraped: 2026-05-12T12:13:33.488288
---

# Credential vault API - JSON models

# Credential vault API - JSON models

* Reference
* Published Oct 14, 2019

This API is deprecated. Use the [Credential vault API](/managed/dynatrace-api/environment-api/credential-vault "Learn what the Dynatrace API for credentials offers.") from the Environment API instead.

JSON models of the **Credential vault** API vary depending on the **type** of the object. Here you can find JSON models for each variation.

## Variations of the `Credentials` object

The `Credentials` object is the base for all credentials. The actual set of fields depends on the **type** of the credentials.

### CERTIFICATE

CertificateCredentials

Parameters

JSON model

#### The `CertificateCredentials` object

A credentials set of the `CERTIFICATE` type.

| Element | Type | Description |
| --- | --- | --- |
| certificate | string | String containing the certificate file bytes encoded in Base64 without carriage return. |
| certificateFormat | string | The certificate format. Use `PEM` for PEM certificates and `PKCS12` for PFX and P12 certificates. The element can hold these values * `PEM` * `PKCS12` * `UNKNOWN` |
| password | string | The password of the credential encoded in Base64. Must be empty for `PEM` certificates. |

```
{



"name": "string",



"id": "string",



"description": "string",



"password": "string",



"ownerAccessOnly": true,



"type": "CERTIFICATE",



"certificate": "string"



}
```

Use the following unix command to convert password string to Base64:

```
echo -n testPassword | base64
```

Use the following unix command to convert certificate file to Base64:

```
base64 -i myCertFile.pfx
```

### PUBLIC\_CERTIFICATE

PublicCertificateCredentials

Parameters

JSON model

#### The `PublicCertificateCredentials` object

A credentials set of the `PUBLIC_CERTIFICATE` type.

| Element | Type | Description |
| --- | --- | --- |
| certificate | string | The certificate in the string format. |
| certificateFormat | string | The certificate format. The element can hold these values * `PEM` * `PKCS12` * `UNKNOWN` |
| password | string | The password of the credential (not supported). |

```
{



"name": "string",



"id": "string",



"description": "string",



"password": "string",



"ownerAccessOnly": true,



"type": "CERTIFICATE",



"certificate": "string"



}
```

### TOKEN

TokenCredentials

Parameters

JSON model

#### The `TokenCredentials` object

A credentials set of the `TOKEN` type.

| Element | Type | Description |
| --- | --- | --- |
| externalVault | [ExternalVault](#openapi-definition-ExternalVault) | Information for synchronization credentials with external vault |
| token | string | Token in the string format. |

#### The `ExternalVault` object

Information for synchronization credentials with external vault

| Element | Type | Description |
| --- | --- | --- |
| locationForSynchronizationId | string | Id of a location used by the synchronizing monitor |
| passwordSecretName | string | The name of the secret saved in external vault where password is stored. |
| sourceAuthMethod | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `HASHICORP_VAULT_APPROLE` -> HashicorpApprole * `HASHICORP_VAULT_CERTIFICATE` -> HashicorpCertificate * `AZURE_KEY_VAULT_CLIENT_SECRET` -> AzureClientSecret * `CYBERARK_VAULT_USERNAME_PASSWORD` -> CyberArkUsernamePassword * `CYBERARK_VAULT_ALLOWED_LOCATION` -> CyberArkAllowedLocationDto The element can hold these values * `AZURE_KEY_VAULT_CLIENT_SECRET` * `CYBERARK_VAULT_ALLOWED_LOCATION` * `CYBERARK_VAULT_USERNAME_PASSWORD` * `HASHICORP_VAULT_APPROLE` * `HASHICORP_VAULT_CERTIFICATE` |
| tokenSecretName | string | The name of the secret saved in external vault where token is stored. |
| usernameSecretName | string | The name of the secret saved in external vault where username is stored. |
| vaultUrl | string | External vault URL. |

```
{



"name": "string",



"id": "string",



"description": "string",



"password": "string",



"ownerAccessOnly": true,



"type": "TOKEN",



"token": "string"



}
```

### USERNAME\_PASSWORD

UserPasswordCredentials

Parameters

JSON model

#### The `UserPasswordCredentials` object

A credentials set of the `USERNAME_PASSWORD` type.

| Element | Type | Description |
| --- | --- | --- |
| externalVault | [ExternalVault](#openapi-definition-ExternalVault) | Information for synchronization credentials with external vault |
| password | string | The password of the credential. |
| user | string | The username of the credentials set. |

#### The `ExternalVault` object

Information for synchronization credentials with external vault

| Element | Type | Description |
| --- | --- | --- |
| locationForSynchronizationId | string | Id of a location used by the synchronizing monitor |
| passwordSecretName | string | The name of the secret saved in external vault where password is stored. |
| sourceAuthMethod | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `HASHICORP_VAULT_APPROLE` -> HashicorpApprole * `HASHICORP_VAULT_CERTIFICATE` -> HashicorpCertificate * `AZURE_KEY_VAULT_CLIENT_SECRET` -> AzureClientSecret * `CYBERARK_VAULT_USERNAME_PASSWORD` -> CyberArkUsernamePassword * `CYBERARK_VAULT_ALLOWED_LOCATION` -> CyberArkAllowedLocationDto The element can hold these values * `AZURE_KEY_VAULT_CLIENT_SECRET` * `CYBERARK_VAULT_ALLOWED_LOCATION` * `CYBERARK_VAULT_USERNAME_PASSWORD` * `HASHICORP_VAULT_APPROLE` * `HASHICORP_VAULT_CERTIFICATE` |
| tokenSecretName | string | The name of the secret saved in external vault where token is stored. |
| usernameSecretName | string | The name of the secret saved in external vault where username is stored. |
| vaultUrl | string | External vault URL. |

```
{



"name": "string",



"id": "string",



"description": "string",



"password": "string",



"ownerAccessOnly": true,



"type": "USERNAME_PASSWORD",



"user": "string"



}
```