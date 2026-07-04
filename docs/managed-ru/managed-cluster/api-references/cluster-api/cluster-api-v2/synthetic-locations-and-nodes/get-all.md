---
title: "Synthetic nodes API v2 - GET all nodes (Dynatrace Managed)"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/get-all
updated: 2026-02-09
---

Этот API-вызов возвращает список всех synthetic nodes (и их параметров), доступных в вашем окружении. Запрос возвращает payload `application/json`.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите Cluster API - Authentication.

## Endpoint

`/api/cluster/v2/synthetic/nodes`

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| assignedToLocation | string | Фильтрует результирующий набор нод по назначению на synthetic location или нет. Возможные значения: * `TRUE` * `FALSE` | query | Optional |
| isContainerized | boolean | Если true, возвращает только контейнеризованные ноды. | query | Optional |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [Nodes](#openapi-definition-Nodes) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `Nodes`

Список synthetic nodes

| Элемент | Тип | Описание |
| --- | --- | --- |
| nodes | [NodeCollectionElement[]](#openapi-definition-NodeCollectionElement) | Список synthetic nodes |

#### Объект `NodeCollectionElement`

Краткое представление synthetic-объекта. Содержит только ID и отображаемое имя.

| Элемент | Тип | Описание |
| --- | --- | --- |
| activeGateVersion | string | Версия Active Gate. |
| autoUpdateEnabled | boolean | У Active Gate включена опция Auto update ('true') или нет ('false') |
| browserMonitorsEnabled | boolean | Флаг включения Browser check capabilities. |
| capabilities | string[] | Список возможностей ноды. |
| entityId | string | ID ноды. |
| healthCheckStatus | string | Статус health check synthetic node. |
| hostname | string | Hostname ноды. |
| ips | string[] | IP ноды. |
| oneAgentRoutingEnabled | boolean | У Active Gate включён One Agent routing ('true') или нет ('false'). |
| operatingSystem | string | Операционная система хоста Active Gate. |
| playerVersion | string | Версия synthetic player. |
| status | string | Статус synthetic node. |
| version | string | Версия ноды |

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


"nodes": [


{


"activeGateVersion": "1.172.2.20190607-040913",


"autoUpdateEnabled": true,


"browserMonitorsEnabled": true,


"capabilities": [


"HTTP_HIGH_RESOURCE",


"HTTP"


],


"entityId": "3086117876",


"healthCheckStatus": "Ok",


"hostname": "gdn.dyna.trace",


"ips": [


"238.245.160.14"


],


"oneAgentRoutingEnabled": true,


"operatingSystem": "Linux",


"playerVersion": "1.179.0.20190920-145430",


"status": "Running",


"version": "1.161.0.20181210-173639"


}


]


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

В этом примере запрос возвращает все synthetic nodes, доступные в окружении `mySampleEnv`.

API-токен передаётся в заголовке **Authorization**.

Результат усечён до двух записей.

#### Curl

```
curl -X GET \


https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/nodes \


-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/nodes
```

#### Тело ответа

```
{


"nodes": [


{


"entityId": "3086117876",


"hostname": "gdn.dyna.trace",


"ips": [


"238.245.160.14"


],


"version": "1.207.0.20201029-141904",


"browserMonitorsEnabled": true,


"activeGateVersion": "1.207.0.20201029-180431",


"oneAgentRoutingEnabled": false,


"operatingSystem": "Platform: Linux, Version: 4.4.0-1092-aws, Architecture: amd64, Processors: 2",


"autoUpdateEnabled": true,


"status": "Running",


"playerVersion": "1.207.0.20201029-081128",


"healthCheckStatus": "Ok"


},


{


"entityId": "1267320067",


"hostname": "244.94.30.253",


"ips": [


"244.94.30.253"


],


"version": null,


"browserMonitorsEnabled": true,


"activeGateVersion": "1.207.0.20201029-180431",


"oneAgentRoutingEnabled": false,


"operatingSystem": "Platform: Linux, Version: 4.15.0-1057-azure, Architecture: amd64, Processors: 2",


"autoUpdateEnabled": true,


"status": null,


"playerVersion": null,


"healthCheckStatus": "Offline"


}


]


}
```

#### Код ответа

200
