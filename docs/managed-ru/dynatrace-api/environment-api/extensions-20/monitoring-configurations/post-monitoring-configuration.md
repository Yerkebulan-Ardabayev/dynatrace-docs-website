---
title: Extensions 2.0 API - POST monitoring configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/extensions-20/monitoring-configurations/post-monitoring-configuration
scraped: 2026-05-12T11:56:17.036489
---

# Extensions 2.0 API - POST monitoring configuration

# Extensions 2.0 API - POST monitoring configuration

* Справочник
* Опубликовано 7 апреля 2021 г.

Создаёт новую monitoring configuration для указанного Extensions 2.0 extension.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/extensions/{extensionName}/monitoringConfigurations` |
| POST | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/extensions/{extensionName}/monitoringConfigurations` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `extensionConfigurations.write`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| extensionName | string | Имя требуемого extension 2.0. | path | Обязательный |
| body | [MonitoringConfigurationDto[]](#openapi-definition-MonitoringConfigurationDto) | JSON-тело запроса, содержащее параметры monitoring configuration. | body | Обязательный |

### Объекты тела запроса

#### Объект `RequestBody`

#### Объект `MonitoringConfigurationDto`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| scope | string | Scope, для которого будет определена эта monitoring configuration | Обязательный |
| value | [JsonNode](#openapi-definition-JsonNode) | Monitoring configuration | Необязательный |

#### Объект `JsonNode`

Monitoring configuration

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать для использования в реальном запросе.

```
[



{



"scope": "HOST-D3A3C5A146830A79",



"value": {}



}



]
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [MonitoringConfigurationResponse[]](#openapi-definition-MonitoringConfigurationResponse) | Успех |
| **207** | [MonitoringConfigurationResponse[]](#openapi-definition-MonitoringConfigurationResponse) | Multi-Status, если не все запросы привели к одинаковому статусу |
| **400** | [ErrorEnvelope[]](#openapi-definition-ErrorEnvelope) | Неудача. Входные данные некорректны. |
| **404** | [ErrorEnvelope[]](#openapi-definition-ErrorEnvelope) | Неудача. Запрашиваемый ресурс не существует. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ResponseBody`

#### Объект `MonitoringConfigurationResponse`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| objectId | string | Идентификатор новой конфигурации |

#### Объект `ErrorResponseBody`

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
[



{



"code": 1,



"objectId": "331e416f-9ab7-4694-8408-816026820645"



}



]
```

```
[



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



]
```

## Связанные темы

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Разработка собственных Extensions в Dynatrace.")