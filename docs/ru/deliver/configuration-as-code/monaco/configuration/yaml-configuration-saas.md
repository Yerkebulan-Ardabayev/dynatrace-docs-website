---
title: Структура YAML-файла конфигурации Monaco
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/monaco/configuration/yaml-configuration-saas
scraped: 2026-03-06T21:28:37.690091
---

* Latest Dynatrace

YAML-файл `configs` содержит список конфигураций для развёртывания.

Вот базовый пример YAML-файла `configs` для SLO:

```
configs:


- id: newSLO


type: slo-v2


config:


parameters:


target: 95


title: myNewSLO


entityScope: HOST-#######


template: slo-cpu-usage.json


skip: false
```

Вот базовый пример YAML-файла `slo-cpu-usage.json` для SLO:

```
{


"name": "{{ .title }}",


"description": "test SLO for template test",


"tags": [],


"customSli": {


"filterSegments": [],


"indicator": "timeseries sli=avg(dt.host.cpu.usage)\n, by: { \"{{ .entityScope }}\" }


\n  , filter: in(dt.entity.host, { $hosts })\n  | fieldsAdd entityName(dt.entity.host)"


},


"criteria": [


{


"target": {{ .target }},


"timeframeFrom": "now-7d",


"timeframeTo": "now",


"warning": 99


}


]


}
```

Элемент верхнего уровня в файле конфигурации — `configs`. Его значение — список конфигураций.

Обязательно. Каждая конфигурация требует следующих полей: `id`, `type` и `config`.

Вы можете переопределять значения из `config` на уровне окружения и группы окружений.
Для этого используются необязательные поля `groupOverrides` и `environmentOverrides`.

## Поле `id`

