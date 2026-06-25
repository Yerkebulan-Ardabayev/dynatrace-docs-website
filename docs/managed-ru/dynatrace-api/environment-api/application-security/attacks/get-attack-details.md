---
title: Attacks API - GET attack details
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/application-security/attacks/get-attack-details
scraped: 2026-05-12T11:58:06.162042
---

# Attacks API - GET attack details

# Attacks API - GET attack details

* Reference
* Published Aug 30, 2023

Возвращает детали конкретной [атаки](/managed/secure/application-security/application-protection/manage-attacks "Отслеживайте атаки на код вашего приложения.").

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/attacks/{id}` |
| GET | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/attacks/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `attacks.read`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID атаки. | path | Обязательный |
| fields | string | Список дополнительных свойств атаки, которые можно добавить в ответ.  Доступны следующие свойства (все остальные свойства всегда включены, и их нельзя убрать из ответа):  * `attackTarget`: Целевой host/database атаки. * `request`: Запрос, отправленный от атакующего. * `entrypoint`: Точка входа, использованная атакующим для начала конкретной атаки. * `vulnerability`: Уязвимость, использованная атакой. * `securityProblem`: Связанная security problem. * `attacker`: Атакующий. * `managementZones`: Связанные management zones.  Чтобы добавить свойства, укажите их через запятую и поставьте перед каждым свойством знак плюс (например, `+attackTarget,+securityProblem`). | query | Опциональный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [Attack](#openapi-definition-Attack) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

#### Объект `Attack`

Описывает атаку.

| Элемент | Тип | Описание |
| --- | --- | --- |
| affectedEntities | [AffectedEntities](#openapi-definition-AffectedEntities) | Информация о затронутых сущностях атаки. |
| attackId | string | ID атаки. |
| attackTarget | [AttackTarget](#openapi-definition-AttackTarget) | Информация о целевом host/database атаки. |
| attackType | string | Тип атаки. Элемент может принимать значения * `COMMAND_INJECTION` * `JNDI_INJECTION` * `SQL_INJECTION` * `SSRF` |
| attacker | [Attacker](#openapi-definition-Attacker) | Атакующий. |
| displayId | string | Display ID атаки. |
| displayName | string | Display name атаки. |
| entrypoint | [AttackEntrypoint](#openapi-definition-AttackEntrypoint) | Описывает точку входа, использованную атакующим для начала конкретной атаки. |
| managementZones | [ManagementZone[]](#openapi-definition-ManagementZone) | Список management zones, к которым принадлежат затронутые сущности. |
| request | [RequestInformation](#openapi-definition-RequestInformation) | Описывает полную информацию о запросе атаки. |
| securityProblem | [AttackSecurityProblem](#openapi-definition-AttackSecurityProblem) | Информация об оценке и ID security problem, связанной с атакой. |
| state | string | Состояние атаки. Элемент может принимать значения * `ALLOWLISTED` * `BLOCKED` * `EXPLOITED` |
| technology | string | Технология атаки. Элемент может принимать значения * `DOTNET` * `GO` * `JAVA` * `NODE_JS` |
| timestamp | integer | Временная метка, когда произошла атака. |
| vulnerability | [Vulnerability](#openapi-definition-Vulnerability) | Описывает использованную уязвимость. |

#### Объект `AffectedEntities`

Информация о затронутых сущностях атаки.

| Элемент | Тип | Описание |
| --- | --- | --- |
| processGroup | [AffectedEntity](#openapi-definition-AffectedEntity) | Информация о затронутой сущности. |
| processGroupInstance | [AffectedEntity](#openapi-definition-AffectedEntity) | Информация о затронутой сущности. |

#### Объект `AffectedEntity`

Информация о затронутой сущности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | Monitored entity ID затронутой сущности. |
| name | string | Имя затронутой сущности. |

#### Объект `AttackTarget`

Информация о целевом host/database атаки.

| Элемент | Тип | Описание |
| --- | --- | --- |
| entityId | string | Monitored entity ID целевого host/database. |
| name | string | Имя целевого host/database. |

#### Объект `Attacker`

Атакующий.

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | [AttackerLocation](#openapi-definition-AttackerLocation) | Местоположение атакующего. |
| sourceIp | string | Source IP атакующего. |

#### Объект `AttackerLocation`

Местоположение атакующего.

| Элемент | Тип | Описание |
| --- | --- | --- |
| city | string | Город атакующего. |
| country | string | Страна атакующего. |
| countryCode | string | Код страны атакующего согласно стандарту ISO 3166-1 Alpha-2. |

#### Объект `AttackEntrypoint`

Описывает точку входа, использованную атакующим для начала конкретной атаки.

| Элемент | Тип | Описание |
| --- | --- | --- |
| codeLocation | [CodeLocation](#openapi-definition-CodeLocation) | Информация о расположении в коде. |
| entrypointFunction | [FunctionDefinition](#openapi-definition-FunctionDefinition) | Информация об определении функции. |
| payload | object[] | Список значений, который мог быть усечён. |

#### Объект `CodeLocation`

Информация о расположении в коде.

| Элемент | Тип | Описание |
| --- | --- | --- |
| className | string | Полное имя класса для расположения в коде. |
| columnNumber | integer | Номер столбца расположения в коде. |
| displayName | string | Человекочитаемое строковое представление расположения в коде. |
| fileName | string | Имя файла расположения в коде. |
| functionName | string | Имя функции/метода расположения в коде. |
| lineNumber | integer | Номер строки расположения в коде. |
| parameterTypes | [TruncatableListString](#openapi-definition-TruncatableListString) | Список значений, который мог быть усечён. |
| returnType | string | Тип возвращаемого значения функции. |

#### Объект `TruncatableListString`

Список значений, который мог быть усечён.

| Элемент | Тип | Описание |
| --- | --- | --- |
| truncationInfo | [TruncationInfo](#openapi-definition-TruncationInfo) | Информация о возможном усечении. |
| values | string[] | Значения списка. |

#### Объект `TruncationInfo`

Информация о возможном усечении.

| Элемент | Тип | Описание |
| --- | --- | --- |
| truncated | boolean | Был ли список/значение усечён. |

#### Объект `FunctionDefinition`

Информация об определении функции.

| Элемент | Тип | Описание |
| --- | --- | --- |
| className | string | Полное имя класса, включающего функцию. |
| displayName | string | Человекочитаемое строковое представление определения функции. |
| fileName | string | Имя файла определения функции. |
| functionName | string | Имя функции/метода определения функции. |
| parameterTypes | [TruncatableListString](#openapi-definition-TruncatableListString) | Список значений, который мог быть усечён. |
| returnType | string | Тип возвращаемого значения функции. |

#### Объект `EntrypointPayload`

Описывает payload, отправленный в точку входа во время атаки.

| Элемент | Тип | Описание |
| --- | --- | --- |
| name | string | Имя payload, если применимо. |
| type | string | Тип payload. Элемент может принимать значения * `HTTP_BODY` * `HTTP_COOKIE` * `HTTP_HEADER_NAME` * `HTTP_HEADER_VALUE` * `HTTP_OTHER` * `HTTP_PARAMETER_NAME` * `HTTP_PARAMETER_VALUE` * `HTTP_URL` * `UNKNOWN` |
| value | string | Значение payload. |

#### Объект `ManagementZone`

Краткое представление management zone.

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | ID management zone. |
| name | string | Имя management zone. |

#### Объект `RequestInformation`

Описывает полную информацию о запросе атаки.

| Элемент | Тип | Описание |
| --- | --- | --- |
| host | string | Целевой host запроса. |
| path | string | Путь запроса. |
| protocolDetails | [ProtocolDetails](#openapi-definition-ProtocolDetails) | Детали, специфичные для использованного протокола. |
| url | string | URL запроса. |

#### Объект `ProtocolDetails`

Детали, специфичные для использованного протокола.

| Элемент | Тип | Описание |
| --- | --- | --- |
| http | [HttpProtocolDetails](#openapi-definition-HttpProtocolDetails) | HTTP-специфичные детали запроса. |

#### Объект `HttpProtocolDetails`

HTTP-специфичные детали запроса.

| Элемент | Тип | Описание |
| --- | --- | --- |
| headers | [TruncatableListAttackRequestHeader](#openapi-definition-TruncatableListAttackRequestHeader) | Список значений, который мог быть усечён. |
| parameters | [TruncatableListHttpRequestParameter](#openapi-definition-TruncatableListHttpRequestParameter) | Список значений, который мог быть усечён. |
| requestMethod | string | HTTP-метод запроса. |

#### Объект `TruncatableListAttackRequestHeader`

Список значений, который мог быть усечён.

| Элемент | Тип | Описание |
| --- | --- | --- |
| truncationInfo | [TruncationInfo](#openapi-definition-TruncationInfo) | Информация о возможном усечении. |
| values | [AttackRequestHeader[]](#openapi-definition-AttackRequestHeader) | Значения списка. |

#### Объект `AttackRequestHeader`

Элемент заголовка запроса атаки.

| Элемент | Тип | Описание |
| --- | --- | --- |
| name | string | Имя элемента заголовка. |
| value | string | Значение элемента заголовка. |

#### Объект `TruncatableListHttpRequestParameter`

Список значений, который мог быть усечён.

| Элемент | Тип | Описание |
| --- | --- | --- |
| truncationInfo | [TruncationInfo](#openapi-definition-TruncationInfo) | Информация о возможном усечении. |
| values | [HttpRequestParameter[]](#openapi-definition-HttpRequestParameter) | Значения списка. |

#### Объект `HttpRequestParameter`

Параметр HTTP-запроса.

| Элемент | Тип | Описание |
| --- | --- | --- |
| name | string | Имя параметра. |
| value | string | Значение параметра. |

#### Объект `AttackSecurityProblem`

Информация об оценке и ID security problem, связанной с атакой.

| Элемент | Тип | Описание |
| --- | --- | --- |
| assessment | [AttackSecurityProblemAssessmentDto](#openapi-definition-AttackSecurityProblemAssessmentDto) | Оценка security problem, связанной с атакой. |
| securityProblemId | string | ID security problem. |

#### Объект `AttackSecurityProblemAssessmentDto`

Оценка security problem, связанной с атакой.

| Элемент | Тип | Описание |
| --- | --- | --- |
| dataAssets | string | Доступность data assets для атакованной цели. Элемент может принимать значения * `NOT_AVAILABLE` * `NOT_DETECTED` * `REACHABLE` |
| exposure | string | Уровень exposure атакованной цели. Элемент может принимать значения * `NOT_AVAILABLE` * `NOT_DETECTED` * `PUBLIC_NETWORK` |
| numberOfReachableDataAssets | integer | Количество data assets, доступных для атакованной цели. |

#### Объект `Vulnerability`

Описывает использованную уязвимость.

| Элемент | Тип | Описание |
| --- | --- | --- |
| codeLocation | [CodeLocation](#openapi-definition-CodeLocation) | Информация о расположении в коде. |
| displayName | string | Display name уязвимости. |
| vulnerabilityId | string | ID уязвимости. |
| vulnerableFunction | [FunctionDefinition](#openapi-definition-FunctionDefinition) | Информация об определении функции. |
| vulnerableFunctionInput | [VulnerableFunctionInput](#openapi-definition-VulnerableFunctionInput) | Описывает, что было передано в code-level уязвимость. |

#### Объект `VulnerableFunctionInput`

Описывает, что было передано в code-level уязвимость.

| Элемент | Тип | Описание |
| --- | --- | --- |
| inputSegments | [VulnerableFunctionInputSegment[]](#openapi-definition-VulnerableFunctionInputSegment) | Список сегментов ввода. |
| type | string | Тип ввода. Элемент может принимать значения * `COMMAND` * `HTTP_CLIENT` * `JNDI` * `SQL_STATEMENT` |

#### Объект `VulnerableFunctionInputSegment`

Описывает один сегмент, переданный в уязвимую функцию.

| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Тип сегмента ввода. Элемент может принимать значения * `MALICIOUS_INPUT` * `REGULAR_INPUT` * `TAINTED_INPUT` |
| value | string | Значение сегмента ввода. |

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



"affectedEntities": {



"processGroup": {



"id": "string",



"name": "string"



},



"processGroupInstance": {}



},



"attackId": "string",



"attackTarget": {



"entityId": "string",



"name": "string"



},



"attackType": "COMMAND_INJECTION",



"attacker": {



"location": {



"city": "string",



"country": "string",



"countryCode": "string"



},



"sourceIp": "string"



},



"displayId": "string",



"displayName": "string",



"entrypoint": {



"codeLocation": {



"className": "string",



"columnNumber": 1,



"displayName": "string",



"fileName": "string",



"functionName": "string",



"lineNumber": 1,



"parameterTypes": {



"truncationInfo": {



"truncated": true



},



"values": [



"string"



]



},



"returnType": "string"



},



"entrypointFunction": {



"className": "string",



"displayName": "string",



"fileName": "string",



"functionName": "string",



"parameterTypes": {},



"returnType": "string"



},



"payload": [



{



"truncationInfo": {},



"values": [



{



"name": "string",



"type": "HTTP_BODY",



"value": "string"



}



]



}



]



},



"managementZones": [



{



"id": "string",



"name": "string"



}



],



"request": {



"host": "string",



"path": "string",



"protocolDetails": {



"http": {



"headers": {



"truncationInfo": {},



"values": [



{



"name": "string",



"value": "string"



}



]



},



"parameters": {



"truncationInfo": {},



"values": [



{



"name": "string",



"value": "string"



}



]



},



"requestMethod": "string"



}



},



"url": "string"



},



"securityProblem": {



"assessment": {



"dataAssets": "NOT_AVAILABLE",



"exposure": "NOT_AVAILABLE",



"numberOfReachableDataAssets": 1



},



"securityProblemId": "string"



},



"state": "ALLOWLISTED",



"technology": "DOTNET",



"timestamp": 1,



"vulnerability": {



"codeLocation": {},



"displayName": "string",



"vulnerabilityId": "string",



"vulnerableFunction": {},



"vulnerableFunctionInput": {



"inputSegments": [



{



"type": "MALICIOUS_INPUT",



"value": "string"



}



],



"type": "COMMAND"



}



}



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

* [Application Security](/managed/secure/application-security "Доступ к функциям Dynatrace Application Security.")
* [Davis Security Advisor API](/managed/dynatrace-api/environment-api/application-security/davis-security-advice "Просмотрите рекомендации Davis Security Advisor через Dynatrace API.")
* [Manage attacks](/managed/secure/application-security/application-protection/manage-attacks "Отслеживайте атаки на код вашего приложения.")