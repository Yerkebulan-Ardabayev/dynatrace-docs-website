---
title: Synthetic monitors API - GET монитор
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/synthetic-monitors/get-a-monitor
scraped: 2026-05-12T11:59:52.446088
---

# Synthetic monitors API - GET монитор

# Synthetic monitors API - GET монитор

* Справочник
* Опубликовано 25 июля 2019 г.

Возвращает свойства указанного монитора, включая его JSON-скрипт.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/synthetic/monitors/{monitorId}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/synthetic/monitors/{monitorId}` |

## Аутентификация

Для выполнения запроса нужен access-токен с одним из следующих scope:

* `ExternalSyntheticIntegration`
* `ReadSyntheticData`

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| monitorId | string | ID требуемого синтетического монитора | path | Обязательный |

## Ответ

Все вариации модели, зависящие от типа модели, смотрите в [JSON-моделях](/managed/dynatrace-api/environment-api/synthetic/synthetic-monitors/models "Узнайте о вариациях моделей в Synthetic monitors v1 API.").

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SyntheticMonitor](#openapi-definition-SyntheticMonitor) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SyntheticMonitor`

Синтетический монитор.

Фактический набор полей зависит от типа монитора. Список фактических объектов смотрите в описании поля **type** или в [Synthetic monitors API - JSON-модели](https://dt-url.net/2523se9).

| Поле | Тип | Описание |
| --- | --- | --- |
| anomalyDetection | [AnomalyDetection](#openapi-definition-AnomalyDetection) | Конфигурация обнаружения аномалий. |
| automaticallyAssignedApps | string[] | Набор автоматически назначенных приложений. |
| createdFrom | string | Источник монитора Поле может принимать значения: * `API` * `GUI` |
| enabled | boolean | Монитор включён (`true`) или отключён (`false`). |
| entityId | string | Entity ID монитора. |
| frequencyMin | integer | Частота монитора, в минутах.  Можно использовать одно из следующих значений: `5`, `10`, `15`, `30` и `60`. |
| locations | string[] | Список локаций, с которых выполняется монитор.  Чтобы указать локацию, используйте её entity ID. Для публичных локаций в форме `GEOLOCATION-9999453BE4BDB3CD` и `SYNTHETIC_LOCATION-DF80ACFB688C583B` для приватных. |
| managementZones | [ManagementZone[]](#openapi-definition-ManagementZone) | Набор management zone, к которым принадлежит монитор. |
| manuallyAssignedApps | string[] | Набор вручную назначенных приложений. |
| name | string | Имя монитора. |
| script | object | Скрипт [браузерного](https://dt-url.net/9c103rda) или HTTP-монитора. |
| tags | [TagWithSourceInfo[]](#openapi-definition-TagWithSourceInfo) | Набор тегов, назначенных монитору. |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из объектов:  * `BROWSER` -> BrowserSyntheticMonitor * `HTTP` -> HttpSyntheticMonitor Поле может принимать значения: * `BROWSER` * `HTTP` |

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

#### Объект `ManagementZone`

Конфигурация management zone.

| Поле | Тип | Описание |
| --- | --- | --- |
| id | string | ID management zone. |
| name | string | Имя management zone. |

#### Объект `TagWithSourceInfo`

Тег с источником сущности Dynatrace.

| Поле | Тип | Описание |
| --- | --- | --- |
| context | string | Источник тега, например AWS или Cloud Foundry.  Пользовательские теги используют значение `CONTEXTLESS`. Поле может принимать значения: * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | Ключ тега.  У пользовательских тегов здесь находится значение тега. |
| source | string | Источник тега, например USER, RULE\_BASED или AUTO Поле может принимать значения: * `AUTO` * `RULE_BASED` * `USER` |
| value | string | Значение тега.  Неприменимо к пользовательским тегам. |

#### Объект `ErrorEnvelope`

| Поле | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Поле | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Поле | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Поле может принимать значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"anomalyDetection": {



"loadingTimeThresholds": {



"enabled": true,



"thresholds": [



{



"eventIndex": 1,



"requestIndex": 1,



"type": "ACTION",



"valueMs": 1



}



]



},



"outageHandling": {



"globalOutage": true,



"globalOutagePolicy": {



"consecutiveRuns": 1



},



"localOutage": true,



"localOutagePolicy": {



"affectedLocations": 1,



"consecutiveRuns": 1



},



"retryOnError": true



}



},



"automaticallyAssignedApps": [



"string"



],



"createdFrom": "API",



"enabled": true,



"entityId": "string",



"frequencyMin": 1,



"locations": [



"string"



],



"managementZones": [



{



"id": "string",



"name": "string"



}



],



"manuallyAssignedApps": [



"string"



],



"name": "string",



"script": {},



"tags": [



{



"context": "AWS",



"key": "string",



"source": "AUTO",



"value": "string"



}



],



"type": "BROWSER"



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

## Пример

В этом примере запрос возвращает параметры монитора **dynatrace.com**, который является **браузерным clickpath**, переходящим на [https://www.dynatrace.com/](https://www.dynatrace.com/) и регистрирующимся на бесплатную пробную версию.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/monitors/SYNTHETIC_TEST-0000000000025434 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/monitors/SYNTHETIC_TEST-0000000000025434
```

#### Тело ответа

```
{



"entityId": "SYNTHETIC_TEST-0000000000025434",



"name": "dynatrace.com",



"frequencyMin": 15,



"enabled": true,



"type": "browser",



"script": {



"type": "clickpath",



"version": "1.0",



"configuration": {



"device": {



"deviceName":"Desktop",



"orientation":"landscape"



}



},



"events": [



{



"type":"navigate",



"description":"Loading of \"http://www.dynatrace.com\"",



"url":"http://www.dynatrace.com",



"wait": {



"waitFor":"page_complete"



}



},



{



"type":"click",



"description":"click on \"Free trial\"",



"target": {



"locators": [



{



"type":"css",



"value":"a:contains(\"Free trial\"):eq(1)"



},



{



"type":"css",



"value":".btn:eq(1)"



},



{



"type":"css",



"value":"#content div div div div div div div p:nth-child(3) a"



},



{



"type":"css",



"value":"#content div.homepage-hero-wrapper div.gallery div.flickity-viewport div.flickity-slider div.gallery-cell div.section div.column p.cta--row a.btn:eq(0)"



}



]



},



"button": 0,



"wait": {



"waitFor":"page_complete"



}



}



{



"type":"click",



"description":"click on \"email\"",



"target": {



"locators": [



{



"type":"css",



"value":"input[type=\"email\"][name=\"email\"]:eq(0)"



},



{



"type":"dom",



"value":"document.forms[0][\"email\"]"



},



{



"type":"css",



"value":".inputfield:eq(0)"



},



{



"type":"css",



"value":"#content div div:nth-child(2) form:nth-child(9) input:nth-child(3)"



},



{



"type":"css",



"value":"#content div.section div.tile form.cta input.inputfield:eq(0)"



}



]



},



"button":0



},



{



"type":"keystrokes",



"description":"keystrokes on \"email\"",



"target":{



"locators":[



{



"type":"css",



"value":"input[type=\"email\"][name=\"email\"]:eq(0)"



},



{



"type":"dom",



"value":"document.forms[0][\"email\"]"



},



{



"type":"css",



"value":".inputfield:eq(0)"



},



{



"type":"css",



"value":"#content div div:nth-child(2) form:nth-child(9) input:nth-child(3)"



},



{



"type":"css",



"value":"#content div.section div.tile form.cta input.inputfield:eq(0)"



}



]



},



"textValue":"sample@sample.com",



"masked":false,



"simulateBlurEvent":true



},



{



"type":"click",



"description":"click on \"Start free trial\"",



"target":{



"locators":[



{



"type":"css",



"value":"input[type=\"submit\"]:eq(0)"



},



{



"type":"dom",



"value":"document.forms[0][19]"



},



{



"type":"css",



"value":".btn:eq(1)"



},



{



"type":"css",



"value":"#content div div:nth-child(2) form:nth-child(9) div:nth-child(22) input"



},



{



"type":"css",



"value":"#content div.section div.tile form.cta div.cta__formgroup input.btn:eq(0)"



}



]



},



"button":0,



"wait":{



"waitFor":"page_complete"



}



}



]



},



"locations": [



"GEOLOCATION-B69A5A40388CC698",



"GEOLOCATION-A9022AAFA0763F56"



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



"thresholds": []



}



},



"tags": [],



"managementZones": [



{



"id": "-7832237287622819191",



"name": "!!allSynthetic"



}



]



}
```

#### Код ответа

200

## Связанные темы

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать браузерный монитор одного URL, браузерный clickpath или HTTP-монитор.")
* [Script mode for browser monitor configuration](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/script-mode-for-browser-monitor-configuration "Создавайте или редактируйте браузерные мониторы в формате JSON.")
* [Script mode for HTTP monitor configuration](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/script-mode-for-http-monitor-configuration-classic "Создавайте или редактируйте HTTP-мониторы в формате JSON.")