# -*- coding: utf-8 -*-
"""L4-IF.73 -- ingest-from/microsoft-azure-services/azure-integrations/azure-vm/monitor-azure-virtual-machines-classic.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/microsoft-azure-services/azure-integrations/azure-vm"

TT_ENABLE = "Включение мониторинга Azure в Dynatrace."

TRANS = {
    "title: Monitor Azure Virtual Machines (classic)": "title: Мониторинг Azure Virtual Machines (classic)",
    "# Monitor Azure Virtual Machines (classic)": "# Мониторинг Azure Virtual Machines (classic)",
    "* How-to guide": "* Практическое руководство",
    "* 2-min read": "* Чтение: 2 мин",
    "* Published Jun 25, 2020": "* Опубликовано 25 июня 2020 г.",
    "On the Azure Virtual Machine (classic) overview page you get insights into various aspects of performance, including CPU usage, disk throughput, IOPS, and more.": "На странице обзора Azure Virtual Machine (classic) доступны сведения о различных аспектах производительности, включая использование CPU, пропускную способность диска, IOPS и другое.",
    "## Prerequisites": "## Предварительные требования",
    "* Dynatrace version 1.196+": "* Dynatrace версии 1.196+",
    "* Environment ActiveGate version 1.195+": "* Environment ActiveGate версии 1.195+",
    "This service monitors Azure Virtual Machine (classic) (`Microsoft.ClassicCompute/virtualMachines`).": "Этот сервис отслеживает Azure Virtual Machine (classic) (`Microsoft.ClassicCompute/virtualMachines`).",
    "You can find the already monitored resources on the Azure overview page in the **Cloud services** section or use a dashboard preset.": "Уже отслеживаемые ресурсы можно найти на странице обзора Azure в разделе **Cloud services** или использовать пресет дашборда.",
    "To monitor resources of the `Microsoft.Compute/virtualMachines` and `Microsoft.Compute/virtualMachineScaleSets` types, check **Azure Virtual machines** and the **VMs**, and **Scale sets** sections on the Azure overview page.": "Для мониторинга ресурсов типов `Microsoft.Compute/virtualMachines` и `Microsoft.Compute/virtualMachineScaleSets` проверьте разделы **Azure Virtual machines**, **VMs** и **Scale sets** на странице обзора Azure.",
    "## Enable monitoring": "## Включение мониторинга",
    f'To learn how to enable service monitoring, see [Enable service monitoring](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").': f'О том, как включить мониторинг сервиса, см. в разделе [Включение мониторинга сервиса](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "{TT_ENABLE}").',
    "## View service metrics": "## Просмотр метрик сервиса",
    "You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.": "Метрики сервиса можно просматривать в окружении Dynatrace на **странице обзора пользовательского устройства** или на странице **Dashboards**.",
    "### View metrics on the custom device overview page": "### Просмотр метрик на странице обзора пользовательского устройства",
    "To access the custom device overview page": "Чтобы открыть страницу обзора пользовательского устройства",
    "1. Go to **Technologies & Processes**.": "1. Перейдите в **Technologies & Processes**.",
    "2. Filter by service name and select the relevant custom device group.": "2. Отфильтруйте по имени сервиса и выберите нужную группу пользовательских устройств.",
    "3. Once you select the custom device group, you're on the **custom device group overview page**.": "3. После выбора группы пользовательских устройств откроется **страница обзора группы пользовательских устройств**.",
    "4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.": "4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), входящие в группу. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.",
    "### View metrics on your dashboard": "### Просмотр метрик на дашборде",
    "If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.": "Если для сервиса есть пресет дашборда, на странице **Dashboards** появится пресет дашборда для данного сервиса со всеми рекомендованными метриками. Конкретные дашборды можно найти с помощью фильтрации по **Preset** и затем по **Name**.",
    "For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.": "Для уже отслеживаемых сервисов может потребоваться повторно сохранить учётные данные, чтобы пресет дашборда появился на странице **Dashboards**. Для этого перейдите в **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure и нажмите **Save**.",
    "You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**…**) and select **Clone**.": "Вносить изменения в пресет дашборда напрямую нельзя, но его можно клонировать и редактировать. Чтобы клонировать дашборд, откройте меню просмотра (**…**) и выберите **Clone**.",
    "To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**…**) and select **Hide**.": "Чтобы убрать дашборд из списка, его можно скрыть. Для этого откройте меню просмотра (**…**) и выберите **Hide**.",
    "Hiding a dashboard doesn't affect other users.": "Скрытие дашборда не влияет на других пользователей.",
    "![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)": "![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)",
    "Clone hide azure": "Clone hide azure",
    "![VM dash](https://dt-cdn.net/images/azurevirtualmachineclassic-3840-410672d47a.png)": "![VM dash](https://dt-cdn.net/images/azurevirtualmachineclassic-3840-410672d47a.png)",
    "VM dash": "VM dash",
    "## Available metrics": "## Доступные метрики",
    "| Name | Description | Dimensions | Unit | Recommended |": "| Имя | Описание | Измерения | Единица измерения | Рекомендуется |",
    "| --- | --- | --- | --- | --- |": "| --- | --- | --- | --- | --- |",
    "| Disk Read | Average bytes read from disk during monitoring period. | None | BytesPerSecond | Applicable |": "| Disk Read | Среднее количество байт, считанных с диска за период мониторинга. | None | BytesPerSecond | Applicable |",
    "| Disk Read Operations/Sec | Disk Read IOPS. | None | CountPerSecond | Applicable |": "| Disk Read Operations/Sec | IOPS чтения с диска. | None | CountPerSecond | Applicable |",
    "| Disk Write | Average bytes written to disk during monitoring period. | None | BytesPerSecond | Applicable |": "| Disk Write | Среднее количество байт, записанных на диск за период мониторинга. | None | BytesPerSecond | Applicable |",
    "| Disk Write Operations/Sec | Disk Write IOPS. | None | CountPerSecond | Applicable |": "| Disk Write Operations/Sec | IOPS записи на диск. | None | CountPerSecond | Applicable |",
    "| Network In | The number of bytes received on all network interfaces by the Virtual Machine(s) (Incoming Traffic). | None | Bytes | Applicable |": "| Network In | Количество байт, полученных на всех сетевых интерфейсах виртуальной машиной (входящий трафик). | None | Bytes | Applicable |",
    "| Network Out | The number of bytes out on all network interfaces by the Virtual Machine(s) (Outgoing Traffic). | None | Bytes | Applicable |": "| Network Out | Количество байт, отправленных на всех сетевых интерфейсах виртуальной машиной (исходящий трафик). | None | Bytes | Applicable |",
    "| Percentage CPU | The percentage of allocated compute units that are currently in use by the Virtual Machine(s). | None | Percent | Applicable |": "| Percentage CPU | Процент выделенных вычислительных единиц, используемых виртуальной машиной в данный момент. | None | Percent | Applicable |",
}

PASS = set()

if __name__ == "__main__":
    build_one(REL, "monitor-azure-virtual-machines-classic.md", TRANS, PASS)
    qa_one(REL, "monitor-azure-virtual-machines-classic.md")
