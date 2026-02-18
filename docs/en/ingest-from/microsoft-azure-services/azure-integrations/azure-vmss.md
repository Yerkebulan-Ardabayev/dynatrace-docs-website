---
title: Monitor Azure Virtual Machine Scale Set (VMSS)
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vmss
scraped: 2026-02-18T05:40:00.516970
---

# Monitor Azure Virtual Machine Scale Set (VMSS)

# Monitor Azure Virtual Machine Scale Set (VMSS)

* Latest Dynatrace
* How-to guide
* 6-min read
* Published Jul 19, 2017

## Capabilities

* Full-stack monitoring powered OneAgent
* [Extensions for easy deployment of OneAgent](#installation)
* [Integration with Azure Monitor](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* Enhanced support for Azure VM Metadata such as Azure regions, AutoScale detection, and more

Dynatrace provides a VM extension to install OneAgent on Azure Virtual Machine Scale Set (VMSS). The extension doesn't include the OneAgent installer. Instead, it uses the Dynatrace REST API to download the latest version from the cluster, unless a [default OneAgent versionï»¿](https://www.dynatrace.com/news/blog/define-default-version-oneagent-new-installations/) is configured. OneAgent updates are provided automatically.

## Prerequisites

* Create a [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").
* Determine your [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
* Determine your server URL if required.

  The server URL is required only if you use an ActiveGate for a Dynatrace SaaS endpoint. The URL is automatically generated from the environment ID.

  + **ActiveGate server URL:**  
    `https://<your-active-gate-IP-or-hostname>:9999/e/<your-environment-id>/api` (the ActiveGate port is configurable)

## Installation

The Dynatrace VM extension is available for Windows and Linux in all public Azure regions.

Azure CLI 2.0

PowerShell

1. Run the command below.

   Replace all values marked with `<...>` with your actual values.

   ```
   az vmss extension set



   --publisher dynatrace.ruxit



   -n "<Extension-Type>"



   -g "<Resource-Group>"



   --vmss-name "<VMSS-Name>"



   --settings "{\"tenantId\":\"<Environment-ID>\",\"token\":\"<API-Token>\", \"server\":\"<Server-Url>\", \"enableLogAnalytics\":\"yes\", \"hostGroup\":\"<Host-Group>\"}"
   ```

   When using the Azure CLI within PowerShell, you need to format the settings as a [here-stringï»¿](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_quoting_rules?view=powershell-6#here-strings).

   ```
   --settings @'"{\"tenantId\":\"<Environment-ID>\",\"token\":\"<API-Token>\"}"'@
   ```

   | Parameter | Required | Description |
   | --- | --- | --- |
   | Resource-Group | Required | Name of the resource group on which the VM is deployed. |
   | VMSS-Name | Required | Name of the VMSS where you want to install the extension. |
   | Extension-Type | Required | For Windows-based VMs, use `oneAgentWindows`. For Linux-based VMs, use `oneAgentLinux`. |
   | tenantId | Required | The environment ID as described in [Prerequisites](#prerequisites). |
   | token | Required | The PaaS token as described in [Prerequisites](#prerequisites). |
   | server | Optional | The server URL, if you want to configure an alternative communication endpoint as described in [Prerequisites](#prerequisites). |
   | enableLogAnalytics | Optional | Set to `yes` if you want to enable Log Monitoring. |
   | hostGroup | Optional | Define the [host group](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") to which the VM belongs. |
2. Update the VMSS virtual machines.

   ```
   az vmss update-instances --instance-ids '*' --resource-group $CLUSTER_RESOURCE_GROUP --name $SCALE_SET_NAME
   ```
3. To check the deployment status, go to **Deployment Status**.

   After installation is complete, restart your applications on the VMs. Immediately after restart, OneAgent will begin monitoring them.

1. Run the command below to apply the extension to the VMSS definition.

   Replace all values marked with `<...>` with your actual values.

   ```
   $vmss = Get-AzVmss -ResourceGroupName "<Resource-Group>" -VMScaleSetName "<VMSS-Name>"



   $vmss = Add-AzVmssExtension



   -VirtualMachineScaleSet $vmss



   -Name "dynatrace"



   -Publisher "dynatrace.ruxit"



   -Type "<Extension-Type>"



   -TypeHandlerVersion "2.300"



   -Setting @{ "tenantId"="<Environment-ID>"; "token"="<API Token>";"server"="<Server-Url>"; "enableLogAnalytics"="yes"; "hostGroup"="<Host-Group>"; }
   ```

   | Parameter | Required | Description |
   | --- | --- | --- |
   | Extension-Type | Required | For Windows-based VMs, use `oneAgentWindows`. For Linux-based VMs, use `oneAgentLinux`. |
   | tenantId | Required | The environment ID as described in [Prerequisites](#prerequisites). |
   | token | Required | The PaaS token as described in [Prerequisites](#prerequisites). |
   | server | Optional | The server URL, if you want to configure an alternative communication endpoint as described in [Prerequisites](#prerequisites). |
   | enableLogAnalytics | Optional | Set to `yes` if you want to enable Log Monitoring. |
   | hostGroup | Optional | Define the [host group](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") to which the VM belongs. |
2. Update the VMSS virtual machines with the new definition.

   ```
   Update-AzVmss



   -ResourceGroupName "<Resource-Group>"



   -Name "<VMSS-Name>"



   -VirtualMachineScaleSet $vmss
   ```

   | Parameter | Required | Description |
   | --- | --- | --- |
   | Resource-Group | Required | Name of the resource group on which the VM is deployed. |
   | VMSS-Name | Required | Name of the VMSS where you want to install the extension. |
3. To check the deployment status, go to **Deployment Status**.

   After installation is complete, restart your applications on the VM. Immediately after restart, OneAgent will begin monitoring them.

## Install Dynatrace OneAgent VM extension via an ARM template

Alternatively to the main installation methods, you can make the Dynatrace site extension part of your ARM templates.

1. Place the JSON configuration for a virtual machine extension in the VMSS resource, under `extensions` in `extensionProfile`.

   Example:

   ```
   {



   "type": "Microsoft.Compute/virtualMachineScaleSets",



   "sku": {...},



   "name": "<VMSS-Name>",



   "apiVersion": "2018-06-01",



   "location": "centralus",



   "properties": {



   "upgradePolicy": {...},



   "virtualMachineProfile": {



   "osProfile": {...},



   "storageProfile": {...},



   "networkProfile": {...},



   "extensionProfile": {



   "extensions": [



   {



   "name": "dynatrace",



   "properties": {



   "publisher": "dynatrace.ruxit",



   "type": "<Extension-Type>",



   "typeHandlerVersion": "<Extension-Version>",



   "autoUpgradeMinorVersion": true,



   "settings": {



   "tenantId": "<Environment-ID>",



   "token": "<API-Token>",



   "enableLogAnalytics": "yes"



   }



   }



   }



   ]



   }



   }



   }



   }
   ```
2. Configure the JSON file.

   ```
   {



   "name": "dynatrace",



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

   | Parameter | Required | Description |
   | --- | --- | --- |
   | Resource-Group | Required | Name of the resource group on which the VM is deployed. |
   | VMSS-Name | Required | Name of the VMSS where you want to install the extension. |
   | Extension-Type | Required | For Windows-based VMs, use `oneAgentWindows`. For Linux-based VMs, use `oneAgentLinux`. |
   | tenantId | Required | The environment ID as described in [Prerequisites](#prerequisites). |
   | token | Required | The PaaS token as described in [Prerequisites](#prerequisites). |
   | Extension-Version | Optional | Required version[1](#fn-1-1-def) of the extension. |
   | server | Optional | The server URL, if you want to configure an alternative communication endpoint as described in [Prerequisites](#prerequisites). |
   | enableLogAnalytics | Optional | Set to `yes` if you want to enable Log Monitoring. |
   | hostGroup | Optional | Define the [host group](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") to which the VM belongs. |

   1

   o fetch the list of extension versions, run

   ```
   az vm extension image list --name oneAgentLinux --publisher dynatrace.ruxit
   ```
3. To check the deployment status, go to **Deployment Status**.

   After installation is complete, restart your applications on the VM. Immediately after restart, OneAgent will begin monitoring them.

## Troubleshooting

VMSS nodes not showing up in Dynatrace

Restart the VMSS nodes via PowerShell, replacing all values marked with `<...>` with your actual values:

```
Restart-AzureRmVmss -ResourceGroupName "<Resource-Group>" -VMScaleSetName "<VMSS-Name>"
```

| Parameter | Required | Description |
| --- | --- | --- |
| Resource-Group | Required | Name of the resource group on which the Virtual Machine is deployed |
| VMSS-Name | Required | Name of the VMSS where you want to install the extension. |

## Related topics

* [Set up Dynatrace on Microsoft Azure](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")