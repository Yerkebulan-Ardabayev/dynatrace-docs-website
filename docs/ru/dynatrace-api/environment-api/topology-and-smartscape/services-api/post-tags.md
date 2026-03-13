---
title: Services API - POST tags
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/services-api/post-tags
scraped: 2026-03-05T21:27:10.445414
---

# Services API - POST tags

# Services API - POST tags

* Справочник
* Обновлено 22 марта 2023 г.
* Устарело

Назначает [пользовательские теги](/docs/manage/tags-and-metadata "Используйте теги и метаданные для организации данных в вашей среде Dynatrace.") указанному сервису. Необходимо указать только значение тега. Контекст `CONTEXTLESS` будет назначен автоматически.

Использование этого API ограничено тегами с только значением. Для назначения тегов формата ключ:значение используйте [Custom tags API](/docs/dynatrace-api/environment-api/custom-tags/post-tags "Назначайте пользовательские теги отслеживаемым сущностям через Dynatrace API.").

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/services/{meIdentifier}` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/services/{meIdentifier}` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью `DataExport`.

Чтобы узнать, как его получить и использовать, см. раздел [Токены и аутентификация](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| meIdentifier | string | Идентификатор сущности Dynatrace для запрашиваемого сервиса. | path | Обязательный |
| body | [UpdateEntity](#openapi-definition-UpdateEntity) | Список тегов, которые необходимо назначить сущности Dynatrace. | body | Необязательный |

### Объекты тела запроса

#### Объект `UpdateEntity`

Список тегов, которые необходимо назначить сущности Dynatrace.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| tags | string[] | Список тегов, которые необходимо назначить сущности Dynatrace. | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса с возможными элементами. Её необходимо адаптировать для использования в реальном запросе.

```
{



"tags": [



"office-linz",



"office-klagenfurt"



]



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успешно. Параметры сервиса были обновлены. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Входные данные недопустимы. |
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
| code | integer | Код статуса HTTP |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | Элемент может принимать следующие значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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

В этом примере запрос назначает тег **PHP** сервису **PHP-FPM via domain socket /run/php7-fpm.sock** с идентификатором **SERVICE-72503CBDD2AEF066**.

Токен API передаётся в заголовке **Authorization**.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/entity/services/SERVICE-72503CBDD2AEF066 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"tags": [



"PHP"



]



}'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/services/SERVICE-72503CBDD2AEF066
```

#### Тело запроса

```
{



"tags": [



"PHP"



]



}
```

#### Код ответа

204

## Связанные темы

* [Services](/docs/observe/application-observability/services "Узнайте, как отслеживать и анализировать ваши сервисы, определять и использовать атрибуты запросов и многое другое.")
