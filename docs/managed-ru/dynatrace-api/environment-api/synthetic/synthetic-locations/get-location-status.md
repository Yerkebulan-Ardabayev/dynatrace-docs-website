---
title: Synthetic locations API - GET статус публичных локаций
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/synthetic-locations/get-location-status
scraped: 2026-05-12T11:56:59.992953
---

# Synthetic locations API - GET статус публичных локаций

# Synthetic locations API - GET статус публичных локаций

* Справочник
* Опубликовано 21 января 2021 г.

Показывает статус публичных синтетических локаций.

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/synthetic/locations/status` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/synthetic/locations/status` |

## Аутентификация

Для выполнения запроса нужен access-токен с одним из следующих scope:

* `DataExport`
* `ExternalSyntheticIntegration`
* `ReadSyntheticData`

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Запрос не предоставляет настраиваемых параметров.

``

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SyntheticPublicLocationsStatus](#openapi-definition-SyntheticPublicLocationsStatus) | Успех. Ответ содержит статус публичных локаций. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SyntheticPublicLocationsStatus`

Статус публичных синтетических локаций.

| Поле | Тип | Описание |
| --- | --- | --- |
| publicLocationsEnabled | boolean | Синтетические мониторы могут (`true`) или не могут (`false`) выполняться на публичных синтетических локациях. |

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



"publicLocationsEnabled": true



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

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать браузерный монитор одного URL, браузерный clickpath или HTTP-монитор.")