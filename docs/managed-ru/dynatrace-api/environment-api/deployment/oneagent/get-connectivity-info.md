---
title: Deployment API - View connectivity information for OneAgent
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/deployment/oneagent/get-connectivity-info
scraped: 2026-05-12T11:58:27.718654
---

# Deployment API - View connectivity information for OneAgent

# Deployment API - View connectivity information for OneAgent

* Справочник
* Опубликовано 28 августа 2019 г.

Получает сведения о подключении OneAgent.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/connectioninfo` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/connectioninfo` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `InstallerDownload`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| networkZone | string | Сетевая зона, с которой должен быть сконфигурирован результат. | query | Необязательный |
| defaultZoneFallback | boolean | Установите `true`, чтобы выполнить откат к сетевой зоне по умолчанию, если указанная сетевая зона не существует. | query | Необязательный |
| version | string | Версия OneAgent, для которой запрашиваются сведения о подключении, в формате `1.221`.  Задайте этот параметр, чтобы получить оптимальный формат списка endpoints для наилучшей производительности. | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ConnectionInfo](#openapi-definition-ConnectionInfo) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ConnectionInfo`

Сведения о подключении OneAgent.

| Поле | Тип | Описание |
| --- | --- | --- |
| communicationEndpoints | string[] | Список endpoints для подключения к окружению Dynatrace. Список отсортирован по приоритету endpoint по убыванию. |
| formattedCommunicationEndpoints | string | Форматированный список endpoints для подключения к окружению Dynatrace. |
| tenantToken | string | Внутренний токен, используемый для аутентификации, когда OneAgent подключается к кластеру Dynatrace для отправки данных. |
| tenantUUID | string | ID вашего окружения Dynatrace. |

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



"communicationEndpoints": [



"string"



],



"formattedCommunicationEndpoints": "string",



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