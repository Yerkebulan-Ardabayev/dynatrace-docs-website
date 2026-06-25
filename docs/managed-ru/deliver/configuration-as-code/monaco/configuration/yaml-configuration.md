---
title: YAML-конфигурация Monaco
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/monaco/configuration/yaml-configuration
scraped: 2026-05-12T12:35:14.056800
---

# Monaco YAML Configuration

# Monaco YAML Configuration

* Overview
* 20-min read
* Updated on Jul 25, 2025

Каждый файл конфигурации YAML содержит список конфигураций для развёртывания.

Базовый файл конфигурации YAML выглядит следующим образом:

```
configs:



- id: test-dashboard



type:



api: dashboard



config:



name: Test Dashboard



template: dashboard.json



parameters:



owner: Test User
```

Как видно, элемент верхнего уровня — `configs`. Его значение представляет собой список конфигураций. Каждая конфигурация требует следующих полей: `id`, `type` и `config`.

Также возможно переопределять значения из `config` на уровне окружения и группы окружений. Для этого предусмотрены необязательные поля `groupOverrides` и `environmentOverrides`.

## ID

Поле `id` идентифицирует конфигурацию в наборе конфигураций. Оно должно быть уникальным для одного configType и одного проекта. Таким образом, возможно иметь, например, два дашборда с одинаковым `id` в двух разных проектах. Обратите внимание, что это поле является локальным для Dynatrace Monaco CLI и не связано с идентификатором, предоставляемым Dynatrace API. Одно из важных применений этого `id` — использование [параметров-ссылок](#reference).

## Type

Поле `type` определяет тип конфигурации Dynatrace.

`type` может быть одним из поддерживаемых [типов конфигурации](/managed/deliver/configuration-as-code/monaco/reference/supported-configuration "Configuration types and access permissions for Dynatrace Configuration as Code via Monaco").

### Type — API

`type` типа API можно определить как:

```
type:



api: dashboard
```

или в краткой форме:

```
type: dashboard
```

Список всех допустимых значений `api` см. в [поддерживаемых типах конфигурации](/managed/deliver/configuration-as-code/monaco/reference/supported-configuration "Configuration types and access permissions for Dynatrace Configuration as Code via Monaco").

#### Параметр scope

Некоторые конфигурации типа API имеют отношение родитель-потомок с другой конфигурацией. Такие конфигурации требуют поля `scope`, указывающего на родительскую конфигурацию.

[Параметр](#parameters) `scope` может быть определён как параметр [value](#value), [reference](#reference) или [environment](#environment).

Поскольку такие конфигурации создаются в области видимости родительского API, ссылка на ID родительской конфигурации является удобным способом настройки сущностей после их создания через Dynatrace Monaco CLI.

В примере ниже настраивается мобильное приложение, после чего задаются ключевые действия пользователя для этого приложения.

```
configs:



- id: mobile-application-id



config:



name: my-mobile-app



template: mobile-app.json



skip: false



type:



api: application-mobile



- id: MyKua



type:



api:



name: key-user-actions-mobile



template: kua.json



scope:



configId: mobile-application-id



configType: application-mobile



property: id



type: reference
```

### Type — Settings

[Settings](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") определяются через `schema`, `scope` и необязательный `schemaVersion`.

`type` типа settings можно определить как:

```
type:



settings:



schema: builtin:tags.auto-tagging



scope: environment
```

`schema` и `schemaVersion` задаются как обычный текст.

#### Параметр scope

[Параметр](#parameters) `scope` может быть определён как параметр [value](#value), [reference](#reference) или [environment](#environment).

В приведённом выше примере он задан как краткий параметр [value](#value) со значением `environment`, создавая настройку в области видимости всего окружения Dynatrace.

Поскольку многие настройки создаются в области видимости сущности Dynatrace, ссылка на ID другой конфигурации является удобным способом настройки сущностей после их создания через Dynatrace Monaco CLI.

В примере ниже настраивается веб-приложение, после чего задаются настройки для этого приложения.

```
configs:



- id: MyApp



type:



api: application-web



config:



name: My Sample Web Application



template: application.json



- id: MyApp_RUMSettings



type:



settings:



schema: builtin:rum.web.enablement



scope:



type: reference



configType: application-web



configId: MyApp



property: id



config:



name: MyApp_RUMSettings



template: rum-settings.json
```

Как видно, `scope` настройки `rum.web.enablement` является ссылкой на веб-приложение.

#### Параметр insertAfter

Dynatrace Monaco CLI версии 2.14.0+

Для обеспечения заданного порядка объектов Settings 2.0 используйте [параметр](#parameters) `insertAfter`.
При развёртывании Monaco гарантирует, что объект settings будет развёрнут после указанного.

Параметр `insertAfter` можно использовать для:

* Определения параметра [reference](#reference) для вставки после другой конфигурации Monaco.
* Определения параметра [value](#value) для задания жёстко заданного ID, после которого должна быть добавлена конфигурация. Dynatrace Monaco CLI версии 2.21.0+
* Значение `front` или `back` используется для добавления конфигурации в начало или конец списка. Dynatrace Monaco CLI версии 2.21.0+

Пример с ссылкой

Пример с жёстко заданным ID

Пример с front/back

```
type:



settings:



schema: builtin:container.monitoring-rule



schemaVersion: 0.0.1



scope: environment



insertAfter:



configId: c2314e1b-409c-3eaf-9efa-5dc593b14aff  # Monaco config id



property: id                                    # Dynatrace id property of the referenced config (must be "id")



type: reference                                 # reference type parameter (must be "reference")
```

```
type:



settings:



schema: builtin:container.monitoring-rule



schemaVersion: 0.0.1



scope: environment



insertAfter:



value: 43e637dd-ca80-4593-94c4-e2077717555e # hardcoded ID of the configuration this configuration should be inserted AFTER



type: value                                 # value type parameter (must be "value")
```

```
type:



settings:



schema: builtin:container.monitoring-rule



schemaVersion: 0.0.1



scope: environment



insertAfter: front  # or `back` to add this configuration to the front or back of the other configurations
```

Если более одной конфигурации или проекта Monaco определяет `front` или `back`, не гарантируется, какая конфигурация окажется самой первой или последней.

#### Параметр permissions

Dynatrace Monaco CLI версии 2.23.0+

Используйте опцию разрешений `allUsers` для задания прав доступа (`no access`, `read access` или `write access`) для определённых объектов settings.

Опция `allUsers` принимает следующие значения:

* `none`: владелец имеет полный доступ к объекту settings, остальные пользователи — нет.
* `read`: владелец имеет полный доступ к объекту settings, остальные пользователи — только чтение.
* `write`: все пользователи имеют полный доступ к объекту settings.

Пользователям необходимы разрешения `settings:objects:read` и `settings:objects:write` для чтения и записи settings.

Даже если разрешение `allUsers` установлено в `write`, пользователи всё равно должны иметь необходимые права для просмотра и редактирования объектов settings.

Пример: нет доступа

Пример: только чтение

Пример: чтение и запись

```
type:



settings:



schema: app:your-owner-based-access-control-app:your-schema-id



schemaVersion: 0.0.1



scope: environment



permissions:



allUsers: none
```

```
type:



settings:



schema: app:your-owner-based-access-control-app:your-schema-id



schemaVersion: 0.0.1



scope: environment



permissions:



allUsers: read
```

```
type:



settings:



schema: app:your-owner-based-access-control-app:your-schema-id



schemaVersion: 0.0.1



scope: environment



permissions:



allUsers: write
```

## Config

Поле `config` предоставляет следующие поля:

* `name` — имя для идентификации объектов в Dynatrace API
* `template` — определяет файл шаблона для формирования запроса к Dynatrace API (подробнее см. [Управление проектом Monaco](/managed/deliver/configuration-as-code/monaco/configuration/projects "Manage a project folder with Dynatrace Configuration as Code via Monaco."))
* Необязательный `skip` — если установлен в `true`, Dynatrace Monaco CLI не будет развёртывать данную конфигурацию
* Необязательный `parameters` — список параметров, доступных в шаблоне
* Необязательный `originObjectId` — задаётся при загрузке; это поле определяет ID объекта конфигурации Dynatrace, из которого происходит данная конфигурация. Используется при развёртывании как дополнительный идентификатор.

### Name

* Dynatrace Monaco CLI версии 2.6.0 и ранее — свойство `name` обязательно и должно быть определено для всех типов конфигурации.
* Dynatrace Monaco CLI версии 2.7.0+ — свойство `name` обязательно только для конфигураций типа API и необязательно для других типов.

#### Для типа API

Для конфигураций [типа API](/managed/deliver/configuration-as-code/monaco/configuration/yaml-configuration#type-config-api "Learn how to set up your Monaco YAML configuration.") `name` используется для идентификации конфигураций в окружении Dynatrace и обеспечения их обновления при повторном существовании.

Для этого `name` необходимо использовать в [JSON-шаблоне](/managed/deliver/configuration-as-code/monaco/configuration/projects#json-template-file "Manage a project folder with Dynatrace Configuration as Code via Monaco.") для заполнения конкретного свойства имени конфигурации. Обычно это тоже `name`, но для некоторых конфигураций это может отличаться; см. специальные случаи в [JSON-шаблонах](/managed/deliver/configuration-as-code/monaco/configuration/projects#json-template-file "Manage a project folder with Dynatrace Configuration as Code via Monaco.") и обратитесь к [документации API](/managed/dynatrace-api "Find out what you need to use the Dynatrace API.") при сомнениях.

При ссылке на `name` в JSON-шаблоне его необходимо использовать как есть, без дополнительного текста или символов вокруг.

Свойство name в JSON всегда должно использоваться следующим образом:

```
"{{ .name }}"
```

Если конфигурации создаются повторно вместо обновления, проверьте, что ссылка на имя не содержит случайных пробелов или других символов, из-за которых значение, отправляемое в Dynatrace в JSON, отличается от имени, определённого в YAML.

#### Для других типов конфигурации

Свойство `name` не используется для идентификации объектов Dynatrace. Вместо этого используются координата конфигурации (комбинация проекта, типа и ID конфигурации) или `originObjectId` (при наличии).

### Skip

Поле `skip` позволяет пропускать развёртывание определённой конфигурации. Если `skip` установлен в `true`, Dynatrace Monaco CLI не будет развёртывать данную конфигурацию.

Поле `skip` ведёт себя как [параметр](#parameters) и может быть определено как параметр [value](#value) или [environment](#environment). Обычно оно задаётся непосредственно как краткая форма [value](#value), как показано в нескольких примерах.

Часто полезно в сочетании с [переопределениями окружений](#env-overrides), когда нужно развернуть конфигурацию в одном окружении, но исключить её из другого.

### Parameters

Параметры используются для предоставления значений в шаблонах конфигурации. Они определяются как YAML-объекты с записью `type`. Этот `type` определяет интерпретацию объекта параметра. Важное свойство параметров — ленивая оценка: значение параметра вычисляется только если на него ссылается конфигурация, которая будет развёрнута.

Доступны следующие типы параметров:

* [Value](#value)
* [Environment](#environment)
* [Reference](#reference)
* [Compound](#compound)
* [List](#list)
* [File](#file)

#### Value

Параметр value — простейший тип параметра. Помимо свойства `type`, он также требует свойства `value`. Значение может быть любым, включая вложенные словари. Это значение доступно в файле шаблона.

Поскольку параметры `value` являются наиболее распространённым типом, для их определения существует специальная краткая форма синтаксиса: можно просто указать значение, если параметр не является массивом или словарём.

Например:

```
parameters:



threshold: 15



complexThreshold:



type: value



value:



amount: 15



unit: sec
```

В шаблоне данной конфигурации доступ к параметру `threshold` осуществляется через `{{ .threshold }}`. Для доступа, например, к `amount` параметра `complexThreshold` используется `{{ .complexThreshold.amount }}`.

#### Environment

Параметры типа `environment` позволяют ссылаться на переменную окружения. Имя переменной окружения указывается через свойство `name`.

* Можно задать значение по умолчанию (через свойство `default`) на случай отсутствия переменной окружения.
* Если свойство `default` не задано и переменная окружения отсутствует, параметр не может быть вычислен. Это приведёт к ошибке развёртывания.

  Это актуально только если параметр нужен для развёртывания. Параметры, на которые не ссылается конфигурация для развёртывания, не вычисляются.

Пример:

```
parameters:



owner:



type: environment



name: OWNER



default: "-"



target:



type: environment



name: TARGET
```

В приведённом примере:

* Параметр `owner` принимает значение переменной окружения `OWNER`. Если переменная отсутствует, используется значение `-`.
* Параметр `target` принимает значение переменной окружения `TARGET`. Если переменная не задана на момент развёртывания, развёртывание завершится ошибкой.

#### Reference

Поскольку часто необходимо ссылаться на свойство другой конфигурации, Dynatrace Monaco CLI предоставляет специальный тип параметра `reference`, позволяющий одной конфигурации зависеть практически от любого параметра другой.

Для использования параметра типа `reference` необходимо указать следующие обязательные поля:

* `project` — имя проекта конфигурации, на которую ссылается параметр.
* `configType` — тип конфигурации, на которую ссылается параметр.

  Для конфигураций типа `settings` значение `configType` должно соответствовать ID схемы (например, `builtin:tags.auto-tagging`).
* `configId` — ID конфигурации, на которую ссылается параметр.
* `property` — имя поля для определения значения параметра.

  Если `property` задан как `id` или `name`, параметр разрешается в фактический ID или имя объекта Dynatrace.

В примере ниже значение `mz_id` будет Dynatrace object ID конфигурации типа `management-zone` с ID `management-zone-config` из проекта `project-1`:

```
parameters:



mz_id:



type: reference



project: project-1



configType: management-zone # or builtin:management-zones if referencing "settings" type configurations



configId: management-zone-config



property: id
```

Dynatrace Monaco CLI гарантирует упорядоченное развёртывание конфигурации: зависимая конфигурация развёртывается первой.

При наличии циклических зависимостей развёртывание завершится ошибкой.

##### Краткая запись

Поскольку параметры `reference` являются одним из наиболее распространённых типов, для их определения существует специальная краткая форма синтаксиса в виде массива:

* Синтаксис: `[ <project>, <configType>, <configId>, <property> ]`
* Пример: `mz_id: ["project-1", "management-zone", "main", "id"]`

Обратите внимание: в этом случае `type` не требуется, поскольку тип определяется по синтаксису.

#### Частичные ссылки

Можно опускать некоторые поля ссылки. В этом случае они принимают то же значение, что и у текущей конфигурации.

Как правило, это удобно для ссылок на конфигурации в пределах одного `project` — просто опустите соответствующее поле.

```
parameters:



mz_id:



type: reference



configType: management-zone



configId: main



property: id
```

Хотя можно опустить `configType` и даже `configId`, обратите внимание, что можно оставить пустым только самый верхний уровень без пропусков в цепочке.
Таким образом, если `configType` опущен, то и `project` тоже должен быть опущен.

Ниже представлен полный пример (с использованием кратких ссылок):

* `infrastructure/management-zone/config.yaml`

  ```
  configs:



  - id: main



  type:



  api: management-zone



  config:



  name: "Main zone"



  template: "zone.json"
  ```
* `development/management-zone/config.yaml`

  ```
  configs:



  - id: development



  type:



  api: management-zone



  config:



  name: "Development zone"



  template: "zone.json"
  ```
* `development/dashboard/config.yaml`

  ```
  configs:



  - id: a_dashboard



  type:



  api: dashboard



  config:



  name: "Overview dashboard"



  template: "dashboard.json"



  - id: overview



  type:



  api: dashboard



  config:



  name: "Overview dashboard"



  template: "dashboard.json"



  parameters:



  zoneId: ["infrastructure", "management-zone", "main", "id"]



  devZoneId: ["management-zone", "development", "id"] # inferred project 'development'



  otherDashboard: ["a_dashboard", "id"] # inferred project 'development' and type 'dashboard'
  ```

#### Compound

Параметр compound — это параметр, составленный из других параметров той же конфигурации. Этот параметр требует двух свойств:

* Строку `format`
* Список `references` на все используемые параметры.

Строка `format` может быть любой строкой. Для использования параметров в ней используется синтаксис `{{ .parameter }}`, где `parameter` — имя подставляемого параметра.

Например:

```
parameters:



example:



type: compound



format: "{{ .greeting }} {{ .entity }}!"



references:



- greeting



- entity



greeting: "Hello"



entity: "World"
```

Это даст значение `Hello World!` для `example`. Составные параметры также можно использовать для более сложных значений, как в следующем примере:

```
parameters:



example:



type: compound



format: "{{ .resource.name }}: {{ .resource.percent }}%"



references:



- resource



progress:



type: value



value:



name: "Health"



percent: 40
```

Это даст значение `Health: 40%`, например.

Хотя параметры по ссылке могут быть только из той же конфигурации, через использование параметра reference возможно создать составной параметр с другими конфигурациями.
Это также справедливо для переменных окружения.

```
parameters:



example:



type: compound



format: "{{ .user }}'s dashboard is {{ .status }}"



references:



- user



- status



user:



type: environment



name: USER_NAME



status:



type: reference



configType: dashboard



configId: dashboard



property: status
```

#### List

Параметры типа `list` позволяют определять списки параметров [value](#value). При записи в шаблон они записываются как JSON-список в квадратных скобках через запятую.

Этот тип параметра удобен, когда требуется простой список значений, например адресов электронной почты или идентификаторов, которые могут быть заполнены любым параметром типа value.

Например:

```
parameters:



recipients:



type: list



values:



- first.last@company.com



- someone.else@company.com



geolocations:



type: list



values: ["GEOLOCATION-1234567", "GEOLOCATION-7654321"]
```

Как показано в примере, значения списка можно определять построчно или в виде массива в YAML.

При использовании параметра типа list в JSON-шаблоне убедитесь, что ссылка на значение указывается без дополнительных скобок.

```
{



"emails": {{ .recipients }}



}
```

Это отличается от иногда используемого строкового списка в v1, где шаблон требовал квадратных скобок (например, `"emails": [ {{ .recipients }} ]`).

#### File

Dynatrace Monaco CLI версии 2.14.0+

Параметры типа `file` позволяют загружать содержимое из файла на диске.

Пример:

```
parameters:



comment: "// hello special comment"



myWf:



type: file        # parameter type "file"



path: "myWf.js"   # relative path to the file



references:       # other parameters names referenced in the content of the file



- comment
```

В данном примере параметр с именем `myWf` динамически разрешается в содержимое файла `myWf.js`, расположенного относительно текущего местонахождения конфигурации. На этот параметр можно ссылаться в JSON-шаблоне следующим образом:

```
{



"script" : {{ .myWf }}



}
```

Кроме того, в содержимом указанного файла можно использовать ссылки на другие параметры. Каждый параметр по ссылке должен быть определён как отдельный параметр и указан в разделе references параметра типа file.

В данном примере дополнительный параметр с именем `comment` можно использовать в содержимом, указанном параметром file, через нотацию `{{ .comment }}`.

### OriginObjectID

При использовании Dynatrace Monaco CLI для загрузки существующих конфигураций из Dynatrace созданные YAML-файлы содержат `originObjectId` для некоторых типов конфигурации.

Это поле хранит ID конкретного объекта Dynatrace, который был загружен. Оно используется при повторном развёртывании загруженной конфигурации в то же окружение Dynatrace для обеспечения корректного обновления существующего объекта.

Например, уже существующий объект Settings 2.0 будет дополнен [данными для его корректной идентификации](/managed/deliver/configuration-as-code/monaco/configuration/special-configuration-types#settings-2-0-objects "Dynatrace Configuration as Code via Monaco - special configuration types.").

Обратите внимание, что `originObjectId` необязателен, и как правило не требует внимания или изменения.

### Экранирование строк в конфигурации

В целом все YAML-значения экранируются перед добавлением в конфигурацию, загружаемую в Dynatrace. Это гарантирует, что полностью заполненные шаблоны являются корректным JSON при загрузке. Все переносы строк, специальные символы (например, двойные кавычки) и т.п. экранируются.

```
parameters:



name: "Dev"



example1: "This is \\n already escaped"



example2: "This will \n be escaped"



example3: This "will" be escaped too



text: |



This will also



be escaped
```

## Переопределение конфигурации для отдельных окружений

Во многих случаях конфигурация похожа, но не идентична для разных окружений. Примеры:

* Оповещение отправляется в разные Slack-каналы для staging и production окружений
* Конфигурацию сервиса следует пропустить, поскольку он ещё не выпущен

Для этого можно переопределять значения конфигурации на уровне окружения и группы окружений с помощью полей `groupOverrides` и `environmentOverrides`.

Оба поля в целом определяются одинаково, отличаясь лишь тем, применяются ли они к группе или к одному окружению. Можно определить название группы/окружения для нацеливания и любые свойства конфигурации для изменения.

В примере ниже для двух окружений применяется специальная конфигурация, а `skip` гарантирует, что конфигурация не будет развёрнута в группе `production-environments`:

```
configs:



- id: test-dashboard



type:



api: dashboard



config:



name: Test Dashboard



template: dashboard.json



parameters:



owner: Test User



content: "Some Text ..."



environmentOverrides:



- environment: dev-env-42



override:



name: Special Dev Dashboard



parameters:



content: "Some even better Text!"



- environment: staging-env-21



override:



name: Special Staging Dashboard



parameters:



content: "Some much better Text!"



groupOverrides:



- group: production-environments



override:



skip: true
```