---
title: Analyze database services (new page)
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/databases/database-services-classic/analyze-database-services-new
scraped: 2026-03-05T21:31:30.344039
---

# Анализ сервисов баз данных (новая страница)

# Анализ сервисов баз данных (новая страница)

* Classic
* Explanation
* 5-min read
* Published Jun 20, 2023

Мы обновили дизайн страницы обзора базы данных.

* Эта документация описывает новый дизайн.
* Если вы хотите вернуться к классической странице базы данных, на странице обзора базы данных выберите **More** (**...**) > **Return to classic page**, а затем обратитесь к [документации по классической странице базы данных](analyze-database-services.md "Analyze your database services with Dynatrace (classic page).").

Все базы данных, обнаруженные Dynatrace в вашей среде, отображаются на странице **Databases**. Вы можете анализировать каждую базу данных и углубляться до информации на уровне кода.

Как перейти:

1. Перейдите в ![Databases Services Classic](https://dt-cdn.net/images/databases-512-6aa6fff194.png "Databases Services Classic") **Database Services Classic**.
2. Выберите имя базы данных в списке, чтобы перейти на страницу обзора этой базы данных.

На каждой странице **Database** отображается наиболее важная информация для данной базы данных.

![Database overview | Unified analysis](https://dt-cdn.net/images/database-ua-overview-3502-2a520ae771.png)

Все соответствующие метрики базы данных отображаются на одной странице, разделённой на несколько логических секций. Другие панели страницы обзора базы данных показывают производительность базы данных и служат точками входа для более глубокого анализа.

## Панель уведомлений

Панель уведомлений базы данных даёт вам быстрый обзор состояния базы данных. Выберите элемент уведомления для отображения дополнительной информации.

### Свойства и теги

Выберите **Properties and tags** на панели уведомлений для отображения панели **Properties and tags**, которая содержит метаданные о выбранной базе данных:

* **Tags** — список тегов, применённых к базе данных.
  Выберите **Add Tag**, чтобы добавить тег к метаданным базы данных.
* **Properties** — список различных свойств базы данных, таких как имя приложения, тип базы данных, технологии и зоны управления.

### Проблемы

* На панели уведомлений **Problems** указывает на активные и закрытые проблемы, связанные с выбранной базой данных.
* Выберите **Problems** на панели уведомлений для отображения панели **Problems**, в которой перечислены проблемы.

  + Выберите проблему для отображения подробностей.
  + Выберите **Go to problems**, чтобы перейти на страницу [Problems](../../../../dynatrace-intelligence.md "Get familiar with the capabilities of Dynatrace Intelligence."), отфильтрованную по выбранной базе данных.

### SLO

* На панели уведомлений **SLOs** показывает текущее количество [SLO](../../../../deliver/service-level-objectives-classic.md "Monitor and alert on service-level objectives with Dynatrace in Service-Level Objectives Classic."), связанных с выбранной базой данных.
* Выберите **SLOs** на панели уведомлений для отображения панели **Service-level objectives**, которая содержит SLO, прямо или косвенно связанные с базой данных.

#### Прямо связанные SLO

* SLO считается прямо связанным с сервисом, когда [селектор сущности](../../../../dynatrace-api/environment-api/entity-v2/entity-selector.md "Configure the entity selector for Environment API endpoints.") SLO соответствует следующим критериям:

  + Тип сущности установлен как `"DATABASE"`.
  + ID сущности установлен как ID базы данных.
* Чтобы видеть только SLO, прямо связанные с базой данных, убедитесь, что **Show only directly connected SLOs** включён.

#### Косвенно связанные SLO

* SLO не является прямо связанным с базой данных, когда в [селекторе сущности](../../../../dynatrace-api/environment-api/entity-v2/entity-selector.md "Configure the entity selector for Environment API endpoints.") SLO не указан ID сущности.

  Пример: когда указаны общие значения, такие как `type("DATABASE"),tag("slo")`, запрос возвращает все SLO для всех баз данных, включая текущую.
* Чтобы увидеть SLO, не связанные напрямую с базой данных, отключите **Show only directly connected SLOs**.

#### Параметры

* Разверните **Details**, чтобы просмотреть график соответствующих метрик SLO.
* В разделе **Actions** выберите:

  + **View in Data Explorer**, чтобы [просмотреть метрики SLO в Data Explorer](../../../../deliver/service-level-objectives-classic/configure-and-monitor-slo.md#explorer "Create, configure, and monitor service-level objectives with Dynatrace.").
  + **Pin to Dashboard**, чтобы [закрепить SLO на вашем дашборде](../../../../deliver/service-level-objectives-classic/configure-and-monitor-slo.md#dash "Create, configure, and monitor service-level objectives with Dynatrace.").
  + **SLO definition**, чтобы отредактировать SLO в **Service-level objective definitions**.
  + **Clone**, чтобы [клонировать SLO](../../../../deliver/service-level-objectives-classic/configure-and-monitor-slo.md#clone "Create, configure, and monitor service-level objectives with Dynatrace.").
  + **Create alert**, чтобы [создать оповещение для SLO](../../../../deliver/service-level-objectives-classic/configure-and-monitor-slo.md#alerts "Create, configure, and monitor service-level objectives with Dynatrace.").

#### Нет SLO

Если SLO не найдены, вы можете:

* Выбрать другой временной диапазон в правом верхнем углу.

  ![Timeframe selector: menu bar](https://dt-cdn.net/images/timeframe-selector-menu-bar-264-8193110c8c.png)
* Выбрать **Add SLO**, чтобы создать SLO в [мастере SLO](../../../../deliver/service-level-objectives-classic/configure-and-monitor-slo.md#wizard "Create, configure, and monitor service-level objectives with Dynatrace.").

### Доступность базы данных

Выберите **Database availability** на панели уведомлений для отображения графика, обобщающего обнаруженные проблемы доступности базы данных за выбранный период.

### Владельцы

Выберите **Owners** на панели уведомлений для отображения панели **Ownership**, в которой перечислены [владельцы](../../../../deliver/ownership.md "Map team ownership to monitored entities for better collaboration, task assignment, incident and vulnerability response, and service-level management.") выбранной базы данных.

* Выберите для получения дополнительной информации о текущем владении.
* Чтобы добавить тег владельца, выберите **Add Ownership tag**.

## Производительность

### Обзор сервиса базы данных

Вы можете настроить секцию **Database service overview** для фокусировки на различных метриках производительности базы данных. Для каждой метрики вы можете выбрать **More** (**...**) и:

* Проанализировать метрику в Data Explorer.
* Создать событие метрики.
* Закрепить метрику на классическом дашборде. Подробнее см. [Pin tiles to your dashboard](../../../../analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard.md "Learn to pin tiles to your dashboards.").

### Топология

В секции **Topology** вы можете узнать:

* Какие сервисы вызывают базу данных и какие сервисы вызываются базой данных.
  Выберите **Related services**, чтобы понять взаимосвязи сервисов. Разверните **Details** для просмотра графика соответствующих метрик сервиса. Для продолжения анализа вы можете выбрать [**View backtrace**](../../../application-observability/services-classic/service-backtrace.md "Trace the sequence of service calls all the way back up to the browser click that triggered the sequence of calls.").
* Процессы и хосты, на которых работает сервис.
  Разверните **Details** для просмотра графика соответствующих метрик процесса. Выберите имя процесса для его анализа.

### Типы операторов

Содержит обзор типов операторов, найденных для базы данных в выбранном временном диапазоне.

* Разверните **Details** для просмотра графика соответствующего оператора.
* Выберите имя типа оператора для анализа операторов базы данных, отфильтрованных по выбранному типу.
* Выберите **View all statements** для анализа всех операторов базы данных.

### Распределённые трассировки

Секция **Distributed traces** предоставляет обзор последних трассировок за выбранный временной диапазон. Выберите **Full search**, чтобы перейти к [обзору распределённых трассировок для базы данных](../../../application-observability/distributed-traces/analysis/get-started.md "Get started with distributed trace analysis in Dynatrace.").

### События

Список [событий](../../../../dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation.md "Gain an understanding of the Events section on each host, process, and service overview page."), влияющих на базу данных в текущем временном диапазоне.

### Связанные логи

Список [логов](../../../../analyze-explore-automate/logs.md "Log Management and Analytics provides a unified approach to controlling and studying your log data in Dynatrace."), связанных с базой данных в текущем временном диапазоне.

* Для анализа всех логов связанной базы данных выберите **Go to logs**.
* Для анализа конкретного лога разверните **Details**. Если для строки лога найдена трассировка или сеанс пользователя, вы можете перейти к ним непосредственно из этого представления.

## Связанные темы

* [Unified analysis pages](../../../../ingest-from/extend-dynatrace/extend-ui/unified-analysis.md "Extend the Dynatrace web UI using entity-tailored unified analysis pages.")
