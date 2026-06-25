---
title: Third-party synthetic API - POST изменить состояние сторонних мониторов
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/third-party-synthetic/post-modify-state
scraped: 2026-05-12T11:54:38.789186
---

# Third-party synthetic API - POST изменить состояние сторонних мониторов

# Third-party synthetic API - POST изменить состояние сторонних мониторов

* Справочник
* Опубликовано 15 мая 2020 г.

Изменяет операционное состояние всех сторонних мониторов.

Запрос принимает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/synthetic/ext/stateModifications` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/synthetic/ext/stateModifications` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `ExternalSyntheticIntegration`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | [StateModification](#openapi-definition-StateModification) | JSON-тело запроса. Содержит новый операционный статус сторонних синтетических мониторов. | body | Обязательный |

### Объекты тела запроса

#### Объект `StateModification`

Операционное состояние, которое нужно установить для всех сторонних синтетических мониторов

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| state | string | Новое операционное состояние для всех сторонних синтетических мониторов. Поле может принимать значения: * `ACTIVE` * `HIDDEN` * `INACTIVE` | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные поля. Её нужно скорректировать для использования в реальном запросе.

```
{



"state": "ACTIVE"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Состояние сторонних мониторов изменено. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Не удалось. Входные данные недействительны. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Поле | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Поле | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Поле | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Поле может принимать значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

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

В этом примере запрос устанавливает состояние сторонних мониторов в **active**.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/ext/stateModifications \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"state": "ACTIVE"



}



'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/ext/stateModifications
```

#### Тело запроса

```
{



"state": "ACTIVE"



}
```

#### Код ответа

204