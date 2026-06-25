---
title: Synthetic nodes API - GET узел
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/synthetic-nodes/get-node
scraped: 2026-05-12T11:55:17.532172
---

# Synthetic nodes API - GET узел

# Synthetic nodes API - GET узел

* Справочник
* Опубликовано 26 июля 2019 г.

Доступна новая версия этого API, [Synthetic API v2](/managed/dynatrace-api/environment-api/synthetic-v2 "Узнайте, что предлагает Dynatrace Synthetic v2 API."). Попробуйте её!

Возвращает все параметры указанного синтетического узла.

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/synthetic/nodes/{nodeId}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/synthetic/nodes/{nodeId}` |

## Аутентификация

Для выполнения запроса нужен access-токен с одним из следующих scope:

* `DataExport`
* `ExternalSyntheticIntegration`
* `ReadSyntheticData`

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

В этом примере запрос возвращает список всех синтетических узлов, доступных в окружении `mySampleEnv`.

API-токен передаётся в заголовке **Authorization**.

Результат усечён до трёх записей.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/nodes/353074222 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/nodes/353074222
```

#### Тело ответа

```
{



"entityId": "353074222",



"hostname": "GDN-007",



"ips": [



"132.46.87.141"



],



"version": "1.166.0.20190311-110828",



"browserMonitorsEnabled": true



}
```

#### Код ответа

200