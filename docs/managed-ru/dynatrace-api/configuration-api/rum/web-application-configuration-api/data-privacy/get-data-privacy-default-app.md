---
title: Web application configuration API - GET data privacy of the default application
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/get-data-privacy-default-app
---

# Web application configuration API - GET data privacy of the default application

# Web application configuration API - GET data privacy of the default application

* Справка
* Опубликовано 03 сентября 2019

Получает параметры конфиденциальности данных веб-приложения по умолчанию для окружения Dynatrace.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/default/dataPrivacy` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/default/dataPrivacy` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `ReadConfig`.

Подробнее о том, как получить и использовать такой токен, см. в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Запрос не предусматривает настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ApplicationDataPrivacy](#openapi-definition-ApplicationDataPrivacy) | Успешно |

### Объекты тела ответа

#### Объект `ApplicationDataPrivacy`

Настройки конфиденциальности данных приложения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| dataCaptureOptInEnabled | boolean | Установи `true`, чтобы отключить сбор данных и cookie до вызова JavaScriptAPI `dtrum.enable()`. |
| doNotTrackBehaviour | string | Как обрабатывать заголовок "Do Not Track":  * `IGNORE_DO_NOT_TRACK`: игнорировать заголовок и собирать данные. * `CAPTURE_ANONYMIZED`: собирать данные, но не привязывать их к пользователю. * `DO_NOT_CAPTURE`: соблюдать заголовок и не собирать данные. Элемент может принимать следующие значения * `CAPTURE_ANONYMIZED` * `DO_NOT_CAPTURE` * `IGNORE_DO_NOT_TRACK` |
| identifier | string | ID сущности Dynatrace для веб-приложения. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки |
| persistentCookieForUserTracking | boolean | Установи `true`, чтобы установить постоянный cookie для распознавания повторных устройств. |
| sessionReplayDataPrivacy | [SessionReplayDataPrivacySettings](#openapi-definition-SessionReplayDataPrivacySettings) | Настройки конфиденциальности данных для Session Replay. |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `SessionReplayDataPrivacySettings`

Настройки конфиденциальности данных для Session Replay.

| Элемент | Тип | Описание |
| --- | --- | --- |
| contentMaskingSettings | [SessionReplayContentMaskingSettings](#openapi-definition-SessionReplayContentMaskingSettings) | Настройки маскирования контента для Session Replay.  Подробнее см. в разделе [Configure Session Replay﻿](https://dt-url.net/0m03slq?dt=m) в документации Dynatrace. |
| optInModeEnabled | boolean | Если установлено `true`, запись сессий отключена до вызова JavaScriptAPI `dtrum.enableSessionReplay()`. |
| urlExclusionRules | string[] | Список URL, исключаемых из записи. |

#### Объект `SessionReplayContentMaskingSettings`

Настройки маскирования контента для Session Replay.

Подробнее см. в разделе [Configure Session Replay﻿](https://dt-url.net/0m03slq?dt=m) в документации Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| playbackMaskingSettings | [SessionReplayMaskingSetting](#openapi-definition-SessionReplayMaskingSetting) | Конфигурация маскирования Session Replay. |
| recordingMaskingSettings | [SessionReplayMaskingSetting](#openapi-definition-SessionReplayMaskingSetting) | Конфигурация маскирования Session Replay. |
| recordingMaskingSettingsVersion | integer | Версия маскирования контента.  Этот API можно использовать только с версией 2.  Если используется версия 1, установи в этом поле значение `2` в запросе PUT, чтобы переключиться на версию 2. |

#### Объект `SessionReplayMaskingSetting`

Конфигурация маскирования Session Replay.

| Элемент | Тип | Описание |
| --- | --- | --- |
| maskingPreset | string | Тип маскирования:  * `MASK_ALL`: маскировать весь текст, пользовательский ввод и изображения. * `MASK_USER_INPUT`: маскировать все данные, вводимые пользователем * `ALLOW_LIST`: отображаются только элементы, указанные в **maskingRules**, всё остальное маскируется. * `BLOCK_LIST`: элементы, указанные в **maskingRules**, маскируются, всё остальное отображается. Элемент может принимать следующие значения * `ALLOW_LIST` * `BLOCK_LIST` * `MASK_ALL` * `MASK_USER_INPUT` |
| maskingRules | [MaskingRule](#openapi-definition-MaskingRule)[] | Список правил маскирования. |

#### Объект `MaskingRule`

Правило маскирования, определяющее, как скрываются данные.

| Элемент | Тип | Описание |
| --- | --- | --- |
| maskingRuleType | string | Тип правила маскирования. Элемент может принимать следующие значения * `ATTRIBUTE` * `ELEMENT` |
| selector | string | Селектор элемента или атрибута, подлежащего маскированию.  Укажи CSS-выражение для элемента или [регулярное выражение﻿](https://dt-url.net/k9e0iaq?dt=m) для атрибута. |
| userInteractionHidden | boolean | Взаимодействия с элементом маскируются (`true`) или не маскируются (`false). |

### Модели тела ответа JSON

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