# -*- coding: utf-8 -*-
"""L4-IF.73 — ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/monitor-app-service.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/microsoft-azure-services/azure-integrations/azure-appservice"

TT_ENABLE = "Включение мониторинга Azure в Dynatrace."
TT_SETTINGS = "Настройки"

TRANS = {
    "title: Monitor Azure App Service Plan metrics": "title: Мониторинг метрик Azure App Service Plan",
    "# Monitor Azure App Service Plan metrics": "# Мониторинг метрик Azure App Service Plan",
    "* How-to guide": "* Практическое руководство",
    "* 2-min read": "* Чтение: 2 мин",
    "* Published Sep 23, 2020": "* Опубликовано 23 сентября 2020 г.",
    "Dynatrace ingests metrics from Azure Metrics API for **Azure App Service Plan** used by your deployed App Service. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.": "Dynatrace получает метрики из Azure Metrics API для **Azure App Service Plan**, используемого вашим развёрнутым App Service. Можно просматривать метрики для каждого экземпляра сервиса, разбивать метрики по нескольким измерениям и создавать пользовательские диаграммы, которые можно закрепить на дашбордах.",
    "## Prerequisites": "## Предварительные требования",
    "* Dynatrace version 1.203+": "* Dynatrace версии 1.203+",
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
    "![App service plan](https://dt-cdn.net/images/dashboard-87-873-b330e8b901.png)": "![App service plan](https://dt-cdn.net/images/dashboard-87-873-b330e8b901.png)",
    "App service plan": "App service plan",
    "## Available metrics": "## Доступные метрики",
    "| Name | Description | Dimensions | Unit | Recommended |": "| Имя | Описание | Измерения | Единица | Рекомендовано |",
    "| --- | --- | --- | --- | --- |": "| --- | --- | --- | --- | --- |",
    "| BytesReceived | Data in | Instance | Byte | ✔️ |": "| BytesReceived | Входящие данные | Instance | Byte | ✔️ |",
    "| BytesSent | Data out | Instance | Byte | ✔️ |": "| BytesSent | Исходящие данные | Instance | Byte | ✔️ |",
    "| CpuPercentage | CPU percentage | Instance | Percent | ✔️ |": "| CpuPercentage | Загрузка CPU | Instance | Percent | ✔️ |",
    "| DiskQueueLength | Disk queue length | Instance | Count | ✔️ |": "| DiskQueueLength | Длина очереди диска | Instance | Count | ✔️ |",
    "| HttpQueueLength | HTTP queue length | Instance | Count | ✔️ |": "| HttpQueueLength | Длина очереди HTTP | Instance | Count | ✔️ |",
    "| MemoryPercentage | Memory percentage | Instance | Percent | ✔️ |": "| MemoryPercentage | Использование памяти | Instance | Percent | ✔️ |",
    "| SocketInboundAll | Socket inbound all |  | Count |  |": "| SocketInboundAll | Все входящие сокеты |  | Count |  |",
    "| SocketLoopback | Socket loopback | Instance | Count |  |": "| SocketLoopback | Петлевые сокеты | Instance | Count |  |",
    "| SocketOutboundAll | Socket Outbound All |  | Count |  |": "| SocketOutboundAll | Все исходящие сокеты |  | Count |  |",
    "| SocketOutboundEstablished | Socket outbound established | Instance | Count |  |": "| SocketOutboundEstablished | Установленные исходящие сокеты | Instance | Count |  |",
    "| SocketOutboundTimeWait | Socket outbound time wait | Instance | Count |  |": "| SocketOutboundTimeWait | Исходящие сокеты в состоянии ожидания | Instance | Count |  |",
    "| TcpCloseWait | TCP close wait | Instance | Count |  |": "| TcpCloseWait | TCP ожидание закрытия | Instance | Count |  |",
    "| TcpClosing | TCP closing | Instance | Count |  |": "| TcpClosing | TCP закрытие | Instance | Count |  |",
    "| TcpEstablished | TCP established | Instance | Count |  |": "| TcpEstablished | TCP соединения установлены | Instance | Count |  |",
    "| TcpFinWait1 | TCP fin wait 1 | Instance | Count |  |": "| TcpFinWait1 | TCP fin wait 1 | Instance | Count |  |",
    "| TcpFinWait2 | TCP fin wait 2 | Instance | Count |  |": "| TcpFinWait2 | TCP fin wait 2 | Instance | Count |  |",
    "| TcpLastAck | TCP last ack | Instance | Count |  |": "| TcpLastAck | TCP last ack | Instance | Count |  |",
    "| TcpSynReceived | TCP syn received | Instance | Count |  |": "| TcpSynReceived | TCP syn received | Instance | Count |  |",
    "| TcpSynSent | TCP syn sent | Instance | Count |  |": "| TcpSynSent | TCP syn sent | Instance | Count |  |",
    "| TcpTimeWait | TCP time wait | Instance | Count |  |": "| TcpTimeWait | TCP time wait | Instance | Count |  |",
}

PASS = set()

if __name__ == "__main__":
    build_one(REL, "monitor-app-service.md", TRANS, PASS)
    qa_one(REL, "monitor-app-service.md")
