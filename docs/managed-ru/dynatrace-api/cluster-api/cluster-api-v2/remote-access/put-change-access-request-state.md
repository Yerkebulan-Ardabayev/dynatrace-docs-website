---
title: Change state of access request
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v2/remote-access/put-change-access-request-state
scraped: 2026-05-12T11:05:59.951223
---

# Change state of access request

# Change state of access request

* Published Feb 12, 2020

Этот API-вызов меняет состояние access request по конкретному request ID. Можно установить состояние access request в `PENDING`, `ACCEPTED`, `REJECTED` или `EXPIRED`. Запрос принимает payload `application/json`.

## Аутентификация

Для выполнения этого запроса API-токену нужен один из следующих scope'ов:

* **Cluster token management** (`ClusterTokenManagement`)
* **Service Provider API** (`ServiceProviderAPI`)
* Доступ Nodekeeper для управления нодами (`Nodekeeper`)
  Как его получить и использовать, смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/remoteaccess/requests`

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| requestId | string | Параметр request id | path | Required |
| body | [AccessRequestStateData](#openapi-definition-AccessRequestStateData) | JSON-тело запроса с новым состоянием access request. | body | Optional |

### Объекты тела запроса

#### Объект `AccessRequestStateData`

Данные access request: формат для смены состояния запроса

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| state | string | Состояние access request. Возможные значения: * `ACCEPTED` * `EXPIRED` * `PENDING` * `REJECTED` | Optional |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

```
{



"state": "ACCEPTED"



}
```

## Код ответа

### Коды ответа

| Код | Описание |
| --- | --- |
| **200** | Успех |
| **400** | Bad request |
| **403** | Одобрение запросов remote access отключено |
| **404** | Access request не найден |
| **409** | Access request найден, но уже истёк |
| **500** | Операция не выполнена |

## Пример

В этом примере отправляется запрос на смену состояния remote access permission на `rejected` для access request ID `7a397770-86b7-473b-b23e-4a07d79f2eff`. Код ответа `200`, состояние remote access permission изменено.

#### Curl

```
curl -X PUT "https://myManaged.cluster.com/api/cluster/v2/remoteaccess/requests/7a397770-86b7-473b-b23e-4a07d79f2eff/state"



-H  "accept: */*"



-H  "Content-Type: */*"



-d "{\"state\":\"ACCEPTED\"}"
```

#### URL запроса

```
https://myManaged.cluster.com/api/cluster/v2/remoteaccess/requests/7a397770-86b7-473b-b23e-4a07d79f2eff/state
```

#### Тело запроса

```
{



"state": "REJECTED"



}
```

#### Код ответа

`200`