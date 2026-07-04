---
title: "Get cluster access request"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/remote-access/get-cluster-access-request
updated: 2026-02-09
---

Этот API-вызов возвращает информацию о запросе доступа к кластеру по конкретному ID. Запрос возвращает payload `application/json`.

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
| requestId | string | Параметр request id | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AccessRequestData](#openapi-definition-AccessRequestData) | Успешно |
| **400** | - | Bad request |
| **403** | - | Одобрение запросов remote access отключено |
| **404** | - | Не найдено |

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

В этом примере запрашивается информация о remote access permission по конкретному request ID (`7a397770-86b7-473b-b23e-4a07d79f2eff`). В ответ возвращается JSON, показывающий, что запрос с ID `7a397770-86b7-473b-b23e-4a07d79f2eff` для пользователя `john.smith@dynatrace.com` даёт remote access permission с ролью admin на `7` дней с целью проверить состояние кластера после обновления.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/cluster/v2/remoteaccess/requests/7a397770-86b7-473b-b23e-4a07d79f2eff"


-H  "accept: application/json"
```

#### URL запроса

```
https://myManaged.cluster.com/api/cluster/v2/remoteaccess/requests/7a397770-86b7-473b-b23e-4a07d79f2eff
```

#### Тело ответа

```
{


"requestId": "7a397770-86b7-473b-b23e-4a07d79f2eff",


"userId": "john.smith@dynatrace.com",


"reason": "SUP-123456 Verifying cluster state after upgrade",


"requestedDays": 7,


"role": "devops-admin",


"createdTimestamp": 1586452866661,


"expirationTimestamp": 1587081600000,


"state": "ACCEPTED",


"stateModifiedByUser": "katie.novak"


}
```

#### Код ответа

`200`
