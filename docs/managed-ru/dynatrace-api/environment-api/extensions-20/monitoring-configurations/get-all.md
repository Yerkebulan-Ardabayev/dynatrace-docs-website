---
title: Extensions 2.0 API - GET все monitoring configurations
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/extensions-20/monitoring-configurations/get-all
scraped: 2026-05-12T11:56:19.045417
---

# Extensions 2.0 API - GET все monitoring configurations

# Extensions 2.0 API - GET все monitoring configurations

* Справочник
* Опубликовано 7 апреля 2021 г.

Список всех monitoring configurations указанного Extensions 2.0 extension.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/extensions/{extensionName}/monitoringConfigurations` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/extensions/{extensionName}/monitoringConfigurations` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `extensionConfigurations.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| nextPageKey | string | Курсор для следующей страницы результатов. Его можно найти в поле **nextPageKey** предыдущего ответа.  Если параметр запроса **nextPageKey** не указан, всегда возвращается первая страница.  Когда **nextPageKey** задан для получения последующих страниц, все остальные параметры запроса нужно опустить. | query | Необязательный |
| pageSize | integer | Количество extensions в одном payload ответа.  Максимально допустимый размер страницы, 100.  Если не задано, используется 20. | query | Необязательный |
| extensionName | string | Имя требуемого extension 2.0. | path | Обязательный |
| version | string | Фильтрует результирующий набор конфигураций по версии extension 2.0. | query | Необязательный |
| active | boolean | Фильтрует результирующий набор конфигураций по активному состоянию. | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ExtensionMonitoringConfigurationsList](#openapi-definition-ExtensionMonitoringConfigurationsList) | Успех |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Входные данные некорректны. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Запрашиваемый ресурс не существует. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ExtensionMonitoringConfigurationsList`

| Элемент | Тип | Описание |
| --- | --- | --- |
| items | [ExtensionMonitoringConfiguration[]](#openapi-definition-ExtensionMonitoringConfiguration) | Список monitoring configurations extension. |
| nextPageKey | string | Курсор для следующей страницы результатов. На последней странице имеет значение `null`.  Используйте его в параметре запроса **nextPageKey** для получения последующих страниц результата. |
| pageSize | integer | Количество записей на странице. |
| totalCount | integer | Общее количество записей в результате. |

#### Объект `ExtensionMonitoringConfiguration`

| Элемент | Тип | Описание |
| --- | --- | --- |
| objectId | string | ID конфигурации |
| scope | string | Scope конфигурации |
| value | object | Конфигурация |

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



"items": [



{



"objectId": "string",



"scope": "string",



"value": {}



}



],



"nextPageKey": "AQAAABQBAAAABQ==",



"pageSize": 1,



"totalCount": 1



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