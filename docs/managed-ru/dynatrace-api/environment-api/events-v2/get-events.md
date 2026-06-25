---
title: Events API v2 - GET списка событий
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/events-v2/get-events
scraped: 2026-05-12T11:12:15.477000
---

# Events API v2 - GET списка событий

# Events API v2 - GET списка событий

* Reference
* Published Aug 06, 2021

Выводит список событий, произошедших в указанный временной интервал, вместе с их свойствами.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/events` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/events` |

## Аутентификация

Для выполнения запроса необходим access token со scope `events.read`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательность |
| --- | --- | --- | --- | --- |
| nextPageKey | string | Курсор для следующей страницы результатов. Его можно найти в поле **nextPageKey** предыдущего ответа.  Первая страница возвращается всегда, если параметр запроса **nextPageKey** не указан.  Когда **nextPageKey** задан для получения последующих страниц, все остальные query-параметры должны быть пропущены. | query | Опциональный |
| pageSize | integer | Количество событий в одном теле ответа.  Максимально допустимый размер страницы 1000.  Если не задано, используется 100. | query | Опциональный |
| from | string | Начало запрашиваемого временного интервала.  Можно использовать один из следующих форматов:  * Временная метка в UTC-миллисекундах. * Человеко-читаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды опциональны. * Относительный временной интервал, отсчитываемый назад от текущего момента. Формат: `now-NU/A`, где `N` это объём времени, `U` это единица времени, а `A` это выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w` это один год назад, выравненный по неделе.   Относительный интервал можно задавать и без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного интервала: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, используется относительный интервал в два часа (`now-2h`). | query | Опциональный |
| to | string | Конец запрашиваемого временного интервала.  Можно использовать один из следующих форматов:  * Временная метка в UTC-миллисекундах. * Человеко-читаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды опциональны. * Относительный временной интервал, отсчитываемый назад от текущего момента. Формат: `now-NU/A`, где `N` это объём времени, `U` это единица времени, а `A` это выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w` это один год назад, выравненный по неделе.   Относительный интервал можно задавать и без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного интервала: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, используется текущая временная метка. | query | Опциональный |
| eventSelector | string | Определяет область запроса. В ответ включаются только события, соответствующие указанным критериям.  Можно добавить один или несколько перечисленных ниже критериев. Для каждого критерия можно указать несколько значений через запятую, если не указано иначе. Если указано несколько значений, применяется логика **OR**.  * ID события: `eventId("id-1", "id-2")`. * ID связанной сущности: `entityId("id-1", "id-2")`. * Статус события: `status("OPEN")` или `status("CLOSED")`. Можно указать только один статус. * ID зоны управления: `managementZoneId("123", "321")`. * Тип события: `eventType("event-type")`. Можно указать только один тип события. Получить список возможных типов событий можно с помощью вызова [GET типов событий](https://dt-url.net/qc03u6w). * ID корреляции: `correlationId("id-1", "id-2")`. * Произошло во время технического обслуживания (true, false): `underMaintenance(true)`. * Уведомления подавлены (true, false): `suppressAlert(true)`. * Создание проблемы подавлено (true, false): `suppressProblem(true)`. * Частое событие (true, false): `frequentEvent(true)`. * Свойство события: `property.<key>("value-1", "value-2")`. Можно использовать только свойства, у которых **filterable** установлено в `true`. Проверить свойства событий можно через вызов [GET свойств событий](https://dt-url.net/es03nwo).  Чтобы задать несколько критериев, разделите их запятыми (`,`). В ответ включаются только результаты, соответствующие **всем** критериям. | query | Опциональный |
| entitySelector | string | Область сущностей для запроса. Необходимо задать один из следующих критериев:  * Тип сущности: `type("TYPE")` * ID сущности Dynatrace: `entityId("id")`. Можно указать несколько ID через запятую (`entityId("id-1","id-2")`). Все запрошенные сущности должны быть одного типа.  Можно добавить один или несколько следующих критериев. Значения чувствительны к регистру, используется оператор `EQUALS`, если не указано иное.  * Тег: `tag("value")`. Теги в форматах `[context]key:value`, `key:value` и `value` распознаются и разбираются автоматически. Любые двоеточия (`:`), являющиеся частью ключа или значения, должны экранироваться обратной косой чертой (`\`). В противном случае двоеточие будет интерпретировано как разделитель между ключом и значением. Все значения тегов чувствительны к регистру. * ID зоны управления: `mzId(123)` * Имя зоны управления: `mzName("value")` * Имя сущности: + `entityName.equals`: выполняет регистронечувствительный запрос `EQUALS`.   + `entityName.startsWith`: меняет оператор на `BEGINS WITH`.   + `entityName.in`: позволяет передать несколько значений. Применяется оператор `EQUALS`.   + `caseSensitive(entityName.equals("value"))`: принимает любой критерий имени сущности в качестве аргумента и делает значение чувствительным к регистру. * Состояние здоровья (HEALTHY,UNHEALTHY): `healthState("HEALTHY")` * Временная метка первого появления: `firstSeenTms.<operator>(now-3h)`. Используйте любой формат временной метки из параметров **from**/**to**.   Доступны следующие операторы: + `lte`: раньше или в указанный момент времени   + `lt`: раньше указанного момента времени   + `gte`: позже или в указанный момент времени   + `gt`: позже указанного момента времени * Атрибут сущности: `<attribute>("value1","value2")` и `<attribute>.exists()`. Чтобы получить список доступных атрибутов, выполните запрос [GET типа сущности](https://dt-url.net/2ka3ivt) и проверьте поле **properties** ответа. * Связи: `fromRelationships.<relationshipName>()` и `toRelationships.<relationshipName>()`. Этот критерий принимает селектор сущностей в качестве атрибута. Чтобы получить список доступных связей, выполните запрос [GET типа сущности](https://dt-url.net/2ka3ivt) и проверьте поля **fromRelationships** и **toRelationships**. * Отрицание: `not(<criterion>)`. Инвертирует любой критерий, кроме **type**.  Подробнее см. [Селектор сущностей](https://dt-url.net/apientityselector) в документации Dynatrace.  Чтобы задать несколько критериев, разделите их запятой (`,`). Например, `type("HOST"),healthState("HEALTHY")`. В ответ включаются только результаты, соответствующие **всем** критериям.  Максимальная длина строки 2000 символов.  Количество выбираемых сущностей ограничено 10000. | query | Опциональный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [EventList](#openapi-definition-EventList) | Успех. Ответ содержит список событий. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `EventList`

Список событий.

| Элемент | Тип | Описание |
| --- | --- | --- |
| events | [Event[]](#openapi-definition-Event) | Список событий. |
| nextPageKey | string | Курсор для следующей страницы результатов. На последней странице имеет значение `null`.  Используйте его в параметре запроса **nextPageKey**, чтобы получить последующие страницы результата. |
| pageSize | integer | Количество записей на странице. |
| totalCount | integer | Общее количество записей в результате. |
| warnings | string[] | Список предупреждений. |

#### Объект `Event`

Конфигурация события.

| Элемент | Тип | Описание |
| --- | --- | --- |
| correlationId | string | ID корреляции события. |
| endTime | integer | Временная метка закрытия события в UTC-миллисекундах.  Имеет значение `null`, если событие всё ещё активно. |
| entityId | [EntityStub](#openapi-definition-EntityStub) | Краткое представление мониторируемой сущности. |
| entityTags | [METag[]](#openapi-definition-METag) | Список тегов связанной сущности. |
| eventId | string | ID события. |
| eventType | string | Тип события. |
| frequentEvent | boolean | Если `true`, событие происходит [часто](https://dt-url.net/4da3kdg).  Частое событие не порождает проблему. |
| managementZones | [ManagementZone[]](#openapi-definition-ManagementZone) | Список всех зон управления, которым принадлежит событие. |
| properties | [EventProperty[]](#openapi-definition-EventProperty) | Список свойств события. |
| startTime | integer | Временная метка возникновения события в UTC-миллисекундах. |
| status | string | Статус события. Элемент может принимать значения * `CLOSED` * `OPEN` |
| suppressAlert | boolean | Статус оповещения во время [технического обслуживания](https://dt-url.net/b2123rg0):  * `false`: оповещение работает как обычно. * `true`: оповещение отключено. |
| suppressProblem | boolean | Статус обнаружения проблем во время [технического обслуживания](https://dt-url.net/b2123rg0):  * `false`: обнаружение проблем работает как обычно. * `true`: обнаружение проблем отключено. |
| title | string | Заголовок события. |
| underMaintenance | boolean | Если `true`, событие произошло, когда мониторируемая система находилась в режиме технического обслуживания. |

#### Объект `EntityStub`

Краткое представление мониторируемой сущности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| entityId | [EntityId](#openapi-definition-EntityId) | Краткое представление мониторируемой сущности. |
| name | string | Имя сущности.  Не включается в ответ, если сущность с соответствующим ID не найдена. |

#### Объект `EntityId`

Краткое представление мониторируемой сущности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | ID сущности. |
| type | string | Тип сущности. |

#### Объект `METag`

Тег мониторируемой сущности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| context | string | Происхождение тега, например AWS или Cloud Foundry.  Пользовательские теги используют значение `CONTEXTLESS`. |
| key | string | Ключ тега. |
| stringRepresentation | string | Строковое представление тега. |
| value | string | Значение тега. |

#### Объект `ManagementZone`

Краткое представление зоны управления.

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | ID зоны управления. |
| name | string | Имя зоны управления. |

#### Объект `EventProperty`

Свойство события.

| Элемент | Тип | Описание |
| --- | --- | --- |
| key | string | Ключ свойства события. |
| value | string | Значение свойства события. |

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
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"events": [



{



"correlationId": "933613657e1c8fcf",



"endTime": 1564039524182,



"entityId": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"entityTags": [



{



"context": "string",



"key": "string",



"stringRepresentation": "string",



"value": "string"



}



],



"eventId": "4293884258445543163_1564039524182",



"eventType": "LOW_DISK_SPACE",



"frequentEvent": true,



"managementZones": [



{



"id": "string",



"name": "string"



}



],



"properties": [



{



"key": "string",



"value": "string"



}



],



"startTime": 1564039524182,



"status": "OPEN",



"suppressAlert": true,



"suppressProblem": true,



"title": "High CPU load on host X",



"underMaintenance": true



}



],



"nextPageKey": "AQAAABQBAAAABQ==",



"pageSize": 1,



"totalCount": 1,



"warnings": [



"string"



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

В этом примере запрос выводит список всех событий типа **PROCESS\_RESTART** (`eventSelector=eventType("PROCESS_RESTART")`), произошедших за последние **2 часа** (`from=now-2h`) при активном maintenance window (`eventSelector=underMaintenance(true)`). Результат усечён до двух событий.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl --request GET \



--url 'https://mySampleEnv.live.dynatrace.com/api/v2/events?eventSelector=eventType(%22PROCESS_RESTART%22)%2CunderMaintenance(true)&from=now-2h' \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/events?eventSelector=eventType(%22PROCESS_RESTART%22)%2CunderMaintenance(true)&from=now-2h
```

#### Тело ответа

```
{



"totalCount": 43,



"pageSize": 100,



"events": [



{



"eventId": "-6475311485380369979_1628500180000",



"startTime": 1628500180000,



"endTime": 1628500240000,



"eventType": "PROCESS_RESTART",



"title": "Process restart",



"entityId": {



"entityId": {



"id": "PROCESS_GROUP_INSTANCE-03F98EA8639FD052",



"type": "PROCESS_GROUP_INSTANCE"



},



"name": "IIS app pool dotNetFrontend_easyTravel_x64"



},



"properties": [



{



"key": "dt.event.group_label",



"value": "Process restart"



}



],



"status": "OPEN",



"entityTags": [



{



"context": "CONTEXTLESS",



"key": "easyTravel",



"stringRepresentation": "easyTravel"



},



{



"context": "CONTEXTLESS",



"key": "tech",



"value": "IIS",



"stringRepresentation": "tech:IIS"



},



{



"context": "CONTEXTLESS",



"key": "tech",



"value": ".NET",



"stringRepresentation": "tech:.NET"



},



{



"context": "CONTEXTLESS",



"key": "hosts",



"value": "w-077",



"stringRepresentation": "hosts:w-077"



},



{



"context": "CONTEXTLESS",



"key": "Infrastructure",



"value": "Windows",



"stringRepresentation": "Infrastructure:Windows"



},



{



"context": "CONTEXTLESS",



"key": "dotNetFrontend",



"stringRepresentation": "dotNetFrontend"



},



],



"managementZones": [



{



"id": "9130632296508575249",



"name": "Easytravel"



},



{



"id": "-6239538939987181652",



"name": "frontend"



},



{



"id": "5130731705740636866",



"name": "Windows"



}



],



"underMaintenance": true,



"suppressAlert": true,



"suppressProblem": true,



"frequentEvent": false



},



{



"eventId": "-231290298591263162_1628500000000",



"startTime": 1628500000000,



"endTime": 1628500060000,



"eventType": "PROCESS_RESTART",



"title": "Process restart",



"entityId": {



"entityId": {



"id": "PROCESS_GROUP_INSTANCE-00CA9B0F1AE9BAF8",



"type": "PROCESS_GROUP_INSTANCE"



},



"name": "chromedriver_linux64"



},



"properties": [



{



"key": "dt.event.group_label",



"value": "Process restart"



}



],



"status": "CLOSED",



"entityTags": [



{



"context": "CONTEXTLESS",



"key": "Infrastructure",



"value": "Linux",



"stringRepresentation": "Infrastructure:Linux"



},



{



"context": "CONTEXTLESS",



"key": "hosts",



"value": "l-008",



"stringRepresentation": "hosts:l-008"



}



],



"managementZones": [



{



"id": "2631544906797876001",



"name": "Linux"



}



],



"underMaintenance": true,



"suppressAlert": false,



"suppressProblem": false,



"frequentEvent": false



}



],



"warnings": []



}
```

#### Код ответа

200

## Связанные темы

* [Категории событий](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Узнайте о различных категориях событий и поддерживаемых типах событий, об их уровнях серьёзности и логике их порождения.")
* [Анализ и корреляция событий](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Получите представление о секции Events на каждой странице обзора хоста, процесса и сервиса.")