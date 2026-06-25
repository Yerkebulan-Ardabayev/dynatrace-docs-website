---
title: Delete Cluster token
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v2/cluster-tokens/delete-cluster-token
scraped: 2026-05-12T11:05:43.993140
---

# Delete Cluster token

# Delete Cluster token

* Published Feb 12, 2020

Этот API-вызов удаляет cluster token. Можно удалить любой токен, включая токены, не принадлежащие пользователю, чей токен используется для аутентификации вызова.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Cluster token management** (`ClusterTokenManagement`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/tokens`

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID токена для удаления. Может быть публичным идентификатором или секретом.  Нельзя удалить токен, который используется для аутентификации запроса. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Нельзя удалить токен, который используется для аутентификации запроса. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Запрошенный токен не найден. |

### Объекты тела ответа

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

В этом примере запрос удаляет токен с ID `4e9f128e-04f9-4795-pj319-8b7c-3c14a5e885e4`. Код ответа `204` означает успешное удаление.

API-токен передаётся в заголовке Authorization.

#### Curl

```
curl -X DELETE "https://myManaged.cluster.com/api/cluster/v2/tokens/4e9f128e-04f9-4795-pj319-8b7c-3c14a5e885e4"



-H "accept: application/json; charset=utf-8"
```

#### URL запроса

```
https://myManaged.cluster.com/api/cluster/v2/tokens/4e9f128e-04f9-4795-pj319-8b7c-3c14a5e885e4
```

#### Код ответа

`204`