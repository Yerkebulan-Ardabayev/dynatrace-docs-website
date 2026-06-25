---
title: Назначение команд владельцев отслеживаемым сущностям
source: https://docs.dynatrace.com/managed/deliver/ownership/assign-ownership
scraped: 2026-05-12T11:12:49.061767
---

# Assign ownership teams to monitored entities

# Assign ownership teams to monitored entities

* How-to guide
* 9-min read
* Updated on Sep 16, 2025

Вы можете назначать [команды-владельцы](/managed/deliver/ownership/ownership-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership.") **любой отслеживаемой сущности** в Dynatrace, используя основной идентификатор команды или дополнительные идентификаторы (определяемые при [создании команды](/managed/deliver/ownership/ownership-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership.")). Это позволяет мгновенно находить ответственную команду и связываться с ней при возникновении проблем с сущностью, например если сущность затронута уязвимостью.

Владение можно применять несколькими способами: через метки и аннотации Kubernetes, метаданные хоста, переменные окружения и теги (в том числе через [Custom tags API](/managed/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.") Dynatrace).

## Поддерживаемые методы назначения владения

Поддерживаются следующие методы применения владения и типы сущностей.

* **Метаданные развёртывания или конфигурации** Рекомендуется

  | Метод | Типы сущностей |
  | --- | --- |
  | Метки и аннотации Kubernetes | Все объекты Kubernetes |
  | Метаданные хоста через `oneagentctl` или `hostcustomproperties.conf` | Хосты |
  | Переменные окружения | Процессы |
* **Теги** (ручные, автоматические и через API) — все отслеживаемые сущности

Настоятельно рекомендуется использовать предпочтительный метод применения владения в зависимости от типа сущности, как описано в разделах ниже.

* [Метки и аннотации Kubernetes для объектов Kubernetes](#kubernetes)
* [Метаданные для хостов](#host-metadata)
* [Переменные окружения для процессов](#process-env-variables)
* [Теги (ручные, автоматические и через API) для всех прочих сущностей](#tags)

Наши рекомендации основаны на наиболее эффективных методах обеспечения достаточного охвата сущностей владением. Подробнее см. в разделе [Рекомендации по владению сущностями](/managed/deliver/ownership/best-practices "Tips and best practices to ensure that entities have adequate ownership coverage").

## Формат применения информации о владении

Независимо от используемого метода информация о владении применяется к сущностям в виде **пар ключ-значение**. Ключи по умолчанию `owner` и `dt.owner` доступны в каждом окружении мониторинга — см. **Settings** > **Ownership** > **Configuration**. Однако вы можете изменить или удалить ключи по умолчанию и [определить собственные](#custom-keys).

Значение всегда является уникальным идентификатором команды, указанным при её создании. Также можно использовать дополнительные идентификаторы. (Подробнее об определении этих значений см. в разделе [Создание и управление командами для владения сущностями](/managed/deliver/ownership/ownership-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership.").)

Сущность может иметь более одной команды-владельца. Для этого применяется несколько пар ключ-значение, как показано в следующих разделах.

### Пользовательские ключи для информации о владении

Вы можете определить не более пяти ключей для применения информации о владении.

1. Перейдите в **Settings** > **Ownership** > **Configure**.
2. Выберите **Add key**.
3. Введите ключ (по умолчанию **Enabled**).
4. **Save changes**.

![Custom keys for ownership](https://dt-cdn.net/images/ownership-custom-keys-1482-1a7f6383f7.png)

Пользовательские ключи для владения

При **отключении или удалении ключа** сущности, назначенные командам через такие ключи, больше не будут отображать или хранить метаданные владения. Однако такие ключи будут отображаться как обычные теги, применённые к сущностям.

### Дополнительные требования к ключам владения

* Можно определить не более пяти и не менее одного ключа.
* Любой из определённых ключей можно использовать как префикс в парах ключ-значение. Например, для ключей `owner` и `dt.owner` можно использовать `owner-1` и `dt.owner-test`.

## Метки и аннотации Kubernetes

Вы можете указывать владение командой для различных объектов Kubernetes: Deployment, Pod, Service или пространство имён. Чтобы обеспечить достаточное покрытие владением для объектов Kubernetes — что особенно важно для короткоживущих сущностей, таких как Pod — предоставляйте информацию о владении в виде меток или аннотаций Kubernetes с [парами ключ-значение](#format) в файле спецификации развёртывания, например `deployment.yaml`.

Рекомендуется определять владение для Deployment и всех других объектов, для которых требуется покрытие владением. См. также [Рекомендации по владению сущностями](/managed/deliver/ownership/best-practices "Tips and best practices to ensure that entities have adequate ownership coverage").

* Указание идентификатора команды в качестве метки или аннотации для Deployment, CronJob, Job, DaemonSet или StatefulSet предоставляет информацию о владении командой для соответствующих сущностей `CLOUD_APPLICATION`. Обратите внимание, что это владение не распространяется на `CLOUD_APPLICATION_INSTANCE`.

  В этом примере двойное владение задаётся через две метки для Deployment. Каждая метка имеет уникальный ключ. **Уникальность ключей — обязательное требование в метках и аннотациях Kubernetes**.

  ```
  apiVersion: apps/v1



  kind: Deployment



  metadata:



  name: demo



  labels:



  dt.owner-1: my-team-1 # Dual team ownership defined for the Deployment



  dt.owner-2: my-team-2



  spec:
  ```

  Пример ниже показывает аннотацию для владения на уровне Deployment.

  ```
  apiVersion: apps/v1



  kind: Deployment



  metadata:



  name: demo



  annotations:



  dt.owner: my-team # Ownership defined for the Deployment
  ```
* Задавайте метки для Pod, чтобы указать владение для соответствующей сущности `CLOUD_APPLICATION_INSTANCE`. Указывайте владение для каждого Pod.

  ```
  apiVersion: apps/v1



  kind: Deployment



  metadata:



  name: demo



  spec:



  replicas: 3



  selector:



  matchLabels:



  app: demo



  template:



  metadata:



  labels:



  app: demo



  dt.owner: my-team # Ownership defined for the Pod



  spec:
  ```

  Пример ниже показывает манифест Pod с аннотацией `dt.owner: myTeam`.

  ```
  apiVersion: v1



  kind: Pod



  metadata:



  name: annotations-demo



  annotations:



  imageregistry: "https://hub.docker.com/"



  dt.owner: my-team



  spec:



  containers:



  - name: nginx



  image: nginx:1.14.2



  ports:



  - containerPort: 80
  ```
* Для **процесса** укажите владение через пары ключ-значение с помощью переменной окружения `DT_CUSTOM_PROP`, определённой для контейнера.

  В переменных окружения можно указывать несколько значений для одного ключа. В этом примере двойное владение определяется с использованием ключа `owner`.

  ```
  apiVersion: apps/v1



  kind: Deployment



  metadata:



  name: demo



  spec:



  replicas: 3



  selector:



  matchLabels:



  app: demo



  template:



  spec:



  containers:



  - name: demo



  image: demo:1.0.0



  env:



  - name: DT_CUSTOM_PROP ## Environment variable



  value: "owner=team-automation owner=team-dev" # Dual ownership for the process; team IDs are team-automation and team-dev.
  ```
* Метки Kubernetes для Service

  ```
  apiVersion: v1



  kind: Service



  metadata:



  name: my-service



  labels:



  dt.owner: team-a # Ownership defined for the Service



  spec:



  selector:



  app.kubernetes.io/name: MyApp



  ports:



  - protocol: TCP



  port: 80



  targetPort: 9376
  ```
* Метки Kubernetes для пространства имён

  ```
  apiVersion: v1



  kind: Namespace



  metadata:



  name: my-namespace



  labels:



  dt.owner: team-a # Ownership defined for the namespace
  ```

## Метаданные хоста

Для хостов в качестве основного метода применения владения рекомендуется использовать [метаданные хоста](/managed/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts#host-metadata "Learn how to tag and set additional properties for a monitored host.").

Подробнее см. в разделах [определение тегов и метаданных для хостов](/managed/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts "Learn how to tag and set additional properties for a monitored host.") и [интерфейс командной строки `oneagentctl` OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

Владение хостами также можно применять с помощью [тегов](#tags).

### Через `oneagentctl`

OneAgent версии 1.189+ Для хостов с OneAgent версии 1.189+ используйте интерфейс командной строки `oneagentctl` после установки для задания свойства метаданных отдельного хоста. Запускайте `oneagentctl` с правами администратора или root из следующих расположений по умолчанию.

* Windows: `%PROGRAMFILES%\dynatrace\oneagent\agent\tools`
* Все Unix-подобные системы: `/opt/dynatrace/oneagent/agent/tools`

Этот пример для Unix-подобных систем использует `--set-host-property` для задания владения через [пару ключ-значение](#format) `owner-1=team-automation`, где `team-automation` — это [основной идентификатор команды или дополнительный идентификатор](/managed/deliver/ownership/ownership-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership.").

```
./oneagentctl --set-host-property owner-1=team-automation
```

### Через `hostcustomproperties.conf`

OneAgent версии 1.187 и ранее Для хостов с OneAgent 1.187 и ранее создайте или отредактируйте файл конфигурации OneAgent `hostcustomproperties.conf` в следующих расположениях.

* Windows: `%PROGRAMDATA%\dynatrace\oneagent\agent\config`
* Все Unix-подобные системы: `/var/lib/dynatrace/oneagent/agent/config`

Этот пример для Unix-подобных систем задаёт владение хостом через [пару ключ-значение](#format) `dt.owner-1=team-automation`, где `team-automation` — это [основной идентификатор команды или дополнительный идентификатор](/managed/deliver/ownership/ownership-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership.").

```
cat hostcustomproperties.conf dt.owner-1=team-automation
```

## Переменные окружения процессов

Для процессов рекомендуется указывать владение в парах ключ-значение через переменную окружения `DT_CUSTOM_PROP`.

**Не рекомендуется** использовать теги для применения владения к процессам или группам процессов.

Подробнее см. в разделе [определение метаданных группы процессов](/managed/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata "Configure your own process-related metadata based on the unique needs of your organization or environment."), например, о настройке переменной окружения `DT_CUSTOM_PROP` для [IIS](/managed/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata#iis "Configure your own process-related metadata based on the unique needs of your organization or environment.") и [Windows](/managed/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata#windows "Configure your own process-related metadata based on the unique needs of your organization or environment.").

```
export DT_CUSTOM_PROP dt.owner=DemoTeam
```

Все существующие варианты ключ-значение или инструкции по созданию собственных см. в разделе [Формат применения информации о владении](#format).

## Теги

**Используйте теги для применения владения только к сущностям, не охватываемым методами, описанными выше**. Как правило, это такие сущности, как клиентские приложения, которые стабильны и немногочисленны.

### Методы тегирования

Для применения владения в [парах ключ-значение](#format) к любой отслеживаемой сущности можно использовать теги — подробнее о [тегировании](/managed/manage/tags-and-metadata "Use tags and metadata to organize data in your Dynatrace environment.").

![Ownership via a manual tag](https://dt-cdn.net/images/ownership-manual-tag-1004-f7c90a9b42.png)

Владение через ручной тег

* [Ручные теги](/managed/manage/tags-and-metadata/setup/how-to-define-tags#manual "Find out how to define and apply tags manually and automatically.") с использованием определённых ключей или префиксов ключей (например, `owner` и `dt.owner`) легко применять через веб-интерфейс.
* Также можно настроить [правила автоматического тегирования](/managed/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Find out how to define and apply tags manually and automatically.") через веб-интерфейс.
* Для применения владения к сущностям рекомендуется использовать [Custom tags API](/managed/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.") вместо правил автоматического тегирования. Custom tags API позволяет удобно применять теги к большой группе сущностей одним вызовом API, выполняемым немедленно.

Обратите внимание, что ручные теги можно удалять вручную. Автоматически применённые теги нельзя вручную удалить с отдельных сервисов, групп процессов, экземпляров групп процессов, приложений или хостов.

Подробнее о преимуществах и ограничениях тегирования при назначении владельцев сущностям см. в разделе [Рекомендации по владению сущностями](/managed/deliver/ownership/best-practices "Tips and best practices to ensure that entities have adequate ownership coverage"). См. также [Рекомендации по масштабированию тегирования и правил зон управления](/managed/manage/tags-and-metadata/basic-concepts/best-practice-tagging-at-scale "Optimize auto-tagging and management-zone rules to speed up the automatic assignment process.").

### Разрешения

Для добавления, изменения или удаления владения через Custom tags API необходимы **все** следующие разрешения.

* Разрешение токена `entities.write` [token permission](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.")
* Разрешение токена `settings.read` или [политика IAM](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies") `ALLOW settings:objects:read WHERE settings:schemaId = "builtin:ownership.teams";`

Для добавления, изменения или удаления тегов через веб-интерфейс требуется разрешение **Manage monitoring settings** [permission](/managed/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions") на уровне окружения или зоны управления.

## Просмотр информации о владении в веб-интерфейсе

Информация о владении доступна только на [унифицированных страницах анализа](/managed/ingest-from/extend-dynatrace/extend-ui/unified-analysis "Extend the Dynatrace web UI using entity-tailored unified analysis pages.").

Для хостов и всех сущностей Kubernetes выберите **Owners** на странице сведений о сущности для просмотра информации о владении.

Этот пример показывает Kubernetes workload, соответствующий сущности `CLOUD_APPLICATION`. Разверните имя команды для просмотра её деталей. Нажмите ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") в карточке **Ownership** для [редактирования сведений о команде](/managed/deliver/ownership/ownership-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership.") в **Settings**.

![Owner of a Kubernetes workload](https://dt-cdn.net/images/ownership-k8s-workload-2213-2217e57297.png)

Владелец Kubernetes workload

Этот пример показывает информацию о владении для Kubernetes Pod.

![Owner of a Kubernetes Pod](https://dt-cdn.net/images/ownership-k8s-pod-2214-e55133496a.png)

Владелец Kubernetes Pod

На странице **Hosts** можно искать хосты с владением — фильтруйте по **Tags** с определёнными вами префиксами ключей, например `owner` и `dt-owner`. Обратите внимание, что [пары ключ-значение владения](#format) должны быть применены хотя бы к одному хосту, чтобы ключ стал доступен в фильтре **Tags**. Этот метод поиска по владению доступен на всех страницах групп сущностей, которые можно фильтровать по тегам.

![Filter by ownership tags on entity group pages](https://dt-cdn.net/images/ownership-hosts-page-2190-8b47f48119.png)

Фильтрация по тегам владения на страницах групп сущностей

На примере страницы сведений о хосте ниже у хоста три команды-владельца. Один из владельцев помечен **Unknown team identifier**. Это означает, что хотя идентификатор команды был применён к хосту (например, через [oneagentctl](#oneagentctl) или [ручной тег](#tags)) в паре ключ-значение, команда не существует. **Invalid team identifier** означает, что идентификатор команды или дополнительный ID был применён к хосту в неверном [формате](#format).

Выберите **Properties and tags** для просмотра всех тегов, применённых к хосту.

![Owners of a host](https://dt-cdn.net/images/ownership-host-2199-95873a776f.png)

Владельцы хоста

Нажмите ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") рядом с неизвестной командой, затем выберите **Add team**, чтобы определить информацию о команде в **Settings**. Сущность будет автоматически обновлена с определением команды.

![Unknown team](https://dt-cdn.net/images/ownership-unknown-team-909-590ed7fbc0.png)

Неизвестная команда

## Связанные темы

* [Настройка Dynatrace на Kubernetes](/managed/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")
* [Определение тегов и метаданных для хостов](/managed/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts "Learn how to tag and set additional properties for a monitored host.")
* [Определение собственных метаданных группы процессов](/managed/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata "Configure your own process-related metadata based on the unique needs of your organization or environment.")
* [Теги и метаданные](/managed/manage/tags-and-metadata "Use tags and metadata to organize data in your Dynatrace environment.")
* [Custom tags API](/managed/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.")
* [Рекомендации по масштабированию тегирования и правил зон управления](/managed/manage/tags-and-metadata/basic-concepts/best-practice-tagging-at-scale "Optimize auto-tagging and management-zone rules to speed up the automatic assignment process.")
* [Метки Kubernetes](https://dt-url.net/g442yn5 "Official Kubernetes documentation on labels")
* [Аннотации Kubernetes](https://dt-url.net/bz62yto "Official Kubernetes documentation on annotations")
* [Унифицированные страницы анализа](/managed/ingest-from/extend-dynatrace/extend-ui/unified-analysis "Extend the Dynatrace web UI using entity-tailored unified analysis pages.")