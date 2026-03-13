---
title: Правила обнаружения сервисов
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v1/customize-service-detection
scraped: 2026-03-06T21:22:34.909415
---

# Правила обнаружения сервисов

# Правила обнаружения сервисов

* Classic
* Практическое руководство
* Чтение: 15 мин
* Обновлено 21 октября 2025 г.

При мониторинге с помощью OneAgent ваши развёрнутые приложения и связанные микросервисы автоматически обнаруживаются Dynatrace на основе определённых свойств развёртывания и конфигурации приложения, таких как идентификатор приложения, часть URL или имя сервера.

Атрибуты, используемые для обнаружения, отмечены звёздочкой * на странице обзора [сервиса](/docs/observe/application-observability/services-classic/service-analysis-new "Узнайте обо всех деталях мониторинга сервисов, которые предоставляет Dynatrace."), в разделе **Properties and tags**.

В некоторых случаях качество данных, доступных Dynatrace, может быть недостаточным для высокоточного обнаружения сервисов. Чтобы адаптировать обнаружение «из коробки» к вашей среде, вы можете создать новые правила или настроить улучшения.

## Управление обнаружением сервисов на основе правил

Вы можете использовать правила трансформации, например, для решения следующих задач:

* Если идентификаторы веб-приложений содержат версию или дату сборки, вы можете определить правило, которое удаляет дату сборки/ID из идентификатора веб-приложения.
* Когда имена серверов неправильно определены в базовом развёртывании (например, Apache HTTP или Nginx в средах AWS), вы можете определить стабильное имя веб-сервера и, следовательно, стабильный кластерный сервис, содержащий все экземпляры.
* Вы можете исправить неправильное использование корневого контекста в развёрнутом приложении.

  Типичный веб-сервер имеет концепцию корневого контекста для разделения сервисов на основе URL. Для некоторых технологий, таких как Node.js, корневой контекст недоступен или неправильно определён. Вы можете наложить корневой контекст и создать отдельные сервисы для каждого из ваших приложений вместо одного сервиса, содержащего несколько приложений.
* Вы можете игнорировать порт при обнаружении сервиса. Это полезно, когда порт используется динамически, например, в приложениях Node.js.

Кроме того, правила можно экспортировать и импортировать из одной среды в другую.

Правила обнаружения оцениваются сверху вниз, и применяется первое совпавшее правило, поэтому убедитесь, что ваше правило расположено в правильной позиции в списке.

### Предварительные требования

