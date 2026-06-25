---
title: Mobile and custom app API - PUT an app
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/apps/put-app
scraped: 2026-05-12T11:15:38.277755
---

# Mobile and custom app API - PUT an app

# Mobile and custom app API - PUT an app

* Reference
* Published Nov 05, 2020

Обновляет указанное мобильное или пользовательское приложение.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{id}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | UUID нужного мобильного или пользовательского приложения. Его можно найти в мастере инструментирования вашего приложения. | path | Required |
| body | [MobileCustomAppConfig](#openapi-definition-MobileCustomAppConfig) | JSON-тело запроса. Содержит обновлённую конфигурацию мобильного или пользовательского приложения.  Не указывайте identifier в теле. | body | Optional |

### Объекты тела запроса

#### Объект `MobileCustomAppConfig`

Конфигурация существующего мобильного или пользовательского приложения.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| apdexSettings | [MobileCustomApdex](#openapi-definition-MobileCustomApdex) | Конфигурация Apdex для мобильного или пользовательского приложения.  Длительность меньше порога **tolerable** считается удовлетворительной. | Required |
| applicationId | string | UUID приложения.  Используется только OneAgent для отправки данных в Dynatrace. | Optional |
| applicationType | string | Тип приложения. Возможные значения: * `CUSTOM_APPLICATION` * `MOBILE_APPLICATION` | Optional |
| beaconEndpointType | string | Тип beacon-эндпоинта. Возможные значения: * `CLUSTER_ACTIVE_GATE` * `ENVIRONMENT_ACTIVE_GATE` * `INSTRUMENTED_WEB_SERVER` | Required |
| beaconEndpointUrl | string | URL beacon-эндпоинта.  Применимо только когда **beaconEndpointType** установлен в `ENVIRONMENT_ACTIVE_GATE` или `INSTRUMENTED_WEB_SERVER`. | Optional |
| costControlUserSessionPercentage | integer | Процент пользовательских сессий для анализа. | Required |
| iconType | string | Иконка пользовательского приложения.  Мобильные приложения всегда используют иконку мобильного устройства, поэтому эту иконку можно задать только для пользовательских приложений. Возможные значения: * `AMAZON_ECHO` * `DESKTOP` * `EMBEDDED` * `IOT` * `MICROSOFT_HOLOLENS` * `UFO` * `USERS` | Optional |
| identifier | string | ID сущности Dynatrace для приложения. | Optional |
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



"identifier": "string",



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
| **204** | - | Успех. Приложение обновлено. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |
| **404** | - | Сбой. Указанная сущность не существует. |

### Объекты тела ответа

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
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{id}/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{id}/validator` |

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