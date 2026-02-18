---
title: Dashboards
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new
scraped: 2026-02-18T05:31:19.406174
---

# Dashboards

# Dashboards

* Последние Dynatrace
* Приложение
* 10 мин на чтение
* Обновлено 28 января 2026 г.

Необходимые условия

### Разрешения

В следующей таблице описаны необходимые разрешения.

Разрешение

Описание

app-engine:functions:run

Разрешает пользователю запускать функции

app-engine:apps:run

Разрешает пользователю запускать функции

app-engine:edge-connects:read

Разрешает пользователю читать конфигурацию EdgeConnect через функции

document:environment-shares:read

Разрешает пользователю доступ к общим панелям мониторинга

document:direct-shares:read

Разрешает пользователю доступ к общим панелям мониторинга

state:user-app-states:write

Разрешает приложению сохранять настройки представления, такие как выбранный временной интервал или значения переменных

state:user-app-states:read

Разрешает приложению читать настройки представления, такие как выбранный временной интервал или значения переменных

state:user-app-states:delete

Разрешает приложению удалять настройки представления, такие как выбранный временной интервал или значения переменных

davis:analyzers:read

Разрешает пользователю читать конфигурацию анализаторов Davis

davis:analyzers:execute

Разрешает пользователю запускать анализаторы Davis

10

строк на страницу

Страница

1

из 1

Начните работу

Основные понятия

Варианты использования

С помощью ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** вы можете создавать мощные, основанные на данных документы для пользовательской аналитики.

