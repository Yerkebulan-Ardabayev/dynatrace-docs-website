---
title: Vulnerabilities API - GET remediation item details
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/application-security/vulnerabilities/get-remediation-item-details
scraped: 2026-05-12T11:59:03.102148
---

# Vulnerabilities API - GET remediation item details

# Vulnerabilities API - GET remediation item details

* Reference
* Updated on Sep 25, 2024

Возвращает детали process group [remediation tracking](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Отслеживайте прогресс устранения уязвимостей.") third-party уязвимости (или, в случае Kubernetes-уязвимостей, параметры remediation tracking Kubernetes-узла).

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems/{remediationItemId}` |
| GET | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems/{remediationItemId}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `securityProblems.read`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID требуемой third-party security problem. | path | Обязательный |
| remediationItemId | string | ID remediation item. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [RemediationDetailsItem](#openapi-definition-RemediationDetailsItem) | Успех. Ответ содержит детали одного remediation item security problem. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

#### Объект `RemediationDetailsItem`

Детальная информация о remediation item для security problem.

| Элемент | Тип | Описание |
| --- | --- | --- |
| assessment | [RemediationAssessment](#openapi-definition-RemediationAssessment) | Оценка remediation item. |
| entityIds | string[] | - |
| firstAffectedTimestamp | integer | - |
| id | string | - |
| muteState | [RemediationItemMuteState](#openapi-definition-RemediationItemMuteState) | Состояние заглушения remediation item security problem. |
| name | string | - |
| remediationProgress | [RemediationProgress](#openapi-definition-RemediationProgress) | Прогресс этого remediation item. Содержит затронутые и незатронутые сущности. |
| resolvedTimestamp | integer | - |
| trackingLink | [TrackingLink](#openapi-definition-TrackingLink) | URL внешней ссылки трекинга, связанной с устранимой сущностью security problem. |
| vulnerabilityState | string | -Элемент может принимать значения * `RESOLVED` * `VULNERABLE` |
| vulnerableComponents | [RemediationItemDetailsVulnerableComponent[]](#openapi-definition-RemediationItemDetailsVulnerableComponent) | Список уязвимых компонентов remediation item.  Уязвимый компонент это то, что вызывает security problem. |

#### Объект `RemediationAssessment`

Оценка remediation item.

| Элемент | Тип | Описание |
| --- | --- | --- |
| assessmentAccuracy | string | Точность оценки. Элемент может принимать значения * `FULL` * `NOT_AVAILABLE` * `REDUCED` |
| assessmentAccuracyDetails | [AssessmentAccuracyDetails](#openapi-definition-AssessmentAccuracyDetails) | Детали точности оценки. |
| dataAssets | string | Доступность связанных data assets для затронутых сущностей. Элемент может принимать значения * `NOT_AVAILABLE` * `NOT_DETECTED` * `REACHABLE` |
| exposure | string | Уровень exposure затронутых сущностей. Элемент может принимать значения * `NOT_AVAILABLE` * `NOT_DETECTED` * `PUBLIC_NETWORK` |
| numberOfDataAssets | integer | Количество связанных data assets. |
| vulnerableFunctionRestartRequired | boolean | Требуется ли перезапуск для последних данных об уязвимой функции. |
| vulnerableFunctionUsage | string | Использование уязвимых функций. Элемент может принимать значения * `IN_USE` * `NOT_AVAILABLE` * `NOT_IN_USE` |
| vulnerableFunctionsInUse | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | Список уязвимых функций в использовании. |
| vulnerableFunctionsNotAvailable | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | Список уязвимых функций, которые недоступны. |
| vulnerableFunctionsNotInUse | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | Список уязвимых функций, которые не используются. |

#### Объект `AssessmentAccuracyDetails`

Детали точности оценки.

| Элемент | Тип | Описание |
| --- | --- | --- |
| reducedReasons | string[] | Причина пониженной точности оценки. Элемент может принимать значения * `LIMITED_AGENT_SUPPORT` * `LIMITED_BY_CONFIGURATION` |

#### Объект `VulnerableFunction`

Определяет уязвимую функцию.

| Элемент | Тип | Описание |
| --- | --- | --- |
| className | string | Имя класса уязвимой функции. |
| filePath | string | Путь к файлу уязвимой функции. |
| functionName | string | Имя функции уязвимой функции. |

#### Объект `RemediationItemMuteState`

Состояние заглушения remediation item security problem.

| Элемент | Тип | Описание |
| --- | --- | --- |
| comment | string | Короткий комментарий о последнем изменении состояния заглушения. |
| lastUpdatedTimestamp | integer | Временная метка (миллисекунды UTC) последнего обновления состояния заглушения. |
| muted | boolean | Remediation заглушен (`true`) или не заглушен (`false`). |
| reason | string | Причина последнего изменения состояния заглушения. Элемент может принимать значения * `AFFECTED` * `CONFIGURATION_NOT_AFFECTED` * `FALSE_POSITIVE` * `IGNORE` * `INITIAL_STATE` * `OTHER` * `VULNERABLE_CODE_NOT_IN_USE` |
| user | string | Пользователь, который последним изменил состояние заглушения. |

#### Объект `RemediationProgress`

Прогресс этого remediation item. Содержит затронутые и незатронутые сущности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| affectedEntities | string[] | Список связанных сущностей, затронутых security problem. |
| unaffectedEntities | string[] | Список связанных сущностей, затронутых security problem. |

#### Объект `TrackingLink`

URL внешней ссылки трекинга, связанной с устранимой сущностью security problem.

| Элемент | Тип | Описание |
| --- | --- | --- |
| displayName | string | Display name (title), установленный для ссылки трекинга, например, 'ISSUE-123'. |
| lastUpdatedTimestamp | integer | Временная метка (миллисекунды UTC) последнего обновления ссылки трекинга. |
| url | string | URL, установленный для ссылки трекинга, например, https://example.com/ISSUE-123 |
| user | string | Пользователь, который последним изменил ссылку трекинга. |

#### Объект `RemediationItemDetailsVulnerableComponent`

Уязвимый компонент с деталями для remediation item (PG).

| Элемент | Тип | Описание |
| --- | --- | --- |
| affectedEntities | string[] | Список затронутых сущностей. |
| displayName | string | Display name уязвимого компонента. |
| fileName | string | Имя файла уязвимого компонента. |
| id | string | Dynatrace entity ID уязвимого компонента. |
| loadOrigins | string[] | Источники загрузки уязвимых компонентов. |
| numberOfAffectedEntities | integer | Количество затронутых сущностей. |
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



"assessment": {



"assessmentAccuracy": "FULL",



"assessmentAccuracyDetails": {



"reducedReasons": [



"LIMITED_AGENT_SUPPORT"



]



},



"dataAssets": "NOT_AVAILABLE",



"exposure": "NOT_AVAILABLE",



"numberOfDataAssets": 1,



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



"entityIds": [



"string"



],



"firstAffectedTimestamp": 1,



"id": "string",



"muteState": {



"comment": "string",



"lastUpdatedTimestamp": 1,



"muted": true,



"reason": "AFFECTED",



"user": "string"



},



"name": "string",



"remediationProgress": {



"affectedEntities": [



"string"



],



"unaffectedEntities": [



"string"



]



},



"resolvedTimestamp": 1,



"trackingLink": {



"displayName": "string",



"lastUpdatedTimestamp": 1,



"url": "string",



"user": "string"



},



"vulnerabilityState": "RESOLVED",



"vulnerableComponents": [



{



"affectedEntities": [



"string"



],



"displayName": "string",



"fileName": "string",



"id": "string",



"loadOrigins": [



"string"



],



"numberOfAffectedEntities": 1,



"shortName": "string"



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

Запросить устранимую сущность.

Обязательные фильтры:

* `securityProblemid`
* `remediationItemId`

#### Curl

```
curl -X 'GET' 'https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/7412525767433554374/remediationItems/PROCESS_GROUP-F32C09AEDCB7A450' \



-H 'accept: application/json; charset=utf-8' \



-H 'Authorization: Api-Token [your_token]'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/7412525767433554374/remediationItems/PROCESS_GROUP-F32C09AEDCB7A4
```

#### Response body

```
{



"id": "PROCESS_GROUP-F32C09AEDCB7A450",



"entityIds": [



"PROCESS_GROUP-F32C09AEDCB7A450"



],



"name": "app.js (frontend) unguard-frontend-*",



"firstAffectedTimestamp": 1725894871213,



"assessment": {



"exposure": "PUBLIC_NETWORK",



"dataAssets": "NOT_DETECTED",



"numberOfDataAssets": 0,



"vulnerableFunctionRestartRequired": false,



"vulnerableFunctionUsage": "NOT_AVAILABLE",



"vulnerableFunctionsInUse": [],



"vulnerableFunctionsNotInUse": [],



"vulnerableFunctionsNotAvailable": [],



"assessmentAccuracy": "FULL",



"assessmentAccuracyDetails": {



"reducedReasons": []



}



},



"vulnerabilityState": "VULNERABLE",



"muteState": {



"muted": false,



"user": "unknown",



"reason": "INITIAL_STATE"



},



"vulnerableComponents": [



{



"id": "SOFTWARE_COMPONENT-30CF12729DF87E61",



"displayName": "minimatch:3.0.4",



"shortName": "minimatch",



"numberOfAffectedEntities": 1,



"affectedEntities": [



"PROCESS_GROUP_INSTANCE-66B8C7F0FA77E541"



]



}



],



"remediationProgress": {



"affectedEntities": [



"PROCESS_GROUP_INSTANCE-66B8C7F0FA77E541"



],



"unaffectedEntities": []



}



}
```

## Связанные темы

* [Application Security](/managed/secure/application-security "Доступ к функциям Dynatrace Application Security.")
* [Davis Security Advisor API](/managed/dynatrace-api/environment-api/application-security/davis-security-advice "Просмотрите рекомендации Davis Security Advisor через Dynatrace API.")
* [Remediation tracking](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Отслеживайте прогресс устранения уязвимостей.")