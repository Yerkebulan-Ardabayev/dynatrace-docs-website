---
title: Deployment API - GET сведения о подключении ActiveGate
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/deployment/activegate/get-activegate-connectivity
scraped: 2026-05-12T11:36:33.286160
---

# Deployment API - GET сведения о подключении ActiveGate

# Deployment API - GET сведения о подключении ActiveGate

* Справочник
* Опубликовано 02 июля 2020 г.

Получает сведения о подключении ActiveGate.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/installer/gateway/connectioninfo` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/deployment/installer/gateway/connectioninfo` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `InstallerDownload`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| networkZone | string | Сетевая зона, с которой должен быть сконфигурирован результат. | query | Необязательный |
| defaultZoneFallback | boolean | Установите `true`, чтобы выполнить откат к сетевой зоне по умолчанию, если указанная сетевая зона не существует. | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ActiveGateConnectionInfo](#openapi-definition-ActiveGateConnectionInfo) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ActiveGateConnectionInfo`

Сведения о подключении для Environment ActiveGate (кроме токенов ActiveGate)

| Поле | Тип | Описание |
| --- | --- | --- |
| communicationEndpoints | string | - |
| tenantToken | string | - |
| tenantUUID | string | - |

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



"communicationEndpoints": "string",



"tenantToken": "string",



"tenantUUID": "string"



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