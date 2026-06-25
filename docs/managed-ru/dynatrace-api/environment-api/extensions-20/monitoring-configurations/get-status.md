---
title: Extensions 2.0 API - GET статус monitoring configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/extensions-20/monitoring-configurations/get-status
scraped: 2026-05-12T11:56:36.602995
---

# Extensions 2.0 API - GET статус monitoring configuration

# Extensions 2.0 API - GET статус monitoring configuration

* Справочник
* Опубликовано 29 июня 2021 г.

Возвращает самое последнее выполнение monitoring configuration.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/extensions/{extensionName}/monitoringConfigurations/{configurationId}/status` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/extensions/{extensionName}/monitoringConfigurations/{configurationId}/status` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `extensionConfigurations.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| extensionName | string | Имя требуемого extension 2.0. | path | Обязательный |
| configurationId | string | ID требуемой monitoring configuration. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ExtensionStatusDto](#openapi-definition-ExtensionStatusDto) | Успех |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Запрашиваемый ресурс не существует. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ExtensionStatusDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| status | string | Последний статус данной конфигурации. Элемент может принимать значения * `ERROR` * `OK` * `PENDING` * `UNKNOWN` * `WARNING` |
| timestamp | integer | Метка времени последнего статуса данной конфигурации. |

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
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"status": "ERROR",



"timestamp": 1



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

## Связанные темы

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Разработка собственных Extensions в Dynatrace.")