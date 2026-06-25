---
title: Правила обнаружения сервисов
source: https://docs.dynatrace.com/managed/observe/application-observability/services/service-detection/service-detection-v1/customize-service-detection
scraped: 2026-05-12T11:36:06.797426
---

# Правила обнаружения сервисов

# Правила обнаружения сервисов

* How-to guide
* 15-min read
* Updated on Apr 22, 2026

При мониторинге с помощью OneAgent развёрнутые приложения и связанные микросервисы автоматически обнаруживаются Dynatrace на основе конкретных свойств развёртывания и конфигурации приложения, таких как идентификатор приложения, часть URL или имя сервера.

Атрибуты, используемые для обнаружения, отмечены звёздочкой ✱ на странице обзора [сервиса](/managed/observe/application-observability/services-classic/service-analysis-new "Узнайте обо всех деталях мониторинга сервисов, которые может предоставить Dynatrace.") в разделе **Properties and tags**.

В некоторых случаях качество данных, доступных Dynatrace, может быть недостаточным для высокоточного обнаружения сервисов. Чтобы адаптировать обнаружение «из коробки» к своему окружению, можно создавать новые правила или настраивать улучшения.

## Управление обнаружением сервисов на основе правил

Правила преобразования можно использовать, например, для устранения следующих ситуаций:

* Если идентификаторы веб-приложений содержат версию или дату сборки, можно определить правило, удаляющее дату/ID сборки из идентификатора веб-приложения.
* Когда имена серверов неправильно определены в базовом развёртывании (например, с Apache HTTP или Nginx в окружениях AWS), можно определить стабильное имя веб-сервера и, следовательно, стабильный кластерный сервис, содержащий все экземпляры.
* Можно исправить неправильное использование корневого контекста в развёрнутом приложении.

  Типичный веб-сервер использует концепцию корневого контекста для разделения сервисов на основе URL. Для некоторых технологий, таких как Node.js, корневой контекст недоступен или неправильно определён. Можно наложить корневой контекст и создать отдельные сервисы для каждого из приложений вместо одного сервиса, содержащего несколько приложений.
* Можно игнорировать порт при обнаружении сервисов. Это удобно, когда порт используется динамически, например в приложениях Node.js.

Кроме того, правила можно экспортировать и импортировать из одного окружения в другое.

Правила обнаружения оцениваются сверху вниз, и применяется первое совпавшее правило, поэтому убедитесь, что правило размещено на правильной позиции в списке.

## Настройка правил обнаружения сервисов через пользовательский интерфейс

Правила обнаружения сервисов можно настроить через веб-интерфейс Dynatrace.

### Предварительные условия

