---
title: Рекомендации по владению сущностями
source: https://docs.dynatrace.com/managed/deliver/ownership/best-practices
scraped: 2026-05-12T11:12:46.095289
---

# Best practices for entity ownership

# Best practices for entity ownership

* 5-min read
* Updated on Apr 25, 2023

Эти рекомендации и советы по владению разработаны для того, чтобы помочь вам:

* Обеспечить охват владением для короткоживущих сущностей, таких как экземпляры групп процессов и Kubernetes Pod.
* Минимизировать время выполнения тегирования.
* Эффективно масштабировать назначение владения в больших, сложных окружениях.
* Обеспечить покрытие владением для сущностей путём назначения команд в момент развёртывания.
* Поддерживать достаточную информацию о командах для маршрутизации и отображения.

## Назначение владения

Рекомендуется **назначать владельцев для критических сущностей**. Это сущности, которые часто испытывают сбои или проблемы с безопасностью, имеют высокую пропускную способность, являются критически важными для бизнеса или ориентированы на клиентов.

**Используйте рекомендуемые методы применения владения в зависимости от типа сущности**; хотя для применения владения к любой отслеживаемой сущности можно использовать теги, перечисленные методы являются наиболее эффективными способами назначения сущностей владельцам.

* [Метки Kubernetes для объектов Kubernetes](/managed/deliver/ownership/assign-ownership#kubernetes "Assign owners to entities using entity metadata like labels, environment variables, and tags.")
* [Метаданные для хостов](/managed/deliver/ownership/assign-ownership#host-metadata "Assign owners to entities using entity metadata like labels, environment variables, and tags.")
* [Переменные окружения для процессов](/managed/deliver/ownership/assign-ownership#process-env-variables "Assign owners to entities using entity metadata like labels, environment variables, and tags.")
* [Теги (ручные, автоматические и через API) для всех прочих сущностей](/managed/deliver/ownership/assign-ownership#tags "Assign owners to entities using entity metadata like labels, environment variables, and tags.")

### Kubernetes

Для [объектов Kubernetes](/managed/deliver/ownership/assign-ownership#kubernetes "Assign owners to entities using entity metadata like labels, environment variables, and tags.") **определяйте владение одновременно для всех нужных объектов Kubernetes**. Это гарантирует достаточное покрытие владением для всех ваших объектов Kubernetes в момент развёртывания.

* Всегда применяйте метки для **Deployment**.
* Рекомендуется указывать владение как минимум для `CLOUD_APPLICATION` (например, Deployment, Job, CronJob или DaemonSet) и `CLOUD_APPLICATION_INSTANCE` (Pod).
* Уникальность ключей — обязательное требование для [пар ключ-значение](/managed/deliver/ownership/assign-ownership#format "Assign owners to entities using entity metadata like labels, environment variables, and tags.") в метках Kubernetes. Ключи должны начинаться с [пользовательских имён ключей, которые вы определяете для информации о владении](/managed/deliver/ownership/assign-ownership#custom-keys "Assign owners to entities using entity metadata like labels, environment variables, and tags."). Например, в качестве префиксов для создания уникальных ключей можно использовать `owner` и `dt.owner`.

Пример файла развёртывания Kubernetes с определённым владением для Deployment, Pod и процесса

```
apiVersion: apps/v1



kind: Deployment



metadata:



name: demo



labels:



dt.owner-1: my-team-1 # Dual team ownership defined for the Deployment



dt.owner-2: my-team-2



spec:



replicas: 1



selector:



matchLabels:



app: demo



template:



metadata:



labels:



app: demo



dt.owner-1: my-team-1 # Ownership defined for the Pod



spec:



containers:



- name: demo



image: demo:1.0.0



ports:



- containerPort: 8888



env:



- name: DT_CUSTOM_PROP # Environment variable



value: 'dt.owner-1=my-team-1' # Ownership defined for the process
```

### Теги

**Используйте [теги для применения владения](/managed/deliver/ownership/assign-ownership#tags "Assign owners to entities using entity metadata like labels, environment variables, and tags.") только для сущностей, не охватываемых другими методами**.

#### Преимущества и применение тегов

* Теги подходят для назначения **нескольких стабильных сущностей** (например, приложения и синтетических мониторов, работающих против него) конкретным командам-владельцам.
* [Ручное тегирование](/managed/manage/tags-and-metadata/setup/how-to-define-tags#manual "Find out how to define and apply tags manually and automatically.") или [Custom tags API](/managed/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.") эффективны для применения владения к **существующим (уже развёрнутым) сущностям**.
* [Правила автоматического тегирования](/managed/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Find out how to define and apply tags manually and automatically.") имеют преимущество в виде захвата **новых сущностей**, соответствующих вашим правилам тегирования. Автоматически применённые теги также нельзя вручную удалить с отдельных сервисов, групп процессов, экземпляров групп процессов, приложений или хостов.
* Хотя Custom tags API и правила автоматического тегирования используют мощный и гибкий [**селектор сущностей**](/managed/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") для выбора сущностей, **вызов Custom tags API выполняется немедленно**. Это является [значительным преимуществом по сравнению с правилами автоматического тегирования](/managed/manage/tags-and-metadata/basic-concepts/best-practice-tagging-at-scale#custom-tags-api "Optimize auto-tagging and management-zone rules to speed up the automatic assignment process."), которые планируются через процесс тегирования Dynatrace. Это помогает ускорить время выполнения при необходимости сложных правил тегирования.

#### Важные соображения при использовании тегов для владения

* **Ручное тегирование** недостаточно **масштабируется** для назначения владения в больших, динамичных окружениях мониторинга. Ручные теги также можно удалять вручную.
* Хотя (основанные на веб-интерфейсе) **правила автоматического тегирования** разработаны для работы со сложными случаями, автоматические запуски тегирования могут занимать **много времени** в зависимости от сложности ваших правил и размера окружения. В это время критическая сущность, испытывающая проблему, может не получить тег с владением. Подробнее об оптимизации тегирования см. в разделе [Рекомендации по масштабированию тегирования и правил зон управления](/managed/manage/tags-and-metadata/basic-concepts/best-practice-tagging-at-scale "Optimize auto-tagging and management-zone rules to speed up the automatic assignment process.").
* Хотя **вызов Custom tags API** выполняется немедленно, его недостатком является то, что это **однократная операция**. В зависимости от частоты ваших запусков тегирования новые или короткоживущие сущности могут полностью пропустить получение информации о владении, что затруднит поиск владельцев в случае уязвимостей или сбоев.
* **Не рекомендуется** использовать теги для применения владения к процессам или группам процессов.

## Информация о команде

Хотя для создания [команды-владельца](/managed/deliver/ownership/ownership-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership.") обязательны только поля **Team name** и **Team identifier**, приведём рекомендации по использованию других полей.

* При определении [пользовательских ключей](#custom-keys) для идентификаторов владения используйте конкретные, легко понимаемые имена, которые вряд ли будут использоваться для других нужд тегирования.
* Всегда добавляйте **Description** команды — он отображается вместе с именем команды на странице настроек **Ownership teams** и помогает различать команды с первого взгляда. Команды без описания или с плохим именем (team 1) не дают никаких подсказок об их роли в вашей организации. Команды с описаниями (2 и 3) легче идентифицировать.

  ![Team definitions](https://dt-cdn.net/images/ownership-team-definitions-1888-78e12327f8.png)

  Определения команд
* **Дополнительные идентификаторы** — можно определить до трёх на команду — особенно полезны когда:

  + Имя вашей команды меняется — можно добавить дополнительный идентификатор для отражения изменения имени, оставив основной идентификатор команды без изменений. (После создания основной идентификатор команды не может быть изменён.)
  + Вы хотите определить подкоманды. Создайте дополнительный ID для каждой подкоманды — в качестве префикса можно использовать основной ID команды. Например, для основного ID команды `team1` создайте дополнительные ID `team1-taskforce` и `team1-planning`.

  Дополнительные идентификаторы обеспечивают большую гибкость.

  + Независимо от того, применяете ли вы к сущности основной или дополнительный ID команды, она помечается как принадлежащая одной и той же именованной команде.
  + Дополнительные ID можно изменять и удалять.
  + Дополнительный идентификатор может совпадать с основным или дополнительным идентификатором другой команды. В этом случае при применении дополнительного идентификатора к сущности обе команды будут помечены как владельцы.
* Всегда выбирайте **Responsibilities** команды, даже если они не обязательны. Обязанности отображаются на видном месте вместе с описаниями команды в карточке **Ownership** сущности. Эта информация о команде является ключевым индикатором для добавления контактной информации для маршрутизации сообщений и эскалаций.

  ![Ownership card](https://dt-cdn.net/images/ownership-card-responsibilities-905-94c952fe00.png)

  Карточка владения
* Определите хотя бы один email или Slack-канал на команду в **Contact details**, чтобы создать автоматизированный рабочий процесс с целевым уведомлением или просто извлекать контактную информацию любой отслеживаемой сущности при необходимости.
* Для **Additional information**: хотя вы можете определять пары ключ-значение произвольно, рекомендуется рационализировать ключи между командами, чтобы их можно было повторно использовать для одних и тех же видов информации. Например, используйте одинаковые или связанные ключи для определения информации о центрах затрат и другой набор ключей по всей организации для определения иерархий и связей команд.

## Связанные темы

* [Рекомендации по масштабированию тегирования и правил зон управления](/managed/manage/tags-and-metadata/basic-concepts/best-practice-tagging-at-scale "Optimize auto-tagging and management-zone rules to speed up the automatic assignment process.")