---
title: Создание пользовательских метрик USQL для веб-приложений
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/additional-configuration/custom-metrics-from-user-sessions
scraped: 2026-03-04T21:28:06.966694
---

С помощью событий метрик USQL вы можете извлекать KPI-метрики бизнес-уровня из данных пользовательских сессий и действий пользователей и сохранять их в виде временных рядов. Затем вы можете использовать сохранённые метрики в пользовательских графиках, механизмах оповещения или Metrics API.

События метрик USQL доступны в виде:

* **Событий метрик пользовательских сессий**. Эти метрики сокращённо называются USCM и имеют префикс `uscm.`.
* **Событий метрик действий пользователей**. Эти метрики сокращённо называются UACM и имеют префикс `uacm.`.

События метрик действий пользователей доступны начиная с Dynatrace версии 1.260.

События метрик USQL помогут вам ответить на такие вопросы, как:

* Как изменяется индекс пользовательского опыта для моего веб-сайта с течением времени?
* Как изменяется индекс Apdex для определённого типа действий пользователей с течением времени?
* Как изменяется доход, генерируемый моими пользователями, с течением времени?
* Сколько пользователей приходят на мой веб-сайт и какие браузеры они используют?
* Какова средняя продолжительность сессии для моего веб-приложения?
* Какова средняя продолжительность действия пользователя для моего мобильного приложения?

