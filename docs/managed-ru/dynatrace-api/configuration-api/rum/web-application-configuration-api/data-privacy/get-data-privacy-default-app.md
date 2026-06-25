---
title: Web application configuration API - GET data privacy of the default application
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/get-data-privacy-default-app
scraped: 2026-05-12T11:16:53.190468
---

# Web application configuration API - GET data privacy of the default application

# Web application configuration API - GET data privacy of the default application

* Reference
* Published Sep 03, 2019

Возвращает параметры конфиденциальности данных веб-приложения по умолчанию вашего окружения Dynatrace.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/default/dataPrivacy` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/default/dataPrivacy` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

В запросе нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ApplicationDataPrivacy](#openapi-definition-ApplicationDataPrivacy) | Успех |

### Объекты тела ответа

#### Объект `ApplicationDataPrivacy`

Настройки конфиденциальности данных приложения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| dataCaptureOptInEnabled | boolean | Установите `true`, чтобы отключить сбор данных и cookie, пока не будет вызван JavaScriptAPI `dtrum.enable()`. |
| doNotTrackBehaviour | string | Как обрабатывать заголовок "Do Not Track":  * `IGNORE_DO_NOT_TRACK`: игнорировать заголовок и собирать данные. * `CAPTURE_ANONYMIZED`: собирать данные, но не связывать их с пользователем. * `DO_NOT_CAPTURE`: учитывать заголовок и не собирать. Возможные значения: * `CAPTURE_ANONYMIZED` * `DO_NOT_CAPTURE` * `IGNORE_DO_NOT_TRACK` |
| identifier | string | ID сущности Dynatrace для веб-приложения. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки |
| persistentCookieForUserTracking | boolean | Установите `true`, чтобы задать постоянный cookie для распознавания возвращающихся устройств. |
| sessionReplayDataPrivacy | [SessionReplayDataPrivacySettings](#openapi-definition-SessionReplayDataPrivacySettings) | Настройки конфиденциальности данных для Session Replay. |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `SessionReplayDataPrivacySettings`

Настройки конфиденциальности данных для Session Replay.

| Элемент | Тип | Описание |
| --- | --- | --- |
| contentMaskingSettings | [SessionReplayContentMaskingSettings](#openapi-definition-SessionReplayContentMaskingSettings) | Настройки маскирования контента для Session Replay.  Подробнее смотрите [Configure Session Replay](https://dt-url.net/0m03slq) в документации Dynatrace. |
| optInModeEnabled | boolean | Если `true`, запись сессий отключена, пока не будет вызван JavaScriptAPI `dtrum.enableSessionReplay()`. |
| urlExclusionRules | string[] | Список URL, исключаемых из записи. |

#### Объект `SessionReplayContentMaskingSettings`

Настройки маскирования контента для Session Replay.

Подробнее смотрите [Configure Session Replay](https://dt-url.net/0m03slq) в документации Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| playbackMaskingSettings | [SessionReplayMaskingSetting](#openapi-definition-SessionReplayMaskingSetting) | Конфигурация маскирования Session Replay. |
| recordingMaskingSettings | [SessionReplayMaskingSetting](#openapi-definition-SessionReplayMaskingSetting) | Конфигурация маскирования Session Replay. |
| recordingMaskingSettingsVersion | integer | Версия маскирования контента.  Этот API можно использовать только с версией 2.  Если вы используете версию 1, задайте в этом поле `2` в PUT-запросе, чтобы переключиться на версию 2. |

#### Объект `SessionReplayMaskingSetting`

Конфигурация маскирования Session Replay.

| Элемент | Тип | Описание |
| --- | --- | --- |
| maskingPreset | string | Тип маскирования:  * `MASK_ALL`: маскировать весь текст, пользовательский ввод и изображения. * `MASK_USER_INPUT`: маскировать все данные, предоставленные через пользовательский ввод * `ALLOW_LIST`: показываются только элементы, заданные в **maskingRules**, всё остальное маскируется. * `BLOCK_LIST`: элементы, заданные в **maskingRules**, маскируются, всё остальное показывается. Возможные значения: * `ALLOW_LIST` * `BLOCK_LIST` * `MASK_ALL` * `MASK_USER_INPUT` |
| maskingRules | [MaskingRule[]](#openapi-definition-MaskingRule) | Список правил маскирования. |

#### Объект `MaskingRule`

Правило маскирования, определяющее, как скрываются данные.

| Элемент | Тип | Описание |
| --- | --- | --- |
| maskingRuleType | string | Тип правила маскирования. Возможные значения: * `ATTRIBUTE` * `ELEMENT` |
| selector | string | Селектор маскируемого элемента или атрибута.  Укажите CSS-выражение для элемента или [регулярное выражение](https://dt-url.net/k9e0iaq) для атрибута. |
| userInteractionHidden | boolean | Взаимодействия с элементом маскируются (`true`) или не маскируются (`false). |

### JSON-модели тела ответа

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