---
title: "Get cluster user sessions"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/user-management/get-cluster-user-sessions
updated: 2026-02-09
---

Этот API-вызов возвращает сессии пользователей по конкретному user ID. Можно запросить список пользовательских сессий для конкретного user ID в конкретном окружении.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите Cluster API - Authentication.

## Endpoint

`/api/cluster/v2/userSessions`

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| userId | string | ID пользователя (опциональный) | query | Optional |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [UserSession[]](#openapi-definition-UserSession) | Успех |
| **500** | - | Операция не выполнена |

### Объекты тела ответа

#### Объект `ResponseBody`

#### Объект `UserSession`

Экземпляр пользовательской сессии Managed

| Элемент | Тип | Описание |
| --- | --- | --- |
| creationTime | integer | Timestamp создания пользовательской сессии |
| device | string | Устройство, с которого вошёл пользователь |
| ip | string | IP, с которого вошёл пользователь |
| lastAccessedTimestamp | integer | Timestamp последнего обращения к сессии |
| loginType | string | Способ входа пользователя. Возможные значения: * `LOCAL` * `LDAP` * `SSO_MANAGED` * `DEVOPSTOKEN` |
| nodeId | integer | Нода, на которой существует пользовательская сессия |
| sessionId | string | ID пользовательской сессии |
| tenantUuid | string | UUID тенанта, в который вошёл пользователь (или UUID кластера, если пользователь вошёл в CMC) |
| userId | string | ID пользователя |

### JSON-модели тела ответа

```
[


{


"creationTime": 1,


"device": "string",


"ip": "string",


"lastAccessedTimestamp": 1,


"loginType": "LOCAL",


"nodeId": 1,


"sessionId": "string",


"tenantUuid": "string",


"userId": "string"


}


]
```

## Пример

В этом примере запрос возвращает пользовательские сессии в кластере `myManaged.cluster.com` для пользователя `user.name`.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/cluster/v2/userSessions?userId=user.name"


-H  "accept: application/json"
```

#### URL запроса

```
https://myManaged.cluster.com/api/cluster/v2/userSessions?userId=user.name
```

#### Тело ответа

```
[


{


"userId": "user.name",


"nodeId": 4,


"sessionId": "string",


"creationTime": 0,


"lastAccessedTimestamp": 0,


"tenantUuid": "string",


"loginType": "LOCAL",


"device": "string",


"ip": "string"


}


]
```

#### Код ответа

`200`
