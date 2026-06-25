---
title: Problems API v2 - GET детали проблемы
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/problems-v2/problems/get-problem-details
scraped: 2026-05-12T11:57:21.415895
---

# Problems API v2 - GET детали проблемы

# Problems API v2 - GET детали проблемы

* Справочник
* Опубликовано 12 октября 2020 г.

Возвращает все детали указанной проблемы.

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/problems/{problemId}` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/problems/{problemId}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `problems.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| problemId | string | ID требуемой проблемы. | path | Обязательный |
| fields | string | Список дополнительных свойств проблемы, которые можно добавить в ответ. Доступны следующие свойства (все остальные включаются всегда, и убрать их из ответа нельзя): * `evidenceDetails`: детали первопричины. * `impactAnalysis`: анализ воздействия проблемы на другие сущности/пользователей. * `recentComments`: список самых свежих комментариев к проблеме. Чтобы добавить свойства, укажите их списком через запятую (например, `evidenceDetails,impactAnalysis`). | query | Необязательный |

## Ответ

Некоторые JSON-модели различаются в зависимости от **type** модели. Все возможные вариации смотрите в [JSON-моделях](/managed/dynatrace-api/environment-api/problems-v2/models "Изучите вариации моделей в Problems API v2.").

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [Problem](#openapi-definition-Problem) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

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