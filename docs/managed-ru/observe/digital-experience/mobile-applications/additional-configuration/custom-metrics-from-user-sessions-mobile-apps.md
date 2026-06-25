---
title: Создание USQL-пользовательских метрик для мобильных приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/additional-configuration/custom-metrics-from-user-sessions-mobile-apps
scraped: 2026-05-12T11:07:14.308701
---

# Создание USQL-пользовательских метрик для мобильных приложений

# Создание USQL-пользовательских метрик для мобильных приложений

* How-to guide
* 1-min read
* Updated on Feb 21, 2023

С помощью метрических событий USQL вы можете извлекать KPI бизнес-уровня из данных пользовательских сессий и действий и сохранять эти метрики в виде временных рядов. Затем сохранённые метрики можно использовать в [пользовательских графиках](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения нужных аналитических данных."), [механизмах оповещения](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Узнайте о метрических событиях в Dynatrace") или в [Metrics API](/managed/dynatrace-api/environment-api/metric-v2 "Получайте информацию о метриках через Metrics v2 API.").

Метрические события USQL доступны в виде:

* **Метрических событий пользовательских сессий**. Эти метрики сокращённо обозначаются USCM и имеют префикс `uscm.`.
* **Метрических событий пользовательских действий**. Эти метрики сокращённо обозначаются UACM и начинаются с префикса `uacm.`.

Метрические события пользовательских действий доступны начиная с версии Dynatrace 1.260.

Метрические события USQL помогают ответить на такие вопросы, как:

* Как изменяется индекс пользовательского опыта на моём сайте с течением времени?
* Как изменяется индекс Apdex для определённого типа пользовательских действий?
* Как изменяется доход, генерируемый моими пользователями?
* Сколько пользователей посещает мой сайт и какие браузеры они используют?
* Какова средняя продолжительность сессии для моего веб-приложения?
* Какова средняя продолжительность пользовательских действий для моего мобильного приложения?

