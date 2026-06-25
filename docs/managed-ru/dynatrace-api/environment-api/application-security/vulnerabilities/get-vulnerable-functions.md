---
title: Vulnerabilities API - GET vulnerable functions
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/application-security/vulnerabilities/get-vulnerable-functions
scraped: 2026-05-12T11:58:45.867594
---

# Vulnerabilities API - GET vulnerable functions

# Vulnerabilities API - GET vulnerable functions

* Reference
* Updated on Sep 25, 2024

Возвращает список уязвимых функций и их использование.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/securityProblems/{id}/vulnerableFunctions` |
| GET | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/{id}/vulnerableFunctions` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `securityProblems.read`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID требуемой third-party security problem. | path | Обязательный |
| vulnerableFunctionsSelector | string | Определяет область запроса. В ответ включаются только уязвимые функции, соответствующие указанным критериям.  Можно добавить следующие критерии. Значения *не* регистрозависимы, и используется оператор `EQUALS`, если не указано иное.  * Management zone ID: `managementZoneIds("mzId-1", "mzId-2")`. * Management zone name: `managementZones("name-1", "name-2")`. Значения регистрозависимы. * Process group ID: `processGroupIds("pgId-1", "pgId-2")`. Здесь указывайте Dynatrace entity IDs. * Process group name: `processGroupNames("name-1", "name-2")`. Значения регистрозависимы. * Process group name contains: `processGroupNameContains("name-1")`. Используется оператор `CONTAINS`.  Указывайте значение критерия как строку в кавычках. Следующие специальные символы должны быть экранированы тильдой (`~`) внутри кавычек:  * Тильда `~` * Кавычка `"` | query | Опциональный |
| groupBy | string | Определяет дополнительные типы группировки, в которых должны отображаться уязвимые функции.  Можно добавить один из следующих типов группировки.  * Process group: `PROCESS_GROUP` | query | Опциональный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [VulnerableFunctionsContainer](#openapi-definition-VulnerableFunctionsContainer) | Успех. Ответ содержит список уязвимых функций. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

#### Объект `VulnerableFunctionsContainer`

Список уязвимых функций, их использований в рамках security problem и их использований по process group.
Опционально: список использований уязвимых функций по process group для security problem.

| Элемент | Тип | Описание |
| --- | --- | --- |
| vulnerableFunctions | [VulnerableFunctionProcessGroups[]](#openapi-definition-VulnerableFunctionProcessGroups) | Список уязвимых функций, их использований в рамках security problem и их использований по process group. |
| vulnerableFunctionsByProcessGroup | [ProcessGroupVulnerableFunctions[]](#openapi-definition-ProcessGroupVulnerableFunctions) | Список использований уязвимых функций по process group для security problem. Результат отсортирован по следующим критериям:  * количество используемых уязвимых функций (по убыванию). * количество неиспользуемых уязвимых функций (по убыванию). * количество недоступных уязвимых функций (по убыванию). * идентификатор process group (по возрастанию). |

#### Объект `VulnerableFunctionProcessGroups`

Уязвимая функция, включая её использование конкретными process groups в контексте security problem.

| Элемент | Тип | Описание |
| --- | --- | --- |
| function | [VulnerableFunction](#openapi-definition-VulnerableFunction) | Определяет уязвимую функцию. |
| processGroupsInUse | string[] | Идентификаторы process group, где эта уязвимая функция используется. |
| processGroupsNotAvailable | string[] | Идентификаторы process group, где информация об использовании этой функции недоступна. |
| processGroupsNotInUse | string[] | Идентификаторы process group, где эта уязвимая функция не используется. |
| usage | string | Использование уязвимой функции на основе заданных process groups:  * IN\_USE если хотя бы одна process group вызывает эту уязвимую функцию. * NOT\_IN\_USE если ни одна process group не вызывает эту уязвимую функцию. * NOT\_AVAILABLE если использование уязвимой функции не удалось определить хотя бы для одной process group и ни одна process group не вызывает эту уязвимую функцию. Элемент может принимать значения * `IN_USE` * `NOT_AVAILABLE` * `NOT_IN_USE` |

#### Объект `VulnerableFunction`

Определяет уязвимую функцию.

| Элемент | Тип | Описание |
| --- | --- | --- |
| className | string | Имя класса уязвимой функции. |
| filePath | string | Путь к файлу уязвимой функции. |
| functionName | string | Имя функции уязвимой функции. |

#### Объект `ProcessGroupVulnerableFunctions`

Уязвимые функции process group, включая их использование.

| Элемент | Тип | Описание |
| --- | --- | --- |
| functionsInUse | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | Список уязвимых функций в использовании. |
| functionsNotAvailable | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | Список уязвимых функций с неизвестным состоянием. |
| functionsNotInUse | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | Список неиспользуемых уязвимых функций. |
| processGroup | string | Идентификатор process group. |

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



"vulnerableFunctions": [



{



"function": {



"className": "string",



"filePath": "string",



"functionName": "string"



},



"processGroupsInUse": [



"string"



],



"processGroupsNotAvailable": [



"string"



],



"processGroupsNotInUse": [



"string"



],



"usage": "IN_USE"



}



],



"vulnerableFunctionsByProcessGroup": [



{



"functionsInUse": [



{}



],



"functionsNotAvailable": [



{}



],



"functionsNotInUse": [



{}



],



"processGroup": "string"



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

Для уязвимости с ID `2919200225913269102`, у которой есть используемые уязвимые функции, запросить оба представления уязвимых функций (уязвимая функция к `PROCESS_GROUP` и `PROCESS_GROUP` к уязвимой функции).

Обязательный фильтр: `groupBy=PROCESS_GROUP`.

#### Curl

```
curl -X 'GET' 'https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/vulnerableFunctions?groupBy=PROCESS_GROUP' \



-H 'accept: application/json; charset=utf-8' \



-H 'Authorization: Api-Token [your_token]'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/vulnerableFunctions?groupBy=PROCESS_GROUP
```

#### Response body

```
{



"vulnerableFunctions": [



{



"function": {



"className": "org.apache.coyote.http11.Http11InputBuffer",



"filePath": null,



"functionName": "parseHeader"



},



"usage": "IN_USE",



"processGroupsInUse": [



"PROCESS_GROUP-285FF9C91448BC8B"



],



"processGroupsNotInUse": [],



"processGroupsNotAvailable": []



}



],



"vulnerableFunctionsByProcessGroup": [



{



"processGroup": "PROCESS_GROUP-285FF9C91448BC8B",



"functionsInUse": [



{



"className": "org.apache.coyote.http11.Http11InputBuffer",



"filePath": null,



"functionName": "parseHeader"



}



],



"functionsNotInUse": [],



"functionsNotAvailable": []



}



]



}
```

## Связанные темы

* [Application Security](/managed/secure/application-security "Доступ к функциям Dynatrace Application Security.")
* [Davis Security Advisor API](/managed/dynatrace-api/environment-api/application-security/davis-security-advice "Просмотрите рекомендации Davis Security Advisor через Dynatrace API.")