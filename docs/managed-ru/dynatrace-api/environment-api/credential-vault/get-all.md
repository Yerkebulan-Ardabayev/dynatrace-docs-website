---
title: Credential vault API - GET all credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/credential-vault/get-all
scraped: 2026-05-12T11:54:23.968569
---

# Credential vault API - GET all credentials

# Credential vault API - GET all credentials

* Reference
* Published Oct 06, 2022

Возвращает список всех учётных данных для [synthetic-мониторов](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать single-URL browser monitor, browser clickpath или HTTP monitor."), хранящихся в вашем окружении.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/credentials` |
| GET | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/credentials` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `credentialVault.read`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| type | string | Фильтрует результат по указанному типу учётных данных. Элемент может принимать значения * `CERTIFICATE` * `USERNAME_PASSWORD` * `TOKEN` * `SNMPV3` * `AWS_MONITORING_KEY_BASED` * `AWS_MONITORING_ROLE_BASED` | query | Опциональный |
| name | string | Фильтрует результат по имени. В кавычках берётся целая фраза. Регистр не учитывается. | query | Опциональный |
| user | string | Фильтрует учётные данные, доступные пользователю (принадлежащие пользователю или доступные всем). | query | Опциональный |
| scope | string | Фильтрует учётные данные с указанным scope. | query | Опциональный |
| nextPageKey | string | Курсор для следующей страницы результатов. Его можно найти в поле **nextPageKey** предыдущего ответа.  Первая страница возвращается всегда, если параметр **nextPageKey** не указан.  Когда **nextPageKey** установлен для получения последующих страниц, все остальные query-параметры должны быть опущены. | query | Опциональный |
| pageSize | integer | Количество учётных данных в одном payload ответа.  Максимально допустимый размер страницы 500.  Если не задано, используется 100. | query | Опциональный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [CredentialsList](#openapi-definition-CredentialsList) | Успех |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Входные данные некорректны. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

#### Объект `CredentialsList`

Список наборов учётных данных для Synthetic-мониторов.

| Элемент | Тип | Описание |
| --- | --- | --- |
| credentials | [CredentialsResponseElement[]](#openapi-definition-CredentialsResponseElement) | Список наборов учётных данных для Synthetic-мониторов. |
| nextPageKey | string | - |
| pageSize | integer | - |
| totalCount | integer | - |

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

## Связанные темы

* [Configure browser monitors](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Узнайте о настройке browser-мониторов и clickpath.")
* [Configure HTTP monitors](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Узнайте о настройке HTTP-мониторов.")