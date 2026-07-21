---
title: Synthetic monitors API - PUT монитор
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/synthetic-monitors/put-a-monitor
scraped: 2026-05-12T11:59:48.035764
---

# Synthetic monitors API - PUT монитор

# Synthetic monitors API - PUT монитор

* Справочник
* Опубликовано 24 сентября 2018 г.

Обновляет указанный монитор.

Конфигурация монитора передаётся через его JSON-скрипт.

Можно скопировать скрипт существующего монитора и скорректировать его по необходимости.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/synthetic/monitors/{monitorId}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/synthetic/monitors/{monitorId}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `ExternalSyntheticIntegration`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Все вариации модели, зависящие от типа модели, смотрите в [JSON-моделях](/managed/dynatrace-api/environment-api/synthetic/synthetic-monitors/models "Узнайте о вариациях моделей в Synthetic monitors v1 API.").

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| monitorId | string | ID обновляемого синтетического монитора. | path | Обязательный |
| body | [SyntheticMonitorUpdate](#openapi-definition-SyntheticMonitorUpdate) | Обновление синтетического монитора.  Фактический набор полей зависит от типа монитора. Список фактических объектов смотрите в описании поля **type** или в [Synthetic monitors API - JSON-модели](https://dt-url.net/2523se9?dt=m). | body | Необязательный |

### Объекты тела запроса

#### Объект `SyntheticMonitorUpdate`

Обновление синтетического монитора.

Фактический набор полей зависит от типа монитора. Список фактических объектов смотрите в описании поля **type** или в [Synthetic monitors API - JSON-модели](https://dt-url.net/2523se9?dt=m).

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| anomalyDetection | [AnomalyDetection](#openapi-definition-AnomalyDetection) | Конфигурация обнаружения аномалий. | Необязательный |
| enabled | boolean | Монитор включён (`true`) или отключён (`false`). | Обязательный |
| frequencyMin | integer | Частота монитора, в минутах.  Можно использовать одно из следующих значений: `5`, `10`, `15`, `30` и `60`. | Обязательный |
| locations | string[] | Список локаций, с которых выполняется монитор.  Чтобы указать локацию, используйте её entity ID. Для публичных локаций используйте форму `GEOLOCATION-9999453BE4BDB3CD` и `SYNTHETIC_LOCATION-DF80ACFB688C583B` для приватных. | Обязательный |
| manuallyAssignedApps | string[] | Набор вручную назначенных приложений. | Обязательный |
| name | string | Имя монитора. | Обязательный |
| script | object | Скрипт [браузерного](https://dt-url.net/9c103rda?dt=m) или HTTP-монитора. | Обязательный |
| tags | [TagWithSourceInfo[]](#openapi-definition-TagWithSourceInfo) | Набор тегов, назначенных монитору.  Здесь можно указать только значение тега, а контекст `CONTEXTLESS` и источник 'USER' будут добавлены автоматически. Но предпочтительный вариант, это использование модели TagWithSourceDto. | Обязательный |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из объектов:  * `BROWSER` -> BrowserSyntheticMonitorUpdate * `HTTP` -> HttpSyntheticMonitorUpdate Поле может принимать значения: * `BROWSER` * `HTTP` | Обязательный |

#### Объект `AnomalyDetection`

Конфигурация обнаружения аномалий.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| loadingTimeThresholds | [LoadingTimeThresholdsPolicyDto](#openapi-definition-LoadingTimeThresholdsPolicyDto) | Конфигурация порогов производительности. | Необязательный |
| outageHandling | [OutageHandlingPolicy](#openapi-definition-OutageHandlingPolicy) | Конфигурация обработки недоступности. | Необязательный |

#### Объект `LoadingTimeThresholdsPolicyDto`

Конфигурация порогов производительности.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| enabled | boolean | Порог производительности включён (`true`) или отключён (`false`). | Обязательный |
| thresholds | [LoadingTimeThreshold[]](#openapi-definition-LoadingTimeThreshold) | Список правил порогов производительности. | Обязательный |

#### Объект `LoadingTimeThreshold`

Правило порога производительности.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| eventIndex | integer | Укажите событие, к которому применяется порог ACTION. | Необязательный |
| requestIndex | integer | Укажите запрос, к которому применяется порог ACTION. | Необязательный |
| type | string | Тип порога: общее время загрузки или время загрузки действия. Поле может принимать значения: * `ACTION` * `TOTAL` | Обязательный |
| valueMs | integer | Уведомлять, если загрузка монитора занимает больше *X* миллисекунд. | Обязательный |

#### Объект `OutageHandlingPolicy`

Конфигурация обработки недоступности.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| globalOutage | boolean | Когда включено (`true`), создавать проблему и отправлять алерт, когда монитор недоступен во всех настроенных локациях. | Обязательный |
| globalOutagePolicy | [GlobalOutagePolicy](#openapi-definition-GlobalOutagePolicy) | Конфигурация обработки глобальной недоступности. | Необязательный |
| localOutage | boolean | Когда включено (`true`), создавать проблему и отправлять алерт, когда монитор недоступен в течение одного или нескольких последовательных запусков в любой локации. | Обязательный |
| localOutagePolicy | [LocalOutagePolicy](#openapi-definition-LocalOutagePolicy) | Конфигурация обработки локальной недоступности.  Алерт, если **affectedLocations** локаций не могут получить доступ к веб-приложению **consecutiveRuns** раз подряд. | Обязательный |
| retryOnError | boolean | Запланировать повтор, если выполнение браузерного монитора завершается неудачей. Для HTTP-мониторов это свойство игнорируется. | Необязательный |

#### Объект `GlobalOutagePolicy`

Конфигурация обработки глобальной недоступности.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| consecutiveRuns | integer | Алерт, если все локации не могут получить доступ к веб-приложению *X* раз подряд. | Обязательный |

#### Объект `LocalOutagePolicy`

Конфигурация обработки локальной недоступности.

Алерт, если **affectedLocations** локаций не могут получить доступ к веб-приложению **consecutiveRuns** раз подряд.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| affectedLocations | integer | Число затронутых локаций для срабатывания алерта. | Обязательный |
| consecutiveRuns | integer | Число последовательных неудач для срабатывания алерта. | Обязательный |

#### Объект `TagWithSourceInfo`

Тег с источником сущности Dynatrace.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| context | string | Источник тега, например AWS или Cloud Foundry.  Пользовательские теги используют значение `CONTEXTLESS`. Поле может принимать значения: * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` | Обязательный |
| key | string | Ключ тега.  У пользовательских тегов здесь находится значение тега. | Обязательный |
| source | string | Источник тега, например USER, RULE\_BASED или AUTO Поле может принимать значения: * `AUTO` * `RULE_BASED` * `USER` | Необязательный |
| value | string | Значение тега.  Неприменимо к пользовательским тегам. | Необязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные поля. Её нужно скорректировать для использования в реальном запросе.

```
{



"anomalyDetection": {



"loadingTimeThresholds": {



"enabled": true,



"thresholds": [



{



"requestIndex": 1,



"type": "TOTAL",



"valueMs": 100



}



]



},



"outageHandling": {



"globalOutage": true,



"localOutage": true,



"localOutagePolicy": {



"affectedLocations": 1,



"consecutiveRuns": 3



}



}



},



"enabled": true,



"events": [],



"frequencyMin": 5,



"keyPerformanceMetrics": {



"loadActionKpm": "VISUALLY_COMPLETE",



"xhrActionKpm": "VISUALLY_COMPLETE"



},



"locations": [



"GEOLOCATION-9999453BE4BDB3CD",



"SYNTHETIC_LOCATION-DF80ACFB688C583B"



],



"manuallyAssignedApps": [



"APPLICATION-4ADF0EF407C7C545"



],



"name": "Browser Monitor Example",



"script": {



"configuration": {



"device": {



"deviceName": "Desktop",



"orientation": "landscape"



}



},



"events": [



{



"description": "Loading of \"example.com\"",



"type": "navigate",



"url": "http://example.com",



"wait": {



"waitFor": "page_complete"



}



}



],



"type": "availability",



"version": "1.0"



},



"tags": [



"example"



],



"type": "BROWSER"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Синтетический монитор обновлён. У ответа нет тела. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

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

В этом примере запрос обновляет монитор **dynatrace.com** из [примера GET monitor](/managed/dynatrace-api/environment-api/synthetic/synthetic-monitors/get-a-monitor#example "Просмотр синтетического монитора через Synthetic v1 API."), меняя список локаций, с которых он выполняется, и увеличивая частоту до **10 минут**.

API-токен передаётся в заголовке **Authorization**.

Поскольку тело запроса объёмное, в этом примере оно усечено в секции **Curl**. Полное тело смотрите в секции **Request body**. Можно скачать или скопировать пример тела запроса, чтобы попробовать его самостоятельно. Перед использованием убедитесь, что локация из примера доступна в вашем окружении. Список доступных локаций можно получить вызовом [**GET all synthetic locations**](/managed/dynatrace-api/environment-api/synthetic/synthetic-locations/get-all-locations "Получение списка всех синтетических локаций через Synthetic v1 API."). Если локация недоступна, замените её на любую используемую вами локацию.

#### Curl

```
curl -X PUT \



https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/monitors/SYNTHETIC_TEST-0000000000025434 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{<truncated - see the Request body section > }



'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/monitors/SYNTHETIC_TEST-0000000000025434
```

#### Тело запроса

```
{



"frequencyMin": 10,



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



"type": "browser",



"name": "dynatrace.com",



"locations": [



"GEOLOCATION-0A41430434C388A9",



"GEOLOCATION-95196F3C9A4F4215",



"GEOLOCATION-0DF9A0E1095A5A62"



],



"enabled": true,



"script": {



"type": "clickpath",



"version": "1.0",



"configuration": {



"device": {



"deviceName": "Desktop",



"orientation": "landscape"



}



},



"events": [



{



"type": "navigate",



"description": "Loading of \"http://www.dynatrace.com\"",



"url": "http://www.dynatrace.com",



"wait": {



"waitFor": "page_complete"



}



},



{



"type": "click",



"description": "click on \"Free trial\"",



"target": {



"locators": [



{



"type": "css",



"value": "a:contains(\"Free trial\"):eq(1)"



},



{



"type": "css",



"value": ".btn:eq(1)"



},



{



"type": "css",



"value": "#content div div div div div div div p:nth-child(3) a"



},



{



"type": "css",



"value": "#content div.homepage-hero-wrapper div.gallery div.flickity-viewport div.flickity-slider div.gallery-cell div.section div.column p.cta--row a.btn:eq(0)"



}



]



},



"button": 0,



"wait": {



"waitFor": "page_complete"



}



},



{



"type": "click",



"description": "click on \"email\"",



"target": {



"locators": [



{



"type": "css",



"value": "input[type=\"email\"][name=\"email\"]:eq(0)"



},



{



"type": "dom",



"value": "document.forms[0][\"email\"]"



},



{



"type": "css",



"value": ".inputfield:eq(0)"



},



{



"type": "css",



"value": "#content div div:nth-child(2) form:nth-child(9) input:nth-child(3)"



},



{



"type": "css",



"value": "#content div.section div.tile form.cta input.inputfield:eq(0)"



}



]



},



"button": 0



},



{



"type": "keystrokes",



"description": "keystrokes on \"email\"",



"target": {



"locators": [



{



"type": "css",



"value": "input[type=\"email\"][name=\"email\"]:eq(0)"



},



{



"type": "dom",



"value": "document.forms[0][\"email\"]"



},



{



"type": "css",



"value": ".inputfield:eq(0)"



},



{



"type": "css",



"value": "#content div div:nth-child(2) form:nth-child(9) input:nth-child(3)"



},



{



"type": "css",



"value": "#content div.section div.tile form.cta input.inputfield:eq(0)"



}



]



},



"textValue": "sample@sample.com",



"masked": false,



"simulateBlurEvent": true



},



{



"type": "click",



"description": "click on \"Start free trial\"",



"target": {



"locators": [



{



"type": "css",



"value": "input[type=\"submit\"]:eq(0)"



},



{



"type": "dom",



"value": "document.forms[0][19]"



},



{



"type": "css",



"value": ".btn:eq(1)"



},



{



"type": "css",



"value": "#content div div:nth-child(2) form:nth-child(9) div:nth-child(22) input"



},



{



"type": "css",



"value": "#content div.section div.tile form.cta div.cta__formgroup input.btn:eq(0)"



}



]



},



"button": 0,



"wait": {



"waitFor": "page_complete"



}



}



]



},



"tags": []



}
```

#### Код ответа

204

## Связанные темы

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать браузерный монитор одного URL, браузерный clickpath или HTTP-монитор.")
* [Script mode for browser monitor configuration](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/script-mode-for-browser-monitor-configuration "Создавайте или редактируйте браузерные мониторы в формате JSON.")
* [Script mode for HTTP monitor configuration](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/script-mode-for-http-monitor-configuration-classic "Создавайте или редактируйте HTTP-мониторы в формате JSON.")