---
title: Credential vault API - POST a set of credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/credential-vault/post-credentials
---

# Credential vault API - POST a set of credentials

# Credential vault API - POST a set of credentials

* Справка
* Опубликовано 14 октября 2019 г.

Создаёт новый набор учётных данных для [synthetic-мониторов](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать браузерный монитор с одним URL, браузерный clickpath или HTTP-монитор.").

Запрос принимает и возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/credentials` |
| POST | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/credentials` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `credentialVault.write`.

О том, как получить и использовать его, читайте в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

См. [модели JSON](/managed/dynatrace-api/environment-api/credential-vault/models "Узнайте о вариантах моделей JSON набора учётных данных в Dynatrace API."), чтобы найти все модели JSON, зависящие от типа модели.

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | [Credentials](#openapi-definition-Credentials) | Тело JSON запроса. Содержит параметры нового набора учётных данных. | body | Обязательный |

### Объекты тела запроса

#### Объект `Credentials`

Набор учётных данных для synthetic-мониторов.

Фактический набор полей зависит от типа учётных данных. Список фактических объектов приведён в описании поля **type** или в разделе [Credential vault API - модели JSON﻿](https://dt-url.net/2sa3sen?dt=m).

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| allowContextlessRequests | boolean | Разрешает ad-hoc-функциям доступ к деталям учётных данных (требуется область действия APP\_ENGINE). | Опционально |
| allowedEntities | [CredentialAccessData](#openapi-definition-CredentialAccessData)[] | Набор сущностей, которым разрешено использовать учётные данные. | Опционально |
| description | string | Краткое описание набора учётных данных. | Опционально |
| id | string | ID набора учётных данных. | Опционально |
| name | string | Имя набора учётных данных. | Обязательный |
| ownerAccessOnly | boolean | Набор учётных данных доступен всем пользователям (`false`) или только владельцу (`true`). | Опционально |
| ~~scope~~ | string | УСТАРЕЛО  Область действия набора учётных данных. Элемент может принимать следующие значения * `APP_ENGINE` * `EXTENSION` * `EXTENSION_AUTHENTICATION` * `SYNTHETIC` | Опционально |
| scopes | string[] | Набор областей действия набора учётных данных.  Ограничения: `CredentialsScope.APP_ENGINE` доступна только на новой SaaS-платформе Dynatrace, она недоступна в managed или не-Grail SaaS-окружениях. Элемент может принимать следующие значения * `APP_ENGINE` * `EXTENSION` * `EXTENSION_AUTHENTICATION` * `SYNTHETIC` | Обязательный |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `CERTIFICATE` -> CertificateCredentials * `PUBLIC_CERTIFICATE` -> PublicCertificateCredentials * `USERNAME_PASSWORD` -> UserPasswordCredentials * `TOKEN` -> TokenCredentials * `SNMPV3` -> SNMPV3Credentials * `AWS_MONITORING_KEY_BASED` -> AWSKeyBasedCredentialsDto * `AWS_MONITORING_ROLE_BASED` -> AWSRoleBasedCredentials Элемент может принимать следующие значения * `AWS_MONITORING_KEY_BASED` * `AWS_MONITORING_ROLE_BASED` * `CERTIFICATE` * `PUBLIC_CERTIFICATE` * `SNMPV3` * `TOKEN` * `USERNAME_PASSWORD` | Обязательный |

#### Объект `CredentialAccessData`

Набор сущностей, которым разрешено использовать учётные данные.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| id | string | - | Опционально |
| type | string | -Элемент может принимать следующие значения * `APPLICATION` * `UNKNOWN` * `USER` | Опционально |

### Модель JSON тела запроса

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
| **201** | [CredentialsId](#openapi-definition-CredentialsId) | Успешно. Новый набор учётных данных создан. Ответ содержит ID набора. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

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
| code | integer | Код статуса HTTP |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Модели JSON тела ответа

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

В этом примере запрос создаёт новый набор учётных данных типа **USERNAME\_PASSWORD**. Имя пользователя набора учётных данных, **john.smith**, пароль, **abcd1234**.

Токен API передаётся в заголовке **Authorization**.

Пример тела запроса можно скачать или скопировать, чтобы попробовать самостоятельно.

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

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/credentials/
```

#### Тело запроса

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

#### Тело ответа

```
{



"id": "CREDENTIALS_VAULT-1E6EA5075AF7E85D"



}
```

#### Код ответа

200

## Похожие темы

* [Configure browser monitors in Classic](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Узнайте о настройке браузерных мониторов и clickpath.")
* [Configure HTTP monitors in Classic](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Узнайте о настройке HTTP-мониторов.")