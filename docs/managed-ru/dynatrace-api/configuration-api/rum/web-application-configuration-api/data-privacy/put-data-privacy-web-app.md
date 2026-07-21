---
title: Web application configuration API - PUT data privacy of a web application
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/put-data-privacy-web-app
---

# Web application configuration API - PUT data privacy of a web application

# Web application configuration API - PUT data privacy of a web application

* Справка
* Опубликовано 03 сентября 2019 г.

Обновляет параметры конфиденциальности данных указанного веб-приложения.

Этот API поддерживает только веб-приложения. Для мобильных и пользовательских приложений см. [Mobile and custom app API](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration "Learn what the Dynatrace mobile and custom app config API offers.").

Запрос принимает и возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}/dataPrivacy` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}/dataPrivacy` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа со скоупом `DataPrivacy`.

О том, как его получить и использовать, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID веб-приложения, для которого нужно обновить настройки конфиденциальности данных. | path | Обязательный |
| body | [ApplicationDataPrivacy](#openapi-definition-ApplicationDataPrivacy) | JSON тело запроса, содержащее новые настройки конфиденциальности данных. | body | Необязательный |

### Объекты тела запроса

#### Объект `ApplicationDataPrivacy`

Настройки конфиденциальности данных приложения.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| dataCaptureOptInEnabled | boolean | Установить значение `true`, чтобы отключить захват данных и cookie до вызова JavaScriptAPI `dtrum.enable()`. | Обязательный |
| doNotTrackBehaviour | string | Как обрабатывать заголовок "Do Not Track":  * `IGNORE_DO_NOT_TRACK`: игнорировать заголовок и захватывать данные. * `CAPTURE_ANONYMIZED`: захватывать данные, но не привязывать их к пользователю. * `DO_NOT_CAPTURE`: соблюдать заголовок и не захватывать данные. Элемент может принимать следующие значения * `CAPTURE_ANONYMIZED` * `DO_NOT_CAPTURE` * `IGNORE_DO_NOT_TRACK` | Обязательный |
| identifier | string | Dynatrace ID сущности веб-приложения. | Необязательный |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Необязательный |
| persistentCookieForUserTracking | boolean | Установить значение `true`, чтобы устанавливать постоянный cookie для распознавания повторно заходящих устройств. | Обязательный |
| sessionReplayDataPrivacy | [SessionReplayDataPrivacySettings](#openapi-definition-SessionReplayDataPrivacySettings) | Настройки конфиденциальности данных для Session Replay. | Необязательный |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Необязательный |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Необязательный |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Необязательный |

#### Объект `SessionReplayDataPrivacySettings`

Настройки конфиденциальности данных для Session Replay.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| contentMaskingSettings | [SessionReplayContentMaskingSettings](#openapi-definition-SessionReplayContentMaskingSettings) | Настройки маскирования содержимого для Session Replay.  Подробнее см. [Configure Session Replay﻿](https://dt-url.net/0m03slq?dt=m) в документации Dynatrace. | Необязательный |
| optInModeEnabled | boolean | Если `true`, запись сессий отключена до вызова JavaScriptAPI `dtrum.enableSessionReplay()`. | Необязательный |
| urlExclusionRules | string[] | Список URL, которые нужно исключить из записи. | Необязательный |

#### Объект `SessionReplayContentMaskingSettings`

Настройки маскирования содержимого для Session Replay.

Подробнее см. [Configure Session Replay﻿](https://dt-url.net/0m03slq?dt=m) в документации Dynatrace.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| playbackMaskingSettings | [SessionReplayMaskingSetting](#openapi-definition-SessionReplayMaskingSetting) | Конфигурация маскирования Session Replay. | Необязательный |
| recordingMaskingSettings | [SessionReplayMaskingSetting](#openapi-definition-SessionReplayMaskingSetting) | Конфигурация маскирования Session Replay. | Необязательный |
| recordingMaskingSettingsVersion | integer | Версия маскирования содержимого.  Этот API можно использовать только с версией 2.  Если используется версия 1, установите в этом поле значение `2` в PUT-запросе, чтобы переключиться на версию 2. | Обязательный |

#### Объект `SessionReplayMaskingSetting`

Конфигурация маскирования Session Replay.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| maskingPreset | string | Тип маскирования:  * `MASK_ALL`: маскировать весь текст, пользовательский ввод и изображения. * `MASK_USER_INPUT`: маскировать все данные, введённые пользователем * `ALLOW_LIST`: показываются только элементы, указанные в **maskingRules**, всё остальное маскируется. * `BLOCK_LIST`: элементы, указанные в **maskingRules**, маскируются, всё остальное отображается. Элемент может принимать следующие значения * `ALLOW_LIST` * `BLOCK_LIST` * `MASK_ALL` * `MASK_USER_INPUT` | Обязательный |
| maskingRules | [MaskingRule](#openapi-definition-MaskingRule)[] | Список правил маскирования. | Необязательный |

#### Объект `MaskingRule`

Правило маскирования, определяющее, как скрываются данные.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| maskingRuleType | string | Тип правила маскирования. Элемент может принимать следующие значения * `ATTRIBUTE` * `ELEMENT` | Обязательный |
| selector | string | Селектор элемента или атрибута, который нужно маскировать.  Укажите CSS-выражение для элемента или [регулярное выражение﻿](https://dt-url.net/k9e0iaq?dt=m) для атрибута. | Обязательный |
| userInteractionHidden | boolean | Взаимодействия с элементом маскируются (`true`) или не маскируются (`false`). | Обязательный |

### JSON модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

```
{



"dataCaptureOptInEnabled": true,



"doNotTrackBehaviour": "CAPTURE_ANONYMIZED",



"identifier": "string",



"metadata": {



"clusterVersion": "1.192.1",



"configurationVersions": [



4,



2



],



"currentConfigurationVersions": [



"1.0.4",



"1.23"



]



},



"persistentCookieForUserTracking": true,



"sessionReplayDataPrivacy": {



"contentMaskingSettings": {



"playbackMaskingSettings": {



"maskingPreset": "ALLOW_LIST",



"maskingRules": [



{



"maskingRuleType": "ATTRIBUTE",



"selector": "string",



"userInteractionHidden": false



}



]



},



"recordingMaskingSettings": {},



"recordingMaskingSettingsVersion": 2



},



"optInModeEnabled": true,



"urlExclusionRules": [



"string"



]



}



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успешно. Настройки конфиденциальности данных обновлены. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Введённые данные недействительны. |

### Объекты тела ответа

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

### JSON модели тела ответа

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

## Проверка payload

Рекомендуется проверять payload перед его отправкой в составе реального запроса. Код ответа **204** означает, что payload действителен.

Запрос принимает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}/dataPrivacy/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}/dataPrivacy/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа со скоупом `DataPrivacy`.

О том, как его получить и использовать, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Проверено. Отправленная конфигурация действительна. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Введённые данные недействительны. |

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

#### Модели тела ответа JSON

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