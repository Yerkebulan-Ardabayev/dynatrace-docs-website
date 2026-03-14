---
title: Уязвимости API - Получение элементов исправления
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/application-security/vulnerabilities/get-remediation-items
scraped: 2026-03-05T21:33:07.529890
---

# Vulnerabilities API — GET элементов исправления

# Vulnerabilities API — GET элементов исправления

* Справочник
* Обновлено 3 мая 2022 г.

Возвращает список групп процессов [отслеживания исправлений](../../../../secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking.md "Track the remediation progress of vulnerabilities.") для сторонней уязвимости (или, в случае уязвимостей Kubernetes, узлов Kubernetes для отслеживания исправлений).

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/securityProblems/{id}/remediationItems` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью действия `securityProblems.read`.

Чтобы узнать, как получить и использовать его, см. [Токены и аутентификация](../../../../discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication.md).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | Идентификатор запрашиваемой сторонней проблемы безопасности. | path | Обязательный |
| remediationItemSelector | string | Определяет область действия запроса. В ответ включаются только исправляемые сущности, соответствующие указанным критериям.  Вы можете добавить один или несколько следующих критериев. Значения *не* чувствительны к регистру, и используется оператор `EQUALS`, если не указано иное.  * Состояние уязвимости: `vulnerabilityState("value")`. Возможные значения: `VULNERABLE` и `RESOLVED`. Если не задано, возвращаются все сущности. * Заглушено: `muted("value")`. Возможные значения: `TRUE` или `FALSE`. * Оценка доступности данных: `assessment.dataAssets("value")`. Возможные значения: `REACHABLE` и `NOT_DETECTED`. * Оценка сетевой доступности: `assessment.exposure("value")`. Возможные значения: `PUBLIC_NETWORK` и `NOT_DETECTED`. * Оценка использования уязвимых функций: `assessment.vulnerableFunctionUsage("value")`. Возможные значения: `IN_USE` и `NOT_IN_USE`. * Требуется перезапуск для уязвимых функций: `assessment.vulnerableFunctionRestartRequired("value")`. Возможные значения: `TRUE` или `FALSE`. * Используемые уязвимые функции содержат: `assessment.vulnerableFunctionInUseContains("value")`. Возможные значения: `class::function`, `class::` и `function`. Используется оператор `CONTAINS`. Учитываются только используемые уязвимые функции. * Точность оценки: `assessment.accuracy("value")`. Возможные значения: `FULL` и `REDUCED`. * Имя сущности содержит: `entityNameContains("value-1")`. Используется оператор `CONTAINS`. * Отображаемое имя ссылки отслеживания: `trackingLink.displayNameContains("value")`. Используется оператор `CONTAINS`.  Для указания нескольких критериев разделите их запятой (`,`). В ответ включаются только результаты, соответствующие **всем** критериям.  Значение критерия указывается в кавычках. Следующие специальные символы должны быть экранированы тильдой (`~`) внутри кавычек:  * Тильда `~` * Кавычка `"` | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [RemediationItemList](#openapi-definition-RemediationItemList) | Успех. Ответ содержит список элементов исправления проблемы. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `RemediationItemList`

Список элементов исправления.

