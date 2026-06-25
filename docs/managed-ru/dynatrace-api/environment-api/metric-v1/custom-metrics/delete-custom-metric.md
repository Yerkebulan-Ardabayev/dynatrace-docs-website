---
title: Timeseries API v1 - DELETE пользовательскую метрику
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metric-v1/custom-metrics/delete-custom-metric
scraped: 2026-05-12T11:58:40.172874
---

# Timeseries API v1 - DELETE пользовательскую метрику

# Timeseries API v1 - DELETE пользовательскую метрику

* Справочник
* Опубликовано 07 ноября 2019 г.

Удаляет указанную пользовательскую метрику. При удалении определения метрики теряются все данные этой метрики, поэтому будьте осторожны с удалением.

Встроенные метрики удалить нельзя.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/timeseries/{timeseriesIdentifier}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/timeseries/{timeseriesIdentifier}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `DataExport`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| timeseriesIdentifier | string | ID метрики для удаления. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Пользовательская метрика удалена. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

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

В этом примере запрос удаляет пользовательскую метрику **custom:firewall.connections.dropped**.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X DELETE \



https://mySampleEnv.live.dynatrace.com/api/v1/timeseries/custom:firewall.connections.dropped \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/timeseries/custom:firewall.connections.dropped
```

#### Код ответа

204