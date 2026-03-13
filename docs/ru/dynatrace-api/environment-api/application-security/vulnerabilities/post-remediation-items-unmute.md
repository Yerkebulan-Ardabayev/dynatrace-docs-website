---
title: Vulnerabilities API - POST unmute remediation items
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/application-security/vulnerabilities/post-remediation-items-unmute
scraped: 2026-03-06T21:35:54.405045
---

# Vulnerabilities API — POST снятие отключения элементов устранения

# Vulnerabilities API — POST снятие отключения элементов устранения

* Справочник
* Обновлено 25 сент. 2024

Снимает отключение (unmute) для нескольких групп процессов [отслеживания устранения](../../../../secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking.md "Отслеживание прогресса устранения уязвимостей.") или, в случае уязвимостей Kubernetes, для нескольких узлов Kubernetes отслеживания устранения.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/securityProblems/{id}/remediationItems/unmute` |
| POST | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems/unmute` |

## Аутентификация

Для выполнения этого запроса вам необходим токен доступа с областью `securityProblems.write`.

Чтобы узнать, как получить и использовать его, см. [Токены и аутентификация](../../../../discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication.md).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | Идентификатор запрашиваемой сторонней проблемы безопасности. | path | Обязательный |
| body | [RemediationItemsBulkUnmute](#openapi-definition-RemediationItemsBulkUnmute) | JSON-тело запроса. Содержит информацию о снятии отключения. | body | Необязательный |

### Объекты тела запроса

#### Объект `RemediationItemsBulkUnmute`

Информация о снятии отключения для нескольких элементов устранения.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| comment | string | Комментарий о причине снятия отключения. | Необязательный |
| reason | string | Причина снятия отключения элементов устранения. Элемент может содержать следующие значения: * `AFFECTED` | Обязательный |
| remediationItemIds | string[] | Идентификаторы элементов устранения, для которых снимается отключение. | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её необходимо адаптировать для использования в реальном запросе.

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
| **200** | [RemediationItemsBulkUnmuteResponse](#openapi-definition-RemediationItemsBulkUnmuteResponse) | Успех. Отключение элемента(ов) устранения снято. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `RemediationItemsBulkUnmuteResponse`

Ответ на снятие отключения нескольких элементов устранения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| summary | [RemediationItemMutingSummary[]](#openapi-definition-RemediationItemMutingSummary) | Сводка о том, для каких элементов устранения было снято отключение, а для каких оно уже было снято ранее. |

#### Объект `RemediationItemMutingSummary`

Сводка по отключению/снятию отключения элемента устранения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| muteStateChangeTriggered | boolean | Было ли изменение состояния отключения для данного элемента устранения инициировано этим запросом. |
| reason | string | Содержит причину, если запрошенная операция не была выполнена. Элемент может содержать следующие значения: * `ALREADY_MUTED` * `ALREADY_UNMUTED` * `REMEDIATION_ITEM_NOT_AFFECTED_BY_GIVEN_SECURITY_PROBLEM` |
| remediationItemId | string | Идентификатор элемента устранения, для которого будет выполнено отключение/снятие отключения. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код состояния HTTP |
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

Снятие отключения для двух сущностей: `PROCESS_GROUP-46C0E12D9B0EF2D9` и `PROCESS_GROUP-549E6AD75BD598EC`.

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

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/remediationItems/unmute
```

#### Тело запроса

```
{



"comment": "Example unmute multiple",



"reason": "AFFECTED",



"remediationItemIds": ["PROCESS_GROUP-46C0E12D9B0EF2D9", "PROCESS_GROUP-549E6AD75BD598EC"]



}
```

#### Тело ответа

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

* [Application Security](../../../../secure/application-security.md "Доступ к функциям Application Security Dynatrace.")
* [Davis Security Advisor API](../davis-security-advice.md "Просмотр рекомендаций Davis Security Advisor через Dynatrace API.")
* [Отслеживание устранения](../../../../secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking.md "Отслеживание прогресса устранения уязвимостей.")
