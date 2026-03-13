---
title: Vulnerabilities API - GET remediation item details
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/application-security/vulnerabilities/get-remediation-item-details
scraped: 2026-03-06T21:35:17.504404
---

# Vulnerabilities API - GET сведения об элементе исправления

# Vulnerabilities API - GET сведения об элементе исправления

* Справочник
* Обновлено 25 сентября 2024 г.

Возвращает сведения о группе процессов [отслеживания исправлений](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Отслеживайте прогресс исправления уязвимостей.") для сторонней уязвимости (или, в случае уязвимостей Kubernetes, параметры узла Kubernetes для отслеживания исправлений).

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/securityProblems/{id}/remediationItems/{remediationItemId}` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems/{remediationItemId}` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью действия `securityProblems.read`.

Чтобы узнать, как получить и использовать токен, см. [Токены и аутентификация](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | Идентификатор запрашиваемой сторонней проблемы безопасности. | path | Обязательный |
| remediationItemId | string | Идентификатор элемента исправления. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [RemediationDetailsItem](#openapi-definition-RemediationDetailsItem) | Успешно. Ответ содержит сведения об одном элементе исправления проблемы безопасности. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `RemediationDetailsItem`

Подробная информация об элементе исправления для проблемы безопасности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| assessment | [RemediationAssessment](#openapi-definition-RemediationAssessment) | Оценка элемента исправления. |
| entityIds | string[] | - |
| firstAffectedTimestamp | integer | - |
| id | string | - |
| muteState | [RemediationItemMuteState](#openapi-definition-RemediationItemMuteState) | Состояние отключения уведомлений для элемента исправления проблемы безопасности. |
| name | string | - |
| remediationProgress | [RemediationProgress](#openapi-definition-RemediationProgress) | Прогресс данного элемента исправления. Содержит затронутые и незатронутые сущности. |
| resolvedTimestamp | integer | - |
| trackingLink | [TrackingLink](#openapi-definition-TrackingLink) | URL внешней ссылки для отслеживания, связанной с исправляемой сущностью проблемы безопасности. |
| vulnerabilityState | string | - Элемент может принимать следующие значения: * `RESOLVED` * `VULNERABLE` |
| vulnerableComponents | [RemediationItemDetailsVulnerableComponent[]](#openapi-definition-RemediationItemDetailsVulnerableComponent) | Список уязвимых компонентов элемента исправления. Уязвимый компонент — это то, что вызывает проблему безопасности. |

#### Объект `RemediationAssessment`

Оценка элемента исправления.

| Элемент | Тип | Описание |
| --- | --- | --- |
| assessmentAccuracy | string | Точность оценки. Элемент может принимать следующие значения: * `FULL` * `NOT_AVAILABLE` * `REDUCED` |
| assessmentAccuracyDetails | [AssessmentAccuracyDetails](#openapi-definition-AssessmentAccuracyDetails) | Подробности точности оценки. |
| dataAssets | string | Доступность связанных информационных активов для затронутых сущностей. Элемент может принимать следующие значения: * `NOT_AVAILABLE` * `NOT_DETECTED` * `REACHABLE` |
| exposure | string | Уровень доступности затронутых сущностей. Элемент может принимать следующие значения: * `NOT_AVAILABLE` * `NOT_DETECTED` * `PUBLIC_NETWORK` |
| numberOfDataAssets | integer | Количество связанных информационных активов. |
| vulnerableFunctionRestartRequired | boolean | Требуется ли перезапуск для получения актуальных данных об уязвимых функциях. |
| vulnerableFunctionUsage | string | Использование уязвимых функций. Элемент может принимать следующие значения: * `IN_USE` * `NOT_AVAILABLE` * `NOT_IN_USE` |
| vulnerableFunctionsInUse | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | Список используемых уязвимых функций. |
| vulnerableFunctionsNotAvailable | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | Список уязвимых функций, данные о которых недоступны. |
| vulnerableFunctionsNotInUse | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | Список неиспользуемых уязвимых функций. |

#### Объект `AssessmentAccuracyDetails`

Подробности точности оценки.

| Элемент | Тип | Описание |
| --- | --- | --- |
| reducedReasons | string[] | Причина пониженной точности оценки. Элемент может принимать следующие значения: * `LIMITED_AGENT_SUPPORT` * `LIMITED_BY_CONFIGURATION` |

#### Объект `VulnerableFunction`

Определяет уязвимую функцию.

| Элемент | Тип | Описание |
| --- | --- | --- |
| className | string | Имя класса уязвимой функции. |
| filePath | string | Путь к файлу уязвимой функции. |
| functionName | string | Имя уязвимой функции. |

#### Объект `RemediationItemMuteState`

Состояние отключения уведомлений для элемента исправления проблемы безопасности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| comment | string | Краткий комментарий о последнем изменении состояния отключения. |
| lastUpdatedTimestamp | integer | Временная метка (в миллисекундах UTC) последнего обновления состояния отключения. |
| muted | boolean | Элемент исправления отключён (`true`) или не отключён (`false`). |
| reason | string | Причина последнего изменения состояния отключения. Элемент может принимать следующие значения: * `AFFECTED` * `CONFIGURATION_NOT_AFFECTED` * `FALSE_POSITIVE` * `IGNORE` * `INITIAL_STATE` * `OTHER` * `VULNERABLE_CODE_NOT_IN_USE` |
| user | string | Пользователь, последним изменивший состояние отключения. |

#### Объект `RemediationProgress`

Прогресс данного элемента исправления. Содержит затронутые и незатронутые сущности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| affectedEntities | string[] | Список связанных сущностей, затронутых проблемой безопасности. |
| unaffectedEntities | string[] | Список связанных сущностей, затронутых проблемой безопасности. |

#### Объект `TrackingLink`

URL внешней ссылки для отслеживания, связанной с исправляемой сущностью проблемы безопасности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| displayName | string | Отображаемое имя (заголовок) ссылки для отслеживания, например 'ISSUE-123'. |
| lastUpdatedTimestamp | integer | Временная метка (в миллисекундах UTC) последнего обновления ссылки для отслеживания. |
| url | string | URL-адрес ссылки для отслеживания, например https://example.com/ISSUE-123 |
| user | string | Пользователь, последним изменивший ссылку для отслеживания. |

#### Объект `RemediationItemDetailsVulnerableComponent`

Уязвимый компонент с подробными сведениями для элемента исправления (PG).

| Элемент | Тип | Описание |
| --- | --- | --- |
| affectedEntities | string[] | Список затронутых сущностей. |
| displayName | string | Отображаемое имя уязвимого компонента. |
| fileName | string | Имя файла уязвимого компонента. |
| id | string | Идентификатор сущности Dynatrace уязвимого компонента. |
| loadOrigins | string[] | Источники загрузки уязвимых компонентов. |
| numberOfAffectedEntities | integer | Количество затронутых сущностей. |
| shortName | string | Краткое имя уязвимого компонента (только компонент). |

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
| parameterLocation | string | - Элемент может принимать следующие значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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

Запрос исправляемой сущности.

Обязательные фильтры:

* `securityProblemid`
* `remediationItemId`

#### Curl

```
curl -X 'GET' 'https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/7412525767433554374/remediationItems/PROCESS_GROUP-F32C09AEDCB7A450' \



-H 'accept: application/json; charset=utf-8' \



-H 'Authorization: Api-Token [your_token]'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/7412525767433554374/remediationItems/PROCESS_GROUP-F32C09AEDCB7A4
```

#### Тело ответа

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

* [Application Security](/docs/secure/application-security "Доступ к функциям Dynatrace Application Security.")
* [Davis Security Advisor API](/docs/dynatrace-api/environment-api/application-security/davis-security-advice "Просмотр рекомендаций Davis Security Advisor через Dynatrace API.")
* [Отслеживание исправлений](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Отслеживайте прогресс исправления уязвимостей.")
