---
title: Vulnerabilities API - PUT mute or unmute a remediation item
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/application-security/vulnerabilities/put-remediation-items
scraped: 2026-03-05T21:38:03.339161
---

# Vulnerabilities API - PUT заглушить или снять заглушение элемента устранения

# Vulnerabilities API - PUT заглушить или снять заглушение элемента устранения

* Reference
* Updated on May 03, 2022

Установка состояния заглушения для группы процессов [отслеживания устранения](../../../../secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking.md "Отслеживание хода устранения уязвимостей.") или, в случае уязвимостей Kubernetes, для узла Kubernetes отслеживания устранения, в значение `mute` (заглушить) или `unmute` (снять заглушение).

Запрос принимает полезную нагрузку в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/securityProblems/{id}/remediationItems/{remediationItemId}/muteState` |
| PUT | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems/{remediationItemId}/muteState` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью `securityProblems.write`.

Чтобы узнать, как получить и использовать его, см. [Токены и аутентификация](../../../../discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication.md).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | Идентификатор запрашиваемой проблемы безопасности сторонних компонентов. | path | Обязательный |
| remediationItemId | string | Идентификатор элемента устранения. | path | Обязательный |
| body | [RemediationItemMuteStateChange](#openapi-definition-RemediationItemMuteStateChange) | JSON-тело запроса. Содержит информацию о состоянии заглушения, которую необходимо применить. | body | Необязательный |

### Объекты тела запроса

#### Объект `RemediationItemMuteStateChange`

Обновлённая конфигурация состояния заглушения элемента устранения.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| comment | string | Комментарий о причине изменения состояния заглушения. | Обязательный |
| muted | boolean | Желаемое состояние заглушения элемента устранения. | Обязательный |
| reason | string | Причина изменения состояния заглушения. Элемент может содержать следующие значения: * `AFFECTED` * `CONFIGURATION_NOT_AFFECTED` * `FALSE_POSITIVE` * `IGNORE` * `INITIAL_STATE` * `OTHER` * `VULNERABLE_CODE_NOT_IN_USE` | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Она должна быть скорректирована для использования в реальном запросе.

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
| **200** | - | Успех. Запрошенное состояние заглушения было применено к элементу устранения. |
| **204** | - | Не выполнено. Элемент устранения ранее был переведён в запрошенное состояние заглушения тем же пользователем с той же причиной и комментарием. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

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

Заглушить элемент устранения `PROCESS_GROUP-70DF2C1374244F5A` для уязвимости `8788643471842202915` из [примера GET-запроса](get-remediation-items.md#example "Просмотр списка элементов устранения уязвимости через Dynatrace API."). Код ответа **200** указывает на успешный запрос.

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

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/8788643471842202915/remediationItems/PROCESS_GROUP-70DF2C1374244F5A/muteState
```

#### Тело запроса

```
{



"muted": true,



"reason": "OTHER",



"comment": "API test"



}
```

#### Код ответа

200

## Связанные темы

* [Application Security](../../../../secure/application-security.md "Доступ к функциям Dynatrace Application Security.")
* [Davis Security Advisor API](../davis-security-advice.md "Просмотр рекомендаций Davis Security Advisor через Dynatrace API.")
* [Отслеживание устранения](../../../../secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking.md "Отслеживание хода устранения уязвимостей.")