* Ознакомьтесь с понятием [полного и внешнего (непрозрачного) запроса](/docs/discover-dynatrace/get-started/glossary#request "Ознакомьтесь с терминологией Dynatrace.").
* Только для APIТребуется Для настройки обнаружения сервисов на основе правил через [Settings API](/docs/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.") вам необходим токен доступа с правами **Read settings** (`settings.read`) и **Write settings** (`settings.write`). Чтобы узнать, как его получить, см. [Создание токена доступа](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Узнайте, как пройти аутентификацию для использования Dynatrace API.").

### Создание правила

Когда вы определяете новое правило, в зависимости от конфигурации исходные сервисы могут получать меньше трафика или вообще не получать его. Новые данные мониторинга затем перенаправляются в соответствии с конфигурацией правила между исходными и вновь обнаруженными сервисами.

через веб-интерфейс

через API

Для определения нового правила обнаружения сервиса через веб-интерфейс

1. Перейдите в **Settings**.
2. Разверните **Service Detection** и выберите тип запроса (**Full web request rules** или **Full web service rules**, или **External web request rules** или **External web service rules**).
3. Выберите **Add item** и начните настраивать параметры нового правила.

   1. Введите **Rule name**.
   2. Чтобы изменить поведение обнаружения сервиса, включите хотя бы один из участников идентификатора сервиса, чтобы правило сработало.
   3. Чтобы нацелить применение правила, в разделе **Conditions** настройте ограничения, связанные, например, с Management Zone, конкретными условиями или портом.
4. Выберите **Save changes**.

Эта процедура перезаписывает любую существующую конфигурацию. Если вы хотите изменить существующую конфигурацию, см. раздел [**Изменение правила**](#api-update) ниже.

Для определения нового правила обнаружения сервиса через API

1. Запросите схему настроек через вызов [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "Просмотр схемы настроек через Dynatrace API.") — он содержит информацию о параметрах, включённых в объект настроек.

   ID схемы зависит от типа запроса, как указано в таблице ниже.
2. Создайте JSON-объект для ваших настроек.

   Пример JSON для правила полного веб-запроса

   ```
   [



   {



   "schemaId":"builtin:service-detection.full-web-request",



   "scope":"environment",



   "value":{



   "enabled":true,



   "name":"Detect Application,Application-1 as the same",



   "description":"Example: merge services",



   "managementZones":["-8445121454707515572"],



   "idContributors":{



   "applicationId":{



   "enableIdContributor":true,



   "serviceIdContributor":{



   "contributionType":"TransformValue",



   "transformations": [



   {



   "transformationType":"REMOVE_NUMBERS",



   "minDigitCount":1,



   "includeHexNumbers":false



   }



   ]



   }



   },



   "contextRoot":{



   "enableIdContributor":false



   },



   "serverName":{



   "enableIdContributor":false



   }



   },



   "conditions": [



   {



   "attribute":"ApplicationId",



   "compareOperationType":"StringStartsWith",



   "textValues": ["application"],



   "ignoreCase":false



   }



   ]



   }



   }



   ]
   ```
3. Используйте вызов [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Создание или валидация объекта настроек через Dynatrace API.") для отправки вашей конфигурации.

### Изменение правила

Когда вы изменяете правило, некоторые сервисы могут перестать подпадать под его действие. В то время как исторические данные доступны только для предыдущего сервиса, все вновь собранные данные связываются с новым автономным сервисом.

через веб-интерфейс

через API

Для редактирования существующего правила через веб-интерфейс

1. Перейдите в **Settings**.
2. Разверните **Service Detection** и выберите тип запроса (**Full web request rules** или **Full web service rules**, или **External web request rules** или **External web service rules**).
3. Разверните ![Развернуть строку](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Развернуть строку") строку правила.
4. Отредактируйте настройки правила.
5. Выберите **Save changes**.

Для обновления существующего правила через API

1. Запросите схему настроек через вызов [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "Просмотр схемы настроек через Dynatrace API.") — он содержит информацию о параметрах, включённых в объект настроек.

   ID схемы зависит от типа запроса, как указано в таблице ниже.
2. Запросите текущую конфигурацию через вызов [GET objects](/docs/dynatrace-api/environment-api/settings/objects/get-objects "Просмотр нескольких объектов настроек через Dynatrace API.").
3. Создайте JSON-объект для обновления. Мы рекомендуем использовать **updateToken** из предыдущего объекта — это обеспечивает корректное версионирование ваших настроек.

   Пример JSON для правила полного веб-запроса

   ```
   [



   {



   "updateToken":"vu9U3hXY3q0ATAAkOWFiNGI2ZDAtYWFhNC00M2IwLWEzZDYtNDQ2OTZkNzIyYzE5ACRmMTA1NTJlMC01M2Q5LTExZWQtODAwMS0wMTAwMDAwMDAwMDO-71TeFdjerQ",



   "value":{



   "enabled":true,



   "name":"Detect Application, Application-1 as the same",



   "description":"Example: merge services",



   "managementZones":["-8445121454707515572"],



   "idContributors":{



   "applicationId":{



   "enableIdContributor":true,



   "serviceIdContributor":{



   "contributionType":"TransformValue",



   "transformations":[



   {



   "transformationType":"REMOVE_NUMBERS",



   "minDigitCount":1,



   "includeHexNumbers":false



   }



   ]



   }



   },



   "contextRoot":{



   "enableIdContributor":false



   },



   "serverName":{



   "enableIdContributor":false



   }



   },



   "conditions":[



   {



   "attribute":"ApplicationId",



   "compareOperationType":"StringStartsWith",



   "textValues":["application"],



   ///Added condition to ignore case sensitivity for texts.



   "ignoreCase":true



   }



   ]



   }



   }



   ]
   ```
4. Используйте вызов [PUT an object](/docs/dynatrace-api/environment-api/settings/objects/put-object "Редактирование объекта настроек через Dynatrace API.") для отправки вашей конфигурации.

### Удаление правила

Если вы удалите правило, все отдельные сервисы разделяются и снова рассматриваются как автономные сервисы.

через веб-интерфейс

через API

Для удаления правила обнаружения сервиса

1. Перейдите в **Settings**.
2. Разверните **Service Detection** и выберите тип запроса (**Full web request rules** или **Full web service rules**, или **External web request rules** или **External web service rules**).
3. В столбце **Delete** для соответствующей строки правила выберите **Delete row** ![Удалить](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Удалить")

Для удаления правила через API

1. Запросите список существующих правил через вызов [GET objects](/docs/dynatrace-api/environment-api/settings/objects/get-objects "Просмотр нескольких объектов настроек через Dynatrace API."). Укажите схему вашего типа запроса в параметре запроса **schemaIds**.
   ID схемы зависит от типа запроса, как указано в таблице ниже.
2. Найдите правило, которое хотите удалить, и скопируйте его **objectId**.
3. Удалите правило через вызов [DELETE an object](/docs/dynatrace-api/environment-api/settings/objects/del-object "Удаление объекта настроек через Dynatrace API."). Используйте ID объекта, полученный на предыдущем шаге.

### Примеры

#### Разделение полностью мониторируемых сервисов веб-запросов на основе URL или наложенного корневого контекста

Для некоторых технологий, мониторируемых Dynatrace, корневой контекст не поддерживается. По умолчанию обнаруживается один сервис на группу процессов. Вы можете изменить обнаружение сервиса, наложив корневой контекст на полностью мониторируемый веб-запрос.

В этом примере, когда путь URL полного веб-запроса начинается с определённого текста (`blog/`), мы хотим обнаружить сервис, идентификатор которого будет трансформирован в первый сегмент URL.

Настройка правила

через веб-интерфейс

через API

1. Перейдите в **Settings**.
2. Разверните **Service Detection** и выберите **Full web request rules**.
3. В правилах полных веб-запросов выберите **Add item**.
4. Настройте параметры следующим образом

   1. Введите **Rule name**.
   2. Необязательно Введите **Description**.
   3. Перейдите к **URL context root** и включите **Transform this value before letting it contribute to the Service ID**.

      1. Из списка **Contribution type** выберите **Use transformed URL path**.
      2. В поле **Segments to copy from URL path** введите количество сегментов URL, которые нужно сохранить (`1`).
   4. Перейдите к **Conditions** и выберите **Add item**.

      1. Из списка **Take the value of this attribute** выберите **URL path**.
      2. Из списка **Apply this operation** выберите **Starts with**.
      3. Перейдите к **Values** и выберите **Add item**, затем введите `blog/`.
5. Выберите **Save changes**.

```
[



{



"schemaId":"builtin:service-detection.full-web-request",



"scope":"environment",



"value":{



"enabled":true,



"name":"Dynatrace Blog",



"description":"Detect first segment of an URL path as service when it starts with blog/",



"managementZones":[],



"idContributors":{



"applicationId":{



"enableIdContributor":false



},



"contextRoot":{



"enableIdContributor":true,



"serviceIdContributor":{



"contributionType":"TransformURL",



"segmentCount":1,



"transformations":[]



}



},



"serverName":{



"enableIdContributor":false



}



},



"conditions":[



{



"attribute":"UrlPath",



"compareOperationType":"StringStartsWith",



"textValues":["blog/"],



"ignoreCase":false



}



]



}



}



]
```

#### Объединение данных приложения в один сервис на основе значения идентификатора приложения

Когда входящие данные нестабильны или недостаточно специфичны, вы можете использовать правила обнаружения сервисов для объединения сервисов, например, кластеров Apache HTTP в AWS без правильного виртуального хоста или идентификаторов веб-приложений, содержащих дату сборки.

В этом примере мы хотим объединить в один сервис все входящие данные от приложений, идентификатор которых начинается с `application`.

Настройка правила

через веб-интерфейс

через API

1. Перейдите в **Settings**.
2. Разверните **Service Detection** и выберите **Full web request rules**.
3. В правилах полных веб-запросов выберите **Add item**.
4. Настройте параметры следующим образом.

   1. Введите **Rule name**.
   2. Необязательно Введите **Description**.
   3. Выберите **Set a management zone** и укажите Management Zone из списка.
   4. Перейдите к **Application identifier** и включите **Transform this value before letting it contribute to the Service ID**.

      1. Из списка **Contribution type** выберите **Use transformed value**.
      2. Перейдите к **Transformations** и выберите **Add item**.

         1. Из списка **Transformation type** выберите **remove numbers**.
         2. Введите **min digit count** (`1`)
   5. Перейдите к **Conditions** и выберите **Add item**.

      1. Из списка **Take the value of this attribute** выберите **Application identifier**.
      2. Из списка **Apply this operation** выберите **Starts with**.
      3. Перейдите к **Values** и выберите **Add item**, затем введите `application`.
5. Выберите **Save changes**.

См. следующий [пример JSON](#eg_appId).

#### Разделение сервисов для «публичных сетевых сервисов» на основе URL

В этом примере, когда домен верхнего уровня внешнего веб-запроса заканчивается определённым текстом (`dynatrace.com`), мы хотим обнаружить сервис, идентификатор которого будет трансформирован в первый сегмент URL.

Настройка правила

через веб-интерфейс

через API

1. Перейдите в **Settings**.
2. Разверните **Service Detection** и выберите **External web request rules**.
3. В правилах внешних веб-запросов выберите **Add item**.
4. Настройте параметры следующим образом.

   1. Введите **Rule name**.
   2. Необязательно Введите **Description**.
   3. Перейдите к **URL context root** и включите **Transform this value before letting it contribute to the Service ID**.

      1. Из списка **Contribution type** выберите **Use transformed URL path**.
      2. В поле **Segments to copy from URL path** введите количество сегментов URL, которые нужно сохранить (`1`).
   4. Перейдите к **Public domain name** и отключите **Port**.
   5. Перейдите к **Conditions** и выберите **Add item**.

      1. Из списка **Take the value of this attribute** выберите **Top level domain**.
      2. Из выпадающего списка **Apply this operation** выберите **Ends with**.
      3. Перейдите к **Values** и выберите **Add item**, затем введите `dynatrace.com`.
      4. Чтобы игнорировать регистр, включите **Ignore case**.
5. Выберите **Save changes**.

```
[



{



"schemaId":"builtin:service-detection.external-web-request",



"scope":"environment",



"value":{



"enabled":true,



"name":"Dynatrace.com - based on URL",



"description":"Blog example: Dynatrace.com based on URL",



"managementZones":[],



"idContributors":{



"applicationId":{



"enableIdContributor":false



},



"contextRoot":{



"enableIdContributor":true,



"serviceIdContributor":{



"contributionType":"TransformURL",



"segmentCount":1,



"transformations":[]



}



},



"publicDomainName":{



"enableIdContributor":false



},



"portForServiceId":false



},



"conditions":[



{



"attribute":"TopLevelDomain",



"compareOperationType":"StringEndsWith",



"textValues":["dynatrace.com"],



"ignoreCase":true



}



]



}



}



]
```

#### Разделение сервисов для «публичных сетевых сервисов» на основе поддоменов

Если разные конечные точки не должны объединяться в один сервис (например, `support.dynatrace.com` и `blog.dynatrace.com`), вы можете указать Dynatrace обнаруживать несколько сервисов из одного домена на основе обнаруженного имени хоста вместо доменного имени запроса.

Настройка правила

через веб-интерфейс

через API

1. Перейдите в **Settings**.
2. Разверните **Service Detection** и выберите **External web request rules**.
3. В правилах внешних веб-запросов выберите **Add item**.
4. Настройте параметры следующим образом.

   1. Введите **Rule name**.
   2. Необязательно Введите **Description**.
   3. Перейдите к **Public domain name** и включите **Transform this value before letting it contribute to the Service ID**.

      1. Из списка **Contribution type** выберите **Use the original value**.
      2. Включите **Copy from host name**.
      3. Отключите **Port**.
   4. Перейдите к **Conditions** и выберите **Add item**.

      1. Из списка **Take the value of this attribute** выберите **Top level domain**.
      2. Из выпадающего списка **Apply this operation** выберите **Ends with**.
      3. Перейдите к **Values** и выберите **Add item**, затем введите `dynatrace.com`.
      4. Чтобы игнорировать регистр, включите **Ignore case**.
5. Выберите **Save changes**.

```
[



{



"schemaId":"builtin:service-detection.external-web-request",



"scope":"environment",



"value":{



"enabled":true,



"name":"Dynatrace.com - based on subdomains",



"description":"Blog example: Separate services for public network services based on subdomains ",



"managementZones":[],



"idContributors":{



"applicationId":{



"enableIdContributor":false



},



"contextRoot":{



"enableIdContributor":false



},



"publicDomainName":{



"enableIdContributor":true,



"serviceIdContributor":{



"contributionType":"OriginalValue",



"copyFromHostName":true



}



},



"portForServiceId":false



},



"conditions":[



{



"attribute":"TopLevelDomain",



"compareOperationType":"StringEndsWith",



"textValues":["dynatrace.com"],



"ignoreCase":true



}



]



}



}



]
```

## Улучшение обнаружения сервисов

### Проблемы с именованием веб-серверов

* В некоторых случаях веб-серверы не имеют чётко определённых виртуальных хостов, имён серверов или сайтов. Веб-сервер может называться просто `localhost`. Это может привести к появлению нескольких похожих сервисов, содержащих несколько экземпляров веб-сайтов. Для решения таких проблем настройте [параметры обнаружения групп процессов](/docs/observe/infrastructure-observability/process-groups/configuration/pg-monitoring#rules "Способы настройки мониторинга групп процессов").
* Когда на сервере Apache HTTP не настроен виртуальный хост, имя веб-сервера по умолчанию соответствует имени физического хоста. В облачных средах это приводит к созданию одного виртуального хоста для каждого физического экземпляра хоста и, следовательно, одного экземпляра сервиса. Если облачная среда запускает и останавливает хосты, эти сервисы будут временными.

  Для решения таких сценариев с localhost используйте переменную среды для определения имён виртуальных хостов: задайте `DT_LOCALTOVIRTUALHOSTNAME` для каждого процесса веб-сервера любое значение. Dynatrace подхватит эти имена и будет использовать их вместо существующих имён виртуальных хостов localhost. При таком подходе вы гарантируете, что несколько физических хостов сообщают одно и то же имя виртуального хоста и, таким образом, получается один сервис с несколькими экземплярами — по одному экземпляру на физический хост.

### Определение идентификаторов веб-приложений

Некоторые технологии не предоставляют уникальных имён приложений. В таких случаях вы можете определить переменную среды `DT_APPLICATIONID` для предоставления уникального имени. Это влияет только на сервисы соответствующего процесса, у которых ещё нет идентификаторов приложений. Для Java-приложений вы можете альтернативно использовать системное свойство `dynatrace.application.id`.

### Ротируемые и анонимные порты

Dynatrace учитывает порт прослушивания каждого сервиса веб-запроса при именовании и обнаружении запросов. В некоторых случаях эти порты не имеют значения или являются случайными, изменяясь при каждом перезапуске. Это особенно характерно при использовании балансировщика нагрузки, который динамически назначает порты процессам приложений, как это происходит во многих сценариях Node.js.

Для решения этой проблемы задайте переменную среды `DT_IGNOREDYNAMICPORT=true`. Это удаляет порт из обнаружения и заменяет его на `*`.

## Часто задаваемые вопросы

Что происходит с сервисом, если он не получает новых данных после создания/редактирования/удаления правила?

Когда вы создаёте, редактируете или удаляете правило, данные, собранные после изменения правил обнаружения сервисов, агрегируются и назначаются сервисам в зависимости от конфигурации правила. Если сервис перестаёт получать данные, его исторические данные остаются доступными (например, для построения графиков). Вы по-прежнему можете видеть сервис и его трассировки в вашей среде.

## Связанные темы

* [Объединённые сервисы](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types/merged-services "Консолидация нескольких сервисов веб-запросов одной группы процессов в один сервис.")
* [Settings API](/docs/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.")
* [API обнаружения сервисов](/docs/dynatrace-api/configuration-api/service-api/detection-rules "Узнайте, что предлагает API конфигурации правил обнаружения сервисов Dynatrace.")
* [[Блог] Новый Dynatrace API улучшает автоматическое обнаружение сервисов — с конкретными примерами](https://www.dynatrace.com/news/blog/new-dynatrace-api-enhances-automatic-service-detection/#how-to-use-the-new-api)