| Элемент | Тип | Описание |
| --- | --- | --- |
| remediationItems | [RemediationItem[]](#openapi-definition-RemediationItem) | Список элементов исправления. |

#### Объект `RemediationItem`

Возможное исправление для проблемы безопасности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| assessment | [RemediationAssessment](#openapi-definition-RemediationAssessment) | Оценка элемента исправления. |
| entityIds | string[] | - |
| firstAffectedTimestamp | integer | - |
| id | string | - |
| muteState | [RemediationItemMuteState](#openapi-definition-RemediationItemMuteState) | Состояние заглушения элемента исправления проблемы безопасности. |
| name | string | - |
| remediationProgress | [RemediationProgress](#openapi-definition-RemediationProgress) | Прогресс этого элемента исправления. Содержит затронутые и незатронутые сущности. |
| resolvedTimestamp | integer | - |
| trackingLink | [TrackingLink](#openapi-definition-TrackingLink) | URL внешней ссылки отслеживания, связанной с исправляемой сущностью проблемы безопасности. |
| vulnerabilityState | string | - Элемент может содержать следующие значения: * `RESOLVED` * `VULNERABLE` |
| vulnerableComponents | [VulnerableComponent[]](#openapi-definition-VulnerableComponent) | Список уязвимых компонентов элемента исправления.  Уязвимый компонент — это то, что вызывает проблему безопасности. |

#### Объект `RemediationAssessment`

Оценка элемента исправления.

| Элемент | Тип | Описание |
| --- | --- | --- |
| assessmentAccuracy | string | Точность оценки. Элемент может содержать следующие значения: * `FULL` * `NOT_AVAILABLE` * `REDUCED` |
| assessmentAccuracyDetails | [AssessmentAccuracyDetails](#openapi-definition-AssessmentAccuracyDetails) | Детали точности оценки. |
| dataAssets | string | Достижимость связанных активов данных затронутыми сущностями. Элемент может содержать следующие значения: * `NOT_AVAILABLE` * `NOT_DETECTED` * `REACHABLE` |
| exposure | string | Уровень доступности затронутых сущностей. Элемент может содержать следующие значения: * `NOT_AVAILABLE` * `NOT_DETECTED` * `PUBLIC_NETWORK` |
| numberOfDataAssets | integer | Количество связанных активов данных. |
| vulnerableFunctionRestartRequired | boolean | Требуется ли перезапуск для получения последних данных об уязвимых функциях. |
| vulnerableFunctionUsage | string | Использование уязвимых функций. Элемент может содержать следующие значения: * `IN_USE` * `NOT_AVAILABLE` * `NOT_IN_USE` |
| vulnerableFunctionsInUse | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | Список используемых уязвимых функций. |
| vulnerableFunctionsNotAvailable | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | Список недоступных уязвимых функций. |
| vulnerableFunctionsNotInUse | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | Список неиспользуемых уязвимых функций. |

#### Объект `AssessmentAccuracyDetails`

Детали точности оценки.

| Элемент | Тип | Описание |
| --- | --- | --- |
| reducedReasons | string[] | Причина сниженной точности оценки. Элемент может содержать следующие значения: * `LIMITED_AGENT_SUPPORT` * `LIMITED_BY_CONFIGURATION` |

#### Объект `VulnerableFunction`

Определяет уязвимую функцию.

| Элемент | Тип | Описание |
| --- | --- | --- |
| className | string | Имя класса уязвимой функции. |
| filePath | string | Путь к файлу уязвимой функции. |
| functionName | string | Имя уязвимой функции. |

#### Объект `RemediationItemMuteState`

Состояние заглушения элемента исправления проблемы безопасности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| comment | string | Краткий комментарий о последнем изменении состояния заглушения. |
| lastUpdatedTimestamp | integer | Метка времени (UTC в миллисекундах) последнего обновления состояния заглушения. |
| muted | boolean | Исправление заглушено (`true`) или не заглушено (`false`). |
| reason | string | Причина последнего изменения состояния заглушения. Элемент может содержать следующие значения: * `AFFECTED` * `CONFIGURATION_NOT_AFFECTED` * `FALSE_POSITIVE` * `IGNORE` * `INITIAL_STATE` * `OTHER` * `VULNERABLE_CODE_NOT_IN_USE` |
| user | string | Пользователь, который последним изменил состояние заглушения. |

#### Объект `RemediationProgress`

Прогресс этого элемента исправления. Содержит затронутые и незатронутые сущности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| affectedEntities | string[] | Список связанных сущностей, затронутых проблемой безопасности. |
| unaffectedEntities | string[] | Список связанных сущностей, не затронутых проблемой безопасности. |

#### Объект `TrackingLink`

URL внешней ссылки отслеживания, связанной с исправляемой сущностью проблемы безопасности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| displayName | string | Отображаемое имя (заголовок), установленное для ссылки отслеживания, например, 'ISSUE-123'. |
| lastUpdatedTimestamp | integer | Метка времени (UTC в миллисекундах) последнего обновления ссылки отслеживания. |
| url | string | URL, установленный для ссылки отслеживания, например, https://example.com/ISSUE-123 |
| user | string | Пользователь, который последним изменил ссылку отслеживания. |

#### Объект `VulnerableComponent`

Уязвимый компонент проблемы безопасности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| affectedEntities | string[] | Список затронутых сущностей. |
| displayName | string | Отображаемое имя уязвимого компонента. |
| fileName | string | Имя файла уязвимого компонента. |
| id | string | Идентификатор сущности Dynatrace уязвимого компонента. |
| numberOfAffectedEntities | integer | Количество затронутых сущностей. |
| shortName | string | Короткое имя уязвимого компонента (только компонент). |

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
| parameterLocation | string | - Элемент может содержать следующие значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"remediationItems": [



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



"numberOfAffectedEntities": 1,



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

Получение списка элементов исправления уязвимости `8788643471842202915`. Ответ сокращён до двух записей.

#### Curl

```
curl --request GET \



--url https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/8788643471842202915/remediationItems \



--header 'Authorization: Api-Token [your_token]'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/8788643471842202915/remediationItems
```

#### Тело ответа

```
{



"remediationItems": [



{



"id": "PROCESS_GROUP-70DF2C1374244F5A",



"entityIds": [



"PROCESS_GROUP-70DF2C1374244F5A"



],



"name": "KpiTomcatBackEnd-CWS-1-IG-144-HG",



"firstAffectedTimestamp": 1633531037359,



"assessment": {



"exposure": "NOT_DETECTED",



"dataAssets": "REACHABLE"



},



"vulnerabilityState": "VULNERABLE",



"muteState": {



"muted": false,



"user": "unknown",



"reason": "INITIAL_STATE"



},



"vulnerableComponents": [



{



"id": "SOFTWARE_COMPONENT-2559CD116033C217",



"displayName": "io.software.component.1.1",



"fileName": "io.software.component.1.1.jar",



"numberOfAffectedEntities": 2,



"affectedEntities": [



"PROCESS_GROUP_INSTANCE-3684888745E180D5",



"PROCESS_GROUP_INSTANCE-8F100796B9296962"



]



},



{



"id": "SOFTWARE_COMPONENT-0A679AA673B2B525",



"displayName": "io.software.component.loader.2.0.Final",



"fileName": "io.software.component.loader.2.0.jar",



"numberOfAffectedEntities": 4,



"affectedEntities": [



"PROCESS_GROUP_INSTANCE-0D133F13A28B477A",



"PROCESS_GROUP_INSTANCE-258962DC804FEDBC",



"PROCESS_GROUP_INSTANCE-3684888745E180D5",



"PROCESS_GROUP_INSTANCE-B79C2594071FBF6C"



]



}



],



"remediationProgress": {



"affectedEntities": [



"PROCESS_GROUP_INSTANCE-0D133F13A28B477A",



"PROCESS_GROUP_INSTANCE-258962DC804FEDBC",



"PROCESS_GROUP_INSTANCE-3684888745E180D5",



"PROCESS_GROUP_INSTANCE-8F100796B9296962",



"PROCESS_GROUP_INSTANCE-B79C2594071FBF6C"



],



"unaffectedEntities": [



"PROCESS_GROUP_INSTANCE-63AD33941D667CAC",



"PROCESS_GROUP_INSTANCE-E20A5DDF167AF3B8",



"PROCESS_GROUP_INSTANCE-F1166B3AB1F4312D",



"PROCESS_GROUP_INSTANCE-F9D0250A7432521D",



"PROCESS_GROUP_INSTANCE-FF1B355E4E252FA1"



]



}



},



{



"id": "PROCESS_GROUP-18407614632D87A6",



"entityIds": [



"PROCESS_GROUP-18407614632D87A6"



],



"name": "KpiTomcatFrontEnd-CWS-1-IG-67-HG",



"firstAffectedTimestamp": 1633531037359,



"assessment": {



"exposure": "PUBLIC_NETWORK",



"dataAssets": "NOT_DETECTED"



},



"resolvedTimestamp": 1636096094323,



"vulnerabilityState": "RESOLVED",



"muteState": {



"muted": false,



"user": "unknown",



"reason": "INITIAL_STATE"



},



"vulnerableComponents": [



{



"id": "SOFTWARE_COMPONENT-2559CD116033C217",



"displayName": "io.software.component.1.1.Final",



"fileName": "io.software.component.1.1.jar",



"numberOfAffectedEntities": 1,



"affectedEntities": [



"PROCESS_GROUP_INSTANCE-41115D4B6F8BFEEC"



]



}



],



"remediationProgress": {



"affectedEntities": [



"PROCESS_GROUP_INSTANCE-41115D4B6F8BFEEC"



],



"unaffectedEntities": [



"PROCESS_GROUP_INSTANCE-0189CF4780B4B872",



"PROCESS_GROUP_INSTANCE-2D54D85C45C0BA57",



"PROCESS_GROUP_INSTANCE-3E6373ACEA9DE722",



"PROCESS_GROUP_INSTANCE-47BCF72F93FF9528",



"PROCESS_GROUP_INSTANCE-6B5EF5C1A5ED42D0",



"PROCESS_GROUP_INSTANCE-BA18DB16A7A28A04",



"PROCESS_GROUP_INSTANCE-BCAECCB29AB12462",



"PROCESS_GROUP_INSTANCE-DD3CD2024A06BB5B",



"PROCESS_GROUP_INSTANCE-DE5B280889AC6569"



]



}



}



]



}
```

#### Код ответа

200

## Связанные темы

* [Application Security](../../../../secure/application-security.md "Access the Dynatrace Application Security functionalities.")
* [Davis Security Advisor API](../davis-security-advice.md "View the Davis Security Advisor recommendations via Dynatrace API.")
* [Отслеживание исправлений](../../../../secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking.md "Track the remediation progress of vulnerabilities.")