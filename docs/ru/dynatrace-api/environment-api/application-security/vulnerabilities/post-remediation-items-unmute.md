---
title: Уязвимости API - POST снятие ограничений с элементов исправления
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/application-security/vulnerabilities/post-remediation-items-unmute
scraped: 2026-03-06T21:35:54.405045
---

Снимает ограничения с нескольких групп процессов отслеживания исправления или, в случае уязвимостей Kubernetes, нескольких узлов отслеживания исправления Kubernetes.

Запрос использует полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/securityProblems/{id}/remediationItems/unmute` |
| POST | Environment ActiveGateКластер ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems/unmute` |

## Аутентификация

Чтобы выполнить этот запрос, вам нужен токен доступа с областью `securityProblems.write`.

Чтобы узнать, как получить и использовать его, см. [Токены и аутентификация](../../../../discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication.md).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| id | строка | Идентификатор запрошенной проблемы безопасности третьих сторон. | путь | Обязательный |
| body | [RemediationItemsBulkUnmute](#openapi-definition-RemediationItemsBulkUnmute) | JSON тело запроса. Содержит информацию о снятии ограничений. | тело | Необязательный |

### Объекты тела запроса

#### Объект `RemediationItemsBulkUnmute`

Информация о снятии ограничений с нескольких элементов исправления.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| comment | строка | Комментарий о причине снятия ограничений. | Необязательный |
| reason | строка | Причина снятия ограничений с элементов исправления. Элемент может содержать следующие значения * `AFFECTED` | Обязательный |
| remediationItemIds | строковый массив | Идентификаторы элементов исправления, которые необходимо снять с ограничений. | Обязательный |

### Модель тела запроса JSON

Это модель тела запроса, показывающая возможные элементы. Ее необходимо скорректировать для использования в фактическом запросе.

```
{


"comment": "строка",


"reason": "AFFECTED",


"remediationItemIds": [


"строка"


]


}
```

## Ответ

### Код ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [RemediationItemsBulkUnmuteResponse](#openapi-definition-RemediationItemsBulkUnmuteResponse) | Успех. Элемент(ы) исправления сняты с ограничений. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `RemediationItemsBulkUnmuteResponse`

Ответ на снятие ограничений с нескольких элементов исправления.

| Элемент | Тип | Описание |
| --- | --- | --- |
| summary | [RemediationItemMutingSummary[]](#openapi-definition-RemediationItemMutingSummary) | Сводка того, какие элементы исправления были сняты с ограничений и какие ранее уже были сняты с ограничений. |

#### Объект `RemediationItemMutingSummary`

Сводка снятия ограничений с элемента исправления.

| Элемент | Тип | Описание |
| --- | --- | --- |
| muteStateChangeTriggered | логический | Было ли событие смены состояния ограничения для данного элемента исправления вызвано этим запросом. |
| reason | строка | Содержит причину, если запрошенная операция не была выполнена. Элемент может содержать следующие значения * `ALREADY_MUTED` * `ALREADY_UNMUTED` * `REMEDIATION_ITEM_NOT_AFFECTED_BY_GIVEN_SECURITY_PROBLEM` |
| remediationItemId | строка | Идентификатор элемента исправления, который будет снят с ограничений. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | целое число | Код состояния HTTP |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | строка | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | строка | - |
| message | строка | - |
| parameterLocation | строка | -Элемент может содержать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | строка | - |

### Модели тела ответа JSON

```
{


"summary": [


{


"muteStateChangeTriggered": true,


"reason": "ALREADY_MUTED",


"remediationItemId": "строка"


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


"location": "строка",


"message": "строка",


"parameterLocation": "HEADER",


"path": "строка"


?


],


"message": "строка"


?


}


}
```

## Пример

Снять ограничения с двух сущностей, `PROCESS_GROUP-46C0E12D9B0EF2D9` и `PROCESS_GROUP-549E6AD75BD598EC`.

#### Curl

```
curl -X 'POST' 'https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/remediationItems/unmute' \
\
-H 'accept: application/json; charset=utf-8' \
\
-H 'Authorization: Api-Token [your_token]' \
\
-H 'Content-Type: application/json; charset=utf-8' \
\
-d '{


"comment": "Пример снятия ограничений с нескольких элементов",


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


"comment": "Пример снятия ограничений с нескольких элементов",


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


?),


{


"remediationItemId": "PROCESS_GROUP-549E6AD75BD598EC",


"muteStateChangeTriggered": true


?


?


]


}
```

## Связанные темы

* [Безопасность приложений](../../../../secure/application-security.md "Доступ к функциям безопасности приложений Dynatrace.")
* [Советник по безопасности Davis API](../davis-security-advice.md "Просмотр рекомендаций советника по безопасности Davis через Dynatrace API. ")
* [Отслеживание исправления](../../../../secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking.md "Отслеживание прогресса исправления уязвимостей.")