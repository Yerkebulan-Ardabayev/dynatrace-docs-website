---
title: Анализ служб баз данных (новый дизайн)
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/database-services-classic/analyze-database-services-new
---

# Анализ служб баз данных (новый дизайн)

# Анализ служб баз данных (новый дизайн)

* Пояснение
* 5 минут на чтение
* Опубликовано 20 июня 2023 г.

Страница обзора базы данных была переработана.

* В этой документации описывается новый дизайн.
* Чтобы вернуться к классической странице базы данных, на странице обзора базы данных выбери **Ещё** (**…**) > **Вернуться к классической странице**, а затем обратись к [документации по классической странице базы данных](/managed/observe/infrastructure-observability/database-services-classic/analyze-database-services "Analyze your database services with Dynatrace (classic page).").

Все базы данных, обнаруженные Dynatrace в окружении, отображаются на странице **Databases**. Можно анализировать каждую базу данных и переходить к информации на уровне кода.

Как туда попасть:

1. Перейди в **Database Services**.
2. Выбери имя базы данных в списке, чтобы перейти на страницу обзора этой базы данных.

На каждой странице **Database** перечислена самая важная информация об этой базе данных.

![Database overview | Unified analysis](https://dt-cdn.net/images/database-ua-overview-3502-2a520ae771.png)

Database overview | Unified analysis

Все значимые метрики базы данных показаны на одной странице, разделённой на несколько логических секций. Другие панели страницы обзора базы данных показывают производительность базы данных и служат точками входа для более глубокого анализа.

## Панель уведомлений

Панель уведомлений базы данных даёт быстрый обзор состояния базы данных. Выбери элемент уведомления, чтобы увидеть подробную информацию.

### Properties and tags

Выбери **Properties and tags** на панели уведомлений, чтобы открыть панель **Properties and tags**, на которой отображаются метаданные выбранной базы данных:

* **Tags** содержит теги, применённые к базе данных в настоящий момент.  
  Выбери **Add Tag**, чтобы добавить тег к метаданным базы данных.
* **Properties** содержит различные свойства базы данных, такие как имя приложения, тип базы данных, технологии и management zone.

### Problems

* На панели уведомлений **Problems** показывает активные и закрытые проблемы, связанные с выбранной базой данных.
* Выбери **Problems** на панели уведомлений, чтобы открыть панель **Problems**, в которой перечислены проблемы.

  + Выбери проблему, чтобы увидеть подробности.
  + Выбери **Go to problems**, чтобы перейти на страницу [Problems](/managed/dynatrace-intelligence "Learn how Davis® AI detects performance anomalies, identifies root causes, and uses AI models for adaptive thresholds across your environment."), отфильтрованную по выбранной базе данных.

### SLOs

* На панели уведомлений **SLOs** показывает текущее количество [SLO](/managed/deliver/service-level-objectives-classic "Monitor and alert on service-level objectives with Dynatrace in Service-Level Objectives Classic."), связанных с выбранной базой данных.
* Выбери **SLOs** на панели уведомлений, чтобы открыть панель **Service-level objectives**, в которой перечислены SLO, прямо или косвенно связанные с базой данных.

#### Напрямую связанные SLO

* SLO напрямую связан с сервисом, если [entity selector](/managed/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") этого SLO соответствует следующим критериям:

  + Тип сущности установлен как `"DATABASE"`.
  + ID сущности установлен как ID базы данных.
* Чтобы видеть только SLO, напрямую связанные с базой данных, убедись, что опция **Show only directly connected SLOs** включена.

#### Косвенно связанные SLO

* SLO не связан с базой данных напрямую, если в [entity selector](/managed/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") SLO не указан ID сущности.

  Пример: если заданы общие значения, такие как `type("DATABASE"),tag("slo")`, запрос возвращает все SLO для всех баз данных, включая текущую базу данных.
* Чтобы видеть SLO, не связанные с базой данных напрямую, отключи **Show only directly connected SLOs**.

#### Опции

* Разверни **Details**, чтобы увидеть график соответствующих метрик SLO.
* В разделе **Actions** выбери

  + **View in Data Explorer**, чтобы [увидеть метрики SLO в Data Explorer](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo#explorer "Create, configure, and monitor service-level objectives with Dynatrace.").
  + **Pin to Dashboard**, чтобы [закрепить SLO на дашборде](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo#dash "Create, configure, and monitor service-level objectives with Dynatrace.").
  + **SLO definition**, чтобы изменить SLO в **Service-level objective definitions**.
  + **Clone**, чтобы [клонировать SLO](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo#clone "Create, configure, and monitor service-level objectives with Dynatrace.").
  + **Create alert**, чтобы [создать оповещение для SLO](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo#alerts "Create, configure, and monitor service-level objectives with Dynatrace.").

#### Нет SLO

Если SLO не найдены, можно

* Выбрать другой временной диапазон в правом верхнем углу.

  ![Timeframe selector: menu bar](https://dt-cdn.net/images/timeframe-selector-menu-bar-264-8193110c8c.png)

  Timeframe selector: menu bar
* Выбрать **Add SLO**, чтобы создать SLO в [мастере SLO](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo#wizard "Create, configure, and monitor service-level objectives with Dynatrace.").

### Database availability

Выбери **Database availability** на панели уведомлений, чтобы увидеть график, суммирующий обнаруженные проблемы доступности базы данных за выбранный период времени.

### Owners

Выбери **Owners** на панели уведомлений, чтобы открыть панель **Ownership**, в которой перечислены [владельцы](/managed/deliver/ownership "Map team ownership to monitored entities for better collaboration, task assignment, incident and vulnerability response, and service-level management.") выбранной базы данных.

* Выбери , чтобы узнать больше о текущем владении.
* Чтобы добавить тег владения, выбери **Add Ownership tag**.

## Производительность

### Database service overview

Секцию **Database service overview** можно настроить так, чтобы сфокусироваться на различных метриках производительности базы данных. Для каждой метрики можно выбрать **Ещё** (**…**) и

* Проанализировать метрику в Data Explorer.
* Создать событие метрики (metric event).
* Закрепить метрику на классическом дашборде. Подробности см. в разделе [Закрепление плиток на дашборде](/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Learn to pin tiles to your dashboards.").

### Topology

В секции **Topology** можно узнать

* Какие сервисы вызывают базу данных и какие сервисы вызываются базой данных.  
  Выбери **Related services**, чтобы понять связь сервисов. Разверни **Details**, чтобы увидеть график соответствующих метрик сервиса. Чтобы продолжить анализ, можно выбрать [**View backtrace**](/managed/observe/application-observability/services-classic/service-backtrace "Trace the sequence of service calls all the way back up to the browser click that triggered the sequence of calls.").
* Процессы и хосты, на которых работает сервис.  
  Разверни **Details**, чтобы увидеть график соответствующих метрик процесса. Выбери имя процесса, чтобы проанализировать его.

### Statement types

Содержит обзор типов операторов (statement types), найденных для базы данных за выбранный период времени.

* Разверни **Details**, чтобы увидеть график соответствующего оператора.
* Выбери имя типа оператора, чтобы проанализировать операторы базы данных, отфильтрованные по выбранному типу.
* Выбери **View all statements**, чтобы проанализировать все операторы для базы данных.

### Distributed traces

Секция **Distributed traces** содержит обзор самых последних трасс за выбранный период времени. Выбери **Full search**, чтобы перейти к [обзору distributed traces для базы данных](/managed/observe/application-observability/distributed-traces/analysis/get-started "Get started with distributed trace analysis in Dynatrace.").

### Events

Содержит список [событий](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Gain an understanding of the Events section on each host, process, and service overview page."), влияющих на базу данных в текущем периоде времени.

### Related logs

Содержит список [логов](/managed/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more."), связанных с базой данных в текущем периоде времени.

* Чтобы проанализировать все логи для связанной базы данных, выбери **Go to logs**.
* Чтобы проанализировать конкретный лог, разверни **Details**. Если для строки лога найдена трасса или сессия пользователя, к ней можно перейти прямо из этого представления.

## Похожие темы

* [Страницы унифицированного анализа](/managed/ingest-from/extend-dynatrace/extend-ui/unified-analysis "Extend the Dynatrace web UI using entity-tailored unified analysis pages.")