---
title: Vulnerabilities API - GET remediation item entities
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/application-security/vulnerabilities/get-remediation-item-entities
scraped: 2026-03-06T21:37:32.135216
---

# Vulnerabilities API - GET remediation item entities

# Vulnerabilities API - GET remediation item entities

* Справочник
* Обновлено 25 сентября 2024 г.

Возвращает список процессов [отслеживания исправлений](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Track the remediation progress of vulnerabilities.") для уязвимости сторонней библиотеки.

Запрос возвращает полезную нагрузку в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/securityProblems/{id}/remediationItems/{remediationItemId}/remediationProgressEntities` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems/{remediationItemId}/remediationProgressEntities` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью действия `securityProblems.read`.

Чтобы узнать, как получить и использовать такой токен, см. [Токены и аутентификация](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательность |
| --- | --- | --- | --- | --- |
| id | string | Идентификатор запрашиваемой проблемы безопасности сторонней библиотеки. | path | Обязательный |
| remediationItemId | string | Идентификатор элемента исправления. | path | Обязательный |
| remediationProgressEntitySelector | string | Определяет область запроса. В ответ включаются только сущности прогресса исправления, соответствующие указанным критериям.  Вы можете добавить один или несколько следующих критериев. Значения *нечувствительны* к регистру, и используется оператор `EQUALS`, если не указано иное.  * Состояние: `state("value")`. Возможные значения поля **state**: `AFFECTED` и `UNAFFECTED`. Если не задано, возвращаются все сущности. * Оценка использования уязвимой функции: `assessment.vulnerableFunctionUsage("value")` Возможные значения: `IN_USE` и `NOT_IN_USE`. * Требуется перезапуск уязвимой функции: `assessment.vulnerableFunctionRestartRequired("value")` Возможные значения: `TRUE` или `FALSE`. * Содержит используемую уязвимую функцию: `assessment.vulnerableFunctionInUseContains("value")`. Возможные значения: `class::function`, `class::` и `function`. Используется оператор `CONTAINS`. Учитываются только используемые уязвимые функции. * Имя сущности содержит: `entityNameContains("value-1")`. Используется оператор `CONTAINS`.  Для указания нескольких критериев разделяйте их запятой (`,`). В ответ включаются только результаты, соответствующие **всем** критериям.  Укажите значение критерия в виде строки в кавычках. Следующие специальные символы должны быть экранированы тильдой (`~`) внутри кавычек:  * Тильда `~` * Кавычка `"` | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [RemediationProgressEntityList](#openapi-definition-RemediationProgressEntityList) | Успех. Ответ содержит список сущностей прогресса исправления для элемента исправления проблемы безопасности. Количество возвращаемых сущностей ограничено. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `RemediationProgressEntityList`

Список сущностей прогресса исправления.

| Элемент | Тип | Описание |
| --- | --- | --- |
| remediationProgressEntities | [RemediationProgressEntity[]](#openapi-definition-RemediationProgressEntity) | Список сущностей прогресса исправления. |

#### Объект `RemediationProgressEntity`

Затронутая или незатронутая сущность исправления для проблемы безопасности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| assessment | [RemediationProgressEntityAssessment](#openapi-definition-RemediationProgressEntityAssessment) | Оценка сущности прогресса исправления. |
| firstAffectedTimestamp | integer | Метка времени, когда сущность прогресса исправления впервые была связана с уязвимостью. |
| id | string | Идентификатор сущности прогресса исправления. |
| name | string | Имя сущности прогресса исправления. |
| state | string | Текущее состояние сущности прогресса исправления. Элемент может содержать следующие значения: * `AFFECTED` * `UNAFFECTED` |
| vulnerableComponents | [RemediationProgressVulnerableComponent[]](#openapi-definition-RemediationProgressVulnerableComponent) | Список уязвимых компонентов элемента исправления.  Уязвимый компонент — это то, что вызывает проблему безопасности. |

#### Объект `RemediationProgressEntityAssessment`

Оценка сущности прогресса исправления.

| Элемент | Тип | Описание |
| --- | --- | --- |
| vulnerableFunctionRestartRequired | boolean | Требуется ли перезапуск для получения актуальных данных об уязвимых функциях. |
| vulnerableFunctionUsage | string | Использование уязвимых функций. Элемент может содержать следующие значения: * `IN_USE` * `NOT_AVAILABLE` * `NOT_IN_USE` |
| vulnerableFunctionsInUse | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | Список используемых уязвимых функций. |
| vulnerableFunctionsNotAvailable | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | Список недоступных уязвимых функций. |
| vulnerableFunctionsNotInUse | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | Список неиспользуемых уязвимых функций. |

#### Объект `VulnerableFunction`

Определяет уязвимую функцию.

| Элемент | Тип | Описание |
| --- | --- | --- |
| className | string | Имя класса уязвимой функции. |
| filePath | string | Путь к файлу уязвимой функции. |
| functionName | string | Имя уязвимой функции. |

#### Объект `RemediationProgressVulnerableComponent`

Уязвимый компонент с подробностями для сущности прогресса исправления (PGI).

| Элемент | Тип | Описание |
| --- | --- | --- |
| displayName | string | Отображаемое имя уязвимого компонента. |
| fileName | string | Имя файла уязвимого компонента. |
| id | string | Идентификатор сущности Dynatrace уязвимого компонента. |
| loadOrigins | string[] | Источники загрузки уязвимых компонентов. |
| shortName | string | Краткое, только компонентное имя уязвимого компонента. |

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

Просмотр текущих затронутых процессов элемента исправления.

Обязательный фильтр: `remediationProgressEntitySelector=state("AFFECTED")`.

#### Curl

```
curl -X 'GET' 'https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/7412525767433554374/remediationItems/PROCESS_GROUP-F32C09AEDCB7A450/remediationProgressEntities?remediationProgressEntitySelector=state%28%22AFFECTED%22%29' \



-H 'accept: application/json; charset=utf-8' \



-H 'Authorization: Api-Token [your_token]'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/7412525767433554374/remediationItems/PROCESS_GROUP-F32C09AEDCB7A450/remediationProgressEntities?remediationProgressEntitySelector=state%28%22AFFECTED%22%29
```

#### Тело ответа

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

* [Application Security](/docs/secure/application-security "Access the Dynatrace Application Security functionalities.")
* [Davis Security Advisor API](/docs/dynatrace-api/environment-api/application-security/davis-security-advice "View the Davis Security Advisor recommendations via Dynatrace API.")
* [Отслеживание исправлений](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Track the remediation progress of vulnerabilities.")
