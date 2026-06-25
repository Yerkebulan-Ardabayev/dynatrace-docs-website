---
title: Synthetic monitors API - GET все мониторы
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/synthetic-monitors/get-all-monitors
scraped: 2026-05-12T11:59:43.388358
---

# Synthetic monitors API - GET все мониторы

# Synthetic monitors API - GET все мониторы

* Справочник
* Опубликовано 25 июля 2019 г.

Возвращает список всех синтетических мониторов в вашем окружении. Список содержит только имена и ID мониторов. Чтобы получить детали, используйте вызов [**GET a monitor**](/managed/dynatrace-api/environment-api/synthetic/synthetic-monitors/get-a-monitor "Просмотр синтетического монитора через Synthetic v1 API.").

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/synthetic/monitors` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/synthetic/monitors` |

## Аутентификация

Для выполнения запроса нужен access-токен с одним из следующих scope:

* `ExternalSyntheticIntegration`
* `DataExport`
* `ReadSyntheticData`

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| managementZone | integer | Фильтрует итоговый набор мониторов, оставляя те, что входят в указанную management zone.  Укажите здесь ID management zone. | query | Необязательный |
| tag | string[] | Фильтрует итоговый набор мониторов по указанным тегам.  Можно указать несколько тегов в формате: `tag=tag1&tag=tag2`. Монитор должен соответствовать **всем** указанным тегам.  В случае тегов «ключ-значение», например импортированных тегов AWS или CloudFoundry, используйте формат: `[context]key:value`. | query | Необязательный |
| location | string | Фильтрует итоговый набор мониторов, оставляя те, что назначены указанной синтетической локации.  Укажите здесь ID локации. | query | Необязательный |
| assignedApps | string[] | Фильтрует итоговый набор мониторов, оставляя те, что назначены указанным приложениям.  Можно указать несколько приложений в формате: `assignedApps=app1&assignedApps=app2`. Монитору должны быть назначены **все** указанные приложения.  Укажите здесь Dynatrace entity ID приложений. | query | Необязательный |
| type | string | Фильтрует итоговый набор мониторов, оставляя те, что имеют указанный тип: `BROWSER` или `HTTP`. | query | Необязательный |
| enabled | boolean | Фильтрует итоговый набор мониторов, оставляя те, что включены (`true`) или отключены (`false`). | query | Необязательный |
| credentialId | string | Фильтрует итоговый набор мониторов, оставляя те, что используют указанный набор учётных данных.  Укажите здесь ID набора учётных данных. | query | Необязательный |
| credentialOwner | string | Фильтрует итоговый набор мониторов, оставляя те, что используют учётные данные, принадлежащие указанному пользователю. | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [Monitors](#openapi-definition-Monitors) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `Monitors`

Список синтетических мониторов

| Поле | Тип | Описание |
| --- | --- | --- |
| monitors | [MonitorCollectionElement[]](#openapi-definition-MonitorCollectionElement) | Список синтетических мониторов. |

#### Объект `MonitorCollectionElement`

Краткое представление синтетического монитора.

| Поле | Тип | Описание |
| --- | --- | --- |
| enabled | boolean | Состояние синтетического монитора. |
| entityId | string | ID синтетического объекта. |
| name | string | Имя синтетического объекта. |
| type | string | Тип синтетического монитора. Поле может принимать значения: * `BROWSER` * `HTTP` |

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



"monitors": [



{



"enabled": true,



"entityId": "string",



"name": "string",



"type": "BROWSER"



}



]



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

## Пример

В этом примере запрос возвращает список всех доступных мониторов окружения **mySampleEnv**.

API-токен передаётся в заголовке **Authorization**.

Результат усечён до первых трёх записей.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/monitors \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/monitors
```

#### Тело ответа

```
{



"monitors": [



{



"name": "easyTravel Angular",



"entityId": "SYNTHETIC_TEST-000000000000C69F"



},



{



"name": "dynatrace.com",



"entityId": "SYNTHETIC_TEST-0000000000025434"



},



{



"name": "easytravel special offers",



"entityId": "SYNTHETIC_TEST-000000000000987A"



}



]



}
```

#### Код ответа

200

## Связанные темы

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать браузерный монитор одного URL, браузерный clickpath или HTTP-монитор.")