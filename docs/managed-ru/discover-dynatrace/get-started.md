---
title: Начало работы
source: https://docs.dynatrace.com/managed/discover-dynatrace/get-started
scraped: 2026-05-12T11:03:11.305200
---

# Начало работы

# Начало работы

* How-to guide
* 3-min read
* Published Dec 19, 2025

Dynatrace Managed — это локальная платформа наблюдаемости, позволяющая анализировать, автоматизировать и внедрять инновации с использованием возможностей искусственного интеллекта. Начните работу с Dynatrace Managed всего за несколько шагов.

## Приступайте к работе!

### Шаг 1 Получите лицензию Dynatrace Managed

* Для получения лицензии на Dynatrace Managed обратитесь в [Dynatrace Sales](https://dt-url.net/c901yj9). Ваш торговый представитель предоставит дополнительные сведения. Лицензирование мониторинга Dynatrace осуществляется на основе потребления различных типов единиц мониторинга, которые вы приобретаете и используете в соответствии с вашими потребностями. Подробнее см. в разделе [Лицензирование Dynatrace](/managed/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.").
* После заключения договора вы получите электронное письмо с информацией о лицензии и инструкциями по началу работы.

### Шаг 2 Настройте кластер Managed

* Выберите [модель развёртывания](/managed/managed-cluster/basics/managed-deployments "Understand how Dynatrace Managed deployments evolve from a basic internal setup to a globally distributed high-availability architecture."), наилучшим образом соответствующую вашим потребностям. На основе выбранной модели [настройте кластер Managed](/managed/managed-cluster/installation/install-managed-cluster "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration.") и создайте первый узел кластера.
* Вы можете [добавлять узлы](/managed/managed-cluster/installation/add-cluster-node "Add a node to your Managed Cluster by downloading the installer, running it on the target host, and monitoring synchronization progress.") в любое время. Для кластера Managed в производственной среде требуется не менее 3 узлов.

### Шаг 3 Установите ActiveGate

* Установите [Cluster ActiveGate](/managed/managed-cluster/installation/install-cluster-activegate "Install a Cluster ActiveGate on Linux or Windows to route OneAgent traffic or run Synthetic monitors, and connect it to your Managed Cluster.") и/или [Environment ActiveGate](/managed/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate") в соответствии с требованиями выбранной модели развёртывания.

### Шаг 4 Передайте телеметрические данные

* [Установите OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation "Install OneAgent on a server for the very first time.") на хост для автоматического мониторинга и анализа производительности и работоспособности всей ИТ-инфраструктуры,
* или [передайте данные через OpenTelemetry](https://www.dynatrace.com/news/blog/send-opentelemetry-data-to-dynatrace/#configure-the-otel-collector-for-dynatrace) для более гибридной инфраструктуры.

### Шаг 5 Проверьте получение данных

* Просматривайте **обнаруженную топологию** с помощью [Smartscape](/managed/analyze-explore-automate/smartscape-classic "Learn how Smartscape visualizes all the entities and dependencies in your environment.") в вашей [среде мониторинга](/managed/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").

### Шаг 6 Визуализируйте данные

* Начните создавать собственные [Dashboards](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.").

### Шаг 7 Настройте уведомления

* Настройте первые [уведомления](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications "Learn how to integrate third-party problem notification systems with Dynatrace.").