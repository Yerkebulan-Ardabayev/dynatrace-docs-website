---
title: Конфигурационный YAML-файл Monaco - список полей type
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/monaco/configuration/yaml-configuration-saas-type-fields
scraped: 2026-03-06T21:30:43.612602
---

# Конфигурационный YAML-файл Monaco - список полей type


* Latest Dynatrace
* Справочник
* 11 мин чтения
* Обновлено 15 янв. 2026

Поле [`type`](yaml-configuration-saas.md#type-field "Структура конфигурационного YAML-файла Monaco.") в YAML-файле `configs` определяет тип конфигурации Dynatrace.

Список полей `type`

* [`api`](#API-type-field)
* [`Settings`](#settings-type-field)
* [`Automation`](#automation-type-field)
* [`Bucket`](#bucket-type-field)
* [`Document`](#document-type-field)
* [`OpenPipeline`](#openpipeline-type-field)
* [`Segment`](#segment-type-field)
* [`SLO` (Service-level objective)](#slo-v2-type-field)
* [`Account configuration`](#accounts-type-field)

## Поле type api

Поле `type` со значением `api` может быть определено следующим образом.

```
configs:


id: [...]


type:


api: synthetic-monitor


config:


[...]
```

или

```
configs:


id: [...]


type: synthetic-monitor


config:


[...]
```

Дополнительную информацию см. в разделе [Поддерживаемые типы API](../monaco-api-support-and-access-handling.md#supported-api-types "Список поддержки API Monaco и обработки прав доступа.").

Некоторые конфигурации `api` `type` имеют связь типа "родитель-потомок" с другой конфигурацией.
Такая конфигурация требует поля scope, указывающего на родительскую конфигурацию.
Определите `scope` как `value`, `reference` или `environment`.

Поскольку такие конфигурации создаются в области видимости родительского API, ссылка на `id` родительской конфигурации является удобным способом настройки сущностей после их создания через CLI Monaco Dynatrace.

В приведённом ниже примере настраивается мобильное приложение и связанные ключевые действия пользователя, а `id` в `configs` ссылается на мобильное приложение.

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


config:


name: myKeyUserAction


template: kua.json


skip: false


type:


api:


name: key-user-actions-mobile


scope:


type: reference


configType: application-mobile


configId: mobile-application-id


property: id
```

## Поле type settings

[Settings API](../../../../dynatrace-api/environment-api/settings.md "Узнайте, что предлагает Settings API Dynatrace.") определяются через `schema`, `scope` и необязательный `schemaVersion`.

Поле `type` со значением `settings` может быть определено следующим образом.

```
configs:


id: [...]


type:


settings:


schema: builtin:davis.anomaly-detectors


schemaVersion: 1.0.2


scope: environment


config:


[...]
```

Вы можете определить параметр `scope` как `value`, `reference` или `environment`.
Установка scope в значение `environment` позволяет создать конфигурацию настроек для всего Environment Dynatrace.

Для сущности Dynatrace может быть создано множество `settings`, поэтому ссылка на `id` другого `configs` является удобным способом настройки сущностей после их создания через CLI Monaco Dynatrace.

В приведённом ниже примере настраивается веб-приложение, а затем для него создаются `settings`.
Scope `rum.web.enablement` в `settings` ссылается на веб-приложение `MyApp`.

```
configs:


- id: MyAppId


type:


api: application-web


config:


name: My Sample Web Application


template: application.json


skip: false


- id: MyApp_RUMSettingsId


type:


settings:


schema: builtin:rum.web.enablement


scope:


type: reference


configType: application-web


configId: MyAppId


property: id


config:


name: MyApp_RUMSettings


template: rum-settings.json


skip: false
```

Ещё один полезный параметр — `insertAfter`.
Этот параметр обеспечивает определённый порядок отдельных объектов Settings 2.0.

В приведённом ниже примере, если установлен `insertAfter`, Monaco Dynatrace гарантирует, что объект настроек будет развёрнут:

* Для CLI Monaco Dynatrace версии 2.14.0+ после указанного объекта с использованием параметра reference.

  ```
  - id: mySecondAppDetectionRuleId


  config:


  parameters:


  [...]


  template: wed-detect-rule.json


  skip: false


  type:


  settings:


  schema: builtin:rum.web.app-detection


  schemaVersion: 2.1.1


  scope: environment


  insertAfter:


  configId: myFirstAppDetectionRuleId  # Monaco config id


  property: id                         # must be "id"


  type: reference                      # must be "reference"
  ```
* Для CLI Monaco Dynatrace версии 2.21.0+ после указанной конфигурации через жёстко заданный ID с использованием параметра value

  ```
  type:


  settings:


  schema: builtin:rum.web.app-detection


  schemaVersion: 2.1.1


  scope: environment


  insertAfter:


  value: myFirstAppDetectionRuleId     # hardcoded config id


  type: value                          # must be "value"
  ```
* Для CLI Monaco Dynatrace версии 2.21.0+ в начало или конец списка с использованием значений front или back.

  ```
  type:


  settings:


  schema: builtin:rum.web.app-detection


  schemaVersion: 2.1.1


  scope: environment


  insertAfter: front       # "front" puts the config on top of the list, "back" puts it at the bottom
  ```

* Если несколько конфигураций или проектов Monaco определяют front или back, не гарантируется, какая конфигурация будет первой или последней.
* Поскольку Monaco Dynatrace разворачивает `configs` параллельно, рекомендуется добавлять параметр `insertAfter` ко всем `configs`, чтобы гарантировать размещение конфигурации в начале или конце списка.

Начиная с CLI Monaco Dynatrace версии 2.23.0+, определённые объекты Settings 2.0 позволяют задать более детальную область разрешений для указания доступа на чтение или запись к отдельным объектам настроек с использованием параметра `permissions`.

Параметр `permissions` поддерживает поле `allUsers`:

* `none`: только владелец (создатель) объекта настроек имеет полный доступ к нему, остальные пользователи не имеют доступа.
* `read`: владелец (создатель) имеет полный доступ к объекту настроек, остальные пользователи с разрешением `settings:objects:read` имеют доступ только на чтение.
* `write`: каждый пользователь с разрешениями `settings:objects:read` и `settings:objects:write` имеет полный доступ (чтение и запись) к объекту настроек.

Пример приведён ниже.

```
configs:


- id: security-jira-connection


config:


name: 'Security: Jira Connection'


template: jira-connection.json


skip: false


parameters:


[...]


type:


settings:


schema: app:dynatrace.jira:connection


scope: environment


permissions:


allUsers: read
```

## Поле type automation

Начиная с CLI Monaco Dynatrace версии 2.6.0+, поддерживается тип `automation`.
Конфигурации типа `automation` представляют ресурсы, связанные с [рабочими процессами (Workflows)](../../../../analyze-explore-automate/workflows.md "Автоматизируйте IT-процессы с помощью Dynatrace Workflows — реагируйте на события, планируйте задачи и подключайте сервисы.").

Поле `type` со значением `automation` может быть определено следующим образом.

```
type:


automation:


resource: workflow # or business-calendar, or scheduling-rule
```

Поле `resource` указывает желаемый ресурс автоматизации. Каждый ресурс требует отдельных разрешений OAuth.
Дополнительную информацию см. в разделе [Поддержка API Monaco и обработка прав доступа](../monaco-api-support-and-access-handling.md#supported-api-types "Список поддержки API Monaco и обработки прав доступа.").

Пример приведён ниже.

```
configs:


- id: myRemediationWorkflow


config:


name:


value: "High Prio Incident Remediation"


parameters:


[...]


template: remediationWorkflow.json


skip: false


type:


automation:


resource: workflow
```

API автоматизации поддерживает параметр запроса `adminAccess` для получения всех доступных ресурсов рабочих процессов на данном тенанте.
Если не используется, доступны только ресурсы рабочих процессов, привязанные к правам пользователя, создавшего OAuth-клиент.

Для использования этого параметра OAuth-клиенту необходимо иметь область видимости `automation:workflows:admin configured`.

Чтобы получить область видимости `automation:workflows:admin configured`

1. Создайте пользовательскую политику, предоставляющую разрешение `automation:workflows:admin`, используя следующее выражение политики `ALLOW automation:workflows:admin`.
2. Привяжите её к группе.
3. Назначьте пользователя в эту группу.

По умолчанию CLI Monaco Dynatrace использует этот флаг при обращении к API.
Если операция завершается с ошибкой, она повторяется без флага, но в этом случае вы можете получить доступ только к рабочим процессам, созданным вашим собственным пользователем.

## Поле type bucket

Начиная с CLI Monaco Dynatrace версии 2.9.0+, поддерживается тип `bucket`, который представляет конфигурации [управления хранением данных в Grail с пользовательскими бакетами Grail](../../../../platform/grail/organize-data.md#creating-new-buckets "Обзор модели данных Grail, состоящей из бакетов, таблиц и представлений.").

Поле `type` со значением `bucket` может быть определено следующим образом.

```
type: bucket
```

Дополнительные поля не требуются.

Помимо определения и создания нового бакета хранения, необходимо дополнительное правило бакета через [Settings API](../../../../dynatrace-api/environment-api/settings.md "Узнайте, что предлагает Settings API Dynatrace.") для указания того, какие данные в нём хранятся.

Пример приведён ниже.

```
configs:


# this is the new custom bucket


- id: my-bucket-id


config:


name: My awesome bucket


template: bucket.json


parameters:


retention_days: 372


type: bucket


# this is a new setting to define the rule what data shall be stored in the previously defined custom Grail bucket


- id: log-bucket-rule


type:


settings:


schema: builtin:logmonitoring.log-buckets-rules


scope: environment


config:


name: My custom rule


template: log-bucket-rule.json


parameters:


phrase: My phrase to look for


bucket:


type: reference


configType: bucket


configId: my-bucket-id


property: id
```

### Именование бакетов

Если в конфигурации бакета задан `originObjectId`, он используется как имя бакета.
В противном случае имя бакета автоматически генерируется из имени проекта и `id` в `config` по шаблону `project_configId`.
Это имя используется как в качестве имени бакета, так и в качестве его идентификатора.

По умолчанию имя бакета очищается для обеспечения совместимости с требованиями именования Dynatrace.

## Поле type document

Начиная с CLI Monaco Dynatrace версии 2.15.0+, поддерживается тип `document`, который представляет [API для дашбордов и ноутбуков](../../../../analyze-explore-automate/dashboards-and-notebooks/document-api.md "Управляйте документами Dynatrace (такими как дашборды и ноутбуки) через API.").

Начиная с CLI Monaco Dynatrace версии 2.18.0+, тип `document` также представляет `launchpad`.

Начиная с CLI Monaco Dynatrace версии 2.28.0+, тип `document` также поддерживает поле `id` для пользовательских идентификаторов.

Поле `type` со значением `document` может быть определено следующим образом.

```
type:


document:


kind: dashboard # other possible types: "notebook" or "launchpad"


private: true # optional field specifying the visibility of the document


id: custom-document-id # optional field specifying a user-defined document ID
```

Необязательное поле `private` указывает, является ли документ скрытым.
Если не указано иное, `document` по умолчанию является публичным, что означает, что его может видеть каждый, у кого есть соответствующие права доступа.

Необязательное поле `id` позволяет задать пользовательский идентификатор для документа.
Если это поле задано, в [файле удаления](../configuration.md#file-structure-for-direct-reference "Управление файлами конфигурации Dynatrace с помощью Monaco с набором проектов и манифестом развёртывания.") необходима прямая ссылка через `objectId`, если вы захотите удалить документ позже.

Если не указано, Monaco генерирует пользовательский идентификатор. В обоих случаях (пользовательский и сгенерированный Monaco) этот идентификатор используется для заполнения поля `id` при скачивании.

Monaco не скачивает [готовые документы](../../../../analyze-explore-automate/dashboards-and-notebooks/ready-made-documents.md "Используйте готовые документы прямо из коробки.").

В зависимости от учётных данных пользователя Monaco может не иметь возможности повторно развернуть все скачанные документы в определённых ситуациях.
Это происходит, когда документы общедоступны, но пользователь Monaco не обладает правами владельца. Другими словами, пользователь Monaco не является владельцем документа.
Дополнительную информацию о совместном использовании документов или смене владельца см. в разделах [Дашборды](../../../../analyze-explore-automate/dashboards-and-notebooks/dashboards-new.md "Создавайте интерактивные, настраиваемые представления для визуализации, анализа и обмена данными наблюдаемости в реальном времени."), [Ноутбуки](../../../../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Анализируйте, визуализируйте и делитесь выводами из данных наблюдаемости — всё в одном совместном настраиваемом рабочем пространстве.") или [Лаунчпады](../../../../discover-dynatrace/get-started/dynatrace-ui/launchpads.md "Создавайте и управляйте пользовательскими стартовыми страницами с помощью лаунчпадов.").

Дополнительную информацию см. в [репозитории примеров конфигурации как кода](https://github.com/Dynatrace/dynatrace-configuration-as-code-samples)

## Поле type openpipeline

Устарело

Начиная с CLI Monaco Dynatrace версии 2.15.0+, поддерживается тип `openpipeline`.
Конфигурация `openpipeline` управляет приёмом и обработкой данных из различных источников.

Поле `type` со значением `openpipeline` может быть определено следующим образом.

```
type:


openpipeline:


kind: bizevents # id of openpipeline configuration (for example, "bizevents", "events", "logs", "spans", or "metrics")
```

Развёртывание конфигурации `openpipeline` перезаписывает существующую конфигурацию того же типа, что приводит к потере всех ручных изменений, сделанных в веб-интерфейсе, или других конфигураций, управляемых Monaco или Terraform.
Для предотвращения потери данных убедитесь, что все конфигурации определены в единой конфигурации Monaco или Terraform.

Этот ресурс устарел и перемещён в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings**. Дополнительную информацию см. в разделе [OpenPipeline API](../../../../platform/openpipeline/reference/openpipeline-api.md "Настройте возможности OpenPipeline по приёму, маршрутизации и обработке источников данных через API.").

Поле `kind` указывает `id` предварительно существующей конфигурации `openpipeline`.
Monaco может получать и обновлять конфигурации, но не может создавать или удалять новые.

## Поле type segment

Начиная с CLI Monaco Dynatrace версии 2.19.0+, поддерживается тип `segment`.
[Сегменты](../../../../manage/segments.md "Используйте сегменты для логического структурирования и удобной фильтрации данных наблюдаемости в приложениях.") используются для структурирования и фильтрации данных для создания адаптированных представлений в Dynatrace.

Поле `type` со значением `segment` может быть определено следующим образом.

```
type: segment
```

Дополнительные поля не требуются, но сегмент может быть использован как ссылка в других конфигурациях для соответствующей фильтрации визуализируемых данных.

Пример приведён ниже.

```
configs:


- id: segment                # configures the desired segment


type: segment


config:


template: segment.json


- id: dashboard              # creates a dashboard that references a segment


type:


document:


kind: dashboard


private: true


config:


name: Log Dashboard with Dynatrace Segment


parameters:


segment_id:            # references the previously created segment within a dashboard


configId: segment


configType: segment


property: id


type: reference


template: dashboard.json
```

## Поле type `slo-v2` (Service-level objective)

Начиная с CLI Monaco Dynatrace версии 2.22.0+, поддерживается тип `slo-v2`.

[Настройка и мониторинг целей уровня обслуживания с помощью Dynatrace](../../../service-level-objectives-classic/configure-and-monitor-slo.md "Создание, настройка и мониторинг целей уровня обслуживания с помощью Dynatrace."), основанных на Grail и использующих DQL, управляются через `type` `slo-v2`.

Тип конфигурации `slo-v2` отличается от существующего типа `slo` и представляет SLO, использующие Grail, как описано в обзоре [Настройка и мониторинг целей уровня обслуживания с помощью Dynatrace](../../../service-level-objectives-classic/configure-and-monitor-slo.md "Создание, настройка и мониторинг целей уровня обслуживания с помощью Dynatrace.").
Эти два типа конфигурации несовместимы, и развёртывание конфигурации `slo` как `slo-v2` или наоборот приведёт к отклонению запроса API.

Поле `type` со значением `slo-v2` может быть определено следующим образом.

```
type: slo-v2
```

Этот тип не требует дополнительных полей.

Пример приведён ниже.

```
configs:


- id: custom-sli          # An SLO based using a custom DQL query as SLI


type: slo-v2


config:


name: custom-sli


template: custom-sli.json


- id: sli-reference       # another SLO using an out-of-the-box template (aka reference)


type: slo-v2


config:


name: sli-reference


template: sli-reference.json
```

## Учётные записи (accounts)

Для определения `accounts`, для которых Monaco настраивает ресурсы управления учётными записями, необходимо создать раздел accounts в файле конфигурации.

Следующий пример определяет единственный объект `accounts`, содержащий информацию об учётной записи.
Свойство `name` указывает имя учётной записи my-account, на которое можно ссылаться с помощью флага `--account` команды CLI Monaco.

```
accounts:


- name: my-account


accountUUID: 12345678-1234-5678-1234-123456789012


oAuth:


clientId:


name: OAUTH_CLIENT_ID


clientSecret:


name: OAUTH_CLIENT_SECRET
```

### Ресурсы учётных записей

С помощью Monaco вы можете определить `users`, `service users`, `groups` и `policies` как отдельные типы.

В отличие от обычных конфигураций уровня окружения, файлы шаблонов JSON не требуются.
Monaco создаёт необходимые данные API непосредственно из вашей YAML-конфигурации.

Конфигурация на уровне учётной записи обычно отличается от конфигурации на уровне окружения.
Она изменяется реже; существующие команды, такие как `monaco deploy`, игнорируют любую конфигурацию учётных записей, которая может быть определена в файле манифеста.

Вместо этого необходимо использовать специальную команду `monaco account deploy`.

Пример показывает, как Monaco представляет ресурсы управления учётными записями локально, с примерами определения пользователей, сервисных пользователей, групп и политик.

```
users: # users define one or more users bound to different groups


- email: monaco@dynatrace.com


groups:


- Log viewer # default group


- type: reference


id: my-group


# id: specifies a custom group. The ID must match a group defined in groups. Custom groups need to be referenced (vs. default groups)


serviceUsers:     # supported with Monaco CLI v2.23.0+


- name: Monaco service user # name: must be unique. Otherwise, an originObjectId is needed


description: Description of service user


originObjectId: 3037325d-6475-4adf-a14d-93d1c862f9e9 # (optional) only needed if the user's name is not unique


groups:


- Log viewer # default group


- type: reference # custom group my-group needs to be referenced


id: my-group


groups:


- name: My Group


id: my-group


description: This is my group


account: # specifies permissions and policies to which the group is bound on the account level.


permissions:


- account-viewer


policies:


- policy: Environment role - Access environment


environments: # specify the permissions and policies to which the group is bound on the environment/tenant level.


- environment: abc12345


permissions:


- tenant-viewer


policies:


- policy: Environment role - Replay session data without masking


- type: reference


id: my-policy


managementZones: # classic Dynatrace only


- environment: abc12345


managementZone: Management Zone 2000


permissions:


- tenant-viewer


policies: # defines one or more policies for the selected group


- name: My Policy


id: my-policy


level:


type: account


description: abcde


policy: |- # contains any policy rules of this particular policy.


ALLOW automation:workflows:read;
```

Хотя в этом примере пользователи, сервисные пользователи, политики и группы определены в одном файле, вы можете определять их в отдельных файлах и структурировать проекты и файлы ресурсов учётных записей по мере необходимости.

## Связанные темы

* [Структура конфигурационного YAML-файла Monaco](yaml-configuration-saas.md "Структура конфигурационного YAML-файла Monaco.")
