---
title: Credential vault API - POST a set of credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/credential-vault/post-credentials
---

# Credential vault API - POST a set of credentials

# Credential vault API - POST a set of credentials

* Справка
* Опубликовано 14 октября 2019 г.

Этот API устарел. Вместо него нужно использовать [Credential vault API](/managed/dynatrace-api/environment-api/credential-vault "Learn what the Dynatrace API for credentials offers.") из Environment API.

Создаёт новый набор учётных данных для [синтетических мониторов](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.").

Запрос принимает и возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/credentials` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/credentials` |

## Authentication

Для выполнения этого запроса нужен токен доступа с областью действия `credentialVault.write`.

Как получить и использовать такой токен, описано в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

Разновидности моделей JSON для набора учётных данных, зависящие от типа модели, приведены в разделе [JSON models](/managed/dynatrace-api/configuration-api/credential-vault/models "Learn the variations of credential set JSON models in the Dynatrace API.").

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [Credentials](#openapi-definition-Credentials) | Тело JSON запроса. Содержит параметры нового набора учётных данных. | body | Required |

### Request body objects

#### The `Credentials` object

Набор учётных данных для синтетических мониторов.

Фактический набор полей зависит от типа учётных данных. Список фактических объектов приведён в описании поля **type** или в разделе [Credential vault API - JSON models﻿](https://dt-url.net/2sa3sen?dt=m).

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| allowContextlessRequests | boolean | Разрешить произвольным функциям доступ к сведениям об учётных данных (требуется область действия APP\_ENGINE). | Optional |
| allowedEntities | [CredentialAccessData](#openapi-definition-CredentialAccessData)[] | Набор сущностей, которым разрешено использовать учётные данные. | Optional |
| description | string | Краткое описание набора учётных данных. | Optional |
| id | string | ID набора учётных данных. | Optional |
| name | string | Имя набора учётных данных. | Required |
| ownerAccessOnly | boolean | Набор учётных данных доступен всем пользователям (`false`) или только владельцу (`true`). | Optional |
| ~~scope~~ | string | УСТАРЕЛО  Область действия набора учётных данных. Элемент может принимать следующие значения * `APP_ENGINE` * `EXTENSION` * `EXTENSION_AUTHENTICATION` * `SYNTHETIC` | Optional |
| scopes | string[] | Набор областей действия для набора учётных данных.  Ограничения: `CredentialsScope.APP_ENGINE` доступна только на новой платформе Dynatrace SaaS, она недоступна в managed-средах и в средах Grail SaaS, не относящихся к новой платформе. Элемент может принимать следующие значения * `APP_ENGINE` * `EXTENSION` * `EXTENSION_AUTHENTICATION` * `SYNTHETIC` | Required |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `CERTIFICATE` -> CertificateCredentials * `PUBLIC_CERTIFICATE` -> PublicCertificateCredentials * `USERNAME_PASSWORD` -> UserPasswordCredentials * `TOKEN` -> TokenCredentials * `SNMPV3` -> SNMPV3Credentials * `AWS_MONITORING_KEY_BASED` -> AWSKeyBasedCredentialsDto * `AWS_MONITORING_ROLE_BASED` -> AWSRoleBasedCredentials Элемент может принимать следующие значения * `AWS_MONITORING_KEY_BASED` * `AWS_MONITORING_ROLE_BASED` * `CERTIFICATE` * `PUBLIC_CERTIFICATE` * `SNMPV3` * `TOKEN` * `USERNAME_PASSWORD` | Required |

#### The `CredentialAccessData` object

Набор сущностей, которым разрешено использовать учётные данные.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| id | string | - | Optional |
| type | string | -Элемент может принимать следующие значения * `APPLICATION` * `UNKNOWN` * `USER` | Optional |

### Request body JSON model

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать для использования в фактическом запросе.

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
| **201** | [CredentialsId](#openapi-definition-CredentialsId) | Успешно. Новый набор учётных данных создан. Ответ содержит ID набора. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные недопустимы. |

### Response body objects

#### The `CredentialsId` object

Краткое представление набора учётных данных.

| Element | Type | Description |
| --- | --- | --- |
| id | string | ID набора учётных данных. |

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | Код статуса HTTP |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### The `ConstraintViolation` object

Список нарушений ограничений

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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

В этом примере запрос создаёт новый набор учётных данных типа **USERNAME\_PASSWORD**. Имя пользователя в наборе учётных данных, **john.smith**, а пароль, **abcd1234**.

Токен API передаётся в заголовке **Authorization**.

Пример тела запроса можно скачать или скопировать, чтобы попробовать его самостоятельно.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/config/v2/credentials/ \



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
https://mySampleEnv.live.dynatrace.com/api/config/v2/credentials/
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

* [Configure browser monitors in Classic](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Learn about configuring browser monitors and clickpaths.")
* [Configure HTTP monitors in Classic](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Learn about configuring HTTP monitors.")