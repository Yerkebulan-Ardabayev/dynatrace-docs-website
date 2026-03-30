---
title: Applications API - GET all apps
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-all
scraped: 2026-03-05T21:26:54.216194
---

# Applications API — GET всех приложений


* Устарело

Этот API устарел. Вместо него используйте API отслеживаемых сущностей. Дополнительную информацию о переходе на новый API можно найти в руководстве по миграции.

Извлекает список всех приложений в вашей среде Dynatrace вместе с их параметрами.

Полный список может быть длинным, поэтому вы можете сузить его, указав параметры фильтрации, такие как теги. Подробнее см. в разделе **Параметры**.

Вы также можете ограничить вывод с помощью пагинации:

1. Укажите количество результатов на странице в параметре запроса **pageSize**.
2. Затем используйте курсор из заголовка ответа **Next-Page-Key** в параметре запроса **nextPageKey** для получения последующих страниц.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/applications` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/applications` |

## Аутентификация

Для выполнения этого запроса вам нужен токен доступа с областью действия `DataExport`.

Чтобы узнать, как получить и использовать его, см. Токены и аутентификация.

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательность |
| --- | --- | --- | --- | --- |
| startTimestamp | integer | Начальная метка времени запрашиваемого временного диапазона, в миллисекундах (UTC). Если не указана, используется значение 72 часа назад от текущего момента. | query | Необязательно |
| endTimestamp | integer | Конечная метка времени запрашиваемого временного диапазона, в миллисекундах (UTC). Если не указана, используется текущая метка времени. Временной диапазон не должен превышать 3 дня. | query | Необязательно |
| relativeTime | string | Относительный временной диапазон, отсчитываемый от текущего момента. Элемент может содержать следующие значения: * `min` * `5mins` * `10mins` * `15mins` * `30mins` * `hour` * `2hours` * `6hours` * `day` * `3days` | query | Необязательно |
| tag | string[] | Фильтрует результирующий набор приложений по указанному тегу. Вы можете указать несколько тегов в следующем формате: `tag=tag1&tag=tag2`. Приложение должно соответствовать **всем** указанным тегам. Для тегов типа ключ-значение, таких как импортированные теги AWS или CloudFoundry, используйте следующий формат: `tag=[context]key:value`. Для пользовательских тегов типа ключ-значение опустите контекст: `tag=key:value`. | query | Необязательно |
| entity | string[] | Фильтрует результат только указанными приложениями. Для указания нескольких приложений используйте следующий формат: `entity=ID1&entity=ID2`. | query | Необязательно |
| managementZone | integer | Возвращает только приложения, которые являются частью указанной зоны управления. | query | Необязательно |
| includeDetails | boolean | Включает (`true`) или исключает (`false`) детали, которые запрашиваются из связанных сущностей. Исключение деталей может ускорить запросы. Если не указано, используется значение `true`. | query | Необязательно |
| pageSize | integer | Количество приложений на страницу результатов. Если не указано, пагинация не используется и результат содержит все приложения, соответствующие указанным критериям фильтрации. | query | Необязательно |
| nextPageKey | string | Курсор для следующей страницы результатов. Его можно найти в заголовке **Next-Page-Key** предыдущего ответа. При использовании пагинации первая страница всегда возвращается без этого курсора. Все остальные параметры запроса должны оставаться такими же, как в первом запросе, для получения последующих страниц. | query | Необязательно |

## Заголовки ответа

| Заголовок | Тип | Описание |
| --- | --- | --- |
| Total-Count | integer | Оценочное количество результатов. |
| Next-Page-Key | string | Курсор для следующей страницы результатов. Без него вы получите первую страницу снова. |
| Page-Size | string | Максимальное количество результатов на странице. |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [Application[]](#openapi-definition-Application) | Успешно |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Недопустимые входные данные. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ResponseBody`

#### Объект `Application`

| Элемент | Тип | Описание |
| --- | --- | --- |
| applicationMatchTarget | string | -Элемент может содержать следующие значения: * `DOMAIN` * `URL` |
| applicationType | string | -Элемент может содержать следующие значения: * `AGENTLESS_MONITORING` * `AUTO_INJECTED` * `DEFAULT` * `SAAS_VENDOR` |
| customizedName | string | Пользовательское имя сущности |
| discoveredName | string | Обнаруженное имя сущности |
| displayName | string | Имя сущности Dynatrace, отображаемое в пользовательском интерфейсе. |
| entityId | string | Идентификатор сущности Dynatrace для запрашиваемой сущности. |
| firstSeenTimestamp | integer | Метка времени первого обнаружения сущности, в миллисекундах UTC |
| fromRelationships | object | Список исходящих вызовов от приложения. |
| lastSeenTimestamp | integer | Метка времени последнего обнаружения сущности, в миллисекундах UTC |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | Зоны управления, к которым принадлежит сущность. |
| ruleAppliedMatchType | string | -Элемент может содержать следующие значения: * `ALL_URLS_AND_DOMAINS` * `CONTAINS` * `ENDS` * `EQUALS` * `MATCHES` * `STARTS` |
| ruleAppliedPattern | string | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | Список тегов сущности. |
| toRelationships | object | Список входящих вызовов к приложению. |

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | Идентификатор сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

#### Объект `TagInfo`

Тег сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| context | string | Источник тега, например AWS или Cloud Foundry. Пользовательские теги используют значение `CONTEXTLESS`. Элемент может содержать следующие значения: * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | Ключ тега. Для пользовательских тегов здесь хранится значение тега. |
| value | string | Значение тега. Не применимо к пользовательским тегам. |

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
| parameterLocation | string | -Элемент может содержать следующие значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
[


{


"applicationMatchTarget": "DOMAIN",


"applicationType": "AGENTLESS_MONITORING",


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

В этом примере запрос извлекает список всех приложений в среде.

API-токен передаётся в заголовке **Authorization**.

Результат сокращён до трёх записей.

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

* Мониторинг реальных пользователей
