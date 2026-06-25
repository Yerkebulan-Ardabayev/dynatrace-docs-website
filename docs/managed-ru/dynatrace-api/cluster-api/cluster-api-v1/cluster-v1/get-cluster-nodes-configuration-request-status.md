---
title: Get cluster nodes configuration request status
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/get-cluster-nodes-configuration-request-status
scraped: 2026-05-12T12:12:21.416593
---

# Get cluster nodes configuration request status

# Get cluster nodes configuration request status

* Published Apr 30, 2021

Этот API-вызов возвращает статус запросов на конфигурацию узлов кластера.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать — смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/cluster/configuration/status/{requestedAt}`

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| requestedAt | integer | - | path | Required |

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **200** | Успех |

## Пример

Этот запрос возвращает информацию о статусе указанной операции. Идентифицировать запрос можно по его timestamp, переданному в path-параметр `requestedAt`.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/v1.0/onpremise/cluster/configuration/status/1" -H  "accept: */*"
```

#### URL запроса

```
https://myManaged.cluster.com/api/v1.0/onpremise/cluster/configuration/status/1
```

#### Тело ответа

```
{



"id": 1619771074449,



"request": {



"clusterNodes": [



{



"id": 1,



"ipAddress": "10.10.4.2",



"webUI": false,



"agent": true,



"datacenter": "datacenter-1",



"kubernetesRole": ""



}



]



},



"state": "SUCCESS",



"details": "",



"requestedAt": "2021/04/30 08:24:34 Etc/UTC",



"finishedAt": "2021/04/30 08:25:50 Etc/UTC",



"states": {



"DOMAIN_UPDATE": {



"id": 0,



"request": null,



"state": "SUCCESS",



"details": "",



"requestedAt": "2021/04/30 08:25:13 Etc/UTC",



"finishedAt": "2021/04/30 08:25:41 Etc/UTC",



"states": {}



},



"OPERATION_STATE": {



"id": 0,



"request": null,



"state": "SUCCESS",



"details": "Update operation state step finished",



"requestedAt": "2021/04/30 08:25:41 Etc/UTC",



"finishedAt": "2021/04/30 08:25:41 Etc/UTC",



"states": {}



},



"AGENT_TRAFFIC": {



"id": 0,



"request": null,



"state": "SUCCESS",



"details": "Update agent traffic step finished",



"requestedAt": "2021/04/30 08:25:41 Etc/UTC",



"finishedAt": "2021/04/30 08:25:50 Etc/UTC",



"states": {}



},



"WEB_UI": {



"id": 0,



"request": null,



"state": "SUCCESS",



"details": "Update web step finished",



"requestedAt": "2021/04/30 08:24:36 Etc/UTC",



"finishedAt": "2021/04/30 08:25:13 Etc/UTC",



"states": {}



}



}



}
```

#### Код ответа

`200`