---
title: Workflows
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows
scraped: 2026-03-06T21:15:26.954952
---

# Workflows

# Workflows

* Последняя версия Dynatrace
* Приложение
* Чтение: 4 мин
* Обновлено 18 ноября 2024 г.

![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** -- это мощный инструмент, позволяющий автоматически реагировать на данные мониторинга.

Workflow не предназначен для массового приёма или массового экспорта данных. Для крупномасштабной обработки данных рассмотрите использование [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.") или создание собственных решений с помощью [Dynatrace Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.").

Для получения дополнительной информации см. [пример быстрого старта](/docs/analyze-explore-automate/workflows/quickstart "Build and run your first workflow.").

Предварительные требования

### Разрешения

В следующей таблице описаны необходимые разрешения.

hub:catalog:read

Доступ на чтение к приложениям Hub.

document:documents:read

Чтение документов для шаблонов workflow.

app-engine:apps:run

Позволяет просматривать список всех приложений и читать пакеты приложений.

app-engine:functions:run

Позволяет использовать function-executor.

automation:calendars:read

Доступ на чтение к бизнес-календарям.

automation:calendars:write

Доступ на запись к бизнес-календарям.

automation:rules:read

Доступ на чтение к правилам планирования.

automation:rules:write

Доступ на запись к правилам планирования.

automation:workflows:admin

Административный доступ к workflow и выполнениям.

automation:workflows:read

Доступ на чтение к workflow.

Для выполнения определённых задач в ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** могут потребоваться дополнительные разрешения.

Полный список разрешений, необходимых для использования ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**, можно найти в разделе **Hub**: найдите и выберите **Workflows**, затем перейдите на вкладку **Technical information**.

Для получения дополнительной информации о безопасности ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** см. [Пользовательские разрешения для workflow](/docs/analyze-explore-automate/workflows/security "Guide on security aspects of workflow automation in Dynatrace Workflows").

### Установка

Убедитесь, что приложение [установлено в вашей среде](/docs/manage/hub#install "See the information about Dynatrace Hub.").

Концепции

Сценарии использования

![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** -- это ваша точка входа для управления и мониторинга workflow. Приложение взаимодействует с сервисом автоматизации через его REST API. Сервис автоматизации отвечает за обработку ваших workflow и отслеживание выполнений.

### Workflow

Workflow определяет повторяемый процесс путём сборки последовательности задач.

* Последовательность задач определяется их переходами, которые позволяют выполнение последовательно, параллельно и с условными путями.
* Workflow можно редактировать и отслеживать в визуальном графе.

### Простой workflow

Простой workflow определяет повторяемый процесс только с одной задачей.

* Workflow с ограниченной функциональностью: только одна задача, ограниченное логирование выполнений, ограниченные параметры и условия задач, задачи на JavaScript не допускаются.
* Создание workflow не требует дополнительных затрат, так как простые workflow не потребляют часы workflow.

### Задача

Каждый шаг в workflow называется задачей.

* Workflow отслеживает задачи и их порядок.
* Задача определяет единицу работы (например, `Create Incident`, `Notify Ops in Slack` или `Get error log count`), включая условия, поведение при повторных попытках, тайм-ауты и, что наиболее важно, входную конфигурацию, необходимую для выполнения работы и предоставления результата для последующих задач.

### Действие

Действие -- это универсальная, повторно используемая функция, настраиваемая и запускаемая задачами. Например, действием может быть `Create Jira Issue`, а задача выполнит это действие с определённой конфигурацией для `Create Bug in Sample project`.

* Действия -- это инструменты, которые собираются в ваших workflow для соответствия вашему пользовательскому процессу.
* Действия предоставляются Dynatrace и партнёрами «из коробки» и могут быть установлены через Dynatrace Hub.

### Выполнение

Workflow, задачи и действия определяют, как должна выполняться работа. Выполнение представляет собой конкретный экземпляр прохождения этого процесса.

* Выполнение запускается либо по расписанию, либо по событиям, либо вручную через ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** или REST API.
* Каждое выполнение одного и того же workflow может отличаться в зависимости от его параметров, входных данных и контекста.
* Каждый запуск workflow можно найти как отдельную запись в таблице **Executions**.

Просмотр прошлых и текущих выполнений

Чтобы просмотреть все выполнения в вашей среде, выберите **Executions** в заголовке приложения Workflows.

* Для фильтрации таблицы можно указать комбинацию из:

  + **Keyword**: строка поиска
  + **Workflow**: имя workflow, отображаемое в интерфейсе
  + **Execution state**: `Success`, `Running`, `Error` или `Waiting`
  + **Trigger type**: `Manual`, `Schedule` или `Event`
  + **Timeframe**: относительный временной интервал, например `Last 2 hours`, или пользовательский интервал с настраиваемыми параметрами «От» и «До»
* Чтобы просмотреть выполнения определённого workflow, найдите workflow в таблице и выберите ![More actions](https://dt-cdn.net/images/dashboards-app-menu-kebab-c39eda426b.svg "More actions") > **View execution history** в столбце **Action**.

Чтобы просмотреть выполнения редактируемого workflow, выберите **Executions** в редакторе.

## EdgeConnect

EdgeConnect позволяет обращаться к непубличным сервисам в задачах workflow. HTTP-запросы, выполняемые в любом типе действия или функции платформы, могут проксироваться через EdgeConnect в целевую сеть.

Любой HTTP-запрос (из вашего пользовательского приложения, workflow или произвольного кода на JavaScript), соответствующий заданному шаблону хоста, обрабатывается экземпляром EdgeConnect, указанным в конфигурации платформы. Для получения дополнительной информации см. [Настройка и развёртывание EdgeConnect](/docs/ingest-from/edgeconnect "Use EdgeConnect to control how your apps and workflows interact with your internal systems.").

## Сценарии использования

Workflows позволяет:

* Создавать **[агентные workflow](http://https://www.dynatrace.com/hub/detail/agentic-workflows)**
* Автоматически реагировать на события Dynatrace Intelligence или проблемы безопасности.
* Планировать отчёты с учётом праздников и рабочих часов.
* Оркестрировать ИТ-процессы по всему вашему ИТ-ландшафту.
* Подключаться как к облачным, так и к локально защищённым сервисам.
* Комбинировать готовые интеграции с пользовательским кодом.
* Визуализировать автоматизированные процессы в графическом интерфейсе workflow.
* Получать мониторинг в реальном времени и полный аудиторский след для всех выполнений автоматизации.
* Определять логику потока с пользовательскими условиями, автоматическими повторными попытками, циклами и параллельной обработкой.

## Учебные модули

Следующие учебные модули показывают, как можно использовать ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** для автоматического реагирования на данные мониторинга.

[01Краткое руководство по Workflows

* Практическое руководство
* Создайте и запустите свой первый workflow.](/docs/analyze-explore-automate/workflows/quickstart)[02Создание workflow в Dynatrace Workflows

* Практическое руководство
* Создание и редактирование workflow в Dynatrace Workflows.](/docs/analyze-explore-automate/workflows/building)[03Создание простого workflow в Dynatrace Workflows

* Практическое руководство
* Создайте и запустите простой workflow.](/docs/analyze-explore-automate/workflows/simple-workflow)[04Триггеры workflow

* Обзор
* Введение в триггеры автоматизации для workflow.](/docs/analyze-explore-automate/workflows/trigger)[05Запуск и мониторинг workflow, созданных в Dynatrace Workflows

* Практическое руководство
* Запуск и мониторинг workflow, созданных в Dynatrace Workflows.](/docs/analyze-explore-automate/workflows/running)[06Пользовательские разрешения для workflow

* Справочник
* Руководство по аспектам безопасности автоматизации workflow в Dynatrace Workflows](/docs/analyze-explore-automate/workflows/security)[07Действия Workflows

* Обзор
* Используйте готовые действия Dynatrace для ваших workflow.](/docs/analyze-explore-automate/workflows/default-workflow-actions)[08Коннекторы Workflows

* Обзор
* Используйте готовые действия Dynatrace для ваших workflow и интегрируйте Dynatrace со сторонними системами.](/docs/analyze-explore-automate/workflows/actions)[09Управление workflow

* Обзор
* Управляйте вашими workflow](/docs/analyze-explore-automate/workflows/manage-workflows)[10Справочник по выражениям

* Справочник
* Познакомьтесь с выражениями workflow](/docs/analyze-explore-automate/workflows/reference)[11Сценарии использования Workflows

* Обзор
* Изучите распространённые сценарии использования Workflows в развёртываниях Dynatrace.](/docs/analyze-explore-automate/workflows/use-cases)

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Откройте в Dynatrace Hub

[Автоматизируйте задачи в вашем ИТ-ландшафте, устраняйте проблемы и визуализируйте процессы.](https://www.dynatrace.com/hub/detail/automations?internal_source=doc&internal_medium=link&internal_campaign=cross)
