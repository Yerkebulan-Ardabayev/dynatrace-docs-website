---
title: Фильтрация узлов Smartscape с сегментами
source: https://www.dynatrace.com/docs/manage/segments/getting-started/segments-getting-started-filter-smartscape-nodes
scraped: 2026-03-06T21:24:58.481368
---

# Фильтрация узлов Smartscape с помощью сегментов


* Latest Dynatrace
* Tutorial
* Preview

В Smartscape на Grail можно фильтровать отслеживаемые объекты с помощью рекомендуемого блока включения `Data (all types)` или блока включения для конкретного типа объектов.

## Для кого предназначена эта статья

Статья предназначена для всех пользователей, стремящихся эффективно фильтровать данные Smartscape на Grail в различных приложениях платформы Dynatrace.

## Чему вы научитесь

В этой статье вы узнаете, как использовать сегменты для фильтрации узлов Smartscape с помощью блоков включения.

## Прежде чем начать

Предварительные знания

* Включение данных в сегменты
* Переменные в сегментах

Приложения Dynatrace, поддерживающие сегменты:

* [Dashboards ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards")](../../../analyze-explore-automate/dashboards-and-notebooks/dashboards-new.md "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.")
* [Notebooks ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks")](../../../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.")
* [Problems ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new")](../../../dynatrace-intelligence/davis-problems-app.md "Use the Problems app to quickly get to the root cause of incidents in your environment.")
* [Workflows ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")](../../../analyze-explore-automate/workflows.md "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.")
* [Distributed Tracing ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing")](../../../observe/application-observability/distributed-tracing.md "Trace and analyze in real time highly distributed systems with Grail.")
* Discovery & Coverage

Поддержка сегментов в других приложениях будет добавлена позже. Следите за обновлениями.

Предварительные требования

* Среда Dynatrace SaaS на основе Grail и AppEngine.
* У вас есть разрешение `storage:filter-segments:read`. Сведения о настройке разрешений см. в разделе Permissions in Grail.

## Фильтрация узлов Smartscape с помощью блоков включения данных

Чтобы отфильтровать узлы Smartscape с помощью блоков включения для `Data (all types)`:

1. Выберите **Settings** (Настройки) > **Environment segmentation** (Сегментация среды) > **Segments** (Сегменты).
2. Нажмите **Segment** (Сегмент), чтобы создать новый сегмент.
3. В разделе **All data** (Все данные) введите нужное условие фильтрации (например, `k8s.namespace.name = dynatrace`) в поле фильтра.
4. Нажмите **Preview** (Предварительный просмотр), чтобы просмотреть данные, соответствующие условию фильтрации.
5. Выберите **Entities** (Объекты) в списке типов данных, доступных для вашего условия фильтрации, чтобы просмотреть соответствующие узлы Smartscape.

![An example of configuring Smartscape nodes filters with segments data include blocks](https://dt-cdn.net/images/smartscape-segments-data-includes-2546-c374a90d0b.png)

## Фильтрация узлов Smartscape с помощью блоков включения объектов

Чтобы отфильтровать узлы Smartscape с помощью блоков включения для объектов:

1. Выберите **Settings** (Настройки) > **Environment segmentation** (Сегментация среды) > **Segments** (Сегменты).
2. Нажмите **Segment** (Сегмент), чтобы создать новый сегмент.
3. Нажмите **More** (Ещё) > **Entities** (Объекты), чтобы создать блок включения для объектов в сегменте.
4. В разделе **Entities** (Объекты) введите нужное условие фильтрации (например, `k8s.namespace.name = dynatrace`) в поле фильтра.
5. Нажмите **Preview** (Предварительный просмотр), чтобы просмотреть узлы Smartscape, соответствующие условию фильтрации.

![An example of configuring Smartscape nodes filters with segments entities include blocks](https://dt-cdn.net/images/smartscape-segments-entity-includes-2546-b1c7bf6b93.png)

## Заключение

Вы узнали, как создавать фильтры узлов Smartscape с помощью блоков включения сегментов для данных всех типов и объектов. Теперь вы можете использовать их для фильтрации отслеживаемых объектов в Smartscape на Grail.
