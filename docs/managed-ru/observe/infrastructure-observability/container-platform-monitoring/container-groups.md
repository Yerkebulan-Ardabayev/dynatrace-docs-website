---
title: Мониторинг групп контейнеров
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/container-platform-monitoring/container-groups
scraped: 2026-05-12T11:09:33.074893
---

# Monitor container groups

# Мониторинг групп контейнеров

* How-to guide
* 3-min read
* Updated on Apr 21, 2024

Страница обзора **Container groups** позволяет просматривать список всех контейнеров в вашей среде и фильтровать их по группе процессов, группе контейнеров или свойствам Kubernetes.

1. Перейдите в раздел **Containers**, чтобы просмотреть список всех групп контейнеров в вашей среде.

   ![Container groups overview](https://dt-cdn.net/images/screenshot-2022-09-12-at-10-13-25-1737-8388b7f687.png)

   Обзор групп контейнеров

   Таблица **Container groups** отображает свойства отдельных групп контейнеров. Таблицу можно фильтровать по:

   * **Name**: имя группы контейнеров.
   * **Image name**: имя образа, назначенного конкретной группе контейнеров Docker. Только для контейнеров Docker.
   * **K8s namespace**: пространство имён Kubernetes, которому назначены контейнеры. Только для контейнеров Kubernetes.
   * **K8s container name**: имя контейнера Kubernetes. Только для контейнеров Kubernetes.
   * **K8s pod name**: полное имя пода Kubernetes, которому принадлежит контейнер. Только для контейнеров Kubernetes.
2. Выберите группу контейнеров из таблицы, чтобы перейти на страницу обзора группы контейнеров.

   ![Container group overview](https://dt-cdn.net/images/screenshot-2022-09-12-at-10-34-05-1728-233f3fccd3.png)

   Обзор группы контейнеров

## Анализ контейнеров

Для лучшего понимания поведения контейнеров перейдите в раздел **Container analysis**. Здесь отображаются все контейнеры, назначенные выбранной группе контейнеров.

Предоставляемые метрики:

* **CPU usage, mCores**: использование CPU контейнером в миллиядрах.
* **CPU throttling, mCores**: тротлинг CPU контейнера в миллиядрах.
* **Memory usage, bytes**: размер резидентного набора (Linux) или размер частного рабочего набора (Windows) контейнера в байтах.

Выберите контейнер для перехода на страницу обзора контейнера, где можно просмотреть подробности и доступные метрики для выбранного контейнера.

Использование диаграмм

Нажмите в правом верхнем углу диаграммы, чтобы:

* **Show in Data Explorer** — открыть [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") с соответствующим запросом для более детального изучения данных, настройки параметров диаграммы и закрепления её на панели мониторинга.
* **Create metric event** — открыть [Metric events](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace") для выбранной метрики.
* **Pin to dashboard** — закрепить копию выбранной диаграммы на любой классической панели мониторинга, доступной для редактирования. Подробнее см. в разделе [Закрепление плиток на панели мониторинга](/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Learn to pin tiles to your dashboards.").

## Группы процессов

В разделе **Process groups** отображаются все группы процессов для выбранной группы контейнеров. Выберите группу процессов из таблицы для перехода на специальную страницу обзора. Подробнее см. в разделе [Обзор всех технологий в вашей среде](/managed/observe/infrastructure-observability/process-groups/monitoring/overview-of-all-technologies-running-in-my-environment "Get a summary of the performance of all the technologies in your environment.").

## События

На плитке **Events** отображается распределение [событий](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Gain an understanding of the Events section on each host, process, and service overview page."), таких как развёртывания сервисов, сбои процессов и дампы памяти. Разверните плитку для просмотра списка событий.

## Журналы

Временная шкала средства просмотра журналов является интерактивной и поддерживает глобальный выбор временного диапазона. Используйте её для выявления проблем в окрестности конкретного события журнала и анализа его связи с производительностью контейнера.

Использование диаграмм

Нажмите в правом верхнем углу диаграммы, чтобы:

* **Go to Log Viewer** — открыть [Log Viewer](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer "Learn how to use Dynatrace log viewer to analyze log data.") с фильтром по выбранной группе контейнеров.
* **Create metric** — открыть страницу [Log metrics](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics "Learn how to create and use Dynatrace log metrics to analyze log data.") с установленным в поле **Query** значением для выбранной группы контейнеров.