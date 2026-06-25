---
title: Remote environments API - POST a remote environment configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/remote-environments/post-remote-environment
scraped: 2026-05-12T11:20:44.494690
---

# Remote environments API - POST a remote environment configuration

# Remote environments API - POST a remote environment configuration

* Reference
* Published Nov 19, 2019

Этот API устарел. Используйте [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API."). Ищите schema **Remote environment** (`builtin:remote.environment`).

Создаёт новую конфигурацию удалённого окружения.

Перед созданием Dynatrace проверяет указанные URI и токен, пытаясь подключиться к окружению с использованием токена для аутентификации. Если попытка неудачна, конфигурация удалённого окружения не создаётся.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/remoteEnvironments` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/remoteEnvironments` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

В теле не должно быть ID. ID назначается Dynatrace автоматически.

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [RemoteEnvironmentConfigDto](#openapi-definition-RemoteEnvironmentConfigDto) | JSON-тело запроса. Содержит параметры новой конфигурации удалённого окружения. | body | Optional |

### Объекты тела запроса

#### Объект `RemoteEnvironmentConfigDto`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| displayName | string | Отображаемое имя удалённого окружения. | Required |
| id | string | ID конфигурации. | Optional |
| networkScope | string | Сетевая область удалённого окружения:  * `EXTERNAL`: удалённое окружение находится в другой сети. * `INTERNAL`: удалённое окружение находится в той же сети. * `CLUSTER`: удалённое окружение находится в том же кластере.  Dynatrace SaaS может использовать только `EXTERNAL`.  Если не задано, используется `EXTERNAL`. Возможные значения: * `CLUSTER` * `EXTERNAL` * `INTERNAL` | Optional |
| token | string | API-токен, дающий доступ к удалённому окружению.  Токен должен иметь scope **Fetch data from a remote environment** (`RestRequestForwarding`).  По соображениям безопасности GET-запросы возвращают это поле как `null`. | Optional |
| uri | string | URI удалённого окружения. | Required |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

```
{



"displayName": "string",



"id": "string",



"networkScope": "EXTERNAL",



"token": "string",



"uri": "string"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [RemoteEnvironmentConfigStub](#openapi-definition-RemoteEnvironmentConfigStub) | Успех. Новая конфигурация удалённого окружения создана. Тело ответа содержит ID конфигурации. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

### Объекты тела ответа

#### Объект `RemoteEnvironmentConfigStub`

Краткое представление удалённого окружения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | - |
| name | string | - |
| networkScope | string | Сетевая область удалённого окружения:  * `EXTERNAL`: удалённое окружение находится в другой сети. * `INTERNAL`: удалённое окружение находится в той же сети. * `CLUSTER`: удалённое окружение находится в том же кластере.  Dynatrace SaaS может использовать только `EXTERNAL`.  Если не задано, используется `EXTERNAL`. Возможные значения: * `CLUSTER` * `EXTERNAL` * `INTERNAL` |
| uri | string | Отображаемое имя удалённого окружения. |

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



"id": "string",



"name": "string",



"networkScope": "CLUSTER",



"uri": "string"



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

## Validate payload

Рекомендуется валидировать payload перед отправкой реального запроса. Код ответа **204** означает валидный payload.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/remoteEnvironments/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/remoteEnvironments/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Validated. Переданная конфигурация валидна. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

#### Объекты тела ответа

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

#### JSON-модели тела ответа

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

В этом примере запрос создаёт новую конфигурацию удалённого окружения, ссылаясь на окружение **Pre-Production**.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/config/v1/remoteEnvironments/ \



-H 'Accept: application/json' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"displayName": "Pre-Production",



"uri": "https://preProd.live.dynatrace.com",



"token": "1234567890abcdefjhij",



"networkScope": "EXTERNAL"



}



'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/remoteEnvironments/
```

#### Тело запроса

```
{



"displayName": "Pre-Production",



"uri": "https://PreProd.live.dynatrace.com",



"token": "1234567890abcdefjhij",



"networkScope": "INTERNAL"



}
```

#### Тело ответа

```
{



"id": "c89b9d9f-8c59-4c5b-b7ef-1a082d11e9ba",



"name": "Pre-Production",



"uri": "https://preProd.live.dynatrace.com",



"networkScope": "EXTERNAL"



}
```

#### Код ответа

201