---
title: Создание пользовательских USQL-метрик для пользовательских приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/custom-applications/additional-configuration/custom-metrics-from-user-sessions-custom-apps
scraped: 2026-05-12T11:07:12.964628
---

# Создание пользовательских USQL-метрик для пользовательских приложений

# Создание пользовательских USQL-метрик для пользовательских приложений

* How-to guide
* 1-min read
* Updated on Feb 21, 2023

С помощью метрических событий USQL вы можете извлекать бизнес-метрики уровня KPI из данных о сессиях и действиях пользователей и сохранять их как временные ряды. Хранящиеся метрики можно использовать в [пользовательских диаграммах](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения нужных аналитических данных."), [механизмах оповещения](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Узнайте о метрических событиях в Dynatrace") или через [Metrics API](/managed/dynatrace-api/environment-api/metric-v2 "Получайте информацию о метриках через Metrics v2 API.").

Метрические события USQL доступны в виде:

* **User session metric events**. Эти метрики сокращённо называются USCM и имеют префикс `uscm.`.
* **User action metric events**. Эти метрики сокращённо называются UACM и начинаются с префикса `uacm.`.

User action metric events доступны начиная с версии Dynatrace 1.260.

Метрические события USQL помогают ответить на вопросы:

* Как со временем меняется индекс пользовательского опыта на моём сайте?
* Как меняется индекс Apdex для определённого типа пользовательских действий?
* Как меняется выручка, генерируемая пользователями?
* Сколько пользователей посещают мой сайт и какие браузеры они используют?
* Какова средняя продолжительность сессии для моего веб-приложения?
* Какова средняя продолжительность пользовательского действия для моего мобильного приложения?