![Получайте информацию в режиме реального времени, преобразуя сложные данные в динамические интерактивные панели мониторинга.](https://dt-cdn.net/hub/00_General.png)![Быстрый старт с помощью готовых панелей мониторинга, разработанных для ваших повседневных нужд.](https://dt-cdn.net/hub/01_Ready_made.png)![Создавайте свою панель мониторинга легко, всего в несколько кликов.](https://dt-cdn.net/hub/02_Explore.png)![Настраивайте любую визуализацию с легкостью.](https://dt-cdn.net/hub/03_Customize.png)![Оцените динамические и интерактивные панели мониторинга с универсальными фильтрами переменных.](https://dt-cdn.net/hub/04_Variables.png)![Делитесь своими выводами с другими за считанные секунды.](https://dt-cdn.net/hub/05_Share.png)

1 из 6Получайте информацию в режиме реального времени, преобразуя сложные данные в динамические интерактивные панели мониторинга.

## Плитки панели мониторинга

В ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** панель мониторинга может состоять из нескольких плиток:

* [Explore](#explore): исследуйте данные, такие как журналы, метрики и бизнес-события, с помощью нашего интерфейса point-and-click.
* [Query](#query): отображает данные, полученные с помощью запросов Grail.
* [Code](#code): отображает данные, возвращаемые кодом, выполненным с помощью функций Dynatrace.
* [Markdown](#markdown): статический контент, отредактированный в markdown.

### Плитка Explore

Вы можете использовать параметры Explore для изучения журналов, метрик, бизнес-событий и многого другого с помощью нашего интерфейса point-and-click. Без знания DQL или программирования вы можете создавать и начинать использовать плитки панели мониторинга за считанные минуты.

Для получения дополнительной информации ознакомьтесь со страницей [Explore data](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data "Explore your data with our point-and-click interface."), которая показывает, как создавать плитки Explore.

### Плитка Query

Плитки запросов позволяют легко запрашивать данные из Grail и [визуализировать](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.") результат различными способами.

Плитка запроса состоит из поля ввода запроса, в котором можно написать запрос DQL. В поле ввода используйте **Ctrl**+**Space**, чтобы в любое время вызвать автозаполнение.

Вы можете управлять временным интервалом для запроса с помощью выпадающего списка временного интервала. Если временной интервал определен в самом запросе, выпадающий список будет отключен.

### Плитка Code

Раздел кода позволяет получать данные для вашей панели мониторинга с помощью функций Dynatrace.

### Плитка Markdown

Раздел markdown может быть чем угодно, от небольшого примечания о чем-то на панели мониторинга до целой страницы отформатированной информации с ссылками и изображениями.

* Легко редактировать
* Приятно на вид

Чтобы вставить запросы из вашей панели мониторинга с автозаполнением, используйте **Ctrl**+**Space**.

Вы можете ссылаться на другие места на вашей панели мониторинга и в других местах.

Синтаксис ссылки Markdown

Ссылка в Markdown — это метка и ссылка в форме `[метка](адрес)`, где:

* `метка` — это произвольный текст для отображения ссылки в вашей плитке или разделе Markdown
* `адрес` указывает, что открыть при выборе ссылки, например веб-сайт или приложение Dynatrace

Ссылка на

Синтаксис и примеры

Веб-сайт

```
[Моя метка](https://www.example.com/)
```

Приложение Notebooks

```
[Моя метка](/ui/apps/dynatrace.notebooks/notebooks)
```

Конкретный Notebook

**Синтаксис**:

```
[метка](/ui/apps/dynatrace.notebooks/notebook/<notebookid>)
```

**Пример**:

```
[Моя метка](/ui/apps/dynatrace.notebooks/notebook/274edae4-dfe8-41fb-aced-5020fb1270bc)
```

Чтобы получить адрес

1. Отобразите целевой Notebook.
2. Скопируйте все из адресной строки браузера, начиная с `/ui/`.
3. Вставьте его в свой Markdown в качестве адреса ссылки.

Конкретный раздел Notebook

**Синтаксис**:

```
[метка](/ui/apps/dynatrace.notebooks/notebook/<notebookid>#<sectionid>)
```

**Пример**:

```
[Моя метка](/ui/apps/dynatrace.notebooks/notebook/274edae4-dfe8-41fb-aced-5020fb1270bc#cb69caf1-52ed-4e73-8a3e-120e8cd7e8f8)
```

Чтобы получить адрес

1. Отобразите целевой Notebook.
2. Выберите целевой раздел Notebook.
3. Скопируйте все из адресной строки браузера, начиная с `/ui/`.
4. Вставьте его в свой Markdown в качестве адреса ссылки.

Приложение Dashboards

```
[Моя метка](/ui/apps/dynatrace.dashboards/)
```

Конкретная панель мониторинга

**Синтаксис**:

```
[метка](/ui/apps/dynatrace.dashboards/<dashboardid>)
```

**Пример**:

```
[Моя метка](/ui/apps/dynatrace.dashboards/dashboard/9f24c36e-ca5f-401c-8e00-5e4b05c46bd2)
```

Чтобы получить адрес

1. Отобразите целевую панель мониторинга.
2. Скопируйте все из адресной строки браузера, начиная с `/ui/`.
3. Вставьте его в свой Markdown в качестве адреса ссылки.

Конкретная плитка панели мониторинга

**Синтаксис**:

```
[метка](/ui/apps/dynatrace.dashboards/dashboard/<dashboardid>#tileIds=n)
```

**Пример**:

```
[Моя метка](/ui/apps/dynatrace.dashboards/dashboard/9f24c36e-ca5f-401c-8e00-5e4b05c46bd2#from=now%28%29-2h&to=now%28%29&tileIds=6)
```

Чтобы включить конкретный ID плитки в ссылку

1. Отобразите целевую панель мониторинга.
2. Выберите целевую плитку на целевой панели мониторинга.
3. Скопируйте все из адресной строки браузера, начиная с `/ui/`.
4. Вставьте его в свой Markdown в качестве адреса ссылки.

## Варианты использования

Dashboards позволяет вам:

* Использовать готовые панели мониторинга для мониторинга состояния вашей системы в режиме реального времени.
* Создавать пользовательские панели мониторинга легко с помощью простого в использовании редактора или Davis CoPilot™ .
* Детально изучать свои данные благодаря бесшовной интеграции с другими приложениями Dynatrace.
* Использовать возможности Davis AI для выявления аномалий и прогнозирования непосредственно на ваших графиках.
* Искать любой тип данных на платформе и объединять их даже с внешними данными в одном представлении.
* Настраивать фильтры переменных для мониторинга различных ресурсов в рамках одной панели мониторинга.

Эти процедуры описывают основы использования ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** и помогут вам начать настройку и создание собственных панелей мониторинга.

## Использовать панели мониторинга

### Использовать сочетания клавиш

Сочетания клавиш помогают вам работать быстрее в ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.

Чтобы отобразить список сочетаний клавиш, в ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** откройте меню и выберите **Сочетания клавиш** или используйте сочетание клавиш **Shift**+**?**

| Действие | Сочетание клавиш |
| --- | --- |
| **Общие** |  |
| Выделить несколько плиток | Выберите плитку, нажмите **Space**, чтобы получить двойную рамку вокруг плитки, используйте клавиши со стрелками, чтобы перейти к другой плитке, а затем снова нажмите **Space**, чтобы выбрать несколько плиток |
| Выделить все плитки | **Ctrl**/**Cmd**+**A** |
| Удалить выбранные плитки | **Del** |
| Скопировать выбранные плитки в буфер обмена | **Ctrl**/**Cmd**+**C** |
| Вставить плитки из буфера обмена | **Ctrl**/**Cmd**+**V** |
| Добавить плитку | **Ctrl**/**Cmd**+**Shift**+**Enter** |
|  |  |
| **Плитки кода** |  |
| Добавить код | **Shift**+**C** |
| Выполнить код | **Ctrl**/**Cmd**+**Enter** |
|  |  |
| **Плитки данных** |  |
| Добавить запрос | **Shift**+**D** |
| Выполнить запрос | **Ctrl**/**Cmd**+**Enter** |
|  |  |
| **Плитки Markdown** |  |
| Добавить Markdown | **Shift**+**M** |
|  |  |
| **Плитки Service-Level Objective** |  |
| Добавить Service-Level Objective | **Shift**+**S** |
|  |  |
| **Переменные** |  |
| Добавить переменную | **Shift**+**V** |

### Список панелей мониторинга

#### List all dashboards

To list dashboards

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. In the **Dashboards** panel, the **Last opened by you** section lists recently accessed dashboards.
3. Наведите курсор на название панели мониторинга и выберите  для меню доступных команд для этой панели мониторинга. В этом примере мы отобразим меню для панели мониторинга с именем `my dashboard 3`.

   ![Dashboards: Last opened by you: dashboard-specific menu](https://dt-cdn.net/images/dashboards-last-opened-by-you-dashboard-specific-menu-269-08e78a134c.png)

   Команды, которые вы видите в меню, зависят от ваших разрешений для этой панели мониторинга. Например, вы не можете переименовать панель мониторинга другого пользователя, если он не предоставил вам права на редактирование этой панели мониторинга. (Но вы *можете* сделать копию общей панели мониторинга, а затем отредактировать свою копию.)

   * **Rename** включает редактирование имени панели мониторинга
   * **Duplicate** создает копию панели мониторинга
   * **Download** записывает панель мониторинга в JSON файл, который можно импортировать
   * **Change owner** назначает право собственности на панель мониторинга новому владельцу
   * **Move to trash** перемещает панель мониторинга в корзину

   Этот значок  после названия панели мониторинга означает, что кто-то поделился этой панелью мониторинга с вами.
4. Чтобы отобразить таблицу всех панелей мониторинга, к которым у вас есть доступ — ваших собственных панелей мониторинга и всех панелей мониторинга, которыми поделились с вами, — выберите  **All dashboards**.

   * Чтобы отсортировать таблицу, выберите заголовки **Name**, **Created** или **Last modified**.
   * Чтобы отфильтровать таблицу:

     + Вы можете ввести строку поиска в  панели фильтра в верхней части таблицы.
     + Вы можете выбрать **Owned by anyone**, **Owned by me** или **Shared with me** в списке в верхней части таблицы.
   * Чтобы создать новую панель мониторинга, выберите  **Dashboard** в верхнем левом углу.
   * Чтобы загрузить панель мониторинга, выберите  **Upload** в верхнем левом углу.
   * Чтобы удалить панель мониторинга, выберите  **Move to trash**. Если для панели мониторинга нет  значка, это означает, что у вас есть разрешение на просмотр этой общей панели мониторинга, но не на ее удаление.
   * Чтобы просмотреть удаленные панели мониторинга, выберите вкладку **Deleted** на странице **Dashboards**.

     + Чтобы восстановить удаленную панель мониторинга, выберите  **Restore**.
     + Чтобы окончательно удалить панель мониторинга, выберите  **Delete permanently**.

#### List my dashboards

To list all dashboards you own

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. In the **Dashboards** panel, select  **All dashboards**.
3. В верхней части таблицы **Dashboards** выберите **Owned by me**.

#### List dashboards shared with me

To list all dashboards shared with you

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. In the **Dashboards** panel, select  **All dashboards**.
3. В верхней части таблицы **Dashboards** выберите **Shared with me**.

#### List ready-made dashboards

To list all ready-made dashboards

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. In the **Dashboards** panel, select  **Ready-made dashboards**.

Alternatively, you can select  **All dashboards** and then change the filter at the top of the table from **All dashboards** to **Ready-made**.

What's special about ready-made documents

* Созданы и автоматически распространяются Dynatrace в качестве примеров и шаблонов.
* Только для чтения: вы можете редактировать их для использования во время сеанса и сохранять копию с вашими изменениями, но вы не можете сохранить свои изменения в исходном документе.
* Этот значок  в таблице документов указывает, что это готовый документ.

### Display a dashboard

To display a dashboard

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. Выберите название панели мониторинга. В этом примере мы открываем `my dashboard 2`.

   ![Open a dashboard](https://dt-cdn.net/images/open-my-dashboard-2-264-194755db23.png)

### Interact with a tile

If you see something on a dashboard that you want to zoom in on, you can maximize it and have a closer look, and then minimize it again when you're done.

When you maximize a tile, it is temporarily zoomed to the maximum size of the display so you can see the details of the selected tile.

To maximize a tile

1. Наведите курсор на плитку, чтобы отобразить команды, относящиеся к этой плитке.
2. Выберите  **Maximize**.

To return to the normal dashboard view, select **Minimize** in the upper-right corner.

### Refresh a dashboard

When you open a dashboard for the first time, the refresh rate is set to `Off` (no automatic refresh).

#### Manual refresh

To refresh the current dashboard manually, in the upper-right corner of the dashboard, select  (in the   pair).

#### Automatic refresh

To refresh the current dashboard automatically, in the upper-right corner of the dashboard, select  (in the   pair) and select a refresh rate.

* `Off` отключает автоматическое обновление
* Другие настройки будут обновлять панель мониторинга через указанный интервал

Если вы измените частоту обновления, эта частота будет запомнена при следующем открытии панели мониторинга.

Частая частота обновления может держать вас в курсе событий, но сложная панель мониторинга может потребовать некоторого времени для пересчета каждый раз при обновлении. Выберите частоту обновления, которая соответствует вашим потребностям и сложности панели мониторинга.

### Edit read-only dashboards

When you open a document (dashboard or notebook) for which you don't have write permission, you can still edit the document during your session. After you're finished, you have two options:

* Save your changes to a new document
* Discard your changes

Example:

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, list the ready-made dashboards, and select the **Getting started** dashboard.

   В верхнем левом углу, рядом с названием документа, написано  **Ready-made**.
2. Выберите плитку Pie chart и затем выберите  **Edit**.
3. Измените визуализацию с Pie на Donut.

   Теперь вам предлагается два варианта: **Save as new** и **Discard changes**.
4. Используйте обновленную панель мониторинга по мере необходимости. У вас есть полный доступ к редактированию для этого сеанса.
5. Когда вы закончите, выберите, что делать с вашими изменениями:

   * **Save as new** — сохраняет ваши изменения в новой копии отредактированной панели мониторинга.
   * **Discard changes** — отменяет ваши изменения и возвращает вас к нередактированной панели мониторинга только для чтения.

### Select the timeframe



To review or change settings that apply to an entire dashboard

1. Display the dashboard.
2. In the upper-right corner of the dashboard, select  **Settings**.

   The **Settings** panel is displayed.
3. Review or change settings as needed.

   Custom timeframe

   To set a default timeframe for a dashboard

   1. Display the dashboard.
   2. In the upper-right corner of the dashboard, select  **Settings**.
   3. Turn on **Custom timeframe**.
   4. Select the default timeframe for the selected dashboard.

      Changing this setting does not immediately update the timeframe of the current dashboard. The change is applied only to a new session with the dashboard (either for a different user, or for the same user returning to the dashboard for another session).

   For details about the dashboard timeframes, see [Select the timeframe](#dashboard-timeframe).

   Default segment

   To review or change the dashboard default segment

   1. Display the dashboard.
   2. In the upper-right corner of the dashboard, select  **Settings**.
   3. Turn on **Default segment**.
   4. Select the default segment for the selected dashboard.

      Changing this setting does not immediately update the segment of the current dashboard. The change is applied only to a new session with the dashboard (either for a different user, or for the same user returning to the dashboard for another session).

   For details about dashboard segments, see [Select segments](#segment).

   {$} Variables

   To review or change dashboard variables

   1. Display the dashboard.
   2. In the upper-right corner of the dashboard, select  **Settings**.

      The **Settings** panel is displayed.
   3. Select **Variables**.

   For details about dashboard variables, see [Add a variable to a dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-variable "Add variables to your Dynatrace dashboards.").

The timeframe describes the *when* of the data on the dashboard.

* When you open a dashboard for the first time, the standard global timeframe (**Last 2 hours**) is applied.
* If you change the global timeframe setting for your dashboard, that timeframe is applied the next time you open the dashboard. However, there are exceptions as described below.
* You can [set a dashboard-specific default timeframe](#timeframe-dashboard) that is applied each subsequent time you open the dashboard.
* You can [set a tile-specific timeframe](#timeframe-tile). This setting overrides the global timeframe.
* When you open a dashboard via a link, if a timeframe is included in the link, the link timeframe is applied and the default dashboard timeframe is ignored.

#### Change global timeframe

To change the global timeframe

1. In the upper-right corner of the dashboard, open the timeframe selector menu (the default is **Last 2 hours** ).
2. Select a new timeframe.

   * To select a standard timeframe, choose one of the standard **Relative timeframes**
   * To define a custom timeframe, define the timeframe in the **Custom timeframe** panel and select **Apply**.

     + Use the calendar buttons ![Calendar](https://dt-cdn.net/images/dashboards-app-dashboard-timeframe-calendar-b05d935595.svg "Calendar") to select calendar dates
     + Edit the resulting **From** and **To** settings to fine-tune the range

When you change the global timeframe:

* The new timeframe is displayed in the upper-right corner of the dashboard.
* The dashboard contents are recalculated and displayed according to the new timeframe. This overrides the default dashboard timeframe.
* This does not affect any tile-specific timeframe overrides. Tile-specific timeframes take precedence over any global timeframe settings.

#### Default dashboard timeframe

To set a default timeframe for a dashboard

1. Display the dashboard.
2. In the upper-right corner of the dashboard, select  **Settings**.
3. Turn on **Custom timeframe**.
4. Select the default timeframe for the selected dashboard.

   Changing this setting does not immediately update the timeframe of the current dashboard. The change is applied only to a new session with the dashboard (either for a different user, or for the same user returning to the dashboard for another session).

#### Tile-specific timeframe override

To specify a custom timeframe in a dashboard tile

1. Edit the tile.
2. In the edit panel, turn on **Custom timeframe**.
3. Select the timeframe to apply to the selected tile.

   This timeframe overrides the dashboard timeframe set in the upper-right corner of the dashboard. Using this method, a dashboard can have multiple tiles, where each tile has its own timeframe.

You can also specify a custom timeframe in a data tile's DQL query. If you use this method (with a timeframe specified in the query), the above UI setting is disabled and the timeframe specified in the query is used.

Example timeframe specification in DQL:

```
fetch [recordtype], from:now() - 2h



| ....
```

For details on specifying a timeframe in DQL, see [Specify timeframe](/docs/platform/grail/dynatrace-query-language/dql-guide#specifytimeframe "Find out how DQL works and what are DQL key concepts.") in the DQL documentation.

### Select segments

To filter data, you can specify segments at two levels: dashboard and tile. Tile-level segment selections override dashboard-level segment selections.

Should I use segments or variables?

#### Segments

Use segments when you want to reuse them across dashboards. For example, use segments for recurring filters such as for your Kubernetes clusters, namespaces, workloads, or pods. Segments automatically apply on top of the queries of your tiles/sections, so you donât need to reference them within.

#### Variables

If you need more control over how a filter is applied, however, you might want to use variables.

* Variables allow you to fully control the underlying query or within your Explore section or tile, determining where and how they are applied. For example, you can specify how they connect with other filters applied (**AND**, **OR**) and you can control which operator is used for your filter (such as `equals`, `contains`, `startsWith`, and `endsWith`).
* Additionally, use variables when you need fine-grained control over how filters are interdependent.

* For details on segments, see [Segments](/docs/manage/segments "Segments logically structure monitoring data in Grail and function as convenient filters for data that users are allowed to access based on permissions.")
* For a ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**-specific segments use case, see [Analyze monitoring data with segments](/docs/manage/segments/getting-started/segments-getting-started-analyze-monitoring-data "Learn how to analyze monitoring data more efficiently by using segments in Dashboards.")

#### Dashboard-level segments

To select dashboard-level segments

1. Display the dashboard.
2. Open the segment selector  at the top of the dashboard and, in **Filter by segments**, select a segment.  
   If the segment requires an additional value selection, select it now.
3. To add another segment, select  **Segment**. Repeat this step for each segment you want to add.
4. Select **Apply** to apply the selection and filter data on the dashboard.

   * The segment selector  now displays the name of the selected segment or, if you select more than one segment, the number of selected segments.
   * To change your segment selection, select  again, make your changes, and select **Apply**.
   * To manage segments in general (list, create, view, edit, delete), select  and then select the **Manage segments** link.

#### Tile-level segments

To select tile-level segments

1. Display the dashboard.
2. Select the tile and then select  in the tile controls to edit the tile.
3. In the edit panel, turn on **Custom segments**.
4. In the **Custom segments** list, select a segment.  
   If the segment requires an additional value selection, select it now.
5. To add another segment, select  **Segment**. Repeat this step for each segment you want to add for the selected tile.
6. Select **Apply** to apply the selection and filter data on the tile.

   * The segment selector  now displays the name of the selected segment or, if you select more than one segment, the number of selected segments.
   * To change your segment selection, select  again, make your changes, and select **Apply**.
   * To manage segments in general (list, create, view, edit, delete), select  and then select the **Manage segments** link.

### Dashboard settings

Чтобы просмотреть или изменить настройки, применяемые ко всей панели мониторинга

1. Отобразите панель мониторинга.
2. В правом верхнем углу панели мониторинга выберите **Settings** (Настройки).

   Отображается панель **Settings**.
3. Просмотрите или измените настройки по мере необходимости.

   Custom timeframe (Настраиваемый временной интервал)

   Чтобы установить временной интервал по умолчанию для панели мониторинга

   1. Отобразите панель мониторинга.
   2. В правом верхнем углу панели мониторинга выберите **Settings**.
   3. Включите **Custom timeframe**.
   4. Выберите временной интервал по умолчанию для выбранной панели мониторинга.

      Изменение этой настройки не обновит немедленно временной интервал текущей панели мониторинга. Изменение применяется только к новой сессии с панелью мониторинга (либо для другого пользователя, либо для того же пользователя, возвращающегося к панели мониторинга для другой сессии).

   Подробности о временных интервалах панели мониторинга см. в разделе [Select the timeframe](#dashboard-timeframe).

   Default segment (Сегмент по умолчанию)

   Чтобы просмотреть или изменить сегмент панели мониторинга по умолчанию

   1. Отобразите панель мониторинга.
   2. В правом верхнем углу панели мониторинга выберите **Settings**.
   3. Включите **Default segment**.
   4. Выберите сегмент по умолчанию для выбранной панели мониторинга.

      Изменение этой настройки не обновит немедленно сегмент текущей панели мониторинга. Изменение применяется только к новой сессии с панелью мониторинга (либо для другого пользователя, либо для того же пользователя, возвращающегося к панели мониторинга для другой сессии).

   Подробности о сегментах панели мониторинга см. в разделе [Select segments](#segment).

   {$} Variables (Переменные {$})

   Чтобы просмотреть или изменить переменные панели мониторинга

   1. Отобразите панель мониторинга.
   2. В правом верхнем углу панели мониторинга выберите **Settings**.

      Отображается панель **Settings**.
   3. Выберите **Variables**.

   Подробности о переменных панели мониторинга см. в разделе [Add a variable to a dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-variable "Add variables to your Dynatrace dashboards.").

### Run a code tile (Запуск плитки кода)

При открытии документа от другого пользователя вы можете увидеть следующее сообщение:

`This dashboard contains custom code. It is read-only until you review the code and select â€œAccept and runâ€ .` (Эта панель мониторинга содержит пользовательский код. Она доступна только для чтения, пока вы не просмотрите код и не выберете â€œAccept and runâ€ .)

При запуске плитки кода или раздела, написанного другим человеком, Dynatrace выполняет JavaScript этого человека, используя вашу учетную запись и ваши разрешения. Это мощная функция, но ее необходимо использовать правильно и ответственно. JavaScript-код может получать доступ к внешним APIs от вашего имени (используя вашу учетную запись и разрешения).

Чтобы просмотреть код

1. Выберите **Review all code**. (Просмотреть весь код).

   Страница **Review code** отображает код каждой плитки кода в отдельном блоке.
2. Просмотрите код и решите, хотите ли вы его запустить.

   Если вы хотите запустить код, вы можете одобрить его только для этого раза или навсегда.

   * Чтобы запустить код только для этого раза, выберите **Accept and run**. (Принять и запустить). В следующий раз, когда вы откроете этот документ, вам снова будет предложено просмотреть код перед его запуском.
   * Чтобы навсегда принять код в этом документе, выберите **Always trust code in this document** (Всегда доверять коду в этом документе) и затем выберите **Accept and run**.

### Download result (Загрузка результата)

Чтобы загрузить (экспортировать) результат текущей плитки панели мониторинга или раздела блокнота в локальный файл

1. Выберите плитку или раздел.
2. На панели команд откройте меню и выберите **Download result** (Загрузить результат) > [format] (формат).

   Доступные варианты формата зависят от визуализации.

   * **CSV**: Результат загружается в локальный файл значений, разделенных запятыми (\*.csv). Этот вариант включает форматирование таблицы, такое как видимые столбцы и форматирование единиц измерения.
   * **CSV (raw)**: Результат загружается в локальный файл значений, разделенных запятыми (\*.csv). Этот вариант включает полные неформатированные данные.
   * **JSON**: Результат загружается в локальный JSON (\*.json) файл.

   Некоторые визуализации не предлагают возможности загрузки результата.

#### Possible issue with importing CSV into Excel (Возможная проблема с импортом CSV в Excel)

При экспорте результатов в CSV-файл — будь то **CSV** или **CSV (raw)** — с переносами строк в любом столбце/поле результата, а затем открытии файла в Microsoft Excel или попытке преобразования файла в таблицу с помощью опции Excel **Data** (Данные) > **Text to Columns** (Текст по столбцам), вы можете столкнуться с проблемой, при которой переносы строк отображаются в Excel неправильно. Это вызвано ограничением Excel.

Чтобы избежать этой проблемы, используйте опцию Excel **Data** (Данные) > **From Text/CSV**.

## Manage dashboards (Управление панелями мониторинга)

### Add dashboard to Dock (Добавление панели мониторинга в Dock)

Чтобы добавить панель мониторинга в Dock для быстрого доступа

1. Отобразите панель мониторинга.
2. Откройте меню рядом с названием панели мониторинга (в левом верхнем углу панели мониторинга).
3. Выберите **Add to dock**. (Добавить в Dock).

   Если вы измените название панели мониторинга, оно автоматически обновится в Dock.

Чтобы удалить панель мониторинга из Dock

1. Наведите курсор на название панели мониторинга в Dock.
2. Выберите **Unpin from dock**. (Открепить от Dock).

### Rename a dashboard (Переименование панели мониторинга)

Чтобы переименовать панель мониторинга из панели **Dashboards**

1. Перейдите по ссылке ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.

   В разделе **Last opened by you** (Недавно открытые вами) перечислены ваши наиболее часто используемые панели мониторинга.
2. Наведите курсор на название панели мониторинга, которую вы хотите переименовать, и выберите > **Rename**. (Переименовать). Если опция переименования недоступна, у вас нет прав на редактирование этой панели мониторинга.

### Duplicate a dashboard (Дублирование панели мониторинга)

Чтобы дублировать панель мониторинга из панели **Dashboards**

1. Перейдите по ссылке ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.

   В разделе **Last opened by you** (Недавно открытые вами) перечислены ваши наиболее часто используемые панели мониторинга.
2. Наведите курсор на название панели мониторинга, которую вы хотите дублировать, и выберите > **Make a copy**. (Создать копию).

Чтобы сделать копию текущей панели мониторинга

1. В верхней части панели мониторинга откройте меню панели мониторинга рядом с названием панели мониторинга.
2. Выберите **Duplicate** (Дублировать) из меню.

   Создается копия с названием **Copy of** (Копия) + названием текущей панели мониторинга. Копия теперь отображается в панели **Dashboards**.

### Share a dashboard (Предоставление доступа к панели мониторинга)

Если вы являетесь владельцем панели мониторинга или блокнота, вы можете поделиться им.

Существует три способа поделиться документом с другими пользователями Dynatrace в вашей компании:

* **Access for all (view-only)** (Доступ для всех (только для просмотра)): Предоставьте доступ только для просмотра всем пользователям в вашей среде Dynatrace.
* **Share access** (Предоставление доступа): Создайте и поддерживайте список пользователей и групп пользователей с доступом к документу.
* **Share links** (Предоставление ссылок): Создайте ссылки (URL-адреса), указывающие на ваш документ, и распространяйте ссылки по выбранным каналам (например, по электронной почте).

Эти методы не являются взаимоисключающими. Например, вы можете поддерживать сфокусированный список пользователей для постоянного доступа к документу (возможно, все в определенной группе регулярно редактируют документ) и создавать и распространять ссылки только для просмотра для более широкой аудитории по мере необходимости.

В любом случае вы контролируете, могут ли люди редактировать документ или только просматривать его.

Подробности о предоставлении доступа к документам см. в разделе [Share documents](/docs/discover-dynatrace/get-started/dynatrace-ui/share "Share Dynatrace documents (dashboards, notebooks, and launchpads) with other Dynatrace users in your company.").

### Manage dashboard versions (Управление версиями панели мониторинга)

Версии панели мониторинга сохраняются автоматически.

* Вы можете получить доступ к 50 последним версиям вашей панели мониторинга.
* Каждая версия панели мониторинга доступна до 30 дней.

Чтобы просмотреть и управлять версиями панели мониторинга

1. Отобразите свою панель мониторинга.
2. В правом верхнем углу вашей панели мониторинга выберите ![History](https://dt-cdn.net/images/history-icon-dc67cc1e2c.svg "History"). (История).

   Это отображает меню последних версий текущей панели мониторинга.

   * Дата
   * Время
   * Имя человека, создавшего эту версию
3. Из любой записи версии в меню **Versions** (Версии) вы можете выбрать действия, относящиеся к версии.

   * ![Preview](https://dt-cdn.net/images/icon-preview-1-138a2e67eb.svg "Preview") **Preview** (Предварительный просмотр) отображает предварительный просмотр выбранной версии.
   * **Restore** (Восстановить) переключает вашу панель мониторинга на выбранную версию.
   * **Make a copy** (Создать копию) создает новую панель мониторинга из выбранной версии и отображает новую панель мониторинга. Оригинальная панель мониторинга остается неизменной.
   * **Download** (Загрузить) сохраняет JSON файл выбранной версии панели мониторинга на ваш локальный компьютер.
   * **Preview in new tab** (Предварительный просмотр в новой вкладке) отображает предварительный просмотр выбранной версии в новой вкладке браузера.
   * **Delete this version** (Удалить эту версию) удаляет выбранную версию.
4. Чтобы отобразить и управлять всеми версиями панели мониторинга в отдельном окне, перейдите в нижнюю часть меню **Versions** и выберите **Show all**. (Показать все).

Подробности см. в разделе [Manage document versions](/docs/analyze-explore-automate/dashboards-and-notebooks/document-version "View and manage versions of documents created in Dynatrace Notebooks and Dashboards.").

### Change dashboard owner (Смена владельца панели мониторинга)

При создании документа (панели мониторинга или блокнота) вы являетесь владельцем. Чтобы передать право собственности на документ другому пользователю Dynatrace

1. Откройте меню документа и выберите **Change owner**. (Сменить владельца).
2. Найдите и выберите нового владельца, а затем выберите **Change owner**.

   После смены владельца документа вы немедленно потеряете к нему доступ.

   * Убедитесь, что вы готовы передать право собственности, прежде чем выбирать эту команду.
   * Вы можете восстановить доступ к документу только в том случае, если новый владелец предоставит вам разрешение.
3. После завершения передачи новый владелец получит электронное письмо об изменении права собственности на документ.

### Download a dashboard (Загрузка панели мониторинга)

Чтобы скачать (экспортировать) текущую отображаемую панель управления как JSON

1. В верхней части панели управления откройте меню справа от названия панели управления.
2. Выберите **Download** (Загрузить) из меню.

   Определение текущей панели управления скачивается в локальный JSON файл.

Чтобы скачать (экспортировать) панель управления из боковой панели ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** (Панели управления)

1. Перейдите в ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** (Панели управления).
2. В разделе **Last opened by you** (Недавно открытые вами) наведите курсор на название панели управления, которую хотите экспортировать, и выберите **Download** (Загрузить) из меню. Панель управления скачивается в локальный JSON файл, который можно загрузить.

   Если ваша панель управления не отображается в разделе **Last opened by you** (Недавно открытые вами), выберите **All dashboards** (Все панели управления), чтобы отобразить таблицу всех панелей управления, к которым у вас есть доступ (ваши панели управления или панели управления, которыми поделились с вами). Там вы можете найти панель управления и выбрать **Download** (Загрузить) из меню.

### Загрузка панели управления

Чтобы загрузить (импортировать) определение JSON панели управления из боковой панели **Dashboards** (Панели управления)

1. Перейдите в ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** (Панели управления).
2. В панели **Dashboards** (Панели управления) слева выберите **Upload** (Загрузить).
3. Найдите и откройте файл определения JSON панели управления.

Чтобы загрузить (импортировать) определение JSON панели управления из таблицы **Dashboards** (Панели управления)

1. Перейдите в ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** (Панели управления).
2. В панели **Dashboards** (Панели управления) слева выберите **All dashboards** (Все панели управления).

   Таблица **Dashboards** (Панели управления) отображает все панели управления по **Name** (Названию) и дате **Last modified** (Последнего изменения).
3. В верхнем левом углу страницы выберите **Upload** (Загрузить).
4. Найдите и откройте файл определения JSON панели управления.

Загруженная панель управления:

* Открывается в Dynatrace.

  Если при загрузке панели управления вы видите сообщение о запуске пользовательского кода, обратитесь к [Run code warnings](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-code#run-code-warnings "Add code to your Dynatrace dashboards.") (Предупреждения о запуске кода) для получения дополнительной информации.
* Добавляется в ваш список **Last opened by you** (Недавно открытые вами).
* Добавляется на страницу **Dashboards** (Панели управления) с датой **Last modified** (Последнего изменения), установленной на дату и время загрузки.

### Удаление панели управления

Чтобы удалить любую панель управления на странице **Dashboards** (Панели управления)

1. Перейдите в ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** (Панели управления).
2. В панели **Dashboards** (Панели управления) слева выберите **All dashboards** (Все панели управления).

   Таблица отображает все панели управления по **Name** (Названию) и дате **Last modified** (Последнего изменения).
3. На странице **Dashboards** (Панели управления) выберите **Move to trash** (Переместить в корзину) для панели управления, которую хотите удалить.

### Панели управления через API: лучшие практики

При создании или управлении панелями управления через API эти лучшие практики могут облегчить вашу жизнь.

* Чтобы получить надежный старт, создайте панель управления в приложении ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** (Панели управления), а затем [скачайте](#dashboards-download) файл конфигурации панели управления.
* Чтобы проверить изменения, внесенные через API, [загрузите](#dashboards-upload) файл в ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** (Панели управления). Все ли по-прежнему выглядит так, как ожидалось?
* Будьте осторожны с изменениями макета, так как пустые вертикальные пространства автоматически сдвигают плитки вверх при загрузке документа и вызывают появление кнопки **Discard changes** (Отменить изменения).
* Чтобы подробно изучить изменения, выберите **Save as new** (Сохранить как новый), чтобы скачать документ и сравнить его с исходной версией.
* Не устанавливайте свойство `version` конфигурации на произвольное значение. Это внутреннее свойство, необходимое для целей миграции.

## Создание и редактирование панелей управления

### Создание панели управления

Самый быстрый и простой способ изучить свои данные — использовать наши новые плитки и разделы [Explore](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data "Explore your data with our point-and-click interface.") (Исследование). Всего за несколько секунд вы можете найти и проанализировать свои журналы, метрики или бизнес-события. Не требуется DQL!

Чтобы создать новую панель управления

1. Перейдите в ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** (Панели управления).
2. Выберите **Dashboard** (Панель управления).

После создания пустой панели управления необходимо добавить на нее плитки.

* Query Grail
* Add code (Добавить код)
* Add Markdown (Добавить Markdown)
* Add a variable (Добавить переменную)
* Add a snippet (Добавить фрагмент)

### Query Grail

Чтобы выполнить Query Grail

1. В верхнем правом углу панели управления выберите **Add** (Добавить) > **DQL**.

   Сочетание клавиш: **Shift**+**D**

   ![Dashboards: Add tile button (Plus)](https://dt-cdn.net/images/updated-dashboards-add-tile-button-481-c21ba8f200.png)

   Открывается боковая панель конфигурации справа с двумя вкладками:

   * **Data** (Данные)
   * **Visual** (Визуализация)
2. На вкладке **Data** (Данные) используйте [Dynatrace Query Language (DQL)](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") (Язык запросов Dynatrace) для определения вашего запроса.
3. Выберите **Run** (Выполнить), чтобы выполнить запрос.
4. На вкладке **Visual** (Визуализация) выберите формат [визуализации](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.") (Создание, редактирование и просмотр визуализаций на ваших панелях управления и блокнотах) для ваших результатов.

   * означает, что тип визуализации недоступен для вашего запроса.
5. Под селектором **Visualization** (Визуализация) разверните разделы параметров, чтобы настроить параметры визуализации по мере необходимости.
6. Закройте боковую панель, когда закончите.

   Если вы хотите вернуться к этим настройкам, выберите свою плитку, чтобы отобразить их.

Подробности см. в разделе [Add data to a dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-data "Add data to your Dynatrace dashboards.") (Добавление данных на панель управления).

### Add code (Добавить код)

Чтобы добавить код на панель управления

1. В верхнем правом углу панели управления выберите **Add** (Добавить) > **Code** (Код).

   Сочетание клавиш: **Shift**+**C**

   ![Dashboards: Add tile button (Plus)](https://dt-cdn.net/images/updated-dashboards-add-tile-button-481-c21ba8f200.png)

   На панель управления добавляется пустая плитка, и справа открывается боковая панель **Options** (Параметры).
2. Необязательно В поле **Tile title** (Название плитки) введите название, которое будет отображаться в верхней части плитки.
3. В пронумерованном поле **Code** (Код) введите пользовательский JavaScript для получения внешних данных из любого доступного API. Используйте [Fetch APIï»¿](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) (Получение данных из внешних источников) для получения данных из внешних API.

   Чтобы ваши запросы не блокировались, попросите вашего администратора разрешить ваши внешние источники данных, добавив их в **External requests** (Внешние запросы).

   External requests (Внешние запросы) обеспечивают исходящие сетевые подключения из вашей среды Dynatrace к внешним службам. Они позволяют вам контролировать доступ к общедоступным конечным точкам из AppEngine с помощью функций приложений и функций в Dashboards (Панели управления), Notebooks (Блокноты) и Automations (Автоматизация).

   1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** (Настройки) > **General** (Общие) > **External requests** (Внешние запросы).
   2. Выберите **New host pattern** (Новый шаблон хоста).
   3. Добавьте доменные имена.
   4. Выберите **Add** (Добавить).

   Таким образом, вы можете детально контролировать веб-службы, к которым могут подключаться ваши функции.

   Не включайте префикс адреса. Например, если адрес `https://some.service.org`, просто добавьте `some.service.org`.

Подробности см. в разделе [Add code to a dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-code "Add code to your Dynatrace dashboards.") (Добавление кода на панель управления).

### Add markdown (Добавить Markdown)

Чтобы добавить плитку Markdown на панель управления

1. В верхнем правом углу панели управления откройте меню **Add** (Добавить) и выберите **Add markdown** (Добавить Markdown).

   Сочетание клавиш: **Shift**+**M**

   ![Dashboards: Add tile button (Plus)](https://dt-cdn.net/images/updated-dashboards-add-tile-button-481-c21ba8f200.png)

   Открывается боковая панель **Options** (Параметры).
2. В боковой панели **Options** (Параметры) введите свой текст.

   * Используйте Markdown для форматирования текста и добавления ссылок и изображений.
   * Плитка обновляется по мере редактирования.
   * Во время редактирования текста нажмите Ctrl+Space, чтобы увидеть параметры.
3. Закройте боковую панель **Options** (Параметры), когда закончите.

Подробности см. в разделе [Add Markdown to dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-markdown "Add Markdown-formatted annotations to your Dynatrace dashboards.") (Добавление аннотаций в формате Markdown на ваши панели управления Dynatrace).

### Add variable (Добавить переменную)

Используйте переменные для фильтрации ваших панелей мониторинга, чтобы они выступали в качестве значений переменных в кодовых плитках и в качестве плейсхолдеров в названиях плиток и тексте Markdown-плиток.

Чтобы добавить переменную к панели мониторинга

1. В заголовке панели мониторинга откройте меню и выберите **Переменные**.
   Клавишная комбинация: **Shift**+**V**

   Клавишная комбинация: **Shift**+**V**

   ![Панели мониторинга: Кнопка добавления плитки (Плюс)](https://dt-cdn.net/images/updated-dashboards-add-tile-button-481-c21ba8f200.png)

   Отображается панель **Переменная**.
2. Определите переменную.

   * **Имя**: имя переменной.

     + Разрешены только алфавитно-цифровые значения
     + Не начинайте имя переменной с `dt_`
   * **Тип**: может быть одним из следующих:

     + **DQL**: значение возвращается из запроса, который вы вводите при определении переменной.

       - Выберите **Выполнить**, чтобы протестировать ваш запрос.
     + **Код**: значение возвращается из кода, который вы вводите при определении переменной.
     + **Список**: список значений, разделенных запятыми (CSV).

       - Чтобы определить возможные значения, введите их (разделенные запятыми) в поле под **Данные**.
       - Чтобы определить значение по умолчанию, выберите одно из списка **Значение по умолчанию**.
       - Чтобы разрешить выбор нескольких значений одновременно, включите **Множественный выбор**.
     + **Свободный текст**: свободный текст. Вы можете ввести **Значение по умолчанию**.
       Ваши изменения сохраняются автоматически.
3. Установите **Параметры отображения**.

   * Если выпадающий список переменной должен отображаться на панели мониторинга, включите **Отображать как фильтр на панели мониторинга**.  
     Выключите его, когда вы хотите скрыть его, например, когда переменная используется в качестве статического значения во всех плитках, но не должна отображаться пользователю панели мониторинга.
   * Если пользователям следует разрешить выбирать несколько значений одновременно в выпадающем списке переменной, включите **Множественный выбор**.  
     Выключите его, когда вы хотите использовать только одиночные значения выпадающего списка переменной.
   * Выберите **Значение по умолчанию** для выпадающего списка переменной. Если вы не введете ничего в этом поле, будет выбрано первое доступное значение.
4. Когда вы закончите, выберите **< Переменная** вверху, чтобы перейти к панели **Переменные**, или выберите , чтобы закрыть панель **Переменные**.

Переменные в панелях мониторинга могут быть определены так, чтобы зависеть от других переменных.

* Значение переменной пересчитывается, если ее определение ссылается на другую переменную и значение другой переменной изменяется.

  Например, если значение переменной A изменяется, значение любой переменной, определение которой ссылается на переменную A, пересчитывается.
* Циклы не допускаются.

  Например, если значение переменной A зависит от значения переменной B, значение переменной B не может зависеть от значения переменной A.

Для подробностей см. [Добавление переменной к панели мониторинга](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-variable "Добавьте переменные к вашим Dynatrace панелям мониторинга.").

### Добавить фрагмент

Чтобы начать работу на основе фрагмента

1. В правом верхнем углу панели мониторинга выберите **Добавить**, чтобы открыть меню **Добавить**.

   Клавишная комбинация: **Ctrl**/**Cmd**+**Shift**+**Enter**

   ![Панели мониторинга: Кнопка добавления плитки (Плюс)](https://dt-cdn.net/images/updated-dashboards-add-tile-button-481-c21ba8f200.png)
2. Прокрутите вниз до раздела **Начать с фрагмента** и выберите один из фрагментов. В этом примере мы выбираем фрагмент **Получить журналы**, который отображается в панели предварительного просмотра.

   ![Пример: выберите фрагмент "Получить журналы".](https://dt-cdn.net/images/add-snippet-menu-example-fetch-logs-754-d4435c09eb.png)
3. После выбора фрагмента панель редактирования отображает добавленный фрагмент.

   ![Пример: фрагмент "Получить журналы" добавлен.](https://dt-cdn.net/images/add-snippet-menu-example-fetch-logs-result-1436-77cc9fa8f1.png)
4. Отредактируйте запрос или код (в зависимости от типа фрагмента, который вы выбрали) и настройки визуализации по мере необходимости.
5. Выберите **Выполнить**, чтобы увидеть результаты.
6. Закройте боковую панель, когда закончите.

Для подробностей см. [Добавление фрагмента к панели мониторинга](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-snippet "Начните с фрагмента").

### Анализ данных с помощью ИИ

Для анализа данных с использованием Dynatrace Intelligence Data Analyzers

1. Изучите временной ряд.

   Пример

   В вашем документе (панели мониторинга или блокноте)

   1. Выберите  чтобы добавить новый раздел или плитку, а затем выберите **Metrics** (Метрики) для изучения метрик.

      ![Пример: выберите Add > Metrics](https://dt-cdn.net/images/example-select-explore-metrics-637-025cadac69.png)
   2. В **Select metric** (Выберите метрику) выберите **Infrastructure** (Инфраструктура) > **CPU** (ЦП) > **CPU usage %** (Загрузка ЦП в процентах).

      ![Пример: выберите метрику "CPU usage %"](https://dt-cdn.net/images/example-select-metric-cpu-usage-percent-771-a672aa20e2.png)
   3. Установите **Split by** (Разделить по) на `host.name`.

      ![Пример: установите "Split by" на host.name](https://dt-cdn.net/images/example-select-host-name-743-5bd89ea6a3.png)
   4. Установите **Limit** (Лимит) на максимальное количество серий для анализа. Dynatrace Intelligence Data Analyzer в настоящее время поддерживает анализ до 1000 серий.

   В результате вы должны получить что-то вроде этого:

   ![Пример: завершенный запрос](https://dt-cdn.net/images/example-complete-query-737-dfa24f730d.png)
2. Запустите запрос.
3. На панели опций справа прокрутите вниз и разверните **Davis AI**.

   Показать мне

   ![Пример выбора настроек Analyze and alert (Анализ и оповещение) в приложении Dashboards.](https://dt-cdn.net/images/dashboards-select-analyze-and-alert-settings-746-7155ef9415.png)

   ![Начальная панель настроек Analyze and alert (Анализ и оповещение) в приложении Dashboards.](https://dt-cdn.net/images/dashboards-analyze-and-alert-details-746-8d503491c8.png)
4. На панели **Davis AI** установите **Analyzers** (Анализаторы) на нужный анализатор, а затем настройте анализатор.

   * Для обзора обнаружения аномалий см. [Обнаружение аномалий](/docs/dynatrace-intelligence/anomaly-detection "Как Dynatrace обнаруживает аномалии в вашей среде.")
   * Для получения подробной информации о настройках обнаружения аномалий см. [Конфигурация обнаружения аномалий](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#analyzer "Как настроить оповещение об отсутствующих измерениях.")

   * Для получения подробной информации о настройках анализа прогнозов см. [Dynatrace Intelligence predictive AI analysis](/docs/dynatrace-intelligence/reference/ai-models/forecast-analysis "Узнайте, как Dynatrace Intelligence predictive AI генерирует прогнозы.")

   Обнаружение аномалий: Адаптивное пороговое обнаружение аномалий

   * **Number of signal fluctuations** (Количество колебаний сигнала) — количество раз, которое колебание сигнала добавляется к базовому уровню для получения фактического порога для оповещения.
   * **Alert condition** (Условие оповещения) — ваш выбор зависит от того, хотите ли вы узнать, когда метрика выше, ниже или за пределами (выше или ниже) нормального диапазона.

   Для получения подробной информации см. [Конфигурация обнаружения аномалий](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#analyzer "Как настроить оповещение об отсутствующих измерениях.").

   Обнаружение аномалий: Сезонное базовое обнаружение аномалий

   * **Tolerance** (Допуск) — чем выше допуск, тем шире полоса доверия, что приводит к меньшему количеству сработанных событий.
   * **Alert condition** (Условие оповещения) — ваш выбор зависит от того, хотите ли вы узнать, когда метрика выше, ниже или за пределами (выше или ниже) нормального диапазона.

   Для получения подробной информации см. [Конфигурация обнаружения аномалий](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#analyzer "Как настроить оповещение об отсутствующих измерениях.").

   Обнаружение аномалий: Статическое пороговое обнаружение аномалий

   * **Threshold** (Порог) — жесткое ограничение, которое метрика не должна нарушать.
   * **Unit** (Единица измерения) — единица измерения значения.
   * **Alert condition** (Условие оповещения) — ваш выбор зависит от того, хотите ли вы узнать, когда метрика выше или ниже порогового значения.
   * **Suggest threshold** (Предложить порог) — Davis AI может помочь вам найти правильный порог на основе исторических данных.

   Для получения подробной информации см. [Конфигурация обнаружения аномалий](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#analyzer "Как настроить оповещение об отсутствующих измерениях.").

   Прогноз: Forecast (Прогноз)

   * **Data points to predict** (Количество точек данных для прогнозирования) — общее количество шагов, на которые прогнозируется временной ряд. Большее количество шагов обычно приводит к менее надежным прогнозам и более длительному времени выполнения анализатора.
   * **Forecast offset** (Смещение прогноза) — смещение для начала прогноза. Например, если смещение установлено на `2`, последние две точки данных игнорируются, и возвращается прогноз для этих точек.

   Для получения подробной информации см. [Dynatrace Intelligence predictive AI analysis](/docs/dynatrace-intelligence/reference/ai-models/forecast-analysis "Узнайте, как Dynatrace Intelligence predictive AI генерирует прогнозы.").

   Дополнительные настройки (для обнаружения аномалий)

   Вы можете использовать значения по умолчанию или включить **Show advanced properties** (Показать дополнительные свойства), чтобы точно настроить эти параметры.

   * **Alert on missing data** (Оповещать об отсутствии данных) — оповещать, если данные не обнаружены в течение скользящего окна.
   * **Violating samples** (Нарушающие выборки) — количество выборок в скользящем окне, которые должны нарушить, чтобы вызвать событие.
   * **Sliding window** (Скользящее окно) — количество выборок, составляющих скользящее окно.
   * **Dealerting samples** (Выборки для снятия оповещения) — количество выборок в скользящем окне, которые должны вернуться к нормальному состоянию, чтобы закрыть событие.
5. По умолчанию анализатор не включен. Чтобы включить его, переключите переключатель в верхней части панели редактирования (переключитесь с **AI data analysis is not active** (Анализ данных ИИ не активен) на **AI data analysis is active** (Анализ данных ИИ активен)).
6. Чтобы просмотреть результаты, выберите визуализацию **Davis AI analysis** (анализ) и разверните раздел **Davis AI analysis chart** (диаграмма анализа), чтобы просмотреть или изменить параметры визуализации.

   Показать мне

   ![Пример выбора визуализации "AI analysis" и отображения параметров визуализации в приложении Notebooks.](https://dt-cdn.net/images/notebooks-ai-analysis-visualizations-757-4cf3f48b3c.png)

   Визуализация **Davis AI analysis** имеет два раздела: chart (диаграмма) и visualization (визуализация). Вы можете использовать настройку **Visible sections** (Видимые разделы), чтобы отобразить один или оба из них.

   * **All** (Все) — показать диаграмму и таблицу. Диаграмма отражает ваши выборы в таблице.
   * **Table** (Таблица) — показать только таблицу. Вы можете сортировать столбцы, которые отображают значок сортировки  в заголовке. Выберите заголовок столбца, чтобы переключить порядок сортировки вверх  или вниз .
   * **Chart** (Диаграмма) — показать только диаграмму. Используйте таблицу, чтобы выбрать записи, которые вы хотите отобразить на диаграмме.

#### Пример: аномальная загрузка ЦП в процентах

Чтобы обнаружить, когда загрузка ЦП в процентах превышает 70 процентов, в вашем документе (панели мониторинга или блокноте)

1. Выберите  чтобы добавить новый раздел или плитку, а затем выберите **Metrics** (Метрики) для изучения метрик.

   Показать мне

   ![Пример: выберите Add > Metrics](https://dt-cdn.net/images/example-select-explore-metrics-637-025cadac69.png)
2. В **Select metric** (Выберите метрику) выберите **Infrastructure** (Инфраструктура) > **CPU** (ЦП) > **CPU usage %** (Загрузка ЦП в процентах).

   Показать мне

   ![Пример: выберите метрику "CPU usage %"](https://dt-cdn.net/images/example-select-metric-cpu-usage-percent-771-a672aa20e2.png)
3. Установите **Split by** (Разделить по) на `host.name`.

   Показать мне

   ![Пример: установите "Split by" на host.name](https://dt-cdn.net/images/example-select-host-name-743-5bd89ea6a3.png)
4. Установите **Limit** (Лимит) на максимальное количество серий для анализа. Davis analyzer в настоящее время поддерживает анализ до 1000 серий.

   Показать мне

   ![Пример: завершенный запрос](https://dt-cdn.net/images/example-complete-query-737-dfa24f730d.png)
5. Выберите **Run** (Запустить).
6. На панели редактирования разверните **Davis AI**.

   Показать мне

   ![Пример выбора настроек Analyze and alert (Анализ и оповещение) в приложении Dashboards.](https://dt-cdn.net/images/dashboards-select-analyze-and-alert-settings-746-7155ef9415.png)

   ![Начальная панель настроек Analyze and alert (Анализ и оповещение) в приложении Dashboards.](https://dt-cdn.net/images/dashboards-analyze-and-alert-details-746-8d503491c8.png)
7. В списке **Analyzers** (Анализаторы) выберите **Static threshold anomaly detection** (Статическое пороговое обнаружение аномалий).

   Показать мне

   ![Выбор анализатора "Static threshold anomaly detection" в настройках Analyze and alert приложения Dashboards.](https://dt-cdn.net/images/dashboards-analyze-and-alert-select-static-threshold-anomaly-detection-752-45026264f0.png)
8. Установите **Threshold** (Порог) на `70` (введите значение) и **Alert condition** (Условие оповещения) на **Alert if metric is above** (Оповещать, если метрика выше) (по умолчанию).

   Показать мне

   ![Настройка параметров анализатора "Static threshold anomaly detection" в приложении Dashboards.](https://dt-cdn.net/images/dashboards-static-threshold-anomaly-detection-settings-748-4d20c8220e.png)
9. Активируйте анализатор: в верхней части панели редактирования переключитесь с **AI data analysis is not active** (Анализ данных ИИ не активен) на **AI data analysis is active** (Анализ данных ИИ активен).
10. Чтобы просмотреть результаты, выберите визуализацию **Davis AI analysis** (анализ). Разверните раздел **Davis AI analysis chart** (диаграмма анализа), чтобы увидеть параметры визуализации.

    Показать мне

    ![Пример выбора визуализации "AI analysis" и отображения параметров визуализации в приложении Notebooks.](https://dt-cdn.net/images/notebooks-ai-analysis-visualizations-757-4cf3f48b3c.png)
11. В разделе **Davis AI analysis chart** (диаграмма анализа) установите **Visible sections** (Видимые разделы) на **All** (Все).
12. Просмотрите результаты.

    В этом примере мы выбрали хосты, которые превысили порог.

    * Диаграмма показывает линию для выбранной метрики (`CPU usage %`) для каждого выбранного хоста.
    * Красная полоса в верхней части визуализации указывает, где был превышен порог для этой метрики.
    * Таблица под диаграммой содержит выбранные хосты.

    ![Пример результатов анализатора с визуализацией "AI analysis" в приложении Notebooks.](https://dt-cdn.net/images/notebooks-ai-analysis-chart-1920-5ac0e1f854.png)

### Изменение значений переменных



If a dashboard has one or more variables, they are listed by name along the upper-left of the dashboard, under the dashboard name. When you change variable values, the dashboard contents are recalculated and displayed according to the new values.

To change the value of a variable

1. In the upper-left of the dashboard, locate the variable name.
2. Use the menu or edit box under the variable name to change the value.

   * If the variable allows just one selection (value) at a time, select the value that you want to apply to the dashboard.
   * If the variable allows multiple selections (values) at a time, select the checkbox for each value you want to apply to the dashboard. The menu name for that variable shows how many values are selected.
   * For a Free Text variable, you can edit the text in the box under the variable name.

### Copy to another document

You can copy a dashboard tile to another document (such as a different dashboard or a notebook).

For example, an easy way to start a new notebook is to copy reusable tiles from existing dashboards to a new notebook and then edit the copied sections as part of the new notebook.

To copy a dashboard tile to a notebook (as a notebook section)

1. In the dashboard, select the tile that you want to copy to a notebook.
2. Open the  menu and select ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Add to notebook**.
3. In **Select destination**:

   * If you want to create a new notebook with the selected dashboard tile as a section, select **New notebook**.
   * If you want to add the selected dashboard tile as another section in an existing notebook, select the existing notebook from the list and then select **Confirm**.

   The notebook opens with the selected tile copied into it as a notebook section.

To copy a dashboard tile to a different app (not ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**), open the  menu and select  **Open with**, and then select the target app.

For details, see [Drilldowns and navigation](/docs/analyze-explore-automate/dashboards-and-notebooks/drilldowns-and-navigation "Drill down from Dashboards and Notebooks using links based on intents or URLs.").

### Edit a tile

To edit a tile

1. Select the tile to display the tile-specific commands.
2. Select  **Edit**.

   An **Options** panel opens on the right to display the tile or section configuration.
3. Select and drag the expander control left or right as needed to resize the **Options** panel for a better look at the code.

   ![Resize options panel](https://dt-cdn.net/images/options-panel-resize-155-a8c92d2683.png)

### Add or edit a tile title

You can add a title to any dashboard tile (except for a Markdown tile).

Regardless of the title setting, a title bar is automatically created as needed to display tile indicators such as for a warning or to indicate a custom tile timeframe.

1. Select the tile and  edit it.

   * The title is displayed in the box at the top of the tile edit panel.
   * If the tile has no title, the box displays `Untitled tile`.
2. Edit the title. Your edits are displayed as you type.

   A title can include emojis (such as ð and ð and â¤ï¸) and variables.

   **Example:**

   1. In your dashboard, define [variables](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-variable "Add variables to your Dynatrace dashboards.") called `Status` and `Emoji`.
   2. Set the title to `Current $Emoji status is $Status`.
   3. Set variable `Status` to `Good`.
   4. Set variable `Emoji` to `ð`.

   The title will be displayed as `Current ð status is Good`, and it will update automatically when the variable values change.

To remove a tile title, select the tile and  edit it, and then clear the title box.

### Configure a tile visualization

Each visualization has visualization-specific settings.

To edit a tile visualization, see the [visualization instructions](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.").

## Layout

### Resize a tile

To resize a tile

1. Hover over the tile.
2. Select and drag  in the lower-right corner of the tile to change the dimensions of the tile.

   To help you select a specific size, the tile size is displayed on the tile command bar.

### Move a tile

You can move one tile at a time or select and move multiple tiles simultaneously.

To move a tile, drag the tile to a new position.

* If the tile has a title, select and drag  the title bar to move the tile.
* If the tile has no title, select the tile to display the tile-specific commands, and then select and drag  on the tile command bar to drag the selected tile to a new location.

  To help you align tiles, a background grid is displayed when you're moving a tile.

To move multiple tiles simultaneously

1. Select one tile.
2. Ctrl-click additional tiles that you want to move.

   * Each selected tile is highlighted.
   * The total number of selected tiles is displayed on the tile command bar.
3. Select and drag  **Move** to drag all of the selected tiles to a new location.

### Copy and paste a tile

You can copy and paste tiles to the same dashboard or another dashboard.

To copy and paste one tile

1. Select the tile to display the tile-specific commands.
2. On the tile command bar, select  **Copy to clipboard**.

   The selected tile is copied to your clipboard.
3. Paste the tile (Ctrl-V).

   * You can paste the copied tile to the current dashboard, in which case it's the equivalent of  **Duplicate**.
   * You can switch to another dashboard and paste the copied tile there.

To copy and paste multiple tiles simultaneously

1. Click one tile to select it.
2. Ctrl-click additional tiles that you want to copy and paste.

   * Each selected tile is highlighted.
   * The total number of selected tiles is displayed on the tile command bar.
3. On the tile command bar, select  **Copy to clipboard**.

   The selected tiles are copied to your clipboard.
4. Paste the tiles (Ctrl-V) to the same dashboard or switch to another dashboard and paste them there.

### Duplicate a tile

You can duplicate one tile at a time or duplicate multiple tiles simultaneously.

To duplicate one tile

1. Select the tile to display the tile-specific commands.
2. Select  **Duplicate**.

   A copy of the tile is created on the current dashboard.

To duplicate multiple tiles simultaneously

1. Click one tile to select it.
2. Ctrl-click additional tiles that you want to duplicate.

   * Each selected tile is highlighted.
   * The total number of selected tiles is displayed on the tile command bar.
3. On the tile command bar, select  **Duplicate**.

   The selected tiles are duplicated on the current dashboard.

### Split tile space to insert new tile

When laying out a dashboard, you can split the space that a tile uses on the grid, and insert a second tile next to the first tile within the same space.

* The first tile is unaffected other than that it now uses half the width or height it used before you split the space.
* The second (new) tile uses the other half of that layout space.
* This is available only when you select a single tile that is big enough to split. It's not available when you select multiple tiles, or if the size of the selected tile is too small to split.

For example, let's select a tile and add another tile to its right, so that the two tiles share the space originally used by the first tile.

1. Select the tile.
2. Hover over the tile to see the  split controlsâleft, right, and bottomâto indicate where you split that space and insert a new tile.

   ![Split a dashboard tile to insert another tile within the same space](https://dt-cdn.net/images/split-tiles-01-1515-c796df2c96.png)
3. In this example, select the  control on the right. It opens a menu similar to the  menu you would otherwise use to add a tile to the dashboard.
4. Select the tile type you want to add.
5. Edit the definition of the new tile and close the edit panel to see the changed layout.

   * The original tile is unchanged except that it now uses only the left half of the space it used before.
   * The new tile uses the right half of that space.
   * You can still adjust the tile sizes and positions manually.

### Delete a tile

You can delete one tile at a time or select and delete multiple tiles simultaneously.

To delete one tile

1. Select the tile to display the tile-specific commands.
2. On the tile command bar, select  **More actions** >  **Delete**.
3. In the **Are you sure you want to delete this tile?** message, select **Cancel** or **Delete**.

To delete multiple tiles simultaneously

1. Click one tile to select it.
2. Ctrl-click additional tiles that you want to delete.

   * Each selected tile is highlighted.
   * The total number of selected tiles is displayed on the tile command bar.
3. On the tile command bar, select  **Delete**.
4. In the **Are you sure you want to delete this tile?** message, select **Cancel** or **Delete**.