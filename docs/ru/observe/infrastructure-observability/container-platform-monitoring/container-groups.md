---
title: Monitor container groups
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/container-groups
scraped: 2026-03-06T21:16:48.623627
---

# Мониторинг групп контейнеров

# Мониторинг групп контейнеров

* Classic
* How-to guide
* 3-min read
* Updated on Apr 21, 2024

Страница обзора **Container groups** позволяет просматривать список всех контейнеров в вашей среде и фильтровать их по группе процессов, группе контейнеров или свойствам Kubernetes.

1. Перейдите в раздел **Containers**, чтобы получить список всех групп контейнеров в вашей среде.

   ![Container groups overview](https://dt-cdn.net/images/screenshot-2022-09-12-at-10-13-25-1737-8388b7f687.png)

   В таблице **Container groups** отображаются свойства отдельных групп контейнеров. Таблицу можно фильтровать по следующим критериям:

   * **Name**: имя группы контейнеров.
   * **Image name**: имя образа, назначенного конкретной группе контейнеров Docker. Только для контейнеров Docker.
   * **K8s namespace**: пространство имён Kubernetes, которому назначены контейнеры. Только для контейнеров Kubernetes.
   * **K8s container name**: имя контейнера Kubernetes. Только для контейнеров Kubernetes.
   * **K8s pod name**: полное имя пода Kubernetes, которому принадлежит контейнер. Только для контейнеров Kubernetes.
2. Выберите группу контейнеров из таблицы, чтобы перейти на страницу обзора группы контейнеров.

   ![Container group overview](https://dt-cdn.net/images/screenshot-2022-09-12-at-10-34-05-1728-233f3fccd3.png)

## Анализ контейнеров

Для лучшего понимания поведения контейнеров перейдите в раздел **Container analysis**. Здесь отображаются все контейнеры, назначенные выбранной группе контейнеров.

Доступные метрики включают:

* **CPU usage, mCores**: использование ЦП на контейнер в милликорах.
* **CPU throttling, mCores**: троттлинг ЦП на контейнер в милликорах.
* **Memory usage, bytes**: размер резидентного набора (Linux) или размер частного рабочего набора (Windows) на контейнер в байтах.

Выберите контейнер для перехода на страницу обзора контейнера, где можно просмотреть подробные сведения и доступные метрики выбранного контейнера.

Работа с графиками

Нажмите на значок в правом верхнем углу графика, чтобы:

* **Show in Data Explorer** — открыть [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") для соответствующего запроса, чтобы просмотреть запрос, изучить данные детальнее, настроить параметры графика и закрепить его на собственной панели мониторинга.
* **Create metric event** — открыть страницу [Metric events](/docs/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace") для выбранной метрики.
* **Pin to dashboard** — закрепить копию выбранного графика на любой классической панели мониторинга, доступной для редактирования. Например, если определённые хосты особенно важны для вашего бизнеса, создайте панель мониторинга для наблюдения только за этими хостами и закрепите на неё графики со страниц их обзора — практически без ввода текста. Подробнее см. [Pin tiles to your dashboard](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Learn to pin tiles to your dashboards.").

## Группы процессов

В разделе **Process groups** отображаются все группы процессов для выбранной группы контейнеров. Выберите группу процессов из таблицы для перехода на соответствующую страницу обзора. Дополнительные сведения см. в разделе [Overview of all technologies running in your environment](/docs/observe/infrastructure-observability/process-groups/monitoring/overview-of-all-technologies-running-in-my-environment "Get a summary of the performance of all the technologies in your environment.").

## События

На плитке **Events** отображается распределение [событий](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Gain an understanding of the Events section on each host, process, and service overview page."), таких как развёртывания сервисов, сведения об аварийном завершении процессов и дампы памяти. Разверните плитку для просмотра списка событий.

## Журналы

Временная шкала средства просмотра журналов является интерактивной и позволяет выполнять глобальный выбор временного диапазона. Используйте её для выявления проблем, связанных с конкретным событием журнала, и анализа его связи с производительностью контейнера.

Работа с графиками

Нажмите на значок в правом верхнем углу графика, чтобы:

* **Go to Log Viewer** — открыть страницу [Log Viewer](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer "Learn how to use Dynatrace log viewer to analyze log data."), отфильтрованную по выбранной группе контейнеров.
* **Create metric** — открыть страницу [Log metrics](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics "Learn how to create and use Dynatrace log metrics to analyze log data.") со значением поля **Query**, установленным для выбранной группы контейнеров.