Ознакомьтесь с понятием [полного и внешнего (непрозрачного) запроса](/managed/discover-dynatrace/get-started/glossary#request "Ознакомьтесь с терминологией Dynatrace.").

### Создание правила

При определении нового правила, в зависимости от конфигурации, исходные сервисы могут получать меньше трафика или не получать его вовсе. Новые данные мониторинга затем перенаправляются согласно конфигурации правила между исходными и вновь обнаруженными сервисами.

Чтобы определить новое правило обнаружения сервисов через веб-интерфейс Dynatrace

1. Перейдите в **Settings**.
2. Разверните **Service Detection** и выберите тип запроса (**Full web request rules**, **Full web service rules**, **External web request rules** или **External web service rules**).
3. Выберите **Add item** и начните настройку параметров нового правила.

   1. Введите **Rule name**.
   2. Чтобы изменить поведение обнаружения сервисов, включите хотя бы один из вкладчиков идентификаторов сервисов, чтобы правило срабатывало.
   3. Для задания области применения правила в разделе **Conditions** настройте ограничения, связанные, например, с зоной управления, конкретными условиями или портом.
4. Выберите **Save changes**.

### Изменение правила

При изменении правила на некоторые сервисы оно может перестать влиять. Хотя исторические данные доступны только для предыдущего сервиса, все вновь захватываемые данные затем связываются с новым самостоятельным сервисом.

Чтобы отредактировать существующее правило через веб-интерфейс Dynatrace

1. Перейдите в **Settings**.
2. Разверните **Service Detection** и выберите тип запроса.
3. Разверните ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") строку правила.
4. Отредактируйте настройки правила.
5. Выберите **Save changes**.

### Удаление правила

При удалении правила все отдельные сервисы разделяются и снова рассматриваются как самостоятельные.

Чтобы удалить правило обнаружения сервисов через веб-интерфейс Dynatrace

1. Перейдите в **Settings**.
2. Разверните **Service Detection** и выберите тип запроса.
3. В столбце **Delete** для соответствующей строки правила выберите **Delete row** ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove").

## Настройка правил обнаружения сервисов через Settings API

Также можно настроить правила обнаружения сервисов через [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.").

### Предварительные условия

* **Токен доступа**: необходим токен доступа с областями **Read settings** (`settings.read`) и **Write settings** (`settings.write`). О его получении см. в разделе [Создание токена](/managed/dynatrace-api/basics/dynatrace-api-authentication#create-token "Узнайте, как пройти аутентификацию для использования Dynatrace API.").
* **ID схемы**: вызовы Settings API требуют ID схемы настроек, которые нужно настроить.

  ID схемы зависит от типа запроса, как показано в следующей таблице.

  | Тип запроса | ID схемы |
  | --- | --- |
  | Full web request | [`builtin:service-detection.full-web-request`](/managed/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-full-web-request "Просмотрите таблицу схемы настроек builtin:service-detection.full-web-request вашего окружения мониторинга через Dynatrace API.") |
  | Full web service | [`builtin:service-detection.full-web-service`](/managed/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-full-web-service "Просмотрите таблицу схемы настроек builtin:service-detection.full-web-service вашего окружения мониторинга через Dynatrace API.") |
  | External web request | [`builtin:service-detection.external-web-request`](/managed/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-external-web-request "Просмотрите таблицу схемы настроек builtin:service-detection.external-web-request вашего окружения мониторинга через Dynatrace API.") |
  | External web service | [`builtin:service-detection.external-web-service`](/managed/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-external-web-service "Просмотрите таблицу схемы настроек builtin:service-detection.external-web-service вашего окружения мониторинга через Dynatrace API.") |

  Каждая связанная схема содержит информацию о типах и параметрах для конкретного типа правил.

### Получение списка всех правил

Для получения списка существующих правил через API используйте вызов [GET objects](/managed/dynatrace-api/environment-api/settings/objects/get-objects "Просмотрите несколько объектов настроек через Dynatrace API."). Укажите схему типа запроса в параметре запроса `schemaIds`.

```
GET /api/v2/settings/objects?schemaIds=builtin:service-detection.full-web-service
```

### Просмотр правила

Для получения сведений о конкретном правиле обнаружения сервисов через API используйте вызов [GET objects](/managed/dynatrace-api/environment-api/settings/objects/get-objects "Просмотрите несколько объектов настроек через Dynatrace API.") и укажите `objectId` нужного правила.

```
GET /api/v2/settings/objects/{objectId}
```

### Создание правила

Для создания нового правила обнаружения сервисов через API используйте запрос `POST` к конечной точке [POST an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Создайте или проверьте объект настроек через Dynatrace API.") и укажите ID схемы настроек и конфигурацию правила в теле запроса.

```
POST /api/v2/settings/objects
```

Пример JSON для правила full web request:

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

### Изменение правила

Для обновления существующего правила через API используйте запрос `PUT` к конечной точке [PUT an object](/managed/dynatrace-api/environment-api/settings/objects/put-object "Редактируйте объект настроек через Dynatrace API."). Укажите `objectId` обновляемого правила в URL и обновлённую конфигурацию правила в теле запроса.

```
PUT /api/v2/settings/objects/{objectId}
```

### Удаление правила

Для удаления правила обнаружения сервисов через API используйте запрос `DELETE` к конечной точке [DELETE an object](/managed/dynatrace-api/environment-api/settings/objects/del-object "Удалите объект настроек через Dynatrace API."). Укажите `objectId` удаляемого правила в URL.

```
DELETE /api/v2/settings/objects/{objectId}
```

### Изменение порядка правил

Для изменения порядка оценки правил обнаружения сервисов обновите каждое правило, установив поле `insertAfter` или `insertBefore` в ID объекта правила, которое должно предшествовать или следовать за ним. Чтобы разместить правило в начале списка, оставьте `insertAfter` пустым. Чтобы переместить его в конец, добавьте пустой атрибут `insertBefore`.

```
[



{



"schemaId": "builtin:service-detection.full-web-request",



"scope": "environment",



"value": {



"name": "New top rule",



"...": "..."



},



"insertAfter": ""



}



]
```

## Примеры настройки обнаружения сервисов

### Разделение полностью отслеживаемых сервисов веб-запросов на основе URL или наложенного корневого контекста

Для некоторых технологий, отслеживаемых Dynatrace, корневой контекст не поддерживается. По умолчанию обнаруживается один сервис на группу процессов. Можно изменить обнаружение сервисов, наложив корневой контекст на полностью отслеживаемый веб-запрос.

В этом примере, когда путь URL полного веб-запроса начинается с конкретного слова (`blog/`), нужно обнаружить сервис, ID которого будет преобразован в первый сегмент URL.

Настройка правила

через веб-интерфейс

через API

1. Перейдите в **Settings**.
2. Разверните **Service Detection** и выберите **Full web request rules**.
3. В правилах full web request выберите **Add item**.
4. Настройте параметры следующим образом:

   1. Введите **Rule name**.
   2. Необязательно Введите **Description**.
   3. Перейдите в **URL context root** и включите **Transform this value before letting it contribute to the Service ID**.

      1. В списке **Contribution type** выберите **Use transformed URL path**.
      2. В поле **Segments to copy from URL path** введите количество сегментов URL для сохранения (`1`).
   4. Перейдите в **Conditions** и выберите **Add item**.

      1. В списке **Take the value of this attribute** выберите **URL path**.
      2. В списке **Apply this operation** выберите **Starts with**.
      3. Перейдите в **Values**, выберите **Add item** и введите `blog/`.
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

### Объединение данных приложений в один сервис на основе значения идентификатора приложения

Когда входящие данные неустойчивы или недостаточно специфичны, можно использовать правила обнаружения сервисов для объединения сервисов, например кластеров Apache HTTP в AWS без правильно настроенного виртуального хоста или идентификаторов веб-приложений, содержащих дату сборки.

В этом примере нужно объединить в один сервис все входящие данные от приложений, чей ID начинается с `application`.

Настройка правила

через веб-интерфейс

через API

1. Перейдите в **Settings**.
2. Разверните **Service Detection** и выберите **Full web request rules**.
3. В правилах full web request выберите **Add item**.
4. Настройте параметры следующим образом:

   1. Введите **Rule name**.
   2. Необязательно Введите **Description**.
   3. Выберите **Set a management zone** и выберите зону управления из списка.
   4. Перейдите в **Application identifier** и включите **Transform this value before letting it contribute to the Service ID**.

      1. В списке **Contribution type** выберите **Use transformed value**.
      2. Перейдите в **Transformations** и выберите **Add item**.

         1. В списке **Transformation type** выберите **remove numbers**.
         2. Введите **min digit count** (`1`).
   5. Перейдите в **Conditions** и выберите **Add item**.

      1. В списке **Take the value of this attribute** выберите **Application identifier**.
      2. В списке **Apply this operation** выберите **Starts with**.
      3. Перейдите в **Values**, выберите **Add item** и введите `application`.
5. Выберите **Save changes**.

### Разделение сервисов для «сервисов публичной сети» на основе URL

В этом примере, когда домен верхнего уровня внешнего веб-запроса заканчивается определённым словом (`dynatrace.com`), нужно обнаружить сервис, ID которого будет преобразован в первый сегмент URL.

Настройка правила

через веб-интерфейс

через API

1. Перейдите в **Settings**.
2. Разверните **Service Detection** и выберите **External web request rules**.
3. В правилах external web request выберите **Add item**.
4. Настройте параметры следующим образом:

   1. Введите **Rule name**.
   2. Необязательно Введите **Description**.
   3. Перейдите в **URL context root** и включите **Transform this value before letting it contribute to the Service ID**.

      1. В списке **Contribution type** выберите **Use transformed URL path**.
      2. В поле **Segments to copy from URL path** введите количество сегментов URL для сохранения (`1`).
   4. Перейдите в **Public domain name** и отключите **Port**.
   5. Перейдите в **Conditions** и выберите **Add item**.

      1. В списке **Take the value of this attribute** выберите **Top level domain**.
      2. В раскрывающемся списке **Apply this operation** выберите **Ends with**.
      3. Перейдите в **Values**, выберите **Add item** и введите `dynatrace.com`.
      4. Для игнорирования регистра включите **Ignore case**.
5. Выберите **Save changes**.

### Разделение сервисов для «сервисов публичной сети» на основе поддоменов

Если различные конечные точки не должны объединяться в один сервис (например, `support.dynatrace.com` и `blog.dynatrace.com`), можно настроить Dynatrace на обнаружение нескольких сервисов из одного домена на основе обнаруженного имени хоста вместо доменного имени запроса.

Настройка правила

через веб-интерфейс

через API

1. Перейдите в **Settings**.
2. Разверните **Service Detection** и выберите **External web request rules**.
3. В правилах external web request выберите **Add item**.
4. Настройте параметры следующим образом:

   1. Введите **Rule name**.
   2. Необязательно Введите **Description**.
   3. Перейдите в **Public domain name** и включите **Transform this value before letting it contribute to the Service ID**.

      1. В списке **Contribution type** выберите **Use the original value**.
      2. Включите **Copy from host name**.
      3. Отключите **Port**.
   4. Перейдите в **Conditions** и выберите **Add item**.

      1. В списке **Take the value of this attribute** выберите **Top level domain**.
      2. В раскрывающемся списке **Apply this operation** выберите **Ends with**.
      3. Перейдите в **Values**, выберите **Add item** и введите `dynatrace.com`.
      4. Для игнорирования регистра включите **Ignore case**.
5. Выберите **Save changes**.

## Улучшение обнаружения сервисов

### Проблемы с именованием веб-серверов

* В некоторых случаях веб-серверы не имеют чётко определённых виртуальных хостов, имён серверов или сайтов. Веб-сервер может просто называться `localhost`. Это может привести к появлению нескольких похожих сервисов, содержащих несколько экземпляров веб-сайта. Для устранения таких проблем скорректируйте [настройки обнаружения группы процессов](/managed/observe/infrastructure-observability/process-groups/configuration/pg-monitoring#rules "Способы настройки мониторинга группы процессов").
* Когда на Apache HTTP-сервере не настроен виртуальный хост, имя веб-сервера по умолчанию совпадает с именем физического хоста. В облачных окружениях это приводит к одному виртуальному хосту на каждый физический хост и, следовательно, к одному экземпляру сервиса. Если облачное окружение запускает и останавливает хосты, эти сервисы будут временными.

  Для устранения таких сценариев с localhost используйте переменную окружения для определения имён виртуальных хостов: установите `DT_LOCALTOVIRTUALHOSTNAME` для каждого процесса веб-сервера в любое значение. Dynatrace подхватит имена и будет использовать их вместо существующих имён виртуальных хостов localhost. С таким подходом несколько физических хостов сообщают об одном виртуальном хосте и, таким образом, получают один сервис с несколькими экземплярами — по одному на физический хост.

### Определение идентификаторов веб-приложений

Некоторые технологии не предоставляют уникальные имена приложений. В таких случаях можно определить переменную окружения `DT_APPLICATIONID` для предоставления уникального имени. Это влияет только на сервисы соответствующего процесса, у которых ещё нет идентификаторов приложений. Для Java-приложений можно также использовать системное свойство `dynatrace.application.id`.

### Rotating и анонимные порты

Dynatrace учитывает порт прослушивания каждого сервиса веб-запросов при именовании и обнаружении запросов. В некоторых случаях эти порты не несут смысла или являются случайными и меняются при каждом перезапуске. Это особенно характерно при использовании балансировщика нагрузки, который динамически назначает порты процессам приложений, как в многих сценариях Node.js.

Для устранения этого установите переменную окружения `DT_IGNOREDYNAMICPORT=true`. Это удалит порт из обнаружения и заменит его на `*`.

## Часто задаваемые вопросы

Что произойдёт, если сервис не получает новые данные после создания/редактирования/удаления правила?

При создании, редактировании или удалении правила данные, отслеживаемые после изменения правил обнаружения сервисов, агрегируются и назначаются сервисам в зависимости от конфигурации правила. Если сервис перестаёт получать данные, его исторические данные остаются доступными (например, для построения диаграмм). Сервис и его трассировки по-прежнему видны в окружении.

## Связанные темы

* [Объединённые сервисы](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/merged-services "Объедините несколько сервисов веб-запросов одной группы процессов в один сервис.")
* [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.")
* [API обнаружения сервисов](/managed/dynatrace-api/configuration-api/service-api/detection-rules "Узнайте, что предлагает Dynatrace API конфигурации правил обнаружения сервисов.")
* [[Блог] Новый API Dynatrace улучшает автоматическое обнаружение сервисов — с конкретными примерами](https://www.dynatrace.com/news/blog/new-dynatrace-api-enhances-automatic-service-detection/#how-to-use-the-new-api)