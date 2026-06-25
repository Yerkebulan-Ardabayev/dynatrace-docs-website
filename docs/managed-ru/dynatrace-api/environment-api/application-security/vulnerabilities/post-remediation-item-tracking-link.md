---
title: Vulnerabilities API - POST remediation item tracking links
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/application-security/vulnerabilities/post-remediation-item-tracking-link
scraped: 2026-05-12T11:58:56.243299
---

# Vulnerabilities API - POST remediation item tracking links

# Vulnerabilities API - POST remediation item tracking links

* Reference
* Updated on Sep 25, 2024

Добавляет, редактирует или удаляет ссылки трекинга process groups [remediation tracking](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Отслеживайте прогресс устранения уязвимостей.") third-party уязвимости (или, в случае Kubernetes-уязвимостей, remediation tracking Kubernetes-узлов).

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems/trackingLinks` |
| POST | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems/trackingLinks` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `securityProblems.write`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID требуемой third-party security problem. | path | Обязательный |
| body | [RemediationItemsBulkUpdateDeleteDto](#openapi-definition-RemediationItemsBulkUpdateDeleteDto) | Содержит ассоциации внешних ссылок трекинга, которые нужно установить или удалить на remediation items security problem.  * Ссылки для установки должны быть отправлены в объекте `updates`. * Ссылки для удаления должны быть отправлены в массиве `deletes`.  Запрос должен содержать хотя бы одну запись для установки или удаления, чтобы быть валидным.  Конфликтующие изменения для одного и того же remediation item (ID появляется и в `deletes`, и в `updates`) отправлять нельзя.  Обратите внимание, что все обновления ссылок трекинга для security problem должны быть отправлены в одном запросе. | body | Опциональный |

### Объекты тела запроса

#### Объект `RemediationItemsBulkUpdateDeleteDto`

Содержит ассоциации внешних ссылок трекинга, которые нужно применить к remediation items security problem.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| deletes | string[] | Ссылки трекинга для удаления из security problem.  Список ID remediation items security problem, для которых нужно удалить ссылки трекинга. | Опциональный |
| updates | object | Ссылки трекинга для установки в security problem.  Map ID remediation item к объектам ссылки трекинга.  Ключи должны быть валидными ID remediation items security problem, связанное значение должно содержать ссылку для установки на элемент. | Опциональный |

#### Объект `TrackingLinkUpdate`

Ассоциация URL внешней ссылки трекинга, устанавливаемая для устранимой сущности security problem.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| displayName | string | Желаемое отображаемое имя (title) ссылки трекинга, установленное для remediation item, например, 'ISSUE-123'. | Обязательный |
| url | string | Желаемый URL ссылки трекинга, установленный для remediation item, например, https://example.com/ISSUE-123  Обратите внимание, что поддерживаются только валидные URL с протоколами 'http' или 'https'. | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

```
{



"deletes": [



"string"



],



"updates": {}



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Запрошенные ссылки трекинга обновлены. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

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

## Примеры

### Установка ссылок трекинга

Сетап: настроена автоматизация, создающая тикет для каждой устранимой сущности.

Цель: чтобы endpoint связал тикет с remediation item. Будут установлены следующие ссылки трекинга:

* `https://example.com/TICKET-46C0E12D9B0EF2D9` для `"PROCESS_GROUP-46C0E12D9B0EF2D9"`
* `https://example.com/TICKET-549E6AD75BD598EC` для `"PROCESS_GROUP-549E6AD75BD598EC"`

#### Curl

```
curl -X 'POST' 'https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/remediationItems/trackingLinks' \



-H 'accept: */*' \



-H 'Authorization: Api-Token [your_token]' \



-H 'Content-Type: application/json; charset=utf-8' \



-d '{



"updates": {



"PROCESS_GROUP-46C0E12D9B0EF2D9": {



"displayName": "TICKET-46C0E12D9B0EF2D9",



"url": "https://example.com/TICKET-46C0E12D9B0EF2D9"



},



"PROCESS_GROUP-549E6AD75BD598EC": {



"displayName": "TICKET-549E6AD75BD598EC",



"url": "https://example.com/TICKET-549E6AD75BD598EC"



}



}



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/remediationItems/trackingLinks
```

#### Request body

```
{



"updates": {



"PROCESS_GROUP-46C0E12D9B0EF2D9": {



"displayName": "TICKET-46C0E12D9B0EF2D9",



"url": "https://example.com/TICKET-46C0E12D9B0EF2D9"



},



"PROCESS_GROUP-549E6AD75BD598EC": {



"displayName": "TICKET-549E6AD75BD598EC",



"url": "https://example.com/TICKET-549E6AD75BD598EC"



}



}



}
```

#### Response code

200

### Удаление ссылок трекинга

Удалить ссылки трекинга с `"PROCESS_GROUP-46C0E12D9B0EF2D9"` и `"PROCESS_GROUP-549E6AD75BD598EC"`.

#### Curl

```
curl -X 'POST' 'https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/remediationItems/trackingLinks' \



-H 'accept: */*' \



-H 'Authorization: Api-Token [your_token]' \



-H 'Content-Type: application/json; charset=utf-8' \



-d '{



"deletes": ["PROCESS_GROUP-46C0E12D9B0EF2D9", "PROCESS_GROUP-549E6AD75BD598EC"]



}



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/remediationItems/trackingLinks
```

#### Request body

```
{



"deletes": ["PROCESS_GROUP-46C0E12D9B0EF2D9", "PROCESS_GROUP-549E6AD75BD598EC"]



}
```

#### Response code

200

## Связанные темы

* [Application Security](/managed/secure/application-security "Доступ к функциям Dynatrace Application Security.")
* [Remediation tracking](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Отслеживайте прогресс устранения уязвимостей.")