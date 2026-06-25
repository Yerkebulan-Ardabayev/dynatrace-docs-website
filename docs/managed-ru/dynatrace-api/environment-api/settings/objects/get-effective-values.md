---
title: Settings API - GET effective values
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/objects/get-effective-values
scraped: 2026-05-12T11:38:47.251777
---

# Settings API - GET effective values

# Settings API - GET effective values

* Reference
* Published Aug 26, 2022

Возвращает список фактических значений настроек для указанных schemas на указанном scope.

Если для указанной комбинации schema/scope нет доступных settings objects, запрос возвращает значения настроек по умолчанию.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/effectiveValues` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/settings/effectiveValues` |

## Аутентификация

Для выполнения запроса необходим access token со scope `settings.read`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| schemaIds | string | Список разделённых запятыми schema IDs, к которым относятся запрашиваемые объекты.  Учитывается только при загрузке первой страницы, когда **nextPageKey** не задан. | query | Optional |
| scope | string | Scope, на который нацелены запрашиваемые объекты.  Выборка сопоставляет только объекты, напрямую нацеленные на указанный scope. Например, `environment` не сопоставит объекты, нацеленные на хост внутри окружения. Подробнее см. [Dynatrace Documentation](https://dt-url.net/ky03459).  Для загрузки первой страницы, когда **nextPageKey** не задан, этот параметр обязателен. | query | Optional |
| fields | string | Список полей, включаемых в ответ. Предоставленный набор полей заменяет набор по умолчанию.  Укажите нужные поля верхнего уровня, разделённые запятыми (например, `origin,value`).  Поддерживаемые поля: `summary`, `searchSummary`, `created`, `modified`, `createdBy`, `modifiedBy`, `author`, `origin`, `schemaId`, `schemaVersion`, `value`, `externalId`. | query | Optional |
| nextPageKey | string | Курсор для следующей страницы результатов. Вы можете найти его в поле **nextPageKey** предыдущего ответа.  Первая страница всегда возвращается, если вы не указываете query-параметр **nextPageKey**.  Когда **nextPageKey** задан для получения последующих страниц, вы должны опустить все остальные query-параметры. | query | Optional |
| pageSize | integer | Количество settings objects в одном payload ответа.  Максимально допустимый размер страницы: 500.  Если не задан, используется 100. | query | Optional |
| adminAccess | boolean | Если установлено в true и у пользователя есть право settings:objects:admin, endpoint будет действовать так, как будто пользователь является владельцем всех объектов | query | Optional |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [EffectiveSettingsValuesList](#openapi-definition-EffectiveSettingsValuesList) | Успех |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Указанная schema или scope не найдены. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `EffectiveSettingsValuesList`

Список фактических значений настроек.

| Элемент | Тип | Описание |
| --- | --- | --- |
| items | [EffectiveSettingsValue[]](#openapi-definition-EffectiveSettingsValue) | Список фактических значений настроек. |
| nextPageKey | string | Курсор для следующей страницы результатов. На последней странице имеет значение `null`.  Используйте его в query-параметре **nextPageKey** для получения последующих страниц результата. |
| pageSize | integer | Количество записей на странице. |
| totalCount | integer | Общее количество записей в результате. |

#### Объект `EffectiveSettingsValue`

Фактическое значение настройки.

| Элемент | Тип | Описание |
| --- | --- | --- |
| author | string | Пользователь (идентифицированный по ID пользователя или ID публичного токена), который выполнил эту последнюю модификацию. |
| created | integer | Временная метка создания. |
| externalId | string | Внешний идентификатор settings object. |
| modified | integer | Временная метка последней модификации. |
| origin | string | Источник значения настройки. |
| schemaId | string | Schema, на которой основан объект. |
| schemaVersion | string | Версия schema, на которой основан объект. |
| searchSummary | string | Доступная для поиска строка-сводка значения настройки. Обычный текст без Markdown. |
| summary | string | Краткая сводка настроек. Может содержать Markdown и будет соответствующим образом экранирована. |
| value | string | Значение настройки.  Оно определяет фактические значения параметров настроек.  Фактическое содержимое зависит от schema объекта. |

#### Объект `AnyValue`

Schema, представляющая произвольный тип значения.

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"items": [



{



"author": "john.doe@example.com",



"created": 1,



"externalId": "string",



"modified": 1,



"origin": "HOST-D3A3C5A146830A79",



"schemaId": "builtin:container.built-in-monitoring-rule",



"schemaVersion": "1.0.0",



"searchSummary": "string",



"summary": "string",



"value": "string"



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