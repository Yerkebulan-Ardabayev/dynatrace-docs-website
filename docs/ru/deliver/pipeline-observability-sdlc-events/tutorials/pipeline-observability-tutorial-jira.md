---
title: Оптимизация метрик потока инженерии с помощью данных Jira
source: https://www.dynatrace.com/docs/deliver/pipeline-observability-sdlc-events/tutorials/pipeline-observability-tutorial-jira
scraped: 2026-03-02T21:30:16.892113
---

# Оптимизация метрик инженерного потока с использованием данных Jira


* Latest Dynatrace
* Preview

В этом руководстве вы настроите интеграцию между Jira и Dynatrace для ежедневного импорта снимка ваших эпиков Jira в Dynatrace.
Вы анализируете систему доставки ценности с наивысшей точки обзора.
По умолчанию это эпики в Jira.
Мы предоставляем вам дашборд, который вы заполните данными из Jira, что позволит оптимизировать ваш инженерный поток, принимая решения на основе данных для улучшения фокуса, предсказуемости и времени доставки ценности.

Ниже представлен скриншот с основными разделами дашборда **Engineering Flow Metrics**.

![Скриншот с основными разделами дашборда Engineering Flow Metrics.](https://dt-cdn.net/images/20251128-engineering-flow-metrics-dashboard-on-playground-highlights-3065-0660cc0d38.png)

## Концепции

События жизненного цикла разработки ПО (SDLC events)
:   SDLC-события в рамках жизненного цикла разработки программного обеспечения (SDLC) играют ключевую роль в достижении эффективной наблюдаемости пайплайнов.
    Они представляют ключевые действия, происходящие на протяжении жизненного цикла, такие как выпуск новой версии ПО, развёртывание этой версии или успешное прохождение нагрузочного теста.
    Подробнее см. Семантический словарь SDLC-событий.")

## Целевая аудитория

Дашборд **Engineering Flow Metrics** предназначен для:

* Руководителей высшего звена и лиц, принимающих решения, которым требуется общий обзор потоков создания ценности для согласования бизнес-целей с результатами доставки.
* Команд разработки, владельцев продуктов, продуктовых менеджеров, agile-коучей и инженерных менеджеров, которые используют Jira для получения информации о прогрессе их команды.

## Предварительные требования

* Доступ к экземпляру Jira Cloud.
* У вас есть [токен доступа](../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#create-api-token "Узнайте о концепции токена доступа и его областях действия.") с областью действия `OpenPipeline - Ingest Software Development Lifecycle Events (Built-in)`.

## Инструкция

1. Jira: Настройка быстрого фильтра

В Jira настройте быстрый фильтр, чтобы получить `<filter-id>` для запланированной [автоматизации Jira](https://www.atlassian.com/software/jira/guides/automation/overview#board-vs-project).

1. Перейдите в ваш экземпляр Jira и [настройте быстрый фильтр Jira](https://support.atlassian.com/jira-software-cloud/docs/configure-quick-filters/).

   Для мониторинга эпиков в Jira вы можете использовать следующий JQL-запрос в качестве примера.

   ```
   type = Epic AND project = <your-project-name> AND (resolved is EMPTY or resolved > -2w)
   ```
2. Выберите **Copy filter**.
   Откроется диалоговое окно **Copy filter**.
3. Введите имя фильтра в поле **Name**.
4. Выберите, кто может просматривать, в выпадающем списке **Viewers**.

   Фильтр должен быть видим для исполнителя автоматизации.
   Для надёжности установите разрешение так, чтобы все могли видеть фильтр.

   Подробнее об исполнителях в автоматизации Jira см. [Что такое исполнитель правила?](https://support.atlassian.com/cloud-automation/docs/what-is-a-rule-actor/).
5. Выберите **Save**.
6. Получите ID фильтра из URL Jira.
   Формат аналогичен `/issues/?filter=<filter-id>`, например, `?filter=12345`

2. Dynatrace: Скопируйте путь эндпоинта

Вам нужен **Endpoints path** для настройки запланированной автоматизации Jira.

Чтобы найти и скопировать **Endpoints path**:

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Software development lifecycle**.
2. На вкладке **Ingest sources** > **Endpoints path** наведите курсор на **Endpoints path**.
3. В меню источника выберите **Copy**, чтобы скопировать **Endpoints path**.

3. Jira: Настройка триггера для запланированной автоматизации Jira

Данные хранятся как события в Dynatrace.
Соответственно, данные тарифицируются как Events powered by Grail.
Подробнее о стоимости Events powered by Grail см. Обзор Events powered by Grail (DPS).

Чтобы заполнить Dynatrace данными из Jira, настройте автоматизацию Jira.

1. Перейдите в Jira и откройте ваш проект Jira.
2. Выберите **Project settings**.
3. В левой панели выберите **Automation**.
4. Выберите **Create rule**.
   Начните с пустого правила автоматизации Jira, что позволит настроить правильные поля.
5. Выберите триггер **Scheduled**.
   Подробнее см. [Триггеры автоматизации Jira](https://support.atlassian.com/cloud-automation/docs/jira-automation-triggers/) и [Jira Automation: установка «Scheduled» в качестве триггера и использование нескольких действий](https://confluence.atlassian.com/automationkb/automation-set-scheduled-as-a-trigger-and-use-multiple-actions-1388151419.html).
6. В поле **Occurrence** для ежедневного запуска, например, в 4:00 утра.

   1. В поле **Run rule every** установите триггер **Scheduled** на `1`.
   2. В поле **Run rule every** выберите **Days**.
   3. В поле **At** установите время `4:00 AM`.
   4. В поле **At** выберите часовой пояс.
7. Установите флажок **Run a JQL search and execute actions for each work item in the query**.
8. Обязательно: в поле **JQL** введите фильтр, созданный ранее, в формате `filter=<filter-id>`.
   Замените `<filter-id>` на ID фильтра, который вы создали ранее.

   Убедитесь, что **Only include work items that have changed since last time** не выбрано.
9. Выберите **Next** для завершения настройки запланированного триггера.

4. Jira: Начало настройки действия Send web request для автоматизации Jira

В рамках автоматизации Jira необходимо настроить действие **Send web request**.
Это действие отправляет HTTP-запрос на указанный URL.

1. Добавьте [действие **Send web request**](https://confluence.atlassian.com/automation074/actions-1141481289.html#Actions-sendwebrequest).
2. Введите **Web request URL** из шага [Dynatrace: Скопируйте путь эндпоинта](pipeline-observability-tutorial-jira.md#copy "Стабилизируйте систему доставки ценности, принимая решения на основе данных для улучшения фокуса, предсказуемости и времени доставки ценности.").
   Шаблон: `https://{your-environment-id}.live.dynatrace.com/platform/ingest/v1/events.sdlc`.
3. В поле **HTTP method** выберите **POST**.
4. В поле **Web request body** выберите **Custom data**.
5. В разделе **Headers** установите следующие пары **Key** и **Value**:

   1. **Content-Type** — `application/json`.
   2. **Authorization** — `Api-Token <your-API-token>`.
   3. **accept** — `application/json; charset=utf-8`.
6. Замените `<your-API-token>` на ваш токен доступа API Dynatrace, сгенерированный на предыдущем шаге.

5. Jira: Поиск ID полей Rank и Team в Jira

Вам нужно найти автоматически созданные ID полей **Rank** и **Team** в Jira, специфичные для вашего экземпляра Jira, чтобы использовать их для аналитики на следующем шаге.

В вашем браузере для поиска полей Jira выполните вызов к Jira API для любого задания в вашем проекте.

1. Введите следующий URL в адресную строку браузера: `https://<your-endpoint>.atlassian.net/rest/api/2/issue/<your-issue>?expand=names`.
   Замените `<your-endpoint>` на ваш URL.
   Замените `<your-issue>` на любой из ваших ключей заданий.
2. Откройте URL.
   Этот запрос возвращает JSON-вывод в браузер.
3. Найдите пользовательские поля **Rank** и **Team**.
   Вы можете использовать ID пользовательского поля в автоматизации Jira для отправки данных на ваш дашборд.

   Формат поля: `customfield_xxxxx`, где `xxxxx` — ID поля.
   Блок кода ниже показывает пример тела JSON-ответа, включая ID пользовательских полей.

   ```
   {


   "expand": "renderedFields,names,schema,operations,editmeta,changelog,versionedRepresentations",


   "id": "10000",


   "self": "https://<your-endpoint>.atlassian.net/rest/api/2/issue/10000",


   "key": "SCRUM-1",


   "names": {


   "customfield_10001": "Team",


   "customfield_10019": "Rank"


   }


   }
   ```

6. Jira: Завершение настройки действия Send web request для автоматизации Jira

Добавьте ID пользовательских полей автоматически созданных полей **Rank** и **Team** в Jira в поле **Custom data** вашего действия **Send web request** в Jira.

1. Перейдите к вашей автоматизации Jira.
2. В поле **Custom data** введите следующий шаблон для генерации JSON из данных задания JIRA:

   ```
   {


   "specversion": "1.0"


   , "id": "{{issue.key}}"


   , "source": "JIRA"


   , "day": "{{now.jiraDate}}"


   , "version": "1"


   , "key": "{{issue.key}}"


   , "summary": {{issue.summary.asJsonString()}}


   , "type": "{{issue.issuetype.name}}"


   {{#exists(issue.assignee)}}


   , "assignee": "{{issue.assignee.displayName}}"


   {{/}}


   {{#exists(issue.customfield_<your-team-custom-field-id>)}}


   , "team": "{{issue.customfield_<your-team-custom-field-id>.name}}"


   {{/}}


   , "status": "{{issue.status.name}}"


   , "status_category": "{{issue.status.statuscategory.name}}"


   {{#exists(issue.resolution)}}


   , "resolution": "{{issue.resolution.name}}"


   {{/}}


   {{#if(not(issue.labels.isEmpty))}}


   , "labels": [


   {{#issue.labels}}


   "{{.}}" {{^last}},{{/}}


   {{/}}


   ]


   {{/}}


   {{#if(equals(issue.fixVersions.size, 1))}}


   {{#issue.fixVersions}}


   , "fix_version": "{{name}}"


   , "fix_version.release_date": "{{releaseDate.format("yyyy-MM-dd")}}"


   {{/}}


   {{/}}


   , "created": "{{issue.created}}"


   , "status_changed_on": "{{issue.statuscategorychangedate}}"


   , "resolved": "{{issue.resolved}}"


   , "rank": "{{issue.customfield_<your-rank-custom-field-id>}}"


   , "project": "{{issue.project.key}}"


   }
   ```

   Этот пример использует [смарт-значения Jira](https://support.atlassian.com/cloud-automation/docs/smart-values-in-jira-automation/) для извлечения необходимой информации и загрузки её в Dynatrace.
   `{{#if(equals(issue.fixVersions.size, 1))}}` подразумевает, что эпик Jira имеет только одну целевую версию (fix version).
3. Замените `<your-rank-custom-field-id>` на ID пользовательского поля **Rank**.
4. Замените `<your-team-custom-field-id>` на ID пользовательского поля **Team**.
5. Выберите **Next** для завершения настройки действия **Send web request**.
6. Выберите **Turn on rule** для сохранения автоматизации.
7. Введите **Name** для автоматизации Jira.
8. Выберите **Turn on rule** для сохранения.

7. Организация данных

Для организации данных в Dynatrace настройте [пользовательский бакет Grail](../../../platform/grail/organize-data.md#custom-grail-buckets "Информация о модели данных Grail, состоящей из бакетов, таблиц и представлений.").

1. В Dynatrace перейдите в **Settings** > **Storage management** > **Bucket storage management**.
2. Выберите **Bucket**.
3. В диалоговом окне **New bucket** введите **Bucket name** и **Display name**. Используйте `jira_events`, поскольку пример дашборда ожидает это имя.
4. Установите **Bucket table type** в значение **events**.
5. Установите **Retention period** на три года в днях, то есть `1095` дней.
6. Выберите **Create**.

Если данные должны быть ограничены, настройте разрешения бакета.

8. Маршрутизация данных

Для маршрутизации данных в пользовательский бакет настройте пайплайн SDLC.

1. Перейдите в **Settings** > **Process and contextualize** > **OpenPipeline** > **Software development lifecycle**.
2. Перейдите на вкладку **Pipelines**.
3. Выберите **Pipeline**.
4. Введите **Name** пайплайна.
5. Перейдите на вкладку **Storage**.
6. Выберите **Processor** > **Bucket assignment**.
7. Введите **Name** нового процессора, например, `Jira Daily Snapshot`.
8. Установите **Matching condition** в `source == "JIRA"`.
9. В выпадающем списке **Storage** выберите ваш бакет из предыдущего шага.
10. Выберите **Save**.
11. Перейдите на вкладку **Dynamic routing**.
12. Выберите **Dynamic routing**.
13. В диалоговом окне **Add a new dynamic route** введите **Name** нового динамического маршрута.
14. В поле **Matching condition** введите `source == "JIRA"`.
15. Выберите ваш пользовательский пайплайн в выпадающем списке **Pipeline**.
16. Выберите **Add**.
17. Выберите **Save**.

Все события, созданные автоматизацией Jira, добавляются в бакет.
Подробнее см. [Настройка пайплайна обработки](../../../platform/openpipeline/getting-started/tutorial-configure-processing.md#process "Настройте источники приёма, маршруты и обработку ваших данных в OpenPipeline.").

9. Проверка настройки

Этот шаг посвящён проверке настройки Jira и Dynatrace.

1. Запустите автоматизацию Jira вручную для проверки правила автоматизации.
2. Запросите события через DQL, например в **Notebooks**, чтобы убедиться, что ваши события были успешно загружены.

   1. Перейдите в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
   2. Выберите или создайте блокнот.
   3. Выберите ![Grail](https://cdn.bfldr.com/B686QPH3/at/kc3c7k476pbx2pb8cphzktf/Grail.svg?auto=webp&width=72&height=72 "Grail") DQL, чтобы добавить новую секцию с полем ввода DQL-запроса.
   4. Введите следующий DQL-запрос:

      ```
      fetch events


      | filter dt.system.bucket == "jira_events"
      ```

Этот запрос вернёт данные после успешного выполнения автоматизации.

10. Использование дашборда Engineering Flow Metrics для анализа

Мы предоставляем вам готовый дашборд.

Чтобы найти и использовать дашборд:

1. Перейдите к [дашборду Engineering Flow Metrics на Playground](https://dt-url.net/e0032zt).
2. [Скачайте](../../../analyze-explore-automate/dashboards-and-notebooks/dashboards-new.md#dashboards-download "Создавайте интерактивные, настраиваемые представления для визуализации, анализа и обмена данными наблюдаемости в реальном времени.") дашборд.
3. [Загрузите](../../../analyze-explore-automate/dashboards-and-notebooks/dashboards-new.md#dashboards-upload "Создавайте интерактивные, настраиваемые представления для визуализации, анализа и обмена данными наблюдаемости в реальном времени.") дашборд в вашу среду.

   Вам потребуется скорректировать начальную дату определённых запросов в соответствии с началом загрузки ваших данных, что подробно описано в разделе **Hard-Coded Dates** дашборда.

   Разделы **Epic Throughput**, **Lead Time** и **Implementation Aging Chart** заполняются сразу после первого импорта данных.

   После того как данные ежедневных снимков будут доступны как минимум две недели, вы можете выполнять анализ с помощью различных разделов дашборда, например **Epic Burndown**, **Cumulative Flow Diagram**, **Work In Progress**, **Backlog Stability** и **Changes**.

   Дашборд показывает:

   * **Epic Throughput**:
     Историческая пропускная способность показана серым цветом и основана на **Fix Version**.
     Эпики, запланированные на будущее, показаны синим, на основе кварталов года **Fix Version**.
     Тонкая зелёная линия показывает среднее за последние четыре завершённых квартала.
     Таблица на дашборде отображает отклонение от среднего для каждого квартала.
   * **Epic Burndown**:
     Burndown показывает эпики Jira по статусам с течением времени.
     Графики основаны на недельном расписании с использованием последней доступной точки данных за каждую неделю.
   * **Lead Time**:
     Время между созданием и закрытием эпика.
     Учитываются эпики, закрытые в пределах квартала.
   * **Implementation Aging Chart**:
     Время в разработке.
     Один месяц равен 30 дням.
   * **Cumulative Flow Diagram**:
     Количество эпиков Jira по статусам с течением времени.
     Закрытые эпики исчезают через две недели.
   * **Work In Progress**:
     Эпики **In Progress**.
   * **Backlog Stability**:
     Показывает топ-35 эпиков в бэклоге.
     Одна линия представляет один эпик.
     Линия на диаграмме начинается при создании эпика и заканчивается, как только эпик закрыт со статусом **Closed**.
     Эпики ниже топ-35 объединены в одну линию внизу графика.
     Если линии пересекаются, приоритеты изменились.
   * **Changes in the last 2 weeks**:
     Показаны изменения в полях **Status**, **Fix Version** и **Assignee**.

## Дальнейшие шаги

Теперь у вас есть дашборд, который позволяет просматривать метрики и начать оптимизацию потока доставки ценности.
Дашборд служит отправной точкой; вы можете расширить или уточнить его в соответствии с вашими конкретными потребностями.

Ниже представлен полный скриншот дашборда **Engineering Flow Metrics**.

![Скриншот дашборда Engineering Flow Metrics.](https://dt-cdn.net/images/20251128-engineering-flow-metrics-dashboard-on-playground-3065-68560a9b6d.png)

## Связанные темы

* События жизненного цикла разработки ПО (SDLC).")
* Загрузка SDLC-событий, которые затем можно загрузить для генерации аналитики.")
* Поток данных в OpenPipeline
* Источники приёма в OpenPipeline
* Анализ SDLC-событий из вашего пайплайна на наших примерах.")
