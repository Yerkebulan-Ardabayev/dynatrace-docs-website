---
title: Приложение для проблем
source: https://www.dynatrace.com/docs/dynatrace-intelligence/davis-problems-app
scraped: 2026-02-17T04:45:25.029159
---

# Приложение для проблем

# Приложение для проблем

* Latest Dynatrace
* App
* 15-min read
* Updated on Jan 28, 2026

Быстрое выявление, расследование и устранение входящих инцидентов является основной задачей для команд операций. ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Приложение для проблем - новое") **Приложение для проблем** поддерживает их, автоматически анализируя сложные инциденты, собирая все контекст и представляя коренную причину и влияние в рамках согласованного вида.

![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Приложение для проблем - новое") **Приложение для проблем**, поддерживаемое данными из Grail и анализом Dynatrace Intelligence, помогает операционным и командам по обеспечению надежности сайта сократить среднее время ремонта (MTTR) путем представления всех аспектов инцидента.

Предварительные условия

### Права доступа

Ниже приведена таблица, описывающая необходимые права доступа.

Право доступа

Описание

business-analytics:business-flows:read

Чтение оценки затронутых бизнес-потоков

davis-copilot:conversations:execute

Выполнение разговоров с копилотом

davis-copilot:document-search:execute

Выполнение поиска документов с копилотом

davis:analyzers:execute

Выполнение анализатора деталей проблемы

document:documents:read

Чтение документов из рабочего процесса Doc

document:documents:write

Запись документов в рабочем процессе Doc

document:documents:delete

Удаление документов из рабочего процесса Doc

notification:notifications:read

Чтение уведомлений для оповещения о сохраненных фильтрах

notification:notifications:write

Сохранение уведомлений для оповещения о сохраненных фильтрах

settings:objects:read

Чтение объектов настроек из Environment API

10

строк на странице

Страница

1

из 1

## Установка

Убедитесь, что приложение [установлено в вашей среде](/docs/manage/hub#install "Смотрите информацию о Dynatrace Hub.").

Начало работы

Сценарии использования

## Цель и контекст

Эта страница показывает вам, как использовать ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Приложение для проблем - новое") **Приложение для проблем** для выявления обнаруженных проблем и расследования их коренной причины и влияния.

## Целевая аудитория

Эта страница написана для:

* Инженеров по эксплуатации
* Инженеров по конвейерам
* Системных инженеров
* Инженеров по обеспечению надежности сайта (SRE)
* Инженеров по автоматизации сборки

## Резюме

**Приложение для проблем** ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Приложение для проблем - новое") упрощает выявление, анализ и устранение активных инцидентов, сокращая MTTR. Это позволяет вам сосредоточиться на проблемах, обнаруженных с помощью ИИ, и быстро перейти к их коренной причине.

* Данные, предоставляемые Grail и DQL, позволяют анализировать все связанные с проблемой сведения для огромного количества проблем и событий.
* Интеграция с контекстно-зависимыми приложениями Dynatrace позволяет анализировать проблемы без необходимости переключать контекст.

## Расследование и устранение активных проблем

### Установка фокуса и выявление

По умолчанию, ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Приложение для проблем - новое") **Приложение для проблем** показывает:

* Ленту всех проблем за последние 2 часа. Чтобы помочь командам операций обнаружить открытые проблемы, независимо от установленного фильтра, открытые проблемы остаются вверху ленты, независимо от того, как долго они открыты.
* График проблем вверху визуализирует любые аномалии с большим количеством проблем в прошлом. Выберите пик на графике, чтобы более подробно расследовать.

![Problems app - problem feed view](https://dt-cdn.net/images/problem-table-1920-1ff1983035.webp)

#### Фильтрация

Чтобы сосредоточиться на вашем домене и выявить проблемы, которые на него влияют, установите фильтры. Два наиболее распространенных фильтра - **Статус** и **Категория** - имеют настраиваемые параметры слева от таблицы для быстрого доступа. Чтобы установить другие фильтры, используйте строку фильтрации над таблицей.

* **Статус** - может быть `Активно` или `Закрыто`.

  + Если это не установлено, перечислены все проблемы (активные или закрытые).
  + Если вы выбираете статус в контроле слева, соответствующий фильтр также отображается в строке фильтрации.
* **Категория** - указывает на характер инцидента, такой как замедления, ошибки, проблемы, связанные с ресурсами, или инциденты доступности.

  + Если вы выбираете одну или несколько категорий в контроле слева, соответствующие фильтры также отображаются в строке фильтрации.

Фильтрация с помощью строки фильтрации позволяет сосредоточить ленту на проблемах на основе нескольких критериев, таких как статус, количество затронутых сущностей, коренная причина сущности и многое другое. Поместите курсор в поле ввода, чтобы увидеть все доступные варианты. По умолчанию критерии фильтрации объединяются логикой **И**. Для каждого критерия Dynatrace Intelligence предоставляет список предложенных значений, основанных на вашей ленте проблем.

Например, чтобы увидеть проблемы, которые были вызваны увеличением ошибок JavaScript и которые сохраняются более 1 часа, используйте следующие критерии фильтрации:

* `Статус=АКТИВНО`
* `Продолжительность>1ч`
* `Категория=Ошибка`
* `Имя=Увеличение ошибок JavaScript`

Строка фильтрации проблем поддерживает логические фильтры с использованием булевой логики. Это позволяет объединять критерии **И** и **ИЛИ** и создавать сложные фильтры, используя скобки для группировки булевых термов. Вы можете увидеть выражение логической фильтрации в приложении **Приложение для проблем** в примере ниже.

![Мощные булевы фильтры в строке фильтрации проблем.](https://dt-cdn.net/images/complex-problem-filters-1920-db9346a85b.png)

#### Использование предварительно определенных сегментов команд для увеличения операционной производительности

Сегменты - это предварительно определенные фильтры, используемые для быстрой фильтрации данных, чтобы включить только соответствующие записи. В контексте приложения **Приложение для проблем** вы или ваша команда можете использовать предварительно определенный набор командных сегментов для фильтрации таблицы проблем вместо того, чтобы создавать свои собственные фильтры проблем.

Пример ниже показывает, как использовать сегменты для фильтрации проблем, связанных с easyTravel.

![Фильтрация по сегментам в приложении для проблем.](https://dt-cdn.net/images/problems-filter-by-segments-1920-c5610b610e.png)

Кроме того, использование сегментов в приложении **Приложение для проблем** позволяет:

* Создавать наборы фильтров, которые можно повторно использовать вами и вашей командой.
* Экономить время на повторном создании фильтров, примененных во время предыдущих сессий.
* Повысить производительность, быстро фильтруя соответствующие проблемы.
* Быстро проверять статус вашей службы, создавая и применяя служебные сегменты.

Поскольку проблемы хранятся как события в Grail, сегменты, созданные для фильтрации проблем, должны определять фильтр событий. Например, если вы хотите фильтровать проблемы, которые были вызваны в определенном облачном регионе, вы можете создать сегмент с следующим фильтром событий:

```
cloud.region = "us-east-1c" AND event.kind = "DAVIS_PROBLEM"
```

Пример экрана определения сегмента для фильтрации проблем

![Пример определения сегмента для фильтрации проблем в приложении для проблем.](https://dt-cdn.net/images/problems-segment-definition-1512-4649153a97.png)

Фильтры сегментов применяются напрямую к записям проблем Grail. Следовательно, фильтры сущностей не применяются к проблеме, если идентификатор сущности не выбран в качестве основного поля фильтрованной проблемы.

Для получения дополнительной информации о сегментах и том, как они работают, см. [Сегменты](/docs/manage/segments "Сегменты логически структурируют данные мониторинга в Grail и функционируют как удобные фильтры для данных, к которым пользователи имеют доступ на основе разрешений.") ![Сегменты](https://dt-cdn.net/images/segments-256-8e66310720.webp "Сегменты").

### Активация автоперезагрузки

Чтобы всегда обнаруживать входящие проблемы, используйте настройки перезагрузки ![Перезагрузка](https://dt-cdn.net/images/dashboards-app-refresh-33a794c2f1.svg "Перезагрузка") ![Расширить меню](https://dt-cdn.net/images/dashboards-app-menu-expand-3398af0cdf.svg "Расширить меню") в правом верхнем углу приложения **Приложение для проблем**.

* Чтобы автоматически перезагрузить ленту проблем, выберите ![Расширить меню](https://dt-cdn.net/images/dashboards-app-menu-expand-3398af0cdf.svg "Расширить меню") и выберите скорость перезагрузки (или выберите `Выключено`, чтобы отключить автоматическую перезагрузку)
* Чтобы вручную перезагрузить ленту проблем в любое время, независимо от настройки автоматической перезагрузки, выберите ![Перезагрузка](https://dt-cdn.net/images/dashboards-app-refresh-33a794c2f1.svg "Перезагрузка")

### Расследование и сравнение проблем



To see the details of a problem

1. In the table, select the problem ID in the **ID** column.
2. Review the details page.

The problems details page provides all available details about the problem, highlighting the root cause entity with a red mark, to guide your attention to the right things. The example below shows details of a problem with user action degradationâincluding the root cause entity (`easyTravelBusiness` service) and a chart of abnormal response time of that service.

![Example of the problem detail view in the Problems app.](https://dt-cdn.net/images/problems-details-view-page-1920-3d5f2bb781.png)

All entities affected by the problem are listed in the **Affected entities** section, along with information about entity type and the number of events, detected during the analysis.

* As a suggestion for the starting point of the investigation, Dynatrace Intelligence marks the entity that it determined to be the root cause of the problem.
* To review details about an affected entity, select it in the table.

#### Compare multiple problems

If all the filters are applied and you still have multiple problems to investigate, you can select and compare the details of multiple problems.

1. In the table, use the checkboxes to select two or more problems.
2. Select **Show details**.

   This preloads the details of all selected problems and adds controls to the upper-right corner of the problem details page so you can quickly switch between each selected problem.

### Read event properties for additional information

Dynatrace receives events from multiple event sources, such as OneAgent, Synthetic, extensions, and ingestion APIs. Dynatrace accepts and understands various properties (also referred to as fields) of those events that provide additional information about the event.

Event sources can be customized to provide the information you need to analyze and remediate problems caused by the events. For example, linking the configuration that detected the event (`dt.settings.schema_id` and `dt.settings.object_id`) helps you to quickly adapt the threshold or baseline if such action is necessary.

Another example is adjusting the sensitivity of the custom alert that triggered the event by modifying the detector's configuration in the settings.

Since available event properties depend on the event's source, events that are not generated by custom alerts don't contain links to relevant event settings. If you want an event to link to a settings object, you can do so by attaching a `dt.settings.object_id` property to events ingested via API and/or extensions.

![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** displays all event properties for each collected event in a table and provides intent links, such as direct navigation to a custom alert's configuration, as shown below.

![Problems app offering a direct link to settings object.](https://dt-cdn.net/images/problems-app-settings-direct-link-1920-b7ded7d7d3.png)

Examples of powerful event properties include:

* Event description (`event.description`). The event description supports Markdown-formatted text, enabling you to include links to resources that can help to remediate the problem.
* DQL query (`dt.query`) allows you to rebuild the event's chart in a notebook or at a dashboard or to copy the raw value of a property.
* Related entities (`dt.entity.*`) allow you to directly navigate to entities through the `dt.entity.*` properties.
* Link to a settings object (`dt.settings.object_id`) and settings schema (`dt.settings.schema_id`).

To learn more about the semantics and syntax of event properties and how they can be used across Dynatrace, see [Semantic Dictionary](/docs/semantic-dictionary/fields "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.").

### Analyze problems with your own tools by exporting CSV

For cases when your software tools create integration gaps preventing you from effective usage of Dynatrace data, we provide the ability to export problem feed data in the CSV format. You can later use this data in various tools, including spreadsheet programs, databases, and data analysis tools.

As illustrated below, you can export problem related-data from the problem feed table. You can also export it from **Notebooks** and **Dashboards** within all table visualizations.

![Export selected problems as a CSV file.](https://dt-cdn.net/images/problems-app-csv-export-1920-c5d456c07a.png)

You can export all loaded problems (up to a limit of 1000) or use the multi-select feature to choose specific problems. Additionally, the filter bar above the table allows you to filter through larger subsets of problems. The **Select all** checkbox helps you to export all problems in the filtered set of entries.

### Check the root cause without leaving your context

Depending on your team's responsibility, you might want to focus your attention on Kubernetes clusters, cloud resources, and workloads of critical services. To minimize context switching, Dynatrace offers consistent root cause information across multiple apps. No matter where your investigation starts, you don't have to switch to ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** to see the root cause.

In the example below, the **Kubernetes** app displays information about a problem affecting a workload.

![Problem information integrated into the Kubernetes app.](https://dt-cdn.net/images/dynatrace-intelligence-in-k8s-app-1920-2da55950a8.png)

### Investigate all problem relevant logs

A Davis-analyzed problem highlights the root cause of an incident and shows all the incident-relevant log lines across multiple entities in the problem details.

To access the log lines that were collected during the incident, select the **Logs** tab. Additionally, you're able to see their log level across all entities affected by the problem, allowing you to save time on manual investigations and filtering logs of relevant entities separately.

The **Logs** tab also includes references to the affected entities and information about all related entities, such as parent hosts. To verify which entities are affected by the problem event, you can refer to all the event properties that start with the `dt.entity.` prefix.

See how **Logs** tab summarizes all problem-relevant logs in the image below.

![Dynatrace Intelligence Problems app log count.](https://dt-cdn.net/images/problems-log-count-1920-330dd46337.png)

The image below illustrates the further sorting of the log lines with the help of a DQL query.

![Dynatrace Intelligence Problems app error log lines.](https://dt-cdn.net/images/problems-error-log-lines-1920-cb4599df02.png)

### Visually notify and automate to speed up remediation

![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** features a global problem indicator that shows the number of active problems within the environment and is always visible in the Dock. When the Dock is collapsed, a red dot is displayed next to the app icon instead of a number.

To personalize the indicator and the number of the displayed active issues, select filters in **Category** and save the filter configuration by selecting the  icon. The saved filter will automatically apply to the global problem indicator, reducing the number of problems counted for the user, as shown below. Selecting the **Default filter** button restores the last saved configuration.

![Saving filter configuration in Problems app.](https://dt-cdn.net/images/problems-app-notifications-config-save-1920-af4147c3c1.png)

While a problem filter is active, the indicator number will only show active problems from your chosen categories. The indicator updates on a one-minute schedule, which means that after the filter is updated, it can take some time for the indicator to adapt.

You can also set up email notifications for filtered problems using your email address by selecting the  icon, as shown below:

![Turning on email notifications for the filters applied in the Problems app.](https://dt-cdn.net/images/problems-app-turn-on-notifications-1920-6806895778.png)

The email notification is your personal setting, so you can enable it without the need for configuration permissions or the risk of impacting other users within the same environment.

The email notification is directly triggered within OpenPipeline, meaning only simple filters can be applied. Workflows that query ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** through DQL can use the complete feature set of Grail queries, such as joining tables.

If you need to send out customized email messages or have more complex automation and integration needs, you should apply a complete workflow along with the problem trigger.

### Visualize affected deployments to gather additional insights

**Развертывание** перспектива обеспечивает команды эксплуатации более глубоким пониманием инфраструктуры и облачных ресурсов, затронутых крупномасштабными инцидентами. Функция анализа коренной причины автоматически собирает и визуализирует затронутые развертывания и связанные с ними ресурсы.

Дополнительный контекст, предоставляемый связанными ресурсами, позволяет вам:

* Быстро понять, где находится затронутый ресурс, например, в конкретном облачном регионе или кластере Kubernetes.
* Собрать дополнительную информацию для развертываний в нескольких облаках, показывая развертывание приложения в облаках, регионах и технологических границах.

**Развертывание** представление использует диаграмму, подобную диаграмме развертывания Unified Modeling Language (UML), и следует подходу сверху вниз, начиная с самого большого контейнерного элемента вверху и становясь более подробным, когда вы углубляетесь. Структура развертывания визуализируется в виде сворачиваемых карточек с горизонтально перекрывающимися элементами, например, сервисами, работающими в нескольких регионах. В этом случае карточки, представляющие такие сервисы, дублируются и показываются в нескольких стопках развертывания.

Развертывание, содержащее коренную причину, автоматически разворачивается и помечается красной меткой коренной причины, в то время как все остальные развертывания сворачиваются по умолчанию. Иерархия развертывания фокусируется на максимум 5 уровнях, начиная с листовых узлов иерархии в нижней части диаграммы, как показано в примере ниже:

![Dynatrace Intelligence Problems Deployment view с выделенной коренной причиной.](https://dt-cdn.net/images/problem-deployment-view-1920-e646972d40.png)

Интерактивность является важной функцией представления развертывания. Справа вы можете кликнуть на любой элемент, чтобы визуализировать результаты, такие как события, связанные с проблемой, вместе с прямой ссылкой на выбранную сущность. Этот структурированный подход позволяет вам и вашей команде эксплуатации сократить время, необходимое для реагирования на инциденты, навигируя по знакомому визуальному представлению.

Не все связанные с инцидентом элементы могут показывать информацию справа. Некоторые элементы, такие как облачный регион, отображаются для лучшего контекста, но могут не обязательно показывать события, связанные с проблемой.

### Определение пользовательских полей проблем

Dynatrace Intelligence причинно-следственный анализ коренной причины выявляет и сообщает о проблемах, вызванных одним или несколькими событиями в среде Dynatrace, и сохраняет результаты в виде записи проблемы в Grail.

Запись проблемы включает в себя массив идентификаторов событий (`dt.davis.event_ids`), который представляет все события, собранные и объединенные во время анализа коренной причины. Событийные поля **Проблем** таблицы, такие как категория, имя, описание, статус, начало и конец, получаются из этих событий, что позволяет вам эффективно фильтровать и сортировать все входящие записи проблем.

По умолчанию Dynatrace распространяет набор встроенных полей проблем вместе с полями разрешений на уровне записи, такими как `dt.host_group.id`, `k8s.namespace.name`, `k8s.cluster.name`, на проблемы. Для полного списка встроенных полей проблем см. [Разрешения на уровне записи в Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table-record "Узнайте, как назначать разрешения на бакеты и таблицы в Grail.").

Другие встроенные и пользовательские поля событий не автоматически распространяются, чтобы избежать чрезмерного количества записей проблем.

В событиях Davis политики разрешений, основанные на разрешениях на уровне записи Grail, работают как ожидается, поскольку поля содержат единственные значения. Однако, когда несколько событий агрегируются в проблему, значения одного и того же поля объединяются в массив. Из-за текущей реализации фильтров разрешений на уровне записи Grail только `dt.security_context` поддерживает фильтрацию массивов значений. Другие поля разрешений не могут быть использованы с фильтрами на основе массивов в политиках разрешений.

Это поведение отличается от функциональности фильтрации DQL, где фильтры массивов на полях массивов полностью поддерживаются. Хотя это ограничение может повлиять на гибкость фильтров разрешений, важно учитывать при управлении политиками разрешений.

* Dynatrace не позволяет определять имена полей проблем, которые повторяют существующие имена полей событий [Семантического словаря](/docs/semantic-dictionary/model/davis#davis-ai-events "Узнайте о моделях Семантического словаря, связанных с Davis AI.").
* Вы можете определять поля проблем только для полей источника с значениями типа `string`. Поля, содержащие значения других типов, не поддерживаются.

#### Изменение пользовательских полей проблем

Чтобы просмотреть или изменить поля, автоматически распространяемые из событий в проблемы, перейдите в ![Настройки](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Настройки") **Настройки** >  **Dynatrace Intelligence** > **Анализ коренной причины** > **Поля проблем**. Изменяя эти поля проблем, вы можете:

* Подписаться на пользовательские поля записей, чтобы они автоматически распространялись из всех отдельных событий на любую обнаруженную проблему.
* Переименовать существующие поля проблем.
* Удалить поля проблем.

Переименование существующих полей проблем и удаление полей проблем изменяет текущие и будущие записи проблем Grail и может нарушить ваши запросы DQL.

Чтобы узнать больше о случаях использования пользовательских полей проблем, см. [Dynatrace Intelligence Проблемы использования случаев](/docs/dynatrace-intelligence/davis-problems-app/problems-app-custom-problem-field-examples "Изучите сценарии использования пользовательских полей проблем в Проблемах.").

### Создание руководства по устранению неполадок

![Проблемы приложения - новое](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Проблемы приложения - новое") **Проблемы** позволяет создавать руководства по устранению неполадок, используя ![Панели мониторинга](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Панели мониторинга") **Панели мониторинга** или ![Тетради](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Тетради") **Тетради**, чтобы документировать ваше расследование и шаги, предпринятые для решения проблемы. Руководство основано на предварительно определенной шаблоне и содержит два типа разделов:

* Разделы с информацией, извлеченной直接 из проблемы.
* Шаблонные разделы (такие как `Первоначальный ответ и обнаружение`, `Устранение неполадок` и `Шаги по устранению`) которые вы можете редактировать, чтобы описать процесс и шаги, предпринятые для решения проблемы.

Чтобы создать руководство по устранению неполадок

1. Перейдите в ![Проблемы приложения - новое](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Проблемы приложения - новое") **Проблемы** и откройте проблему, которую необходимо решить.
2. На странице деталей проблемы выберите **Устранение неполадок**.
3. Выберите  **Новое**.

   * Выберите  **Тетради**, чтобы создать новый документ в ![Тетради](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Тетради") **Тетради**.
   * Выберите  **Панели мониторинга**, чтобы создать новый документ в ![Панели мониторинга](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Панели мониторинга") **Панели мониторинга**.
4. Следуйте инструкциям в шаблоне, чтобы документировать детали для вашего руководства по устранению неполадок.

Если вы поделитесь руководством по устранению неполадок со всеми пользователями в вашей среде и включите предложения документов на основе векторной подобности, Dynatrace Intelligence генеративный ИИ проиндексирует ваш документ и предложит его вашей команде, чтобы помочь им быстрее устранить подобные проблемы. Чтобы узнать больше о предложениях документов Dynatrace Intelligence генеративного ИИ, см. [Найти релевантные документы с помощью Dynatrace Intelligence генеративного ИИ](/docs/dynatrace-intelligence/copilot/copilot-find-relevant-troubleshooting-guides "Узнайте, как Dynatrace Intelligence генеративный ИИ может предложить руководства по устранению неполадок для решения проблем.").

Возможность создавать и делиться руководствами по устранению неполадок позволяет командам DevOps:

* Делиться и распространять свои знания о конкретной бизнес-логике, реализации программного обеспечения и инфраструктуре.
* Обогащать Dynatrace AI в своей среде с общими знаниями для более упрощенного и адаптированного опыта во время расследования и решения проблем.
* Обогащать Dynatrace AI в своей среде.

### Решение случаев пропущенных событий

Dynatrace предлагает широкий спектр инструментов, подходящих для ваших потребностей, таких как настройка разрешений групп пользователей, правил оповещения Dynatrace Intelligence или правил ингестии OpenPipeline. Однако из-за богатых возможностей настройки могут возникнуть случаи, когда события не будут видны в ![Проблемы приложения - новое](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Проблемы приложения - новое") **Проблемы** и различия в количестве затронутых сущностей в доступных вкладках. Наиболее распространенные причины пропуска событий из ![Проблемы приложения - новое](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Проблемы приложения - новое") **Проблемы** являются:

* Разница в периоде хранения бакета: вы можете настроить период хранения бакета для мониторинговых данных, чтобы он длился дольше, так что события, связанные с проблемой, будут видны независимо от того, как долго проблема находится в открытом состоянии. Чтобы узнать больше о настройке периода хранения бакета для мониторинговых данных, см. [Сохранять данные трассировки в течение длительного периода](/docs/observe/application-observability/distributed-tracing/data-retention "Создайте и назначьте бакеты с пользовательским хранением данных для ваших данных трассировки в Grail.").
* Отсутствие необходимых разрешений для просмотра события: проверьте с группой поддержки Dynatrace и убедитесь, что у вас есть необходимые разрешения. Попросите администратора скорректировать разрешения, чтобы событие стало видимым для вас.
* Правила ингестии OpenPipeline, которые удаляют записи: вы можете скорректировать правила ингестии OpenPipeline, чтобы они не удаляли никаких записей или расширили правила, чтобы сохранить записи, которые могут быть связаны с оповещенной проблемой. Чтобы узнать больше о настройке правил ингестии OpenPipeline, см. [Обработка журналов с помощью OpenPipeline](/docs/analyze-explore-automate/logs/lma-log-processing/lma-openpipeline "Обрабатывайте журналы, используя Dynatrace OpenPipeline.").

### Упрощение решения проблем с помощью специфических для проблем опций просмотра

...



![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** provides drill-down options that are designed to guide you toward the most relevant actions for resolving detected problems and help you streamline problem resolution.

Drill-down options available to you are displayed within the problem details view and depend on the type of the affected entity (such as service, Kubernetes workload, host, or AWS availability zone).

Some of the available drill-down options are:

* Analyze failures: Perform a focused failure analysis to identify the root cause of failure rates, error patterns, or performance issues.
* View related logs: Investigate relevant log entries directly within ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**.
* View failed traces: Analyze failed traces in ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** to understand the root cause of failures.
* View `app`: Navigate to the associated app's details page. The exact name is specific to the affected entity (such as View service, View Kubernetes workload, or View host).

To access drill-down options

1. In **Dynatrace**, go to ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**.
2. Select the problem you want to investigate from the ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** overview. This opens a problem details page.
3. Optional On the left side of the problem details page, select the affected entity or infrastructure you want to investigate further. Usually, when you open the problem details page, the affected entity is pre-selected for you.
4. From the affected entity details on the right, select the preferred option for further investigation.

   * Select  > **View related logs** to continue the investigation without leaving ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**.
   * Select  > **View failed traces** to continue the investigation in the [![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**](/docs/observe/application-observability/distributed-tracing "Trace and analyze in real time highly distributed systems with Grail.").
   * Select  > **View** `app` to continue the investigation in one of the available Dynatrace apps.
   * Select  > **Open with** to see all available investigation options.

Drill-down options provide you with seamless navigation between ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** and other Dynatrace apps to ensure focus and continuity in problem resolution.

### Review problem overview

The **Overview** is a concise, executive summary of a detected problem.

To view a problem overview

1. Go to ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** and open the problem you need to resolve.
2. On the problem details page, select **Overview**.

   **Example**:

   ![Example problem details Overview tab](https://dt-cdn.net/images/problems-screenshot-with-overview-1920-6c68de3f34.png)

The **Overview** has four sections:

Section

Description

[Impact](#overview-impact)

Displays all impacted Smartscape entities (for example, services, processes, and hosts) along with brief issue details for each entity.

[Root cause](#overview-root-cause)

Focuses on the root cause of the issue, including detailed information about the affected deployment stack.

[Visual resolution path](#overview-visual-resolution-path)

Graphically illustrates the relationships between frontends, services, and backends involved in the issue.

[Automation and remediation](#overview-automation-and-remediation)

Lists all automation workflows triggered by the problem, such as notifications, remediations, and external integrations.

Customize the layout

You can move these sections around to personalize your view of the **Overview**.

1. In the header of the section you want to move, select  and drag the section.
2. Drop the section where you want it to appear in the layout.

These changes are saved per user. Your layout changes don't affect how others see the overview.

### Impact

The **Impact** section displays all impacted [Smartscape](/docs/analyze-explore-automate/smartscape-classic "Learn how Smartscape Classic visualizes all the entities and dependencies in your environment.") entities (for example, services, processes, and hosts) along with brief issue details for each entity.

The **Impact** section is categorized by:

* **Frontends**
* **Services**
* **Infrastructure**
* **Synthetic monitoring**
* **Environment**

### Root cause

The **Root cause** section focuses on the root cause of the issue, including detailed information about the affected deployment stack. This may include:

* The process and host where the root-cause service is running.
* The Kubernetes workload serving the impacted service.

To ensure consistency, the root-cause entity is also listed in the **Impact** table.

### Visual resolution path

The **Visual resolution path** section graphically illustrates the relationships between frontends, services, and backends involved in the issue.

* Each node represents a [Smartscape](/docs/analyze-explore-automate/smartscape-classic "Learn how Smartscape Classic visualizes all the entities and dependencies in your environment.") entity (frontend, service, or backend) where a health issue was detected.
* Gray nodes indicate related entities used in the analysis but not directly impacted.

This graph helps explain how Dynatrace AI identified the root-cause backend service.

To maximize your view of the graph, select  **Maximize**.

### Automation and remediation

The **Automation and remediation** section lists all automation workflows triggered by the problem. These workflows may include:

* Alert notifications sent to response teams.
* Remediation flows and runbooks for auto-remediation.
* External AI agent triggers, such as cloud platform SRE agents, to gather further insights or resolve issues within cloud vendor infrastructure.

The table provides key details for each workflow, including:

* The last trigger time (as workflows may run multiple times during problem updates).
* The execution state (for example, success or failure).

Workflow execution details are based on standard workflow execution events, which can also be queried using DQL in [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") and [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.").

**Note**:

* Only users with system event read permissions can view workflow executions. Without these permissions, the table is empty and a message indicates the missing access.
* Workflows not shared with your user are listed but shown in gray without direct links, indicating restricted access.

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

## Explore in Dynatrace Hub

Triage, investigate, and remediate incidences directly in ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**.](https://www.dynatrace.com/hub/detail/problems/)