---
title: Mobile and custom app API - GET an app
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/apps/get-app
scraped: 2026-05-12T11:15:36.778042
---

# Mobile and custom app API - GET an app

# Mobile and custom app API - GET an app

* Reference
* Published Nov 05, 2020

Возвращает параметры указанного мобильного или пользовательского приложения.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | UUID нужного мобильного или пользовательского приложения. Его можно найти в мастере инструментирования вашего приложения. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [MobileCustomAppConfig](#openapi-definition-MobileCustomAppConfig) | Успех |
| **404** | - | Сбой. Указанная сущность не существует. |

### Объекты тела ответа

#### Объект `MobileCustomAppConfig`

Конфигурация существующего мобильного или пользовательского приложения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| apdexSettings | [MobileCustomApdex](#openapi-definition-MobileCustomApdex) | Конфигурация Apdex для мобильного или пользовательского приложения.  Длительность меньше порога **tolerable** считается удовлетворительной. |
| applicationId | string | UUID приложения.  Используется только OneAgent для отправки данных в Dynatrace. |
| applicationType | string | Тип приложения. Возможные значения: * `CUSTOM_APPLICATION` * `MOBILE_APPLICATION` |
| beaconEndpointType | string | Тип beacon-эндпоинта. Возможные значения: * `CLUSTER_ACTIVE_GATE` * `ENVIRONMENT_ACTIVE_GATE` * `INSTRUMENTED_WEB_SERVER` |
| beaconEndpointUrl | string | URL beacon-эндпоинта.  Применимо только когда **beaconEndpointType** установлен в `ENVIRONMENT_ACTIVE_GATE` или `INSTRUMENTED_WEB_SERVER`. |
| costControlUserSessionPercentage | integer | Процент пользовательских сессий для анализа. |
| iconType | string | Иконка пользовательского приложения.  Мобильные приложения всегда используют иконку мобильного устройства, поэтому эту иконку можно задать только для пользовательских приложений. Возможные значения: * `AMAZON_ECHO` * `DESKTOP` * `EMBEDDED` * `IOT` * `MICROSOFT_HOLOLENS` * `UFO` * `USERS` |
| identifier | string | ID сущности Dynatrace для приложения. |
| name | string | Имя приложения. |
| optInModeEnabled | boolean | Режим opt-in включён (`true`) или отключён (`false`).  Это значение применимо только к мобильным, а не к пользовательским приложениям. |
| sessionReplayEnabled | boolean | Session Replay включён (`true`) или отключён (`false`). Это значение применимо только к мобильным, а не к пользовательским приложениям. |
| sessionReplayOnCrashEnabled | boolean | **Устарело**. Используйте `sessionReplayEnabled` для включения или отключения Session Replay для мобильных приложений. |

#### Объект `MobileCustomApdex`

Конфигурация Apdex для мобильного или пользовательского приложения.

Длительность меньше порога **tolerable** считается удовлетворительной.

| Элемент | Тип | Описание |
| --- | --- | --- |
| frustratedOnError | boolean | Условие ошибки Apdex: если `true`, пользовательская сессия считается frustrated при сообщении об ошибке. |
| frustratingThreshold | integer | Порог Apdex **frustrated**, в миллисекундах: длительность больше или равная этому значению считается frustrated. |
| toleratedThreshold | integer | Порог Apdex **tolerable**, в миллисекундах: длительность больше или равная этому значению считается tolerable. |

### JSON-модели тела ответа

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