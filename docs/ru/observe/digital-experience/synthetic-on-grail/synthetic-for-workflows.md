---
title: Synthetic for Workflows
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-on-grail/synthetic-for-workflows
scraped: 2026-03-06T21:31:47.956083
---

# Synthetic for Workflows

# Synthetic for Workflows

* Последняя версия Dynatrace
* Практическое руководство
* Время чтения: 5 мин
* Обновлено 20 января 2025 г.

Synthetic for Workflows позволяет выполнять синтетические мониторы по запросу в выбранных локациях в рамках ваших рабочих процессов. Dynatrace может реагировать на любое событие и запускать синтетические мониторы в рабочих процессах для оценки его влияния на пользовательский опыт. В зависимости от результата, **Workflows** могут уведомить команду, создав заявку в Jira, отправив сообщение в Slack или инициировав процесс исправления.

С помощью Synthetic for Workflows вы можете выбрать, какие мониторы хотите запустить.

* Список всех доступных мониторов.
* Мониторы, помеченные определёнными идентификаторами.
* Мониторы, назначенные определённым фронтенд-приложениям.

Также возможно использовать [выражения рабочих процессов](../../../analyze-explore-automate/workflows/reference.md#expressions "Познакомьтесь с выражениями рабочих процессов") для извлечения списка мониторов и локаций из входящих событий, что позволяет создавать повторно используемые рабочие процессы.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Установите Synthetic for Workflows**](synthetic-for-workflows.md#install "Расширьте возможности автоматизации с помощью синтетического мониторинга.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Предоставьте разрешения для Workflows**](synthetic-for-workflows.md#permissions "Расширьте возможности автоматизации с помощью синтетического мониторинга.")

### Шаг 1: Установка Synthetic for Workflows

Чтобы использовать действия Synthetic for Workflows, сначала необходимо установить **Synthetic for Workflows** из Dynatrace Hub.

1. В Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub") найдите **Synthetic for Workflows**.
2. Выберите **Synthetic for Workflows** и нажмите **Install**.

После установки действия `synthetic_for_workflows` автоматически появятся в разделе **Choose action** в [**Workflows**](../../../analyze-explore-automate/workflows.md "Автоматизируйте ИТ-процессы с помощью Dynatrace Workflows -- реагируйте на события, планируйте задачи и подключайте сервисы.").
Перед началом работы убедитесь, что ваши мониторы правильно настроены. Чтобы создать новый монитор, найдите **Synthetic** в Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub").

### Шаг 2: Предоставление разрешений для Workflows

Необходимые разрешения перечислены в [Workflows](../../../analyze-explore-automate/workflows.md#authorization "Автоматизируйте ИТ-процессы с помощью Dynatrace Workflows -- реагируйте на события, планируйте задачи и подключайте сервисы."). Кроме того, для выполнения **Synthetic for Workflows** вам потребуются следующие разрешения

```
environment:roles:manage-settings,



storage:buckets:read,



storage:events:read
```

Пример политики:

```
ALLOW



app-engine:apps:run,



automation:workflows:read,



app-engine:functions:run,



automation:workflows:run,



automation:workflows:write,



environment:roles:manage-settings,



storage:buckets:read,



storage:events:read;
```

## Использование действия `synthetic_for_workflows`

### Выбор синтетических мониторов

Чтобы выбрать мониторы из списка для Synthetic for Workflows, необходимо указать синтетические мониторы, которые вы хотите запускать при срабатывании рабочего процесса. Вы можете выбрать монитор из режима **Visual** или **From event**.
Вы можете найти наиболее подходящие мониторы, фильтруя список по различным критериям, таким как тип, имя, приложения и теги.

Вы также можете

* Выбрать **With specific tags**, чтобы просмотреть мониторы с определённым тегом.
* Выбрать **Assigned to frontend applications**, чтобы выбрать мониторы, назначенные определённым приложениям. Доступные приложения можно найти в списке **Select frontend applications**.

### Выбор синтетической локации

В разделе **Select a synthetic location**

1. Выберите **Visual** или **From event**.
2. Для **Visual** выберите синтетическую локацию из выпадающего списка.
3. Для **From event** вы можете определить список синтетических мониторов, которые хотите запускать в рабочем процессе, на основе входящего события. Для этого необходимо создать [выражение](../../../analyze-explore-automate/workflows/reference.md#expressions "Познакомьтесь с выражениями рабочих процессов"), которое позволит рабочему процессу извлечь эту информацию из события и запустить выбранные мониторы.

Если вы не выберете локацию, монитор будет запущен в локации, определённой в конфигурации монитора.

### Добавление метаданных

В разделе **Add metadata** вы можете обогатить результаты синтетического тестирования контекстом выполнения, таким как имя приложения, версия, стадия разработки и версия сборки.

Чтобы добавить метаданные

1. Нажмите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add")**Add metadata**.
2. Заполните поля **Key** и **Value**. В этих полях можно использовать [выражения рабочих процессов](../../../analyze-explore-automate/workflows/reference.md#expressions "Познакомьтесь с выражениями рабочих процессов").
3. Ваши метаданные сохраняются автоматически.

### Настройка выполнения монитора

Вы можете настроить параметры выполнения, которые будут применяться ко всем запускам в рамках Workflows.

Для этого включите или отключите любой из следующих параметров:

* Остановить при обнаружении проблемы
* Завершить с ошибкой при проблеме производительности
* Завершить с ошибкой при предупреждении SSL
* Делать снимки экрана при успешном выполнении

### Настройка выполнения рабочего процесса

Вы можете настроить поведение рабочего процесса в случае сбоя пакетного выполнения синтетического монитора.
Это выполняется с помощью переключателя **Fail workflow task on failed batch execution**.

Вы можете включить или отключить его:

* Включено (  ): Если выполнение монитора завершается неудачей, задача завершается с ошибкой.
  Это можно комбинировать с другими параметрами конфигурации, такими как переключатель **Retry on error**, чтобы управлять поведением рабочего процесса в зависимости от неудавшейся задачи.
* Отключено (  ): Если выполнение монитора завершается неудачей, задача завершается успешно.
  Действие Synthetic for Workflows генерирует результаты, которые могут быть использованы следующей задачей, например [Site Reliability Guardian](synthetic-for-workflows.md#synthetic-srg "Расширьте возможности автоматизации с помощью синтетического мониторинга.").

По умолчанию этот переключатель отключён.

## Результаты синтетического тестирования в Grail

Обратите внимание, что Synthetic **не** генерирует события Grail для тенантов без DPS. Вся обработка будет основываться исключительно на данных API. Чтобы узнать больше о лицензировании DPS, см. [Лицензирование Dynatrace](../../../license.md "О Dynatrace Platform Subscription (DPS), модели лицензирования для всех возможностей Dynatrace.").

Результаты синтетических мониторов, запущенных по запросу, хранятся как события в Grail.

Существует три типа событий:

* `batch_status` -- содержит сводный результат всех выполнений мониторов в пакете
* `browser_monitor_execution` -- содержит подробную информацию об одном выполнении браузерного монитора
* `http_monitor_execution` -- содержит подробную информацию об одном выполнении HTTP-монитора

## Интеграция Synthetic for Workflows с Site Reliability Guardian

Если вы хотите оценивать цели на основе результатов синтетических мониторов, вы можете интегрировать [Site Reliability Guardian (SRG)](../../../deliver/site-reliability-guardian.md "Автоматическая проверка целей производительности, доступности и ёмкости ваших критически важных сервисов для принятия правильного решения о релизе.") в качестве следующего действия в вашем рабочем процессе.

Для этого

1. Нажмите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") на задаче `synthetic_for_workflows` и затем выберите **Site Reliability Guardian** из **Choose action**. Это создаст задачу `site_reliability_guardian_1`.
2. Выберите задачу `site_reliability_guardian_1`. В **Variables** укажите параметр `batchId` из результата синтетического теста и значение `{{ result("synthetic_for_workflows_1")["event.id"] }}`. Вы можете заменить `"synthetic_for_workflows_1_"` на любое другое имя задачи.
3. В Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub") найдите **Site Reliability Guardian**.
4. Нажмите кнопку **+ Guardian**.
5. В вашем guardian выберите ![More actions](https://dt-cdn.net/images/dashboards-app-menu-kebab-c39eda426b.svg "More actions") и выберите ![Summarize](https://dt-cdn.net/images/dashboards-app-menu-list-63d17138c9.svg "Summarize") **Variables**.
6. Нажмите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Add variable**.
7. Введите `batchId` в поле **Name**. В поле **Value** укажите значение по умолчанию. Нажмите кнопку **Add**, чтобы сохранить изменения.
8. В правой части заполните **Guardian name**.
9. Нажмите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Add new objective** и укажите один из следующих запросов [DQL](../../../platform/grail/dynatrace-query-language.md "Как использовать Dynatrace Query Language.").

Обратите внимание, что запросы для синтетических событий, выполняемые за пределами приложения Synthetic, например из Notebooks, Dashboards и SRG, **не** тарифицируются.

Используйте следующий запрос для получения общей длительности всего пакета.

```
fetch dt.synthetic.events



| filter event.id == $batchId



| fields batch_result.duration
```

Используйте следующий запрос для проверки успешного завершения пакета.

```
fetch dt.synthetic.events



| filter event.id == $batchId



| filter batch.status == "Success"



| summarize count = count()
```

## Связанные темы

* [Обновления имён атрибутов Synthetic](synthetic-for-workflows/synthetic-event-formats.md "Необходимые обновления имён атрибутов синтетических событий в Workflows.")
