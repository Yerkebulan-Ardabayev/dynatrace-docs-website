---
title: Problems API v2 - GET список проблем
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/problems-v2/problems/get-problems-list
scraped: 2026-05-12T11:57:19.194499
---

# Problems API v2 - GET список проблем

# Problems API v2 - GET список проблем

* Справочник
* Опубликовано 12 октября 2020 г.

Возвращает список проблем (и их детали), обнаруженных Dynatrace за относительный период времени.

Проблема включается в ответ, если её метка времени начала или окончания попадает в заданный временной интервал.

Сузить вывод можно через критерии фильтрации, смотрите [раздел **Параметры**](#parameters).

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/problems` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/problems` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `problems.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| fields | string | Список дополнительных свойств проблемы, которые можно добавить в ответ. Доступны следующие свойства (все остальные включаются всегда, и убрать их из ответа нельзя): * `evidenceDetails`: детали первопричины. * `impactAnalysis`: анализ воздействия проблемы на другие сущности/пользователей. * `recentComments`: список самых свежих комментариев к проблеме. Чтобы добавить свойства, укажите их списком через запятую (например, `evidenceDetails,impactAnalysis`). Поле действует только для текущей страницы результатов. Его нужно задавать для каждой запрашиваемой страницы. | query | Необязательный |
| nextPageKey | string | Курсор для следующей страницы результатов. Находится в поле **nextPageKey** предыдущего ответа. Первая страница возвращается всегда, если query-параметр **nextPageKey** не указан. Когда **nextPageKey** задан для получения следующих страниц, все остальные query-параметры нужно опустить, кроме необязательного параметра **fields**. | query | Необязательный |
| pageSize | integer | Количество проблем в одном payload ответа. Максимально допустимый размер страницы: 500. Если не задан, используется 50. | query | Необязательный |
| from | string | Начало запрашиваемого временного интервала. Можно использовать один из форматов: * Метка времени в UTC миллисекундах. * Читаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Можно использовать пробел вместо `T`. Секунды и доли секунды необязательны. * Относительный интервал назад от текущего момента. Формат `now-NU/A`, где `N`, количество, `U`, единица времени, `A`, выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w`, это год назад, выровненный по неделе. Можно указать относительный интервал и без выравнивания: `now-NU`. Поддерживаемые единицы времени для относительного интервала: + `m`: минуты + `h`: часы + `d`: дни + `w`: недели + `M`: месяцы + `y`: годы Если не задан, используется относительный интервал в два часа (`now-2h`). | query | Необязательный |
| to | string | Конец запрашиваемого временного интервала. Можно использовать один из форматов: * Метка времени в UTC миллисекундах. * Читаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Можно использовать пробел вместо `T`. Секунды и доли секунды необязательны. * Относительный интервал назад от текущего момента. Формат `now-NU/A`, где `N`, количество, `U`, единица времени, `A`, выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w`, это год назад, выровненный по неделе. Можно указать относительный интервал и без выравнивания: `now-NU`. Поддерживаемые единицы времени для относительного интервала: + `m`: минуты + `h`: часы + `d`: дни + `w`: недели + `M`: месяцы + `y`: годы Если не задан, используется текущая метка времени. | query | Необязательный |
| problemSelector | string | Определяет область запроса. В ответ попадают только проблемы, удовлетворяющие критериям. Можно добавить один или несколько перечисленных ниже критериев. Для каждого критерия можно указать несколько значений через запятую, если не оговорено иное. Если указано несколько значений, применяется логика **OR**. Все значения должны быть в кавычках. * Статус: `status("open")` или `status("closed")`. Можно указать только один статус. * Уровень серьёзности: `severityLevel("level-1","level-2")`. Возможные значения смотрите в описании поля **severityLevel** в ответе. * Уровень воздействия: `impactLevel("level-11","level-2")`. Возможные значения смотрите в описании поля **impactLevel** в ответе. * Сущность-первопричина: `rootCauseEntity("id-1", "id-2")`. * ID зоны управления: `managementZoneIds("mZId-1", "mzId-2")`. * Имя зоны управления: `managementZones("value-1","value-2")`. * Затронутые (impacted) сущности: `impactedEntities("id-1", "id-2")`. * Затронутые (affected) сущности: `affectedEntities("id-1", "id-2")`. * Тип затронутых сущностей: `affectedEntityTypes("value-1","value-2")`. * ID проблемы: `problemId("id-1", "id-2")`. * ID профиля оповещений: `problemFilterIds("id-1", "id-2")`. * Имя профиля оповещений (содержит, без учёта регистра): `problemFilterNames("value-1","value-2")`. * Имя профиля оповещений (точное совпадение, без учёта регистра): `problemFilterNames.equals("value-1","value-2")`. * Теги сущностей: `entityTags("[context]key:value","key:value")`. Теги в форматах `[context]key:value`, `key:value` и `value` распознаются и разбираются автоматически. Если тег-значение содержит двоеточие (`:`), его необходимо экранировать обратной косой (`\`). Иначе тег будет разобран как `key:value`. Все значения тегов регистрозависимы. * Отображаемый ID проблемы: `displayId("id-1", "id-2")`. * На обслуживании: `underMaintenance(true|false)`. Показывает (`true`) или скрывает (`false`) все проблемы, созданные в режиме обслуживания. * Текстовый поиск: `text("value")`. Текстовый поиск по полям: заголовок проблемы, заголовки событий, displayId и id затронутых (affected и impacted) сущностей. Поиск без учёта регистра, частичное совпадение, на основе оценки релевантности. Поэтому для получения наиболее релевантных проблем в начале списка стоит использовать опцию сортировки `relevance`. Спецсимволы `~` и `"` нужно экранировать через `~` (например, поиск двойной кавычки `text("~"")`). Значение поиска ограничено 30 символами. Чтобы указать несколько критериев, перечислите их через запятую (`,`). В ответ попадут только результаты, соответствующие **всем** критериям. | query | Необязательный |
| entitySelector | string | Область запроса по сущностям. Необходимо указать один из критериев: * Тип сущности: `type("TYPE")` * Dynatrace entity ID: `entityId("id")`. Можно указать несколько ID через запятую (`entityId("id-1","id-2")`). Все запрашиваемые сущности должны быть одного типа. Дополнительно можно добавить один или несколько следующих критериев. Значения регистрозависимы, оператор по умолчанию `EQUALS`. * Тег: `tag("value")`. Теги в форматах `[context]key:value`, `key:value` и `value` распознаются и разбираются автоматически. Двоеточия (`:`), входящие в состав ключа или значения, должны быть экранированы обратной косой (`\`). Иначе они будут восприняты как разделитель между ключом и значением. Все значения тегов регистрозависимы. * ID зоны управления: `mzId(123)` * Имя зоны управления: `mzName("value")` * Имя сущности: + `entityName.equals`: выполняет регистронезависимый запрос `EQUALS`. + `entityName.startsWith`: меняет оператор на `BEGINS WITH`. + `entityName.in`: позволяет указать несколько значений. Применяется оператор `EQUALS`. + `caseSensitive(entityName.equals("value"))`: принимает любой критерий по имени сущности и делает сравнение регистрозависимым. * Состояние работоспособности (HEALTHY, UNHEALTHY): `healthState("HEALTHY")` * Метка времени первого обнаружения: `firstSeenTms.<operator>(now-3h)`. Используется любой формат timestamp из параметров **from**/**to**. Доступные операторы: + `lte`: раньше указанного времени или в это же время + `lt`: раньше указанного времени + `gte`: позже указанного времени или в это же время + `gt`: позже указанного времени * Атрибут сущности: `<attribute>("value1","value2")` и `<attribute>.exists()`. Список доступных атрибутов можно получить запросом [GET entity type](https://dt-url.net/2ka3ivt), посмотрев поле **properties** в ответе. * Связи: `fromRelationships.<relationshipName>()` и `toRelationships.<relationshipName>()`. Критерий принимает в качестве аргумента селектор сущностей. Список доступных связей можно получить запросом [GET entity type](https://dt-url.net/2ka3ivt), посмотрев поля **fromRelationships** и **toRelationships**. * Инверсия: `not(<criterion>)`. Инвертирует любой критерий, кроме **type**. Подробнее смотрите [Entity selector](https://dt-url.net/apientityselector) в документации Dynatrace. Чтобы указать несколько критериев, перечислите их через запятую (`,`). Например, `type("HOST"),healthState("HEALTHY")`. В ответ попадут только результаты, соответствующие **всем** критериям. Максимальная длина строки: 2 000 символов. Максимальное количество выбираемых сущностей: 10000. | query | Необязательный |
| sort | string | Задаёт набор полей (через запятую `,`) для сортировки в списке проблем. Сортировать можно по следующим свойствам, со знаковым префиксом для направления сортировки. * `status`: статус проблемы (`+` сначала открытые или `-` сначала закрытые) * `startTime`: время начала проблемы (`+` сначала старые или `-` сначала новые) * `relevance`: релевантность проблемы (`+` сначала наименее релевантные или `-` сначала наиболее релевантные), используется только в сочетании с текстовым поиском Если префикс не указан, используется `+`. Можно задать несколько уровней сортировки. Например, `+status,-startTime` сортирует проблемы по статусу, открытые первыми. Внутри статуса проблемы сортируются по времени начала, сначала старые. | query | Необязательный |

## Ответ

Некоторые JSON-модели различаются в зависимости от **type** модели. Все возможные вариации смотрите в [JSON-моделях](/managed/dynatrace-api/environment-api/problems-v2/models "Изучите вариации моделей в Problems API v2.").

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [Problems](#openapi-definition-Problems) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `Problems`

Список проблем.

| Поле | Тип | Описание |
| --- | --- | --- |
| nextPageKey | string | Курсор для следующей страницы результатов. На последней странице имеет значение `null`. Используйте его в query-параметре **nextPageKey** для получения следующих страниц результата. |
| pageSize | integer | Количество записей на страницу. |
| problems | [Problem[]](#openapi-definition-Problem) | Записи результата. |
| totalCount | integer | Общее количество записей в результате. |
| warnings | string[] | Список предупреждений. |

#### Объект `Problem`

Свойства проблемы.

| Поле | Тип | Описание |
| --- | --- | --- |
| affectedEntities | [EntityStub[]](#openapi-definition-EntityStub) | Список всех сущностей, затронутых проблемой. |
| displayId | string | Отображаемый ID проблемы. |
| endTime | integer | Метка времени окончания проблемы, в UTC миллисекундах. Имеет значение `-1`, если проблема ещё открыта. |
| entityTags | [METag[]](#openapi-definition-METag) | Список всех тегов сущностей проблемы. |
| evidenceDetails | [EvidenceDetails](#openapi-definition-EvidenceDetails) | Детали доказательств проблемы. |
| impactAnalysis | [ImpactAnalysis](#openapi-definition-ImpactAnalysis) | Список всех воздействий проблемы. |
| impactLevel | string | Уровень воздействия проблемы. Показывает, что затронуто проблемой. Поле может принимать значения: * `APPLICATION` * `ENVIRONMENT` * `INFRASTRUCTURE` * `SERVICES` |
| impactedEntities | [EntityStub[]](#openapi-definition-EntityStub) | Список всех сущностей, на которые повлияла проблема. |
| k8s.cluster.name | string[] | Имена связанных Kubernetes-кластеров. |
| k8s.cluster.uid | string[] | UID связанных Kubernetes-кластеров. |
| k8s.namespace.name | string[] | Имена связанных Kubernetes-namespace. |
| linkedProblemInfo | [LinkedProblem](#openapi-definition-LinkedProblem) | Свойства связанной проблемы. |
| managementZones | [ManagementZone[]](#openapi-definition-ManagementZone) | Список всех зон управления, к которым относится проблема. |
| problemFilters | [AlertingProfileStub[]](#openapi-definition-AlertingProfileStub) | Список профилей оповещений, подходящих под проблему. |
| problemId | string | ID проблемы. |
| recentComments | [CommentsList](#openapi-definition-CommentsList) | Список комментариев. |
| rootCauseEntity | [EntityStub](#openapi-definition-EntityStub) | Краткое представление отслеживаемой сущности. |
| severityLevel | string | Серьёзность проблемы. Поле может принимать значения: * `AVAILABILITY` * `CUSTOM_ALERT` * `ERROR` * `INFO` * `MONITORING_UNAVAILABLE` * `PERFORMANCE` * `RESOURCE_CONTENTION` |
| startTime | integer | Метка времени начала проблемы, в UTC миллисекундах. |
| status | string | Статус проблемы. Поле может принимать значения: * `CLOSED` * `OPEN` |
| title | string | Имя проблемы, отображаемое в UI. |

#### Объект `EntityStub`

Краткое представление отслеживаемой сущности.

| Поле | Тип | Описание |
| --- | --- | --- |
| entityId | [EntityId](#openapi-definition-EntityId) | Краткое представление отслеживаемой сущности. |
| name | string | Имя сущности. Не включается в ответ, если сущность с соответствующим ID не найдена. |

#### Объект `EntityId`

Краткое представление отслеживаемой сущности.

| Поле | Тип | Описание |
| --- | --- | --- |
| id | string | ID сущности. |
| type | string | Тип сущности. |

#### Объект `METag`

Тег отслеживаемой сущности.

| Поле | Тип | Описание |
| --- | --- | --- |
| context | string | Источник тега, например AWS или Cloud Foundry. Пользовательские теги используют значение `CONTEXTLESS`. |
| key | string | Ключ тега. |
| stringRepresentation | string | Строковое представление тега. |
| value | string | Значение тега. |

#### Объект `EvidenceDetails`

Детали доказательств проблемы.

| Поле | Тип | Описание |
| --- | --- | --- |
| details | [Evidence[]](#openapi-definition-Evidence) | Список всех доказательств. |
| totalCount | integer | Общее число доказательств проблемы. |

#### Объект `Evidence`

Доказательство первопричины.

Фактический набор полей зависит от типа доказательства. Список фактических объектов смотрите в описании поля **evidenceType** или в [Problems API v2 - JSON-модели](https://dt-url.net/we03sp2).

| Поле | Тип | Описание |
| --- | --- | --- |
| displayName | string | Отображаемое имя доказательства. |
| entity | [EntityStub](#openapi-definition-EntityStub) | Краткое представление отслеживаемой сущности. |
| evidenceType | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из объектов: * `EVENT` -> EventEvidence * `METRIC` -> MetricEvidence * `TRANSACTIONAL` -> TransactionalEvidence * `MAINTENANCE_WINDOW` -> MaintenanceWindowEvidence * `AVAILABILITY_EVIDENCE` -> AvailabilityEvidence Поле может принимать значения: * `AVAILABILITY_EVIDENCE` * `EVENT` * `MAINTENANCE_WINDOW` * `METRIC` * `TRANSACTIONAL` |
| groupingEntity | [EntityStub](#openapi-definition-EntityStub) | Краткое представление отслеживаемой сущности. |
| rootCauseRelevant | boolean | Доказательство является (`true`) или не является (`false`) частью первопричины. |
| startTime | integer | Время начала доказательства, в UTC миллисекундах. |

#### Объект `ImpactAnalysis`

Список всех воздействий проблемы.

| Поле | Тип | Описание |
| --- | --- | --- |
| impacts | [Impact[]](#openapi-definition-Impact) | Список всех воздействий проблемы. |

#### Объект `Impact`

Анализ воздействия проблемы на другие сущности/пользователей.

Фактический набор полей зависит от типа воздействия. Список фактических объектов смотрите в описании поля **impactType** или в [Problems API v2 - JSON-модели](https://dt-url.net/we03sp2).

| Поле | Тип | Описание |
| --- | --- | --- |
| estimatedAffectedUsers | integer | Оценочное число затронутых пользователей. |
| impactType | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из объектов: * `SERVICE` -> ServiceImpact * `APPLICATION` -> ApplicationImpact * `MOBILE` -> MobileImpact * `CUSTOM_APPLICATION` -> CustomApplicationImpact Поле может принимать значения: * `APPLICATION` * `CUSTOM_APPLICATION` * `MOBILE` * `SERVICE` |
| impactedEntity | [EntityStub](#openapi-definition-EntityStub) | Краткое представление отслеживаемой сущности. |

#### Объект `LinkedProblem`

Свойства связанной проблемы.

| Поле | Тип | Описание |
| --- | --- | --- |
| displayId | string | Отображаемый ID проблемы. |
| problemId | string | ID проблемы. |

#### Объект `ManagementZone`

Краткое представление зоны управления.

| Поле | Тип | Описание |
| --- | --- | --- |
| id | string | ID зоны управления. |
| name | string | Имя зоны управления. |

#### Объект `AlertingProfileStub`

Краткое представление профиля оповещений.

| Поле | Тип | Описание |
| --- | --- | --- |
| id | string | ID профиля оповещений. |
| name | string | Имя профиля оповещений. |

#### Объект `CommentsList`

Список комментариев.

| Поле | Тип | Описание |
| --- | --- | --- |
| comments | [Comment[]](#openapi-definition-Comment) | Записи результата. |
| nextPageKey | string | Курсор для следующей страницы результатов. На последней странице имеет значение `null`. Используйте его в query-параметре **nextPageKey** для получения следующих страниц результата. |
| pageSize | integer | Количество записей на страницу. |
| totalCount | integer | Общее количество записей в результате. |

#### Объект `Comment`

Комментарий к проблеме.

| Поле | Тип | Описание |
| --- | --- | --- |
| authorName | string | Пользователь, написавший комментарий. |
| content | string | Текст комментария. |
| context | string | Контекст комментария. |
| createdAtTimestamp | integer | Метка времени создания комментария, в UTC миллисекундах. |
| id | string | ID комментария. |

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



"nextPageKey": "AQAAABQBAAAABQ==",



"pageSize": 1,



"problems": [



{



"affectedEntities": [



{



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



}



],



"displayId": "string",



"endTime": 1,



"entityTags": [



{



"context": "string",



"key": "string",



"stringRepresentation": "string",



"value": "string"



}



],



"evidenceDetails": {



"details": [



{



"displayName": "string",



"entity": {},



"evidenceType": "AVAILABILITY_EVIDENCE",



"groupingEntity": {},



"rootCauseRelevant": true,



"startTime": 1



}



],



"totalCount": 1



},



"impactAnalysis": {



"impacts": [



{



"estimatedAffectedUsers": 1,



"impactType": "APPLICATION",



"impactedEntity": {}



}



]



},



"impactLevel": "APPLICATION",



"impactedEntities": [



{}



],



"k8s.cluster.name": [



"string"



],



"k8s.cluster.uid": [



"string"



],



"k8s.namespace.name": [



"string"



],



"linkedProblemInfo": {



"displayId": "string",



"problemId": "string"



},



"managementZones": [



{



"id": "string",



"name": "string"



}



],



"problemFilters": [



{



"id": "string",



"name": "string"



}



],



"problemId": "string",



"recentComments": {



"comments": [



{



"authorName": "string",



"content": "string",



"context": "string",



"createdAtTimestamp": 1,



"id": "string"



}



],



"nextPageKey": "AQAAABQBAAAABQ==",



"pageSize": 1,



"totalCount": 1



},



"rootCauseEntity": {},



"severityLevel": "AVAILABILITY",



"startTime": 1,



"status": "CLOSED",



"title": "string"



}



],



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

## Связанные темы

* [Davis® AI](/managed/dynatrace-intelligence "Познакомьтесь с возможностями Davis AI.")