Создавать метрические события USQL и управлять ими можно через веб-интерфейс Dynatrace или через [Dynatrace Settings API](#create-metrics-via-API).

## Настройка метрик через интерфейс

Метрические события USQL можно создавать и управлять ими через веб-интерфейс Dynatrace.

![Страница метрических событий сессий пользователей в веб-интерфейсе Dynatrace](https://dt-cdn.net/images/user-session-custom-metrics-page-2112-726ab6bf4a.png)

Страница метрических событий сессий пользователей в веб-интерфейсе Dynatrace

1. Перейдите в **Settings** > **Web and mobile monitoring** > **User session metric events** или **User action metric events**.
2. Нажмите **Add item**.
3. Введите **Metric key**, который будет использоваться при приёме метрики. Этот ключ используется при запросе данных метрики через [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения нужных аналитических данных.").

   * Для метрических событий сессий пользователей ключ должен начинаться с префикса `uscm.`.
   * Для метрических событий действий пользователей ключ должен начинаться с префикса `uacm.`.
4. В разделе **Value type to be extracted** выберите один из следующих вариантов.

   * Для метрических событий сессий пользователей:

     + **User session counter** — для подсчёта количества сессий пользователей (аналог `COUNT(*)` в [USQL](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Узнайте, как получать доступ к данным сессий и выполнять запросы на основе ключевых слов, синтаксиса, функций и многого другого.")).
     + **User session field value** — для извлечения значения поля сессии пользователя. Также укажите **Field name**. Возможные значения см. в разделе [Значения для метрических событий сессий пользователей](#values-uscm).
   * Для метрических событий действий пользователей:

     + **User action counter** — для подсчёта количества действий пользователей (аналог `COUNT(*)` в [USQL](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Узнайте, как получать доступ к данным сессий и выполнять запросы на основе ключевых слов, синтаксиса, функций и многого другого.")).
     + **User action field value** — для извлечения значения поля действия пользователя. Также укажите **Field name**. Возможные значения см. в разделе [Значения для метрических событий действий пользователей](#values-uacm).
5. В разделе **Add a dimension** укажите поля, которые следует использовать в качестве измерений. Возможные значения см. в разделах [Измерения для метрических событий сессий пользователей](#dimensions-uscm) и [Измерения для метрических событий действий пользователей](#dimensions-uacm).
6. В разделе **Add a filter** добавьте необходимые фильтры.

   * Введите **Field name**. Возможные значения см. в разделах [Фильтры для метрических событий сессий пользователей](#filters-uscm) или [Фильтры для метрических событий действий пользователей](#filters-uacm).
   * Выберите **Operator**.
   * Если выбран один из бинарных операторов, например **equals** или **greater than**, укажите второй аргумент в поле **Value**.

![Создание пользовательской метрики сессий пользователей](https://dt-cdn.net/images/creating-user-session-custom-metric-1359-e1cdae0345.png)

Создание пользовательской метрики сессий пользователей

Также можно использовать [USQL](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data#convert-usql-into-custom-metrics "Узнайте, как получать доступ к данным сессий и выполнять запросы на основе ключевых слов, синтаксиса, функций и многого другого.") для создания метрических событий USQL.

## Настройка метрик через API

Метрические события USQL можно также настраивать через [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.").

1. [Создайте токен доступа](/managed/dynatrace-api/basics/dynatrace-api-authentication#create-token "Узнайте, как пройти аутентификацию для использования Dynatrace API.") с правами **Write settings** (`settings.write`) и **Read settings** (`settings.read`).
2. Используйте конечную точку [GET a schema](/managed/dynatrace-api/environment-api/settings/schemas/get-schema "Просматривайте схему настроек через Dynatrace API."), чтобы узнать формат JSON для отправки конфигурации.

   User session custom metric

   User action custom metric

   Идентификатор схемы конфигурации метрики (`schemaId`) — `builtin:custom-metrics`.

   Пример JSON-payload с конфигурацией пользовательской метрики сессий:

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

   Пример JSON-payload с конфигурацией пользовательской метрики действий:

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
3. Используйте конечную точку [POST an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Создавайте или проверяйте объект настроек через Dynatrace API.") для отправки конфигурации.

В таблице ниже описаны все свойства конфигурации, необходимые для создания или обновления пользовательской USQL-метрики через API.

| Свойство | Описание | Возможные значения |
| --- | --- | --- |
| `enabled` | Определяет, включена ли пользовательская USQL-метрика. Установите `false`, чтобы временно отключить метрику. | `true` или `false` |
| `metricKey` | Ключ метрики, используемый при её приёме. Используйте этот ключ при запросе данных метрики через [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения нужных аналитических данных."). * Для метрических событий сессий ключ должен начинаться с префикса `uscm.`. * Для метрических событий действий ключ должен начинаться с префикса `uacm.`. |  |
| `value` | Источник значения метрики. |  |
| `value.type` | * Для подсчёта сессий или действий (аналог `COUNT(*)` в [USQL](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Узнайте, как получать доступ к данным сессий и выполнять запросы.")): значение `COUNTER`. * Для извлечения значения поля: значение `FIELD`. | `COUNTER` или `FIELD` |
| `value.fieldName` | Если `value.type`=`FIELD`, указывает имя поля сессии или действия пользователя. | См. разделы [Значения для метрических событий сессий](#values-uscm) и [Значения для метрических событий действий](#values-uacm). |
| `dimensions` | Список полей, используемых в качестве измерений. | См. разделы [Измерения для метрических событий сессий](#dimensions-uscm) и [Измерения для метрических событий действий](#dimensions-uacm). |
| `filters` | Определяет фильтры. |  |
| `filter.fieldName` | Имя поля фильтра. | См. разделы [Фильтры для метрических событий сессий](#filters-uscm) и [Фильтры для метрических событий действий](#filters-uacm). |
| `filter.operator` | Оператор фильтра. | `EQUALS`, `NOT_EQUAL`, `IS_NULL`, `IS_NOT_NULL`, `LIKE`, `LESS_THAN`, `LESS_THAN_OR_EQUAL_TO`, `GREATER_THAN`, `GREATER_THAN_OR_EQUAL_TO` |
| `filter.value` | Второй аргумент для бинарных операторов (таких как `EQUALS` или `GREATER_THAN`). |  |

## Поддерживаемые значения, измерения и фильтры

В разделах ниже приведены списки поддерживаемых значений, измерений и фильтров для метрических событий сессий пользователей.

Values for user session metric events

* В качестве значения поддерживаются только поля сессий пользователей. Поля действий пользователей не поддерживаются.
* Все имена полей должны соответствовать именам полей USQL.
* Префикс `usersession.` в имени поля является необязательным. Например, `usersession.duration` и `duration` означают одно и то же.
* Если настроенное поле содержит `null`, метрика игнорируется, но Dynatrace использует самомониторинг для выявления таких случаев.

#### Поля сессий пользователей, поддерживаемые в качестве значений

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

Dimensions for user session metric events

* В качестве измерений поддерживаются как поля сессий, так и поля действий пользователей. Поддержка полей действий доступна начиная с версии Dynatrace 1.234.
* Все имена полей должны соответствовать именам полей USQL.
* Для поля сессии пользователя префикс `usersession.` является необязательным. При приёме метрики префикс `usersession.` опускается.
* Для поля действия пользователя префикс `useraction.` является обязательным. При приёме метрики префикс `useraction.` сохраняется.
* Для одной пользовательской метрики сессии можно добавить до 10 измерений.
* Если поле, настроенное как измерение, содержит `null`, Dynatrace использует строку `null` в качестве значения измерения.
* При использовании `useraction.application` в качестве измерения и охвате сессии нескольких приложений значение метрики записывается для каждого приложения. Во избежание двойного счёта разбейте метрику по приложению.

#### Поля сессий пользователей, поддерживаемые в качестве измерений

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

Любое пользовательское строковое свойство, например `stringProperties.author`. Используйте поля с низкой кардинальностью во избежание создания слишком большого числа значений измерений.

#### Поля действий пользователей, поддерживаемые в качестве измерений

`useraction.application`[1](#fn-3-1-def)

1

Поддерживается начиная с версии Dynatrace 1.234

Filters for user session metric events

* В качестве фильтров поддерживаются как поля сессий, так и поля действий пользователей.
* Все имена полей должны соответствовать именам полей USQL.
* Для поля сессии пользователя префикс `usersession.` является необязательным.
* Для поля действия пользователя префикс `useraction.` является обязательным.
* При добавлении нескольких фильтров все они должны совпадать: фильтры объединяются через `AND`.
* Фильтры, использующие поле действия пользователя, требуют совпадения хотя бы одного действия. Действия сопоставляются через `ANY`.
* Для одной пользовательской метрики сессии можно задать до 10 фильтров.

#### Поля сессий пользователей, поддерживаемые в качестве фильтров

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

#### Поля действий пользователей, поддерживаемые в качестве фильтров

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

Раскройте разделы ниже для ознакомления с поддерживаемыми значениями, измерениями и фильтрами для метрических событий действий пользователей.

Values for user action metric events

* В качестве значений поддерживаются как поля сессий, так и поля действий пользователей.
* Все имена полей должны соответствовать именам полей USQL.
* Для полей действий пользователей префикс `useraction.` является необязательным.
* Для полей сессий пользователей префикс `usersession.` является обязательным.
* Если настроенное поле содержит `null`, метрика игнорируется, но Dynatrace использует самомониторинг для выявления таких случаев.

#### Поля действий пользователей, поддерживаемые в качестве значений

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
`totalBlockingTime` Deprecated  
`cumulativeLayoutShift`  
`longProperties.*`[1](#fn-5-1-def)  
`doubleProperties.*`[1](#fn-5-1-def)

1

Любое пользовательское свойство типа long или double

#### Поля сессий пользователей, поддерживаемые в качестве значений

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

Dimensions for user action metric events

* В качестве измерений поддерживаются как поля сессий, так и поля действий пользователей.
* Все имена полей должны соответствовать именам полей USQL.
* Для полей действий пользователей префикс `useraction.` является необязательным. При приёме метрики префикс `useraction.` опускается.
* Для полей сессий пользователей префикс `usersession.` является обязательным. При приёме метрики префикс `usersession.` сохраняется.
* Для одной пользовательской метрики действия можно указать до 4 измерений, из которых только 2 могут быть высококардинальными.
* Если поле, настроенное как измерение, содержит `null`, Dynatrace использует строку `null` в качестве значения измерения.
* В списке ниже высококардинальные измерения выделены жирным шрифтом.

#### Поля действий пользователей, поддерживаемые в качестве измерений

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

Любое пользовательское строковое свойство. Используйте поля с низкой кардинальностью во избежание создания слишком большого числа значений измерений.

#### Поля сессий пользователей, поддерживаемые в качестве измерений

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

Любое пользовательское строковое свойство, например `usersession.stringProperties.author`. Используйте поля с низкой кардинальностью.

Filters for user action metric events

* В качестве фильтров поддерживаются как поля сессий, так и поля действий пользователей.
* Все имена полей должны соответствовать именам полей USQL.
* Для полей действий пользователей префикс `useraction.` является необязательным.
* Для полей сессий пользователей префикс `usersession.` является обязательным.
* При добавлении нескольких фильтров все они должны совпадать: фильтры объединяются через `AND`.
* Для одной пользовательской метрики действия можно задать до 10 фильтров.

#### Поля действий пользователей, поддерживаемые в качестве фильтров

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
`totalBlockingTime` Deprecated  
`type`  
`userActionPropertyCount`  
`visuallyCompleteTime`  
`syntheticEvent`  
`longProperties.*`[1](#fn-9-1-def)  
`doubleProperties.*`[1](#fn-9-1-def)  
`stringProperties.*`[1](#fn-9-1-def)

1

Любое пользовательское свойство типа long, double или string

#### Поля сессий пользователей, поддерживаемые в качестве фильтров

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

Выявленные ограничения для метрических событий USQL:

* Для одной среды можно создать до 500 пользовательских метрик сессий.
* Для одной среды можно создать до 100 пользовательских метрик действий.

* Данные синтетических сессий не учитываются в значениях метрических событий USQL; учитываются только данные реальных пользователей.
* Dynatrace обновляет метрические события USQL при каждом закрытии сессии. Это означает, что данные активных сессий не включаются в значения метрик USQL; учитываются только закрытые сессии.
* Ключевое слово `DISTINCT`, используемое в [USQL](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Узнайте, как получать доступ к данным сессий и выполнять запросы."), не поддерживается. Если у вас есть запрос вида `SELECT COUNT(DISTINCT country) from usersession`, создать эквивалентную пользовательскую USQL-метрику невозможно.

## Руководство

Чтобы лучше понять принцип работы метрических событий USQL, выполните приведённое ниже руководство для метрических событий сессий пользователей.

![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Создание метрики**

![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Создание и закрепление диаграммы**

![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Создание оповещения**

Через веб-интерфейс Dynatrace создадим пользовательскую метрику сессий (USCM) **Average session duration** на основе данных сессий реальных пользователей. Метрика будет включать два измерения для сегментации данных по семейству браузера и его основной версии. Затем создадим диаграмму для этой метрики, закрепим её на дашборде и настроим пользовательское событие для получения оповещений при превышении заданного порогового значения.

Create a metric

1. Перейдите в **Settings** > **Web and mobile monitoring** > **User session metric events**.
2. Нажмите **Add item**.
3. Введите `uscm.average_duration_of_sessions_by_browser_family_and_version` в поле **Metric key**.
4. В разделе **Value type to be extracted** выберите **User session field value** и установите **Field name** в значение `duration`.
5. Нажмите **Add dimension** и добавьте измерения `browserMajorVersion` и `browserFamily`.
6. В разделе **Add a filter** добавьте следующие фильтры:

   * `userType` = `REAL_USER` (**Field name** — `userType`, **Operator** — `equals`, **Value** — `REAL_USER`)
   * `useraction.application` = `www.easytravel.com` (**Field name** — `useraction.application`, **Operator** — `equals`, **Value** — `www.easytravel.com`). Вместо `www.easytravel.com` можно указать имя своего приложения.
7. Нажмите **Save changes**.

![Создание пользовательской метрики сессий пользователей](https://dt-cdn.net/images/create-custom-metric-example-1910-e74ff5a09d.png)

Создание пользовательской метрики сессий пользователей

Теперь у вас есть пользовательская метрика сессий, извлекаемая как поле (`duration`) только когда `useraction.application` равно `www.easytravel.com` (фильтр по конкретному приложению) и `userType` равно `REAL_USER` (фильтр только для реальных пользователей). Добавлены два измерения для разбивки данных по семейству браузера или основной версии браузера.

После получения данных сессий и заполнения метрики вы можете построить диаграмму, закрепить её на дашборде и даже создать оповещение на основе этой метрики.

Create and pin a chart

Создадим диаграмму на основе метрики `uscm.average_duration_of_sessions_by_browser_family_and_version` и закрепим её на одном из дашбордов.

1. Перейдите в **Data Explorer**.
2. Выберите метрику `uscm.average_duration_of_sessions_by_browser_family_and_version` и нажмите **Run query**.

   ![Создание диаграммы в Data Explorer на основе метрики сессий](https://dt-cdn.net/images/data-explorer-custom-metric-1221-7d8891ede4.png)

   Создание диаграммы в Data Explorer на основе метрики сессий
3. С помощью [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения нужных аналитических данных.") выполните разбивку собранных данных по `browserMajorVersion`, `browserFamily` или обоим параметрам.
4. Отфильтруйте данные сессий по `browserMajorVersion` или `browserFamily`, чтобы сосредоточиться на нужных данных.
5. После создания диаграммы закрепите её на классическом дашборде: нажмите **Pin to dashboard**, выберите один из дашбордов и введите имя плитки.

![Диаграмма пользовательской метрики, закреплённая на дашборде](https://dt-cdn.net/images/dashboard-custom-metric-944-005355f3e5.png)

Диаграмма пользовательской метрики, закреплённая на дашборде

Create an alert

В последней части примера создадим оповещение на основе метрических событий сессий пользователей.

Чтобы создать оповещение:

1. Перейдите в **Settings** > **Anomaly detection** > **Metric events**.
2. Нажмите **Add metric event**.
3. Создайте метрическое событие на основе метрики `uscm.average_duration_of_sessions_by_browser_family_and_version`. Подробнее см. [Метрические события](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Узнайте о метрических событиях в Dynatrace").

![Создание пользовательского события для оповещений на основе метрики сессий](https://dt-cdn.net/images/create-custom-events-for-alerting-2092-9b1d66309a.png)

Создание пользовательского события для оповещений на основе метрики сессий

## Часто задаваемые вопросы

Данные сессий пользователей видны, но данные метрических событий USQL в Data Explorer отсутствуют.

Убедитесь, что сессия пользователя не является активной. Dynatrace извлекает и сохраняет данные метрик как временные ряды только после завершения сессии.

Почему метрические события USQL активных сессий не отображаются в Data Explorer?

По мере завершения сессий в приложениях они помещаются в очередь на последующую обработку. Фоновые процессы извлекают данные метрик из сессий пользователей для подготовки к приёму метрик.

Почему результаты USQL-запросов не совпадают с метрическими событиями USQL?

Данные синтетических сессий не учитываются в метрических событиях USQL.

Исключите синтетические сессии из запроса. Также убедитесь, что к запросу и метрике применяется один и тот же временной диапазон.

Как тарифицируются метрические события USQL?

Начиная с Dynatrace 1.232, метрические события USQL подпадают под [лицензирование по единицам данных Davis (DDU)](/managed/license/monitoring-consumption-classic/davis-data-units "Узнайте, как рассчитывается потребление мониторинга Dynatrace на основе единиц данных Davis (DDU)."). Эти метрики тарифицируются как обычные схемные метрики.

Для оценки стоимости метрики анализируются сессии за последние 7 дней и рассчитывается стоимость в DDU на основе ожидаемого приёма в минуту. Подробнее см. [Как рассчитывается потребление DDU для метрических событий?](/managed/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation#calculation-details "Узнайте, как рассчитать потребление единиц данных Davis и связанные затраты.").

Какова гранулярность интервалов для метрических событий USQL?

Хранение метрических данных в Dynatrace следует стратегии агрегирования метрик со временем. Стратегия хранения данных для метрических событий USQL идентична стратегии для встроенных метрик временных рядов.

Подробнее см. [Периоды хранения данных > Метрики](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods#metrics-classic "Проверьте сроки хранения различных типов данных.")

## Связанные темы

* [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Получайте информацию о метриках через Metrics v2 API.")