Вы можете создавать и управлять событиями метрик USQL с помощью веб-интерфейса Dynatrace или [Dynatrace Settings API](#create-metrics-via-API).

## Настройка метрик через пользовательский интерфейс

Вы можете создавать и управлять событиями метрик USQL с помощью веб-интерфейса Dynatrace.

![Страница событий метрик пользовательских сессий в веб-интерфейсе Dynatrace](https://dt-cdn.net/images/user-session-custom-metrics-page-2112-726ab6bf4a.png)

1. Перейдите в **Settings** > **Web and mobile monitoring** > **User session metric events** или **User action metric events**.
2. Выберите **Add item**.
3. Введите **Metric key** (ключ метрики), который будет использоваться при загрузке метрики. Вы будете использовать этот ключ при запросе данных метрики через Data Explorer.

   * Для событий метрик пользовательских сессий начинайте ключ метрики с префикса `uscm.`.
   * Для событий метрик действий пользователей начинайте ключ метрики с префикса `uacm.`.
4. В разделе **Value type to be extracted** выберите один из следующих вариантов.

   * Для событий метрик пользовательских сессий:

     + **User session counter** — для подсчёта количества пользовательских сессий, аналогично `COUNT(*)` при использовании USQL.
     + **User session field value** — для извлечения значения поля пользовательской сессии. Также укажите **Field name**. Возможные значения см. в разделе [Значения для событий метрик пользовательских сессий](#values-uscm).
   * Для событий метрик действий пользователей:

     + **User action counter** — для подсчёта количества действий пользователей, аналогично `COUNT(*)` при использовании USQL.
     + **User action field value** — для извлечения значения поля действия пользователя. Также укажите **Field name**. Возможные значения см. в разделе [Значения для событий метрик действий пользователей](#values-uacm).
5. В разделе **Add a dimension** укажите поля, которые должны использоваться в качестве измерений. Возможные значения см. в разделах [Измерения для событий метрик пользовательских сессий](#dimensions-uscm) и [Измерения для событий метрик действий пользователей](#dimensions-uacm).
6. В разделе **Add a filter** добавьте необходимые фильтры.

   * Введите **Field name**. Возможные значения см. в разделах [Фильтры для событий метрик пользовательских сессий](#filters-uscm) или [Фильтры для событий метрик действий пользователей](#filters-uacm).
   * Выберите **Operator**.
   * Если вы выбрали один из бинарных операторов, например **equals** или **greater than**, также укажите второй аргумент в текстовом поле **Value**.

![Создание пользовательской метрики пользовательской сессии](https://dt-cdn.net/images/creating-user-session-custom-metric-1359-e1cdae0345.png)

В качестве альтернативы вы можете использовать [USQL](../../session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data.md#convert-usql-into-custom-metrics "Узнайте, как получать доступ к данным пользовательских сессий и выполнять запросы на основе ключевых слов, синтаксиса, функций и т.д.") для создания событий метрик USQL.

## Настройка метрик через API

Вы также можете использовать Settings API для настройки событий метрик USQL.

1. [Создайте токен доступа](../../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Узнайте, как пройти аутентификацию для использования Dynatrace API.") с разрешениями **Write settings** (`settings.write`) и **Read settings** (`settings.read`).
2. Используйте эндпоинт GET a schema, чтобы узнать формат JSON, необходимый для отправки вашей конфигурации.

   Пользовательская метрика пользовательской сессии

   Пользовательская метрика действия пользователя

   Идентификатор схемы конфигурации метрики (`schemaId`) — `builtin:custom-metrics`.

   Вот пример JSON-полезной нагрузки с конфигурацией пользовательской метрики пользовательской сессии:

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

   Вот пример JSON-полезной нагрузки с конфигурацией пользовательской метрики действия пользователя:

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
3. Используйте эндпоинт POST an object для отправки вашей конфигурации.

В таблице ниже описаны все свойства конфигурации, необходимые для создания или обновления пользовательской метрики USQL через API.

## Поддерживаемые значения, измерения и фильтры

Ознакомьтесь с разделами ниже, чтобы просмотреть списки поддерживаемых значений, измерений и фильтров для событий метрик пользовательских сессий.

Значения для событий метрик пользовательских сессий

* В качестве значения поддерживаются только поля пользовательских сессий. Поля действий пользователей не поддерживаются в качестве значения.
* Все имена полей должны совпадать с именами полей USQL.
* Префикс `usersession.` в имени поля является необязательным. Например, `usersession.duration` и `duration` означают одно и то же.
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

Измерения для событий метрик пользовательских сессий

* В качестве измерений поддерживаются как поля пользовательских сессий, так и поля действий пользователей. Поля действий пользователей поддерживаются начиная с Dynatrace версии 1.234.
* Все имена полей должны совпадать с именами полей USQL.
* Для имени поля пользовательской сессии префикс `usersession.` является необязательным. Например, `usersession.country` и `country` означают одно и то же. При загрузке метрики префикс `usersession.` удаляется, например, `usersession.country` становится `country`.
* Для имени поля действия пользователя префикс `useraction.` является обязательным. При загрузке метрики префикс `useraction.` сохраняется.
* Вы можете добавить до 10 измерений к одной пользовательской метрике пользовательской сессии.
* Если поле, настроенное как измерение, содержит `null`, Dynatrace использует строку `null` в качестве значения измерения.
* Если вы используете `useraction.application` в качестве измерения и пользовательская сессия охватывает несколько приложений, значение пользовательской метрики записывается для каждого приложения. Чтобы избежать двойного подсчёта значения, разделите метрику по приложениям.

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

Любое пользовательское строковое свойство, например `stringProperties.author`. Используйте поля с низкой кардинальностью, чтобы избежать создания слишком большого количества значений измерений.

#### Поля действий пользователей, поддерживаемые в качестве измерений

`useraction.application`[1](#fn-3-1-def)

1

Поддерживается начиная с Dynatrace версии 1.234

Фильтры для событий метрик пользовательских сессий

* В качестве фильтров поддерживаются как поля пользовательских сессий, так и поля действий пользователей.
* Все имена полей должны совпадать с именами полей USQL.
* Для имени поля пользовательской сессии префикс `usersession.` является необязательным. Например, `usersession.country` и `country` означают одно и то же.
* Для имени поля действия пользователя префикс `useraction.` является обязательным.
* При добавлении нескольких фильтров все они должны совпадать — фильтры объединяются с помощью `AND`.
* Фильтры, использующие поле действия пользователя, требуют совпадения хотя бы одного действия пользователя. Действия пользователей сопоставляются с помощью `ANY`.
* Вы можете установить до 10 фильтров для одной пользовательской метрики пользовательской сессии.

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

#### Поля действий пользователей, поддерживаемые в качестве полей

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

Разверните разделы ниже, чтобы просмотреть поддерживаемые значения, измерения и фильтры для событий метрик действий пользователей.

Значения для событий метрик действий пользователей

* В качестве значений поддерживаются как поля пользовательских сессий, так и поля действий пользователей.
* Все имена полей должны совпадать с именами полей USQL.
* Для полей действий пользователей префикс `useraction.` является необязательным. Например, `useraction.type` и `type` означают одно и то же.
* Для полей пользовательских сессий префикс `usersession.` является обязательным.
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
`totalBlockingTime` Устарело
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

Измерения для событий метрик действий пользователей

* Поддерживаются как поля пользовательских сессий, так и поля действий пользователей.
* Все имена полей должны совпадать с именами полей USQL.
* Для полей действий пользователей префикс `useraction.` является необязательным. Например, `useraction.type` и `type` означают одно и то же. При загрузке метрики префикс `useraction.` удаляется, например, `useraction.type` становится `type`.
* Для полей пользовательских сессий префикс `usersession.` является обязательным. При загрузке метрики префикс `usersession.` сохраняется.
* Вы можете указать до 4 измерений для пользовательской метрики действия пользователя, но только 2 из них могут быть измерениями с высокой кардинальностью.
* Если поле, настроенное как измерение, содержит `null`, Dynatrace использует строку `null` в качестве значения измерения.
* В списке ниже измерения, выделенные жирным шрифтом, являются измерениями с высокой кардинальностью.

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

Любое пользовательское строковое свойство. Используйте поля с низкой кардинальностью, чтобы избежать создания слишком большого количества значений измерений.

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

Любое пользовательское строковое свойство, например `usersession.stringProperties.author`. Используйте поля с низкой кардинальностью, чтобы избежать создания слишком большого количества значений измерений.

Фильтры для событий метрик действий пользователей

* В качестве фильтров поддерживаются как поля пользовательских сессий, так и поля действий пользователей.
* Все имена полей должны совпадать с именами полей USQL.
* Для полей действий пользователей префикс `useraction.` является необязательным. Например, `useraction.type` и `type` означают одно и то же.
* Для полей пользовательских сессий префикс `usersession.` является обязательным.
* При добавлении нескольких фильтров все они должны совпадать — фильтры объединяются с помощью `AND`.
* Вы можете установить до 10 фильтров для одной пользовательской метрики действия пользователя.

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

Мы выявили следующие ограничения для событий метрик USQL:

* Вы можете создать до 500 пользовательских метрик пользовательских сессий на одну среду.
* Вы можете создать до 100 пользовательских метрик действий пользователей на одну среду.

* Данные синтетических пользовательских сессий не учитываются в значениях событий метрик USQL; включаются только данные реальных пользователей.
* Dynatrace обновляет события метрик USQL каждый раз при закрытии сессии. Это означает, что данные текущих (живых) сессий не учитываются в значениях пользовательских метрик USQL; включаются только данные закрытых сессий.
* Ключевое слово `DISTINCT`, используемое в USQL, не поддерживается. Если у вас есть запрос вида `SELECT COUNT(DISTINCT country) from usersession`, создать эквивалентную пользовательскую метрику USQL невозможно.

## Руководство

Чтобы лучше понять, как работают события метрик USQL, вы можете следовать приведённому ниже руководству для событий метрик пользовательских сессий.

![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Создание метрики**

![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Создание и закрепление графика**

![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Создание оповещения**

Используя веб-интерфейс Dynatrace, давайте создадим пользовательскую метрику пользовательской сессии (USCM) **Средняя продолжительность сессии** на основе данных сессий реальных пользователей. Метрика будет включать два измерения для сегментации данных сессий по семейству браузера и основной версии браузера. Используя эту метрику, мы затем создадим график, закрепим его на дашборде и создадим пользовательское событие для метрики, чтобы вы могли получать оповещения, когда значение метрики превышает заданный порог.

Создание метрики

1. Перейдите в **Settings** > **Web and mobile monitoring** > **User session metric events**.
2. Выберите **Add item**.
3. Введите `uscm.average_duration_of_sessions_by_browser_family_and_version` в качестве **Metric key**.
4. В разделе **Value type to be extracted** выберите **User session field value**. Также установите **Field name** равным `duration`.
5. Выберите **Add dimension** и добавьте измерения `browserMajorVersion` и `browserFamily`.
6. В разделе **Add a filter** добавьте следующие фильтры:

   * `userType` = `REAL_USER` (**Field name** — `userType`, **Operator** — `equals`, **Value** — `REAL_USER`)
   * `useraction.application` = `www.easytravel.com` (**Field name** — `useraction.application`, **Operator** — `equals`, **Value** — `www.easytravel.com`). Вместо значения `www.easytravel.com` вы можете использовать имя вашего собственного приложения.
7. Выберите **Save changes**.

![Создание пользовательской метрики пользовательской сессии](https://dt-cdn.net/images/create-custom-metric-example-1910-e74ff5a09d.png)

Теперь у вас есть пользовательская метрика пользовательской сессии, которая извлекается как поле (`duration`) только когда `useraction.application` равно `www.easytravel.com` (фильтрация по конкретному приложению) и `userType` равно `REAL_USER` (фильтрация только по реальным пользователям). Кроме того, вы добавили два измерения, которые позволяют разделить данные по семейству браузера или основной версии браузера.

После получения данных пользовательской сессии и заполнения метрики вы можете создать график для этой метрики, закрепить его на дашборде и даже создать оповещение на основе метрики.

Создание и закрепление графика

Теперь давайте создадим график на основе метрики `uscm.average_duration_of_sessions_by_browser_family_and_version` и закрепим этот график на одном из ваших дашбордов.

1. Перейдите в **Data Explorer**.
2. Выберите метрику `uscm.average_duration_of_sessions_by_browser_family_and_version` и выберите **Run query**.

   ![Создание графика в Data Explorer на основе метрики пользовательских сессий](https://dt-cdn.net/images/data-explorer-custom-metric-1221-7d8891ede4.png)
3. Используя Data Explorer, разделите собранные данные, чтобы увидеть данные пользовательских сессий, разбитые по `browserMajorVersion`, `browserFamily` или по обоим параметрам.
4. Отфильтруйте данные пользовательских сессий по `browserMajorVersion` или `browserFamily`, чтобы сосредоточиться на интересующих вас данных.
5. После создания графика, представляющего ваши данные, вы можете закрепить его на классическом дашборде: выберите **Pin to dashboard**, выберите один из ваших дашбордов и введите название плитки.

![График пользовательской метрики, закреплённый на дашборде](https://dt-cdn.net/images/dashboard-custom-metric-944-005355f3e5.png)

Создание оповещения

В заключительной части этого примера мы создадим оповещение на основе событий метрик пользовательских сессий.

Для создания оповещения

1. Перейдите в **Settings** > **Anomaly detection** > **Metric events**.
2. Выберите **Add metric event**.
3. Создайте событие метрики на основе метрики `uscm.average_duration_of_sessions_by_browser_family_and_version`. Подробнее см. События метрик.

![Создание пользовательского события для оповещения на основе метрики пользовательских сессий](https://dt-cdn.net/images/create-custom-events-for-alerting-2092-9b1d66309a.png)

## Часто задаваемые вопросы

Я вижу данные пользовательской сессии, но не вижу данные событий метрик USQL в Data Explorer.

Убедитесь, что пользовательская сессия не является текущей (живой). Dynatrace извлекает и сохраняет данные метрик во временные ряды только после закрытия пользовательской сессии.

Почему события метрик USQL текущих сессий не отображаются в Data Explorer?

По мере закрытия сессий в приложениях они помещаются в очередь для последующей обработки. Затем фоновые обработчики извлекают данные метрик из пользовательских сессий для подготовки данных к загрузке метрик.

Почему результаты моего запроса USQL не совпадают с событиями метрик USQL?

Данные синтетических пользовательских сессий не учитываются в событиях метрик USQL.

Исключите синтетические сессии из вашего запроса. Также убедитесь, что к запросу и метрике применён одинаковый временной интервал.

Как тарифицируются события метрик USQL?

Начиная с Dynatrace 1.232, события метрик USQL подлежат лицензированию по единицам данных Davis (DDU)."). Эти метрики тарифицируются как обычные бессхемные метрики.

Для оценки стоимости на метрику анализируются сессии за последние 7 дней, и стоимость в DDU на метрику рассчитывается в соответствии с ожидаемой загрузкой в минуту. Подробнее см. Как мы рассчитываем потребление DDU для событий метрик?.

Какова гранулярность интервалов для событий метрик USQL?

Система хранения данных метрик Dynatrace следует стратегии хранения данных, которая агрегирует метрики с течением времени. Стратегия хранения данных, применяемая к событиям метрик USQL, идентична стратегии, используемой для встроенных метрик временных рядов.

Подробнее см. [Периоды хранения данных > Метрики](../../../../manage/data-privacy-and-security/data-privacy/data-retention-periods.md#metrics-classic "Проверьте сроки хранения для различных типов данных.")

## Связанные темы

* Metrics API v2