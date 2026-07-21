---
title: Создание пользовательских метрик USQL для веб-приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/custom-metrics-from-user-sessions
---

# Создание пользовательских метрик USQL для веб-приложений в RUM Classic

# Создание пользовательских метрик USQL для веб-приложений в RUM Classic

* Практическое руководство
* Чтение 1 минута
* Обновлено 21 февр. 2023 г.

С помощью metric events USQL можно извлекать бизнес-метрики KPI из данных пользовательских сессий и пользовательских действий и сохранять эти метрики как временные ряды. Затем сохранённые метрики можно использовать в [пользовательских графиках](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), [механизмах оповещения](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace") или [Metrics API](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

Metric events USQL доступны как:

* **Metric events пользовательских сессий**. Эти метрики сокращённо называются USCM и имеют префикс `uscm.`.
* **Metric events пользовательских действий**. Эти метрики сокращённо называются UACM и начинаются с префикса `uacm.`.

Metric events пользовательских действий доступны начиная с версии Dynatrace 1.260.

Metric events USQL помогают отвечать на такие вопросы:

* Как меняется индекс пользовательского опыта для моего сайта со временем?
* Как меняется индекс Apdex для определённого типа пользовательских действий со временем?
* Как меняется доход, генерируемый пользователями, со временем?
* Сколько пользователей заходит на сайт и какими браузерами они пользуются?
* Какова средняя продолжительность сессии для веб-приложения?
* Какова средняя продолжительность пользовательского действия для мобильного приложения?

Создавать metric events USQL и управлять ими можно либо через веб-интерфейс Dynatrace, либо через [Dynatrace Settings API](#create-metrics-via-API).

## Настройка метрик через интерфейс

Создавать metric events USQL и управлять ими можно через веб-интерфейс Dynatrace.

![Страница metric events пользовательских сессий в веб-интерфейсе Dynatrace](https://dt-cdn.net/images/user-session-custom-metrics-page-2112-726ab6bf4a.png)

Страница metric events пользовательских сессий в веб-интерфейсе Dynatrace

1. Перейти в **Settings** > **Web and mobile monitoring** > **User session metric events** или **User action metric events**.
2. Выбрать **Add item**.
3. Ввести **Metric key**, который будет использоваться при получении метрики. Этот ключ понадобится при запросе данных метрики через [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

   * Для metric events пользовательских сессий ключ метрики должен начинаться с префикса `uscm.`.
   * Для metric events пользовательских действий ключ метрики должен начинаться с префикса `uacm.`.
4. В разделе **Value type to be extracted** выбрать один из следующих вариантов.

   * Для metric events пользовательских сессий:

     + **User session counter**, чтобы подсчитывать количество пользовательских сессий, что аналогично `COUNT(*)` при использовании [USQL](/managed/observe/digital-experience/rum-classic/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.").
     + **User session field value**, чтобы извлечь значение поля пользовательской сессии. Также нужно указать **Field name**. Возможные значения см. в [Значения для metric events пользовательских сессий](#values-uscm).
   * Для metric events пользовательских действий:

     + **User action counter**, чтобы подсчитывать количество пользовательских действий, что аналогично `COUNT(*)` при использовании [USQL](/managed/observe/digital-experience/rum-classic/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.").
     + **User action field value**, чтобы извлечь значение поля пользовательского действия. Также нужно указать **Field name**. Возможные значения см. в [Значения для metric events пользовательских действий](#values-uacm).
5. В разделе **Add a dimension** указать поля, которые нужно использовать как измерения. Возможные значения см. в [Измерения для metric events пользовательских сессий](#dimensions-uscm) и [Измерения для metric events пользовательских действий](#dimensions-uacm).
6. В разделе **Add a filter** добавить нужные фильтры.

   * Ввести **Field name**. Возможные значения см. в [Фильтры для metric events пользовательских сессий](#filters-uscm) или [Фильтры для metric events пользовательских действий](#filters-uacm).
   * Выбрать **Operator**.
   * Если выбран один из бинарных операторов, например **equals** или **greater than**, также указать второй аргумент в текстовом поле **Value**.

![Создание пользовательской метрики пользовательской сессии](https://dt-cdn.net/images/creating-user-session-custom-metric-1359-e1cdae0345.png)

Создание пользовательской метрики пользовательской сессии

Также можно создавать metric events USQL с помощью [USQL](/managed/observe/digital-experience/rum-classic/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data#convert-usql-into-custom-metrics "Learn how you can access and query user session data based on keywords, syntax, functions, and more.").

## Настройка метрик через API

Настроить metric events USQL можно также с помощью [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

1. [Создать токен доступа](/managed/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") с правами **Write settings** (`settings.write`) и **Read settings** (`settings.read`).
2. Использовать конечную точку [GET a schema](/managed/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API."), чтобы узнать формат JSON, необходимый для отправки конфигурации.

   User session custom metric

   User action custom metric

   Идентификатор схемы конфигурации метрики (`schemaId`), это `builtin:custom-metrics`.

   Пример полезной нагрузки JSON с конфигурацией пользовательской метрики пользовательской сессии:

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

   Идентификатор схемы конфигурации метрики (`schemaId`), это `builtin:user-action-custom-metrics`.

   Пример полезной нагрузки JSON с конфигурацией пользовательской метрики пользовательского действия:

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
3. Использовать конечную точку [POST an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API."), чтобы отправить конфигурацию.

В таблице ниже описаны все свойства конфигурации, необходимые для создания или обновления пользовательской метрики USQL через API.

| Свойство | Описание | Возможные значения |
| --- | --- | --- |
| `enabled` | Определяет, включена ли пользовательская метрика USQL. Установить `false`, чтобы временно отключить метрику. | `true` или `false` |
| `metricKey` | Ключ метрики, используемый при получении метрики. Этот ключ нужно использовать при запросе данных метрики через [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").  * Для metric events пользовательских сессий ключ метрики должен начинаться с префикса `uscm.`. * Для metric events пользовательских действий ключ метрики должен начинаться с префикса `uacm.`. |  |
| `value` | Источник значения метрики. |  |
| `value.type` | * Чтобы подсчитывать количество пользовательских сессий или пользовательских действий, что аналогично `COUNT(*)` при использовании [USQL](/managed/observe/digital-experience/rum-classic/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more."), установить `COUNTER`. * Чтобы извлечь значение поля пользовательской сессии или пользовательского действия, установить `FIELD`. | `COUNTER` или `FIELD` |
| `value.fieldName` | Если `value.type`=`FIELD`, указывает имя поля пользовательской сессии или пользовательского действия. | См. [Значения для metric events пользовательских сессий](#values-uscm) и [Значения для metric events пользовательских действий](#values-uacm). |
| `dimensions` | Перечисляет поля, используемые как измерения. | См. [Измерения для metric events пользовательских сессий](#dimensions-uscm) и [Измерения для metric events пользовательских действий](#dimensions-uacm). |
| `filters` | Задаёт фильтры. |  |
| `filter.fieldName` | Задаёт имя поля фильтра. | См. [Фильтры для metric events пользовательских сессий](#filters-uscm) и [Фильтры для metric events пользовательских действий](#filters-uacm). |
| `filter.operator` | Задаёт оператор. | `EQUALS`, `NOT_EQUAL`, `IS_NULL`, `IS_NOT_NULL`, `LIKE`, `LESS_THAN`, `LESS_THAN_OR_EQUAL_TO`, `GREATER_THAN`, `GREATER_THAN_OR_EQUAL_TO` |
| `filter.value` | Указывает второй аргумент для бинарных операторов (таких как `EQUALS` или `GREATER_THAN`). |  |

## Поддерживаемые значения, измерения и фильтры

Проверьте разделы ниже, чтобы посмотреть списки поддерживаемых значений, измерений и фильтров для событий метрик пользовательских сессий.

Значения для событий метрик пользовательских сессий

* В качестве значения поддерживаются только поля пользовательской сессии. Поля пользовательского действия в качестве значения не поддерживаются.
* Все имена полей должны совпадать с именами полей USQL.
* Префикс `usersession.` в имени поля необязателен. Например, `usersession.duration` и `duration` означают одно и то же.
* Если настроенное поле содержит `null`, метрика игнорируется, но Dynatrace использует самомониторинг для выявления таких случаев.

#### Поля пользовательской сессии, поддерживаемые как значения

`duration`  
`numberOfRageClicks`  
`numberOfRageTaps`  
`totalErrorCount`  
`totalLicenseCreditCount`  
`userActionCount`  
`longProperties.*`[1](#fn-1-1-def)  
`doubleProperties.*`[1](#fn-1-1-def)

1

Любое пользовательское свойство типа long или double, например, `longProperties.outerwidth` или `doubleProperties.revenue`

Измерения для событий метрик пользовательских сессий

* В качестве измерений поддерживаются как поля пользовательской сессии, так и поля пользовательского действия. Поля пользовательского действия поддерживаются начиная с версии Dynatrace 1.234.
* Все имена полей должны совпадать с именами полей USQL.
* Для имени поля пользовательской сессии префикс `usersession.` необязателен. Например, `usersession.country` и `country` означают одно и то же. При приёме метрики префикс `usersession.` отбрасывается, например, `usersession.country` становится `country`.
* Для имени поля пользовательского действия префикс `useraction.` обязателен. При приёме метрики префикс `useraction.` сохраняется.
* К одной пользовательской метрике сессии можно добавить до 10 измерений.
* Если поле, настроенное как измерение, содержит `null`, Dynatrace использует строку `null` как значение измерения.
* При использовании `useraction.application` в качестве измерения, если пользовательская сессия охватывает несколько приложений, значение пользовательской метрики сессии записывается для каждого приложения. Чтобы избежать двойного учёта значения, разбейте метрику по приложению.

#### Поля пользовательской сессии, поддерживаемые как измерения

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

Любое пользовательское строковое свойство, например, `stringProperties.author`. Используйте поля с низкой кардинальностью, чтобы не создавать слишком много значений измерения.

#### Поля пользовательского действия, поддерживаемые как измерения

`useraction.application`[1](#fn-3-1-def)

1

Поддерживается начиная с версии Dynatrace 1.234

Фильтры для событий метрик пользовательских сессий

* В качестве фильтров поддерживаются как поля пользовательской сессии, так и поля пользовательского действия.
* Все имена полей должны совпадать с именами полей USQL.
* Для имени поля пользовательской сессии префикс `usersession.` необязателен. Например, `usersession.country` и `country` означают одно и то же.
* Для имени поля пользовательского действия префикс `useraction.` обязателен.
* При добавлении нескольких фильтров все они должны совпадать: фильтры объединяются с помощью `AND`.
* Фильтры, использующие поле пользовательского действия, требуют совпадения хотя бы одного пользовательского действия. Пользовательские действия сопоставляются с помощью `ANY`.
* Для одной пользовательской метрики сессии можно задать до 10 фильтров.

#### Поля пользовательской сессии, поддерживаемые как фильтры

`appVersion`  
`applicationType`  
`bounce`  
`browserFamily`  
`browserMajorVersion`  
`browserMonitorName`  
`browserType`  
`carrier`  
`city`  
`region`  
`continent`  
`country`  
`connectionType`  
`device`  
`displayResolution`  
`duration`  
`endReason`  
`hasCrash`  
`hasError`  
`hasSessionReplay`  
`ip`  
`isp`  
`manufacturer`  
`networkTechnology`  
`newUser`  
`numberOfRageClicks`  
`osFamily`  
`osVersion`  
`reasonForNoSessionReplay`  
`reasonForNoSessionReplayMobile`  
`rootedOrJailbroken`  
`screenHeight`  
`screenOrientation`  
`screenWidth`  
`totalErrorCount`  
`totalLicenseCreditCount`  
`userActionCount`  
`userExperienceScore`  
`userId`  
`userType`  
`longProperties.*`[1](#fn-4-1-def)  
`doubleProperties.*`[1](#fn-4-1-def)  
`stringProperties.*`[1](#fn-4-1-def)

1

Любое пользовательское свойство типа long, double или string, например, `longProperties.outerwidth`, `doubleProperties.revenue` или `stringProperties.author`

#### Поля пользовательского действия, поддерживаемые как поля

`useraction.apdexCategory`  
`useraction.application`  
`useraction.cdnBusyTime`  
`useraction.cdnResources`  
`useraction.customErrorCount`  
`useraction.domCompleteTime`  
`useraction.domContentLoadedTime`  
`useraction.documentInteractiveTime`  
`useraction.domain`  
`useraction.duration`  
`useraction.firstInputDelay`  
`useraction.firstPartyBusyTime`  
`useraction.firstPartyResources`  
`useraction.frontendTime`  
`useraction.hasCrash`  
`useraction.internalApplicationId`  
`useraction.internalKeyUserActionId`  
`useraction.javascriptErrorCount`  
`useraction.keyUserAction`  
`useraction.largestContentfulPaint`  
`useraction.name`  
`useraction.networkTime`  
`useraction.requestErrorCount`  
`useraction.serverTime`  
`useraction.speedIndex`  
`useraction.targetUrl`  
`useraction.thirdPartyBusyTime`  
`useraction.thirdPartyResources`  
`useraction.type`  
`useraction.visuallyCompleteTime`

Разверните разделы ниже, чтобы изучить поддерживаемые значения, измерения и фильтры для событий метрик пользовательских действий.

Значения для событий метрик пользовательских действий

* В качестве значений поддерживаются как поля пользовательской сессии, так и поля пользовательского действия.
* Все имена полей должны совпадать с именами полей USQL.
* Для полей пользовательского действия префикс `useraction.` необязателен. Например, `useraction.type` и `type` означают одно и то же.
* Для полей пользовательской сессии префикс `usersession.` обязателен.
* Если настроенное поле содержит `null`, метрика игнорируется, но Dynatrace использует самомониторинг для выявления таких случаев.

#### Поля пользовательского действия, поддерживаемые как значения

`speedIndex`  
`duration`  
`networkTime`  
`serverTime`  
`frontendTime`  
`documentInteractiveTime`  
`firstPartyResources`  
`firstPartyBusyTime`  
`thirdPartyResources`  
`thirdPartyBusyTime`  
`cdnResources`  
`cdnBusyTime`  
`domCompleteTime`  
`domContentLoadedTime`  
`loadEventStart`  
`loadEventEnd`  
`visuallyCompleteTime`  
`requestStart`  
`responseStart`  
`responseEnd`  
`userActionPropertyCount`  
`customErrorCount`  
`javascriptErrorCount`  
`requestErrorCount`  
`largestContentfulPaint`  
`firstInputDelay`  
`totalBlockingTime` Устарело  
`cumulativeLayoutShift`  
`longProperties.*`[1](#fn-5-1-def)  
`doubleProperties.*`[1](#fn-5-1-def)

1

Любое пользовательское свойство типа long или double

#### Поля пользовательской сессии, поддерживаемые как значения

`usersession.duration`  
`usersession.numberOfRageClicks`  
`usersession.numberOfRageTaps`  
`usersession.totalErrorCount`  
`usersession.totalLicenseCreditCount`  
`usersession.userActionCount`  
`usersession.longProperties.*`[1](#fn-6-1-def)  
`usersession.doubleProperties.*`[1](#fn-6-1-def)

1

Любое пользовательское свойство типа long или double, например, `usersession.longProperties.outerwidth` или `usersession.doubleProperties.revenue`

Измерения для событий метрик пользовательских действий

* Поддерживаются как поля пользовательской сессии, так и поля пользовательского действия.
* Все имена полей должны совпадать с именами полей USQL.
* Для полей пользовательского действия префикс `useraction.` необязателен. Например, `useraction.type` и `type` означают одно и то же. При приёме метрики префикс `useraction.` отбрасывается, например, `useraction.type` становится `type`.
* Для полей пользовательской сессии префикс `usersession.` обязателен. При приёме метрики префикс `usersession.` сохраняется.
* Для пользовательской метрики действия можно указать до 4 измерений, но только 2 из них могут быть измерениями с высокой кардинальностью.
* Если поле, настроенное как измерение, содержит `null`, Dynatrace использует строку `null` как значение измерения.
* В списке ниже измерения, выделенные жирным шрифтом, это измерения с высокой кардинальностью.

#### Поля пользовательского действия, поддерживаемые как измерения

`application`  
`hasCrash`  
`type`  
`apdexCategory`  
`internalApplicationId`  
`internalKeyUserActionId`  
`keyUserAction`  
`isEntryAction`  
`isExitAction`  
**`stringProperties.*`**[1](#fn-7-1-def)

1

Любое пользовательское строковое свойство. Используйте поля с низкой кардинальностью, чтобы не создавать слишком много значений измерения.

#### Поля пользовательской сессии, поддерживаемые как измерения

**`usersession.appVersion`**  
`usersession.applicationType`  
`usersession.bounce`  
**`usersession.browserFamily`**  
**`usersession.browserMajorVersion`**  
**`usersession.browserType`**  
**`usersession.carrier`**  
**`usersession.region`**  
`usersession.continent`  
`usersession.country`  
`usersession.connectionType`  
**`usersession.device`**  
**`usersession.displayResolution`**  
`usersession.endReason`  
`usersession.hasCrash`  
`usersession.hasError`  
`usersession.hasSessionReplay`  
**`usersession.manufacturer`**  
**`usersession.networkTechnology`**  
`usersession.newUser`  
**`usersession.osFamily`**  
**`usersession.osVersion`**  
`usersession.reasonForNoSessionReplay`  
`usersession.reasonForNoSessionReplayMobile`  
`usersession.rootedOrJailbroken`  
**`usersession.screenHeight`**  
`usersession.screenOrientation`  
**`usersession.screenWidth`**  
`usersession.userExperienceScore`  
`usersession.userType`  
**`usersession.stringProperties.*`**[1](#fn-8-1-def)

1

Любое пользовательское строковое свойство, например, `usersession.stringProperties.author`. Используйте поля с низкой кардинальностью, чтобы не создавать слишком много значений измерения.

Фильтры для событий метрик пользовательских действий

* Поддерживаются фильтры как по полям user session, так и по полям user action.
* Все имена полей должны совпадать с именами полей USQL.
* Для полей user action префикс `useraction.` необязателен. Например, `useraction.type` и `type` означают одно и то же.
* Для полей user session префикс `usersession.` обязателен.
* При добавлении нескольких фильтров должны совпадать все они, фильтры объединяются через `AND`.
* Для одной пользовательской метрики user action можно задать до 10 фильтров.

#### Поля user action, поддерживаемые в качестве фильтров

`apdexCategory`  
`application`  
`cdnBusyTime`  
`cdnResources`  
`customErrorCount`  
`cumulativeLayoutShift`  
`domCompleteTime`  
`domContentLoadedTime`  
`documentInteractiveTime`  
`domain`  
`duration`  
`firstInputDelay`  
`firstPartyBusyTime`  
`firstPartyResources`  
`frontendTime`  
`hasCrash`  
`internalApplicationId`  
`internalKeyUserActionId`  
`isEntryAction`  
`isExitAction`  
`javascriptErrorCount`  
`keyUserAction`  
`largestContentfulPaint`  
`loadEventStart`  
`loadEventEnd`  
`name`  
`networkTime`  
`requestErrorCount`  
`requestStart`  
`responseStart`  
`responseEnd`  
`serverTime`  
`speedIndex`  
`targetUrl`  
`thirdPartyBusyTime`  
`thirdPartyResources`  
`totalBlockingTime` Устарело  
`type`  
`userActionPropertyCount`  
`visuallyCompleteTime`  
`syntheticEvent`  
`longProperties.*`[1](#fn-9-1-def)  
`doubleProperties.*`[1](#fn-9-1-def)  
`stringProperties.*`[1](#fn-9-1-def)

1

Любое пользовательское свойство типа long, double или string

#### Поля user session, поддерживаемые в качестве фильтров

`usersession.appVersion`  
`usersession.applicationType`  
`usersession.bounce`  
`usersession.browserFamily`  
`usersession.browserMajorVersion`  
`usersession.browserMonitorName`  
`usersession.browserType`  
`usersession.carrier`  
`usersession.city`  
`usersession.region`  
`usersession.continent`  
`usersession.country`  
`usersession.connectionType`  
`usersession.device`  
`usersession.displayResolution`  
`usersession.duration`  
`usersession.endReason`  
`usersession.hasCrash`  
`usersession.hasError`  
`usersession.hasSessionReplay`  
`usersession.ip`  
`usersession.isp`  
`usersession.manufacturer`  
`usersession.networkTechnology`  
`usersession.newUser`  
`usersession.numberOfRageClicks`  
`usersession.numberOfRageTaps`  
`usersession.osFamily`  
`usersession.osVersion`  
`usersession.reasonForNoSessionReplay`  
`usersession.reasonForNoSessionReplayMobile`  
`usersession.rootedOrJailbroken`  
`usersession.screenHeight`  
`usersession.screenOrientation`  
`usersession.screenWidth`  
`usersession.totalErrorCount`  
`usersession.totalLicenseCreditCount`  
`usersession.userActionCount`  
`usersession.userExperienceScore`  
`usersession.userId`  
`usersession.userType`  
`usersession.longProperties.*`[1](#fn-10-1-def)  
`usersession.doubleProperties.*`[1](#fn-10-1-def)  
`usersession.stringProperties.*`[1](#fn-10-1-def)

1

Любое пользовательское свойство типа long, double или string, например `usersession.longProperties.outerwidth`, `usersession.doubleProperties.revenue` или `usersession.stringProperties.author`

## Известные ограничения

Мы выявили следующие ограничения для метрических событий USQL:

* Можно создать до 500 пользовательских метрик сессий на среду.
* Можно создать до 100 пользовательских метрик действий пользователя на среду.

* Синтетические данные пользовательских сессий не учитываются в значениях метрических событий USQL, включаются только данные реальных пользователей.
* Dynatrace обновляет метрические события USQL при каждом закрытии сессии. Это означает, что данные живой сессии не учитываются в значениях пользовательских метрик USQL, включаются только данные закрытых сессий.
* Ключевое слово `DISTINCT`, используемое в [USQL](/managed/observe/digital-experience/rum-classic/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more."), не поддерживается. Если есть запрос вида `SELECT COUNT(DISTINCT country) from usersession`, создать эквивалентную пользовательскую метрику USQL невозможно.

## Учебное руководство

Чтобы лучше понять, как работают метрические события USQL, можно пройти учебное руководство по метрическим событиям пользовательских сессий ниже.

![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Создание метрики**

![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Создание и закрепление графика**

![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Создание оповещения**

Используя веб-интерфейс Dynatrace, создадим пользовательскую метрику сессий (USCM) **Average session duration** на основе данных сессий реальных пользователей. Метрика будет включать два измерения для сегментации данных сессий по семейству браузера и основной версии браузера. С помощью этой метрики затем создадим график, закрепим график на дашборде и создадим пользовательское событие для метрики, чтобы получать оповещения при превышении значением метрики заданного порога.

Создание метрики

1. Перейти в **Settings** > **Web and mobile monitoring** > **User session metric events**.
2. Выбрать **Add item**.
3. Ввести `uscm.average_duration_of_sessions_by_browser_family_and_version` в поле **Metric key**.
4. В разделе **Value type to be extracted** выбрать **User session field value**. Также задать **Field name** равным `duration`.
5. Выбрать **Add dimension** и добавить измерения `browserMajorVersion` и `browserFamily`.
6. В разделе **Add a filter** добавить следующие фильтры:

   * `userType` = `REAL_USER` (**Field name** это `userType`, **Operator** это `equals`, а **Value** это `REAL_USER`)
   * `useraction.application` = `www.easytravel.com` (**Field name** это `useraction.application`, **Operator** это `equals`, а **Value** это `www.easytravel.com`). Вместо значения `www.easytravel.com` можно использовать название собственного приложения.
7. Выбрать **Save changes**.

![Creating a user session custom metric](https://dt-cdn.net/images/create-custom-metric-example-1910-e74ff5a09d.png)

Создание пользовательской метрики сессии

Теперь есть пользовательская метрика сессии, которая извлекается как поле (`duration`) только когда `useraction.application` равно `www.easytravel.com` (фильтрация по конкретному приложению) и `userType` равно `REAL_USER` (фильтрация только реальных пользователей). Кроме того, добавлены два измерения, позволяющие разбивать данные по семейству браузера или основной версии браузера.

После получения данных пользовательских сессий и заполнения метрики можно построить график по этой метрике, закрепить график на дашборде и даже создать оповещение на основе метрики.

Создание и закрепление графика

Теперь создадим график на основе метрики `uscm.average_duration_of_sessions_by_browser_family_and_version` и закрепим этот график на одном из дашбордов.

1. Перейти в **Data Explorer**.
2. Выбрать метрику `uscm.average_duration_of_sessions_by_browser_family_and_version` и выбрать **Run query**.

   ![Creating a chart in Data Explorer based on user sessions metric](https://dt-cdn.net/images/data-explorer-custom-metric-1221-7d8891ede4.png)

   Создание графика в Data Explorer на основе метрики пользовательских сессий
3. С помощью [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") разбить собранные данные, чтобы увидеть данные пользовательских сессий с разбивкой по `browserMajorVersion`, `browserFamily` или обоим измерениям.
4. Отфильтровать данные пользовательских сессий по `browserMajorVersion` или `browserFamily`, чтобы сосредоточиться на интересующих данных пользовательских сессий.
5. После создания графика с данными его можно закрепить на классическом дашборде: выбрать **Pin to dashboard**, выбрать один из дашбордов и ввести название плитки.

![Custom metric chart pinned to the dashboard](https://dt-cdn.net/images/dashboard-custom-metric-944-005355f3e5.png)

График пользовательской метрики, закреплённый на дашборде

Создание оповещения

В качестве последней части этого примера создадим оповещение на основе метрических событий пользовательских сессий.

Чтобы создать оповещение

1. Перейти в **Settings** > **Anomaly detection** > **Metric events**.
2. Выбрать **Add metric event**.
3. Создать метрическое событие на основе метрики `uscm.average_duration_of_sessions_by_browser_family_and_version`. Подробнее см. [Metric events](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace").

![Creating a custom event for alerting based on a user sessions metric](https://dt-cdn.net/images/create-custom-events-for-alerting-2092-9b1d66309a.png)

Создание пользовательского события для оповещения на основе метрики пользовательских сессий

## Частые вопросы

Данные пользовательской сессии видны, но данные метрических событий USQL в Data Explorer не отображаются.

Нужно убедиться, что пользовательская сессия не является активной (live). Dynatrace извлекает и сохраняет данные метрики во временные ряды только после закрытия пользовательской сессии.

Почему метрические события USQL активных сессий не отображаются в Data Explorer?

По мере закрытия сессий в приложениях они помещаются в очередь для последующей обработки. Затем ряд фоновых обработчиков извлекает данные метрик из пользовательских сессий для подготовки данных к приёму метрик.

Почему результаты запроса USQL не совпадают с метрическими событиями USQL?

Синтетические данные пользовательских сессий не учитываются в метрических событиях USQL.

Нужно исключить синтетические сессии из запроса. Также стоит проверить, что к запросу и метрике применён один и тот же временной диапазон.

Как оплачиваются метрические события USQL?

Начиная с Dynatrace 1.232, метрические события USQL подпадают под [лицензирование по единицам данных Davis (DDU)](/managed/license/classic-licensing/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU)."). Эти метрики оплачиваются как обычные бессхемные метрики (schemaless).

Чтобы оценить стоимость по метрике, оцениваются сессии за последние 7 дней и рассчитывается стоимость в DDU на метрику согласно ожидаемому объёму приёма данных в минуту. Подробнее см. [How do we calculate DDU consumption for metric events?](/managed/license/classic-licensing/davis-data-units/metric-cost-calculation#calculation-details "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").

Какова гранулярность интервала для метрических событий USQL?

Хранение данных метрик Dynatrace следует стратегии хранения данных, которая агрегирует метрики с течением времени. Стратегия хранения данных, применяемая к метрическим событиям USQL, идентична стратегии хранения данных, используемой для встроенных метрик временных рядов.

Подробнее см. [Data retention periods > Metrics](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods#metrics-classic "Review default and configurable retention periods for service, RUM Classic, synthetic, Log Monitoring, metric, diagnostic, and security data in Dynatrace Managed.")

## Похожие темы

* [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.")