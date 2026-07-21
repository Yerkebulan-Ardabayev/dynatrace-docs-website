---
title: Web application configuration API - PUT data privacy of the default application
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/put-data-privacy-default-app
---

# Web application configuration API - PUT data privacy of the default application

# Web application configuration API - PUT data privacy of the default application

* Справочник
* Опубликовано 03 сентября 2019

Обновляет параметры конфиденциальности данных веб-приложения по умолчанию окружения Dynatrace.

Запрос принимает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/default/dataPrivacy` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/default/dataPrivacy` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `DataPrivacy`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | [ApplicationDataPrivacy](#openapi-definition-ApplicationDataPrivacy) | Тело JSON запроса, содержащее новые настройки конфиденциальности данных. | body | Опционально |

### Объекты тела запроса

#### Объект `ApplicationDataPrivacy`

Настройки конфиденциальности данных приложения.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| dataCaptureOptInEnabled | boolean | Установить в `true`, чтобы отключить сбор данных и cookie, пока не вызван JavaScriptAPI `dtrum.enable()`. | Обязательно |
| doNotTrackBehaviour | string | Как обрабатывать заголовок «Do Not Track»:  * `IGNORE_DO_NOT_TRACK`: игнорировать заголовок и собирать данные. * `CAPTURE_ANONYMIZED`: собирать данные, но не привязывать их к пользователю. * `DO_NOT_CAPTURE`: соблюдать заголовок и не собирать данные. Элемент может принимать следующие значения * `CAPTURE_ANONYMIZED` * `DO_NOT_CAPTURE` * `IGNORE_DO_NOT_TRACK` | Обязательно |
| identifier | string | ID сущности Dynatrace веб-приложения. | Опционально |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Опционально |
| persistentCookieForUserTracking | boolean | Установить в `true`, чтобы задать постоянный cookie для распознавания возвращающихся устройств. | Обязательно |
| sessionReplayDataPrivacy | [SessionReplayDataPrivacySettings](#openapi-definition-SessionReplayDataPrivacySettings) | Настройки конфиденциальности данных для Session Replay. | Опционально |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Опционально |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Опционально |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Опционально |

#### Объект `SessionReplayDataPrivacySettings`

Настройки конфиденциальности данных для Session Replay.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| contentMaskingSettings | [SessionReplayContentMaskingSettings](#openapi-definition-SessionReplayContentMaskingSettings) | Настройки маскирования содержимого для Session Replay.  Подробнее см. [Настройка Session Replay﻿](https://dt-url.net/0m03slq?dt=m) в документации Dynatrace. | Опционально |
| optInModeEnabled | boolean | Если `true`, запись сессий отключена, пока не вызван JavaScriptAPI `dtrum.enableSessionReplay()`. | Опционально |
| urlExclusionRules | string[] | Список URL, исключаемых из записи. | Опционально |

#### Объект `SessionReplayContentMaskingSettings`

Настройки маскирования содержимого для Session Replay.

Подробнее см. [Настройка Session Replay﻿](https://dt-url.net/0m03slq?dt=m) в документации Dynatrace.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| playbackMaskingSettings | [SessionReplayMaskingSetting](#openapi-definition-SessionReplayMaskingSetting) | Конфигурация маскирования Session Replay. | Опционально |
| recordingMaskingSettings | [SessionReplayMaskingSetting](#openapi-definition-SessionReplayMaskingSetting) | Конфигурация маскирования Session Replay. | Опционально |
| recordingMaskingSettingsVersion | integer | Версия маскирования содержимого.  Это поле API можно использовать только с версией 2.  Если используется версия 1, установите в этом поле значение `2` в запросе PUT, чтобы перейти на версию 2. | Обязательно |

#### Объект `SessionReplayMaskingSetting`

Конфигурация маскирования Session Replay.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| maskingPreset | string | Тип маскирования:  * `MASK_ALL`: маскировать весь текст, пользовательский ввод и изображения. * `MASK_USER_INPUT`: маскировать все данные, введённые пользователем * `ALLOW_LIST`: отображаются только элементы, указанные в **maskingRules**, всё остальное маскируется. * `BLOCK_LIST`: элементы, указанные в **maskingRules**, маскируются, всё остальное отображается. Элемент может принимать следующие значения * `ALLOW_LIST` * `BLOCK_LIST` * `MASK_ALL` * `MASK_USER_INPUT` | Обязательно |
| maskingRules | [MaskingRule](#openapi-definition-MaskingRule)[] | Список правил маскирования. | Опционально |

#### Объект `MaskingRule`

Правило маскирования, определяющее, как скрываются данные.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| maskingRuleType | string | Тип правила маскирования. Элемент может принимать следующие значения * `ATTRIBUTE` * `ELEMENT` | Обязательно |
| selector | string | Селектор элемента или атрибута, подлежащего маскированию.  Укажите CSS-выражение для элемента или [регулярное выражение﻿](https://dt-url.net/k9e0iaq?dt=m) для атрибута. | Обязательно |
| userInteractionHidden | boolean | Взаимодействия с элементом маскируются (`true`) или не маскируются (`false`). | Обязательно |

### Модель тела JSON запроса

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
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Введённые данные некорректны. |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
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

## Проверка полезной нагрузки

Рекомендуется проверять полезную нагрузку перед отправкой в составе реального запроса. Код ответа **204** означает, что полезная нагрузка корректна.

Запрос принимает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/default/dataPrivacy/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/default/dataPrivacy/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `DataPrivacy`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответов

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Проверено. Отправленная конфигурация действительна. Тело ответа отсутствует. |
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