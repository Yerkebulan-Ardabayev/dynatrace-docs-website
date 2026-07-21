---
title: Credential vault API - PUT a set of credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/credential-vault/put-credentials
---

# Credential vault API - PUT a set of credentials

# Credential vault API - PUT a set of credentials

* Справочник
* Опубликовано 14 октября 2019 г.

Этот API устарел. Вместо него используй [Credential vault API](/managed/dynatrace-api/environment-api/credential-vault "Узнай, что предлагает Dynatrace API для учётных данных.") из Environment API.

Обновляет указанный набор учётных данных для [синтетических мониторов](/managed/observe/digital-experience/synthetic-monitoring "Узнай о Synthetic Monitoring и о том, как создать одноадресный браузерный монитор, browser clickpath или HTTP-монитор.").

Запрос принимает и возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/credentials/{id}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/credentials/{id}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `credentialVault.write`.

Подробнее о том, как получить и использовать токен, см. в разделе [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Модели JSON смотри в разделе [JSON моделей](/managed/dynatrace-api/configuration-api/credential-vault/models "Узнай о вариантах моделей JSON набора учётных данных в Dynatrace API."), чтобы найти все модели JSON, зависящие от типа модели.

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID сущности Dynatrace для набора учётных данных, который нужно обновить. | path | Обязательный |
| body | [Credentials](#openapi-definition-Credentials) | Тело JSON запроса. Содержит обновлённые параметры набора учётных данных. | body | Обязательный |

### Объекты тела запроса

#### Объект `Credentials`

Набор учётных данных для синтетических мониторов.

Фактический набор полей зависит от типа учётных данных. Список фактических объектов приведён в описании поля **type**, либо см. [Credential vault API - модели JSON﻿](https://dt-url.net/2sa3sen?dt=m).

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| allowContextlessRequests | boolean | Разрешить произвольным функциям (ad-hoc functions) доступ к данным учётных данных (требуется область действия APP\_ENGINE). | Опционально |
| allowedEntities | [CredentialAccessData](#openapi-definition-CredentialAccessData)[] | Набор сущностей, которым разрешено использовать эти учётные данные. | Опционально |
| description | string | Краткое описание набора учётных данных. | Опционально |
| id | string | ID набора учётных данных. | Опционально |
| name | string | Имя набора учётных данных. | Обязательный |
| ownerAccessOnly | boolean | Набор учётных данных доступен всем пользователям (`false`) или только владельцу (`true`). | Опционально |
| ~~scope~~ | string | УСТАРЕЛО  Область действия набора учётных данных. Элемент может принимать следующие значения * `APP_ENGINE` * `EXTENSION` * `EXTENSION_AUTHENTICATION` * `SYNTHETIC` | Опционально |
| scopes | string[] | Набор областей действия набора учётных данных.  Ограничения: `CredentialsScope.APP_ENGINE` доступен только на новой платформе Dynatrace SaaS, он недоступен в managed-окружениях и в окружениях SaaS, не относящихся к Grail. Элемент может принимать следующие значения * `APP_ENGINE` * `EXTENSION` * `EXTENSION_AUTHENTICATION` * `SYNTHETIC` | Обязательный |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `CERTIFICATE` -> CertificateCredentials * `PUBLIC_CERTIFICATE` -> PublicCertificateCredentials * `USERNAME_PASSWORD` -> UserPasswordCredentials * `TOKEN` -> TokenCredentials * `SNMPV3` -> SNMPV3Credentials * `AWS_MONITORING_KEY_BASED` -> AWSKeyBasedCredentialsDto * `AWS_MONITORING_ROLE_BASED` -> AWSRoleBasedCredentials Элемент может принимать следующие значения * `AWS_MONITORING_KEY_BASED` * `AWS_MONITORING_ROLE_BASED` * `CERTIFICATE` * `PUBLIC_CERTIFICATE` * `SNMPV3` * `TOKEN` * `USERNAME_PASSWORD` | Обязательный |

#### Объект `CredentialAccessData`

Набор сущностей, которым разрешено использовать эти учётные данные.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| id | string | - | Опционально |
| type | string | -Элемент может принимать следующие значения * `APPLICATION` * `UNKNOWN` * `USER` | Опционально |

### Модель JSON тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать для использования в реальном запросе.

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
| **204** | - | Успешно. Набор учётных данных обновлён. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Некорректные входные данные |

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

В этом примере запрос обновляет набор учётных данных, созданный в [примере POST-запроса](/managed/dynatrace-api/configuration-api/credential-vault/post-credentials#example "Создание конфигурации учётных данных через Dynatrace API.").

Он меняет имя пользователя на **mary.brown** и пароль на **4321dcba**.

Токен API передаётся в заголовке **Authorization**.

Пример тела запроса можно скачать или скопировать, чтобы попробовать самостоятельно.

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

## Похожие темы

* [Настройка браузерных мониторов в Classic](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Узнай о настройке браузерных мониторов и clickpath.")
* [Настройка HTTP-мониторов в Classic](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Узнай о настройке HTTP-мониторов.")