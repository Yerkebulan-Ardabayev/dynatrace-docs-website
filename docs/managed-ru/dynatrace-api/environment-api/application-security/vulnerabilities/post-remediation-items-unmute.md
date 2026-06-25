---
title: Vulnerabilities API - POST unmute remediation items
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/application-security/vulnerabilities/post-remediation-items-unmute
scraped: 2026-05-12T11:58:44.553079
---

# Vulnerabilities API - POST unmute remediation items

# Vulnerabilities API - POST unmute remediation items

* Reference
* Updated on Sep 25, 2024

Снимает заглушение нескольких process groups [remediation tracking](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Отслеживайте прогресс устранения уязвимостей.") или, в случае Kubernetes-уязвимостей, нескольких remediation tracking Kubernetes-узлов.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems/unmute` |
| POST | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems/unmute` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `securityProblems.write`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID требуемой third-party security problem. | path | Обязательный |
| body | [RemediationItemsBulkUnmute](#openapi-definition-RemediationItemsBulkUnmute) | JSON-тело запроса. Содержит информацию о снятии заглушения. | body | Опциональный |

### Объекты тела запроса

#### Объект `RemediationItemsBulkUnmute`

Информация о снятии заглушения нескольких remediation items.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| comment | string | Комментарий о причине снятия заглушения. | Опциональный |
| reason | string | Причина снятия заглушения remediation items. Элемент может принимать значения * `AFFECTED` | Обязательный |
| remediationItemIds | string[] | ID remediation items для снятия заглушения. | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

```
{



"comment": "string",



"reason": "AFFECTED",



"remediationItemIds": [



"string"



]



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [RemediationItemsBulkUnmuteResponse](#openapi-definition-RemediationItemsBulkUnmuteResponse) | Успех. Заглушение remediation item(s) снято. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

#### Объект `RemediationItemsBulkUnmuteResponse`

Ответ снятия заглушения нескольких remediation items.

| Элемент | Тип | Описание |
| --- | --- | --- |
| summary | [RemediationItemMutingSummary[]](#openapi-definition-RemediationItemMutingSummary) | Сводка о том, для каких remediation items было снято заглушение и для каких заглушение уже было снято ранее. |

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

Снять заглушение двух сущностей, `PROCESS_GROUP-46C0E12D9B0EF2D9` и `PROCESS_GROUP-549E6AD75BD598EC`.

#### Curl

```
curl -X 'POST' 'https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/remediationItems/unmute' \



-H 'accept: application/json; charset=utf-8' \



-H 'Authorization: Api-Token [your_token]' \



-H 'Content-Type: application/json; charset=utf-8' \



-d '{



"comment": "Example unmute multiple",



"reason": "AFFECTED",



"remediationItemIds": ["PROCESS_GROUP-46C0E12D9B0EF2D9", "PROCESS_GROUP-549E6AD75BD598EC"]



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/remediationItems/unmute
```

#### Request body

```
{



"comment": "Example unmute multiple",



"reason": "AFFECTED",



"remediationItemIds": ["PROCESS_GROUP-46C0E12D9B0EF2D9", "PROCESS_GROUP-549E6AD75BD598EC"]



}
```

#### Response body

```
{



"summary": [



{



"remediationItemId": "PROCESS_GROUP-46C0E12D9B0EF2D9",



"muteStateChangeTriggered": true



},



{



"remediationItemId": "PROCESS_GROUP-549E6AD75BD598EC",



"muteStateChangeTriggered": true



}



]



}
```

## Связанные темы

* [Application Security](/managed/secure/application-security "Доступ к функциям Dynatrace Application Security.")
* [Davis Security Advisor API](/managed/dynatrace-api/environment-api/application-security/davis-security-advice "Просмотрите рекомендации Davis Security Advisor через Dynatrace API.")
* [Remediation tracking](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Отслеживайте прогресс устранения уязвимостей.")