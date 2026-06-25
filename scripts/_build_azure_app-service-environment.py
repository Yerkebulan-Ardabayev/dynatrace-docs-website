# -*- coding: utf-8 -*-
"""L4-IF.73 — ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/monitor-azure-app-service-environment.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/microsoft-azure-services/azure-integrations/azure-appservice"

TT_ENABLE = "Включение мониторинга Azure в Dynatrace."

TRANS = {
    "title: Enable Azure Monitor App Service Environment V2 metrics": "title: Включение метрик Azure Monitor App Service Environment V2",
    "# Enable Azure Monitor App Service Environment V2 metrics": "# Включение метрик Azure Monitor App Service Environment V2",
    "* How-to guide": "* Практическое руководство",
    "* 2-min read": "* Чтение: 2 мин",
    "* Published Jun 29, 2022": "* Опубликовано 29 июня 2022 г.",
    "Dynatrace ingests metrics from the Azure Metrics API for Azure App Service Environment v2. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.": "Dynatrace получает метрики из Azure Metrics API для Azure App Service Environment v2. Можно просматривать метрики для каждого экземпляра сервиса, разбивать метрики по нескольким измерениям и создавать пользовательские диаграммы, которые можно закрепить на дашбордах.",
    "## Prerequisites": "## Предварительные требования",
    "* Dynatrace version 1.201+": "* Dynatrace версии 1.201+",
    "* Environment ActiveGate version 1.195+": "* Environment ActiveGate версии 1.195+",
    "Only App Service Environment v2 can be monitored by Dynatrace.": "Dynatrace может отслеживать только App Service Environment v2.",
    "To monitor App Service Environment v1, contact a Dynatrace product expert via live chat.": "Для мониторинга App Service Environment v1 обратитесь к эксперту по продуктам Dynatrace через live chat.",
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
    "![App Service Environment v2](https://dt-cdn.net/images/azure-metrics-3925-3bc9d7a9da.png)": "![App Service Environment v2](https://dt-cdn.net/images/azure-metrics-3925-3bc9d7a9da.png)",
    "App Service Environment v2": "App Service Environment v2",
    "## Available metrics": "## Доступные метрики",
    "| Name | Description | Dimensions | Unit | Recommended |": "| Имя | Описание | Измерения | Единица | Рекомендовано |",
    "| --- | --- | --- | --- | --- |": "| --- | --- | --- | --- | --- |",
    "| ActiveRequests | Active requests | **Instance** | Count | Applicable |": "| ActiveRequests | Активные запросы | **Instance** | Count | Применимо |",
    "| CpuPercentage | CPU percentage | **Instance** | Percent | Applicable |": "| CpuPercentage | Загрузка CPU | **Instance** | Percent | Применимо |",
    "| BytesReceived | Data in | **Instance** | Byte | Applicable |": "| BytesReceived | Входящие данные | **Instance** | Byte | Применимо |",
    "| BytesSent | Data out | **Instance** | Byte | Applicable |": "| BytesSent | Исходящие данные | **Instance** | Byte | Применимо |",
    "| DiskQueueLength | Disk queue length | **Instance** | Count | Applicable |": "| DiskQueueLength | Длина очереди диска | **Instance** | Count | Применимо |",
    "| Http101 | HTTP 101 | Instance | Count |  |": "| Http101 | HTTP 101 | Instance | Count |  |",
    "| Http2xx | HTTP 2xx | **Instance** | Count | Applicable |": "| Http2xx | HTTP 2xx | **Instance** | Count | Применимо |",
    "| Http3xx | HTTP 3xx | **Instance** | Count | Applicable |": "| Http3xx | HTTP 3xx | **Instance** | Count | Применимо |",
    "| Http401 | HTTP 401 | **Instance** | Count | Applicable |": "| Http401 | HTTP 401 | **Instance** | Count | Применимо |",
    "| Http403 | HTTP 403 | **Instance** | Count | Applicable |": "| Http403 | HTTP 403 | **Instance** | Count | Применимо |",
    "| Http404 | HTTP 404 | **Instance** | Count | Applicable |": "| Http404 | HTTP 404 | **Instance** | Count | Применимо |",
    "| Http406 | HTTP 406 | **Instance** | Count | Applicable |": "| Http406 | HTTP 406 | **Instance** | Count | Применимо |",
    "| Http4xx | HTTP 4xx | **Instance** | Count | Applicable |": "| Http4xx | HTTP 4xx | **Instance** | Count | Применимо |",
    "| Http5xx | HTTP 5xx | **Instance** | Count | Applicable |": "| Http5xx | HTTP 5xx | **Instance** | Count | Применимо |",
    "| HttpQueueLength | HTTP queue length | **Instance** | Count |  |": "| HttpQueueLength | Длина очереди HTTP | **Instance** | Count |  |",
    "| LargeAppServicePlanInstances | Large app service plan workers |  | Count |  |": "| LargeAppServicePlanInstances | Рабочие процессы большого App Service Plan |  | Count |  |",
    "| MediumAppServicePlanInstances | Medium app service plan workers |  | Count |  |": "| MediumAppServicePlanInstances | Рабочие процессы среднего App Service Plan |  | Count |  |",
    "| MemoryPercentage | Memory percentage | **Instance** | Percent | Applicable |": "| MemoryPercentage | Использование памяти | **Instance** | Percent | Применимо |",
    "| Requests | Requests | **Instance** | Count | Applicable |": "| Requests | Запросы | **Instance** | Count | Применимо |",
    "| SmallAppServicePlanInstances | Small app service plan workers |  | Count |  |": "| SmallAppServicePlanInstances | Рабочие процессы малого App Service Plan |  | Count |  |",
    "| TotalFrontEnds | Total frontends |  | Count |  |": "| TotalFrontEnds | Всего фронтендов |  | Count |  |",
}

PASS = set()

if __name__ == "__main__":
    build_one(REL, "monitor-azure-app-service-environment.md", TRANS, PASS)
    qa_one(REL, "monitor-azure-app-service-environment.md")
