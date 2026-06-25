# -*- coding: utf-8 -*-
"""L4-IF.73 -- ingest-from/microsoft-azure-services/azure-integrations/azure-vm/monitor-azure-virtual-machines-builtin.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/microsoft-azure-services/azure-integrations/azure-vm"

TT_ENABLE = "Включение мониторинга Azure в Dynatrace."
TT_TROUBLESHOOT = "Устранение неполадок со сравнением временных интервалов при настройке мониторинга Azure"
TT_DASHBOARDS = "Узнайте, как создавать и редактировать дашборды Dynatrace."

TRANS = {
    "title: Monitor Azure Virtual Machines (built-in)": "title: Мониторинг Azure Virtual Machines (built-in)",
    "# Monitor Azure Virtual Machines (built-in)": "# Мониторинг Azure Virtual Machines (built-in)",
    "* How-to guide": "* Практическое руководство",
    "* 1-min read": "* Чтение: 1 мин",
    "* Published Jul 27, 2022": "* Опубликовано 27 июля 2022 г.",
    "Dynatrace ingests metrics from Azure Metrics API for **Azure Virtual Machines and Azure Virtual Machine Scale Sets**. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.": "Dynatrace получает метрики из Azure Metrics API для **Azure Virtual Machines и Azure Virtual Machine Scale Sets**. Можно просматривать метрики для каждого экземпляра сервиса, разбивать метрики по различным измерениям и создавать пользовательские графики, которые можно закрепить на дашбордах.",
    "## Prerequisites": "## Предварительные требования",
    "* Environment ActiveGate": "* Environment ActiveGate",
    "* To disable monitoring of built-in services, you need Environment ActiveGate version 1.245+ and Dynatrace version 1.247+.": "* Чтобы отключить мониторинг встроенных сервисов, требуется Environment ActiveGate версии 1.245+ и Dynatrace версии 1.247+.",
    "This service monitors Azure Virtual Machines (`Microsoft.Compute/virtualMachines`) and Virtual Machine Scale Sets (`Microsoft.Compute/virtualMachineScaleSets`) with Uniform orchestration mode.": "Этот сервис отслеживает Azure Virtual Machines (`Microsoft.Compute/virtualMachines`) и Virtual Machine Scale Sets (`Microsoft.Compute/virtualMachineScaleSets`) в режиме оркестрации Uniform.",
    "You can find the already monitored resources on the Azure overview page in the **VMs** and **Scale sets** sections. To monitor resources of type `Microsoft.ClassicCompute/virtualMachines`, check **Azure Virtual Machine (classic)** and the **Cloud services** section on the Azure overview page.": "Уже отслеживаемые ресурсы можно найти на странице обзора Azure в разделах **VMs** и **Scale sets**. Для мониторинга ресурсов типа `Microsoft.ClassicCompute/virtualMachines` проверьте раздел **Azure Virtual Machine (classic)** и **Cloud services** на странице обзора Azure.",
    "## Enable monitoring": "## Включение мониторинга",
    f'To learn how to enable service monitoring, see [Enable service monitoring](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").': f'О том, как включить мониторинг сервиса, см. в разделе [Включение мониторинга сервиса](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "{TT_ENABLE}").',
    "## View service metrics": "## Просмотр метрик сервиса",
    "You can view Azure service metrics in your Dynatrace environment on the Azure subscription page or on your own dashboard.": "Метрики сервисов Azure можно просматривать в окружении Dynatrace на странице подписки Azure или на собственном дашборде.",
    f"Values in the table depend upon the selected timeframe. For more details, see [Troubleshoot timeframe comparison for Azure monitoring setup)](https://dt-url.net/7j438f0).": f"Значения в таблице зависят от выбранного временного интервала. Подробнее см. в разделе [Устранение неполадок со сравнением временных интервалов при настройке мониторинга Azure)](https://dt-url.net/7j438f0).",
    "### View metrics on the Azure account page": "### Просмотр метрик на странице учётной записи Azure",
    "To access metrics on the Azure account page": "Чтобы получить доступ к метрикам на странице учётной записи Azure",
    "1. Go to **Azure**.": "1. Перейдите в **Azure**.",
    "2. Choose the Azure subscription.": "2. Выберите подписку Azure.",
    "3. Select the service whose metrics you want to check. Metrics for the selected service are visible under the infographic in the service section, similarly to the example below.": "3. Выберите сервис, метрики которого нужно проверить. Метрики выбранного сервиса отображаются под инфографикой в разделе сервиса, как в примере ниже.",
    "![Azure service metrics](https://dt-cdn.net/images/azure-service-1109-9488bfa5e4.png)": "![Azure service metrics](https://dt-cdn.net/images/azure-service-1109-9488bfa5e4.png)",
    "Azure service metrics": "Azure service metrics",
    "### View metrics on a dashboard": "### Просмотр метрик на дашборде",
    f'You can create your own dashboard for viewing Azure service metrics. For information on how to create dashboards, see [Create and edit Dynatrace dashboards](/managed/analyze-explore-automate/dashboards-classic/dashboards/create-dashboards "Learn how to create and edit Dynatrace dashboards.").': f'Можно создать собственный дашборд для просмотра метрик сервисов Azure. О том, как создавать дашборды, см. в разделе [Создание и редактирование дашбордов Dynatrace](/managed/analyze-explore-automate/dashboards-classic/dashboards/create-dashboards "{TT_DASHBOARDS}").',
    "## Available metrics": "## Доступные метрики",
    "### Azure Virtual Machines": "### Azure Virtual Machines",
    "| Metric key | Name | Unit | Aggregations | Monitoring consumption |": "| Ключ метрики | Имя | Единица измерения | Агрегации | Потребление мониторинга |",
    "| --- | --- | --- | --- | --- |": "| --- | --- | --- | --- | --- |",
    "| builtin:cloud.azure.vm.disk.read | Disk read bytes | Byte | autovalue | DDUs |": "| builtin:cloud.azure.vm.disk.read | Disk read bytes | Byte | autovalue | DDUs |",
    "| builtin:cloud.azure.vm.disk.readOps | Disk read operations per sec | Per second | autoavgmaxmin | DDUs |": "| builtin:cloud.azure.vm.disk.readOps | Disk read operations per sec | Per second | autoavgmaxmin | DDUs |",
    "| builtin:cloud.azure.vm.disk.write | Disk write bytes | Byte | autovalue | DDUs |": "| builtin:cloud.azure.vm.disk.write | Disk write bytes | Byte | autovalue | DDUs |",
    "| builtin:cloud.azure.vm.disk.writeOps | Disk write operations per sec | Per second | autoavgmaxmin | DDUs |": "| builtin:cloud.azure.vm.disk.writeOps | Disk write operations per sec | Per second | autoavgmaxmin | DDUs |",
    "| builtin:cloud.azure.vm.network.bytesIn | Network in bytes | Byte | autovalue | DDUs |": "| builtin:cloud.azure.vm.network.bytesIn | Network in bytes | Byte | autovalue | DDUs |",
    "| builtin:cloud.azure.vm.network.bytesOut | Network out bytes | Byte | autovalue | DDUs |": "| builtin:cloud.azure.vm.network.bytesOut | Network out bytes | Byte | autovalue | DDUs |",
    "| builtin:cloud.azure.vm.cpuUsage | Percentage CPU | Percent (%) | autoavgmaxmin | DDUs |": "| builtin:cloud.azure.vm.cpuUsage | Percentage CPU | Percent (%) | autoavgmaxmin | DDUs |",
    "### Azure Virtual Machines region": "### Регион Azure Virtual Machines",
    "| builtin:cloud.azure.region.vms.initializing | Number of starting VMs in region | Count | autoavgmaxmin | Host units |": "| builtin:cloud.azure.region.vms.initializing | Number of starting VMs in region | Count | autoavgmaxmin | Host units |",
    "| builtin:cloud.azure.region.vms.running | Number of active VMs in region | Count | autoavgmaxmin | Host units |": "| builtin:cloud.azure.region.vms.running | Number of active VMs in region | Count | autoavgmaxmin | Host units |",
    "| builtin:cloud.azure.region.vms.stopped | Number of stopped VMs in region | Count | autoavgmaxmin | Host units |": "| builtin:cloud.azure.region.vms.stopped | Number of stopped VMs in region | Count | autoavgmaxmin | Host units |",
    "### Azure Virtual Machine Scale Sets": "### Azure Virtual Machine Scale Sets",
    "| builtin:cloud.azure.vmScaleSet.disk.read | Disk read bytes | Byte | autovalue | DDUs |": "| builtin:cloud.azure.vmScaleSet.disk.read | Disk read bytes | Byte | autovalue | DDUs |",
    "| builtin:cloud.azure.vmScaleSet.disk.readOps | Disk read operations per sec | Per second | autoavgmaxmin | DDUs |": "| builtin:cloud.azure.vmScaleSet.disk.readOps | Disk read operations per sec | Per second | autoavgmaxmin | DDUs |",
    "| builtin:cloud.azure.vmScaleSet.disk.write | Disk write bytes | Byte | autovalue | DDUs |": "| builtin:cloud.azure.vmScaleSet.disk.write | Disk write bytes | Byte | autovalue | DDUs |",
    "| builtin:cloud.azure.vmScaleSet.disk.writeOps | Disk write operations per sec | Per second | autoavgmaxmin | DDUs |": "| builtin:cloud.azure.vmScaleSet.disk.writeOps | Disk write operations per sec | Per second | autoavgmaxmin | DDUs |",
    "| builtin:cloud.azure.vmScaleSet.network.bytesIn | Network in bytes | Byte | autovalue | DDUs |": "| builtin:cloud.azure.vmScaleSet.network.bytesIn | Network in bytes | Byte | autovalue | DDUs |",
    "| builtin:cloud.azure.vmScaleSet.network.bytesOut | Network out bytes | Byte | autovalue | DDUs |": "| builtin:cloud.azure.vmScaleSet.network.bytesOut | Network out bytes | Byte | autovalue | DDUs |",
    "| builtin:cloud.azure.vmScaleSet.vms.initializing | Number of starting VMs in scale set | Count | autoavgmaxmin | Host units |": "| builtin:cloud.azure.vmScaleSet.vms.initializing | Number of starting VMs in scale set | Count | autoavgmaxmin | Host units |",
    "| builtin:cloud.azure.vmScaleSet.vms.running | Number of active VMs in scale set | Count | autoavgmaxmin | Host units |": "| builtin:cloud.azure.vmScaleSet.vms.running | Number of active VMs in scale set | Count | autoavgmaxmin | Host units |",
    "| builtin:cloud.azure.vmScaleSet.vms.stopped | Number of stopped VMs in scale set | Count | autoavgmaxmin | Host units |": "| builtin:cloud.azure.vmScaleSet.vms.stopped | Number of stopped VMs in scale set | Count | autoavgmaxmin | Host units |",
    "| builtin:cloud.azure.vmScaleSet.cpuUsage | Percentage CPU | Percent (%) | autoavgmaxmin | DDUs |": "| builtin:cloud.azure.vmScaleSet.cpuUsage | Percentage CPU | Percent (%) | autoavgmaxmin | DDUs |",
}

PASS = set()

if __name__ == "__main__":
    build_one(REL, "monitor-azure-virtual-machines-builtin.md", TRANS, PASS)
    qa_one(REL, "monitor-azure-virtual-machines-builtin.md")
