---
title: Credential vault API - PUT a set of credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/credential-vault/put-credentials
---

# Credential vault API - PUT a set of credentials

# Credential vault API - PUT a set of credentials

* Справка
* Опубликовано 06 октября 2022 г.

Обновляет заданный набор учётных данных для [синтетических мониторов](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.").

Запрос принимает и возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/credentials/{id}` |
| PUT | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/credentials/{id}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `credentialVault.write`.

О том, как получить и использовать токен, читайте в разделе [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Модели JSON смотрите в разделе [Модели JSON](/managed/dynatrace-api/environment-api/credential-vault/models "Learn the variations of credential set JSON models in the Dynatrace API."), там перечислены все модели JSON в зависимости от типа модели.

| Параметр | Тип | Описание | Расположение | Обязательность |
| --- | --- | --- | --- | --- |
| id | string | ID сущности Dynatrace набора учётных данных, который нужно обновить. | path | Обязательный |
| body | [Credentials](#openapi-definition-Credentials) | Тело JSON запроса. Содержит обновлённые параметры набора учётных данных. | body | Обязательный |

### Объекты тела запроса

#### Объект `Credentials`

Набор учётных данных для синтетических мониторов.

Фактический набор полей зависит от типа учётных данных. Список фактических объектов приведён в описании поля **type** или в разделе [Credential vault API - модели JSON﻿](https://dt-url.net/2sa3sen?dt=m).

| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| allowContextlessRequests | boolean | Разрешить ad-hoc функциям доступ к данным учётных данных (требуется область действия APP\_ENGINE). | Опционально |
| allowedEntities | [CredentialAccessData](#openapi-definition-CredentialAccessData)[] | Набор сущностей, которым разрешено использовать учётные данные. | Опционально |
| description | string | Краткое описание набора учётных данных. | Опционально |
| id | string | ID набора учётных данных. | Опционально |
| name | string | Название набора учётных данных. | Обязательный |
| ownerAccessOnly | boolean | Набор учётных данных доступен всем пользователям (`false`) или только владельцу (`true`). | Опционально |
| ~~scope~~ | string | УСТАРЕЛО  Область действия набора учётных данных. Элемент может принимать следующие значения * `APP_ENGINE` * `EXTENSION` * `EXTENSION_AUTHENTICATION` * `SYNTHETIC` | Опционально |
| scopes | string[] | Набор областей действия набора учётных данных.  Ограничения: `CredentialsScope.APP_ENGINE` доступна только на новой SaaS-платформе Dynatrace, она недоступна на managed или не-Grail SaaS-средах. Элемент может принимать следующие значения * `APP_ENGINE` * `EXTENSION` * `EXTENSION_AUTHENTICATION` * `SYNTHETIC` | Обязательный |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `CERTIFICATE` -> CertificateCredentials * `PUBLIC_CERTIFICATE` -> PublicCertificateCredentials * `USERNAME_PASSWORD` -> UserPasswordCredentials * `TOKEN` -> TokenCredentials * `SNMPV3` -> SNMPV3Credentials * `AWS_MONITORING_KEY_BASED` -> AWSKeyBasedCredentialsDto * `AWS_MONITORING_ROLE_BASED` -> AWSRoleBasedCredentials Элемент может принимать следующие значения * `AWS_MONITORING_KEY_BASED` * `AWS_MONITORING_ROLE_BASED` * `CERTIFICATE` * `PUBLIC_CERTIFICATE` * `SNMPV3` * `TOKEN` * `USERNAME_PASSWORD` | Обязательный |

#### Объект `CredentialAccessData`

Набор сущностей, которым разрешено использовать учётные данные.

| Элемент | Тип | Описание | Обязательность |
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
| **201** | [CredentialsId](#openapi-definition-CredentialsId) | Успех. Новый набор учётных данных создан. Ответ содержит ID набора. |
| **204** | - | Успех. Набор учётных данных обновлён. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные недопустимы. |
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
| message | string | Текст сообщения об ошибке |

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

## Похожие темы

* [Настройка браузерных мониторов в Classic](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Learn about configuring browser monitors and clickpaths.")
* [Настройка HTTP-мониторов в Classic](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Learn about configuring HTTP monitors.")