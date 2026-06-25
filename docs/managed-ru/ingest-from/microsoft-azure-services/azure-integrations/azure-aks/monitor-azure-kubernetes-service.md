---
title: Мониторинг Azure Kubernetes Service (AKS)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-aks/monitor-azure-kubernetes-service
scraped: 2026-05-12T11:25:41.093431
---

# Мониторинг Azure Kubernetes Service (AKS)

# Мониторинг Azure Kubernetes Service (AKS)

* Практическое руководство
* Чтение: 1 мин
* Опубликовано 19 августа 2020 г.

Dynatrace получает метрики для нескольких предварительно выбранных пространств имён, включая Azure Kubernetes Service. Можно просматривать метрики для каждого экземпляра сервиса, разбивать метрики по нескольким измерениям и создавать пользовательские диаграммы, которые можно закрепить на дашбордах.

## Предварительные требования

* Dynatrace версии 1.200+
* Environment ActiveGate версии 1.195+

## Включение мониторинга

О том, как включить мониторинг сервиса, см. в разделе [Включение мониторинга сервиса](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Включение мониторинга Azure в Dynatrace.").

## Просмотр метрик сервиса

Метрики сервиса можно просматривать в окружении Dynatrace на странице обзора пользовательского устройства (**custom device overview page**) или на странице **Dashboards**.

### Просмотр метрик на странице обзора пользовательского устройства

Чтобы открыть страницу обзора пользовательского устройства

1. Откройте **Technologies & Processes**.
2. Отфильтруйте по имени сервиса и выберите нужную группу пользовательских устройств.
3. После выбора группы пользовательских устройств откроется **custom device group overview page**.
4. На странице **custom device group overview page** перечислены все экземпляры (пользовательские устройства), входящие в группу. Выберите экземпляр, чтобы открыть **custom device overview page**.

### Просмотр метрик на дашборде

Если для сервиса предусмотрен преднастроенный дашборд, на странице **Dashboards** появится преднастроенный дашборд для соответствующего сервиса со всеми рекомендованными метриками. Нужный дашборд можно найти, отфильтровав по **Preset**, а затем по **Name**.

Для существующих отслеживаемых сервисов может потребоваться повторно сохранить учётные данные, чтобы преднастроенный дашборд появился на странице **Dashboards**. Для повторного сохранения учётных данных откройте **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure и нажмите **Save**.

Напрямую вносить изменения в преднастроенный дашборд нельзя, но можно клонировать его и редактировать. Чтобы клонировать дашборд, откройте меню (**…**) и выберите **Clone**.
Чтобы убрать дашборд из списка, его можно скрыть. Для этого откройте меню (**…**) и выберите **Hide**.

Скрытие дашборда не затрагивает других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

Clone hide azure

![AKS dash](https://dt-cdn.net/images/dashboard-35-2560-d7064f1619.png)

AKS dash

Пространство имён **STANDARD** содержит только четыре метрики. Все метрики `Nodes` находятся в пространстве имён **CUSTOM**, а метрики `Node disk capacity` и `IO` находятся в пространстве имён **CUSTOM (LOG-BASED)**.

## Доступные метрики

| Имя | Описание | Единица | Измерения | Рекомендовано |
| --- | --- | --- | --- | --- |
| node\_cpu\_usage\_percentage |  | Percent | Name of the node, Name of the nodepool | Применимо |
| node\_memory\_working\_set\_bytes |  | Byte | Name of the node, Name of the nodepool | Применимо |
| node\_memory\_working\_set\_percentage |  | Percent | Name of the node, Name of the nodepool | Применимо |
| kube\_node\_status\_allocatable\_cpu\_cores | Общее количество доступных ядер CPU в управляемом кластере | Count |  | Применимо |
| kube\_node\_status\_allocatable\_memory\_bytes | Общий объём доступной памяти в управляемом кластере | Byte |  | Применимо |
| kube\_node\_status\_condition | Статусы различных условий узла | Count | condition, status, node | Применимо |
| kube\_pod\_status\_phase | Количество подов по фазам | Count | phase, namespace, pod | Применимо |
| kube\_pod\_status\_ready | Количество подов в состоянии Ready | Count | namespace, pod | Применимо |