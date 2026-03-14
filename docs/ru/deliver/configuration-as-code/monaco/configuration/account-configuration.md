---
title: Конфигурация аккаунтов для управления аккаунтами Monaco
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/monaco/configuration/account-configuration
scraped: 2026-03-02T21:30:29.843938
---

# Конфигурация аккаунтов для управления аккаунтами Monaco


* Последняя Dynatrace
* Практическое руководство
* 4 мин. чтения
* Обновлено 15 января 2026 г.

Для определения аккаунтов, для которых Monaco будет настраивать ресурсы управления аккаунтами, необходимо создать раздел `accounts` в [файле манифеста](../configuration.md#manifest "Управление конфигурационными файлами Dynatrace с помощью Monaco через набор проектов и манифест развёртывания.").

В следующем примере мы определяем один объект аккаунта, содержащий информацию, связанную с аккаунтом. Свойство **name** задаёт имя аккаунта (в данном примере `my-account`), на которое можно ссылаться с помощью флага `--account` команд CLI Monaco.

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

Управление аккаунтами требует учётных данных OAuth.
Платформенные токены и API-токены не поддерживаются.
OAuth-клиент должен иметь соответствующие области, настроенные для ресурсов аккаунта, которыми вы хотите управлять.
Убедитесь, что ваши учётные данные OAuth включают необходимые разрешения для пользователей, групп, политик, границ или сервисных пользователей перед развёртыванием конфигураций.

Помимо раздела `accounts`, файл `manifest.yaml`, определённый для ресурсов аккаунта, аналогичен файлу для конфигураций среды, требуя [`projects`](../configuration.md#project-definitions "Управление конфигурационными файлами Dynatrace с помощью Monaco через набор проектов и манифест развёртывания.") конфигурационных файлов ресурсов аккаунта.

## Ресурсы аккаунта

С помощью Monaco вы можете определять [пользователей](../../../../manage/identity-access-management/user-and-group-management/access-user-management.md "Управление пользователями"), [сервисных пользователей](../../../../manage/identity-access-management/user-and-group-management/access-service-users.md "Сервисные пользователи"), [группы](../../../../manage/identity-access-management/user-and-group-management/access-group-management.md "Управление группами Dynatrace и их разрешениями."), [политики](../../../../manage/identity-access-management/permission-management/manage-user-permissions-policies.md "Работа с политиками") и [границы](../../../../manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-boundaries.md "Ограничение политик безопасности с помощью границ политик для предоставления адаптированного доступа пользователям.") как выделенные типы в YAML-файлах конфигурации.

В отличие от обычных конфигураций уровня среды, файлы JSON-шаблонов не нужны. Monaco создаёт необходимые данные API непосредственно из вашей YAML-конфигурации.

### Пример представления ресурсов управления аккаунтами

Этот пример показывает, как Monaco представляет ресурсы управления аккаунтами локально, с примерами определения пользователей, сервисных пользователей, групп, политик и границ.

Следующие разделы подробно описывают каждую конфигурацию.

```
users:


- email: monaco@dynatrace.com


groups:


- Log viewer


- type: reference


id: my-group


serviceUsers:


- name: Monaco service user


description: Description of service user


groups:


- Log viewer


- type: reference


id: my-group


groups:


- name: My Group


id: my-group


description: This is my group


account:


permissions:


- account-viewer


policies:


- policy: Environment role - Access environment


environments:


- environment: abc12345


permissions:


- tenant-viewer


policies:


- policy: Environment role - Replay session data without masking


- policy:


type: reference


id: my-policy


boundaries:


- type: reference


id: workflow-simple-boundary


- MyExistingBoundary # Если вы хотите ссылаться по имени напрямую


managementZones:


- environment: abc12345


managementZone: Management Zone 2000


permissions:


- tenant-viewer


policies:


- name: My Policy


id: my-policy


level:


type: account


description: My policy description.


policy: |-


ALLOW automation:workflows:read;


boundaries:


- id: workflow-simple-boundary


name: Workflow Simple boundary


query: automation:workflow-type = "SIMPLE";
```

Хотя этот пример показывает пользователей, сервисных пользователей, группы, политики и границы, определённые в одном файле, вы можете определять их в отдельных файлах и структурировать проекты и файлы ресурсов аккаунта по необходимости.

### Пользователи

```
users:


- email: my-user@example.com


groups:


- Log viewer


- type: reference


id: my-group
```

В этом примере мы определяем следующие объекты.

* **users** определяет одного или нескольких пользователей, привязанных к различным группам.

  + **email** — адрес электронной почты
  + **groups** указывает группы, к которым принадлежит пользователь. В примере пользователь принадлежит к группе по умолчанию `Log viewer`.

    - **type**
    - **id** указывает пользовательскую группу, например `my-group`. Этот **id** должен совпадать с группой, определённой в поле **groups**.

### Сервисные пользователи

Dynatrace Monaco CLI версии 2.23.0+

```
serviceUsers:


- name: Monaco service user


description: Description of the service user.


originObjectId: 123e4567-e89b-12d3-a456-426614174000


groups:


- Log viewer


- type: reference


id: my-group
```

В этом примере мы определяем следующие объекты.

* **serviceUsers** определяет одного или нескольких сервисных пользователей, привязанных к различным группам.

  + **name** — имя сервисного пользователя. Если не уникально в рамках аккаунта, необходимо указать **originObjectId**.
  + **description** — необязательное описание сервисного пользователя.
  + **originObjectId** — необязательный Dynatrace ID существующего сервисного пользователя для обновления, используется для различения сервисных пользователей, если несколько имеют одинаковое имя.
  + **groups** указывает группы, к которым принадлежит сервисный пользователь. В примере сервисный пользователь принадлежит к группе по умолчанию `Log viewer` и к `my-group`, определённой в поле **groups**. Поскольку последняя является ссылкой, **type** должен быть установлен как `reference`, а **id** должен совпадать с группой, определённой в поле **groups**.

### Группы

```
groups:


- name: My Group


id: my-group


description: This is my group


account:


permissions:


- account-viewer


policies:


- policy: Environment role - Access environment


environments:


- environment: abc12345


permissions:


- tenant-viewer


policies:


- policy: Environment role - Replay session data without masking


- policy:


type: reference


id: my-policy


boundaries:


- type: reference


id: my-boundary


- MyExistingBoundary # Если вы хотите ссылаться по имени напрямую


managementZones:


- environment: abc12345


managementZone: Management Zone 2000


permissions:


- tenant-viewer
```

В этом примере мы определяем следующие объекты.

* **groups** определяет одну или несколько групп, привязанных к различным политикам или разрешениям.

  + **name**: имя группы.
  + **id**: внутренний уникальный идентификатор Monaco для группы, на который могут ссылаться пользователи и сервисные пользователи.
  + **description**: описание группы.
  + **account** указывает разрешения и политики, к которым группа привязана на уровне аккаунта.
  + **environments** указывает разрешения и политики, к которым группа привязана на уровне среды.

    - **name**: ID среды.
    - **permissions**: список разрешений, назначенных группе для этой среды.
    - **policies**
    - **policy** может ссылаться по имени, если доступна политика по умолчанию.

      * **type** должен быть установлен как `reference` при ссылке на пользовательскую политику.
      * **id** ссылается на пользовательскую политику. **id** должен совпадать с политикой, определённой в **policies**.
    - **boundaries** могут ссылаться по имени, если они доступны.

      * **id** ссылается на пользовательскую границу. **id** должен совпадать с границей, определённой в **boundaries**.
      * **type** должен быть установлен как `reference` при ссылке на пользовательскую границу.
  + **managementZones**: указывает разрешения, назначенные группе на уровне зоны управления.

    - **environment**: ID среды.
    - **managementZone**: имя зоны управления среды, например `Management Zone 2000`.
    - **permissions**: список разрешений, назначенных группе для данной зоны управления.

### Политики

```
policies:


- name: My policy


id: my-policy


level:


type: account


description: My policy is defined for the account.


policy: |-


ALLOW automation:workflows:read;


- name: My other policy.


id: my-other-policy


level:


type: environment


environment: abc12345


description: My policy is defined for a specific environment.


policy: |-


ALLOW automation:workflows:read;
```

В этом примере мы определяем следующие объекты.

* **policies** определяет одну или несколько политик.

  + **name**: имя политики.
  + **id**: внутренний уникальный идентификатор Monaco для политики, на который могут ссылаться группы.
  + **level**: указывает уровень политики.

    - **type**: может быть `account` или `environment`.
    - **environment**: если тип `environment`, укажите ID среды, к которой применяется эта политика.
  + **description**: описание политики.
  + **policy** содержит правила данной политики.

### Границы

```
boundaries:


- id: workflow-simple-boundary


name: Workflow Simple boundary


query: automation:workflow-type = "SIMPLE";
```

В этом примере мы определяем следующие объекты.

* **boundaries** определяет одну или несколько границ.

  + **id**
  + **name**
  + **query** содержит одно или несколько выражений политики, разделённых `;`.

## Команды

Поскольку конфигурация на уровне аккаунта обычно отличается от конфигурации на уровне среды и изменяется реже, существующие команды, такие как `monaco deploy`, игнорируют любую конфигурацию аккаунта, которая может быть определена в файле манифеста.

Для ресурсов аккаунта существуют специальные команды: [Account](../reference/commands-saas.md#account "Как использовать приложение CLI Monaco, включая аргументы и параметры.").