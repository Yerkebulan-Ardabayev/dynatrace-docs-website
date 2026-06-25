---
title: Компоненты Managed
source: https://docs.dynatrace.com/managed/managed-cluster/basics/managed-components
scraped: 2026-05-12T11:08:47.577972
---

# Компоненты Managed

# Компоненты Managed

* Explanation
* 3-min read
* Updated on May 08, 2026

На следующем рисунке показаны компоненты Dynatrace Managed.

![Managed architecture](https://dt-cdn.net/images/managed-general-architecture-1892-448d089eed.png)

Managed architecture

## Managed Cluster

Managed Cluster отвечает за управление различными [средами мониторинга](/managed/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments."). Managed Cluster, как правило, включает несколько узлов. Для каждого Managed Cluster предусмотрена отдельная Cluster Management Console.

Managed Cluster отправляет данные самомониторинга и лицензирования в Mission Control для обеспечения проактивной поддержки.

При создании каждого нового Managed Cluster необходимо [получить лицензию](/managed/discover-dynatrace/get-started "Learn how to get started with Dynatrace Managed.").

## Установщик Managed

Установщик Managed обеспечивает установку Dynatrace Managed и всех необходимых компонентов:

* Dynatrace Server
* Apache Cassandra
* Elasticsearch
* NGINX
* Встроенный ActiveGate

Все перечисленные компоненты развёртываются на первом узле при [настройке Managed Cluster](/managed/managed-cluster/installation/install-managed-cluster "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration."), а также на каждом [последующем узле](/managed/managed-cluster/installation/add-cluster-node "Add a node to your Managed Cluster by downloading the installer, running it on the target host, and monitoring synchronization progress.").

## Cluster Management Console

Для каждого созданного Managed Cluster предусмотрена отдельная Cluster Management Console. Cluster Management Console — это веб-интерфейс для управления вашим Managed Cluster. Из этого интерфейса можно в любое время просматривать статус развёртывания Managed Cluster.

С помощью Cluster Management Console можно, например:

* [Создавать учётные записи пользователей и группы](/managed/manage/identity-access-management/user-and-group-management/user-groups-and-permissions "Learn about the supported permissions and policies, how you can assign them to groups, and how you can manage your users and groups.").
* [Добавлять узлы кластера](/managed/managed-cluster/installation/add-cluster-node "Add a node to your Managed Cluster by downloading the installer, running it on the target host, and monitoring synchronization progress.").
* [Добавлять среды мониторинга](/managed/managed-cluster/operation/manage-your-monitoring-environments "Find out how to create, configure, access, delete, disable, and switch between monitoring environments.").

## Mission Control

[Mission Control](/managed/managed-cluster/basics/mission-control-proactive-support "Mission Control proactively monitors your Managed Cluster, provides software updates, and keeps your installation secure and reliable.") получает данные самомониторинга и лицензирования от Managed Cluster. На основе этих данных команда Dynatrace Mission Control может проактивно анализировать и выявлять неправильные конфигурации или потенциальные несовместимости в вашей установке. Mission Control также предоставляет обновления программного обеспечения для Managed Cluster.