Создавать метрическими событиями USQL и управлять ими можно через веб-интерфейс Dynatrace или [Settings API Dynatrace](#create-metrics-via-API).

## Настройка метрик через пользовательский интерфейс

Создавать метрические события USQL и управлять ими можно через веб-интерфейс Dynatrace.

![User session metric events page in the Dynatrace web UI](https://dt-cdn.net/images/user-session-custom-metrics-page-2112-726ab6bf4a.png)

User session metric events page in the Dynatrace web UI

1. Перейдите в **Settings** > **Web and mobile monitoring** > **User session metric events** или **User action metric events**.
2. Нажмите **Add item**.
3. Введите **Metric key**, который будет использоваться при приёме метрики. Этот ключ понадобится при запросе данных метрики через [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения нужных аналитических данных.").

   * Для метрических событий пользовательских сессий ключ должен начинаться с префикса `uscm.`.
   * Для метрических событий пользовательских действий ключ должен начинаться с префикса `uacm.`.
4. В разделе **Value type to be extracted** выберите один из следующих вариантов.

   * Для метрических событий пользовательских сессий:

     + **User session counter** — для подсчёта числа пользовательских сессий (аналогично `COUNT(*)` в [USQL](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Узнайте, как получать доступ к данным пользовательских сессий и запрашивать их.")).
     + **User session field value** — для извлечения значения поля пользовательской сессии. Также укажите **Field name**. Возможные значения см. в разделе [Значения для метрических событий пользовательских сессий](#values-uscm).
   * Для метрических событий пользовательских действий:

     + **User action counter** — для подсчёта числа пользовательских действий (аналогично `COUNT(*)` в [USQL](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Узнайте, как получать доступ к данным пользовательских сессий и запрашивать их.")).
     + **User action field value** — для извлечения значения поля пользовательского действия. Также укажите **Field name**. Возможные значения см. в разделе [Значения для метрических событий пользовательских действий](#values-uacm).
5. В разделе **Add a dimension** укажите поля, которые должны использоваться в качестве измерений. Возможные значения см. в разделах [Измерения для метрических событий пользовательских сессий](#dimensions-uscm) и [Измерения для метрических событий пользовательских действий](#dimensions-uacm).
6. В разделе **Add a filter** добавьте необходимые фильтры.

   * Введите **Field name**. Возможные значения см. в разделах [Фильтры для метрических событий пользовательских сессий](#filters-uscm) или [Фильтры для метрических событий пользовательских действий](#filters-uacm).
   * Выберите **Operator**.
   * Если вы выбрали один из бинарных операторов, например **equals** или **greater than**, также укажите второй аргумент в текстовом поле **Value**.

![Creating a user session custom metric](https://dt-cdn.net/images/creating-user-session-custom-metric-1359-e1cdae0345.png)

Creating a user session custom metric

Кроме того, для создания метрических событий USQL можно использовать [USQL](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data#convert-usql-into-custom-metrics "Узнайте, как получать доступ к данным пользовательских сессий и запрашивать их.").

## Настройка метрик через API

Для настройки метрических событий USQL также можно использовать [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Settings API Dynatrace.").

1. [Создайте токен доступа](/managed/dynatrace-api/basics/dynatrace-api-authentication#create-token "Узнайте, как пройти аутентификацию для использования Dynatrace API.") с правами **Write settings** (`settings.write`) и **Read settings** (`settings.read`).
2. Используйте конечную точку [GET a schema](/managed/dynatrace-api/environment-api/settings/schemas/get-schema "Просматривайте схему настроек через Dynatrace API."), чтобы узнать формат JSON для публикации конфигурации.

   Метрики пользовательской сессии

   Метрики пользовательских действий

   Идентификатор схемы конфигурации метрики (`schemaId`): `builtin:custom-metrics`.

   Пример полезной нагрузки JSON для конфигурации пользовательской метрики сессии:

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

   Идентификатор схемы конфигурации метрики (`schemaId`): `builtin:user-action-custom-metrics`.

   Пример полезной нагрузки JSON для конфигурации пользовательской метрики действий:

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

В таблице ниже объясняются все свойства конфигурации, необходимые для создания или обновления пользовательской метрики USQL через API.

| Свойство | Описание | Возможные значения |
| --- | --- | --- |
| `enabled` | Определяет, включена ли пользовательская метрика USQL. Установите `false` для временного отключения метрики. | `true` или `false` |
| `metricKey` | Ключ метрики, используемый при приёме. Используйте его при запросе данных метрики через [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения нужных аналитических данных.").  * Для метрик пользовательских сессий ключ должен начинаться с префикса `uscm.`. * Для метрик пользовательских действий ключ должен начинаться с префикса `uacm.`. |  |
| `value` | Источник значения метрики. |  |
| `value.type` | * Для подсчёта числа пользовательских сессий или действий (аналогично `COUNT(*)` в [USQL](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Узнайте, как получать доступ к данным пользовательских сессий и запрашивать их.")) установите `COUNTER`. * Для извлечения значения поля пользовательской сессии или действия установите `FIELD`. | `COUNTER` или `FIELD` |
| `value.fieldName` | Если `value.type`=`FIELD`, задаёт имя поля пользовательской сессии или действия. | См. [Значения для метрических событий пользовательских сессий](#values-uscm) и [Значения для метрических событий пользовательских действий](#values-uacm). |
| `dimensions` | Перечисляет поля, используемые в качестве измерений. | См. [Измерения для метрических событий пользовательских сессий](#dimensions-uscm) и [Измерения для метрических событий пользовательских действий](#dimensions-uacm). |
| `filters` | Задаёт фильтры. |  |
| `filter.fieldName` | Задаёт имя поля фильтра. | См. [Фильтры для метрических событий пользовательских сессий](#filters-uscm) и [Фильтры для метрических событий пользовательских действий](#filters-uacm). |
| `filter.operator` | Задаёт оператор. | `EQUALS`, `NOT_EQUAL`, `IS_NULL`, `IS_NOT_NULL`, `LIKE`, `LESS_THAN`, `LESS_THAN_OR_EQUAL_TO`, `GREATER_THAN`, `GREATER_THAN_OR_EQUAL_TO` |
| `filter.value` | Предоставляет второй аргумент для бинарных операторов (таких как `EQUALS` или `GREATER_THAN`). |  |

## Поддерживаемые значения, измерения и фильтры

Ознакомьтесь с разделами ниже, чтобы просмотреть списки поддерживаемых значений, измерений и фильтров для метрических событий пользовательских сессий.

Значения для метрических событий пользовательских сессий

* В качестве значений поддерживаются только поля пользовательских сессий. Поля пользовательских действий не поддерживаются.
* Все имена полей должны соответствовать именам полей USQL.
* Префикс `usersession.` в имени поля не является обязательным. Например, `usersession.duration` и `duration` означают одно и то же.
* Если настроенное поле содержит `null`, метрика игнорируется, но Dynatrace использует самомониторинг для выявления таких случаев.

#### Поля пользовательских сессий, поддерживаемые в качестве значений

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

* В качестве измерений поддерживаются как поля пользовательских сессий, так и поля пользовательских действий. Поля пользовательских действий поддерживаются начиная с версии Dynatrace 1.234.
* Все имена полей должны соответствовать именам полей USQL.
* Для имён полей пользовательских сессий префикс `usersession.` не является обязательным. Например, `usersession.country` и `country` означают одно и то же. При приёме метрики префикс `usersession.` удаляется, например `usersession.country` становится `country`.
* Для имён полей пользовательских действий префикс `useraction.` является обязательным. При приёме метрики префикс `useraction.` сохраняется.
* Вы можете добавить до 10 измерений в одну пользовательскую метрику сессии.
* Если поле, настроенное как измерение, содержит `null`, Dynatrace использует строку `null` в качестве значения измерения.
* Если вы используете `useraction.application` как измерение и пользовательская сессия охватывает несколько приложений, значение метрики записывается для каждого приложения. Чтобы избежать двойного счёта, разбейте метрику по приложениям.

#### Поля пользовательских сессий, поддерживаемые в качестве измерений

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

#### Поля пользовательских действий, поддерживаемые в качестве измерений

`useraction.application`[1](#fn-3-1-def)

1

Поддерживается начиная с версии Dynatrace 1.234

Фильтры для метрических событий пользовательских сессий

* В качестве фильтров поддерживаются как поля пользовательских сессий, так и поля пользовательских действий.
* Все имена полей должны соответствовать именам полей USQL.
* Для имён полей пользовательских сессий префикс `usersession.` не является обязательным.
* Для имён полей пользовательских действий префикс `useraction.` является обязательным.
* При добавлении нескольких фильтров все они должны совпадать: фильтры объединяются с помощью `AND`.
* Фильтры, использующие поле пользовательского действия, требуют соответствия хотя бы одного действия. Действия сопоставляются с помощью `ANY`.
* Для одной пользовательской метрики сессии можно задать до 10 фильтров.

#### Поля пользовательских сессий, поддерживаемые в качестве фильтров

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

#### Поля пользовательских действий, поддерживаемые как поля

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

Разверните разделы ниже, чтобы просмотреть поддерживаемые значения, измерения и фильтры для метрических событий пользовательских действий.

Значения для метрических событий пользовательских действий

* В качестве значений поддерживаются как поля пользовательских сессий, так и поля пользовательских действий.
* Все имена полей должны соответствовать именам полей USQL.
* Для полей пользовательских действий префикс `useraction.` не является обязательным. Например, `useraction.type` и `type` означают одно и то же.
* Для полей пользовательских сессий префикс `usersession.` является обязательным.
* Если настроенное поле содержит `null`, метрика игнорируется, но Dynatrace использует самомониторинг для выявления таких случаев.

#### Поля пользовательских действий, поддерживаемые в качестве значений

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

#### Поля пользовательских сессий, поддерживаемые в качестве значений

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

Измерения для метрических событий пользовательских действий

* В качестве измерений поддерживаются как поля пользовательских сессий, так и поля пользовательских действий.
* Все имена полей должны соответствовать именам полей USQL.
* Для полей пользовательских действий префикс `useraction.` не является обязательным. Например, `useraction.type` и `type` означают одно и то же. При приёме метрики префикс `useraction.` удаляется, например `useraction.type` становится `type`.
* Для полей пользовательских сессий префикс `usersession.` является обязательным. При приёме метрики префикс `usersession.` сохраняется.
* Вы можете указать до 4 измерений для пользовательской метрики действий, но только 2 из них могут быть высококардинальными.
* Если поле, настроенное как измерение, содержит `null`, Dynatrace использует строку `null` в качестве значения измерения.
* В списке ниже измерения, выделенные жирным, являются высококардинальными.

#### Поля пользовательских действий, поддерживаемые в качестве измерений

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

Любое пользовательское строковое свойство. Используйте поля с низкой кардинальностью, чтобы не создавать слишком много значений измерений.

#### Поля пользовательских сессий, поддерживаемые в качестве измерений

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

Любое пользовательское строковое свойство, например `usersession.stringProperties.author`. Используйте поля с низкой кардинальностью, чтобы не создавать слишком много значений измерений.

Фильтры для метрических событий пользовательских действий

* В качестве фильтров поддерживаются как поля пользовательских сессий, так и поля пользовательских действий.
* Все имена полей должны соответствовать именам полей USQL.
* Для полей пользовательских действий префикс `useraction.` не является обязательным.
* Для полей пользовательских сессий префикс `usersession.` является обязательным.
* При добавлении нескольких фильтров все они должны совпадать: фильтры объединяются с помощью `AND`.
* Для одной пользовательской метрики действий можно задать до 10 фильтров.

#### Поля пользовательских действий, поддерживаемые в качестве фильтров

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

#### Поля пользовательских сессий, поддерживаемые в качестве фильтров

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

Для метрических событий USQL выявлены следующие ограничения:

* Вы можете создать до 500 пользовательских метрик сессий на окружение.
* Вы можете создать до 100 пользовательских метрик действий на окружение.

* Синтетические данные пользовательских сессий не учитываются в значениях метрических событий USQL; учитываются только данные реальных пользователей.
* Dynatrace обновляет метрические события USQL каждый раз, когда сессия закрывается. Это означает, что данные активных сессий не учитываются в значениях пользовательских метрик USQL; учитываются только данные закрытых сессий.
* Ключевое слово `DISTINCT`, используемое в [USQL](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Узнайте, как получать доступ к данным пользовательских сессий и запрашивать их."), не поддерживается. Если у вас есть запрос вида `SELECT COUNT(DISTINCT country) from usersession`, создать эквивалентную пользовательскую метрику USQL невозможно.

## Учебное руководство

Для лучшего понимания работы метрических событий USQL вы можете следовать приведённому ниже руководству по метрическим событиям пользовательских сессий.

![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Создание метрики**

![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Создание и закрепление графика**

![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Создание оповещения**

С помощью веб-интерфейса Dynatrace создадим пользовательскую метрику сессий (USCM) **Average session duration** (средняя продолжительность сессии) на основе данных сессий реальных пользователей. Метрика будет включать два измерения для сегментации данных сессий по семейству браузеров и версии браузера. Используя эту метрику, мы создадим график, закрепим его на панели мониторинга и создадим пользовательское событие, чтобы получать оповещения при превышении значением метрики заданного порога.

Создание метрики

1. Перейдите в **Settings** > **Web and mobile monitoring** > **User session metric events**.
2. Нажмите **Add item**.
3. В качестве **Metric key** введите `uscm.average_duration_of_sessions_by_browser_family_and_version`.
4. В разделе **Value type to be extracted** выберите **User session field value**. Также установите **Field name** в значение `duration`.
5. Нажмите **Add dimension** и добавьте измерения `browserMajorVersion` и `browserFamily`.
6. В разделе **Add a filter** добавьте следующие фильтры:

   * `userType` = `REAL_USER` (**Field name** — `userType`, **Operator** — `equals`, **Value** — `REAL_USER`)
   * `useraction.application` = `www.easytravel.com` (**Field name** — `useraction.application`, **Operator** — `equals`, **Value** — `www.easytravel.com`). Вместо значения `www.easytravel.com` используйте имя вашего приложения.
7. Нажмите **Save changes**.

![Creating a user session custom metric](https://dt-cdn.net/images/create-custom-metric-example-1910-e74ff5a09d.png)

Creating a user session custom metric

Теперь у вас есть пользовательская метрика сессий, которая извлекается как поле (`duration`) только при выполнении условий `useraction.application` равно `www.easytravel.com` (фильтрация по конкретному приложению) и `userType` равно `REAL_USER` (фильтрация только реальных пользователей). Кроме того, вы добавили два измерения для разбивки данных по семейству браузеров или основной версии браузера.

После получения данных пользовательских сессий и заполнения метрики вы сможете построить по ней график, закрепить его на панели мониторинга и создать оповещение.

Создание и закрепление графика

Теперь создадим график на основе метрики `uscm.average_duration_of_sessions_by_browser_family_and_version` и закрепим его на одной из панелей мониторинга.

1. Перейдите в **Data Explorer**.
2. Выберите метрику `uscm.average_duration_of_sessions_by_browser_family_and_version` и нажмите **Run query**.

   ![Creating a chart in Data Explorer based on user sessions metric](https://dt-cdn.net/images/data-explorer-custom-metric-1221-7d8891ede4.png)

   Creating a chart in Data Explorer based on user sessions metric
3. Используя [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения нужных аналитических данных."), разбейте собранные данные для просмотра данных пользовательских сессий по `browserMajorVersion`, `browserFamily` или обоим параметрам.
4. Фильтруйте данные пользовательских сессий по `browserMajorVersion` или `browserFamily`, чтобы сосредоточиться на интересующих данных.
5. После создания графика с вашими данными вы можете закрепить его на классической панели мониторинга: нажмите **Pin to dashboard**, выберите одну из панелей и введите название плитки.

![Custom metric chart pinned to the dashboard](https://dt-cdn.net/images/dashboard-custom-metric-944-005355f3e5.png)

Custom metric chart pinned to the dashboard

Создание оповещения

В завершение создадим оповещение на основе метрических событий пользовательских сессий.

Чтобы создать оповещение:

1. Перейдите в **Settings** > **Anomaly detection** > **Metric events**.
2. Нажмите **Add metric event**.
3. Создайте метрическое событие на основе метрики `uscm.average_duration_of_sessions_by_browser_family_and_version`. Подробнее см. в разделе [Metric events](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Узнайте о метрических событиях в Dynatrace").

![Creating a custom event for alerting based on a user sessions metric](https://dt-cdn.net/images/create-custom-events-for-alerting-2092-9b1d66309a.png)

Creating a custom event for alerting based on a user sessions metric

## Часто задаваемые вопросы

Данные пользовательских сессий отображаются, но данные метрических событий USQL не видны в Data Explorer.

Убедитесь, что пользовательская сессия не является активной. Dynatrace извлекает и сохраняет данные метрик в виде временных рядов только после закрытия пользовательской сессии.

Почему метрические события USQL активных сессий не отображаются в Data Explorer?

По мере закрытия сессий в приложениях они помещаются в очередь для последующей обработки. Затем ряд фоновых процессов извлекает данные метрик из пользовательских сессий для подготовки данных к приёму метрик.

Почему результаты моих USQL-запросов не совпадают с метрическими событиями USQL?

Синтетические данные пользовательских сессий не учитываются в метрических событиях USQL.

Исключите синтетические сессии из запроса. Также убедитесь, что к запросу и метрике применяется одинаковый временной диапазон.

Как тарифицируются метрические события USQL?

Начиная с Dynatrace 1.232, метрические события USQL тарифицируются по [лицензированию единиц данных Davis (DDU)](/managed/license/monitoring-consumption-classic/davis-data-units "Узнайте, как рассчитывается потребление мониторинга Dynatrace на основе единиц данных Davis (DDU)."). Эти метрики тарифицируются как обычные бесструктурные метрики.

Для оценки стоимости на метрику оцениваются сессии за последние 7 дней и рассчитывается стоимость в DDU в соответствии с ожидаемым приёмом в минуту. Подробнее см. в разделе [Как рассчитывается потребление DDU для метрических событий?](/managed/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation#calculation-details "Узнайте, как рассчитать потребление единиц данных Davis и затраты, связанные с отслеживаемыми метриками.").

Какова детализация интервала для метрических событий USQL?

Хранение данных метрик в Dynatrace следует стратегии хранения данных, агрегирующей метрики со временем. Стратегия хранения данных для метрических событий USQL идентична стратегии, применяемой к встроенным метрикам временных рядов.

Подробнее см. в разделе [Сроки хранения данных > Metrics](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods#metrics-classic "Проверьте сроки хранения для различных типов данных.")

## Связанные темы

* [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Получайте информацию о метриках через Metrics v2 API.")