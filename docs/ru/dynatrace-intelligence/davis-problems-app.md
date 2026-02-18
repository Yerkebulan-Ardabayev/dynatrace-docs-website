---
title: Приложение для проблем
source: https://www.dynatrace.com/docs/dynatrace-intelligence/davis-problems-app
scraped: 2026-02-18T05:31:15.356692
---

# Приложение для проблем

# Приложение для проблем

* Последнее Dynatrace
* Приложение
* 15-минутное чтение
* Обновлено 28 января 2026 г.

Быстрое выявление, расследование и устранение входящих инцидентов является основной задачей для операционных команд. ![Приложение для проблем - новое](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Приложение для проблем - новое") **Проблемы** поддерживают их, автоматически анализируя сложные инциденты, собирая все контекст и представляя коренную причину и влияние в рамках единого представления.

![Приложение для проблем - новое](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Приложение для проблем - новое") **Проблемы**, основанные на данных из Grail и Dynatrace анализа интеллекта, помогают операционным и командам по обеспечению надежности сайта уменьшить среднее время ремонта (MTTR) путем представления всех аспектов инцидента.

Предварительные условия

### Права доступа

Следующая таблица описывает необходимые права доступа.

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

Запись документов в рабочий процесс Doc

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

Случаи использования

## Цель и контекст

Эта страница показывает вам, как использовать ![Приложение для проблем - новое](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Приложение для проблем - новое") **Проблемы** для выявления обнаруженных проблем и расследования их коренной причины и влияния.

## Целевая аудитория

Эта страница написана для:

* Операционных инженеров
* Инженеров по конвейерам
* Системных инженеров
* Инженеров по обеспечению надежности сайта (SRE)
* Инженеров по автоматизации сборки

## Сводка

**Проблемы** ![Приложение для проблем - новое](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Приложение для проблем - новое") упрощают выявление, анализ и устранение активных инцидентов, уменьшая MTTR. Это позволяет вам сосредоточиться на проблемах, обнаруженных с помощью ИИ, и быстро ориентироваться в их коренной причине.

* Данные, предоставленные Grail и DQL, позволяют разрезать и измельчить всю информацию, связанную с проблемами и событиями, для огромного количества проблем и событий.
* Интеграция с контекстными приложениями Dynatrace позволяет анализировать проблемы без необходимости переключать контекст.

## Расследование и устранение активных проблем

### Установка фокуса и выявление

По умолчанию, ![Приложение для проблем - новое](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Приложение для проблем - новое") **Проблемы** показывают:

* Ленту всех проблем за последние 2 часа. Чтобы помочь операционным командам обнаружить открытые проблемы, независимо от установленного фильтра, открытые проблемы остаются вверху ленты, независимо от того, как долго они открыты.
* Диаграмму проблем вверху, визуализирующую любую аномалию с большим количеством проблем в прошлом. Выберите пик на диаграмме, чтобы углубиться в него и провести дальнейшее расследование.

![Представление ленты проблем в приложении для проблем](https://dt-cdn.net/images/problem-table-1920-1ff1983035.webp)

#### Фильтрация

Чтобы сосредоточиться на вашем домене и выявить проблемы, которые на него влияют, установите фильтры. Два наиболее распространенных фильтра - **Статус** и **Категория** - имеют настраиваемые параметры слева от таблицы для быстрого доступа. Чтобы установить другие фильтры, используйте панель фильтров над таблицей.

* **Статус** - может быть `Активно` или `Закрыто`.

  + Если это не установлено, перечислены все проблемы (активные или закрытые).
  + Если вы выбираете статус в контроле слева, соответствующий фильтр также отображается в панели фильтров.
* **Категория** - указывает на характер инцидента, такой как замедления, ошибки, проблемы, связанные с ресурсами, или инциденты доступности.

  + Если вы выбираете одну или несколько категорий в контроле слева, соответствующие фильтры также отображаются в панели фильтров.

Фильтрация с помощью панели фильтров позволяет сосредоточить ленту на проблемах на основе нескольких критериев, таких как статус, количество затронутых сущностей, сущность коренной причины и т. д. Поместите курсор в поле ввода, чтобы увидеть все доступные варианты. По умолчанию критерии фильтрации объединяются логикой **И**. Для каждого критерия Dynatrace Intelligence предоставляет список предложенных значений, основанных на вашей ленте проблем.

Например, чтобы увидеть проблемы, которые были вызваны увеличением ошибок JavaScript и которые сохраняются более 1 часа, используйте следующие критерии фильтрации:

* `Статус=АКТИВНО`
* `Продолжительность>1ч`
* `Категория=Ошибка`
* `Имя=Увеличение скорости ошибок JavaScript`

Панель фильтров проблем поддерживает логические фильтры с использованием булевой логики. Это позволяет объединять критерии **И** и **ИЛИ** и создавать сложные фильтры с помощью скобок для группировки булевых термов. Вы можете увидеть заявление логического фильтра с использованием булевой логики в приложении **Проблемы** в примере ниже.

![Мощные булевы фильтры в панели фильтров проблем.](https://dt-cdn.net/images/complex-problem-filters-1920-db9346a85b.png)

#### Использование предопределенных сегментов команд для повышения операционной производительности

Сегменты - это предопределенные фильтры, используемые для быстрой фильтрации данных, чтобы включить только соответствующие записи. В контексте приложения **Проблемы** вы или ваша команда можете использовать предопределенный набор командных сегментов для фильтрации таблиц проблем вместо создания собственных фильтров проблем.

Следующий пример показывает, как использовать сегменты для фильтрации проблем, связанных с easyTravel.

![Фильтрация по сегментам в приложении для проблем.](https://dt-cdn.net/images/problems-filter-by-segments-1920-c5610b610e.png)

Кроме того, использование сегментов в приложении **Проблемы** позволяет:

* Создавать наборы фильтров, которые можно повторно использовать вами и делиться с всей командой.
* Экономить время на повторном создании фильтров, примененных во время предыдущих сессий.
* Повышать производительность, быстро фильтруя соответствующие проблемы.
* Быстро проверять статус вашей службы, создавая и применяя служебные сегменты.

Поскольку проблемы хранятся как события в Grail, сегменты, созданные для фильтрации проблем, должны определять фильтр событий. Например, если вы хотите фильтровать проблемы, которые были вызваны в определенном облачном регионе, вы можете создать сегмент с следующим фильтром событий:

```
cloud.region = "us-east-1c" AND event.kind = "DAVIS_PROBLEM"
```

Пример определения сегмента для фильтрации проблем

![Пример определения сегмента для фильтрации проблем в приложении для проблем.](https://dt-cdn.net/images/problems-segment-definition-1512-4649153a97.png)

Фильтры сегментов применяются напрямую к записям проблем Grail. Следовательно, фильтры сущностей не применяются к проблеме, если идентификатор сущности не выбран в качестве основного поля фильтруемой проблемы.

Для получения более подробной информации о сегментах и их работе смотрите [Сегменты](/docs/manage/segments "Сегменты логически структурируют данные мониторинга в Grail и функционируют как удобные фильтры для данных, к которым пользователи имеют доступ на основе разрешений.") ![Сегменты](https://dt-cdn.net/images/segments-256-8e66310720.webp "Сегменты").

### Активация автоперезагрузки

Чтобы всегда обнаруживать входящие проблемы, используйте настройки перезагрузки ![Перезагрузка](https://dt-cdn.net/images/dashboards-app-refresh-33a794c2f1.svg "Перезагрузка") ![Расширить меню](https://dt-cdn.net/images/dashboards-app-menu-expand-3398af0cdf.svg "Расширить меню") в правом верхнем углу приложения **Проблемы**.

* Чтобы автоматически перезагружать ленту проблем, выберите ![Расширить меню](https://dt-cdn.net/images/dashboards-app-menu-expand-3398af0cdf.svg "Расширить меню") и выберите скорость перезагрузки (или выберите `Выключить`, чтобы отключить автоматическую перезагрузку)
* Чтобы вручную перезагрузить ленту проблем в любое время, независимо от настройки автоматической перезагрузки, выберите ![Перезагрузка](https://dt-cdn.net/images/dashboards-app-refresh-33a794c2f1.svg "Перезагрузка")

### Расследование и сравнение проблем

Чтобы увидеть подробности проблемы

1. В таблице выберите идентификатор проблемы в столбце **ID**.
2. Просмотрите страницу подробностей.

Страница подробностей проблемы предоставляет все доступные подробности о проблеме, выделяя сущность коренной причины красной меткой, чтобы направить ваше внимание на правильные вещи. Пример ниже показывает подробности проблемы с деградацией пользовательского действия — включая сущность коренной причины (`easyTravelBusiness` сервис) и график аномального времени ответа этого сервиса.

![Пример представления подробностей проблемы в приложении Problems.](https://dt-cdn.net/images/problems-details-view-page-1920-3d5f2bb781.png)

Все сущности, затронутые проблемой, перечислены в разделе **Затронутые сущности**, вместе с информацией о типе сущности и количестве событий, обнаруженных во время анализа.

* Как предложение для начала расследования, Dynatrace Intelligence отмечает сущность, которую он определил как коренную причину проблемы.
* Чтобы просмотреть подробности о затронутой сущности, выберите ее в таблице.

#### Сравните несколько проблем

Если все фильтры применены и у вас все еще есть несколько проблем для расследования, вы можете выбрать и сравнить подробности нескольких проблем.

1. В таблице используйте флажки для выбора двух или более проблем.
2. Выберите **Показать подробности**.

   Это предварительно загружает подробности всех выбранных проблем и добавляет элементы управления в правом верхнем углу страницы подробностей проблемы, чтобы вы могли быстро переключаться между каждой выбранной проблемой.

### Читайте свойства событий для дополнительной информации

Dynatrace получает события из нескольких источников событий, таких как OneAgent, Synthetic, расширения и приемники API. Dynatrace принимает и понимает различные свойства (также называемые полями) этих событий, которые предоставляют дополнительную информацию о событии.

Источники событий можно настроить для предоставления информации, необходимой для анализа и устранения проблем, вызванных событиями. Например, связывание конфигурации, которая обнаружила событие (`dt.settings.schema_id` и `dt.settings.object_id`), помогает быстро адаптировать порог или базовую линию, если такое действие необходимо.

Другим примером является настройка чувствительности пользовательского оповещения, которое вызвало событие, путем изменения конфигурации детектора в настройках.

Поскольку доступные свойства событий зависят от источника события, события, которые не генерируются пользовательскими оповещениями, не содержат ссылок на соответствующие настройки событий. Если вы хотите, чтобы событие ссылалось на объект настроек, вы можете сделать это, присвоив свойство `dt.settings.object_id` событиям, принимаемым через API и/или расширения.

![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** отображает все свойства событий для каждого собранного события в таблице и предоставляет ссылки на намерения, такие как прямая навигация к конфигурации пользовательского оповещения, как показано ниже.

![Problems app предлагает прямую ссылку на объект настроек.](https://dt-cdn.net/images/problems-app-settings-direct-link-1920-b7ded7d7d3.png)

Примеры мощных свойств событий включают:

* Описание события (`event.description`). Описание события поддерживает текст, отформатированный с помощью Markdown, что позволяет вам включать ссылки на ресурсы, которые могут помочь в устранении проблемы.
* DQL запрос (`dt.query`) позволяет вам перестроить график события в блокноте или на панели управления или скопировать сырое значение свойства.
* Связанные сущности (`dt.entity.*`) позволяют вам напрямую переходить к сущностям через свойства `dt.entity.*`.
* Ссылка на объект настроек (`dt.settings.object_id`) и схему настроек (`dt.settings.schema_id`).

Чтобы узнать больше о семантике и синтаксисе свойств событий и о том, как они могут быть использованы в Dynatrace, см. [Семантический словарь](/docs/semantic-dictionary/fields "Узнайте список глобальных полей, которые имеют хорошо определенное семантическое значение в Dynatrace и могут быть использованы в разных типах мониторинга.").

### Анализируйте проблемы с помощью своих собственных инструментов, экспортируя CSV

Для случаев, когда ваши программные инструменты создают разрывы интеграции, препятствующие эффективному использованию данных Dynatrace, мы предоставляем возможность экспортировать данные о проблемах в формате CSV. Вы можете использовать эти данные в различных инструментах, включая программы для работы с электронными таблицами, базы данных и инструменты анализа данных.

Как показано ниже, вы можете экспортировать связанные с проблемой данные из таблицы ленты проблем. Вы также можете экспортировать их из **Блокнотов** и **Панелей управления** во всех визуализациях таблиц.

![Экспорт выбранных проблем в виде файла CSV.](https://dt-cdn.net/images/problems-app-csv-export-1920-c5d456c07a.png)

Вы можете экспортировать все загруженные проблемы (до предела в 1000) или использовать функцию многократного выбора для выбора конкретных проблем. Кроме того, панель фильтров над таблицей позволяет фильтровать более крупные подмножества проблем. Флажок **Выбрать все** помогает экспортировать все проблемы в фильтрованном наборе записей.

### Проверьте коренную причину, не покидая контекста

В зависимости от ответственности вашей команды, вы можете сосредоточить внимание на Kubernetes кластерах, облачных ресурсах и рабочих нагрузках критически важных сервисов. Чтобы минимизировать переключение контекста, Dynatrace предлагает последовательную информацию о коренной причине в нескольких приложениях. Независимо от того, где начинается ваше расследование, вам не нужно переключаться на ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**, чтобы увидеть коренную причину.

В примере ниже приложение **Kubernetes** отображает информацию о проблеме, влияющей на рабочую нагрузку.

![Информация о проблеме, интегрированная в приложение Kubernetes.](https://dt-cdn.net/images/dynatrace-intelligence-in-k8s-app-1920-2da55950a8.png)

### Расследуйте все актуальные для проблемы журналы

Проблема, проанализированная Davis, подчеркивает коренную причину инцидента и показывает все актуальные для инцидента строки журнала в нескольких сущностях на странице подробностей проблемы.

Чтобы получить доступ к строкам журнала, собранным во время инцидента, выберите вкладку **Журналы**. Кроме того, вы можете увидеть их уровень журнала во всех сущностях, затронутых проблемой, что позволяет сэкономить время на ручных расследованиях и фильтрации журналов актуальных сущностей отдельно.

Вкладка **Журналы** также включает ссылки на затронутые сущности и информацию о всех связанных сущностях, таких как родительские хосты. Чтобы подтвердить, какие сущности затронуты событием проблемы, вы можете обратиться ко всем свойствам событий, начинающимся с префикса `dt.entity.`.

Смотрите, как вкладка **Журналы** суммирует все актуальные для проблемы журналы на изображении ниже.

![Dynatrace Intelligence Problems app log count.](https://dt-cdn.net/images/problems-log-count-1920-330dd46337.png)

Изображение ниже иллюстрирует дальнейшую сортировку строк журнала с помощью DQL запроса.

![Dynatrace Intelligence Problems app error log lines.](https://dt-cdn.net/images/problems-error-log-lines-1920-cb4599df02.png)

### Визуально уведомляйте и автоматизируйте, чтобы ускорить устранение

![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** имеет глобальный индикатор проблемы, который показывает количество активных проблем в окружении и всегда виден в Dock. Когда Dock свернут, красная точка отображается рядом с иконкой приложения вместо номера.

Чтобы персонализировать индикатор и количество отображаемых активных проблем, выберите фильтры в **Категории** и сохраните конфигурацию фильтра, выбрав иконку. Сохраненный фильтр будет автоматически применен к глобальному индикатору проблемы, уменьшая количество проблем, учитываемых для пользователя, как показано ниже. Выбор кнопки **Фильтр по умолчанию** восстанавливает последнюю сохраненную конфигурацию.

![Сохранение конфигурации фильтра в Problems app.](https://dt-cdn.net/images/problems-app-notifications-config-save-1920-af4147c3c1.png)

Пока фильтр проблемы активен, номер индикатора будет показывать только активные проблемы из выбранных категорий. Индикатор обновляется по расписанию каждую минуту, что означает, что после обновления фильтра может потребоваться некоторое время, чтобы индикатор адаптировался.

Вы также можете настроить уведомления по электронной почте для отфильтрованных проблем, используя свой адрес электронной почты, выбрав иконку, как показано ниже:

![Включение уведомлений по электронной почте для примененных фильтров в Problems app.](https://dt-cdn.net/images/problems-app-turn-on-notifications-1920-6806895778.png)

Уведомление по электронной почте является вашей личной настройкой, поэтому вы можете включить его без необходимости конфигурационных разрешений или риска влияния на других пользователей в одном и том же окружении.

Уведомление по электронной почте запускается напрямую в OpenPipeline, что означает, что могут быть применены только простые фильтры. Рабочие процессы, которые запрашивают ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** через DQL, могут использовать полный набор функций Grail запросов, таких как объединение таблиц.

Если вам нужно отправлять настраиваемые сообщения по электронной почте или иметь более сложные потребности в автоматизации и интеграции, вы должны применить полный рабочий процесс вместе с триггером проблемы.

### Визуализируйте затронутые развертывания, чтобы получить дополнительные сведения

(Этот раздел не был предоставлен в исходном тексте)



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