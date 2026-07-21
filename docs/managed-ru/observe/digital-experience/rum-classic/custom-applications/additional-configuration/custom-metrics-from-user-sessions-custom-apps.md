---
title: Создание пользовательских метрик USQL для пользовательских приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/custom-metrics-from-user-sessions-custom-apps
---

# Создание пользовательских метрик USQL для пользовательских приложений в RUM Classic

# Создание пользовательских метрик USQL для пользовательских приложений в RUM Classic

* Практическое руководство
* Чтение за 1 минуту
* Обновлено 21 февраля 2023 г.

С помощью событий метрик USQL можно извлекать бизнес-метрики KPI из данных пользовательских сессий и пользовательских действий и сохранять эти метрики в виде временных рядов. Затем сохранённые метрики можно использовать в [пользовательских графиках](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), [механизмах оповещения](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace") или [Metrics API](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

События метрик USQL доступны в виде:

* **Событий метрик пользовательских сессий**. Эти метрики сокращённо называются USCM и имеют префикс `uscm.`.
* **Событий метрик пользовательских действий**. Эти метрики сокращённо называются UACM и начинаются с префикса `uacm.`.

События метрик пользовательских действий доступны начиная с версии Dynatrace 1.260.

События метрик USQL помогают ответить на такие вопросы:

* Как меняется со временем индекс пользовательского опыта для сайта?
* Как меняется со временем индекс Apdex для определённого типа пользовательских действий?
* Как меняется со временем доход, генерируемый пользователями?
* Сколько пользователей заходят на сайт и какими браузерами они пользуются?
* Какова средняя продолжительность сессии для веб-приложения?
* Какова средняя продолжительность пользовательского действия для мобильного приложения?

Создавать события метрик USQL и управлять ими можно через веб-интерфейс Dynatrace или через [Dynatrace Settings API](#create-metrics-via-API).

## Настройка метрик через интерфейс

Создавать события метрик USQL и управлять ими можно через веб-интерфейс Dynatrace.

![Страница событий метрик пользовательских сессий в веб-интерфейсе Dynatrace](https://dt-cdn.net/images/user-session-custom-metrics-page-2112-726ab6bf4a.png)

Страница событий метрик пользовательских сессий в веб-интерфейсе Dynatrace

1. Перейти в **Settings** > **Web and mobile monitoring** > **User session metric events** или **User action metric events**.
2. Выбрать **Add item**.
3. Ввести **Metric key**, который будет использоваться при получении метрики. Этот ключ применяется при запросе данных метрики через [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

   * Для событий метрик пользовательских сессий ключ метрики должен начинаться с префикса `uscm.`.
   * Для событий метрик пользовательских действий ключ метрики должен начинаться с префикса `uacm.`.
4. В разделе **Value type to be extracted** выбрать один из следующих вариантов.

   * Для событий метрик пользовательских сессий:

     + **User session counter**, чтобы подсчитывать количество пользовательских сессий, что аналогично `COUNT(*)` при использовании [USQL](/managed/observe/digital-experience/rum-classic/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.").
     + **User session field value**, чтобы извлечь значение поля пользовательской сессии. Также нужно указать **Field name**. Возможные значения см. в разделе [Значения для событий метрик пользовательских сессий](#values-uscm).
   * Для событий метрик пользовательских действий:

     + **User action counter**, чтобы подсчитывать количество пользовательских действий, что аналогично `COUNT(*)` при использовании [USQL](/managed/observe/digital-experience/rum-classic/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.").
     + **User action field value**, чтобы извлечь значение поля пользовательского действия. Также нужно указать **Field name**. Возможные значения см. в разделе [Значения для событий метрик пользовательских действий](#values-uacm).
5. В разделе **Add a dimension** указать поля, которые должны использоваться как измерения. Возможные значения см. в разделах [Измерения для событий метрик пользовательских сессий](#dimensions-uscm) и [Измерения для событий метрик пользовательских действий](#dimensions-uacm).
6. В разделе **Add a filter** добавить нужные фильтры.

   * Ввести **Field name**. Возможные значения см. в разделах [Фильтры для событий метрик пользовательских сессий](#filters-uscm) или [Фильтры для событий метрик пользовательских действий](#filters-uacm).
   * Выбрать **Operator**.
   * Если выбран один из бинарных операторов, например **equals** или **greater than**, также указать второй аргумент в текстовом поле **Value**.

![Создание пользовательской метрики пользовательской сессии](https://dt-cdn.net/images/creating-user-session-custom-metric-1359-e1cdae0345.png)

Создание пользовательской метрики пользовательской сессии

Также для создания событий метрик USQL можно использовать [USQL](/managed/observe/digital-experience/rum-classic/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data#convert-usql-into-custom-metrics "Learn how you can access and query user session data based on keywords, syntax, functions, and more.").

## Настройка метрик через API

Для настройки событий метрик USQL также можно использовать [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

1. [Создать токен доступа](/managed/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") с правами **Write settings** (`settings.write`) и **Read settings** (`settings.read`).
2. Использовать эндпоинт [GET a schema](/managed/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API."), чтобы узнать формат JSON, требуемый для отправки конфигурации.

   Пользовательская метрика пользовательской сессии

   Пользовательская метрика пользовательского действия

   Идентификатор схемы конфигурации метрики (`schemaId`), это `builtin:custom-metrics`.

   Ниже приведён пример полезной нагрузки JSON с конфигурацией пользовательской метрики пользовательской сессии:

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

   Ниже приведён пример полезной нагрузки JSON с конфигурацией пользовательской метрики пользовательского действия:

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
3. Использовать эндпоинт [POST an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API."), чтобы отправить конфигурацию.

В таблице ниже описаны все свойства конфигурации, необходимые для создания или обновления пользовательской метрики USQL через API.

| Свойство | Описание | Возможные значения |
| --- | --- | --- |
| `enabled` | Определяет, включена пользовательская метрика USQL или нет. Установить в `false`, чтобы временно отключить метрику. | `true` или `false` |
| `metricKey` | Ключ метрики, используемый при получении метрики. Этот ключ применяется при запросе данных метрики через [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").  * Для событий метрик пользовательских сессий ключ метрики должен начинаться с префикса `uscm.`. * Для событий метрик пользовательских действий ключ метрики должен начинаться с префикса `uacm.`. |  |
| `value` | Источник значения метрики. |  |
| `value.type` | * Чтобы подсчитывать количество пользовательских сессий или пользовательских действий, что аналогично `COUNT(*)` при использовании [USQL](/managed/observe/digital-experience/rum-classic/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more."), установить значение `COUNTER`. * Чтобы извлечь значение поля пользовательской сессии или пользовательского действия, установить значение `FIELD`. | `COUNTER` или `FIELD` |
| `value.fieldName` | Если `value.type`=`FIELD`, указывает имя поля пользовательской сессии или пользовательского действия. | См. [Значения для событий метрик пользовательских сессий](#values-uscm) и [Значения для событий метрик пользовательских действий](#values-uacm). |
| `dimensions` | Перечисляет поля, используемые как измерения. | См. [Измерения для событий метрик пользовательских сессий](#dimensions-uscm) и [Измерения для событий метрик пользовательских действий](#dimensions-uacm). |
| `filters` | Задаёт фильтры. |  |
| `filter.fieldName` | Указывает имя поля фильтра. | См. [Фильтры для событий метрик пользовательских сессий](#filters-uscm) и [Фильтры для событий метрик пользовательских действий](#filters-uacm). |
| `filter.operator` | Указывает оператор. | `EQUALS`, `NOT_EQUAL`, `IS_NULL`, `IS_NOT_NULL`, `LIKE`, `LESS_THAN`, `LESS_THAN_OR_EQUAL_TO`, `GREATER_THAN`, `GREATER_THAN_OR_EQUAL_TO` |
| `filter.value` | Задаёт второй аргумент для бинарных операторов (таких как `EQUALS` или `GREATER_THAN`). |  |

## Поддерживаемые значения, измерения и фильтры

Ниже приведены разделы со списками поддерживаемых значений, измерений и фильтров для метрических событий пользовательских сессий.

Значения для метрических событий пользовательских сессий

* В качестве значения поддерживаются только поля пользовательской сессии. Поля пользовательского действия в качестве значения не поддерживаются.
* Все имена полей должны совпадать с именами полей USQL.
* Префикс `usersession.` в имени поля необязателен. Например, `usersession.duration` и `duration` означают одно и то же.
* Если настроенное поле содержит `null`, метрика игнорируется, но Dynatrace использует самомониторинг для выявления таких случаев.

#### Поля пользовательской сессии, поддерживаемые в качестве значений

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

* В качестве измерений поддерживаются как поля пользовательской сессии, так и поля пользовательского действия. Поля пользовательского действия поддерживаются начиная с версии Dynatrace 1.234.
* Все имена полей должны совпадать с именами полей USQL.
* Для имени поля пользовательской сессии префикс `usersession.` необязателен. Например, `usersession.country` и `country` означают одно и то же. При приёме метрики префикс `usersession.` отбрасывается, например, `usersession.country` становится `country`.
* Для имени поля пользовательского действия префикс `useraction.` обязателен. При приёме метрики префикс `useraction.` сохраняется.
* К одной пользовательской метрике сессии можно добавить до 10 измерений.
* Если поле, настроенное как измерение, содержит `null`, Dynatrace использует строку `null` в качестве значения измерения.
* При использовании `useraction.application` в качестве измерения, если пользовательская сессия охватывает несколько приложений, значение пользовательской метрики сессии фиксируется для каждого приложения. Чтобы избежать двойного учёта значения, нужно разбить метрику по приложению.

#### Поля пользовательской сессии, поддерживаемые в качестве измерений

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

Любое пользовательское строковое свойство, например `stringProperties.author`. Нужно использовать поля с низкой кардинальностью, чтобы не создавать слишком много значений измерения.

#### Поля пользовательского действия, поддерживаемые в качестве измерений

`useraction.application`[1](#fn-3-1-def)

1

Поддерживается начиная с версии Dynatrace 1.234

Фильтры для метрических событий пользовательских сессий

* В качестве фильтров поддерживаются как поля пользовательской сессии, так и поля пользовательского действия.
* Все имена полей должны совпадать с именами полей USQL.
* Для имени поля пользовательской сессии префикс `usersession.` необязателен. Например, `usersession.country` и `country` означают одно и то же.
* Для имени поля пользовательского действия префикс `useraction.` обязателен.
* При добавлении нескольких фильтров все они должны совпасть: фильтры объединяются с помощью `AND`.
* Фильтры, использующие поле пользовательского действия, требуют совпадения хотя бы одного пользовательского действия. Пользовательские действия сопоставляются с помощью `ANY`.
* Для одной пользовательской метрики сессии можно настроить до 10 фильтров.

#### Поля пользовательской сессии, поддерживаемые в качестве фильтров

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

Любое пользовательское свойство типа long, double или string, например `longProperties.outerwidth`, `doubleProperties.revenue` или `stringProperties.author`

#### Поля пользовательского действия, поддерживаемые в качестве полей

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

Раскрой разделы ниже, чтобы посмотреть поддерживаемые значения, измерения и фильтры для метрических событий пользовательского действия.

Значения для метрических событий пользовательского действия

* В качестве значений поддерживаются как поля пользовательской сессии, так и поля пользовательского действия.
* Все имена полей должны совпадать с именами полей USQL.
* Для полей пользовательского действия префикс `useraction.` необязателен. Например, `useraction.type` и `type` означают одно и то же.
* Для полей пользовательской сессии префикс `usersession.` обязателен.
* Если настроенное поле содержит `null`, метрика игнорируется, но Dynatrace использует самомониторинг для выявления таких случаев.

#### Поля пользовательского действия, поддерживаемые в качестве значений

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

#### Поля пользовательской сессии, поддерживаемые в качестве значений

`usersession.duration`  
`usersession.numberOfRageClicks`  
`usersession.numberOfRageTaps`  
`usersession.totalErrorCount`  
`usersession.totalLicenseCreditCount`  
`usersession.userActionCount`  
`usersession.longProperties.*`[1](#fn-6-1-def)  
`usersession.doubleProperties.*`[1](#fn-6-1-def)

1

Любое пользовательское свойство типа long или double, например `usersession.longProperties.outerwidth` или `usersession.doubleProperties.revenue`

Измерения для метрических событий пользовательского действия

* Поддерживаются как поля пользовательской сессии, так и поля пользовательского действия.
* Все имена полей должны совпадать с именами полей USQL.
* Для полей пользовательского действия префикс `useraction.` необязателен. Например, `useraction.type` и `type` означают одно и то же. При приёме метрики префикс `useraction.` отбрасывается, например, `useraction.type` становится `type`.
* Для полей пользовательской сессии префикс `usersession.` обязателен. При приёме метрики префикс `usersession.` сохраняется.
* Для пользовательской метрики действия можно указать до 4 измерений, но только 2 из них могут быть измерениями с высокой кардинальностью.
* Если поле, настроенное как измерение, содержит `null`, Dynatrace использует строку `null` в качестве значения измерения.
* В списке ниже измерения, выделенные жирным, это измерения с высокой кардинальностью.

#### Поля пользовательского действия, поддерживаемые в качестве измерений

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

Любое пользовательское строковое свойство. Нужно использовать поля с низкой кардинальностью, чтобы не создавать слишком много значений измерения.

#### Поля пользовательской сессии, поддерживаемые в качестве измерений

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

Любое пользовательское строковое свойство, например `usersession.stringProperties.author`. Нужно использовать поля с низкой кардинальностью, чтобы не создавать слишком много значений измерения.

Фильтры для метрических событий пользовательского действия

* И поля пользовательской сессии, и поля пользовательского действия поддерживаются в качестве фильтров.
* Все названия полей должны совпадать с названиями полей USQL.
* Для полей пользовательского действия префикс `useraction.` необязателен. Например, `useraction.type` и `type` означают одно и то же.
* Для полей пользовательской сессии префикс `usersession.` обязателен.
* При добавлении нескольких фильтров все они должны совпадать: фильтры комбинируются через `AND`.
* Для одной пользовательской метрики действия можно задать до 10 фильтров.

#### Поля пользовательского действия, поддерживаемые в качестве фильтров

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

#### Поля пользовательской сессии, поддерживаемые в качестве фильтров

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

Мы выявили следующие ограничения USQL metric events:

* Можно создать до 500 пользовательских метрик сессий (custom metrics) на среду.
* Можно создать до 100 пользовательских метрик действий (custom metrics) на среду.

* Данные синтетических сессий пользователей не учитываются в значениях USQL metric events, учитываются только данные реальных пользователей.
* Dynatrace обновляет USQL metric events при каждом закрытии сессии. Это значит, что данные текущей (live) сессии не учитываются в значениях пользовательских метрик USQL, учитываются только данные закрытых сессий.
* Ключевое слово `DISTINCT`, используемое в [USQL](/managed/observe/digital-experience/rum-classic/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more."), не поддерживается. Если есть запрос вида `SELECT COUNT(DISTINCT country) from usersession`, создать эквивалентную пользовательскую метрику USQL нельзя.

## Руководство

Чтобы лучше понять, как работают USQL metric events, можно пройти руководство по метрикам событий сессий пользователей ниже.

![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Создание метрики**

![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Создание и закрепление графика**

![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Создание оповещения**

Используя веб-интерфейс Dynatrace, создадим пользовательскую метрику сессии (USCM) **Average session duration** на основе данных сессий реальных пользователей. Метрика будет включать два измерения для сегментации данных сессий по семейству браузера и основной версии браузера. Используя эту метрику, затем создадим для неё график, закрепим график на дашборде и создадим пользовательское событие для метрики, чтобы можно было получать оповещения при превышении значением метрики заданного порога.

Создание метрики

1. Перейти в **Settings** > **Web and mobile monitoring** > **User session metric events**.
2. Выбрать **Add item**.
3. Ввести `uscm.average_duration_of_sessions_by_browser_family_and_version` в качестве **Metric key**.
4. В разделе **Value type to be extracted** выбрать **User session field value**. Также установить **Field name** равным `duration`.
5. Выбрать **Add dimension** и добавить измерения `browserMajorVersion` и `browserFamily`.
6. В разделе **Add a filter** включить следующие фильтры:

   * `userType` = `REAL_USER` (**Field name** это `userType`, **Operator** это `equals`, **Value** это `REAL_USER`)
   * `useraction.application` = `www.easytravel.com` (**Field name** это `useraction.application`, **Operator** это `equals`, **Value** это `www.easytravel.com`). Вместо значения `www.easytravel.com` можно использовать имя собственного приложения.
7. Выбрать **Save changes**.

![Creating a user session custom metric](https://dt-cdn.net/images/create-custom-metric-example-1910-e74ff5a09d.png)

Создание пользовательской метрики сессии

Теперь есть пользовательская метрика сессии, которая извлекается как поле (`duration`) только когда `useraction.application` равно `www.easytravel.com` (фильтрация по конкретному приложению) и `userType` это `REAL_USER` (фильтрация только по реальным пользователям). Кроме того, добавлены два измерения, которые позволяют разбивать данные по семейству браузера или основной версии браузера.

После получения данных сессий пользователей и заполнения метрики можно строить по ней график, закреплять график на дашборде и даже создавать оповещение на основе метрики.

Создание и закрепление графика

Теперь создадим график на основе метрики `uscm.average_duration_of_sessions_by_browser_family_and_version` и закрепим его на одном из дашбордов.

1. Перейти в **Data Explorer**.
2. Выбрать метрику `uscm.average_duration_of_sessions_by_browser_family_and_version` и выбрать **Run query**.

   ![Creating a chart in Data Explorer based on user sessions metric](https://dt-cdn.net/images/data-explorer-custom-metric-1221-7d8891ede4.png)

   Создание графика в Data Explorer на основе метрики сессий пользователей
3. Используя [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), разбить собранные данные, чтобы увидеть данные сессий пользователей, разделённые по `browserMajorVersion`, `browserFamily` или обоим измерениям.
4. Отфильтровать данные сессий пользователей по `browserMajorVersion` или `browserFamily`, чтобы сосредоточиться на интересующих данных сессий пользователей.
5. После создания графика, представляющего данные, можно закрепить график на классическом дашборде: выбрать **Pin to dashboard**, выбрать один из дашбордов и ввести имя плитки.

![Custom metric chart pinned to the dashboard](https://dt-cdn.net/images/dashboard-custom-metric-944-005355f3e5.png)

График пользовательской метрики, закреплённый на дашборде

Создание оповещения

В качестве последней части этого примера создадим оповещение на основе metric events сессий пользователей.

Чтобы создать оповещение

1. Перейти в **Settings** > **Anomaly detection** > **Metric events**.
2. Выбрать **Add metric event**.
3. Создать metric event на основе метрики `uscm.average_duration_of_sessions_by_browser_family_and_version`. Подробнее см. [Metric events](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace").

![Creating a custom event for alerting based on a user sessions metric](https://dt-cdn.net/images/create-custom-events-for-alerting-2092-9b1d66309a.png)

Создание пользовательского события для оповещений на основе метрики сессий пользователей

## Часто задаваемые вопросы

Данные сессий пользователей видны, но данные USQL metric events в Data Explorer не отображаются.

Нужно убедиться, что сессия пользователя не является текущей (live). Dynatrace извлекает и сохраняет данные метрики во временные ряды только после закрытия сессии пользователя.

Почему USQL metric events текущих (live) сессий не отображаются в Data Explorer?

Когда сессии в приложениях закрываются, они помещаются в очередь для последующей обработки. Затем ряд фоновых обработчиков извлекает данные метрик из сессий пользователей для подготовки данных к приёму метрик.

Почему результаты моего USQL-запроса не совпадают с USQL metric events?

Данные синтетических сессий пользователей не учитываются в USQL metric events.

Нужно исключить синтетические сессии из запроса. Также нужно проверить, что к запросу и метрике применён один и тот же временной диапазон.

Как оплачиваются USQL metric events?

Начиная с Dynatrace 1.232, USQL metric events подпадают под [лицензирование Davis data unit (DDU)](/managed/license/classic-licensing/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU)."). Эти метрики оплачиваются как обычные метрики без схемы (schemaless).

Чтобы оценить стоимость метрики, оцениваются сессии за последние 7 дней, и стоимость в DDU на метрику рассчитывается исходя из ожидаемого приёма данных в минуту. Подробнее см. [Как рассчитывается потребление DDU для metric events?](/managed/license/classic-licensing/davis-data-units/metric-cost-calculation#calculation-details "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").

Какова гранулярность интервала для USQL metric events?

Сохранение данных метрик Dynatrace следует стратегии хранения данных, которая агрегирует метрики со временем. Стратегия хранения данных, применяемая к USQL metric events, идентична стратегии хранения данных, используемой для встроенных метрик временных рядов.

Подробнее см. [Периоды хранения данных > Метрики](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods#metrics-classic "Review default and configurable retention periods for service, RUM Classic, synthetic, Log Monitoring, metric, diagnostic, and security data in Dynatrace Managed.")

## Похожие темы

* [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.")