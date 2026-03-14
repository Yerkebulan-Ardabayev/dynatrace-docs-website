---
title: Vulnerabilities API - GET vulnerable functions
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/application-security/vulnerabilities/get-vulnerable-functions
scraped: 2026-03-04T21:39:09.965555
---

# Vulnerabilities API — GET vulnerable functions


* Справочник
* Обновлено 25 сентября 2024 г.

Выводит список уязвимых функций и информацию об их использовании.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/securityProblems/{id}/vulnerableFunctions` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/{id}/vulnerableFunctions` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью действия `securityProblems.read`.

Подробнее о получении и использовании токена см. в разделе [Токены и аутентификация](../../../../discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication.md).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательность |
| --- | --- | --- | --- | --- |
| id | string | Идентификатор запрашиваемой проблемы безопасности сторонней библиотеки. | path | Обязательный |
| vulnerableFunctionsSelector | string | Определяет область запроса. В ответ включаются только уязвимые функции, соответствующие указанным критериям.  Можно добавить следующие критерии. Значения *не* чувствительны к регистру, и используется оператор `EQUALS`, если не указано иное.  * Идентификатор зоны управления: `managementZoneIds("mzId-1", "mzId-2")`. * Имя зоны управления: `managementZones("name-1", "name-2")`. Значения чувствительны к регистру. * Идентификатор группы процессов: `processGroupIds("pgId-1", "pgId-2")`. Укажите идентификаторы сущностей Dynatrace. * Имя группы процессов: `processGroupNames("name-1", "name-2")`. Значения чувствительны к регистру. * Имя группы процессов содержит: `processGroupNameContains("name-1")`. Используется оператор `CONTAINS`.  Укажите значение критерия в виде строки в кавычках. Следующие специальные символы должны быть экранированы тильдой (`~`) внутри кавычек:  * Тильда `~` * Кавычка `"` | query | Необязательный |
| groupBy | string | Определяет дополнительные типы группировки, в которых должны отображаться уязвимые функции.  Можно добавить один из следующих типов группировки.  * Группа процессов: `PROCESS_GROUP` | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [VulnerableFunctionsContainer](#openapi-definition-VulnerableFunctionsContainer) | Успех. Ответ содержит список уязвимых функций. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `VulnerableFunctionsContainer`

Список уязвимых функций, информация об их использовании в рамках проблемы безопасности и их использование по группам процессов.
Необязательно: список использования уязвимых функций по группам процессов для проблемы безопасности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| vulnerableFunctions | [VulnerableFunctionProcessGroups[]](#openapi-definition-VulnerableFunctionProcessGroups) | Список уязвимых функций, информация об их использовании в рамках проблемы безопасности и их использование по группам процессов. |
| vulnerableFunctionsByProcessGroup | [ProcessGroupVulnerableFunctions[]](#openapi-definition-ProcessGroupVulnerableFunctions) | Список использования уязвимых функций по группам процессов для проблемы безопасности. Результат сортируется по следующим критериям:  * количество используемых уязвимых функций (по убыванию). * количество неиспользуемых уязвимых функций (по убыванию). * количество уязвимых функций с недоступным статусом (по убыванию). * идентификатор группы процессов (по возрастанию) |

#### Объект `VulnerableFunctionProcessGroups`

Уязвимая функция, включая информацию о её использовании конкретными группами процессов в контексте проблемы безопасности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| function | [VulnerableFunction](#openapi-definition-VulnerableFunction) | Определяет уязвимую функцию. |
| processGroupsInUse | string[] | Идентификаторы групп процессов, в которых эта уязвимая функция используется. |
| processGroupsNotAvailable | string[] | Идентификаторы групп процессов, для которых информация об использовании этой функции недоступна. |
| processGroupsNotInUse | string[] | Идентификаторы групп процессов, в которых эта уязвимая функция не используется. |
| usage | string | Статус использования уязвимой функции на основе данных групп процессов:  * IN\_USE — если хотя бы одна группа процессов вызывает эту уязвимую функцию. * NOT\_IN\_USE — если ни одна группа процессов не вызывает эту уязвимую функцию. * NOT\_AVAILABLE — если информация об использовании уязвимой функции не может быть определена хотя бы для одной группы процессов, и ни одна группа процессов не вызывает эту функцию. Элемент может содержать следующие значения: * `IN_USE` * `NOT_AVAILABLE` * `NOT_IN_USE` |

#### Объект `VulnerableFunction`

Определяет уязвимую функцию.

| Элемент | Тип | Описание |
| --- | --- | --- |
| className | string | Имя класса уязвимой функции. |
| filePath | string | Путь к файлу уязвимой функции. |
| functionName | string | Имя уязвимой функции. |

#### Объект `ProcessGroupVulnerableFunctions`

Уязвимые функции группы процессов, включая информацию об их использовании.

| Элемент | Тип | Описание |
| --- | --- | --- |
| functionsInUse | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | Список используемых уязвимых функций. |
| functionsNotAvailable | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | Список уязвимых функций с неизвестным статусом. |
| functionsNotInUse | [VulnerableFunction[]](#openapi-definition-VulnerableFunction) | Список неиспользуемых уязвимых функций. |
| processGroup | string | Идентификатор группы процессов. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код HTTP-статуса |
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

Для уязвимости с идентификатором `2919200225913269102`, имеющей используемые уязвимые функции, запросите оба представления уязвимых функций (уязвимая функция к `PROCESS_GROUP` и `PROCESS_GROUP` к уязвимой функции).

Обязательный фильтр: `groupBy=PROCESS_GROUP`.

#### Curl

```
curl -X 'GET' 'https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/vulnerableFunctions?groupBy=PROCESS_GROUP' \


-H 'accept: application/json; charset=utf-8' \


-H 'Authorization: Api-Token [your_token]'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/vulnerableFunctions?groupBy=PROCESS_GROUP
```

#### Тело ответа

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

* [Application Security](../../../../secure/application-security.md "Доступ к функциям Dynatrace Application Security.")
* [Davis Security Advisor API](../davis-security-advice.md "Просмотр рекомендаций Davis Security Advisor через Dynatrace API.")
