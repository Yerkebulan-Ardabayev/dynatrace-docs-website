---
title: Applications detection rules API - PUT a rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/put-rule
---

# Applications detection rules API - PUT a rule

# Applications detection rules API - PUT a rule

* Справка
* Опубликовано 30 августа 2019 г.

Обновляет указанное правило обнаружения приложений.

Если правило обнаружения приложений с указанным ID не существует, создаётся новое правило и добавляется в конец списка правил.

Если для существующего правила задан параметр order, запрос использует это значение. В противном случае сохраняется существующий порядок правил.

Запрос принимает и возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/{id}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/{id}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать токен, читай в разделе [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID правила обнаружения приложений, которое нужно обновить.  Если ID задан также в теле запроса, он должен совпадать с этим ID. | путь | Обязательный |
| body | [ApplicationDetectionRuleConfig](#openapi-definition-ApplicationDetectionRuleConfig) | Тело JSON запроса. Содержит обновлённые параметры правила обнаружения приложений.  Если задан параметр **order**, правило размещается в эту позицию. | тело | Необязательный |

### Объекты тела запроса

#### Объект `ApplicationDetectionRuleConfig`

Правило обнаружения приложений.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| applicationIdentifier | string | ID Dynatrace-сущности приложения, например `APPLICATION-4A3B43`.  Нужно использовать существующий ID. Если требуется создать правило для приложения, которого ещё не существует, [сначала создай приложение﻿](https://dt-url.net/vt03khh?dt=m), а затем настрой для него правила обнаружения. | Обязательный |
| filterConfig | [ApplicationFilter](#openapi-definition-ApplicationFilter) | Условие правила обнаружения приложений. | Обязательный |
| id | string | ID правила. | Необязательный |
| metadata | [ConfigurationMetadataDtoImpl](#openapi-definition-ConfigurationMetadataDtoImpl) | Метаданные, полезные для отладки. | Необязательный |
| name | string | Уникальное имя правила обнаружения приложений. | Необязательный |
| order | string | Порядок правила в списке правил.  Правила оцениваются сверху вниз. Применяется первое подходящее правило. | Необязательный |

#### Объект `ApplicationFilter`

Условие правила обнаружения приложений.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| applicationMatchTarget | string | Где искать значение **pattern**. Элемент может принимать следующие значения * `DOMAIN` * `URL` | Обязательный |
| applicationMatchType | string | Оператор сопоставления. Элемент может принимать следующие значения * `BEGINS_WITH` * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `MATCHES` | Обязательный |
| pattern | string | Значение для поиска. | Обязательный |

#### Объект `ConfigurationMetadataDtoImpl`

Метаданные, полезные для отладки.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Необязательный |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Необязательный |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Необязательный |

### Модель тела JSON запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать для использования в реальном запросе.

```
{



"applicationIdentifier": "APPLICATION-123456",



"filterConfig": {



"applicationMatchTarget": "DOMAIN",



"applicationMatchType": "EQUALS",



"pattern": "myapp.example.com"



},



"id": "12345678-abcd-1234-abcd-1234567890ab",



"metadata": {



"clusterVersion": "Mock version",



"configurationVersions": [



4,



2



]



},



"name": "uniqueName"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успешно. Правило обнаружения приложений создано. Ответ содержит ID нового правила. |
| **204** | - | Успешно. Правило обнаружения приложений обновлено. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Введённые данные недопустимы. |

### Объекты тела ответа

#### Объект `EntityShortRepresentation`

Краткое представление Dynatrace-сущности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание Dynatrace-сущности. |
| id | string | ID Dynatrace-сущности. |
| name | string | Имя Dynatrace-сущности. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код статуса HTTP |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Модели тела JSON ответа

```
{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



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

## Проверка данных

Рекомендуется проверять данные перед отправкой их в реальном запросе. Код ответа **204** означает, что данные корректны.

Запрос принимает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/{id}/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/{id}/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать токен, читай в разделе [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Проверено. Отправленная конфигурация корректна. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Введённые данные недопустимы. |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код статуса HTTP |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### Модели тела JSON ответа

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

В этом примере запрос обновляет правило распознавания приложения из [примера POST-запроса](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/post-rule#example "Create an application detection rule via the Dynatrace API."). Он меняет **order** правила на позицию **два** и меняет условие правила на **domain**, который **содержит** паттерн **booking.easyTravel**.

Токен API передаётся в заголовке **Authorization**.

Тело запроса усечено в разделе **Curl**. Полное тело смотри в разделе **Request body**. Пример тела запроса можно скачать или скопировать, чтобы попробовать самостоятельно. Нужно использовать ID приложения, доступный в своей среде.

#### Curl

```
curl -X PUT \



https://mySampleEnv.live.dynatrace.com/api/config/v1/applicationDetectionRules/9568a82b-73d8-4b18-be1a-4289433e2619 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{ <truncated - see the Request body section > }'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/applicationDetectionRules/9568a82b-73d8-4b18-be1a-4289433e2619
```

#### Request body

```
{



"id": "9568a82b-73d8-4b18-be1a-4289433e2619",



"applicationIdentifier": "APPLICATION-900C1E36674F607D",



"order": 2,



"filterConfig": {



"pattern": "booking.easyTravel",



"applicationMatchType": "BEGINS_WITH",



"applicationMatchTarget": "DOMAIN"



}



}
```

#### Response code

204

## Похожие темы

* [Real User Monitoring Classic](/managed/observe/digital-experience/rum-classic/rum-concepts/rum-overview "Learn about Real User Monitoring Classic, key performance metrics, mobile app monitoring, and more.")
* [Проверка правил распознавания приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/application-detection-rules "Easily understand the detection rules of your RUM application.")
* [Определение приложений для Real User Monitoring Classic](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder "Learn how to define your applications following the suggested, manual, or application detection rules approach.")