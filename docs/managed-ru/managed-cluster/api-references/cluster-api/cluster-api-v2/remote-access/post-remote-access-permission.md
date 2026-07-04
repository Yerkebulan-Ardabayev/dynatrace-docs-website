---
title: "Grant remote access permission"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/remote-access/post-remote-access-permission
updated: 2026-02-09
---

Этот API-вызов даёт remote access permission конкретному пользователю. Можно задать роль пользователя, длительность и причину запроса remote access. Запрос принимает и возвращает payload `application/json`.

## Аутентификация

Для выполнения этого запроса API-токену нужен один из следующих scope'ов:

* **Cluster token management** (`ClusterTokenManagement`)
* **Service Provider API** (`ServiceProviderAPI`)
* Доступ Nodekeeper для управления нодами (`Nodekeeper`)
  Как его получить и использовать, смотрите Cluster API - Authentication.

## Endpoint

`/api/cluster/v2/remoteaccess/requests`

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [CreateAccessRequestDto](#openapi-definition-CreateAccessRequestDto) | JSON-тело запроса с параметрами access request. | body | Optional |

### Объекты тела запроса

#### Объект `CreateAccessRequestDto`

Данные access request: формат для создания запроса

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| reason | string | Описание причины запроса | Optional |
| requestedDays | integer | На сколько дней запрашивается доступ | Optional |
| role | string | Запрашиваемая роль. Возможные значения: * `devops-admin` * `devops-user` * `devops-viewer` | Optional |
| userId | string | ID пользователя | Optional |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

```
{


"reason": "string",


"requestedDays": 1,


"role": "devops-admin",


"userId": "string"


}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [AccessRequestData](#openapi-definition-AccessRequestData) | Успешно создано |
| **400** | - | Невалидные параметры |
| **403** | - | Одобрение запросов remote access отключено |
| **500** | - | Операция не выполнена |
| **513** | - | Mission Control недоступен |

### Объекты тела ответа

#### Объект `AccessRequestData`

Данные Access Request

| Элемент | Тип | Описание |
| --- | --- | --- |
| createdTimestamp | integer | Время создания access request (timestamp) |
| expirationTimestamp | integer | Время истечения доступа (timestamp) |
| reason | string | Описание причины запроса |
| requestId | string | ID запроса |
| requestedDays | integer | На сколько дней запрашивается доступ |
| role | string | Запрашиваемая роль. Возможные значения: * `devops-admin` * `devops-user` * `devops-viewer` |
| state | string | Состояние access request. Возможные значения: * `ACCEPTED` * `EXPIRED` * `PENDING` * `REJECTED` |
| stateModifiedByUser | string | Состояние access request было изменено пользователем |
| userId | string | ID пользователя |

### JSON-модели тела ответа

```
{


"createdTimestamp": 1,


"expirationTimestamp": 1,


"reason": "string",


"requestId": "string",


"requestedDays": 1,


"role": "devops-admin",


"state": "ACCEPTED",


"stateModifiedByUser": "string",


"userId": "string"


}
```

## Пример

В этом примере пользователю `john.smith@dynatrace.com` даётся remote cluster permission с ролью admin на `7` дней.

#### Curl

```
curl -X POST "https://myManaged.cluster.com/api/cluster/v2/remoteaccess/requests"


-H  "accept: application/json"


-H  "Content-Type: */*"


-d "{\"userId\":\"john.smith@dynatrace.com\",\"reason\":\"SUP-123456 Verifying cluster state after upgrade\",\"requestedDays\":7,\"role\":\"devops-admin\"}"
```

#### URL запроса

```
https://myManaged.cluster.com/api/cluster/v2/remoteaccess/requests
```

#### Тело запроса

```
{


"userId": "john.smith@dynatrace.com",


"reason": "SUP-123456 Verifying cluster state after upgrade",


"requestedDays": 7,


"role": "devops-admin"


}
```

#### Тело ответа

```
{


"requestId":"7a397770-86b7-473b-b23e-4a07d79f2eff",


"userId":"john.smith@dynatrace.com",


"reason":"SUP-123456 Verifying cluster state after upgrade",


"requestedDays":7,


"role":"devops-admin",


"createdTimestamp":1586452866661,


"expirationTimestamp":null,


"state":"PENDING",


"stateModifiedByUser":null


}
```

#### Код ответа

`201`
