---
title: Monitor Azure Virtual Machines
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vm
scraped: 2026-02-24T21:17:09.941641
---

# Monitor Azure Virtual Machines

# Monitor Azure Virtual Machines

* Latest Dynatrace
* How-to guide
* 8-min read
* Published Jul 19, 2017

Dynatrace provides a [VM Extensionï»¿](https://docs.microsoft.com/en-us/azure/virtual-machines/extensions/overview) to install OneAgent on Azure Virtual Machines. This enables you to leverage the native deployment automation features using Azure Resource Manager (ARM). The Dynatrace VM extension is available for Windows and Linux in all public Azure regions (including support for Classic Virtual Machines).

The Dynatrace OneAgent site extension doesn't include the OneAgent installer. Instead, the extension uses the Dynatrace REST API to download the installer from the cluster in the target version as set in [OneAgent updates](/docs/ingest-from/dynatrace-oneagent/oneagent-update#configure-oneagent-updates "Learn how to update OneAgent.").

## Capabilities

* Full-stack monitoring powered by OneAgent
* [Extensions for easy deployment of OneAgent](#installation)
* [Integration with Azure Monitor](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* Enhanced support for Azure VM metadata such as Azure regions, scale sets and more
* [Classic Virtual Machines](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vm/monitor-azure-virtual-machines-classic "Monitor Azure Virtual Machines (classic) and view available metrics.") are also supported

## Prerequisites

* Create a [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").
* Determine your [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
* Determine your server URL if required.

  The server URL is required only if you use an ActiveGate for a Dynatrace SaaS endpoint. The URL is automatically generated from the environment ID.

  + **ActiveGate server URL:**  
    `https://<your-active-gate-IP-or-hostname>:9999/e/<your-environment-id>/api` (the ActiveGate port is configurable)

## Install Dynatrace OneAgent VM extension

There are several ways to install the Dynatrace OneAgent VM extension: through Azure Portal, Azure CLI, or PowerShell, or by using an ARM template. Follow the steps below for instructions.

Azure Portal

Azure CLI 2.0

PowerShell

### Add the extension to an existing VM

1. In Azure Portal, go to an existing virtual machine where you want to add the OneAgent extension.
2. In the left menu, go to **Settings** and select **Extensions**.
3. Select **Add**.
4. Select **Choose extension**.
5. From the list of extensions, select **Dynatrace OneAgent**.
6. Select **Create** to add the extension.
7. On the **Install extension** page, enter your **environment ID**, your **API token**, and your **server URL**. See [Prerequisites](#prerequisites) for details.
8. Select whether you want to enable Log Monitoring.
9. Optional Define the [host group](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") to which the VM belongs.
10. Select **OK**.
11. To check the deployment status, go to **Deployment Status**.

After installation is complete, restart your applications on the VM. Immediately after restart, OneAgent will begin monitoring them.

### Add the extension to a new VM

1. During the creation of a new VM in the deployment wizard, in **Advanced**, select **Select an extension**.
2. Select **Dynatrace OneAgent**.
3. Select **Create**.
4. On the **Install extension** page, enter your **environment ID**, your **API token**, and your **server URL**. See [Prerequisites](#prerequisites) for details.
5. Select whether you want to enable Log Monitoring.
6. Optional Define the [host group](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") to which the VM belongs.
7. Select **OK**.
8. Continue VM configuration in the deployment wizard.
9. Select **Review and create**.
10. To check the deployment status, go to **Deployment Status**.

After installation is complete, restart your applications on the VM. Immediately after restart, OneAgent will begin monitoring them.

Replace all values marked with `<...>` with your actual values.

```
az vm extension set



--publisher dynatrace.ruxit



-n "<Extension-Type>"



-g "<Resource-Group>"



--vm-name "<VM-Name>"



--settings "{\"tenantId\":\"<Environment-ID>\",\"token\":\"<API-Token>\", \"server\":\"<Server-Url>\", \"enableLogAnalytics\":\"yes\", \"hostGroup\":\"<Host-Group>\"}"
```

When using the Azure CLI within PowerShell, the settings have to be formatted as a [here-stringï»¿](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_quoting_rules?view=powershell-6#here-strings).

```
--settings @'"{\"tenantId\":\"<Environment-ID>\",\"token\":\"<API-Token>\"}"'@
```

| Parameter | Required | Description |
| --- | --- | --- |
| Resource-Group | Required | Name of the resource group on which the VM is deployed. |
| VM-Name | Required | Name of the VM where you want to install the extension. |
| Extension-Type | Required | For Windows-based VMs, use `oneAgentWindows`. For Linux-based VMs, use `oneAgentLinux`. |
| tenantId | Required | The environment ID as described in [Prerequisites](#prerequisites). |
| token | Required | The PaaS token as described in [Prerequisites](#prerequisites). |
| server | Optional | The server URL, if you want to configure an alternative communication endpoint as described in [Prerequisites](#prerequisites). |
| enableLogsAnalytics | Optional | Set to `yes` if you want to enable Log Monitoring. |
| hostGroup | Optional | Define the [host group](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") to which the VM belongs. |
| overrideDefaults [1](#fn-1-1-def) | Optional | Override the default value of the timeoutâ120 seconds. For example, if you want to set the timeout to 600 seconds, add `\"overrideDefaults\": {\"downloadInstallerRequestTimeoutInSeconds\": 600}` to the `-Settings` string, you can also leave it empty `\"overrideDefaults\": {}`, or `null`. In such cases, the 120 seconds default value will apply. |

1

Available from VM extension version 2.201.1.0.

To check the deployment status, go to **Deployment Status**.

After installation is complete, restart your applications on the VM. Immediately after restart, OneAgent will begin monitoring them.

Replace all values marked with `<...>` with your actual values.

```
Set-AzureRmVmExtension



-Name Dynatrace



-Publisher dynatrace.ruxit



-ResourceGroupName "<Resource-Group>"



-Location "<Location>"



-VMName "<VM-Name>"



-ExtensionType "<Extension-Type>"



-TypeHandlerVersion "<Extension-Version>"



-Settings @{ "tenantId"="<Environment-ID>"; "token"="<API Token>";"server"="<Server-Url>"; "enableLogAnalytics"="yes"; "hostGroup"="<Host-Group>"; }
```

| Parameter | Required | Description |
| --- | --- | --- |
| Resource-Group | Required | Name of the resource group on which the VM is deployed. |
| Location | Required | Location where the VM is deployed. |
| VM-Name | Required | Name of the VM where you want to install the extension. |
| Extension-Type | Required | For Windows-based VMs, use `oneAgentWindows`. For Linux-based VMs, use `oneAgentLinux`. |
| tenantId | Required | The environment ID as described in [Prerequisites](#prerequisites). |
| token | Required | The PaaS token as described in [Prerequisites](#prerequisites). |
| Extension-Version | Optional | Required version of the extension. |
| server | Optional | The server URL, if you want to configure an alternative communication endpoint as described in [Prerequisites](#prerequisites). |
| enableLogsAnalytics | Optional | Set to `yes` if you want to enable Log Monitoring. |
| hostGroup | Optional | Define the [host group](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") to which the VM belongs. |
| overrideDefaults [1](#fn-2-1-def) | Optional | Override the default value of the timeoutâ120 seconds. For example, if you want to set the timeout to 600 seconds, add `\"overrideDefaults\": {\"downloadInstallerRequestTimeoutInSeconds\": 600}` to the `-Settings` string, you can also leave it empty `\"overrideDefaults\": {}`, or `null`. In such cases, the 120 seconds default value will apply. |

1

Available from VM extension version 2.201.1.0.

To check the deployment status, go to **Deployment Status**.

After installation is complete, restart your applications on the VM. Immediately after restart, OneAgent will begin monitoring them.

VM extension version 2.201.1.0+

With the VM extension 2.201.1.0 release, you can set the `overrideDefaults` parameter via CLI and PowerShell [installation](#installation) and via [ARM template](#arm-template).

* You can set the custom timeout (`overrideDefaults`) for the Azure VM Extension download, which is helpful in environments with a suboptimal internet connection or smaller network throughput (bandwidth).
* Your error messages became more informative, which is helpful in automated systems.
* Updating the Azure VM Extension on Windows can now be done without uninstalling it first. If the version of OneAgent changes on the tenant, you just need to install the Azure VM Extension again to install this new version.

## Install Dynatrace OneAgent VM extension via an ARM template

Alternatively to the main installation methods, you can make the Dynatrace VM extension part of your ARM templates.  
The JSON file for a virtual machine extension can be nested inside the virtual machine resource, or placed at the root or top level of a resource manager JSON template. [The placement of the JSON file affects the value of the resource name and typeï»¿](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-templates-resources#child-resources).

* The following example assumes the OneAgent extension is nested inside the virtual machine resource. When nesting the extension resource, the JSON file is placed in the "resources": [] object of the virtual machine.

  ```
  {



  "type": "extensions",



  "name": "dynatrace",



  "apiVersion": "2018-06-01",



  "location": "[resourceGroup().location]",



  "dependsOn": [



  "[concat('Microsoft.Compute/virtualMachines/', <VM-Name>)]"



  ],



  "properties": {



  "publisher": "dynatrace.ruxit",



  "type": "<Extension-Type>",



  "typeHandlerVersion": "<Extension-Version>",



  "autoUpgradeMinorVersion": true,



  "settings": {



  "tenantId": "<Environment-ID>",



  "token": "<API-Token>",



  "server": "<Server-Url>",



  "enableLogAnalytics": "yes",



  "hostGroup": "<Host-Group>"



  },



  }



  }
  ```
* When placing the extension JSON at the root of the template, the resource name includes a reference to the parent virtual machine, and the type reflects the nested configuration.

  ```
  {



  "type": "Microsoft.Compute/virtualMachines/extensions",



  "name": "<Parent-VM-Resource>/dynatrace",



  "apiVersion": "2018-06-01",



  "location": "[resourceGroup().location]",



  "dependsOn": [



  "[concat('Microsoft.Compute/virtualMachines/', <VM-Name>)]"



  ],



  "properties": {



  "publisher": "dynatrace.ruxit",



  "type": "<Extension-Type>",



  "typeHandlerVersion": "<Extension-Version>",



  "autoUpgradeMinorVersion": true,



  "settings": {



  "tenantId": "<Environment-ID>",



  "token": "<API-Token>",



  "server": "<Server-Url>",



  "enableLogAnalytics": "yes",



  "hostGroup": "<Host-Group>"



  }



  }



  }
  ```

| Parameter | Required | Description |
| --- | --- | --- |
| Parent-VM-Resource | Required | Name of the parent VM resource where you want to install the extension. Not applicable when using nested resource. |
| VM-Name | Required | Name of the VM where you want to install the extension. |
| Extension-Type | Required | For Windows-based VMs, use `oneAgentWindows`. For Linux-based VMs, use `oneAgentLinux`. |
| tenantId | Required | The environment ID as described in [Prerequisites](#prerequisites). |
| token | Required | The PaaS token as described in [Prerequisites](#prerequisites). From `2.200.0.0` version, it's recommended to pass it in `protectedSettings`. |
| Extension-Version | Optional | Required version of the extension. |
| server | Optional | The server URL, if you want to configure an alternative communication endpoint as described in [Prerequisites](#prerequisites). |
| enableLogsAnalytics | Optional | Set to `yes` if you want to enable Log Monitoring. |
| hostGroup | Optional | Define the [host group](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") to which the VM belongs. |
| overrideDefaults [1](#fn-3-1-def) | Optional | Override the default value of the timeoutâ120 seconds. For example, if you want to set the timeout to 600 seconds, add `\"overrideDefaults\": {\"downloadInstallerRequestTimeoutInSeconds\": 600}` to the ARM template in the `settings` object, you can also leave it empty `\"overrideDefaults\": {}`, or `null`. In such cases, the 120 seconds default value will apply. |

1

Available from VM extension version 2.201.1.0.

To check the deployment status, go to **Deployment Status**.

After installation is complete, restart your applications on the VM. Immediately after restart, OneAgent will begin monitoring them.

## Configure network zones Optional

To configure network zones, use the installer arguments below.

```
az vm extension set



--publisher dynatrace.ruxit



-n "oneAgentLinux"



-g "yourresourcegroup"



--vm-name "awesome-vm"



--settings "{\"tenantId\":\"myawesometenant\",\"token\":\"nope123\", \"installerArguments\":\"--set-host-group=example_hostgroup --set-monitoring-mode=fullstack --set-network-zone=<your.network.zone>\"}"
```

See [network zones](/docs/manage/network-zones "Find out how network zones work in Dynatrace.") for more information.

## Related topics

* [Set up Dynatrace on Microsoft Azure](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")