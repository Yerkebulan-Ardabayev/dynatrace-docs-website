---
title: Settings API - GET effective values
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/settings/objects/get-effective-values
scraped: 2026-03-06T21:34:40.987848
---

# Settings API — GET effective values (получение эффективных значений)


Возвращает список эффективных значений настроек для указанных схем в указанной области действия.

Если для указанной комбинации схемы/области действия нет доступных объектов настроек, запрос возвращает значения по умолчанию для настроек.

Запрос возвращает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/effectiveValues` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/settings/effectiveValues` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью действия `settings.read`.

О том, как получить и использовать токен, см. в разделе Токены и аутентификация.

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| schemaIds | string | Список идентификаторов схем, разделённых запятыми, к которым принадлежат запрашиваемые объекты.  Учитывается только при загрузке первой страницы, когда параметр **nextPageKey** не задан. | query | Необязательный |
| scope | string | Область действия, на которую нацелены запрашиваемые объекты.  Выборка совпадает только с объектами, непосредственно нацеленными на указанную область. Например, `environment` не совпадёт с объектами, нацеленными на хост в среде. Подробнее см. [Документация Dynatrace](https://dt-url.net/ky03459).  Для загрузки первой страницы, когда параметр **nextPageKey** не задан, этот параметр обязателен. | query | Необязательный |
| fields | string | Список полей для включения в ответ. Указанный набор полей заменяет набор по умолчанию.  Укажите необходимые поля верхнего уровня через запятую (например, `origin,value`).  Поддерживаемые поля: `summary`, `searchSummary`, `created`, `modified`, `createdBy`, `modifiedBy`, `author`, `origin`, `schemaId`, `schemaVersion`, `value`, `externalId`. | query | Необязательный |
| nextPageKey | string | Курсор для следующей страницы результатов. Его можно найти в поле **nextPageKey** предыдущего ответа.  Первая страница всегда возвращается, если параметр запроса **nextPageKey** не указан.  Когда **nextPageKey** установлен для получения последующих страниц, все остальные параметры запроса должны быть опущены. | query | Необязательный |
| pageSize | integer | Количество объектов настроек в одном ответе.  Максимально допустимый размер страницы — 500.  Если не задан, используется значение 100. | query | Необязательный |
| adminAccess | boolean | Если установлено значение true и пользователь имеет разрешение settings:objects:admin, конечная точка будет действовать так, как будто пользователь является владельцем всех объектов | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [EffectiveSettingsValuesList](#openapi-definition-EffectiveSettingsValuesList) | Успех |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Указанная схема или область действия не найдена. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `EffectiveSettingsValuesList`

Список эффективных значений настроек.

| Элемент | Тип | Описание |
| --- | --- | --- |
| items | [EffectiveSettingsValue[]](#openapi-definition-EffectiveSettingsValue) | Список эффективных значений настроек. |
| nextPageKey | string | Курсор для следующей страницы результатов. Имеет значение `null` на последней странице.  Используйте его в параметре запроса **nextPageKey** для получения последующих страниц результата. |
| pageSize | integer | Количество записей на странице. |
| totalCount | integer | Общее количество записей в результате. |

#### Объект `EffectiveSettingsValue`

Эффективное значение настройки.

| Элемент | Тип | Описание |
| --- | --- | --- |
| author | string | Пользователь (идентифицируемый по идентификатору пользователя или публичному идентификатору токена), который выполнил последнее изменение. |
| created | integer | Временная метка создания. |
| externalId | string | Внешний идентификатор объекта настройки. |
| modified | integer | Временная метка последнего изменения. |
| origin | string | Источник значения настройки. |
| schemaId | string | Схема, на которой основан объект. |
| schemaVersion | string | Версия схемы, на которой основан объект. |
| searchSummary | string | Доступная для поиска сводка значения настройки. Простой текст без Markdown. |
| summary | string | Краткая сводка настроек. Может содержать Markdown и будет экранирована соответствующим образом. |
| value | string | Значение настройки.  Определяет фактические значения параметров настроек.  Фактическое содержимое зависит от схемы объекта. |

#### Объект `AnyValue`

Схема, представляющая произвольный тип значения.

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код состояния HTTP |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | - Элемент может содержать следующие значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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
