---
title: Vulnerabilities API - GET элементы исправления
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/application-security/vulnerabilities/get-remediation-items
scraped: 2026-05-12T11:59:00.952966
---

# Vulnerabilities API - GET элементы исправления

# Vulnerabilities API - GET элементы исправления

* Reference
* Updated on May 03, 2022

Возвращает список групп процессов из [отслеживания исправления](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Отслеживание прогресса исправления уязвимостей.") для уязвимости стороннего компонента (или, в случае уязвимостей Kubernetes, узлов Kubernetes из отслеживания исправления).

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems` |

## Аутентификация

Для выполнения запроса необходим access token со scope `securityProblems.read`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательность |
| --- | --- | --- | --- | --- |
| id | string | Идентификатор запрашиваемой проблемы безопасности стороннего компонента. | path | Обязательный |
| remediationItemSelector | string | Определяет область запроса. В ответ попадают только подлежащие исправлению сущности, соответствующие указанным критериям.  Можно добавить один или несколько следующих критериев. Значения регистронезависимы, и по умолчанию используется оператор `EQUALS`, если не указано иначе.  * Состояние уязвимости: `vulnerabilityState("value")`. Возможные значения: `VULNERABLE`, `RESOLVED`. Если не задано, возвращаются все сущности. * Приглушено: `muted("value")`. Возможные значения: `TRUE` или `FALSE`. * Оценка доступности активов с данными: `assessment.dataAssets("value")`. Возможные значения: `REACHABLE`, `NOT_DETECTED`. * Оценка сетевой открытости: `assessment.exposure("value")`. Возможные значения: `PUBLIC_NETWORK`, `NOT_DETECTED`. * Оценка использования уязвимых функций: `assessment.vulnerableFunctionUsage("value")`. Возможные значения: `IN_USE`, `NOT_IN_USE`. * Требуется ли перезапуск для уязвимых функций: `assessment.vulnerableFunctionRestartRequired("value")`. Возможные значения: `TRUE` или `FALSE`. * Используемая уязвимая функция содержит: `assessment.vulnerableFunctionInUseContains("value")`. Возможные значения: `class::function`, `class::` и `function`. Используется оператор `CONTAINS`. Учитываются только используемые уязвимые функции. * Точность оценки: `assessment.accuracy("value")`. Возможные значения: `FULL` и `REDUCED`. * Имя сущности содержит: `entityNameContains("value-1")`. Используется оператор `CONTAINS`. * Отображаемое имя ссылки отслеживания: `trackingLink.displayNameContains("value")`. Используется оператор `CONTAINS`.  Чтобы задать несколько критериев, разделите их запятой (`,`). В ответ попадут только результаты, удовлетворяющие **всем** критериям.  Указывайте значение критерия как строку в кавычках. Следующие специальные символы внутри кавычек нужно экранировать тильдой (`~`):  * Тильда `~` * Кавычка `"` | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [RemediationItemList](#openapi-definition-RemediationItemList) | Успех. Ответ содержит список элементов исправления для проблемы. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `RemediationItemList`

Список элементов исправления.

| Элемент | Тип | Описание |
| --- | --- | --- |
| remediationItems | [RemediationItem[]](#openapi-definition-RemediationItem) | Список элементов исправления. |

#### Объект `RemediationItem`

Возможный вариант исправления проблемы безопасности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| assessment | [RemediationAssessment](#openapi-definition-RemediationAssessment) | Оценка элемента исправления. |
| entityIds | string[] | - |
| firstAffectedTimestamp | integer | - |
| id | string | - |
| muteState | [RemediationItemMuteState](#openapi-definition-RemediationItemMuteState) | Приглушённое состояние элемента исправления для проблемы безопасности. |
| name | string | - |
| remediationProgress | [RemediationProgress](#openapi-definition-RemediationProgress) | Прогресс этого элемента исправления. Содержит затронутые и незатронутые сущности. |
| resolvedTimestamp | integer | - |
| trackingLink | [TrackingLink](#openapi-definition-TrackingLink) | URL внешней ссылки отслеживания, связанной с подлежащей исправлению сущностью проблемы безопасности. |
| vulnerabilityState | string | -Элемент может принимать значения * `RESOLVED` * `VULNERABLE` |
| vulnerableComponents | [VulnerableComponent[]](#openapi-definition-VulnerableComponent) | Список уязвимых компонентов элемента исправления.  Уязвимый компонент это то, что вызывает проблему безопасности. |

#### Объект `RemediationAssessment`

Оценка элемента исправления.

| Элемент | Тип | Описание |
| --- | --- | --- |
| assessmentAccuracy | string | Точность оценки. Элемент может принимать значения * `FULL` * `NOT_AVAILABLE` * `REDUCED` |
| assessmentAccuracyDetails | [AssessmentAccuracyDetails](#openapi-definition-AssessmentAccuracyDetails) | Детали точности оценки. |
| dataAssets | string | Доступность связанных активов с данными для затронутых сущностей. Элемент может принимать значения * `NOT_AVAILABLE` * `NOT_DETECTED` * `REACHABLE` |
| exposure | string | Уровень открытости затронутых сущностей. Элемент может принимать значения * `NOT_AVAILABLE` * `NOT_DETECTED` * `PUBLIC_NETWORK` |
| numberOfDataAssets | integer | Количество связанных активов с данными. |
| vulnerableFunctionRestartRequired | boolean | Требуется ли перезапуск для получения актуальных данных об уязвимых функциях. |
| vulnerableFunctionUsage | string | Использование уязвимых функций. Элемент может принимать значения * `IN_USE` * `NOT_AVAILABLE` * `NOT_IN_USE` |
| vulnerableFunctionsInUse | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | Список используемых уязвимых функций. |
| vulnerableFunctionsNotAvailable | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | Список недоступных уязвимых функций. |
| vulnerableFunctionsNotInUse | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | Список не используемых уязвимых функций. |

#### Объект `AssessmentAccuracyDetails`

Детали точности оценки.

| Элемент | Тип | Описание |
| --- | --- | --- |
| reducedReasons | string[] | Причина пониженной точности оценки. Элемент может принимать значения * `LIMITED_AGENT_SUPPORT` * `LIMITED_BY_CONFIGURATION` |

#### Объект `VulnerableFunction`

Описывает уязвимую функцию.

| Элемент | Тип | Описание |
| --- | --- | --- |
| className | string | Имя класса уязвимой функции. |
| filePath | string | Путь к файлу уязвимой функции. |
| functionName | string | Имя уязвимой функции. |

#### Объект `RemediationItemMuteState`

Приглушённое состояние элемента исправления для проблемы безопасности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| comment | string | Короткий комментарий о последнем изменении приглушённого состояния. |
| lastUpdatedTimestamp | integer | Метка времени (в миллисекундах UTC) последнего обновления приглушённого состояния. |
| muted | boolean | Исправление приглушено (`true`) или нет (`false`). |
| reason | string | Причина последнего изменения приглушённого состояния. Элемент может принимать значения * `AFFECTED` * `CONFIGURATION_NOT_AFFECTED` * `FALSE_POSITIVE` * `IGNORE` * `INITIAL_STATE` * `OTHER` * `VULNERABLE_CODE_NOT_IN_USE` |
| user | string | Пользователь, который последний изменил приглушённое состояние. |

#### Объект `RemediationProgress`

Прогресс этого элемента исправления. Содержит затронутые и незатронутые сущности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| affectedEntities | string[] | Список связанных сущностей, затронутых проблемой безопасности. |
| unaffectedEntities | string[] | Список связанных сущностей, затронутых проблемой безопасности. |

#### Объект `TrackingLink`

URL внешней ссылки отслеживания, связанной с подлежащей исправлению сущностью проблемы безопасности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| displayName | string | Отображаемое имя (заголовок) ссылки отслеживания, например 'ISSUE-123'. |
| lastUpdatedTimestamp | integer | Метка времени (в миллисекундах UTC) последнего обновления ссылки отслеживания. |
| url | string | URL, заданный для ссылки отслеживания, например https://example.com/ISSUE-123 |
| user | string | Пользователь, который последний изменил ссылку отслеживания. |

#### Объект `VulnerableComponent`

Уязвимый компонент проблемы безопасности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| affectedEntities | string[] | Список затронутых сущностей. |
| displayName | string | Отображаемое имя уязвимого компонента. |
| fileName | string | Имя файла уязвимого компонента. |
| id | string | Идентификатор сущности Dynatrace для уязвимого компонента. |
| numberOfAffectedEntities | integer | Количество затронутых сущностей. |
| shortName | string | Короткое имя уязвимого компонента (только сам компонент, без версии и т. п.). |

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

Получение списка элементов исправления для уязвимости `8788643471842202915`. Ответ сокращён до двух записей.

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

* [Application Security](/managed/secure/application-security "Доступ к функциям Dynatrace Application Security.")
* [Davis Security Advisor API](/managed/dynatrace-api/environment-api/application-security/davis-security-advice "Просмотр рекомендаций Davis Security Advisor через Dynatrace API.")
* [Отслеживание исправления](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Отслеживание прогресса исправления уязвимостей.")