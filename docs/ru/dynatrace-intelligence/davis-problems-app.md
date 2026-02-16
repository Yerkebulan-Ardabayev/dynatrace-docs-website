---
title: Problems app
source: https://www.dynatrace.com/docs/dynatrace-intelligence/davis-problems-app
scraped: 2026-02-16T21:09:57.707113
---

# Problems app

# Problems app

* Latest Dynatrace
* App
* 15-min read
* Updated on Jan 28, 2026

Quickly triaging, investigating, and remediating incoming incidents is the core challenge for operations teams. ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** supports them by automatically analyzing complex incidents, collecting all the context, and presenting the root cause and impact within a consistent view.

![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**, backed by data from Grail and Dynatrace Intelligence analysis, helps operational and site reliability teams reduce the mean time to repair (MTTR) by presenting every aspect of the incident.

Prerequisites

### Permissions

The following table describes the required permissions.

Permission

Description

business-analytics:business-flows:read

Read evaluation of affected Business Flows

davis-copilot:conversations:execute

Execute copilot conversations

davis-copilot:document-search:execute

Execute copilot document search

davis:analyzers:execute

Execute problem details analyzer

document:documents:read

Read documents from Doc workflow

document:documents:write

Write documents in Doc workflow

document:documents:delete

Delete documents from Doc workflow

notification:notifications:read

Read notifications for alerting on saved filters

notification:notifications:write

Save notifications for alerting on saved filters

settings:objects:read

Read settings objects from Environment API

10

rows per page

Page

1

of 1

## Installation

Make sure the app is [installed in your environment](/docs/manage/hub#install "See the information about Dynatrace Hub.").

Get started

Use cases

## Aim and context

This page shows you how to use ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** to triage detected problems and investigate their root cause and impact.

## Target audience

This page is written for:

* Operations engineers
* Pipeline engineers
* Systems engineers
* Site reliability engineers (SREs)
* Build automation engineers

## Summary

**Problems** ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") streamlines triage, analysis, and remediation of active incidents by reducing the MTTR. It allows you to focus on AI-detected problems and quickly navigate to their root cause.

* The data provided by Grail and DQL makes it possible to slice and dice all problem-related information for huge amounts of problems and events.
* Integration with context-specific Dynatrace apps allows you to analyze problems without the need to switch the context.

## Investigate and remediate active problems

### Set focus and triage

By default, ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** shows:

* A feed of all problems in the last 2 hours. To help operation teams spot open problems regardless of which filter is set, open problems remain on top of the feed no matter how long they are open.
* A problem chart at the top visualizes any abnormality with a high number of problems in the past. Select a peak on the chart to drill into it and investigate further.

![Problems app - problem feed view](https://dt-cdn.net/images/problem-table-1920-1ff1983035.webp)

#### Filtering

To focus on your domain and triage problems that affect it, set filters. The two most common filtersâ**Status** and **Category**âhave selectable settings to the left of the table for quick access. To set other filters, use the filter bar above the table.

* **Status**âCan be `Active` or `Closed`.

  + If this is not set, all problems (active or closed) are listed.
  + If you select a status in the controls on the left, the corresponding filter is also displayed in the filter bar.
* **Category**âIndicates the nature of the incident, such as slowdowns, errors, resource-related issues, or availability incidents.

  + If you select one or more categories in the controls on the left, the corresponding filters are also displayed in the filter bar.

Filtering with the filter bar allows you to focus your feed on problems based on multiple criteria, such as status, number of affected entities, root cause entity, and more. Place your cursor in the input field to see all the available options. By default, filtering criteria are combined by the **AND** logic. For each criterion, Dynatrace Intelligence provides a list of suggested values, based on your problem feed.

For example, to see problems that are raised due to an increase of JavaScript errors and that persist for longer than 1 hour, use the following filter criteria:

* `Status=ACTIVE`
* `Duration>1h`
* `Category=Error`
* `Name=JavaScript error rate increase`

The problem filter bar supports Boolean logic filters. This allows you to combine **AND** and **OR** criteria and create complex filters using parentheses to group Boolean terms. You can see a Boolean logic filter statement within ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** app in the example below.

![Powerful Boolean Filters within the Problems Filter Bar.](https://dt-cdn.net/images/complex-problem-filters-1920-db9346a85b.png)

#### Leverage predefined Team Segments to increase operational productivity

Segments are predefined filters used for quickly filtering the data to include only the relevant entries. In the context of ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**, you or your team can utilize a predefined set of team-specific segments  to filter your problem tables instead of having to create your own problem filters.

The following example shows how to use segments to filter problems connected to easyTravel.

![Filter by segments in the Problems app.](https://dt-cdn.net/images/problems-filter-by-segments-1920-c5610b610e.png)

In addition, using segments in ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** allows you to:

* Create sets of filters that can be reused by you and shared to the whole team.
* Save time on recreating filters applied during the previous sessions.
* Increase productivity by quickly filtering relevant problems.
* Quickly check the status of your service by creating and applying service-specific segments.

Since problems are stored as events in Grail, segments created for filtering problems must define an event filter. For example, if you want to filter problems that were raised in a specific cloud region, you can create a segment with the following event filter:

```
cloud.region = "us-east-1c" AND event.kind = "DAVIS_PROBLEM"
```

Screenshot example of defining a segment for Problems filtering

![An example of defining a segment for filtering problems in the Problems app.](https://dt-cdn.net/images/problems-segment-definition-1512-4649153a97.png)

Segment filters are directly applied to the problem Grail records. Consequently, no entity filters are applied to the problem unless the entity ID is chosen as a primary field of the filtered problem.

For more information on segments and how they work, see [Segments](/docs/manage/segments "Segments logically structure monitoring data in Grail and function as convenient filters for data that users are allowed to access based on permissions.") ![Segments](https://dt-cdn.net/images/segments-256-8e66310720.webp "Segments").

### Activate auto refresh

To make sure you always catch incoming problems, use the refresh settings ![Refresh](https://dt-cdn.net/images/dashboards-app-refresh-33a794c2f1.svg "Refresh") ![Expand menu](https://dt-cdn.net/images/dashboards-app-menu-expand-3398af0cdf.svg "Expand menu") in the upper-right corner of ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**.

* To automatically refresh the problem feed, select ![Expand menu](https://dt-cdn.net/images/dashboards-app-menu-expand-3398af0cdf.svg "Expand menu") and choose a refresh rate (or select `Off` to turn off automatic refresh)
* To manually refresh the problem feed at any time, regardless of the automatic refresh setting, select ![Refresh](https://dt-cdn.net/images/dashboards-app-refresh-33a794c2f1.svg "Refresh")

### Investigate and compare problems

Чтобы просмотреть детали проблемы

1. В таблице выберите идентификатор проблемы в столбце **ID**.
2. Просмотрите страницу деталей.

Страница деталей проблемы предоставляет все доступные детали о проблеме, выделяя сущность коренной причины красной меткой, чтобы направить ваше внимание на правильные вещи. Пример ниже показывает детали проблемы с ухудшением пользовательского действия — включая сущность коренной причины (`easyTravelBusiness` сервис) и график аномального времени ответа этого сервиса.

![Пример детального просмотра проблемы в приложении Problems.](https://dt-cdn.net/images/problems-details-view-page-1920-3d5f2bb781.png)

Все сущности, затронутые проблемой, перечислены в разделе **Затронутые сущности**, вместе с информацией о типе сущности и количестве событий, обнаруженных во время анализа.

* Как предложение для начала расследования, Dynatrace Intelligence отмечает сущность, которую он определил как коренную причину проблемы.
* Чтобы просмотреть детали о затронутой сущности, выберите ее в таблице.

#### Сравнить несколько проблем

Если все фильтры применены и у вас все еще есть несколько проблем для расследования, вы можете выбрать и сравнить детали нескольких проблем.

1. В таблице используйте флажки для выбора двух или более проблем.
2. Выберите **Показать детали**.

   Это предварительно загружает детали всех выбранных проблем и добавляет элементы управления в правом верхнем углу страницы деталей проблемы, чтобы вы могли быстро переключаться между каждой выбранной проблемой.

### Прочитать свойства событий для получения дополнительной информации

Dynatrace получает события из нескольких источников событий, таких как OneAgent, Synthetic, расширения и API ингестии. Dynatrace принимает и понимает различные свойства (также называемые полями) этих событий, которые предоставляют дополнительную информацию о событии.

Источники событий можно настроить для предоставления информации, необходимой для анализа и устранения проблем, вызванных событиями. Например, связывание конфигурации, которая обнаружила событие (`dt.settings.schema_id` и `dt.settings.object_id`), помогает быстро адаптировать порог или базовую линию, если такое действие необходимо.

Другим примером является регулировка чувствительности пользовательского оповещения, которое вызвало событие, путем изменения конфигурации детектора в настройках.

Поскольку доступные свойства событий зависят от источника события, события, которые не генерируются пользовательскими оповещениями, не содержат ссылок на соответствующие настройки событий. Если вы хотите, чтобы событие ссылалось на объект настроек, вы можете сделать это, присвоив свойство `dt.settings.object_id` событиям, принимаемым через API и/или расширения.

![Проблемы приложения - новое](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Проблемы приложения - новое") **Проблемы** отображают все свойства событий для каждого собранного события в таблице и предоставляют намеренные ссылки, такие как прямая навигация к конфигурации пользовательского оповещения, как показано ниже.

![Проблемы приложения предлагают прямую ссылку на объект настроек.](https://dt-cdn.net/images/problems-app-settings-direct-link-1920-b7ded7d7d3.png)

Примеры мощных свойств событий включают:

* Описание события (`event.description`). Описание события поддерживает текст, отформатированный с помощью Markdown, что позволяет включать ссылки на ресурсы, которые могут помочь устранить проблему.
* Запрос DQL (`dt.query`) позволяет перестроить график события в блокноте или на панели управления или скопировать сырое значение свойства.
* Связанные сущности (`dt.entity.*`) позволяют напрямую навигировать к сущностям через свойства `dt.entity.*`.
* Ссылка на объект настроек (`dt.settings.object_id`) и схему настроек (`dt.settings.schema_id`).

Чтобы узнать больше о семантике и синтаксисе свойств событий и о том, как они могут быть использованы в Dynatrace, см. [Семантический словарь](/docs/semantic-dictionary/fields "Ознакомьтесь со списком глобальных полей, имеющих хорошо определенное семантическое значение в Dynatrace и которые могут быть использованы в разных типах мониторинга.").

### Анализировать проблемы с помощью собственных инструментов, экспортируя CSV

Для случаев, когда ваши программные инструменты создают разрывы интеграции, препятствующие эффективному использованию данных Dynatrace, мы предоставляем возможность экспортировать данные ленты проблем в формате CSV. Вы можете позже использовать эти данные в различных инструментах, включая программы для работы с электронными таблицами, базы данных и инструменты анализа данных.

Как показано ниже, вы можете экспортировать связанные с проблемой данные из таблицы ленты проблем. Вы также можете экспортировать их из **Блокнотов** и **Панелей управления** во всех визуализациях таблиц.

![Экспорт выбранных проблем в виде файла CSV.](https://dt-cdn.net/images/problems-app-csv-export-1920-c5d456c07a.png)

Вы можете экспортировать все загруженные проблемы (до предела в 1000) или использовать функцию многократного выбора для выбора конкретных проблем. Кроме того, панель фильтров над таблицей позволяет фильтровать более крупные подмножества проблем. Флажок **Выбрать все** помогает экспортировать все проблемы в фильтрованном наборе записей.

### Проверить коренную причину, не покидая контекст

В зависимости от ответственности вашей команды, вы можете сосредоточить внимание на кластерах Kubernetes, облачных ресурсах и рабочих нагрузках критически важных сервисов. Чтобы минимизировать переключение контекста, Dynatrace предлагает последовательную информацию о коренной причине через несколько приложений. Независимо от того, где начинается ваше расследование, вам не нужно переключаться на ![Проблемы приложения - новое](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Проблемы приложения - новое") **Проблемы**, чтобы увидеть коренную причину.

В примере ниже приложение **Kubernetes** отображает информацию о проблеме, влияющей на рабочую нагрузку.

![Проблемная информация, интегрированная в приложение Kubernetes.](https://dt-cdn.net/images/dynatrace-intelligence-in-k8s-app-1920-2da55950a8.png)

### Расследовать все актуальные для проблемы журналы

Проблема, проанализированная Davis, подчеркивает коренную причину инцидента и показывает все актуальные для инцидента строки журнала через несколько сущностей на странице деталей проблемы.

Чтобы получить доступ к строкам журнала, собранным во время инцидента, выберите вкладку **Журналы**. Кроме того, вы можете увидеть их уровень журнала во всех сущностях, затронутых проблемой, что позволяет сэкономить время на ручных расследованиях и фильтрации журналов актуальных сущностей отдельно.

Вкладка **Журналы** также включает ссылки на затронутые сущности и информацию обо всех связанных сущностях, таких как родительские хосты. Чтобы проверить, какие сущности затронуты событием проблемы, вы можете обратиться ко всем свойствам событий, начинающимся с префикса `dt.entity.`.

Посмотрите, как вкладка **Журналы** суммирует все актуальные для проблемы журналы на изображении ниже.

![Dynatrace Intelligence Problems app журнал подсчета.](https://dt-cdn.net/images/problems-log-count-1920-330dd46337.png)

Изображение ниже иллюстрирует дальнейшую сортировку строк журнала с помощью запроса DQL.

![Dynatrace Intelligence Problems app строки журнала ошибок.](https://dt-cdn.net/images/problems-error-log-lines-1920-cb4599df02.png)

### Визуально уведомлять и автоматизировать, чтобы ускорить устранение

![Проблемы приложения - новое](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Проблемы приложения - новое") **Проблемы** имеют глобальный индикатор проблемы, который показывает количество активных проблем в окружении и всегда виден в Dock. Когда Dock свернут, красная точка отображается рядом с иконкой приложения вместо номера.

Чтобы персонализировать индикатор и количество отображаемых активных проблем, выберите фильтры в **Категории** и сохраните конфигурацию фильтра, выбрав иконку . Сохраненный фильтр будет автоматически применен к глобальному индикатору проблемы, уменьшая количество проблем, подсчитываемых для пользователя, как показано ниже. Выбор кнопки **Фильтр по умолчанию** восстанавливает последнюю сохраненную конфигурацию.

![Сохранение конфигурации фильтра в Problems app.](https://dt-cdn.net/images/problems-app-notifications-config-save-1920-af4147c3c1.png)

Пока фильтр проблемы активен, номер индикатора будет показывать только активные проблемы из выбранных категорий. Индикатор обновляется по расписанию каждую минуту, что означает, что после обновления фильтра может потребоваться некоторое время, чтобы индикатор адаптировался.

Вы также можете настроить уведомления по электронной почте для отфильтрованных проблем, используя свой адрес электронной почты, выбрав иконку , как показано ниже:

![Включение уведомлений по электронной почте для примененных фильтров в Problems app.](https://dt-cdn.net/images/problems-app-turn-on-notifications-1920-6806895778.png)

Уведомление по электронной почте является вашей личной настройкой, поэтому вы можете включить его без необходимости конфигурационных разрешений или риска влияния на других пользователей в одном и том же окружении.

Уведомление по электронной почте запускается直接 в OpenPipeline, что означает, что могут быть применены только простые фильтры. Потоки работы, которые запрашивают **Проблемы** через DQL, могут использовать полный набор функций запросов Grail, таких как соединение таблиц.

Если вам нужно отправлять настраиваемые сообщения по электронной почте или иметь более сложные требования к автоматизации и интеграции, вы должны применить полный поток работы вместе с триггером проблемы.

### Визуализировать затронутые развертывания, чтобы получить дополнительные сведения

(Этот раздел отсутствует в исходном тексте)



The **Deployment** perspective equips operations teams with deeper insight into the infrastructure and cloud resources impacted by large-scale incidents. The root cause analysis feature automatically collects and visualizes affected deployments and related resources.

The additional context provided by related resources allows you to:

* Quickly understand where an affected resource resides, for example, a specific cloud region or Kubernetes cluster.
* Gather additional insight for multicloud deployments by showing an app's deployment across clouds, regions, and technology boundaries.

**Deployment** view uses a diagram similar to a Unified Modeling Language (UML) deployment diagram and follows a top-down approach, starting with the largest container element at the top and becoming more detailed as you drill down. The deployment structure is visualized as collapsible cards with horizontally overlapping elements, for example, services running in multiple regions. In this case, cards representing such services are duplicated and shown in multiple deployment stacks.

The deployment containing the root cause is automatically expanded and tagged with a red root cause badge, while all other deployments are collapsed by default. The deployment hierarchy is focused on a maximum of 5 levels, starting with the hierarchy leaf nodes at the bottom of the diagram upwards, seen in the example below:

![Dynatrace Intelligence Problems Deployment view with highlighted root cause.](https://dt-cdn.net/images/problem-deployment-view-1920-e646972d40.png)

Interactivity is a crucial feature of the deployment view. On the right side, you can click on any element to visualize findings, such as events related to the problem, along with a direct link to the selected entity. This structured approach allows you and your operations team to reduce the time needed to respond to incidents by navigating a familiar visual representation.

Not all incident-relevant related elements may show information on the right. Some elements, like the cloud region, are displayed for better context but may not necessarily show problem-relevant events.

### Define custom problem fields

Dynatrace Intelligence causal AI root-cause detection identifies and reports issues triggered by one or more events within a Dynatrace environment, and saves the results in the form of a problem record in Grail.

The problem record includes an array of event IDs (`dt.davis.event_ids`) that represents all the events collected and merged during the root-cause analysis. Event-related **Problems** table fields such as category, name, description, status, start, and end are derived from these events, which allows you to efficiently filter and sort all incoming problem records.

By default, Dynatrace propagates a set of built-in problem fields along with record-level permission fields, such as `dt.host_group.id`, `k8s.namespace.name`, `k8s.cluster.name`, onto problems. For the full list of built-in problem fields, see [Record level permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.").

Other built-in and custom event fields are not automatically propagated to avoid an excessive number of problem records.

In Davis events, permission policies based on Grail record-level permissions work as expected because the fields contain single values. However, when multiple events are aggregated into a problem, the values of the same field are combined into an array. Due to the current implementation of Grail record-level permission filters, only `dt.security_context` supports filtering array values. Other permission fields can't be used with array-based filters in permission policies.

This behavior differs from the DQL filter functionality, where array filters on array fields are fully supported. While this limitation may impact the flexibility of permission filters, itâs important to consider when you're managing permission policies.

* Dynatrace doesn't allow you to define problem field names that repeat existing [Semantic Dictionary](/docs/semantic-dictionary/model/davis#davis-ai-events "Get to know the Semantic Dictionary models related to Davis AI.") event field names.
* You can only define problem fields for source fields with values of type `string`. Fields that contain values of other types aren't supported.

#### Custom problem fields modification

To view or change the fields automatically propagated from events to problems, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **Dynatrace Intelligence** > **Root cause analysis** > **Problem fields**. By modifying these problem fields, you can:

* Subscribe to custom record fields to be automatically propagated from all single events to any detected problem.
* Rename existing problem fields.
* Remove problem fields.

Renaming existing problem fields and removing problem fields changes current and future Grail problem records and may break your DQL queries.

To learn more about custom problem fields use cases, see [Dynatrace Intelligence Problems use cases](/docs/dynatrace-intelligence/davis-problems-app/problems-app-custom-problem-field-examples "Explore scenarios of how you can use custom problem fields in Problems.").

### Create a troubleshooting guide

![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** allows you to create troubleshooting guides using ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** or ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** to document your investigation and the steps taken to resolve the problem. The guide is based on a predefined template and contains two types of sections:

* Sections with information extracted directly from the problem.
* Template sections (such as `Initial Response & Detection`, `Troubleshooting`, and `Remediation steps`) that you can edit to describe the process and steps followed to resolve the problem.

To create a troubleshooting guide

1. Go to ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** and open the problem you need to resolve.
2. On the problem details page, select **Troubleshooting**.
3. Select  **New**.

   * Select  **Notebooks** to create a new document in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
   * Select  **Dashboards** to create a new document in ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
4. Follow the instructions in the template to document the details for your troubleshooting guide.

If you share a troubleshooting guide with all users in your environment, and you have enabled document suggestions based on vector similarity, Dynatrace Intelligence generative AI will index your document and proactively suggest it to your team to help them remediate similar problems faster. To learn more about Dynatrace Intelligence generative AI document suggestions, see [Find relevant documents with Dynatrace Intelligence generative AI](/docs/dynatrace-intelligence/copilot/copilot-find-relevant-troubleshooting-guides "Learn how Dynatrace Intelligence generative AI can suggest troubleshooting guides for problem remediation.").

The ability to create and share troubleshooting guides allows DevOps teams to:

* Share and spread their domain knowledge about specific business logic, software implementation, and infrastructure.
* Enrich the Dynatrace AI in their environment with shared knowledge for a more streamlined, tailored experience during problem investigation and remediation.
* Enrich the Dynatrace AI in their environment.

### Resolve the cases of missing events

Dynatrace offers a wide range of tools suited for your needs, such as configuring user group permissions, Dynatrace Intelligence alerting rules, or OpenPipeline ingestion rules. Due to the rich customization options, however, there are cases that might lead to events not being visible in ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** and differences in the number of affected entities in the available tabs. The most common reasons for events "missing" from ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** are:

* Difference in bucket retention period: you can configure your bucket retention period for the monitored data to last longer, so that the events related to the problem will be visible regardless of how long the problem has been in the open state. To learn more about configuring bucket retention period for monitored data, see [Retain trace data for long periods](/docs/observe/application-observability/distributed-tracing/data-retention "Create and assign buckets with custom data retention for your trace data in Grail.").
* Missing permissions necessary for viewing the event: check with your Dynatrace support group and ensure that you have necessary permissions. Ask the administrator to adjust permissions, so the event becomes visible to you.
* OpenPipeline ingestion rules dropping records: you can adjust OpenPipeline ingestion rules to prevent it from dropping any records or broaden the rules to keep records that might be connected to the alerted problem. To learn more about configuring OpenPipeline ingestion rules, see [Log processing with OpenPipeline](/docs/analyze-explore-automate/logs/lma-log-processing/lma-openpipeline "Process logs using Dynatrace OpenPipeline.").

### Streamline problem resolution with problems-specific drill-down options

![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** предоставляет варианты детального анализа, предназначенные для того, чтобы направить вас к наиболее актуальным действиям для решения обнаруженных проблем и помочь вам оптимизировать процесс решения проблем.

Варианты детального анализа, доступные вам, отображаются в представлении деталей проблемы и зависят от типа затронутой сущности (например, сервиса, рабочей нагрузки Kubernetes, хоста или зоны доступности AWS).

Некоторые из доступных вариантов детального анализа:

* Анализ неудач: Проведите сосредоточенный анализ неудач, чтобы выявить коренную причину неудач, моделей ошибок или проблем с производительностью.
* Просмотр связанных журналов: Изучите актуальные записи журнала напрямую в ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**.
* Просмотр неудачных трасс: Проанализируйте неудачные трассы в ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**, чтобы понять коренную причину неудач.
* Просмотр `app`: Перейдите на страницу деталей связанного приложения. Точное название зависит от затронутой сущности (например, Просмотр сервиса, Просмотр рабочей нагрузки Kubernetes или Просмотр хоста).

Чтобы получить доступ к вариантам детального анализа

1. В **Dynatrace**, перейдите к ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**.
2. Выберите проблему, которую вы хотите изучить из обзора ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**. Это открывает страницу деталей проблемы.
3. Необязательно: В левой части страницы деталей проблемы выберите затронутую сущность или инфраструктуру, которую вы хотите изучить дальше. Обычно, когда вы открываете страницу деталей проблемы, затронутая сущность предварительно выбрана для вас.
4. Из деталей затронутой сущности справа выберите предпочтительный вариант для дальнейшего изучения.

   * Выберите  > **Просмотр связанных журналов**, чтобы продолжить изучение без выхода из ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**.
   * Выберите  > **Просмотр неудачных трасс**, чтобы продолжить изучение в [![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**](/docs/observe/application-observability/distributed-tracing "Отслеживайте и анализируйте в режиме реального времени высоко分布енные системы с помощью Grail.").
   * Выберите  > **Просмотр** `app`, чтобы продолжить изучение в одном из доступных приложений Dynatrace.
   * Выберите  > **Открыть с помощью**, чтобы увидеть все доступные варианты изучения.

Варианты детального анализа обеспечивают бесшовную навигацию между ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** и другими приложениями Dynatrace, чтобы обеспечить фокус и непрерывность в решении проблем.

### Просмотр обзора проблемы

**Обзор** - это краткий, исполнительный сводка обнаруженной проблемы.

Чтобы просмотреть обзор проблемы

1. Перейдите к ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** и откройте проблему, которую вы хотите решить.
2. На странице деталей проблемы выберите **Обзор**.

   **Пример**:

   ![Пример деталей проблемы Обзор вкладки](https://dt-cdn.net/images/problems-screenshot-with-overview-1920-6c68de3f34.png)

**Обзор** имеет четыре раздела:

Раздел

Описание

[Воздействие](#overview-impact)

Отображает все затронутые сущности Smartscape (например, сервисы, процессы и хосты) вместе с краткими деталями проблемы для каждой сущности.

[Коренная причина](#overview-root-cause)

Сосредоточен на коренной причине проблемы, включая подробную информацию о затронутом стеке развертывания.

[Визуальный путь решения](#overview-visual-resolution-path)

Графически иллюстрирует отношения между фронтендами, сервисами и бэкендами, участвующими в проблеме.

[Автоматизация и решение](#overview-automation-and-remediation)

Перечисляет все рабочие потоки автоматизации, запущенные проблемой, такие как уведомления, решения и внешние интеграции.

Настройка макета

Вы можете переместить эти разделы, чтобы персонализировать ваш вид **Обзора**.

1. В заголовке раздела, который вы хотите переместить, выберите  и перетащите раздел.
2. Отпустите раздел там, где вы хотите, чтобы он появился в макете.

Эти изменения сохраняются на пользователя. Ваши изменения макета не влияют на то, как другие видят обзор.

### Воздействие

Раздел **Воздействие** отображает все затронутые сущности Smartscape (например, сервисы, процессы и хосты) вместе с краткими деталями проблемы для каждой сущности.

Раздел **Воздействие** категоризирован по:

* **Фронтенды**
* **Сервисы**
* **Инфраструктура**
* **Синтетическое мониторинг**
* **Окружение**

### Коренная причина

Раздел **Коренная причина** сосредоточен на коренной причине проблемы, включая подробную информацию о затронутом стеке развертывания. Это может включать:

* Процесс и хост, где работает сервис коренной причины.
* Рабочая нагрузка Kubernetes, обслуживающая затронутый сервис.

Чтобы обеспечить последовательность, сущность коренной причины также перечислена в таблице **Воздействие**.

### Визуальный путь решения

Раздел **Визуальный путь решения** графически иллюстрирует отношения между фронтендами, сервисами и бэкендами, участвующими в проблеме.

* Каждый узел представляет сущность Smartscape (фронтенд, сервис или бэкенд), где была обнаружена проблема с работоспособностью.
* Серые узлы указывают на связанные сущности, используемые в анализе, но не直接 затронутые.

Эта схема помогает объяснить, как Dynatrace AI определила сервис коренной причины.

Чтобы максимизировать ваш вид графика, выберите  **Максимизировать**.

### Автоматизация и решение

Раздел **Автоматизация и решение** перечисляет все рабочие потоки автоматизации, запущенные проблемой. Эти рабочие потоки могут включать:

* Уведомления, отправленные командам реагирования.
* Потоки решения и руководства по автоматизированному решению.
* Внешние триггеры агентов ИИ, такие как агенты SRE облачных платформ, для сбора дополнительных сведений или решения проблем в инфраструктуре облачного поставщика.

Таблица предоставляет ключевые детали для каждого рабочего потока, включая:

* Последнее время запуска (поскольку рабочие потоки могут запускаться несколько раз во время обновления проблемы).
* Состояние выполнения (например, успех или неудача).

Детали выполнения рабочего потока основаны на стандартных событиях выполнения рабочего потока, которые также можно запросить с помощью DQL в [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Анализируйте, визуализируйте и делитесь сведениями из ваших данных наблюдаемости - все в одном совместном, настраиваемом рабочем пространстве.") и [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Создайте интерактивные, настраиваемые представления для визуализации, анализа и обмена вашими данными наблюдаемости в режиме реального времени.").

**Примечание**:

* Только пользователи с разрешениями на чтение системных событий могут просматривать выполнение рабочего потока. Без этих разрешений таблица пуста, и сообщение указывает на отсутствие доступа.
* Рабочие потоки, не共享енные с вашим пользователем, перечислены, но отображаются в сером цвете без прямых ссылок, указывая на ограниченный доступ.

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

## Изучите в Dynatrace Hub

Триаж, расследуйте и устраните инциденты直接 в ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**.](https://www.dynatrace.com/hub/detail/problems/)