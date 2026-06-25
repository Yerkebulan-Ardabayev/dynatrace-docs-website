---
title: Credential vault API - GET credentials metadata
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/credential-vault/get-credentials
scraped: 2026-05-12T11:54:27.999079
---

# Credential vault API - GET credentials metadata

# Credential vault API - GET credentials metadata

* Reference
* Published Oct 06, 2022

Возвращает метаданные указанного набора учётных данных для [synthetic-мониторов](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать single-URL browser monitor, browser clickpath или HTTP monitor."). Сам набор учётных данных (имя пользователя/сертификат и пароль) не входит в ответ.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/credentials/{id}` |
| GET | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/credentials/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `credentialVault.read`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | Dynatrace entity ID требуемого набора учётных данных. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [CredentialsResponseElement](#openapi-definition-CredentialsResponseElement) | Успех. Ответ содержит метаданные набора учётных данных. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Входные данные некорректны. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

#### Объект `CredentialsResponseElement`

Метаданные набора учётных данных.

| Элемент | Тип | Описание |
| --- | --- | --- |
| allowContextlessRequests | boolean | Разрешить доступ без контекста приложения, например, из ad hoc функций в Workflows (требует scope APP\_ENGINE). |
| allowedEntities | [CredentialAccessData[]](#openapi-definition-CredentialAccessData) | Набор сущностей, которым разрешено использовать учётные данные. |
| credentialUsageSummary | [CredentialUsageHandler[]](#openapi-definition-CredentialUsageHandler) | Список содержит сводные данные об использовании учётных данных. |
| description | string | Краткое описание набора учётных данных. |
| externalVault | [ExternalVaultConfig](#openapi-definition-ExternalVaultConfig) | Конфигурация синхронизации с внешним vault для учётных данных типа username/password. |
| id | string | ID набора учётных данных. |
| name | string | Имя набора учётных данных. |
| owner | string | Владелец учётных данных (пользователь, для которого создан использованный API-токен). |
| ownerAccessOnly | boolean | Флаг, указывающий, что эти учётные данные видны только владельцу. |
| scope | string | Scope набора учётных данных. Элемент может принимать значения * `APP_ENGINE` * `EXTENSION` * `SYNTHETIC` |
| scopes | string[] | Набор scope для набора учётных данных. Элемент может принимать значения * `APP_ENGINE` * `EXTENSION` * `SYNTHETIC` |
| type | string | Тип набора учётных данных. Элемент может принимать значения * `AWS_MONITORING_KEY_BASED` * `AWS_MONITORING_ROLE_BASED` * `CERTIFICATE` * `PUBLIC_CERTIFICATE` * `SNMPV3` * `TOKEN` * `UNKNOWN` * `USERNAME_PASSWORD` |

#### Объект `CredentialAccessData`

Набор сущностей, которым разрешено использовать учётные данные.

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | - |
| type | string | -Элемент может принимать значения * `APPLICATION` * `UNKNOWN` * `USER` |

#### Объект `CredentialUsageHandler`

Хранит информацию об использовании учётных данных.

| Элемент | Тип | Описание |
| --- | --- | --- |
| count | integer | Количество использований. |
| type | string | Тип использования. |

#### Объект `ExternalVaultConfig`

Конфигурация синхронизации с внешним vault для учётных данных типа username/password.

| Элемент | Тип | Описание |
| --- | --- | --- |
| credentialsUsedForExternalSynchronization | string[] | - |
| passwordSecretName | string | - |
| sourceAuthMethod | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `HASHICORP_VAULT_APPROLE` -> HashicorpApproleConfig * `HASHICORP_VAULT_CERTIFICATE` -> HashicorpCertificateConfig * `AZURE_KEY_VAULT_CLIENT_SECRET` -> AzureClientSecretConfig * `CYBERARK_VAULT_USERNAME_PASSWORD` -> CyberArkUsernamePasswordConfig * `CYBERARK_VAULT_ALLOWED_LOCATION` -> CyberArkAllowedLocationConfig Элемент может принимать значения * `AZURE_KEY_VAULT_CLIENT_SECRET` * `CYBERARK_VAULT_ALLOWED_LOCATION` * `CYBERARK_VAULT_USERNAME_PASSWORD` * `HASHICORP_VAULT_APPROLE` * `HASHICORP_VAULT_CERTIFICATE` |
| tokenSecretName | string | - |
| type | string | -Элемент может принимать значения * `AZURE_CERTIFICATE_MODEL` * `AZURE_CLIENT_SECRET_MODEL` * `CYBERARK_VAULT_ALLOWED_LOCATION_MODEL` * `CYBERARK_VAULT_USERNAME_PASSWORD_MODEL` * `HASHICORP_APPROLE_MODEL` * `HASHICORP_CERTIFICATE_MODEL` |
| usernameSecretName | string | - |
| vaultUrl | string | - |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния. |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений. |
| message | string | Сообщение об ошибке. |

#### Объект `ConstraintViolation`

Список нарушений ограничений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

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

## Связанные темы

* [Configure browser monitors](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Узнайте о настройке browser-мониторов и clickpath.")
* [Configure HTTP monitors](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Узнайте о настройке HTTP-мониторов.")