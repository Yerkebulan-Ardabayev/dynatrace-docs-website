---
title: Mobile and custom app API - POST an app
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/apps/post-app
scraped: 2026-05-12T11:15:32.993290
---

# Mobile and custom app API - POST an app

# Mobile and custom app API - POST an app

* Reference
* Published Nov 05, 2020

Создаёт новое мобильное или пользовательское приложение.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [NewMobileCustomAppConfig](#openapi-definition-NewMobileCustomAppConfig) | JSON-тело запроса. Содержит параметры нового мобильного или пользовательского приложения. | body | Optional |

### Объекты тела запроса

#### Объект `NewMobileCustomAppConfig`

Конфигурация создаваемого мобильного или пользовательского приложения.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| apdexSettings | [MobileCustomApdex](#openapi-definition-MobileCustomApdex) | Конфигурация Apdex для мобильного или пользовательского приложения.  Длительность меньше порога **tolerable** считается удовлетворительной. | Optional |
| applicationId | string | UUID приложения.  Используется только OneAgent для отправки данных в Dynatrace. | Optional |
| applicationType | string | Тип приложения. Возможные значения: * `CUSTOM_APPLICATION` * `MOBILE_APPLICATION` | Required |
| beaconEndpointType | string | Тип beacon-эндпоинта. Возможные значения: * `CLUSTER_ACTIVE_GATE` * `ENVIRONMENT_ACTIVE_GATE` * `INSTRUMENTED_WEB_SERVER` | Optional |
| beaconEndpointUrl | string | URL beacon-эндпоинта.  Применимо только когда **beaconEndpointType** установлен в `ENVIRONMENT_ACTIVE_GATE` или `INSTRUMENTED_WEB_SERVER`. | Optional |
| costControlUserSessionPercentage | integer | Процент пользовательских сессий для анализа. | Optional |
| iconType | string | Иконка пользовательского приложения.  Мобильные приложения всегда используют иконку мобильного устройства, поэтому эту иконку можно задать только для пользовательских приложений. Возможные значения: * `AMAZON_ECHO` * `DESKTOP` * `EMBEDDED` * `IOT` * `MICROSOFT_HOLOLENS` * `UFO` * `USERS` | Optional |
| name | string | Имя приложения. | Required |
| optInModeEnabled | boolean | Режим opt-in включён (`true`) или отключён (`false`).  Это значение применимо только к мобильным, а не к пользовательским приложениям. | Optional |
| sessionReplayEnabled | boolean | Session Replay включён (`true`) или отключён (`false`). Это значение применимо только к мобильным, а не к пользовательским приложениям. | Optional |
| sessionReplayOnCrashEnabled | boolean | **Устарело**. Используйте `sessionReplayEnabled` для включения или отключения Session Replay для мобильных приложений. | Optional |

#### Объект `MobileCustomApdex`

Конфигурация Apdex для мобильного или пользовательского приложения.

Длительность меньше порога **tolerable** считается удовлетворительной.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| frustratedOnError | boolean | Условие ошибки Apdex: если `true`, пользовательская сессия считается frustrated при сообщении об ошибке. | Required |
| frustratingThreshold | integer | Порог Apdex **frustrated**, в миллисекундах: длительность больше или равная этому значению считается frustrated. | Required |
| toleratedThreshold | integer | Порог Apdex **tolerable**, в миллисекундах: длительность больше или равная этому значению считается tolerable. | Required |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

```
{



"apdexSettings": {



"frustratedOnError": true,



"frustratingThreshold": 1,



"toleratedThreshold": 1



},



"applicationId": "string",



"applicationType": "CUSTOM_APPLICATION",



"beaconEndpointType": "CLUSTER_ACTIVE_GATE",



"beaconEndpointUrl": "string",



"costControlUserSessionPercentage": 1,



"iconType": "AMAZON_ECHO",



"name": "string",



"optInModeEnabled": true,



"sessionReplayEnabled": true,



"sessionReplayOnCrashEnabled": true



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Приложение создано. Ответ содержит идентификатор и имя нового приложения. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |
| **409** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. applicationId уже используется другим приложением. |

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
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Переданная конфигурация валидна. Ответ без тела. |
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