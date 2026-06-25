---
title: Synthetic configuration API v2 - PUT конфигурация
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-configuration-v2/put-configuration
scraped: 2026-05-12T12:05:24.332885
---

# Synthetic configuration API v2 - PUT конфигурация

# Synthetic configuration API v2 - PUT конфигурация

* Справочник
* Updated on Sep 28, 2022

Обновляет конфигурацию Synthetic monitoring в вашем окружении.

Запрос принимает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/config` |
| PUT | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/config` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `syntheticLocations.write`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | [SyntheticConfigDto](#openapi-definition-SyntheticConfigDto) | DTO для конфигурации synthetic. | body | Обязательный |

### Объекты тела запроса

#### Объект `SyntheticConfigDto`

DTO для конфигурации synthetic.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| bmMonitorTimeout | integer | bmMonitorTimeout, тайм-аут выполнения браузерного монитора (мс) | Обязательный |
| bmStepTimeout | integer | bmStepTimeout, тайм-аут выполнения одного шага браузерного монитора (мс) | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные поля. Её нужно скорректировать для использования в реальном запросе.

```
{



"bmMonitorTimeout": 1,



"bmStepTimeout": 1



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | [SyntheticConfigDto](#openapi-definition-SyntheticConfigDto) | Успех. Набор параметров, связанных с synthetic, обновлён. У ответа нет тела. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

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

В этом примере запрос обновляет конфигурацию Synthetic monitoring из примера [GET-запроса](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-configuration-v2/get-configuration#example "Просмотр конфигурации Synthetic monitoring через Synthetic API v2."). Он уменьшает вдвое тайм-ауты для браузерного монитора и шагов браузерного монитора, устанавливая их в `300,000` и `30,000` соответственно.

API-токен передаётся в заголовке **Authorization**.

Можно скачать или скопировать пример тела запроса, чтобы попробовать его самостоятельно. Обязательно создайте резервную копию текущей конфигурации с помощью вызова **GET Synthetic configuration**.

#### Curl

```
curl --request PUT \



--url https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/config \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



--header 'Content-Type: application/json' \



--data '{



"bmMonitorTimeout": 300000,



"bmStepTimeout": 30000



}'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/config
```

#### Тело запроса

```
{



"bmMonitorTimeout": 300000,



"bmStepTimeout": 30000



}
```

#### Код ответа

204

## Связанные темы

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать браузерный монитор одного URL, браузерный clickpath или HTTP-монитор.")