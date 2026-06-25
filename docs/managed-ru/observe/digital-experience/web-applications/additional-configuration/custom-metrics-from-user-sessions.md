---
title: Создание пользовательских метрик USQL для веб-приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/custom-metrics-from-user-sessions
scraped: 2026-05-12T11:07:04.405394
---

# Создание пользовательских метрик USQL для веб-приложений

# Создание пользовательских метрик USQL для веб-приложений

* How-to guide
* 1-min read
* Updated on Feb 21, 2023

С помощью метрических событий USQL можно извлекать бизнес-KPI из данных пользовательских сессий и пользовательских действий и хранить эти метрики в виде временных рядов. Затем хранимые метрики можно использовать в [пользовательских графиках](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), [механизмах оповещения](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace") или [Metrics API](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

Метрические события USQL доступны в двух видах:

* **Метрические события пользовательских сессий**. Эти метрики сокращённо называются USCM и имеют префикс `uscm.`.
* **Метрические события пользовательских действий**. Эти метрики сокращённо называются UACM и начинаются с префикса `uacm.`.

Метрические события пользовательских действий доступны начиная с версии Dynatrace 1.260.

Метрические события USQL помогают ответить на такие вопросы, как:

* Как изменяется индекс пользовательского опыта для моего сайта с течением времени?
* Как изменяется индекс Apdex для определённого типа пользовательских действий?
* Как изменяется выручка, генерируемая пользователями, со временем?
* Сколько пользователей посещает мой сайт и какими браузерами они пользуются?
* Какова средняя продолжительность сессии для моего веб-приложения?
* Какова средняя длительность пользовательского действия для моего мобильного приложения?

Создавать метрическими событиями USQL и управлять ими можно через веб-интерфейс Dynatrace или [Settings API Dynatrace](#create-metrics-via-API).

## Настройка метрик через UI

Метрические события USQL можно создавать и управлять ими через веб-интерфейс Dynatrace.

![Страница метрических событий пользовательских сессий в веб-интерфейсе Dynatrace](https://dt-cdn.net/images/user-session-custom-metrics-page-2112-726ab6bf4a.png)

Страница метрических событий пользовательских сессий в веб-интерфейсе Dynatrace

1. Перейдите в **Settings** > **Web and mobile monitoring** > **User session metric events** или **User action metric events**.
2. Выберите **Add item**.
3. Введите **Metric key**, который будет использоваться при приёме метрики. Этот ключ понадобится при запросе данных метрики через [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

   * Для метрических событий пользовательских сессий ключ метрики должен начинаться с префикса `uscm.`.
   * Для метрических событий пользовательских действий ключ метрики должен начинаться с префикса `uacm.`.
4. В разделе **Value type to be extracted** выберите один из следующих вариантов.

   * Для метрических событий пользовательских сессий:

     + **User session counter** — для подсчёта количества пользовательских сессий (аналог `COUNT(*)` в [USQL](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.")).
     + **User session field value** — для извлечения значения поля пользовательской сессии. Также укажите **Field name**. Возможные значения см. в разделе [Значения для метрических событий пользовательских сессий](#values-uscm).
   * Для метрических событий пользовательских действий:

     + **User action counter** — для подсчёта количества пользовательских действий (аналог `COUNT(*)` в [USQL](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.")).
     + **User action field value** — для извлечения значения поля пользовательского действия. Также укажите **Field name**. Возможные значения см. в разделе [Значения для метрических событий пользовательских действий](#values-uacm).
5. В разделе **Add a dimension** укажите поля, которые должны использоваться как измерения. Возможные значения см. в разделах [Измерения для метрических событий пользовательских сессий](#dimensions-uscm) и [Измерения для метрических событий пользовательских действий](#dimensions-uacm).
6. В разделе **Add a filter** добавьте необходимые фильтры.

   * Введите **Field name**. Возможные значения см. в разделах [Фильтры для метрических событий пользовательских сессий](#filters-uscm) или [Фильтры для метрических событий пользовательских действий](#filters-uacm).
   * Выберите **Operator**.
   * Если выбран один из бинарных операторов (например, **equals** или **greater than**), укажите второй аргумент в поле **Value**.

![Создание пользовательской метрики пользовательских сессий](https://dt-cdn.net/images/creating-user-session-custom-metric-1359-e1cdae0345.png)

Создание пользовательской метрики пользовательских сессий

Также можно использовать [USQL](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data#convert-usql-into-custom-metrics "Learn how you can access and query user session data based on keywords, syntax, functions, and more.") для создания метрических событий USQL.

## Настройка метрик через API

Для настройки метрических событий USQL также можно использовать [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

1. [Создайте токен доступа](/managed/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") с разрешениями **Write settings** (`settings.write`) и **Read settings** (`settings.read`).
2. Используйте конечную точку [GET a schema](/managed/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") для получения требуемого формата JSON для публикации конфигурации.

   Пользовательская метрика пользовательских сессий

   Пользовательская метрика пользовательских действий

   Идентификатор схемы конфигурации метрики (`schemaId`) — `builtin:custom-metrics`.

   Пример JSON-payload с конфигурацией пользовательской метрики пользовательских сессий:

   ```
   [



   {



   "schemaVersion":"0.0.4",



   "schemaId":"builtin:custom-metrics",



   "scope":"tenant",



   "value":{



   "enabled":true,



   "metricKey":"uscm.sessions_by_browser_family_and_country_easytravel",



   "value":{



   "type":"COUNTER"



   },



   "dimensions":[



   "browserFamily",



   "country"



   ],



   "filters":[



   {



   "fieldName":"useraction.application",



   "operator":"EQUALS",



   "value":"www.easytravel.com"



   },



   {



   "fieldName":"userType",



   "operator":"EQUALS",



   "value":"REAL_USER"



   }



   ]



   }



   }



   ]
   ```

   Идентификатор схемы конфигурации метрики (`schemaId`) — `builtin:user-action-custom-metrics`.

   Пример JSON-payload с конфигурацией пользовательской метрики пользовательских действий:

   ```
   [



   {



   "schemaVersion":"1.0.0",



   "schemaId":"builtin:user-action-custom-metrics",



   "scope":"tenant",



   "value":{



   "enabled":true,



   "metricKey":"uacm.actions_by_type_and_country_easytravel",



   "value":{



   "type":"COUNTER"



   },



   "dimensions":[



   "type",



   "usersession.country"



   ],



   "filters":[



   {



   "fieldName":"application",



   "operator":"EQUALS",



   "value":"www.easytravel.com"



   },



   {



   "fieldName":"usersession.userType",



   "operator":"EQUALS",



   "value":"REAL_USER"



   }



   ]



   }



   }



   ]
   ```
3. Используйте конечную точку [POST an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") для отправки конфигурации.

В таблице ниже описаны все свойства конфигурации, необходимые для создания или обновления пользовательской метрики USQL через API.

| Свойство | Описание | Возможные значения |
| --- | --- | --- |
| `enabled` | Определяет, включена ли пользовательская метрика USQL. Установите значение `false` для временного отключения метрики. | `true` или `false` |
| `metricKey` | Ключ метрики, используемый при её приёме. Этот ключ понадобится при запросе данных метрики через [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."). * Для метрических событий пользовательских сессий ключ метрики должен начинаться с префикса `uscm.`. * Для метрических событий пользовательских действий ключ метрики должен начинаться с префикса `uacm.`. |  |
| `value` | Источник значения метрики. |  |
| `value.type` | * Для подсчёта количества пользовательских сессий или действий (аналог `COUNT(*)` в [USQL](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.")) установите значение `COUNTER`. * Для извлечения значения поля пользовательской сессии или действия установите значение `FIELD`. | `COUNTER` или `FIELD` |
| `value.fieldName` | Если `value.type`=`FIELD`, указывает имя поля пользовательской сессии или действия. | См. разделы [Значения для USCM](#values-uscm) и [Значения для UACM](#values-uacm). |
| `dimensions` | Перечисляет поля, используемые как измерения. | См. разделы [Измерения для USCM](#dimensions-uscm) и [Измерения для UACM](#dimensions-uacm). |
| `filters` | Задаёт фильтры. |  |
| `filter.fieldName` | Указывает имя поля фильтра. | См. разделы [Фильтры для USCM](#filters-uscm) и [Фильтры для UACM](#filters-uacm). |
| `filter.operator` | Указывает оператор. | `EQUALS`, `NOT_EQUAL`, `IS_NULL`, `IS_NOT_NULL`, `LIKE`, `LESS_THAN`, `LESS_THAN_OR_EQUAL_TO`, `GREATER_THAN`, `GREATER_THAN_OR_EQUAL_TO` |
| `filter.value` | Предоставляет второй аргумент для бинарных операторов (например, `EQUALS` или `GREATER_THAN`). |  |

## Поддерживаемые значения, измерения и фильтры

В следующих разделах приведены списки поддерживаемых значений, измерений и фильтров для метрических событий пользовательских сессий.

Значения для метрических событий пользовательских сессий

* В качестве значения поддерживаются только поля пользовательских сессий. Поля пользовательских действий не поддерживаются.
* Все имена полей должны соответствовать именам полей USQL.
* Префикс `usersession.` в имени поля необязателен. Например, `usersession.duration` и `duration` означают одно и то же.
* Когда настроенное поле содержит `null`, метрика игнорируется, но Dynatrace использует самомониторинг для выявления таких случаев.

#### Поля пользовательских сессий, поддерживаемые как значения

`duration`
`numberOfRageClicks`
`numberOfRageTaps`
`totalErrorCount`
`totalLicenseCreditCount`
`userActionCount`
`longProperties.*`[1](#fn-1-1-def)
`doubleProperties.*`[1](#fn-1-1-def)

1

Любое пользовательское свойство типа long или double, например `longProperties.outerwidth` или `doubleProperties.revenue`

Измерения для метрических событий пользовательских сессий

* В качестве измерений поддерживаются как поля пользовательских сессий, так и поля пользовательских действий. Поля пользовательских действий поддерживаются начиная с Dynatrace версии 1.234.
* Все имена полей должны соответствовать именам полей USQL.
* Для имени поля пользовательской сессии префикс `usersession.` необязателен. Например, `usersession.country` и `country` означают одно и то же. При приёме метрики префикс `usersession.` отбрасывается, например `usersession.country` становится `country`.
* Для имени поля пользовательского действия префикс `useraction.` обязателен. При приёме метрики префикс `useraction.` сохраняется.
* Можно добавить до 10 измерений для одной пользовательской метрики пользовательских сессий.
* Когда поле, настроенное как измерение, содержит `null`, Dynatrace использует строку `null` в качестве значения измерения.
* При использовании `useraction.application` в качестве измерения, если пользовательская сессия охватывает несколько приложений, значение пользовательской метрики сессии фиксируется для каждого приложения. Чтобы избежать двойного счёта, разделите метрику по приложению.

#### Поля пользовательских сессий, поддерживаемые как измерения

`appVersion`
`applicationType`
`bounce`
`browserFamily`
`browserMajorVersion`
`browserType`
`carrier`
`region`
`continent`
`country`
`connectionType`
`device`
`displayResolution`
`endReason`
`hasCrash`
`hasError`
`hasSessionReplay`
`manufacturer`
`networkTechnology`
`newUser`
`osFamily`
`osVersion`
`reasonForNoSessionReplay`
`reasonForNoSessionReplayMobile`
`rootedOrJailbroken`
`screenHeight`
`screenOrientation`
`screenWidth`
`userExperienceScore`
`userType`
`stringProperties.*`[1](#fn-2-1-def)

1

Любое пользовательское строковое свойство, например `stringProperties.author`. Используйте поля с низкой кардинальностью, чтобы не создавать слишком много значений измерений.

#### Поля пользовательских действий, поддерживаемые как измерения

`useraction.application`[1](#fn-3-1-def)

1

Поддерживается начиная с Dynatrace версии 1.234

Фильтры для метрических событий пользовательских сессий

* В качестве фильтров поддерживаются как поля пользовательских сессий, так и поля пользовательских действий.
* Все имена полей должны соответствовать именам полей USQL.
* Для имени поля пользовательской сессии префикс `usersession.` необязателен.
* Для имени поля пользовательского действия префикс `useraction.` обязателен.
* При добавлении нескольких фильтров все они должны совпадать — фильтры объединяются оператором `AND`.
* Фильтры, использующие поле пользовательского действия, требуют совпадения хотя бы одного пользовательского действия. Пользовательские действия сопоставляются оператором `ANY`.
* Для одной пользовательской метрики пользовательских сессий можно задать до 10 фильтров.

#### Поля пользовательских сессий, поддерживаемые как фильтры

`appVersion`, `applicationType`, `bounce`, `browserFamily`, `browserMajorVersion`, `browserMonitorName`, `browserType`, `carrier`, `city`, `region`, `continent`, `country`, `connectionType`, `device`, `displayResolution`, `duration`, `endReason`, `hasCrash`, `hasError`, `hasSessionReplay`, `ip`, `isp`, `manufacturer`, `networkTechnology`, `newUser`, `numberOfRageClicks`, `osFamily`, `osVersion`, `reasonForNoSessionReplay`, `reasonForNoSessionReplayMobile`, `rootedOrJailbroken`, `screenHeight`, `screenOrientation`, `screenWidth`, `totalErrorCount`, `totalLicenseCreditCount`, `userActionCount`, `userExperienceScore`, `userId`, `userType`, `longProperties.*`, `doubleProperties.*`, `stringProperties.*`

#### Поля пользовательских действий, поддерживаемые как поля

`useraction.apdexCategory`, `useraction.application`, `useraction.cdnBusyTime`, `useraction.cdnResources`, `useraction.customErrorCount`, `useraction.domCompleteTime`, `useraction.domContentLoadedTime`, `useraction.documentInteractiveTime`, `useraction.domain`, `useraction.duration`, `useraction.firstInputDelay`, `useraction.firstPartyBusyTime`, `useraction.firstPartyResources`, `useraction.frontendTime`, `useraction.hasCrash`, `useraction.internalApplicationId`, `useraction.internalKeyUserActionId`, `useraction.javascriptErrorCount`, `useraction.keyUserAction`, `useraction.largestContentfulPaint`, `useraction.name`, `useraction.networkTime`, `useraction.requestErrorCount`, `useraction.serverTime`, `useraction.speedIndex`, `useraction.targetUrl`, `useraction.thirdPartyBusyTime`, `useraction.thirdPartyResources`, `useraction.type`, `useraction.visuallyCompleteTime`

Развернув разделы ниже, можно ознакомиться с поддерживаемыми значениями, измерениями и фильтрами для метрических событий пользовательских действий.

Значения для метрических событий пользовательских действий

* В качестве значений поддерживаются как поля пользовательских сессий, так и поля пользовательских действий.
* Все имена полей должны соответствовать именам полей USQL.
* Для полей пользовательских действий префикс `useraction.` необязателен.
* Для полей пользовательских сессий префикс `usersession.` обязателен.
* Когда настроенное поле содержит `null`, метрика игнорируется, но Dynatrace использует самомониторинг для выявления таких случаев.

#### Поля пользовательских действий, поддерживаемые как значения

`speedIndex`, `duration`, `networkTime`, `serverTime`, `frontendTime`, `documentInteractiveTime`, `firstPartyResources`, `firstPartyBusyTime`, `thirdPartyResources`, `thirdPartyBusyTime`, `cdnResources`, `cdnBusyTime`, `domCompleteTime`, `domContentLoadedTime`, `loadEventStart`, `loadEventEnd`, `visuallyCompleteTime`, `requestStart`, `responseStart`, `responseEnd`, `userActionPropertyCount`, `customErrorCount`, `javascriptErrorCount`, `requestErrorCount`, `largestContentfulPaint`, `firstInputDelay`, `totalBlockingTime` (устаревшее), `cumulativeLayoutShift`, `longProperties.*`, `doubleProperties.*`

#### Поля пользовательских сессий, поддерживаемые как значения

`usersession.duration`, `usersession.numberOfRageClicks`, `usersession.numberOfRageTaps`, `usersession.totalErrorCount`, `usersession.totalLicenseCreditCount`, `usersession.userActionCount`, `usersession.longProperties.*`, `usersession.doubleProperties.*`

Измерения для метрических событий пользовательских действий

* Поддерживаются как поля пользовательских сессий, так и поля пользовательских действий.
* Все имена полей должны соответствовать именам полей USQL.
* Для полей пользовательских действий префикс `useraction.` необязателен. При приёме метрики префикс `useraction.` отбрасывается.
* Для полей пользовательских сессий префикс `usersession.` обязателен. При приёме метрики префикс `usersession.` сохраняется.
* Для одной пользовательской метрики пользовательских действий можно указать до 4 измерений, но не более 2 из них могут быть высококардинальными.
* Когда поле, настроенное как измерение, содержит `null`, Dynatrace использует строку `null` в качестве значения измерения.
* В приведённом ниже списке высококардинальные измерения выделены **жирным шрифтом**.

#### Поля пользовательских действий, поддерживаемые как измерения

`application`, `hasCrash`, `type`, `apdexCategory`, `internalApplicationId`, `internalKeyUserActionId`, `keyUserAction`, `isEntryAction`, `isExitAction`, **`stringProperties.*`**

#### Поля пользовательских сессий, поддерживаемые как измерения

**`usersession.appVersion`**, `usersession.applicationType`, `usersession.bounce`, **`usersession.browserFamily`**, **`usersession.browserMajorVersion`**, **`usersession.browserType`**, **`usersession.carrier`**, **`usersession.region`**, `usersession.continent`, `usersession.country`, `usersession.connectionType`, **`usersession.device`**, **`usersession.displayResolution`**, `usersession.endReason`, `usersession.hasCrash`, `usersession.hasError`, `usersession.hasSessionReplay`, **`usersession.manufacturer`**, **`usersession.networkTechnology`**, `usersession.newUser`, **`usersession.osFamily`**, **`usersession.osVersion`**, `usersession.reasonForNoSessionReplay`, `usersession.reasonForNoSessionReplayMobile`, `usersession.rootedOrJailbroken`, **`usersession.screenHeight`**, `usersession.screenOrientation`, **`usersession.screenWidth`**, `usersession.userExperienceScore`, `usersession.userType`, **`usersession.stringProperties.*`**

Фильтры для метрических событий пользовательских действий

* В качестве фильтров поддерживаются как поля пользовательских сессий, так и поля пользовательских действий.
* Все имена полей должны соответствовать именам полей USQL.
* Для полей пользовательских действий префикс `useraction.` необязателен.
* Для полей пользовательских сессий префикс `usersession.` обязателен.
* При добавлении нескольких фильтров все они должны совпадать — фильтры объединяются оператором `AND`.
* Для одной пользовательской метрики пользовательских действий можно задать до 10 фильтров.

#### Поля пользовательских действий, поддерживаемые как фильтры

`apdexCategory`, `application`, `cdnBusyTime`, `cdnResources`, `customErrorCount`, `cumulativeLayoutShift`, `domCompleteTime`, `domContentLoadedTime`, `documentInteractiveTime`, `domain`, `duration`, `firstInputDelay`, `firstPartyBusyTime`, `firstPartyResources`, `frontendTime`, `hasCrash`, `internalApplicationId`, `internalKeyUserActionId`, `isEntryAction`, `isExitAction`, `javascriptErrorCount`, `keyUserAction`, `largestContentfulPaint`, `loadEventStart`, `loadEventEnd`, `name`, `networkTime`, `requestErrorCount`, `requestStart`, `responseStart`, `responseEnd`, `serverTime`, `speedIndex`, `targetUrl`, `thirdPartyBusyTime`, `thirdPartyResources`, `totalBlockingTime` (устаревшее), `type`, `userActionPropertyCount`, `visuallyCompleteTime`, `syntheticEvent`, `longProperties.*`, `doubleProperties.*`, `stringProperties.*`

#### Поля пользовательских сессий, поддерживаемые как фильтры

`usersession.appVersion`, `usersession.applicationType`, `usersession.bounce`, `usersession.browserFamily`, `usersession.browserMajorVersion`, `usersession.browserMonitorName`, `usersession.browserType`, `usersession.carrier`, `usersession.city`, `usersession.region`, `usersession.continent`, `usersession.country`, `usersession.connectionType`, `usersession.device`, `usersession.displayResolution`, `usersession.duration`, `usersession.endReason`, `usersession.hasCrash`, `usersession.hasError`, `usersession.hasSessionReplay`, `usersession.ip`, `usersession.isp`, `usersession.manufacturer`, `usersession.networkTechnology`, `usersession.newUser`, `usersession.numberOfRageClicks`, `usersession.numberOfRageTaps`, `usersession.osFamily`, `usersession.osVersion`, `usersession.reasonForNoSessionReplay`, `usersession.reasonForNoSessionReplayMobile`, `usersession.rootedOrJailbroken`, `usersession.screenHeight`, `usersession.screenOrientation`, `usersession.screenWidth`, `usersession.totalErrorCount`, `usersession.totalLicenseCreditCount`, `usersession.userActionCount`, `usersession.userExperienceScore`, `usersession.userId`, `usersession.userType`, `usersession.longProperties.*`, `usersession.doubleProperties.*`, `usersession.stringProperties.*`

## Известные ограничения

Для метрических событий USQL выявлены следующие ограничения:

* Можно создать до 500 пользовательских метрик пользовательских сессий на среду.
* Можно создать до 100 пользовательских метрик пользовательских действий на среду.
* Данные синтетических пользовательских сессий не учитываются в значениях метрических событий USQL; включаются только данные реальных пользователей.
* Dynatrace обновляет метрические события USQL при каждом закрытии сессии. Это означает, что данные активных сессий не учитываются в значениях пользовательских метрик USQL; включаются только данные закрытых сессий.
* Ключевое слово `DISTINCT`, используемое в [USQL](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more."), не поддерживается. Например, для запроса типа `SELECT COUNT(DISTINCT country) from usersession` создать эквивалентную пользовательскую метрику USQL невозможно.

## Учебное руководство

Для лучшего понимания работы метрических событий USQL ниже приведено руководство для метрических событий пользовательских сессий.

![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Создание метрики**

![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Создание и закрепление графика**

![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Создание оповещения**

Используя веб-интерфейс Dynatrace, создадим пользовательскую метрику пользовательских сессий (USCM) **Average session duration** на основе данных сессий реальных пользователей. Метрика будет включать два измерения для сегментации данных сессий по семейству браузера и его основной версии. На основе этой метрики создадим график, закрепим его на дашборде и создадим пользовательское событие для получения оповещений при превышении метрикой заданного порогового значения.

Создание метрики

1. Перейдите в **Settings** > **Web and mobile monitoring** > **User session metric events**.
2. Выберите **Add item**.
3. Введите `uscm.average_duration_of_sessions_by_browser_family_and_version` в поле **Metric key**.
4. В разделе **Value type to be extracted** выберите **User session field value**. Также задайте **Field name** равным `duration`.
5. Выберите **Add dimension** и добавьте измерения `browserMajorVersion` и `browserFamily`.
6. В разделе **Add a filter** добавьте следующие фильтры:

   * `userType` = `REAL_USER` (**Field name** — `userType`, **Operator** — `equals`, **Value** — `REAL_USER`)
   * `useraction.application` = `www.easytravel.com` (**Field name** — `useraction.application`, **Operator** — `equals`, **Value** — `www.easytravel.com`). Вместо `www.easytravel.com` можно использовать имя вашего приложения.
7. Выберите **Save changes**.

![Создание пользовательской метрики пользовательских сессий](https://dt-cdn.net/images/create-custom-metric-example-1910-e74ff5a09d.png)

Создание пользовательской метрики пользовательских сессий

Теперь имеется пользовательская метрика пользовательских сессий, которая извлекается как поле (`duration`) только при условии, что `useraction.application` равно `www.easytravel.com` (фильтрация по конкретному приложению) и `userType` — `REAL_USER` (фильтрация только по реальным пользователям). Кроме того, добавлены два измерения для разбивки данных по семейству браузера или его основной версии.

После получения данных пользовательских сессий и заполнения метрики можно построить по ней график, закрепить его на дашборде и даже создать оповещение на основе метрики.

Создание и закрепление графика

Теперь создадим график на основе метрики `uscm.average_duration_of_sessions_by_browser_family_and_version` и закрепим его на одном из дашбордов.

1. Перейдите в **Data Explorer**.
2. Выберите метрику `uscm.average_duration_of_sessions_by_browser_family_and_version` и нажмите **Run query**.

   ![Создание графика в Data Explorer на основе метрики пользовательских сессий](https://dt-cdn.net/images/data-explorer-custom-metric-1221-7d8891ede4.png)

   Создание графика в Data Explorer на основе метрики пользовательских сессий
3. Используя [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), разбейте собранные данные для просмотра данных пользовательских сессий по `browserMajorVersion`, `browserFamily` или по обоим измерениям.
4. Отфильтруйте данные пользовательских сессий по `browserMajorVersion` или `browserFamily`, чтобы сосредоточиться на интересующих данных.
5. После создания графика с данными можно закрепить его на классическом дашборде: выберите **Pin to dashboard**, укажите дашборд и введите название тайла.

![График пользовательской метрики, закреплённый на дашборде](https://dt-cdn.net/images/dashboard-custom-metric-944-005355f3e5.png)

График пользовательской метрики, закреплённый на дашборде

Создание оповещения

В завершение примера создадим оповещение на основе метрических событий пользовательских сессий.

Чтобы создать оповещение:

1. Перейдите в **Settings** > **Anomaly detection** > **Metric events**.
2. Выберите **Add metric event**.
3. Создайте метрическое событие на основе метрики `uscm.average_duration_of_sessions_by_browser_family_and_version`. Подробнее см. раздел [Metric events](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace").

![Создание пользовательского события оповещения на основе метрики пользовательских сессий](https://dt-cdn.net/images/create-custom-events-for-alerting-2092-9b1d66309a.png)

Создание пользовательского события оповещения на основе метрики пользовательских сессий

## Вопросы и ответы

Данные пользовательских сессий видны, но данные метрических событий USQL не отображаются в Data Explorer.

Убедитесь, что пользовательская сессия не является активной. Dynatrace извлекает и сохраняет данные метрик в виде временных рядов только после закрытия пользовательской сессии.

Почему метрические события USQL активных сессий не отображаются в Data Explorer?

По мере закрытия сессий в приложениях они помещаются в очередь для последующей обработки. Ряд фоновых процессов извлекает данные метрик из пользовательских сессий для подготовки данных к приёму метрик.

Почему результаты USQL-запросов не совпадают с метрическими событиями USQL?

Данные синтетических пользовательских сессий не учитываются в метрических событиях USQL.

Исключите синтетические сессии из запроса. Также проверьте, что для запроса и метрики применяется одинаковый временной диапазон.

Как оплачиваются метрические события USQL?

Начиная с Dynatrace 1.232, метрические события USQL подпадают под [лицензирование единиц данных Davis (DDU)](/managed/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU)."). Эти метрики оплачиваются как обычные бесхемные метрики.

Для оценки стоимости метрики анализируются сессии за последние 7 дней и рассчитывается стоимость в DDU в соответствии с ожидаемым потоком приёма в минуту. Подробнее см. раздел [Как рассчитывается потребление DDU для метрических событий?](/managed/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation#calculation-details "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").

Каков интервал детализации для метрических событий USQL?

Сохранение метрических данных в Dynatrace следует стратегии хранения данных, которая агрегирует метрики с течением времени. Стратегия хранения, применяемая к метрическим событиям USQL, идентична стратегии, используемой для встроенных метрик временных рядов.

Подробнее см. раздел [Сроки хранения данных > Метрики](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods#metrics-classic "Check retention times for various data types.")

## Связанные темы

* [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.")