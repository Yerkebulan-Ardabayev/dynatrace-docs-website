---
title: Synthetic nodes API - GET все узлы
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/synthetic-nodes/get-all
scraped: 2026-05-12T11:24:02.860188
---

# Synthetic nodes API - GET все узлы

# Synthetic nodes API - GET все узлы

* Справочник
* Опубликовано 26 июля 2019 г.

Доступна новая версия этого API, [Synthetic API v2](/managed/dynatrace-api/environment-api/synthetic-v2 "Узнайте, что предлагает Dynatrace Synthetic v2 API."). Попробуйте её!

Возвращает список всех синтетических узлов (и их параметры), доступных для вашего окружения.

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/synthetic/nodes` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/synthetic/nodes` |

## Аутентификация

Для выполнения запроса нужен access-токен с одним из следующих scope:

* `DataExport`
* `ExternalSyntheticIntegration`
* `ReadSyntheticData`

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Запрос не предоставляет настраиваемых параметров.

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

Результат усечён до трёх записей.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/nodes \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/nodes
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



"version": "1.164.0.20190205-184318",



"browserMonitorsEnabled": false



},



{



"entityId": "1267320067",



"hostname": "244.94.30.253",



"ips": [



"244.94.30.253"



],



"version": "1.161.0.20181210-173639",



"browserMonitorsEnabled": false



},



{



"entityId": "353074222",



"hostname": "GDN-007",



"ips": [



"132.46.87.141"



],



"version": "1.166.0.20190311-110828",



"browserMonitorsEnabled": true



}



]



}
```

#### Код ответа

200