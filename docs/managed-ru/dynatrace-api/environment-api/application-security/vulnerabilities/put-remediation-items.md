---
title: Vulnerabilities API - PUT mute or unmute a remediation item
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/application-security/vulnerabilities/put-remediation-items
scraped: 2026-05-12T11:59:13.247352
---

# Vulnerabilities API - PUT mute or unmute a remediation item

# Vulnerabilities API - PUT mute or unmute a remediation item

* Reference
* Updated on May 03, 2022

Устанавливает статус заглушения process group [remediation tracking](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Отслеживайте прогресс устранения уязвимостей.") или, в случае Kubernetes-уязвимостей, remediation tracking Kubernetes-узла, в `mute` или `unmute`.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems/{remediationItemId}/muteState` |
| PUT | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems/{remediationItemId}/muteState` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `securityProblems.write`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID требуемой third-party security problem. | path | Обязательный |
| remediationItemId | string | ID remediation item. | path | Обязательный |
| body | [RemediationItemMuteStateChange](#openapi-definition-RemediationItemMuteStateChange) | JSON-тело запроса. Содержит информацию о состоянии заглушения, которое нужно применить. | body | Опциональный |

### Объекты тела запроса

#### Объект `RemediationItemMuteStateChange`

Обновлённая конфигурация состояния заглушения remediation item.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| comment | string | Комментарий о причине изменения состояния заглушения. | Обязательный |
| muted | boolean | Желаемое состояние заглушения remediation item. | Обязательный |
| reason | string | Причина изменения состояния заглушения. Элемент может принимать значения * `AFFECTED` * `CONFIGURATION_NOT_AFFECTED` * `FALSE_POSITIVE` * `IGNORE` * `INITIAL_STATE` * `OTHER` * `VULNERABLE_CODE_NOT_IN_USE` | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

```
{



"comment": "string",



"muted": true,



"reason": "IGNORE"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | - | Успех. Запрошенное состояние заглушения применено к remediation item. |
| **204** | - | Не выполнено. Remediation item ранее был переведён в запрошенное состояние заглушения тем же пользователем с той же причиной и комментарием. |
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

## Пример

Заглушить remediation item `PROCESS_GROUP-70DF2C1374244F5A` уязвимости `8788643471842202915` из [примера GET-запроса](/managed/dynatrace-api/environment-api/application-security/vulnerabilities/get-remediation-items#example "Просмотрите список remediation items уязвимости через Dynatrace API."). Код ответа **200** означает успешный запрос.

#### Curl

```
curl --request PUT \



--url https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/8788643471842202915/remediationItems/PROCESS_GROUP-70DF2C1374244F5A/muteState \



--header 'Authorization: Api-Token [your_token]' \



--header 'Content-Type: application/json' \



--data '{



"muted": true,



"reason": "OTHER",



"comment": "API test"



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/8788643471842202915/remediationItems/PROCESS_GROUP-70DF2C1374244F5A/muteState
```

#### Request body

```
{



"muted": true,



"reason": "OTHER",



"comment": "API test"



}
```

#### Response code

200

## Связанные темы

* [Application Security](/managed/secure/application-security "Доступ к функциям Dynatrace Application Security.")
* [Davis Security Advisor API](/managed/dynatrace-api/environment-api/application-security/davis-security-advice "Просмотрите рекомендации Davis Security Advisor через Dynatrace API.")
* [Remediation tracking](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Отслеживайте прогресс устранения уязвимостей.")