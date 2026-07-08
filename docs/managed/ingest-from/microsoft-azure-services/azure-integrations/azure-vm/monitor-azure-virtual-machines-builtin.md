---
title: Monitor Azure Virtual Machines (built-in)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-vm/monitor-azure-virtual-machines-builtin
---

# Monitor Azure Virtual Machines (built-in)

# Monitor Azure Virtual Machines (built-in)

* How-to guide
* 1-min read
* Published Jul 27, 2022

Dynatrace ingests metrics from Azure Metrics API for **Azure Virtual Machines and Azure Virtual Machine Scale Sets**. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Environment ActiveGate
* To disable monitoring of built-in services, you need Environment ActiveGate version 1.245+ and Dynatrace version 1.247+.

This service monitors Azure Virtual Machines (`Microsoft.Compute/virtualMachines`) and Virtual Machine Scale Sets (`Microsoft.Compute/virtualMachineScaleSets`) with Uniform orchestration mode.

You can find the already monitored resources on the Azure overview page in the **VMs** and **Scale sets** sections. To monitor resources of type `Microsoft.ClassicCompute/virtualMachines`, check **Azure Virtual Machine (classic)** and the **Cloud services** section on the Azure overview page.

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view Azure service metrics in your Dynatrace environment on the Azure subscription page or on your own dashboard.

Values in the table depend upon the selected timeframe. For more details, see [Troubleshoot timeframe comparison for Azure monitoring setup)﻿](https://dt-url.net/7j438f0).

### View metrics on the Azure account page

To access metrics on the Azure account page

1. Go to **Azure**.
2. Choose the Azure subscription.
3. Select the service whose metrics you want to check. Metrics for the selected service are visible under the infographic in the service section, similarly to the example below.

   ![Azure service metrics](https://dt-cdn.net/images/azure-service-1109-9488bfa5e4.png)

   Azure service metrics

### View metrics on a dashboard

You can create your own dashboard for viewing Azure service metrics. For information on how to create dashboards, see [Create and edit Dynatrace dashboards](/managed/analyze-explore-automate/dashboards-classic/dashboards/create-dashboards "Learn how to create and edit Dynatrace dashboards.").

## Available metrics

### Azure Virtual Machines

| Metric key | Name | Unit | Aggregations | Monitoring consumption |
| --- | --- | --- | --- | --- |
| builtin:cloud.azure.vm.disk.read | Disk read bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.vm.disk.readOps | Disk read operations per sec | Per second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.vm.disk.write | Disk write bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.vm.disk.writeOps | Disk write operations per sec | Per second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.vm.network.bytesIn | Network in bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.vm.network.bytesOut | Network out bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.vm.cpuUsage | Percentage CPU | Percent (%) | autoavgmaxmin | DDUs |

### Azure Virtual Machines region

| Metric key | Name | Unit | Aggregations | Monitoring consumption |
| --- | --- | --- | --- | --- |
| builtin:cloud.azure.region.vms.initializing | Number of starting VMs in region | Count | autoavgmaxmin | Host units |
| builtin:cloud.azure.region.vms.running | Number of active VMs in region | Count | autoavgmaxmin | Host units |
| builtin:cloud.azure.region.vms.stopped | Number of stopped VMs in region | Count | autoavgmaxmin | Host units |

### Azure Virtual Machine Scale Sets

| Metric key | Name | Unit | Aggregations | Monitoring consumption |
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