Поле `id` идентифицирует `config` внутри конфигураций.
Оно должно быть уникальным для одного и того же configType и [проекта](monaco-manage-resources.md#projects "Список ресурсов Monaco.").
Это поле необходимо для ссылки на [параметры](../monaco-api-support-and-access-handling.md#supported-api-types "Список поддерживаемых API Monaco и обработки прав доступа.") и описания зависимостей между отдельными конфигурациями.

Допускается наличие, например, двух дашбордов с одинаковым `id`, но в разных проектах.

Поле `id` является локальным для Dynatrace Monaco CLI и не соответствует идентификатору, предоставляемому Dynatrace API.

## Поле `type`

Поле `type` определяет тип конфигурации Dynatrace.

Подробный список см. в разделе YAML-файл конфигурации Monaco — список полей типов.

Типы и подкатегории

* `API`: выбранные Dynatrace API.
  Дополнительную информацию см. в разделе [Поддержка API Monaco и обработка прав доступа](../monaco-api-support-and-access-handling.md#supported-api-types "Список поддерживаемых API Monaco и обработки прав доступа.").

  + `scope`
* `Settings API`

  + `Scope`
  + `Schema`
  + Необязательный `Schema version`
  + Необязательный `insertAfter`

    Не все схемы **Settings** поддерживают разрешения. Применимо только для объектов на основе схем с упорядоченными объектами. Параметр ordered схемы установлен в `true`.
    Дополнительную информацию см. в разделе Объект SettingsObjectUpdate.
  + Необязательный `permission`

    Не все схемы **Settings** поддерживают разрешения. Применимо только для объектов на основе схем с упорядоченными объектами. Параметр ordered схемы установлен в `true`.
    Дополнительную информацию см. в разделе Объект SettingsObjectUpdate.
* `Automation` определяет рабочий процесс (workflow).

  + `resource`
* `Bucket` определяет корзины хранения Grail для хранения данных.
* `Document` определяет дашборд, блокнот и панель запуска.

  + `kind`
  + Необязательный `private`
  + Необязательный `id`
* `OpenPipeline` настраивает потоки приёма данных Dynatrace.

  + `kind`

Dynatrace версии 1.323+ API конфигураций OpenPipeline заменён специализированными схемами Settings API. Чтобы избежать следующих ограничений, выполните миграцию на новый формат, см. Миграция конфигураций OpenPipeline на Settings API. Если вы уже используете новые схемы Settings API, обратитесь к разделу [Тип - Settings](#type-setting).

* `Segment` определяет сегменты данных и маски фильтров.
* `Service-level objectives (SLOs)` настраивает SLO в Dynatrace.

### Дополнительные и необязательные поля

В зависимости от `type` конфигурации может потребоваться определить дополнительные поля или добавить необязательные поля.

Не все поля доступны для всех типов.

Поля `type` конфигурации

* `scope`: применимо для типов `api` и `settings`.
  Позволяет указывать зависимости и связи.
* `schema` и `schemaVersion`: применимо для типа `settings`.
  Определяет конкретную схему настроек, например пользовательские оповещения.
* `permission`: применимо для типа `settings`.
  Позволяет осуществлять детальный контроль доступа к объектам настроек на основе IAM-разрешений.
* `insertAfter`: применимо для типа `settings`.
  Позволяет задать пользовательский порядок объектов Settings.
* `resource`: применимо для типа `automation`.
  Определяет подкатегорию сервиса автоматизации.
* `kind`: применимо для типов `document` и `openpipeline`.
  Указывает вид или категорию типа конфигурации.
* `private`: применимо для типа `document`.
  Определяет доступность/видимость документа в окружении, например, публичный или приватный.
* `id`: применимо для типа `document`.
  Указывает пользовательский идентификатор для документа.
  Если он указан, его также необходимо напрямую использовать в файле удаления, если вы хотите удалить документ позже.
  При создании документа, если это поле не задано, Monaco генерирует пользовательский идентификатор.
  При скачивании поле `id` заполняется, если для создания документа использовался пользовательский идентификатор.

## Поле `config`

Поле `config` определяет единичный экземпляр конфигурации выбранного типа и ссылается на JSON-шаблон, содержащий JSON-полезную нагрузку, загружаемую в конечные точки Dynatrace API.

Следующие поля

* Обязательное `name`: идентифицирует объекты конфигурации в Dynatrace API.
* Обязательное `template`: ссылается на файл шаблона для рендеринга запроса к Dynatrace API.
* Необязательное `skip`: указывает, следует ли развёртывать конфигурацию или нет.
* Необязательное `parameters`: определяет параметры, передаваемые в шаблон.
* Необязательное `originObjectId`: автоматически устанавливается при скачивании объектов конфигурации.
  Dynatrace Monaco использует его как дополнительный идентификатор для обновления существующего ресурса при повторном развёртывании.

### Экранирование строк в конфигурации

Все значения YAML обычно экранируются перед добавлением в конфигурацию и загрузкой в Dynatrace.
Экранирование строк гарантирует, что заполненные шаблоны являются валидным JSON при загрузке.
Символы перевода строки, специальные символы, такие как двойные кавычки, экранируются.

```
parameters:


name: "Dev"


example1: "This is \\n already escaped."


example2: "This will \n be escaped."


example3: This "will" be escaped too.


text: |


This will also


be escaped.
```

### Свойство `name`

Dynatrace Monaco CLI версии 2.6.0 и ранее — свойство `name` является обязательным. Его необходимо определять для всех типов конфигурации.

Dynatrace Monaco CLI версии 2.7.0+ — свойство `name` обязательно только для конфигураций типа API и является необязательным для других типов конфигурации.

#### Конфигурации типа `api`

Если указанная конфигурация является [типом api](yaml-configuration-saas-type-fields.md#type-field "Список полей типов в YAML-файле конфигурации Monaco."), `name` используется для идентификации конфигураций в окружении Dynatrace и обеспечения их обновления при наличии.

Для этого `name` необходимо использовать в JSON-шаблоне для заполнения соответствующего свойства `name` конфигурации.
Обычно это тоже просто `name`, но для некоторых конфигураций может отличаться.
Дополнительную информацию см. в описании исключительных случаев для JSON-шаблонов Работа с командами Dynatrace Monaco CLI для Latest Dynatrace и обратитесь к документации API в случае сомнений.

При [скачивании](../reference/commands-saas.md#download "Как использовать CLI-приложение Monaco, включая аргументы и опции.") имена автоматически извлекаются и помещаются в YAML.

При ссылке на имя в JSON-шаблоне его необходимо использовать как есть, без дополнительного текста или символов вокруг него.

Используйте свойство `name` в JSON следующим образом: `"{{ .name }}"`.

Если вы столкнулись с проблемами, когда конфигурации создаются несколько раз вместо обновления, убедитесь, что ваша ссылка на имя не содержит пробелов или других символов, которые делают отправленное в Dynatrace в JSON отличным от имени, определённого в YAML.

### Другие типы конфигурации

Свойство `name` не используется для идентификации объектов Dynatrace.
Вместо этого используется координата конфигурации — комбинация проекта, типа и идентификатора конфигурации, или `originObjectId`, если он присутствует.

Свойство `name` всё ещё может использоваться и для некоторых типов автоматически извлекается при [скачивании](../reference/commands-saas.md#download "Как использовать CLI-приложение Monaco, включая аргументы и опции.").

### Поле `skip`

Поле `skip` позволяет пропустить развёртывание определённой конфигурации.
Если `skip` установлен в true, Dynatrace Monaco CLI не будет развёртывать конфигурацию.

Поле `skip` ведёт себя как [параметры](yaml-configuration-saas-type-fields.md#parameters "Список полей типов в YAML-файле конфигурации Monaco."), и вы можете определить его как значение или параметр окружения.
Обычно оно определяется непосредственно как сокращённое значение.

Наиболее полезно с переопределениями окружений, когда вы хотите развернуть конфигурацию в одном окружении, но исключить из другого.

### Поле `parameters`

Поле `parameters` используется для предоставления выбранных значений в шаблоне конфигурации.
Оно определяется как объект YAML с записью типа.
Этот тип далее определяет, как интерпретируется объект параметра.
Значение параметра вычисляется только в том случае, если на него ссылается конфигурация, которая будет развёрнута.

Доступны следующие типы параметров:

* value
* environment
* reference и partial reference
* compound
* list
* file

#### Параметр `value`

Параметр `value` — простейшая форма параметра.
Помимо свойства `type`, он также требует свойство value.
В качестве значения можно определить что угодно, даже вложенные карты.
Это значение затем доступно в файле шаблона.
Поскольку параметры `value` являются наиболее распространённым типом параметров, существует специальный сокращённый синтаксис для их определения. Вы можете указать значение, если ваш параметр не является массивом или картой.

Пример установки параметра `value`:

```
parameters:


threshold: 15


complexThreshold:


type: value


value:


amount: 15


unit: sec
```

В JSON-шаблоне этой конфигурации к параметру `threshold` можно обратиться через `{{ .threshold }}`.
Для доступа, например, к `amount` из `complexThreshold`, можно использовать `{{ .complexThreshold.amount }}`.

#### Параметр `environment`

Параметр типа `environment` позволяет ссылаться на переменную окружения.
Имя переменной окружения для ссылки определяется через свойство `name`.

Вы можете предоставить значение по умолчанию через свойство default, если переменная окружения отсутствует.

Параметр не может быть разрешён, если свойство `default` не установлено и переменная окружения отсутствует.
Развёртывание завершится с ошибкой, если свойство `default` не установлено и переменная окружения отсутствует.

Развёртывание завершится с ошибкой только в том случае, если параметр необходим для развёртывания.
Параметры, на которые не ссылается конфигурация для развёртывания, не вычисляются.

Следующий пример определяет параметры `owner` и `target`:

* Параметр `owner` вычисляет значение переменной окружения `OWNER`.
  Если переменная окружения не установлена, он принимает значение `"-"`.
* Параметр target вычисляет значение переменной окружения `TARGET`.
  Развёртывание завершится с ошибкой, если переменная не установлена на момент развёртывания.

  Пример установки параметров `owner` и `target`:

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

#### Параметр `reference`

Конфигурации Dynatrace часто ссылаются на другие конфигурации для поддержки более сложных сценариев использования.
Monaco предоставляет специальный параметр `reference` для поддержки таких ссылок на конфигурации.

Для использования типа параметра reference необходимо указать следующие обязательные поля:

* `project`: имя проекта конфигурации, на которую ссылается параметр.
* `configType`: тип конфигурации, на которую ссылается параметр.
  Для конфигураций типа `settings` значение `configType` должно соответствовать идентификатору схемы, например, `builtin:davis.anomaly-detectors`.
* `configId`: идентификатор конфигурации, на которую ссылается параметр.
* `property`: имя поля для определения значения параметра.
  Если свойство установлено в `id` или `name`, параметр разрешается в фактический идентификатор или имя соответствующего объекта Dynatrace.

  В следующем примере `id` объекта Site Reliability guardian используется в определении рабочего процесса. `guardianid` использует идентификатор объекта Dynatrace конфигурации guardian из проекта `other-project`.

  ```
  configs:


  - id: myservice-srg-validation-workflow


  config:


  name: CasC-sample myService Performance Quality Gate Validation


  parameters:


  event_filter_service:


  value: myService


  type: value


  event_filter_stage:


  value: prod


  type: value


  event_filter_gate:


  value: performance gate


  type: value


  guardianid:


  configId: myservice-guardian


  configType: app:dynatrace.site.reliability.guardian:guardians


  property: id


  type: reference


  project: other-project


  template: myservice-srg-validation-workflow.json


  skip: false


  type:


  automation:


  resource: workflow
  ```

Dynatrace Monaco CLI обеспечивает развёртывание конфигурации в правильном порядке, при этом зависимая конфигурация развёртывается первой.

Если вы настроите циклические зависимости, развёртывание завершится с ошибкой.

##### Сокращённый синтаксис

Параметры reference являются одним из наиболее распространённых типов параметров; существует специальный сокращённый синтаксис для их определения в виде массива:

* Синтаксис: `[ <project>, <configType>, <configId>, <property> ]`
* Пример: guardianId: `["other-project", "app:dynatrace.site.reliability.guardian:guardians", "myservice-guardian", "id"]`

Тип не нужен, так как он определяется автоматически на основе синтаксиса.

##### Частичная ссылка (partial reference)

Можно опустить некоторые поля `reference`.
В этом случае они заполняются тем же значением, что и у текущей конфигурации.
Это можно использовать для упрощения ссылок на конфигурации внутри одного проекта.

```
parameters:


mz_id:


type: reference


configType: management-zone


configId: main


property: id
```

Хотя можно опустить `configType` и даже `configId`, вы можете оставить пустым только верхний уровень и не можете оставлять пропуски.
Если `configType` опущен, то должен быть опущен и `project`.

Хотя можно опустить `configType` и даже `configId`, вы можете оставить пустым только верхний уровень и не можете оставлять пропуски.
Если `configType` опущен, необходимо также опустить `project`.

Ниже приведён полный пример использования сокращённых ссылок:

* infrastructure/management-zone/config.yaml

  ```
  configs:


  - id: main


  type:


  api: management-zone


  config:


  name: "Main zone"


  template: "zone.json"
  ```
* development/management-zone/config.yaml

  ```
  configs:


  - id: development


  type:


  api: management-zone


  config:


  name: "Development zone"


  template: "zone.json"
  ```
* ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Дашборды") **Дашборды** development/dashboard/config.yaml

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


  devZoneId: ["management-zone", "development", "id"] # подразумеваемый проект 'development'


  otherDashboard: ["a_dashboard", "id"] # подразумеваемый проект 'development' и тип 'dashboard'
  ```

#### Параметр `compound`

Параметр `compound` состоит из других параметров той же конфигурации.

Этот параметр требует несколько свойств:

* Строка `format`.
* Список `references` на все используемые параметры.

Строка `format` может быть любой строкой.
Для использования параметров в ней используйте синтаксис `{{ .parameter }}`, где указывается имя параметра составного параметра.

Пример использования параметра `compound`:

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

Этот пример даёт следующий результат: `Health: 40%`.

Хотя ссылочные параметры могут быть только из той же конфигурации, использование параметра reference позволяет создать составной параметр с другими конфигурациями.
Это также справедливо для переменных окружения.

Пример использования составного параметра:

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


configType: dashboarddocument


configId: my-dashboard


property: status
```

#### Параметр `list`

Параметр типа `list` позволяет определять списки [параметров value](yaml-configuration-saas-type-fields.md#value "Список полей типов в YAML-файле конфигурации Monaco.").
При использовании в шаблоне они записываются как JSON-список в квадратных скобках, разделённых запятыми.
Этот тип параметра обычно применяется, когда требуется простой список элементов, таких как адреса электронной почты или идентификаторы, которые могут быть заполнены любым параметром value.

Пример использования параметра `list`:

```
Configs:


- id: myservice-slo-availability


config:


name: CasC-sample myService availability


parameters:


service_id:


name: SERVICE_ID


type: environment


tags: #INPUT: Customize your SLO with tags


type: list


values: ["service:myService", "dt.owner:myTeam"]


template: myservice-slo-availability.json


skip: false


type: slo-v2
```

Пример использования параметра `list` и JSON-шаблона myservice-slo-availability.json:

```
{


"criteria": [


{


"target": 95,


"timeframeFrom": "now-7d",


"timeframeTo": "now"


}


],


"customSli": {


"filterSegments": [],


"indicator": "timeseries { total=sum(dt.service.request.count) ,failures=sum(dt.service.request.failure_count) }\n  , by: { dt.entity.service }\n  , filter: { in (dt.entity.service, { \"{{ .service_id }}\" }) }\n| fieldsAdd sli=(((total[]-failures[])/total[])*(100))\n| fieldsAdd entityName(dt.entity.service)\n| fieldsRemove total, failures"


},


"description": "Measures the proportion of successful service requests over time.",


"name": "{{ .name }}",


"tags": {{ .tags }}


}
```

Как показано в примере выше, вы можете определять значения `list` в YAML как построчно, так и в виде массива.

При использовании значения параметра `list` в JSON-шаблоне ссылайтесь на значение без дополнительных скобок.
`"emails": {{ .recipients }}`

#### Параметр `file`

Dynatrace Monaco CLI версии 2.14.0+

Параметр типа `file` позволяет загружать содержимое из файла на диске.

Пример использования параметра `file`:

```
parameters:


comment: "// hello special comment"


myWf:


type: file        # parameter type "file"


path: "myWf.js"   # relative path to the file


references:       # other parameters names referenced in the content of the file


- comment
```

В этом примере параметр `myWf` динамически разрешается для включения содержимого `myWf.js` относительно текущего расположения конфигурации.

Вы можете ссылаться на этот параметр в JSON-шаблоне следующим образом:

`{ "script" : {{ .myWf }} }`

Вы можете включать ссылки на другие параметры в содержимое указанного файла.
Каждый параметр ссылки должен быть определён как отдельный параметр и указан в разделе references типа параметра file.

В данном примере вы можете ссылаться на дополнительный параметр `comment` в содержимом, указанном параметром file, используя нотацию `{{ .comment }}`.

### `originObjectId`

При использовании Dynatrace Monaco CLI для [скачивания](../reference/commands-saas.md#download "Как использовать CLI-приложение Monaco, включая аргументы и опции.") существующих конфигураций из Dynatrace созданные YAML-файлы содержат `originObjectId` для некоторых типов конфигурации.

`originObjectId` содержит идентификатор скачанного объекта Dynatrace.
Используйте `originObjectId`, если вы планируете повторное развёртывание в то же окружение Dynatrace, чтобы обеспечить корректное обновление существующего объекта скачанной конфигурацией.

Например, его можно использовать для существующего объекта Settings 2.0, который вы дополняете данными для его корректной идентификации.

`originObjectId` является необязательным и устанавливается Monaco автоматически — от пользователя не требуется никаких действий или адаптаций.

### Переопределение конфигураций для каждого окружения или группы окружений

Существует множество случаев, когда конфигурация похожа, но не одинакова между окружениями.

Например:

* Оповещение отправляется в разные каналы Slack для промежуточного и производственного окружений.
* Конфигурацию сервиса следует пропустить, потому что он ещё не выпущен.

Для этого вы можете использовать поля `groupOverrides` и `environmentOverrides` для переопределения значений конфигурации на уровне окружения и группы окружений.

Оба определяются аналогично, различаясь только тем, применяются ли они к группе или к отдельному окружению.
Вы можете указать имя целевого окружения или группы окружений и любые свойства конфигурации для изменения.

В этом примере конфигурация получает специальные настройки для двух окружений, а skip гарантирует, что конфигурация не будет развёрнута в группу production-environments:

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

## Связанные темы

* YAML-файл конфигурации Monaco — список полей типов
