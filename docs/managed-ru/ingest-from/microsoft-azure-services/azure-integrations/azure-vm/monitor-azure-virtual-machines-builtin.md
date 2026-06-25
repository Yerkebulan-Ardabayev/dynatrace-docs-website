---
title: Мониторинг Azure Virtual Machines (built-in)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-vm/monitor-azure-virtual-machines-builtin
scraped: 2026-05-12T11:26:13.745049
---

# Мониторинг Azure Virtual Machines (built-in)

# Мониторинг Azure Virtual Machines (built-in)

* Практическое руководство
* Чтение: 1 мин
* Опубликовано 27 июля 2022 г.

Dynatrace получает метрики из Azure Metrics API для **Azure Virtual Machines и Azure Virtual Machine Scale Sets**. Можно просматривать метрики для каждого экземпляра сервиса, разбивать метрики по различным измерениям и создавать пользовательские графики, которые можно закрепить на дашбордах.

## Предварительные требования

* Environment ActiveGate
* Чтобы отключить мониторинг встроенных сервисов, требуется Environment ActiveGate версии 1.245+ и Dynatrace версии 1.247+.

Этот сервис отслеживает Azure Virtual Machines (`Microsoft.Compute/virtualMachines`) и Virtual Machine Scale Sets (`Microsoft.Compute/virtualMachineScaleSets`) в режиме оркестрации Uniform.

Уже отслеживаемые ресурсы можно найти на странице обзора Azure в разделах **VMs** и **Scale sets**. Для мониторинга ресурсов типа `Microsoft.ClassicCompute/virtualMachines` проверьте раздел **Azure Virtual Machine (classic)** и **Cloud services** на странице обзора Azure.

## Включение мониторинга

О том, как включить мониторинг сервиса, см. в разделе [Включение мониторинга сервиса](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Включение мониторинга Azure в Dynatrace.").

## Просмотр метрик сервиса

Метрики сервисов Azure можно просматривать в окружении Dynatrace на странице подписки Azure или на собственном дашборде.

Значения в таблице зависят от выбранного временного интервала. Подробнее см. в разделе [Устранение неполадок со сравнением временных интервалов при настройке мониторинга Azure)](https://dt-url.net/7j438f0).

### Просмотр метрик на странице учётной записи Azure

Чтобы получить доступ к метрикам на странице учётной записи Azure

1. Перейдите в **Azure**.
2. Выберите подписку Azure.
3. Выберите сервис, метрики которого нужно проверить. Метрики выбранного сервиса отображаются под инфографикой в разделе сервиса, как в примере ниже.

   ![Azure service metrics](https://dt-cdn.net/images/azure-service-1109-9488bfa5e4.png)

   Azure service metrics

### Просмотр метрик на дашборде

Можно создать собственный дашборд для просмотра метрик сервисов Azure. О том, как создавать дашборды, см. в разделе [Создание и редактирование дашбордов Dynatrace](/managed/analyze-explore-automate/dashboards-classic/dashboards/create-dashboards "Узнайте, как создавать и редактировать дашборды Dynatrace.").

## Доступные метрики

### Azure Virtual Machines

| Ключ метрики | Имя | Единица измерения | Агрегации | Потребление мониторинга |
| --- | --- | --- | --- | --- |
| builtin:cloud.azure.vm.disk.read | Disk read bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.vm.disk.readOps | Disk read operations per sec | Per second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.vm.disk.write | Disk write bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.vm.disk.writeOps | Disk write operations per sec | Per second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.vm.network.bytesIn | Network in bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.vm.network.bytesOut | Network out bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.vm.cpuUsage | Percentage CPU | Percent (%) | autoavgmaxmin | DDUs |

### Регион Azure Virtual Machines

| Ключ метрики | Имя | Единица измерения | Агрегации | Потребление мониторинга |
| --- | --- | --- | --- | --- |
| builtin:cloud.azure.region.vms.initializing | Number of starting VMs in region | Count | autoavgmaxmin | Host units |
| builtin:cloud.azure.region.vms.running | Number of active VMs in region | Count | autoavgmaxmin | Host units |
| builtin:cloud.azure.region.vms.stopped | Number of stopped VMs in region | Count | autoavgmaxmin | Host units |

### Azure Virtual Machine Scale Sets

| Ключ метрики | Имя | Единица измерения | Агрегации | Потребление мониторинга |
| --- | --- | --- | --- | --- |
| builtin:cloud.azure.vmScaleSet.disk.read | Disk read bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.vmScaleSet.disk.readOps | Disk read operations per sec | Per second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.vmScaleSet.disk.write | Disk write bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.vmScaleSet.disk.writeOps | Disk write operations per sec | Per second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.vmScaleSet.network.bytesIn | Network in bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.vmScaleSet.network.bytesOut | Network out bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.vmScaleSet.vms.initializing | Number of starting VMs in scale set | Count | autoavgmaxmin | Host units |
| builtin:cloud.azure.vmScaleSet.vms.running | Number of active VMs in scale set | Count | autoavgmaxmin | Host units |
| builtin:cloud.azure.vmScaleSet.vms.stopped | Number of stopped VMs in scale set | Count | autoavgmaxmin | Host units |
| builtin:cloud.azure.vmScaleSet.cpuUsage | Percentage CPU | Percent (%) | autoavgmaxmin | DDUs |