---
title: Vulnerabilities API - POST remediation item tracking links
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/application-security/vulnerabilities/post-remediation-item-tracking-link
scraped: 2026-03-02T21:24:04.456847
---

# Vulnerabilities API - POST ссылки отслеживания элементов исправления


Добавляет, редактирует или удаляет ссылки отслеживания групп процессов отслеживания исправлений для уязвимости сторонних компонентов (или, в случае уязвимостей Kubernetes, узлов Kubernetes для отслеживания исправлений).

Запрос создаёт полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | Managed | `https://{your-environment-id}.live.dynatrace.com/api/v2/securityProblems/{id}/remediationItems/trackingLinks` |
| POST | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems/trackingLinks` |

## Аутентификация

Для выполнения этого запроса вам необходим токен доступа с областью действия `securityProblems.write`.

Чтобы узнать, как получить и использовать его, см. Токены и аутентификация.

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | Идентификатор запрашиваемой проблемы безопасности сторонних компонентов. | path | Обязательный |
| body | [RemediationItemsBulkUpdateDeleteDto](#openapi-definition-RemediationItemsBulkUpdateDeleteDto) | Содержит ассоциации внешних ссылок отслеживания для установки или удаления в элементах исправления проблемы безопасности.  * Ссылки для установки следует отправлять в объекте `updates`. * Ссылки для удаления следует отправлять в массиве `deletes`.  Запрос должен содержать хотя бы одну запись для установки или удаления, чтобы быть действительным.  Конфликтующие изменения для одного и того же элемента исправления (идентификатор присутствует как в `deletes`, так и в `updates`) не допускаются.  Обратите внимание, что все обновления ссылок отслеживания для проблемы безопасности должны быть отправлены в одном запросе. | body | Необязательный |

### Объекты тела запроса

#### Объект `RemediationItemsBulkUpdateDeleteDto`

Содержит ассоциации внешних ссылок отслеживания, которые будут применены к элементам исправления проблемы безопасности.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| deletes | string[] | Ссылки отслеживания для удаления из проблемы безопасности.  Список идентификаторов элементов исправления проблемы безопасности, для которых необходимо удалить ссылки отслеживания. | Необязательный |
| updates | object | Ссылки отслеживания для установки в проблеме безопасности.  Сопоставление идентификатора элемента исправления с объектами ссылок отслеживания.  Ключи должны быть действительными идентификаторами элементов исправления проблемы безопасности, а связанное значение должно содержать ссылку для установки. | Необязательный |

#### Объект `TrackingLinkUpdate`

Ассоциация URL внешней ссылки отслеживания, устанавливаемая для исправляемой сущности проблемы безопасности.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| displayName | string | Желаемое отображаемое имя (заголовок) ссылки отслеживания, установленной для элемента исправления, например 'ISSUE-123'. | Обязательный |
| url | string | Желаемый URL ссылки отслеживания, установленный для элемента исправления, например https://example.com/ISSUE-123  Обратите внимание, что поддерживаются только действительные URL-адреса с протоколами 'http' или 'https'. | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её необходимо адаптировать для использования в реальном запросе.

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
| **204** | - | Успех. Запрошенные ссылки отслеживания были обновлены. |
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

### Установка ссылок отслеживания

Предпосылка: существует автоматизация, которая автоматически создаёт тикет для каждой исправляемой сущности.

Цель: заставить конечную точку связать тикет с элементом исправления. Будут установлены следующие ссылки отслеживания:

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

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/remediationItems/trackingLinks
```

#### Тело запроса

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

#### Код ответа

200

### Удаление ссылок отслеживания

Удаление ссылок отслеживания из `"PROCESS_GROUP-46C0E12D9B0EF2D9"` и `"PROCESS_GROUP-549E6AD75BD598EC"`.

#### Curl

```
curl -X 'POST' 'https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/remediationItems/trackingLinks' \


-H 'accept: */*' \


-H 'Authorization: Api-Token [your_token]' \


-H 'Content-Type: application/json; charset=utf-8' \


-d '{


"deletes": ["PROCESS_GROUP-46C0E12D9B0EF2D9", "PROCESS_GROUP-549E6AD75BD598EC"]


}


'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/remediationItems/trackingLinks
```

#### Тело запроса

```
{


"deletes": ["PROCESS_GROUP-46C0E12D9B0EF2D9", "PROCESS_GROUP-549E6AD75BD598EC"]


}
```

#### Код ответа

200

## Связанные темы

* Application Security
* Отслеживание исправлений
