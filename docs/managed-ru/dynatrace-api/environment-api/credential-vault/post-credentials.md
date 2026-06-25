---
title: Credential vault API - POST a set of credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/credential-vault/post-credentials
scraped: 2026-05-12T11:54:25.960676
---

# Credential vault API - POST a set of credentials

# Credential vault API - POST a set of credentials

* Reference
* Published Oct 14, 2019

Создаёт новый набор учётных данных для [synthetic-мониторов](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать single-URL browser monitor, browser clickpath или HTTP monitor.").

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/credentials` |
| POST | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/credentials` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `credentialVault.write`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Смотрите [JSON models](/managed/dynatrace-api/environment-api/credential-vault/models "Узнайте варианты JSON-моделей набора учётных данных в Dynatrace API."), чтобы найти все JSON-модели, зависящие от типа модели.

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | [Credentials](#openapi-definition-Credentials) | JSON-тело запроса. Содержит параметры нового набора учётных данных. | body | Обязательный |

### Объекты тела запроса

#### Объект `Credentials`

Набор учётных данных для synthetic-мониторов.

Фактический набор полей зависит от типа учётных данных. Список фактических объектов смотрите в описании поля **type** или в [Credential vault API - JSON models](https://dt-url.net/2sa3sen).

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| allowContextlessRequests | boolean | Разрешить ad-hoc функциям доступ к деталям учётных данных (требует scope APP\_ENGINE). | Опциональный |
| allowedEntities | [CredentialAccessData[]](#openapi-definition-CredentialAccessData) | Набор сущностей, которым разрешено использовать учётные данные. | Опциональный |
| description | string | Краткое описание набора учётных данных. | Опциональный |
| id | string | ID набора учётных данных. | Опциональный |
| name | string | Имя набора учётных данных. | Обязательный |
| ownerAccessOnly | boolean | Набор учётных данных доступен каждому пользователю (`false`) или только владельцу (`true`). | Опциональный |
| ~~scope~~ | string | DEPRECATED  Scope набора учётных данных. Элемент может принимать значения * `APP_ENGINE` * `EXTENSION` * `SYNTHETIC` | Опциональный |
| scopes | string[] | Набор scope для набора учётных данных.  Ограничения: `CredentialsScope.APP_ENGINE` доступен только на новой Dynatrace SaaS платформе, он не доступен на managed или non-Grail SaaS окружениях. Элемент может принимать значения * `APP_ENGINE` * `EXTENSION` * `SYNTHETIC` | Обязательный |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `CERTIFICATE` -> CertificateCredentials * `PUBLIC_CERTIFICATE` -> PublicCertificateCredentials * `USERNAME_PASSWORD` -> UserPasswordCredentials * `TOKEN` -> TokenCredentials * `SNMPV3` -> SNMPV3Credentials * `AWS_MONITORING_KEY_BASED` -> AWSKeyBasedCredentialsDto * `AWS_MONITORING_ROLE_BASED` -> AWSRoleBasedCredentials Элемент может принимать значения * `AWS_MONITORING_KEY_BASED` * `AWS_MONITORING_ROLE_BASED` * `CERTIFICATE` * `PUBLIC_CERTIFICATE` * `SNMPV3` * `TOKEN` * `USERNAME_PASSWORD` | Обязательный |

#### Объект `CredentialAccessData`

Набор сущностей, которым разрешено использовать учётные данные.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| id | string | - | Опциональный |
| type | string | -Элемент может принимать значения * `APPLICATION` * `UNKNOWN` * `USER` | Опциональный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

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

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [CredentialsId](#openapi-definition-CredentialsId) | Успех. Новый набор учётных данных создан. Ответ содержит ID набора. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Входные данные некорректны. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

#### Объект `CredentialsId`

Краткое представление набора учётных данных.

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | ID набора учётных данных. |

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

## Пример

В этом примере запрос создаёт новый набор учётных данных типа **USERNAME\_PASSWORD**. Имя пользователя набора **john.smith**, пароль **abcd1234**.

API-токен передаётся в заголовке **Authorization**.

Вы можете скачать или скопировать пример тела запроса, чтобы попробовать его самостоятельно.

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

## Связанные темы

* [Configure browser monitors](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Узнайте о настройке browser-мониторов и clickpath.")
* [Configure HTTP monitors](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Узнайте о настройке HTTP-мониторов.")