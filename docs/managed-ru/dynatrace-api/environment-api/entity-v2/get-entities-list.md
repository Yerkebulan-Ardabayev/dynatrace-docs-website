---
title: API отслеживаемых сущностей - GET список сущностей
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/entity-v2/get-entities-list
scraped: 2026-05-12T11:57:12.938417
---

# API отслеживаемых сущностей - GET список сущностей

# API отслеживаемых сущностей - GET список сущностей

* Справочник
* Опубликовано 28 мая 2020 г.

Возвращает список сущностей, наблюдавшихся в указанном временном интервале, со всеми их свойствами. При запросе сущностей типа `SERVICE_METHOD` возвращаются только следующие запросы:

* [Ключевые запросы](/managed/observe/application-observability/services-classic/monitor-key-requests "Узнайте, как пристально мониторить запросы, критичные для бизнеса.").
* Top X запросов, используемых для [построения baseline](/managed/dynatrace-intelligence/anomaly-detection/automated-multidimensional-baselining "Узнайте, как Dynatrace AI автоматически рассчитывает baseline по многомерной схеме.").
* Запросы, которые вызвали [проблему](/managed/dynatrace-intelligence "Познакомьтесь с возможностями Davis AI.").

Размер вывода можно ограничить пагинацией:

1. Укажите число результатов на страницу в query-параметре **pageSize**.
2. Затем используйте курсор из поля **nextPageKey** предыдущего ответа в query-параметре **nextPageKey**, чтобы получать следующие страницы.

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/entities` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/entities` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `entities.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| nextPageKey | string | Курсор для следующей страницы результатов. Находится в поле **nextPageKey** предыдущего ответа. Первая страница возвращается всегда, если query-параметр **nextPageKey** не указан. Когда **nextPageKey** задан для получения следующих страниц, все остальные query-параметры нужно опустить. | query | Необязательный |
| pageSize | integer | Количество сущностей. Если не задан, используется 50. | query | Необязательный |
| entitySelector | string | Определяет область запроса. В ответ попадают только сущности, удовлетворяющие критериям. Необходимо указать один из критериев: * Тип сущности: `type("TYPE")` * Dynatrace entity ID: `entityId("id")`. Можно указать несколько ID через запятую (`entityId("id-1","id-2")`). Все запрашиваемые сущности должны быть одного типа. Дополнительно можно добавить один или несколько следующих критериев. Значения регистрозависимы, оператор по умолчанию `EQUALS`. * Тег: `tag("value")`. Теги в форматах `[context]key:value`, `key:value` и `value` распознаются и разбираются автоматически. Двоеточия (`:`), входящие в состав ключа или значения, должны быть экранированы обратной косой (`\`). Иначе они будут восприняты как разделитель между ключом и значением. Все значения тегов регистрозависимы. * ID зоны управления: `mzId(123)` * Имя зоны управления: `mzName("value")` * Имя сущности: + `entityName.equals`: выполняет регистронезависимый запрос `EQUALS`. + `entityName.startsWith`: меняет оператор на `BEGINS WITH`. + `entityName.in`: позволяет указать несколько значений. Применяется оператор `EQUALS`. + `caseSensitive(entityName.equals("value"))`: принимает любой критерий по имени сущности и делает сравнение регистрозависимым. * Состояние работоспособности (HEALTHY, UNHEALTHY): `healthState("HEALTHY")` * Метка времени первого обнаружения: `firstSeenTms.<operator>(now-3h)`. Используется любой формат timestamp из параметров **from**/**to**. Доступные операторы: + `lte`: раньше указанного времени или в это же время + `lt`: раньше указанного времени + `gte`: позже указанного времени или в это же время + `gt`: позже указанного времени * Атрибут сущности: `<attribute>("value1","value2")` и `<attribute>.exists()`. Список доступных атрибутов можно получить запросом [GET entity type](https://dt-url.net/2ka3ivt), посмотрев поле **properties** в ответе. * Связи: `fromRelationships.<relationshipName>()` и `toRelationships.<relationshipName>()`. Критерий принимает в качестве аргумента селектор сущностей. Список доступных связей можно получить запросом [GET entity type](https://dt-url.net/2ka3ivt), посмотрев поля **fromRelationships** и **toRelationships**. * Инверсия: `not(<criterion>)`. Инвертирует любой критерий, кроме **type**. Подробнее смотрите [Entity selector](https://dt-url.net/apientityselector) в документации Dynatrace. Чтобы указать несколько критериев, перечислите их через запятую (`,`). Например, `type("HOST"),healthState("HEALTHY")`. В ответ попадут только результаты, соответствующие **всем** критериям. Максимальная длина строки: 2 000 символов. Поле **обязательно** при запросе первой страницы результатов. | query | Необязательный |
| from | string | Начало запрашиваемого временного интервала. Можно использовать один из форматов: * Метка времени в UTC миллисекундах. * Читаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Можно использовать пробел вместо `T`. Секунды и доли секунды необязательны. * Относительный интервал назад от текущего момента. Формат `now-NU/A`, где `N`, количество, `U`, единица времени, `A`, выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w`, это год назад, выровненный по неделе. Можно указать относительный интервал и без выравнивания: `now-NU`. Поддерживаемые единицы времени для относительного интервала: + `m`: минуты + `h`: часы + `d`: дни + `w`: недели + `M`: месяцы + `y`: годы Если не задан, используется относительный интервал в три дня (`now-3d`). | query | Необязательный |
| to | string | Конец запрашиваемого временного интервала. Можно использовать один из форматов: * Метка времени в UTC миллисекундах. * Читаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Можно использовать пробел вместо `T`. Секунды и доли секунды необязательны. * Относительный интервал назад от текущего момента. Формат `now-NU/A`, где `N`, количество, `U`, единица времени, `A`, выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w`, это год назад, выровненный по неделе. Можно указать относительный интервал и без выравнивания: `now-NU`. Поддерживаемые единицы времени для относительного интервала: + `m`: минуты + `h`: часы + `d`: дни + `w`: недели + `M`: месяцы + `y`: годы Если не задан, используется текущая метка времени. | query | Необязательный |
| fields | string | Определяет список свойств сущности, включаемых в ответ. ID и имя сущности **всегда** включаются в ответ. Чтобы добавить свойства, перечислите их с ведущим плюсом `+`. Можно указать несколько свойств через запятую (например `fields=+lastSeenTms,+properties.BITNESS`). Чтобы получить список доступных свойств для вашего типа сущности, используйте запрос [GET entity type](https://dt-url.net/2ka3ivt). Поля из объекта **properties** должны указываться в формате `properties.FIELD` (например, `properties.BITNESS`). При запросе большого количества полей-связей возможно троттлинг (ограничение скорости). | query | Необязательный |
| sort | string | Задаёт порядок сортировки возвращаемых сущностей. Поле **необязательное**, каждое поле имеет знаковый префикс (+/-), который соответствует направлению сортировки (+ по возрастанию, - по убыванию). Если знак не указан, применяется сортировка по возрастанию. Сейчас сортировка доступна только по отображаемому имени (например `sort=name` или `sort=+name` по возрастанию, `sort=-name` по убыванию). | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [EntitiesList](#openapi-definition-EntitiesList) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `EntitiesList`

Список отслеживаемых сущностей вместе с их свойствами.

| Поле | Тип | Описание |
| --- | --- | --- |
| entities | [Entity[]](#openapi-definition-Entity) | Список отслеживаемых сущностей. |
| nextPageKey | string | Курсор для следующей страницы результатов. На последней странице имеет значение `null`. Используйте его в query-параметре **nextPageKey** для получения следующих страниц результата. |
| pageSize | integer | Количество записей на страницу. |
| totalCount | integer | Общее количество записей в результате. |

#### Объект `Entity`

Свойства отслеживаемой сущности.

| Поле | Тип | Описание |
| --- | --- | --- |
| displayName | string | Имя сущности, отображаемое в UI. |
| entityId | string | ID сущности. |
| firstSeenTms | integer | Метка времени, когда сущность была впервые увидена, в UTC миллисекундах. |
| fromRelationships | object | Список связей, в которых сущность занимает позицию FROM. |
| icon | [EntityIcon](#openapi-definition-EntityIcon) | Иконка отслеживаемой сущности. |
| lastSeenTms | integer | Метка времени последнего наблюдения сущности, в UTC миллисекундах. |
| managementZones | [EnrichedManagementZoneDto[]](#openapi-definition-EnrichedManagementZoneDto) | Набор зон управления, к которым относится сущность. |
| properties | object | Список дополнительных свойств сущности. |
| tags | [EnrichedTagDto[]](#openapi-definition-EnrichedTagDto) | Набор тегов, присвоенных сущности. |
| toRelationships | object | Список связей, в которых сущность занимает позицию TO. |
| type | string | Тип сущности. |

#### Объект `EntityId`

Краткое представление отслеживаемой сущности.

| Поле | Тип | Описание |
| --- | --- | --- |
| id | string | ID сущности. |
| type | string | Тип сущности. |

#### Объект `EntityIcon`

Иконка отслеживаемой сущности.

| Поле | Тип | Описание |
| --- | --- | --- |
| customIconPath | string | Пользовательская иконка сущности. Укажите [barista](https://dt-url.net/u403suy) ID иконки или URL вашей собственной иконки. |
| primaryIconType | string | Основная иконка сущности. Указывается [barista](https://dt-url.net/u403suy) ID иконки. |
| secondaryIconType | string | Вторичная иконка сущности. Указывается [barista](https://dt-url.net/u403suy) ID иконки. |

#### Объект `EnrichedManagementZoneDto`

| Поле | Тип | Описание |
| --- | --- | --- |
| id | string | ID зоны управления. |
| name | string | Имя зоны управления. |
| sourceSetting | string | Путь к объекту настроек в Settings API. |

#### Объект `EnrichedTagDto`

| Поле | Тип | Описание |
| --- | --- | --- |
| context | string | Источник тега, например AWS или Cloud Foundry. Пользовательские теги используют значение `CONTEXTLESS`. |
| key | string | Ключ тега. |
| source | string | Источник, откуда пришёл тег. Возможные значения: * Auto tags * Environment tags * User provided tags |
| sourceSetting | string | Путь к объекту настроек в Settings API. Доступно только для тегов с источником Auto tags. |
| stringRepresentation | string | Строковое представление тега. |
| value | string | Значение тега. |

#### Объект `ErrorEnvelope`

| Поле | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Поле | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния. |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений. |
| message | string | Сообщение об ошибке. |

#### Объект `ConstraintViolation`

Список нарушений ограничений.

| Поле | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | Поле может принимать значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"entities": [



{



"displayName": "my host",



"entityId": "HOST-06F288EE2A930951",



"firstSeenTms": 1574697667547,



"fromRelationships": {



"isInstanceOf": [



{



"id": "HOST_GROUP-0E489369D663A4BF",



"type": "HOST_GROUP"



}



]



},



"icon": {



"customIconPath": "host",



"primaryIconType": "linux",



"secondaryIconType": "microsoft-azure-signet"



},



"lastSeenTms": 1588242361417,



"managementZones": [



{



"id": "6239538939987181652",



"name": "main app"



}



],



"properties": {



"bitness": 64,



"cpuCores": 8,



"monitoringMode": "FULL_STACK",



"networkZoneId": "aws.us.east01",



"osArchitecture": "X86",



"osType": "LINUX"



},



"tags": [



{



"context": "CONTEXTLESS",



"key": "architecture",



"stringRepresentation": "architecture:x86",



"value": "x86"



},



{



"context": "ENVIRONMENT",



"key": "Infrastructure",



"stringRepresentation": "[ENVIRONMENT]Infrastructure:Linux",



"value": "Linux"



}



],



"toRelationships": {



"isDiskOf": [



{



"id": "DISK-0393340DCA3853B0",



"type": "DISK"



}



]



},



"type": "HOST"



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

## Пример

В этом примере запрос выводит сервисы, относящиеся к зонам управления с ID **229130632296508575249**. Для этого query-параметр **entitySelector** имеет значение `type("SERVICE"),mzId("229130632296508575249")`.

Кроме стандартных Dynatrace entity ID и имён сущностей, запрос также возвращает метку времени последнего наблюдения сервиса и список технологических типов, работающих в сервисе. Для этого query-параметр **fields** имеет значение `lastSeenTms,properties.serviceTechnologyTypes`.

API-токен передаётся в заголовке **Authorization**.

Результат сокращён до трёх записей.

#### Curl

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/entities?entitySelector=type(%22SERVICE%22),mzId(%229130632296508575249%22)&fields=lastSeenTms,properties.serviceTechnologyTypes' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/entities?entitySelector=type(%22SERVICE%22),mzId(%229130632296508575249%22)&fields=lastSeenTms,properties.serviceTechnologyTypes
```

#### Тело ответа

```
{



"totalCount": 52,



"pageSize": 50,



"nextPageKey": "AQArdHlwZSgiU0VSVklDRSIpL",



"entities": [



{



"entityId": "SERVICE-1125C375A187D27A",



"displayName": "dotNetBackend_easyTravel_x64",



"lastSeenTms": 1590609632865,



"properties": {



"serviceTechnologyTypes": [



"IIS app pool",



"ASP.NET",



"DotNet"



]



}



},



{



"entityId": "SERVICE-42C0B06C4DCFD0EF",



"displayName": "AuthenticationService",



"lastSeenTms": 1590747000977,



"properties": {



"serviceTechnologyTypes": [



"Java"



]



}



},



{



"entityId": "SERVICE-620517BB99A7ED9E",



"displayName": "BookingService",



"lastSeenTms": 1590747028702,



"properties": {



"serviceTechnologyTypes": [



"Java"



]



}



}



]



}
```

#### Код ответа

200

## Связанные темы

* [API пользовательских тегов](/managed/dynatrace-api/environment-api/custom-tags "Управляйте пользовательскими тегами отслеживаемых сущностей через Dynatrace API.")