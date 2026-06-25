# -*- coding: utf-8 -*-
"""L4-IF.73 — ingest-from/microsoft-azure-services/azure-integrations/azure-aks/monitor-azure-kubernetes-service.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/microsoft-azure-services/azure-integrations/azure-aks"

TT_ENABLE = "Включение мониторинга Azure в Dynatrace."

TRANS = {
    "title: Azure Kubernetes Service (AKS) monitoring": "title: Мониторинг Azure Kubernetes Service (AKS)",
    "# Azure Kubernetes Service (AKS) monitoring": "# Мониторинг Azure Kubernetes Service (AKS)",
    "* How-to guide": "* Практическое руководство",
    "* 1-min read": "* Чтение: 1 мин",
    "* Published Aug 19, 2020": "* Опубликовано 19 августа 2020 г.",
    "Dynatrace ingests metrics for multiple preselected namespaces, including Azure Kubernetes Service. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.": "Dynatrace получает метрики для нескольких предварительно выбранных пространств имён, включая Azure Kubernetes Service. Можно просматривать метрики для каждого экземпляра сервиса, разбивать метрики по нескольким измерениям и создавать пользовательские диаграммы, которые можно закрепить на дашбордах.",
    "## Prerequisites": "## Предварительные требования",
    "* Dynatrace version 1.200+": "* Dynatrace версии 1.200+",
    "* Environment ActiveGate version 1.195+": "* Environment ActiveGate версии 1.195+",
    "## Enable monitoring": "## Включение мониторинга",
    f'To learn how to enable service monitoring, see [Enable service monitoring](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").': f'О том, как включить мониторинг сервиса, см. в разделе [Включение мониторинга сервиса](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "{TT_ENABLE}").',
    "## View service metrics": "## Просмотр метрик сервиса",
    "You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.": "Метрики сервиса можно просматривать в окружении Dynatrace на странице обзора пользовательского устройства (**custom device overview page**) или на странице **Dashboards**.",
    "### View metrics on the custom device overview page": "### Просмотр метрик на странице обзора пользовательского устройства",
    "To access the custom device overview page": "Чтобы открыть страницу обзора пользовательского устройства",
    "1. Go to **Technologies & Processes**.": "1. Откройте **Technologies & Processes**.",
    "2. Filter by service name and select the relevant custom device group.": "2. Отфильтруйте по имени сервиса и выберите нужную группу пользовательских устройств.",
    "3. Once you select the custom device group, you're on the **custom device group overview page**.": "3. После выбора группы пользовательских устройств откроется **custom device group overview page**.",
    "4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.": "4. На странице **custom device group overview page** перечислены все экземпляры (пользовательские устройства), входящие в группу. Выберите экземпляр, чтобы открыть **custom device overview page**.",
    "### View metrics on your dashboard": "### Просмотр метрик на дашборде",
    "If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.": "Если для сервиса предусмотрен преднастроенный дашборд, на странице **Dashboards** появится преднастроенный дашборд для соответствующего сервиса со всеми рекомендованными метриками. Нужный дашборд можно найти, отфильтровав по **Preset**, а затем по **Name**.",
    "For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.": "Для существующих отслеживаемых сервисов может потребоваться повторно сохранить учётные данные, чтобы преднастроенный дашборд появился на странице **Dashboards**. Для повторного сохранения учётных данных откройте **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure и нажмите **Save**.",
    "You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**…**) and select **Clone**.": "Напрямую вносить изменения в преднастроенный дашборд нельзя, но можно клонировать его и редактировать. Чтобы клонировать дашборд, откройте меню (**…**) и выберите **Clone**.",
    "To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**…**) and select **Hide**.": "Чтобы убрать дашборд из списка, его можно скрыть. Для этого откройте меню (**…**) и выберите **Hide**.",
    "Hiding a dashboard doesn't affect other users.": "Скрытие дашборда не затрагивает других пользователей.",
    "![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)": "![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)",
    "Clone hide azure": "Clone hide azure",
    "![AKS dash](https://dt-cdn.net/images/dashboard-35-2560-d7064f1619.png)": "![AKS dash](https://dt-cdn.net/images/dashboard-35-2560-d7064f1619.png)",
    "AKS dash": "AKS dash",
    "The **STANDARD** namespace has only four metrics. All `Nodes` metrics are inside the **CUSTOM** namespace, while the `Node disk capacity` and `IO` metrics are in the **CUSTOM (LOG-BASED)** namespace.": "Пространство имён **STANDARD** содержит только четыре метрики. Все метрики `Nodes` находятся в пространстве имён **CUSTOM**, а метрики `Node disk capacity` и `IO` находятся в пространстве имён **CUSTOM (LOG-BASED)**.",
    "## Available metrics": "## Доступные метрики",
    "| Name | Description | Unit | Dimensions | Recommended |": "| Имя | Описание | Единица | Измерения | Рекомендовано |",
    "| --- | --- | --- | --- | --- |": "| --- | --- | --- | --- | --- |",
    "| node\\_cpu\\_usage\\_percentage |  | Percent | Name of the node, Name of the nodepool | Applicable |": "| node\\_cpu\\_usage\\_percentage |  | Percent | Name of the node, Name of the nodepool | Применимо |",
    "| node\\_memory\\_working\\_set\\_bytes |  | Byte | Name of the node, Name of the nodepool | Applicable |": "| node\\_memory\\_working\\_set\\_bytes |  | Byte | Name of the node, Name of the nodepool | Применимо |",
    "| node\\_memory\\_working\\_set\\_percentage |  | Percent | Name of the node, Name of the nodepool | Applicable |": "| node\\_memory\\_working\\_set\\_percentage |  | Percent | Name of the node, Name of the nodepool | Применимо |",
    "| kube\\_node\\_status\\_allocatable\\_cpu\\_cores | Total number of available CPU cores in a managed cluster | Count |  | Applicable |": "| kube\\_node\\_status\\_allocatable\\_cpu\\_cores | Общее количество доступных ядер CPU в управляемом кластере | Count |  | Применимо |",
    "| kube\\_node\\_status\\_allocatable\\_memory\\_bytes | Total amount of available memory in a managed cluster | Byte |  | Applicable |": "| kube\\_node\\_status\\_allocatable\\_memory\\_bytes | Общий объём доступной памяти в управляемом кластере | Byte |  | Применимо |",
    "| kube\\_node\\_status\\_condition | Statuses for various node conditions | Count | condition, status, node | Applicable |": "| kube\\_node\\_status\\_condition | Статусы различных условий узла | Count | condition, status, node | Применимо |",
    "| kube\\_pod\\_status\\_phase | Number of pods by phase | Count | phase, namespace, pod | Applicable |": "| kube\\_pod\\_status\\_phase | Количество подов по фазам | Count | phase, namespace, pod | Применимо |",
    "| kube\\_pod\\_status\\_ready | Number of pods in Ready state | Count | namespace, pod | Applicable |": "| kube\\_pod\\_status\\_ready | Количество подов в состоянии Ready | Count | namespace, pod | Применимо |",
}

PASS = set()

if __name__ == "__main__":
    build_one(REL, "monitor-azure-kubernetes-service.md", TRANS, PASS)
    qa_one(REL, "monitor-azure-kubernetes-service.md")
