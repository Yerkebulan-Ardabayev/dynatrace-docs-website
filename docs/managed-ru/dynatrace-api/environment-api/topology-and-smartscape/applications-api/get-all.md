---
title: Applications API - GET all apps
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-all
scraped: 2026-05-12T12:02:09.098603
---

# Applications API - GET all apps

# Applications API - GET all apps

* Reference
* Updated on Mar 22, 2023
* Deprecated

Этот API устарел. Используйте [Monitored entities API](/managed/dynatrace-api/environment-api/entity-v2 "Узнайте о Dynatrace Monitored entities API.") вместо него.

Получает список всех [приложений](/managed/discover-dynatrace/get-started/glossary#app "Познакомьтесь с терминологией Dynatrace.") в вашем окружении Dynatrace вместе с их параметрами.

Полный список может быть длинным, поэтому его можно сузить, указав параметры фильтрации, например теги. Подробнее см. в разделе **Parameters**.

Дополнительно можно ограничить вывод с помощью постраничной разбивки:

1. Укажите количество результатов на странице в query-параметре **pageSize**.
2. Затем используйте курсор из заголовка ответа **Next-Page-Key** в query-параметре **nextPageKey**, чтобы получить следующие страницы.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/entity/applications` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/entity/applications` |

## Аутентификация

Для выполнения запроса необходим access token со scope `DataExport`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| startTimestamp | integer | Начальная метка времени запрашиваемого диапазона, в миллисекундах (UTC).  Если не задана, используется 72 часа назад от текущего момента. | query | Optional |
| endTimestamp | integer | Конечная метка времени запрашиваемого диапазона, в миллисекундах (UTC).  Если не задана, используется текущая метка времени.  Диапазон не должен превышать 3 дня. | query | Optional |
| relativeTime | string | Относительный диапазон, назад от текущего момента. Возможные значения: * `min` * `5mins` * `10mins` * `15mins` * `30mins` * `hour` * `2hours` * `6hours` * `day` * `3days` | query | Optional |
| tag | string[] | Фильтрует результирующий набор приложений по указанному тегу. Можно указать несколько тегов в следующем формате: `tag=tag1&tag=tag2`. Приложение должно соответствовать **всем** указанным тегам.  В случае тегов key-value, например импортированных тегов AWS или CloudFoundry, используйте следующий формат: `tag=[context]key:value`. Для пользовательских тегов key-value опустите context: `tag=key:value`. | query | Optional |
| entity | string[] | Ограничивает результат только указанными приложениями.  Чтобы указать несколько приложений, используйте следующий формат: `entity=ID1&entity=ID2`. | query | Optional |
| managementZone | integer | Возвращать только приложения, входящие в указанную management zone. | query | Optional |
| includeDetails | boolean | Включает (`true`) или исключает (`false`) детали, запрашиваемые у связанных сущностей.  Исключение деталей может ускорить запросы.  Если не задано, используется `true`. | query | Optional |
| pageSize | integer | Количество приложений на странице результатов.  Если не задано, постраничная разбивка не используется и результат содержит все приложения, подходящие под указанные критерии фильтрации. | query | Optional |
| nextPageKey | string | Курсор для следующей страницы результатов. Его можно найти в заголовке **Next-Page-Key** предыдущего ответа.  Если вы используете постраничную разбивку, первая страница всегда возвращается без этого курсора.  Чтобы получить следующие страницы, нужно сохранить все остальные query-параметры такими, как в первом запросе. | query | Optional |

## Заголовки ответа

| Заголовок | Тип | Описание |
| --- | --- | --- |
| Total-Count | integer | Оценочное количество результатов. |
| Next-Page-Key | string | Курсор для следующей страницы результатов. Без него снова вернётся первая страница. |
| Page-Size | string | Максимальное количество результатов на странице. |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [Application[]](#openapi-definition-Application) | Успех |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ResponseBody`

#### Объект `Application`

| Элемент | Тип | Описание |
| --- | --- | --- |
| applicationMatchTarget | string | -Возможные значения: * `DOMAIN` * `URL` |
| applicationType | string | -Возможные значения: * `AGENTLESS_MONITORING` * `AUTO_INJECTED` * `DEFAULT` * `SAAS_VENDOR` |
| attributes | object | - |
| customizedName | string | Пользовательское имя сущности |
| discoveredName | string | Обнаруженное имя сущности |
| displayName | string | Имя сущности Dynatrace в том виде, как оно отображается в UI. |
| entityId | string | ID сущности Dynatrace для нужной сущности. |
| firstSeenTimestamp | integer | Метка времени, когда сущность была впервые обнаружена, в миллисекундах UTC |
| fromRelationships | object | Список исходящих вызовов от приложения. |
| lastSeenTimestamp | integer | Метка времени, когда сущность была обнаружена в последний раз, в миллисекундах UTC |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | Management zone'ы, частью которых является сущность. |
| ruleAppliedMatchType | string | -Возможные значения: * `ALL_URLS_AND_DOMAINS` * `CONTAINS` * `ENDS` * `EQUALS` * `MATCHES` * `STARTS` |
| ruleAppliedPattern | string | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | Список тегов сущности. |
| toRelationships | object | Список входящих вызовов к приложению. |

#### Объект `AnyValue`

Схема, представляющая произвольный тип значения.

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

#### Объект `TagInfo`

Тег сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| context | string | Происхождение тега, например AWS или Cloud Foundry.  Пользовательские теги используют значение `CONTEXTLESS`. Возможные значения: * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | Ключ тега.  У пользовательских тегов здесь находится значение тега. |
| value | string | Значение тега.  Не применимо к пользовательским тегам. |

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
[



{



"applicationMatchTarget": "DOMAIN",



"applicationType": "AGENTLESS_MONITORING",



"attributes": {



"empty": true



},



"customizedName": "string",



"discoveredName": "string",



"displayName": "string",



"entityId": "string",



"firstSeenTimestamp": 1,



"fromRelationships": {



"calls": [



"string"



]



},



"lastSeenTimestamp": 1,



"managementZones": [



{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}



],



"ruleAppliedMatchType": "ALL_URLS_AND_DOMAINS",



"ruleAppliedPattern": "string",



"tags": [



{



"context": "AWS",



"key": "string",



"value": "string"



}



],



"toRelationships": {



"monitors": [



"string"



]



}



}



]
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

В этом примере запрос запрашивает список всех приложений в окружении.

API-токен передаётся в заголовке **Authorization**.

Результат усечён до трёх записей.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/entity/applications/ \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/applications
```

#### Тело ответа

```
[



{



"entityId": "APPLICATION-EA7C4B59F27D43EB",



"displayName": "RUM Default Application",



"customizedName": "RUM Default Application",



"discoveredName": "RUM Default Application",



"firstSeenTimestamp": 1422282024216,



"lastSeenTimestamp": 1538579528065,



"tags": [



{



"context": "CONTEXTLESS",



"key": "Mytag"



},



{



"context": "CONTEXTLESS",



"key": "Test"



}



],



"fromRelationships": {



"calls": [



"SERVICE-FFE4B7A6D72F2CAC"



]



},



"toRelationships": {},



"applicationType": "DEFAULT",



"ruleAppliedPattern": "http",



"managementZones": [



{



"id": "-6239538939987181652",



"name": "allTypes"



},



{



"id": "-2519468841583898843",



"name": "app name exists"



},



{



"id": "4485554873951847460",



"name": "Applications except easyTravel"



}



]



},



{



"entityId": "APPLICATION-BBFA55551D507E2B",



"displayName": "easyTravel Ionic Web",



"discoveredName": "easyTravel Ionic Web",



"firstSeenTimestamp": 1528695861873,



"lastSeenTimestamp": 1538572321269,



"tags": [],



"fromRelationships": {



"calls": [



"SERVICE-ED0B103392AC86BF"



]



},



"toRelationships": {},



"applicationType": "RUMONLY",



"managementZones": [



{



"id": "-6239538939987181652",



"name": "allTypes"



},



{



"id": "-4085081632192243904",



"name": "easyTravel"



}



]



},



{



"entityId": "MOBILE_APPLICATION-752C288D59734C79",



"displayName": "easyTravel Demo",



"customizedName": "easyTravel Demo",



"discoveredName": "752c288d-5973-4c79-b7d1-3a49d4d42ea0",



"firstSeenTimestamp": 1469613941393,



"lastSeenTimestamp": 1538654940201,



"tags": [



{



"context": "CONTEXTLESS",



"key": "portal"



},



{



"context": "CONTEXTLESS",



"key": "easyTravel"



}



],



"fromRelationships": {



"calls": [



"SERVICE-ED0B103392AC86BF"



]



},



"toRelationships": {},



"mobileOsFamily": [



"ANDROID",



"IOS",



"WINDOWS"



],



"managementZones": [



{



"id": "-4085081632192243904",



"name": "easyTravel"



}



]



}



]
```

#### Код ответа

200

## Связанные темы

* [Мониторинг реальных пользователей](/managed/observe/digital-experience/rum-concepts/rum-overview "Узнайте о Real User Monitoring, ключевых метриках производительности, мониторинге мобильных приложений и многом другом.")