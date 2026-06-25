---
title: Vulnerabilities API - GET remediation item entities
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/application-security/vulnerabilities/get-remediation-item-entities
scraped: 2026-05-12T11:58:47.953075
---

# Vulnerabilities API - GET remediation item entities

# Vulnerabilities API - GET remediation item entities

* Reference
* Updated on Sep 25, 2024

Возвращает список процессов [remediation tracking](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Отслеживайте прогресс устранения уязвимостей.") third-party уязвимости.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems/{remediationItemId}/remediationProgressEntities` |
| GET | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems/{remediationItemId}/remediationProgressEntities` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `securityProblems.read`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID требуемой third-party security problem. | path | Обязательный |
| remediationItemId | string | ID remediation item. | path | Обязательный |
| remediationProgressEntitySelector | string | Определяет область запроса. В ответ включаются только remediation progress entities, соответствующие указанным критериям.  Можно добавить один или несколько критериев. Значения *не* регистрозависимы, и используется оператор `EQUALS`, если не указано иное.  * State: `state("value")`. Возможные значения поля **state** это `AFFECTED` и `UNAFFECTED`. Если не задано, возвращаются все сущности. * Vulnerable function usage assessment: `assessment.vulnerableFunctionUsage("value")` Возможные значения `IN_USE` и `NOT_IN_USE`. * Vulnerable function restart required: `assessment.vulnerableFunctionRestartRequired("value")` Возможные значения `TRUE` или `FALSE`. * Vulnerable function in use contains: `assessment.vulnerableFunctionInUseContains("value")`. Возможные значения `class::function`, `class::` и `function`. Используется оператор `CONTAINS`. Учитываются только уязвимые функции в использовании. * Entity name contains: `entityNameContains("value-1")`. Используется оператор `CONTAINS`.  Чтобы задать несколько критериев, разделите их запятой (`,`). В ответ включаются только результаты, соответствующие **всем** критериям.  Указывайте значение критерия как строку в кавычках. Следующие специальные символы должны быть экранированы тильдой (`~`) внутри кавычек:  * Тильда `~` * Кавычка `"` | query | Опциональный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [RemediationProgressEntityList](#openapi-definition-RemediationProgressEntityList) | Успех. Ответ содержит список remediation progress entities для remediation item security problem. Количество возвращаемых сущностей ограничено. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

#### Объект `RemediationProgressEntityList`

Список remediation progress entities.

| Элемент | Тип | Описание |
| --- | --- | --- |
| remediationProgressEntities | [RemediationProgressEntity[]](#openapi-definition-RemediationProgressEntity) | Список remediation progress entities. |

#### Объект `RemediationProgressEntity`

Затронутая или незатронутая сущность remediation для security problem.

| Элемент | Тип | Описание |
| --- | --- | --- |
| assessment | [RemediationProgressEntityAssessment](#openapi-definition-RemediationProgressEntityAssessment) | Оценка remediation progress entity. |
| firstAffectedTimestamp | integer | Временная метка, когда remediation progress entity впервые была связана с уязвимостью. |
| id | string | ID remediation progress entity. |
| name | string | Имя remediation progress entity. |
| state | string | Текущее состояние remediation progress entity. Элемент может принимать значения * `AFFECTED` * `UNAFFECTED` |
| vulnerableComponents | [RemediationProgressVulnerableComponent[]](#openapi-definition-RemediationProgressVulnerableComponent) | Список уязвимых компонентов remediation item.  Уязвимый компонент это то, что вызывает security problem. |

#### Объект `RemediationProgressEntityAssessment`

Оценка remediation progress entity.

| Элемент | Тип | Описание |
| --- | --- | --- |
| vulnerableFunctionRestartRequired | boolean | Требуется ли перезапуск для последних данных об уязвимой функции. |
| vulnerableFunctionUsage | string | Использование уязвимых функций. Элемент может принимать значения * `IN_USE` * `NOT_AVAILABLE` * `NOT_IN_USE` |
| vulnerableFunctionsInUse | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | Список уязвимых функций в использовании. |
| vulnerableFunctionsNotAvailable | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | Список уязвимых функций, которые недоступны. |
| vulnerableFunctionsNotInUse | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | Список уязвимых функций, которые не используются. |

#### Объект `VulnerableFunction`

Определяет уязвимую функцию.

| Элемент | Тип | Описание |
| --- | --- | --- |
| className | string | Имя класса уязвимой функции. |
| filePath | string | Путь к файлу уязвимой функции. |
| functionName | string | Имя функции уязвимой функции. |

#### Объект `RemediationProgressVulnerableComponent`

Уязвимый компонент с деталями для remediation progress entity (PGI).

| Элемент | Тип | Описание |
| --- | --- | --- |
| displayName | string | Display name уязвимого компонента. |
| fileName | string | Имя файла уязвимого компонента. |
| id | string | Dynatrace entity ID уязвимого компонента. |
| loadOrigins | string[] | Источники загрузки уязвимых компонентов. |
| shortName | string | Короткое имя только компонента уязвимого компонента. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния. |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений. |
| message | string | Сообщение об ошибке. |

#### Объект `ConstraintViolation`

Список нарушений ограничений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"remediationProgressEntities": [



{



"assessment": {



"vulnerableFunctionRestartRequired": true,



"vulnerableFunctionUsage": "IN_USE",



"vulnerableFunctionsInUse": [



{



"className": "string",



"filePath": "string",



"functionName": "string"



}



],



"vulnerableFunctionsNotAvailable": [



{}



],



"vulnerableFunctionsNotInUse": [



{}



]



},



"firstAffectedTimestamp": 1,



"id": "string",



"name": "string",



"state": "AFFECTED",



"vulnerableComponents": [



{



"displayName": "string",



"fileName": "string",



"id": "string",



"loadOrigins": [



"string"



],



"shortName": "string"



}



]



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

Изучить процессы remediation item, которые в данный момент затронуты.

Обязательный фильтр: `remediationProgressEntitySelector=state("AFFECTED")`.

#### Curl

```
curl -X 'GET' 'https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/7412525767433554374/remediationItems/PROCESS_GROUP-F32C09AEDCB7A450/remediationProgressEntities?remediationProgressEntitySelector=state%28%22AFFECTED%22%29' \



-H 'accept: application/json; charset=utf-8' \



-H 'Authorization: Api-Token [your_token]'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/7412525767433554374/remediationItems/PROCESS_GROUP-F32C09AEDCB7A450/remediationProgressEntities?remediationProgressEntitySelector=state%28%22AFFECTED%22%29
```

#### Response body

```
{



"remediationProgressEntities": [



{



"id": "PROCESS_GROUP_INSTANCE-66B8C7F0FA77E541",



"name": "app.js (frontend) unguard-frontend-* (unguard-frontend-696558fd77-cdkxp)",



"firstAffectedTimestamp": 1725894871213,



"state": "AFFECTED",



"vulnerableComponents": [



{



"id": "SOFTWARE_COMPONENT-30CF12729DF87E61",



"displayName": "minimatch:3.0.4",



"shortName": "minimatch"



}



],



"assessment": {



"vulnerableFunctionUsage": "NOT_AVAILABLE",



"vulnerableFunctionRestartRequired": false,



"vulnerableFunctionsInUse": [],



"vulnerableFunctionsNotInUse": [],



"vulnerableFunctionsNotAvailable": []



}



}



]



}
```

## Связанные темы

* [Application Security](/managed/secure/application-security "Доступ к функциям Dynatrace Application Security.")
* [Davis Security Advisor API](/managed/dynatrace-api/environment-api/application-security/davis-security-advice "Просмотрите рекомендации Davis Security Advisor через Dynatrace API.")
* [Remediation tracking](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Отслеживайте прогресс устранения уязвимостей.")