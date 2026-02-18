# Документация Dynatrace: analyze-explore-automate/workflows
Язык: Русский (RU)
Сгенерировано: 2026-02-18
Файлов в разделе: 1
---

## analyze-explore-automate/workflows.md

---
title: Workflows
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows
scraped: 2026-02-18T05:38:27.824812
---

# Workflows

# Workflows

* Последние Dynatrace
* Приложение
* 4-мин. чтение
* Обновлено 18 ноября 2024 г.

![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** — это мощный инструмент, позволяющий автоматически реагировать на данные мониторинга.

Workflows не предназначен для массового приема или экспорта данных. Для крупномасштабной обработки данных рассмотрите возможность использования [OpenPipeline](/docs/platform/openpipeline "Масштабируйте обработку данных платформы Dynatrace с помощью Dynatrace OpenPipeline.") или создание пользовательских решений с помощью [Dynatrace Extensions](/docs/ingest-from/extensions "Узнайте, как создавать и управлять Dynatrace Extensions.").

Дополнительную информацию можно найти в [кратком руководстве](/docs/analyze-explore-automate/workflows/quickstart "Создайте и запустите свой первый workflow.").

Предварительные условия

### Разрешения

В следующей таблице описаны необходимые разрешения.

Разрешение

Описание

hub:catalog:read

Доступ для чтения к Hub приложениям.

document:documents:read

Чтение документов для шаблонов workflows.

app-engine:apps:run

Включает перечисление всех приложений и чтение пакетов приложений.

app-engine:functions:run

Включает использование function-executor.

automation:calendars:read

Доступ для чтения к бизнес-календарям.

automation:calendars:write

Доступ для записи в бизнес-календари.

automation:rules:read

Доступ для чтения к правилам планирования.

automation:rules:write

Доступ для записи в правила планирования.

automation:workflows:admin

Административный доступ к workflows и их выполнениям.

automation:workflows:read

Доступ для чтения к workflows.

10

строк на страницу

Страница

1

из 1

Вам могут потребоваться дополнительные разрешения для выполнения определенных задач в ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**.

Для получения полного списка разрешений, необходимых для использования ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**, перейдите в **Hub**, найдите и выберите **Workflows** и перейдите на вкладку **Technical information** (Техническая информация).

Дополнительную информацию о безопасности ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** можно найти в разделе [Разрешения пользователей для workflows](/docs/analyze-explore-automate/workflows/security "Руководство по аспектам безопасности автоматизации workflows в Dynatrace Workflows").

## Установка

Убедитесь, что приложение [установлено в вашей среде](/docs/manage/hub#install "См. информацию о Dynatrace Hub.").

Основные понятия

Варианты использования

![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** — это ваша точка входа для управления и мониторинга workflows. Приложение взаимодействует со службой автоматизации через свой REST API. Служба автоматизации отвечает за обработку ваших workflows и отслеживание их выполнений.

### Workflow

Workflow определяет повторяющийся процесс путем сборки серии задач.

* Последовательность задач определяется их переходами, которые позволяют выполнять их последовательно, параллельно и с условными путями.
* Workflows можно редактировать и отслеживать в визуальном графе.

### Простой workflow

Простой workflow определяет повторяющийся процесс, состоящий только из одной задачи.

* Workflow с уменьшенной функциональностью, содержащий только одну задачу, ограниченное ведение журналов для выполнений, ограниченные параметры и условия задачи и запрет на использование задач JavaScript.
* Отсутствие дополнительных затрат на создание workflow, поскольку простые workflows не потребляют часы workflow.

### Задача

Каждый шаг в workflow называется задачей.

* Workflow отслеживает задачи и их порядок.
* Задача определяет единицу работы (например, `Create Incident` (Создать инцидент), `Notify Ops in Slack` (Уведомить Ops в Slack) или `Get error log count` (Получить количество записей об ошибках)), включая условия, поведение повторных попыток, тайм-ауты и, что наиболее важно, входную конфигурацию, необходимую для достижения работы и предоставления результата для использования последующими задачами.

### Действие

Действие — это универсальная, многократно используемая функция, которая настраивается и запускается задачами. Например, действие может быть `Create Jira Issue` (Создать задачу Jira), а задача будет выполнять действие с определенной конфигурацией для `Create Bug in Sample project` (Создать ошибку в примере проекта).

* Действия — это инструменты, которые собираются в ваши workflows для соответствия вашему индивидуальному процессу.
* Действия предоставляются из коробки Dynatrace и партнерами и могут быть установлены через Dynatrace Hub.

### Выполнение

Workflows, задачи и действия определяют, как должна выполняться работа. Выполнение представляет собой конкретный экземпляр прохождения этого процесса.

* Выполнение запускается либо по расписанию, либо по событиям, либо вручную через ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** или REST API.
* Каждое выполнение одного и того же workflow может быть разным в зависимости от его параметров, входных данных и контекста.
* Каждое выполнение workflow можно найти в виде отдельной записи в таблице **Executions** (Выполнения).

Чтобы просмотреть прошлые и текущие выполнения

Чтобы просмотреть все выполнения в вашей среде, выберите **Executions** (Выполнения) в заголовке приложения Workflows.

* Чтобы отфильтровать таблицу, можно указать комбинацию:

  + **Keyword** (Ключевое слово): строка поиска
  + **Workflow** (Workflow): имя workflow, отображаемое в пользовательском интерфейсе
  + **Execution state** (Состояние выполнения): `Success` (Успешно), `Running` (Выполняется), `Error` (Ошибка) или `Waiting` (Ожидание)
  + **Trigger type** (Тип триггера): `Manual` (Вручную), `Schedule` (Расписание) или `Event` (Событие)
  + **Timeframe** (Временной интервал): относительный временной интервал, например `Last 2 hours` (Последние 2 часа) или пользовательский временной интервал с выбираемыми настройками From (От) и To (До)
* Чтобы просмотреть выполнения определенного workflow, найдите workflow в таблице и выберите ![More actions](https://dt-cdn.net/images/dashboards-app-menu-kebab-c39eda426b.svg "More actions") > **View execution history** (Просмотреть историю выполнения) в столбце **Action** (Действие).

Чтобы просмотреть выполнения workflow, который вы редактируете, выберите **Executions** (Выполнения) в редакторе.

## EdgeConnect

EdgeConnect позволяет получить доступ к вашим непубличным службам в задачах workflow. HTTP-запросы, происходящие в любом типе действия или функции платформы, могут быть проксированы через EdgeConnect в целевую сеть.

Любой HTTP-запрос (из вашего пользовательского приложения, workflow или ad-hoc JavaScript-кода), соответствующий определенному шаблону хоста, обрабатывается экземпляром EdgeConnect, который вы указываете в конфигурации платформы. Дополнительную информацию можно найти в разделе [Configure and deploy EdgeConnect](/docs/ingest-from/edgeconnect "Используйте EdgeConnect для управления тем, как ваши приложения и workflows взаимодействуют с вашими внутренними системами.").

## Варианты использования

Workflows позволяет:

* Создавать **[agentic workflowsï»¿](http://https://www.dynatrace.com/hub/detail/agentic-workflows)**
* Автоматически реагировать на события Dynatrace Intelligence или проблемы безопасности.
* Планировать отчеты в соответствии с праздниками и рабочими часами.
* Организовывать ИТ-процессы во всей вашей ИТ-инфраструктуре.
* Подключаться как к облачным, так и к локально-ограниченным службам.
* Объединять готовые интеграции с пользовательским кодом.
* Визуализировать автоматизированные процессы в графическом интерфейсе workflow.
* Получать мониторинг в реальном времени и полный аудит всех выполнений автоматизации.
* Определять логику потока с помощью пользовательских условий, автоматических повторных попыток, циклов и параллельной обработки.

## Обучающие модули

Следующие обучающие модули показывают, как можно использовать ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** для автоматической реакции на данные мониторинга.

[01Workflows quick start guide

* How-to guide
* Build and run your first workflow.](/docs/analyze-explore-automate/workflows/quickstart)[02Create workflows in Dynatrace Workflows

* How-to guide
* Create and edit workflows in Dynatrace Workflows.](/docs/analyze-explore-automate/workflows/building)[03Create a simple workflow in Dynatrace Workflows

* How-to guide
* Build and run a simple workflow.](/docs/analyze-explore-automate/workflows/simple-workflow)[04Workflow triggers

* Overview
* Introduction to workflow automation triggers for workflows.](/docs/analyze-explore-automate/workflows/trigger)[05Run and monitor workflows created in Dynatrace Workflows

* How-to guide
* Run and monitor workflows created in Dynatrace Workflows.](/docs/analyze-explore-automate/workflows/running)[06User permissions for workflows

* Reference
* Guide on security aspects of workflow automation in Dynatrace Workflows](/docs/analyze-explore-automate/workflows/security)[07Workflows actions

* Overview
* Use Dynatrace ready-made actions for your workflows.](/docs/analyze-explore-automate/workflows/default-workflow-actions)[08Workflows Connectors

* Overview
* Use Dynatrace ready-made actions for your workflows and integrate Dynatrace with third-party systems.](/docs/analyze-explore-automate/workflows/actions)[09Manage workflows

* Overview
* Manage your workflows](/docs/analyze-explore-automate/workflows/manage-workflows)[10Expression reference

* Reference
* Get to know the workflows expression](/docs/analyze-explore-automate/workflows/reference)[11Workflows use cases

* Overview
* Explore common Workflows use cases in Dynatrace deployments.](/docs/analyze-explore-automate/workflows/use-cases)

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Automate tasks in your IT landscape, remediate problems, and visualize processes.](https://www.dynatrace.com/hub/detail/automations?internal_source=doc&internal_medium=link&internal_campaign=cross)

---
