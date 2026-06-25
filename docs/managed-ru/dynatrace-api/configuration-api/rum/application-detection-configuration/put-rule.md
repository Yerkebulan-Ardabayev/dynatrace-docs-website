---
title: Applications detection rules API - PUT a rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/put-rule
scraped: 2026-05-12T11:16:00.038945
---

# Applications detection rules API - PUT a rule

# Applications detection rules API - PUT a rule

* Reference
* Published Aug 30, 2019

Обновляет указанное правило обнаружения приложений.

Если правило обнаружения приложений с указанным ID не существует, создаётся новое правило и добавляется в конец списка правил.

Если для существующего правила задан параметр order, запрос использует это значение. Иначе сохраняется текущий порядок правил.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/{id}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID обновляемого правила обнаружения приложений.  Если ID указан также в теле, он должен совпадать с этим ID. | path | Required |
| body | [ApplicationDetectionRuleConfig](#openapi-definition-ApplicationDetectionRuleConfig) | JSON-тело запроса. Содержит обновлённые параметры правила обнаружения приложений.  Если задан параметр **order**, правило помещается на эту позицию. | body | Optional |

### Объекты тела запроса

#### Объект `ApplicationDetectionRuleConfig`

Правило обнаружения приложений.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| applicationIdentifier | string | ID сущности Dynatrace для приложения, например `APPLICATION-4A3B43`.  Нужно использовать существующий ID. Если нужно создать правило для ещё не существующего приложения, [сначала создайте приложение](https://dt-url.net/vt03khh), а затем настройте для него правила обнаружения. | Required |
| filterConfig | [ApplicationFilter](#openapi-definition-ApplicationFilter) | Условие правила обнаружения приложений. | Required |
| id | string | ID правила. | Optional |
| metadata | [ConfigurationMetadataDtoImpl](#openapi-definition-ConfigurationMetadataDtoImpl) | Метаданные для отладки. | Optional |
| name | string | Уникальное имя правила обнаружения приложений. | Optional |
| order | string | Порядок правила в списке правил.  Правила оцениваются сверху вниз. Применяется первое подходящее правило. | Optional |

#### Объект `ApplicationFilter`

Условие правила обнаружения приложений.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| applicationMatchTarget | string | Где искать значение **pattern**. Возможные значения: * `DOMAIN` * `URL` | Required |
| applicationMatchType | string | Оператор сопоставления. Возможные значения: * `BEGINS_WITH` * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `MATCHES` | Required |
| pattern | string | Значение для поиска. | Required |

#### Объект `ConfigurationMetadataDtoImpl`

Метаданные для отладки.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Optional |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Optional |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Optional |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

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
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Правило обнаружения приложений создано. Ответ содержит ID нового правила. |
| **204** | - | Успех. Правило обнаружения приложений обновлено. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

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
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

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

## Validate payload

Рекомендуется проверить payload перед его отправкой в реальном запросе. Код ответа **204** означает, что payload корректен.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/{id}/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/{id}/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Validated. Переданная конфигурация валидна. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### JSON-модели тела ответа

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

В этом примере запрос обновляет правило обнаружения приложений из примера [POST request](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/post-rule#example "Создание правила обнаружения приложений через Dynatrace API."). Он меняет **order** правила на позицию **two** и меняет условие правила на **domain**, который **contains** шаблон **booking.easyTravel**.

API-токен передаётся в заголовке **Authorization**.

Тело запроса усечено в разделе **Curl**. Полное тело смотрите в разделе **Request body**. Вы можете скачать или скопировать пример тела запроса, чтобы попробовать его самостоятельно. Обязательно используйте ID приложения, доступного в вашем окружении.

#### Curl

```
curl -X PUT \



https://mySampleEnv.live.dynatrace.com/api/config/v1/applicationDetectionRules/9568a82b-73d8-4b18-be1a-4289433e2619 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{ <truncated - see the Request body section > }'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/applicationDetectionRules/9568a82b-73d8-4b18-be1a-4289433e2619
```

#### Тело запроса

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

#### Код ответа

204

## Связанные темы

* [Мониторинг реальных пользователей](/managed/observe/digital-experience/rum-concepts/rum-overview "Узнайте о мониторинге реальных пользователей, ключевых метриках производительности, мониторинге мобильных приложений и многом другом.")
* [Проверка правил обнаружения приложений](/managed/observe/digital-experience/web-applications/additional-configuration/application-detection-rules "Легко разберитесь в правилах обнаружения вашего RUM-приложения.")
* [Определение приложений для Real User Monitoring](/managed/observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder "Узнайте, как определять приложения с использованием предложенного, ручного подхода или правил обнаружения приложений.")