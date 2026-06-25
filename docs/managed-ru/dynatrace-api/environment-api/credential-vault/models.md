---
title: Credential vault API - JSON models
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/credential-vault/models
scraped: 2026-05-12T12:09:45.491903
---

# Credential vault API - JSON models

# Credential vault API - JSON models

* Reference
* Published Oct 14, 2019

JSON-модели API **Credential vault** различаются в зависимости от поля **type** объекта. Здесь приведены JSON-модели для каждого варианта.

## Варианты объекта `Credentials`

Объект `Credentials` это базовый объект для всех учётных данных. Фактический набор полей зависит от поля **type**.

### CERTIFICATE

CertificateCredentials

Parameters

JSON model

#### Объект `CertificateCredentials`

Набор учётных данных типа `CERTIFICATE`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| certificate | string | Строка, содержащая байты файла сертификата, закодированные в Base64 без переноса строки. |
| certificateFormat | string | Формат сертификата. Используйте `PEM` для PEM-сертификатов и `PKCS12` для PFX и P12 сертификатов. Элемент может принимать значения * `PEM` * `PKCS12` * `UNKNOWN` |
| password | string | Пароль учётных данных, закодированный в Base64. Должен быть пустым для PEM-сертификатов. |

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

Используйте следующую unix-команду для преобразования строки пароля в Base64:

```
echo -n testPassword | base64
```

Используйте следующую unix-команду для преобразования файла сертификата в Base64:

```
base64 -i myCertFile.pfx
```

### PUBLIC\_CERTIFICATE

PublicCertificateCredentials

Parameters

JSON model

#### Объект `PublicCertificateCredentials`

Набор учётных данных типа `PUBLIC_CERTIFICATE`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| certificate | string | Сертификат в виде строки. |
| certificateFormat | string | Формат сертификата. Элемент может принимать значения * `PEM` * `PKCS12` * `UNKNOWN` |
| password | string | Пароль учётных данных (не поддерживается). |

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

#### Объект `TokenCredentials`

Набор учётных данных типа `TOKEN`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| externalVault | [ExternalVault](#openapi-definition-ExternalVault) | Информация для синхронизации учётных данных с внешним vault. |
| token | string | Токен в виде строки. |

#### Объект `ExternalVault`

Информация для синхронизации учётных данных с внешним vault.

| Элемент | Тип | Описание |
| --- | --- | --- |
| locationForSynchronizationId | string | ID локации, используемой синхронизирующим монитором. |
| passwordSecretName | string | Имя секрета во внешнем vault, где хранится пароль. |
| sourceAuthMethod | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `HASHICORP_VAULT_APPROLE` -> HashicorpApprole * `HASHICORP_VAULT_CERTIFICATE` -> HashicorpCertificate * `AZURE_KEY_VAULT_CLIENT_SECRET` -> AzureClientSecret * `CYBERARK_VAULT_USERNAME_PASSWORD` -> CyberArkUsernamePassword * `CYBERARK_VAULT_ALLOWED_LOCATION` -> CyberArkAllowedLocationDto Элемент может принимать значения * `AZURE_KEY_VAULT_CLIENT_SECRET` * `CYBERARK_VAULT_ALLOWED_LOCATION` * `CYBERARK_VAULT_USERNAME_PASSWORD` * `HASHICORP_VAULT_APPROLE` * `HASHICORP_VAULT_CERTIFICATE` |
| tokenSecretName | string | Имя секрета во внешнем vault, где хранится токен. |
| usernameSecretName | string | Имя секрета во внешнем vault, где хранится имя пользователя. |
| vaultUrl | string | URL внешнего vault. |

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

#### Объект `UserPasswordCredentials`

Набор учётных данных типа `USERNAME_PASSWORD`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| externalVault | [ExternalVault](#openapi-definition-ExternalVault) | Информация для синхронизации учётных данных с внешним vault. |
| password | string | Пароль учётных данных. |
| user | string | Имя пользователя набора учётных данных. |

#### Объект `ExternalVault`

Информация для синхронизации учётных данных с внешним vault.

| Элемент | Тип | Описание |
| --- | --- | --- |
| locationForSynchronizationId | string | ID локации, используемой синхронизирующим монитором. |
| passwordSecretName | string | Имя секрета во внешнем vault, где хранится пароль. |
| sourceAuthMethod | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `HASHICORP_VAULT_APPROLE` -> HashicorpApprole * `HASHICORP_VAULT_CERTIFICATE` -> HashicorpCertificate * `AZURE_KEY_VAULT_CLIENT_SECRET` -> AzureClientSecret * `CYBERARK_VAULT_USERNAME_PASSWORD` -> CyberArkUsernamePassword * `CYBERARK_VAULT_ALLOWED_LOCATION` -> CyberArkAllowedLocationDto Элемент может принимать значения * `AZURE_KEY_VAULT_CLIENT_SECRET` * `CYBERARK_VAULT_ALLOWED_LOCATION` * `CYBERARK_VAULT_USERNAME_PASSWORD` * `HASHICORP_VAULT_APPROLE` * `HASHICORP_VAULT_CERTIFICATE` |
| tokenSecretName | string | Имя секрета во внешнем vault, где хранится токен. |
| usernameSecretName | string | Имя секрета во внешнем vault, где хранится имя пользователя. |
| vaultUrl | string | URL внешнего vault. |

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