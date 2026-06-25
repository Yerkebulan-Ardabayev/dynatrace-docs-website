---
title: Extensions API - GET all extension's instances
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/extensions-api/get-all-instances
scraped: 2026-05-12T11:19:56.000353
---

# Extensions API - GET all extension's instances

# Extensions API - GET all extension's instances

* Reference
* Published Mar 06, 2020

Выводит список всех экземпляров указанного расширения.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/instances` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/instances` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID требуемого расширения. | path | Required |
| pageSize | integer | Количество результатов на страницу. Должно быть от 1 до 500 | query | Optional |
| nextPageKey | string | Курсор для следующей страницы результатов. | query | Optional |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ExtensionConfigurationList](#openapi-definition-ExtensionConfigurationList) | Успех |

### Объекты тела ответа

#### Объект `ExtensionConfigurationList`

Список конфигураций.

| Элемент | Тип | Описание |
| --- | --- | --- |
| configurationsList | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | Список конфигураций. |
| nextPageKey | string | Курсор для следующей страницы результатов. На последней странице имеет значение `null`.  Используйте его в query-параметре **nextPageKey** для получения последующих страниц результата. |
| totalResults | integer | Общее количество записей в результате. |

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

### JSON-модели тела ответа

```
{



"configurationsList": [



{



"id": "HOST-E1550E0AED6A572F"



}



],



"nextPageToken": "LlUdYmu5S2MfX/ppfCInR9M=",



"totalResults": 9



}
```

## Связанные темы

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Разработка собственных Extensions в Dynatrace.")