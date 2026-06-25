---
title: Extensions 2.0 API - PUT monitoring configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/extensions-20/monitoring-configurations/put-monitoring-configuration
scraped: 2026-05-12T11:56:21.020617
---

# Extensions 2.0 API - PUT monitoring configuration

# Extensions 2.0 API - PUT monitoring configuration

* Справочник
* Опубликовано 7 апреля 2021 г.

Обновляет указанную monitoring configuration Extensions 2.0 extension.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/extensions/{extensionName}/monitoringConfigurations/{configurationId}` |
| PUT | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/extensions/{extensionName}/monitoringConfigurations/{configurationId}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `extensionConfigurations.write`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| extensionName | string | Имя требуемого extension 2.0. | path | Обязательный |
| configurationId | string | ID требуемой monitoring configuration. | path | Обязательный |
| body | [MonitoringConfigurationUpdateDto](#openapi-definition-MonitoringConfigurationUpdateDto) | JSON-тело запроса, содержащее параметры monitoring configuration. | body | Обязательный |

### Объекты тела запроса

#### Объект `MonitoringConfigurationUpdateDto`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| value | [JsonNode](#openapi-definition-JsonNode) | Monitoring configuration | Необязательный |

#### Объект `JsonNode`

Monitoring configuration

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать для использования в реальном запросе.

```
{



"value": {}



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [MonitoringConfigurationResponse](#openapi-definition-MonitoringConfigurationResponse) | Успех |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Входные данные некорректны. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Запрашиваемый ресурс не существует. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `MonitoringConfigurationResponse`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| objectId | string | Идентификатор новой конфигурации |

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



"code": 1,



"objectId": "331e416f-9ab7-4694-8408-816026820645"



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