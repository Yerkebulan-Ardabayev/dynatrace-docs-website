---
title: Synthetic locations API v2 - PUT статус публичных локаций
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/put-location-status
scraped: 2026-05-12T11:59:17.283607
---

# Synthetic locations API v2 - PUT статус публичных локаций

# Synthetic locations API v2 - PUT статус публичных локаций

* Справочник
* Опубликовано 21 января 2021 г.

Изменяет статус публичных синтетических локаций.

Запрос принимает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/locations/status` |
| PUT | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/locations/status` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `syntheticLocations.write`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | [SyntheticPublicLocationsStatus](#openapi-definition-SyntheticPublicLocationsStatus) | Новый статус публичных синтетических локаций. | body | Обязательный |

### Объекты тела запроса

#### Объект `SyntheticPublicLocationsStatus`

Статус публичных синтетических локаций.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| publicLocationsEnabled | boolean | Синтетические мониторы могут (`true`) или не могут (`false`) выполняться на публичных синтетических локациях. | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные поля. Её нужно скорректировать для использования в реальном запросе.

```
{



"publicLocationsEnabled": true



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Статус локаций обновлён. |
| **409** | - | Конфликт. Публичные локации не удалось отключить, потому что им назначены мониторы. |
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

## Связанные темы

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать браузерный монитор одного URL, браузерный clickpath или HTTP-монитор.")