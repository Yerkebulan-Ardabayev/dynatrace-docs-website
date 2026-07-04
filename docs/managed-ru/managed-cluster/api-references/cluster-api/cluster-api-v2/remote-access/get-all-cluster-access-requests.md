---
title: "Get all cluster access requests"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/remote-access/get-all-cluster-access-requests
updated: 2026-02-09
---

Этот API-вызов возвращает список всех текущих запросов на доступ к кластеру, включая пользователя, роль доступа, длительность доступа и состояние запроса.

## Аутентификация

Для выполнения этого запроса API-токену нужен один из следующих scope'ов:

* **Cluster token management** (`ClusterTokenManagement`)
* **Service Provider API** (`ServiceProviderAPI`)
* Доступ Nodekeeper для управления нодами (`Nodekeeper`)
  Как его получить и использовать, смотрите Cluster API - Authentication.

## Endpoint

`/api/cluster/v2/remoteaccess/requests`

## Параметры

В запросе нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AccessRequestData[]](#openapi-definition-AccessRequestData) | Успешно |
| **403** | - | Одобрение запросов remote access отключено |

### Объекты тела ответа

#### Объект `ResponseBody`

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
[


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


]
```

## Пример

В этом примере отправляется запрос к кластеру (`myManaged.cluster.com`) на получение списка всех текущих remote access requests.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/cluster/v2/remoteaccess/requests"


-H  "accept: application/json"
```

#### URL запроса

```
https://myManaged.cluster.com/api/cluster/v2/remoteaccess/requests
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

`200`
