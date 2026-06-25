---
title: Synthetic nodes API v2 - GET узел
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-nodes-v2/get-node
scraped: 2026-05-12T11:54:32.192717
---

# Synthetic nodes API v2 - GET узел

# Synthetic nodes API v2 - GET узел

* Справочник
* Updated on Oct 17, 2022

Возвращает все параметры указанного синтетического узла.

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/nodes/{nodeId}` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/nodes/{nodeId}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `syntheticLocations.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| nodeId | string | ID требуемого синтетического узла. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [Node](#openapi-definition-Node) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `Node`

Конфигурация синтетического узла.

*Синтетический узел*, это ActiveGate, способный выполнять синтетические мониторы.

| Поле | Тип | Описание |
| --- | --- | --- |
| activeGateVersion | string | Версия Active Gate. |
| autoUpdateEnabled | boolean | У Active Gate включена ('true') или нет ('false') опция Auto update |
| browserMonitorsEnabled | boolean | Синтетический узел может выполнять браузерные мониторы (`true`) или нет (`false`). |
| browserType | string | Тип браузера. |
| browserVersion | string | Версия браузера. |
| capabilities | string[] | Список возможностей узла. |
| entityId | string | ID синтетического узла. |
| healthCheckStatus | string | Статус проверки работоспособности синтетического узла. |
| hostname | string | Имя хоста синтетического узла. |
| ips | string[] | IP синтетического узла. |
| oneAgentRoutingEnabled | boolean | У Active Gate включена ('true') или нет ('false') маршрутизация One Agent. |
| operatingSystem | string | Операционная система хоста Active Gate. |
| playerVersion | string | Версия синтетического плеера. |
| status | string | Статус синтетического узла. |
| version | string | Версия синтетического узла. |

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



"activeGateVersion": "1.172.2.20190607-040913",



"autoUpdateEnabled": true,



"browserMonitorsEnabled": true,



"browserType": "Chrome",



"browserVersion": "69.0.3497.81",



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

В этом примере запрос возвращает параметры узла с ID **3086117876**.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/nodes/3086117876 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/nodes/3086117876
```

#### Тело ответа

```
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



}
```

#### Код ответа

200