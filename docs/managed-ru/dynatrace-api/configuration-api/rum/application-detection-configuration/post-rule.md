---
title: Applications detection rules API - POST a rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/post-rule
---

# Applications detection rules API - POST a rule

# Applications detection rules API - POST a rule

* Справка
* Опубликовано 30 августа 2019 г.

Создаёт новое правило обнаружения приложения и добавляет его в конец списка правил. Чтобы задать определённый порядок, используй запрос [PUT reorder rules](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/reorder-rules "Reorder application detection rules via the Dynatrace API.").

Правила обнаружения можно создавать только для уже существующего приложения. Если нужно создать правило для приложения, которого ещё нет, [сначала создай приложение](/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/post-web-application "Create a web application via the Dynatrace API.") и только потом настраивай для него правила обнаружения.

Запрос принимает и возвращает содержимое в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать токен, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

В теле запроса нельзя указывать ID. ID присваивается автоматически со стороны Dynatrace.

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| position | string | Позиция нового правила:  * `APPEND`: в конец списка правил. * `PREPEND`: в начало списка правил.  Если не задано, используется `APPEND`. Элемент может принимать значения * `APPEND` * `PREPEND` | query | Необязательный |
| body | [ApplicationDetectionRuleConfig](#openapi-definition-ApplicationDetectionRuleConfig) | Тело JSON запроса. Содержит конфигурацию нового правила обнаружения приложения.  ID правила указывать нельзя.  Поле **order** в этом запросе игнорируется. Чтобы задать определённый порядок, используй запрос `PUT /applicationDetectionRules/order`. | body | Необязательный |

### Объекты тела запроса

#### Объект `ApplicationDetectionRuleConfig`

Правило обнаружения приложения.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| applicationIdentifier | string | ID сущности Dynatrace для приложения, например `APPLICATION-4A3B43`.  Нужно использовать уже существующий ID. Если нужно создать правило для приложения, которого ещё нет, [сначала создай приложение﻿](https://dt-url.net/vt03khh?dt=m) и только потом настраивай для него правила обнаружения. | Обязательный |
| filterConfig | [ApplicationFilter](#openapi-definition-ApplicationFilter) | Условие правила обнаружения приложения. | Обязательный |
| id | string | ID правила. | Необязательный |
| metadata | [ConfigurationMetadataDtoImpl](#openapi-definition-ConfigurationMetadataDtoImpl) | Метаданные, полезные при отладке. | Необязательный |
| name | string | Уникальное имя правила обнаружения приложения. | Необязательный |
| order | string | Порядок правила в списке правил.  Правила проверяются сверху вниз. Применяется первое подходящее правило. | Необязательный |

#### Объект `ApplicationFilter`

Условие правила обнаружения приложения.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| applicationMatchTarget | string | Где искать значение **pattern**. Элемент может принимать значения * `DOMAIN` * `URL` | Обязательный |
| applicationMatchType | string | Оператор сопоставления. Элемент может принимать значения * `BEGINS_WITH` * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `MATCHES` | Обязательный |
| pattern | string | Значение для поиска. | Обязательный |

#### Объект `ConfigurationMetadataDtoImpl`

Метаданные, полезные при отладке.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Необязательный |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Необязательный |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Необязательный |

### Модель JSON тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

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

### Коды ответов

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Правило обнаружения приложения создано. Ответ содержит ID нового правила. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Некорректные входные данные. |

### Объекты тела ответа

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Модели JSON тела ответа

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

## Валидация содержимого

Рекомендуется проверять содержимое перед отправкой в составе реального запроса. Код ответа **204** означает, что содержимое валидно.

Запрос принимает содержимое в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать токен, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответов

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Проверено. Отправленная конфигурация валидна. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Некорректные входные данные. |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### Модели JSON тела ответа

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

В этом примере запрос создаёт новое правило обнаружения приложения для приложения **BookingApp** с ID **APPLICATION-900C1E36674F607D**.

Токен API передаётся в заголовке **Authorization**.

Тело запроса усечено в разделе **Curl**. Полное тело смотри в разделе **Request body**. Пример тела запроса можно скачать или скопировать, чтобы опробовать самостоятельно. Обязательно используй ID приложения, доступный в своей среде.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/config/v1/applicationDetectionRules \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{ <truncated - see the Request body section > }'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/applicationDetectionRules
```

#### Request body

```
{



"applicationIdentifier": "APPLICATION-900C1E36674F607D",



"filterConfig": {



"pattern": "booking",



"applicationMatchType": "CONTAINS",



"applicationMatchTarget": "URL"



}



}
```

#### Response body

```
{



"id": "9568a82b-73d8-4b18-be1a-4289433e2619",



"name": "BookingApp"



}
```

#### Response code

201

#### Result

Новое правило обнаружения приложения выглядит в UI так:

![POST example](https://dt-cdn.net/images/post-result-823-d70be0ef15.png)

POST example

## Похожие темы

* [Real User Monitoring Classic](/managed/observe/digital-experience/rum-classic/rum-concepts/rum-overview "Узнай про Real User Monitoring Classic, ключевые метрики производительности, мониторинг мобильных приложений и многое другое.")
* [Проверка правил обнаружения приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/application-detection-rules "Легко разберись в правилах обнаружения своего RUM-приложения.")
* [Определение приложений для Real User Monitoring Classic](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder "Узнай, как определять приложения по предложенному, ручному подходу или подходу с правилами обнаружения приложений.")