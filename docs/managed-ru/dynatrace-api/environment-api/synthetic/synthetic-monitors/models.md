---
title: Synthetic monitors API - JSON-модели
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/synthetic-monitors/models
scraped: 2026-05-12T12:10:02.374167
---

# Synthetic monitors API - JSON-модели

# Synthetic monitors API - JSON-модели

* Справочник
* Опубликовано 19 августа 2019 г.

Некоторые JSON-модели API **Synthetic monitors** различаются в зависимости от **type** модели. JSON-модели для каждой вариации приведены ниже.

## Вариации объекта `SyntheticMonitor`

### BROWSER

BrowserSyntheticMonitor

Параметры

JSON-модель

#### Объект `BrowserSyntheticMonitor`

Браузерный синтетический монитор. Часть полей наследуется от базовой модели `SyntheticMonitor`.

| Поле | Тип | Описание |
| --- | --- | --- |
| events | [EventDto[]](#openapi-definition-EventDto) | Список событий для этого монитора |
| keyPerformanceMetrics | [KeyPerformanceMetrics](#openapi-definition-KeyPerformanceMetrics) | Конфигурация ключевых метрик производительности. |

#### Объект `EventDto`

| Поле | Тип | Описание |
| --- | --- | --- |
| entityId | string | Идентификатор события |
| name | string | Имя события |
| sequenceNumber | integer | Порядковый номер события |

#### Объект `KeyPerformanceMetrics`

Конфигурация ключевых метрик производительности.

| Поле | Тип | Описание |
| --- | --- | --- |
| loadActionKpm | string | Определяет ключевую метрику производительности для действий загрузки. Поле может принимать значения: * `VISUALLY_COMPLETE` * `SPEED_INDEX` * `USER_ACTION_DURATION` * `TIME_TO_FIRST_BYTE` * `HTML_DOWNLOADED` * `DOM_INTERACTIVE` * `LOAD_EVENT_START` * `LOAD_EVENT_END` |
| xhrActionKpm | string | Определяет ключевую метрику производительности для XHR-действий. Поле может принимать значения: * `VISUALLY_COMPLETE` * `USER_ACTION_DURATION` * `TIME_TO_FIRST_BYTE` * `RESPONSE_END` |

```
{



"entityId": "SYNTHETIC_TEST-790745B687BE4D0E",



"name": "Browser monitor",



"frequencyMin": 10,



"enabled": true,



"type": "BROWSER",



"createdFrom": "GUI",



"script": {



"type": "clickpath",



"version": "1.0",



"configuration": {



"device": {



"mobile": false,



"touchEnabled": false,



"width": 1024,



"height": 768,



"scaleFactor": 1



}



},



"events": [



{



"type": "navigate",



"description": "Loading of \"https://orf.at\"",



"url": "https://orf.at",



"wait": {



"waitFor": "page_complete"



}



}



]



},



"locations": [



"GEOLOCATION-0A41430434C388A9"



],



"anomalyDetection": {



"outageHandling": {



"globalOutage": true,



"localOutage": false,



"localOutagePolicy": {



"affectedLocations": 1,



"consecutiveRuns": 3



}



},



"loadingTimeThresholds": {



"enabled": true,



"thresholds": [



{



"type": "TOTAL",



"valueMs": 10000



}



]



}



},



"tags": [



{



"context": "CONTEXTLESS",



"key": "blabla"



}



],



"managementZones": [



{



"id": "-7832237287622819191",



"name": "!!allSynthetic"



}



],



"automaticallyAssignedApps": [



"APPLICATION-7ADA0EF404C7C545"



],



"manuallyAssignedApps": [



"APPLICATION-4ADF0EF407C7C545"



],



"keyPerformanceMetrics": {



"loadActionKpm": "VISUALLY_COMPLETE",



"xhrActionKpm": "VISUALLY_COMPLETE"



},



"events": [



{



"entityId": "SYNTHETIC_TEST_STEP-2E6FDA5B4BC39A27",



"name": "Loading of \"https://orf.at\"",



"sequenceNumber": 1



}



]



}
```

### HTTP

HttpSyntheticMonitor

Параметры

JSON-модель

#### Объект `HttpSyntheticMonitor`

HTTP-синтетический монитор. Часть полей наследуется от базовой модели `SyntheticMonitor`.

| Поле | Тип | Описание |
| --- | --- | --- |
| requests | [RequestDto[]](#openapi-definition-RequestDto) | Список событий для этого монитора |

#### Объект `RequestDto`

| Поле | Тип | Описание |
| --- | --- | --- |
| entityId | string | Идентификатор запроса |
| name | string | Имя запроса |
| sequenceNumber | integer | Порядковый номер запроса |

```
{



"entityId": "HTTP_CHECK-B58DA1B8B892A05C",



"name": "HTTP monitor",



"frequencyMin": 1,



"enabled": true,



"type": "HTTP",



"createdFrom": "GUI",



"script": {



"version": "1.0",



"requests": [



{



"description": "orf.at",



"url": "https://orf.at",



"method": "GET",



"requestBody": "",



"configuration": {



"acceptAnyCertificate": true,



"followRedirects": true



},



"preProcessingScript": "",



"postProcessingScript": ""



}



]



},



"locations": [



"SYNTHETIC_LOCATION-61F43EECF5FB8345"



],



"anomalyDetection": {



"outageHandling": {



"globalOutage": true,



"localOutage": false,



"localOutagePolicy": {



"affectedLocations": 1,



"consecutiveRuns": 3



}



},



"loadingTimeThresholds": {



"enabled": false,



"thresholds": [



{



"type": "TOTAL",



"valueMs": 10000



}



]



}



},



"tags": [],



"managementZones": [



{



"id": "-7832237287622819191",



"name": "!!allSynthetic"



}



],



"automaticallyAssignedApps": [



"APPLICATION-4ADF0EF407C7C545"



],



"manuallyAssignedApps": [



"APPLICATION-7ADA0EF404C7C545"



],



"requests": [



{



"entityId": "HTTP_CHECK_STEP-E9208469D53BAF38",



"name": "orf.at",



"sequenceNumber": 1



}



]



}
```

## Вариации объекта `SyntheticMonitorUpdate`

### BROWSER

BrowserSyntheticMonitorUpdate

Параметры

JSON-модель

#### Объект `BrowserSyntheticMonitorUpdate`

Обновление браузерного синтетического монитора. Часть полей наследуется от базовой модели `SyntheticMonitorUpdate`.

| Поле | Тип | Описание |
| --- | --- | --- |
| keyPerformanceMetrics | [KeyPerformanceMetrics](#openapi-definition-KeyPerformanceMetrics) | Конфигурация ключевых метрик производительности. |

#### Объект `KeyPerformanceMetrics`

Конфигурация ключевых метрик производительности.

| Поле | Тип | Описание |
| --- | --- | --- |
| loadActionKpm | string | Определяет ключевую метрику производительности для действий загрузки. Поле может принимать значения: * `VISUALLY_COMPLETE` * `SPEED_INDEX` * `USER_ACTION_DURATION` * `TIME_TO_FIRST_BYTE` * `HTML_DOWNLOADED` * `DOM_INTERACTIVE` * `LOAD_EVENT_START` * `LOAD_EVENT_END` |
| xhrActionKpm | string | Определяет ключевую метрику производительности для XHR-действий. Поле может принимать значения: * `VISUALLY_COMPLETE` * `USER_ACTION_DURATION` * `TIME_TO_FIRST_BYTE` * `RESPONSE_END` |

```
{



"name": "Browser monitor",



"frequencyMin": 10,



"enabled": true,



"type": "BROWSER",



"script": {



"type": "clickpath",



"version": "1.0",



"configuration": {



"device": {



"mobile": false,



"touchEnabled": false,



"width": 1024,



"height": 768,



"scaleFactor": 1



}



},



"events": [



{



"type": "navigate",



"description": "Loading of \"https://orf.at\"",



"url": "https://orf.at",



"wait": {



"waitFor": "page_complete"



}



}



]



},



"locations": [



"GEOLOCATION-0A41430434C388A9"



],



"anomalyDetection": {



"outageHandling": {



"globalOutage": true,



"localOutage": false,



"localOutagePolicy": {



"affectedLocations": 1,



"consecutiveRuns": 3



}



},



"loadingTimeThresholds": {



"enabled": true,



"thresholds": [



{



"type": "TOTAL",



"valueMs": 10000



}



]



}



},



"tags": [



{



"context": "CONTEXTLESS",



"key": "blabla"



}



],



"manuallyAssignedApps": [



"APPLICATION-4ADF0EF407C7C545"



],



"keyPerformanceMetrics": {



"loadActionKpm": "VISUALLY_COMPLETE",



"xhrActionKpm": "VISUALLY_COMPLETE"



}



}
```

### HTTP

HttpSyntheticMonitorUpdate

Параметры

JSON-модель

#### Объект `HttpSyntheticMonitorUpdate`

Обновление HTTP-синтетического монитора. Часть полей наследуется от базовой модели `SyntheticMonitorUpdate`.

| Поле | Тип | Описание |
| --- | --- | --- |
| anomalyDetection | [AnomalyDetection](#openapi-definition-AnomalyDetection) | Конфигурация обнаружения аномалий. |
| enabled | boolean | Монитор включён (`true`) или отключён (`false`). |
| frequencyMin | integer | Частота монитора, в минутах.  Можно использовать одно из следующих значений: `5`, `10`, `15`, `30` и `60`. |
| locations | string[] | Список локаций, с которых выполняется монитор.  Чтобы указать локацию, используйте её entity ID. Для публичных локаций используйте форму `GEOLOCATION-9999453BE4BDB3CD` и `SYNTHETIC_LOCATION-DF80ACFB688C583B` для приватных. |
| manuallyAssignedApps | string[] | Набор вручную назначенных приложений. |
| name | string | Имя монитора. |
| script | object | Скрипт [браузерного](https://dt-url.net/9c103rda) или HTTP-монитора. |
| tags | [TagWithSourceInfo[]](#openapi-definition-TagWithSourceInfo) | Набор тегов, назначенных монитору.  Здесь можно указать только значение тега, а контекст `CONTEXTLESS` и источник 'USER' будут добавлены автоматически. Но предпочтительный вариант, это использование модели TagWithSourceDto. |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из объектов:  * `BROWSER` -> BrowserSyntheticMonitorUpdate * `HTTP` -> HttpSyntheticMonitorUpdate Поле может принимать значения: * `BROWSER` * `HTTP` |

#### Объект `AnomalyDetection`

Конфигурация обнаружения аномалий.

| Поле | Тип | Описание |
| --- | --- | --- |
| loadingTimeThresholds | [LoadingTimeThresholdsPolicyDto](#openapi-definition-LoadingTimeThresholdsPolicyDto) | Конфигурация порогов производительности. |
| outageHandling | [OutageHandlingPolicy](#openapi-definition-OutageHandlingPolicy) | Конфигурация обработки недоступности. |

#### Объект `LoadingTimeThresholdsPolicyDto`

Конфигурация порогов производительности.

| Поле | Тип | Описание |
| --- | --- | --- |
| enabled | boolean | Порог производительности включён (`true`) или отключён (`false`). |
| thresholds | [LoadingTimeThreshold[]](#openapi-definition-LoadingTimeThreshold) | Список правил порогов производительности. |

#### Объект `LoadingTimeThreshold`

Правило порога производительности.

| Поле | Тип | Описание |
| --- | --- | --- |
| eventIndex | integer | Укажите событие, к которому применяется порог ACTION. |
| requestIndex | integer | Укажите запрос, к которому применяется порог ACTION. |
| type | string | Тип порога: общее время загрузки или время загрузки действия. Поле может принимать значения: * `ACTION` * `TOTAL` |
| valueMs | integer | Уведомлять, если загрузка монитора занимает больше *X* миллисекунд. |

#### Объект `OutageHandlingPolicy`

Конфигурация обработки недоступности.

| Поле | Тип | Описание |
| --- | --- | --- |
| globalOutage | boolean | Когда включено (`true`), создавать проблему и отправлять алерт, когда монитор недоступен во всех настроенных локациях. |
| globalOutagePolicy | [GlobalOutagePolicy](#openapi-definition-GlobalOutagePolicy) | Конфигурация обработки глобальной недоступности. |
| localOutage | boolean | Когда включено (`true`), создавать проблему и отправлять алерт, когда монитор недоступен в течение одного или нескольких последовательных запусков в любой локации. |
| localOutagePolicy | [LocalOutagePolicy](#openapi-definition-LocalOutagePolicy) | Конфигурация обработки локальной недоступности.  Алерт, если **affectedLocations** локаций не могут получить доступ к веб-приложению **consecutiveRuns** раз подряд. |
| retryOnError | boolean | Запланировать повтор, если выполнение браузерного монитора завершается неудачей. Для HTTP-мониторов это свойство игнорируется. |

#### Объект `GlobalOutagePolicy`

Конфигурация обработки глобальной недоступности.

| Поле | Тип | Описание |
| --- | --- | --- |
| consecutiveRuns | integer | Алерт, если все локации не могут получить доступ к веб-приложению *X* раз подряд. |

#### Объект `LocalOutagePolicy`

Конфигурация обработки локальной недоступности.

Алерт, если **affectedLocations** локаций не могут получить доступ к веб-приложению **consecutiveRuns** раз подряд.

| Поле | Тип | Описание |
| --- | --- | --- |
| affectedLocations | integer | Число затронутых локаций для срабатывания алерта. |
| consecutiveRuns | integer | Число последовательных неудач для срабатывания алерта. |

#### Объект `TagWithSourceInfo`

Тег с источником сущности Dynatrace.

| Поле | Тип | Описание |
| --- | --- | --- |
| context | string | Источник тега, например AWS или Cloud Foundry.  Пользовательские теги используют значение `CONTEXTLESS`. Поле может принимать значения: * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | Ключ тега.  У пользовательских тегов здесь находится значение тега. |
| source | string | Источник тега, например USER, RULE\_BASED или AUTO Поле может принимать значения: * `AUTO` * `RULE_BASED` * `USER` |
| value | string | Значение тега.  Неприменимо к пользовательским тегам. |

```
{



"name": "HTTP monitor",



"frequencyMin": 1,



"enabled": true,



"type": "HTTP",



"script": {



"version": "1.0",



"requests": [



{



"description": "orf.at",



"url": "https://orf.at",



"method": "GET",



"requestBody": "",



"configuration": {



"acceptAnyCertificate": true,



"followRedirects": true



},



"preProcessingScript": "",



"postProcessingScript": ""



}



]



},



"locations": [



"SYNTHETIC_LOCATION-61F43EECF5FB8345"



],



"anomalyDetection": {



"outageHandling": {



"globalOutage": true,



"localOutage": false,



"localOutagePolicy": {



"affectedLocations": 1,



"consecutiveRuns": 3



}



},



"loadingTimeThresholds": {



"enabled": false,



"thresholds": [



{



"type": "TOTAL",



"valueMs": 10000



}



]



}



},



"tags": [],



"manuallyAssignedApps": [



"APPLICATION-7ADA0EF404C7C545"



]



}
```

## Связанные темы

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать браузерный монитор одного URL, браузерный clickpath или HTTP-монитор.")