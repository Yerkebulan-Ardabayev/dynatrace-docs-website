---
title: Vulnarabilities API - POST mute remediation items
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/application-security/vulnerabilities/post-remediation-items-mute
scraped: 2026-05-12T11:59:09.277908
---

# Vulnarabilities API - POST mute remediation items

# Vulnarabilities API - POST mute remediation items

* Reference
* Updated on Sep 25, 2024

Заглушает несколько process groups [remediation tracking](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Отслеживайте прогресс устранения уязвимостей.") или, в случае Kubernetes-уязвимостей, несколько remediation tracking Kubernetes-узлов.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems/mute` |
| POST | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems/mute` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `securityProblems.write`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID требуемой third-party security problem. | path | Обязательный |
| body | [RemediationItemsBulkMute](#openapi-definition-RemediationItemsBulkMute) | JSON-тело запроса. Содержит информацию о заглушении. | body | Опциональный |

### Объекты тела запроса

#### Объект `RemediationItemsBulkMute`

Информация о заглушении нескольких remediation items.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| comment | string | Комментарий о причине заглушения. | Опциональный |
| reason | string | Причина заглушения remediation items. Элемент может принимать значения * `CONFIGURATION_NOT_AFFECTED` * `FALSE_POSITIVE` * `IGNORE` * `OTHER` * `VULNERABLE_CODE_NOT_IN_USE` | Обязательный |
| remediationItemIds | string[] | ID remediation items для заглушения. | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

```
{



"comment": "string",



"reason": "CONFIGURATION_NOT_AFFECTED",



"remediationItemIds": [



"string"



]



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [RemediationItemsBulkMuteResponse](#openapi-definition-RemediationItemsBulkMuteResponse) | Успех. Remediation item(s) заглушены. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

#### Объект `RemediationItemsBulkMuteResponse`

Ответ заглушения нескольких remediation items.

| Элемент | Тип | Описание |
| --- | --- | --- |
| summary | [RemediationItemMutingSummary[]](#openapi-definition-RemediationItemMutingSummary) | Сводка о том, какие remediation items были заглушены и какие уже были заглушены ранее. |

#### Объект `RemediationItemMutingSummary`

Сводка (снятия) заглушения remediation item.

| Элемент | Тип | Описание |
| --- | --- | --- |
| muteStateChangeTriggered | boolean | Было ли изменение состояния заглушения для данного remediation item инициировано этим запросом. |
| reason | string | Содержит причину, если запрошенная операция не была выполнена. Элемент может принимать значения * `ALREADY_MUTED` * `ALREADY_UNMUTED` * `REMEDIATION_ITEM_NOT_AFFECTED_BY_GIVEN_SECURITY_PROBLEM` |
| remediationItemId | string | ID remediation item, для которого будет применено (снятие) заглушения. |

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



"summary": [



{



"muteStateChangeTriggered": true,



"reason": "ALREADY_MUTED",



"remediationItemId": "string"



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

Заглушить два remediation items, `PROCESS_GROUP-46C0E12D9B0EF2D9` и `PROCESS_GROUP-549E6AD75BD598EC`, поскольку конфигурация не затронута.

#### Curl

```
curl -X 'POST' 'https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/remediationItems/mute' \



-H 'accept: application/json; charset=utf-8' \



-H 'Authorization: Api-Token [your_token]' \



-H 'Content-Type: application/json; charset=utf-8' \



-d '{



"comment": "Example muting multiple entities",



"reason": "CONFIGURATION_NOT_AFFECTED",



"remediationItemIds": ["PROCESS_GROUP-46C0E12D9B0EF2D9", "PROCESS_GROUP-549E6AD75BD598EC"]



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/remediationItems/mute
```

#### Request body

```
{



"comment": "Example muting multiple entities",



"reason": "CONFIGURATION_NOT_AFFECTED",



"remediationItemIds": ["PROCESS_GROUP-46C0E12D9B0EF2D9", "PROCESS_GROUP-549E6AD75BD598EC"]



}
```

#### Response body

```
{



"summary": [



{



"remediationItemId": "PROCESS_GROUP-549E6AD75BD598EC",



"muteStateChangeTriggered": true



},



{



"remediationItemId": "PROCESS_GROUP-46C0E12D9B0EF2D9",



"muteStateChangeTriggered": true



}



]



}
```

Если запрос успешен, вы увидите `muteStateChangeTriggered` для каждой сущности.

## Связанные темы

* [Application Security](/managed/secure/application-security "Доступ к функциям Dynatrace Application Security.")
* [Davis Security Advisor API](/managed/dynatrace-api/environment-api/application-security/davis-security-advice "Просмотрите рекомендации Davis Security Advisor через Dynatrace API.")
* [Remediation tracking](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Отслеживайте прогресс устранения уязвимостей.")