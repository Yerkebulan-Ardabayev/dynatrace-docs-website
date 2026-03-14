---
title: Уязвимости API - POST отключение элементов исправления
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/application-security/vulnerabilities/post-remediation-items-mute
scraped: 2026-03-05T21:35:36.655664
---

# API уязвимостей - POST отключение элементов исправления

# API уязвимостей - POST отключение элементов исправления

* Справочник
* Обновлено 25 сентября 2024 г.

Отключает несколько групп процессов [отслеживания исправлений](../../../../secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking.md "Отслеживание прогресса исправления уязвимостей.") или, в случае уязвимостей Kubernetes, несколько узлов Kubernetes для отслеживания исправлений.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/securityProblems/{id}/remediationItems/mute` |
| POST | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems/mute` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью действия `securityProblems.write`.

Чтобы узнать, как получить и использовать его, см. [Токены и аутентификация](../../../../discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication.md).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательность |
| --- | --- | --- | --- | --- |
| id | string | Идентификатор запрашиваемой проблемы безопасности стороннего ПО. | path | Обязательный |
| body | [RemediationItemsBulkMute](#openapi-definition-RemediationItemsBulkMute) | JSON-тело запроса. Содержит информацию об отключении. | body | Необязательный |

### Объекты тела запроса

#### Объект `RemediationItemsBulkMute`

Информация об отключении нескольких элементов исправления.

| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| comment | string | Комментарий о причине отключения. | Необязательный |
| reason | string | Причина отключения элементов исправления. Элемент может содержать следующие значения: * `CONFIGURATION_NOT_AFFECTED` * `FALSE_POSITIVE` * `IGNORE` * `OTHER` * `VULNERABLE_CODE_NOT_IN_USE` | Обязательный |
| remediationItemIds | string[] | Идентификаторы элементов исправления, которые необходимо отключить. | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её необходимо адаптировать для использования в реальном запросе.

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
| **200** | [RemediationItemsBulkMuteResponse](#openapi-definition-RemediationItemsBulkMuteResponse) | Успешно. Элемент(ы) исправления были отключены. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `RemediationItemsBulkMuteResponse`

Ответ на отключение нескольких элементов исправления.

| Элемент | Тип | Описание |
| --- | --- | --- |
| summary | [RemediationItemMutingSummary[]](#openapi-definition-RemediationItemMutingSummary) | Сводка о том, какие элементы исправления были отключены, а какие уже были отключены ранее. |

#### Объект `RemediationItemMutingSummary`

Сводка по включению/отключению элемента исправления.

| Элемент | Тип | Описание |
| --- | --- | --- |
| muteStateChangeTriggered | boolean | Было ли изменение состояния отключения для данного элемента исправления инициировано этим запросом. |
| reason | string | Содержит причину, если запрошенная операция не была выполнена. Элемент может содержать следующие значения: * `ALREADY_MUTED` * `ALREADY_UNMUTED` * `REMEDIATION_ITEM_NOT_AFFECTED_BY_GIVEN_SECURITY_PROBLEM` |
| remediationItemId | string | Идентификатор элемента исправления, который будет включён/отключён. |

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

Отключить два элемента исправления, `PROCESS_GROUP-46C0E12D9B0EF2D9` и `PROCESS_GROUP-549E6AD75BD598EC`, так как конфигурация не затронута.

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

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/remediationItems/mute
```

#### Тело запроса

```
{



"comment": "Example muting multiple entities",



"reason": "CONFIGURATION_NOT_AFFECTED",



"remediationItemIds": ["PROCESS_GROUP-46C0E12D9B0EF2D9", "PROCESS_GROUP-549E6AD75BD598EC"]



}
```

#### Тело ответа

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

Если запрос выполнен успешно, для каждой сущности будет указано значение `muteStateChangeTriggered`.

## Связанные темы

* [Application Security](../../../../secure/application-security.md "Доступ к функциям Dynatrace Application Security.")
* [Davis Security Advisor API](../davis-security-advice.md "Просмотр рекомендаций Davis Security Advisor через Dynatrace API.")
* [Отслеживание исправлений](../../../../secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking.md "Отслеживание прогресса исправления уязвимостей.")
