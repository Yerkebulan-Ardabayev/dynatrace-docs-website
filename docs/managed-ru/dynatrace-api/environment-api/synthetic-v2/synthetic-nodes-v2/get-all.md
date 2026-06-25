---
title: Synthetic nodes API v2 - GET все узлы
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-nodes-v2/get-all
scraped: 2026-05-12T11:54:30.023044
---

# Synthetic nodes API v2 - GET все узлы

# Synthetic nodes API v2 - GET все узлы

* Справочник
* Updated on Oct 17, 2022

Возвращает список всех синтетических узлов (и их параметры), доступных для вашего окружения.

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/nodes` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/nodes` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `syntheticLocations.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| assignedToLocation | string | Фильтрует итоговый набор узлов, оставляя те, что назначены синтетической локации, либо нет. Поле может принимать значения: * `TRUE` * `FALSE` | query | Необязательный |
| isContainerized | boolean | Если задано true, возвращаются только контейнеризированные узлы. | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [Nodes](#openapi-definition-Nodes) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `Nodes`

Список синтетических узлов

| Поле | Тип | Описание |
| --- | --- | --- |
| nodes | [NodeCollectionElement[]](#openapi-definition-NodeCollectionElement) | Список синтетических узлов |

#### Объект `NodeCollectionElement`

Краткое представление синтетического объекта. Содержит только ID и отображаемое имя.

| Поле | Тип | Описание |
| --- | --- | --- |
| activeGateVersion | string | Версия Active Gate. |
| autoUpdateEnabled | boolean | У Active Gate включена ('true') или нет ('false') опция Auto update |
| browserMonitorsEnabled | boolean | Флаг включения возможностей браузерной проверки. |
| capabilities | string[] | Список возможностей узла. |
| entityId | string | ID узла. |
| healthCheckStatus | string | Статус проверки работоспособности синтетического узла. |
| hostname | string | Имя хоста узла. |
| ips | string[] | IP узла. |
| oneAgentRoutingEnabled | boolean | У Active Gate включена ('true') или нет ('false') маршрутизация One Agent. |
| operatingSystem | string | Операционная система хоста Active Gate. |
| playerVersion | string | Версия синтетического плеера. |
| status | string | Статус синтетического узла. |
| version | string | Версия узла |

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

В этом примере запрос возвращает список всех синтетических узлов, доступных в окружении `mySampleEnv`.

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