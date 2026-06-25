---
title: Credential vault API - PUT a set of credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/credential-vault/put-credentials
scraped: 2026-05-12T12:05:38.771719
---

# Credential vault API - PUT a set of credentials

# Credential vault API - PUT a set of credentials

* Reference
* Published Oct 14, 2019

Этот API устарел. Используйте [Credential vault API](/managed/dynatrace-api/environment-api/credential-vault "Узнайте, что предлагает Dynatrace API для credentials.") из Environment API.

Обновляет указанный набор учётных данных для [synthetic-мониторов](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать single-URL browser monitor, browser clickpath или HTTP monitor.").

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/credentials/{id}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/credentials/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `credentialVault.write`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Смотрите [JSON models](/managed/dynatrace-api/configuration-api/credential-vault/models "Узнайте варианты JSON-моделей набора учётных данных в Dynatrace API."), чтобы найти все JSON-модели, зависящие от типа модели.

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID сущности Dynatrace для обновляемого набора учётных данных. | path | Required |
| body | [Credentials](#openapi-definition-Credentials) | JSON-тело запроса. Содержит обновлённые параметры набора учётных данных. | body | Required |

### Объекты тела запроса

#### Объект `Credentials`

Набор учётных данных для synthetic-мониторов.

Фактический набор полей зависит от типа учётных данных. Список фактических объектов смотрите в описании поля **type** или в [Credential vault API - JSON models](https://dt-url.net/2sa3sen).

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| allowContextlessRequests | boolean | Разрешить ad-hoc функциям доступ к деталям учётных данных (требует scope APP\_ENGINE). | Optional |
| allowedEntities | [CredentialAccessData[]](#openapi-definition-CredentialAccessData) | Набор сущностей, которым разрешено использовать учётные данные. | Optional |
| description | string | Краткое описание набора учётных данных. | Optional |
| id | string | ID набора учётных данных. | Optional |
| name | string | Имя набора учётных данных. | Required |
| ownerAccessOnly | boolean | Набор учётных данных доступен каждому пользователю (`false`) или только владельцу (`true`). | Optional |
| ~~scope~~ | string | УСТАРЕЛО  Scope набора учётных данных. Возможные значения: * `APP_ENGINE` * `EXTENSION` * `SYNTHETIC` | Optional |
| scopes | string[] | Набор scope для набора учётных данных.  Ограничения: `CredentialsScope.APP_ENGINE` доступен только на новой Dynatrace SaaS платформе, он не доступен на managed или non-Grail SaaS окружениях. Возможные значения: * `APP_ENGINE` * `EXTENSION` * `SYNTHETIC` | Required |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `CERTIFICATE` -> CertificateCredentials * `PUBLIC_CERTIFICATE` -> PublicCertificateCredentials * `USERNAME_PASSWORD` -> UserPasswordCredentials * `TOKEN` -> TokenCredentials * `SNMPV3` -> SNMPV3Credentials * `AWS_MONITORING_KEY_BASED` -> AWSKeyBasedCredentialsDto * `AWS_MONITORING_ROLE_BASED` -> AWSRoleBasedCredentials Возможные значения: * `AWS_MONITORING_KEY_BASED` * `AWS_MONITORING_ROLE_BASED` * `CERTIFICATE` * `PUBLIC_CERTIFICATE` * `SNMPV3` * `TOKEN` * `USERNAME_PASSWORD` | Required |

#### Объект `CredentialAccessData`

Набор сущностей, которым разрешено использовать учётные данные.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| id | string | - | Optional |
| type | string | -Возможные значения: * `APPLICATION` * `UNKNOWN` * `USER` | Optional |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

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
| **201** | [CredentialsId](#openapi-definition-CredentialsId) | Успех. Новый набор учётных данных создан. Тело ответа содержит ID набора. |
| **204** | - | Успех. Набор учётных данных обновлён. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод |

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
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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

В этом примере запрос обновляет набор учётных данных, созданный в примере [POST request example](/managed/dynatrace-api/configuration-api/credential-vault/post-credentials#example "Создание конфигурации учётных данных через Dynatrace API.").

Он меняет имя пользователя на **mary.brown** и пароль на **4321dcba**.

API-токен передаётся в заголовке **Authorization**.

Вы можете скачать или скопировать пример тела запроса, чтобы попробовать его самостоятельно.

#### Curl

```
curl -X PUT \



https://mySampleEnv.live.dynatrace.com/api/config/v1/credentials/CREDENTIALS_VAULT-1E6EA5075AF7E85D \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"name": "RESTtest",



"description": "Test credentials",



"password": "4321dcba",



"ownerAccessOnly": true,



"type": "USERNAME_PASSWORD",



"user": "mary.brown"



}'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/credentials/CREDENTIALS_VAULT-1E6EA5075AF7E85D
```

#### Тело запроса

```
{



"name": "RESTtest",



"description": "Test credentials",



"password": "4321dcba",



"ownerAccessOnly": true,



"type": "USERNAME_PASSWORD",



"user": "mary.brown"



}
```

#### Код ответа

204

## Связанные темы

* [Configure browser monitors](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Узнайте о настройке browser-мониторов и clickpath.")
* [Configure HTTP monitors](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Узнайте о настройке HTTP-мониторов.")