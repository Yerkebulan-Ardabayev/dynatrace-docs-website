---
title: Azure Native Dynatrace Service
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-native-integration
---

# Azure Native Dynatrace Service

# Azure Native Dynatrace Service

* Explanation
* 17-min read
* Updated on Jun 23, 2026

Azure Native Dynatrace service is an Azure Native Integration available in [Azure Marketplace﻿](https://dt-url.net/9n039mv). It allows you to purchase, set up, and manage Dynatrace directly in the Azure portal. After integration deployment, you'll see Dynatrace as **Azure Native Dynatrace Service**, and you can manage its configuration from the Azure portal.

This integration has been developed and is managed by both Microsoft and Dynatrace.

Capabilities and limitations

Capabilities:

* **Integrated onboarding:** Create and manage Dynatrace as a native Azure service after purchasing the integration through configuration or Marketplace.

* **Unified billing:** When you purchase Dynatrace SaaS through the Azure Marketplace, your Dynatrace license consumption becomes a part of your regular Azure bill. This means that you can manage Dynatrace as a native Azure service and use your organization's Microsoft Azure consumption commitment for Dynatrace purchases visible on a single, consolidated Azure invoice.
* **Single sign-on:** Enable SSO through Azure Active Directory instead of configuring separate authentication to the Dynatrace portal.
* **Ingest Azure Metrics and Logs**: Set up automatic monitoring for Azure Monitor metrics, Azure subscription activity, and resource logs.

* **OneAgent deployment:** Install and uninstall Dynatrace OneAgent as an extension on Azure Virtual Machines, Azure App Services, [Arc-enabled servers](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-arc-enabled-servers "Azure integration with ARC servers"), and Azure Kubernetes Service.
* **Manage Dynatrace**: Verify which resources are sending Azure metrics and logs to Dynatrace and make instant changes as needed.
* **Scale automation**: Manage Dynatrace resources from the Azure CLI, Terraform, and Pulimi (IaC) tools to further extend resources deployment.

Limitations:

* The integration will create a new Dynatrace environment and account; it can't run on an existing Dynatrace SaaS environment.
* The integration works across a single Entra ID environment.

Azure Marketplace

You can access the Azure Native Dynatrace service through the [Azure Marketplace﻿](https://dt-url.net/9n039mv).

To receive a customized private offer for the Azure Native Dynatrace Service, please contact your Dynatrace account team or send an email to Dynatrace sales ([sales@dynatrace.com](mailto:sales@dynatrace.com)).

Alternatively, you can start a free 30-day trial of the Azure Native Dynatrace Service by subscribing to the "Dynatrace for Azure Trial" plan.

## Prerequisites

To prepare for the purchase of Azure Native Dynatrace Service through the Marketplace, do the following:

* [Get your Azure Billing Account ID﻿](https://learn.microsoft.com/en-us/marketplace/private-offers-pre-check#locate-your-billing-account-id) and identify the Azure subscription where you want to deploy Azure Native Dynatrace Service.
* [Get your private offer eligibility report﻿](https://learn.microsoft.com/en-us/marketplace/private-offers-eligibility-report#run-the-report) and share it with your Dynatrace team.
* Check your Azure Marketplace purchase controls. If you organization already has a private Azure Marketplace:

  + Enable Marketplace purchases for the Azure subscription under your billing ID.
  + Ensure that your Azure tenant's global administrator assigned the `Marketplace admin` role to the user managing the private Marketplace store.
  + Go to **Gallery**, and add the Dynatrace Marketplace listing to **Collection Items**.
* Ensure that users responsible the purchase of the private offer have sufficient permissions to accept and subscribe to the offer.

The Azure Native Dynatrace Service is available via a [private offer﻿](https://dt-url.net/3d03xln). To have Dynatrace create a private offer for you, [contact Dynatrace﻿](https://dt-url.net/m003xf1). Once you accept the offer, the Azure Native Dynatrace Service will be available in the Azure Marketplace.

### Day of purchase checklist

On the day of purchase, make sure that you're prepared for the operation by doing the following:

1. **Accept the private offer**: Carefully review the terms provided in the Private offer and accept the offer through the Azure Marketplace.

   You need a `Billing Account Owner` or `Enterprise Administrator` permission to accept the private offer.
2. **Purchase the Azure Native Dynatrace Service**: For SaaS products purchased through the Azure Marketplace, accepting the offer and the actual purchase are two distinct steps.

   To create a Dynatrace resource, you need an `Owner` or `Contributor` level access to the Azure subscription where the deployment will occur.
3. **Create and configure the Dynatrace resource**: During the purchase process, follow the described steps to create and manage the Dynatrace resource as needed.

### Set up permissions

#### Azure portal

To create a Dynatrace resource in your Azure subscription, you need to have at least a `Contributor` permission. However, we recommend that you get `Owner` permissions to ensure that all Azure Native Dynatrace Integrations work properly, including sending Azure Monitor metrics to Dynatrace.

If you set up the Dynatrace resource with `Contributor` permissions, you'll also need to manually grant the privileges of the managed identity associated with the Dynatrace resource, `Monitoring Reader`, for any subscriptions where you want to send Azure Monitor metrics to Dynatrace.

#### Dynatrace

On the Dynatrace side, the Azure portal user who created the first Dynatrace resource and environment becomes the owner of the Dynatrace account that's created during the integration deployment. The account owner's permissions can be delegated to others.

## Set up the integration

When you first deploy the Azure Native Dynatrace resource in your Azure subscription, a new Dynatrace environment hosted in Azure is created for you.

* The Dynatrace environment is created in the same Azure region in which you create the Dynatrace resource. In this new Azure Native integrated environment:

  + You can [install OneAgent](#oa) to enable monitoring for various Azure compute resources.
  + You can monitor [metrics](/managed/analyze-explore-automate/metrics-classic "Learn about metrics classic that Dynatrace offers.") from your Azure resources. You can also set up metrics for the [default services](/managed/ingest-from/microsoft-azure-services/azure-native-integration#default "Set and configure your Dynatrace SaaS environment using Azure Marketplace.").
  + You can collect [logs](/managed/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.") from your Azure resources.

To set up the integration

1. In Azure subscription, expand your private offer and select **Purchase**.
2. On **Create a new Dynatrace environment**, select **Create**.
3. In **Basics**, for **Resource group**, specify whether to create a new resource group or use an existing one.

   A resource group is a container that holds related resources for an Azure solution. For more information, see [Azure Resource Group overview﻿](https://dt-url.net/xv43x96).
4. Enter a **Resource name** for the Dynatrace resource, and then select a **Region** from the dropdown menu. The Dynatrace resource in Azure and the Dynatrace environment will be created in the selected region.

   For a list of supported Azure regions where you can create Azure Native Dynatrace resources, see [Data storage](/managed/manage/data-privacy-and-security/data-security/data-security-controls#data-storage "Learn about data security and operational security controls.").
5. Ensure that the billing term and private offer price are the same as the terms aligned in the private offer.
6. At the bottom of the page, provide your name and your company name to create a Dynatrace account, and then select **Next: Metrics and Logs**.
7. Optional Select whether to **Send subscription activity logs** and/or **Send Azure resource logs**. For details, see [Configure metrics and logs](#metrics-logs).

   If you select **Send Azure resource logs for all defined services**, Azure will automatically send logs for all supported resources. To collect logs only from specific Azure resources in Dynatrace, you can use Azure resource tags. The tagging rules are as follows:

   * Azure resources with `Include` tags send logs to Dynatrace.
   * Azure resources with `Exclude` tags don't send logs to Dynatrace.
   * If there's a conflict between inclusion and exclusion rules, exclusion takes priority.

   There is a limit of 20 entries for either `Include` or `Exclude` tags.
8. Select **Next: Single sign-on**.
9. Optional Choose whether to enable **SSO through Microsoft Entra ID**.

   * If you don't want to enable this feature, select **Next: Tags**.
   * If you want to enable this feature, select it, select the Dynatrace application ID that is displayed, and then select **Next: Tags**.
10. Optional [Specify Azure tags](#tags) for the new Dynatrace resource, and then select **Next: Review and create**.
11. Verify if the information submitted is correct, and then select **Create**. When the deployment is complete, you can select **Go to resource** to navigate to the specific Dynatrace resource.

## Link multiple Azure subscriptions to one Dynatrace environment Optional

Ensure that your Azure account has access to the Dynatrace account with the following permissions:

* `View Account`
* `View Environment`
* `Install OneAgent`
* `Manage Monitoring Settings`

For more details, see [Environment permissions](/managed/manage/identity-access-management/permission-management/role-based-permissions#environment "Role-based permissions").

After deploying the first Dynatrace environment with Azure Native integration, you can:

* Link additional Azure subscriptions to your newly created Dynatrace environment.
* Link more Dynatrace environments to a single Azure subscription.

  When linking multiple Azure subscriptions and creating the resource, you must have Dynatrace Account privileges `tenant-manage-settings` and `tenant-agent-install` permissions. For more information on how to configure these permissions, see [Role-based permissions](/managed/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions").

Follow the steps below, making sure to repeat the procedure for every subscription that you want to link.

1. Go to the Azure portal and search for `Azure Native Dynatrace Service` from the top search bar.
2. Select **Azure Native Dynatrace Service**.
3. Select **Create**.
4. In **Basics**, for **Resource group**, specify whether to create a new resource group or use an existing one.

   A resource group is a container that holds related resources for an Azure solution. For more information, see [Azure Resource Group overview﻿](https://dt-url.net/xv43x96).
5. Enter a **Resource name** and then select a **Region** from the dropdown menu.

   The Dynatrace environment to link and your new Dynatrace resource must be in the same region.
6. Select the **Dynatrace environment** to link to the Azure subscription, and then select **Next: Metrics and Logs**.
7. Optional Select whether to **Send subscription activity logs** and/or **Send Azure resource logs**. For details, see [Configure metrics and logs](#metrics-logs).

   If you select **Send Azure resource logs for all defined services**, Azure will automatically send logs for all supported resources. To collect logs only from specific Azure resources in Dynatrace, you can use Azure resource tags. The tagging rules are as follows:

   * Azure resources with `Include` tags send logs to Dynatrace.
   * Azure resources with `Exclude` tags don't send logs to Dynatrace.
   * If there's a conflict between inclusion and exclusion rules, exclusion takes priority.

   There is a limit of 20 entries for either `Include` or `Exclude` tags.
8. Skip **Next: Single sign-on** since you can only configure SSO after deployment, then select **Next: Tags**.
9. Optional [Specify tags](#tags) for the new Dynatrace resource, and then select **Next: Review and create**.
10. Verify if the information submitted is correct, and then select **Create**. When the deployment is complete, you can select **Go to resource** to navigate to the specific Dynatrace resource.

## Access your Dynatrace environment

After you set up the integration, you can access your Dynatrace environment directly from Azure portal.

In the Azure portal, go to your Dynatrace resource and select **Overview**. All details of your Dynatrace environment will appear there, including direct links to the following web UI pages:

* **Dashboards** - For details, see [Dashboards](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.").
* **Log Viewer** - For details, see [Log viewer (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer "Learn how to use Dynatrace log viewer to analyze log data.").
* **Smartscape topology** - For details, see [Visualize your environment through Smartscape](/managed/analyze-explore-automate/smartscape-classic "Learn how Smartscape visualizes all the entities and dependencies in your environment.").

## Configure metrics and logs

### Metrics

You can activate [metrics](/managed/analyze-explore-automate/metrics-classic "Learn about metrics classic that Dynatrace offers.") after the Azure integration deployment.

Collect metrics from Virtual Machines, App Services, and Azure Kubernetes Service

To start collecting metrics from your Virtual Machines, App Services, and Azure Kubernetes Service, you need to [install Dynatrace OneAgent on these resources as an extension](#oa) .

Collect metrics from cloud services

All services and metrics are enabled by default. You can disable them if needed by selecting the delete button from the list of services. After Dynatrace connects to your Azure environment, it immediately starts monitoring Azure's built-in services for the service principal you have defined. [Azure Cloud Services](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/default-azure-metrics "The list of classic metrics Dynatrace collects by default for Azure monitoring.") page lists the metrics of Azure cloud services monitored by default.

### Manage cloud services

All cloud services are monitored by default, but you can quickly disable them from the list or re-enable them as needed.

To add services to monitoring

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Cloud and virtualization** > **Azure**.
2. On the Azure overview page, find the connection that you want to change and select **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") in that row.
3. Under **Services**, select **Manage services**.
4. For each service that you want to add: select **Add service**, select the service from the list, and then select **Add service**.
5. Select **Save changes** to save your configuration.

Configuration of collected metrics per service

After you add a service, Dynatrace automatically starts collecting a set of metrics for that service.

Recommended metrics:

* Are enabled by default and can't be disabled.
* Can come with recommended dimensions (enabled by default, can't be disabled) and optional dimensions (disabled by default, can be enabled).

Apart from the recommended metrics, most services offer the possibility of enabling optional metrics that can be added and configured manually.

List of Azure cloud services and collected metrics

To see the complete list of Azure cloud services and learn about the metrics collected for each of them, see [All Azure cloud services](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics "Monitor Azure services with Dynatrace and view available metrics.").

Alternatively, you can check the list of supported Azure services within the in-product Dynatrace Hub (search for **Azure**) or in the [web version of Dynatrace Hub﻿](https://www.dynatrace.com/hub/?query=azure).

To add and configure metrics

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Cloud and virtualization** > **Azure**.
2. On the Azure overview page, find the connection that you want to change and select **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") in that row.
3. Under **Services**, select **Manage services**.
4. Select the service for which you want to add metrics. The service details page lists the metrics you are already monitoring for that service.
5. Select **Add metric**.
6. From the **Add new metric** list, select the metric and then select **Add metric**.
7. Select ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") to expand the metric details and configure the metric.
8. Select **Apply** to save your configuration.

After you select the cloud services and save your changes, monitoring of the newly added services starts automatically.

### Logs

* You can activate [logs](/managed/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.") either [during the Azure integration deployment](#setup) or [after deployment](#how-to-logs).
* You can set up two types of Azure logs to Dynatrace: [Subscription activity logs](#activity) and [Azure resource logs](#resource).
* You can send logs from your Azure Entra ID domain by doing the following:

  + Create a diagnostics settings.
  + Set the sending destination to a partner solution.

#### Subscription activity logs

Subscription activity logs provide insights into the operations (PUT, POST, DELETE) performed on each Azure resource in your subscription (the management plane). For each Azure subscription, there's a single activity log.

#### Azure resource logs

Azure resource logs provide insights into operations that were performed within an Azure resource (the data plane), such as getting a secret from a key vault or making a request to a database. The content of resource logs varies by the Azure service and resource type.

All Azure services in the [Azure Monitor log categories﻿](https://dt-url.net/fja38sr) ingest logs, including Microsoft Entra ID and [Azure Monitor Integration Service﻿](https://dt-url.net/dpc38am).

For a list of Azure resource logs, see [Supported categories for Azure Monitor resource logs﻿](https://dt-url.net/ea03xvn).

#### Entra ID activity logs

The data collected in your Microsoft Entra logs allows you to:

* Monitor many aspects of your Microsoft Entra environment.
* Determine how your users utilize your apps and services.
* Detect potential risks affecting the health of your environment.
* Troubleshoot issues preventing your users from getting their work done.
* Gain insights by viewing audit events of changes to your Microsoft Entra directory.

Entra ID provides several types of logs, such as audit logs, sign-in logs, and provisioning logs. To send Microsoft Entra ID logs to Dynatrace, you need to set Dynatrace as a destination in Microsoft Entra ID diagnostic settings.

#### How to activate logs after deployment

Activate subscription activity logs

Activate Azure resource logs

Activate Azure Entra ID logs

1. In the Azure portal, go to your Dynatrace resource and select **Metrics and logs**.
2. Select **Send subscription activity logs**.
3. Select **Save**.

1. In the Azure portal, go to your Dynatrace resource and select **Metrics and logs**.
2. Select **Send Azure resource logs for all defined sources**.

   When selecting this option, Azure resource logs are sent for all defined resources by default, which means that logs are collected for all supported resources.
3. Optional If you want to filter the specific set of Azure resources sending logs to Dynatrace, you can use Azure resource tags. Tag rules are:

   * Azure resources with `Include` tags send logs to Dynatrace.
   * Azure resources with `Exclude` tags don't send logs to Dynatrace.
   * If there's a conflict between inclusion and exclusion rules, exclusion takes priority.
4. Select **Save**.

1. Sign in to the Microsoft Entra admin center.

   To sign in to the Microsoft Entra admin center, you need at least a `Security Administrator` role.
2. Go to **Entra ID** > **Monitoring & health** > **Diagnostic settings**. You'll see **General settings** by default, and existing diagnostic settings will be visible in a table.
3. Select **Edit settings** to change an existing setting or select **Add diagnostic setting** to create a new setting.
4. In **Categories**, select which logs you want to include.
5. In **Destination Details**, select **Send to partner solutions**.
6. Select the **Subscription** and **Dynatrace environment** where you want to send the data.

Azure Native Dynatrace Service automatically enables log forwarding in the Azure subscription where the Dynatrace resource is enabled. Log forwarding is enabled for all supported services and resources. Tag filtering rules can be defined to include or exclude certain Azure resources from sending logs.

Azure Native Dynatrace Service uses a Dynatrace access token called `azure-native-integration` which is rotated every 24 hours.

## Create tags

* You can create [tags](/managed/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.") either [during the Azure integration deployment](#setup) or [after deployment](#how-to-tags).

You can apply tags to your Azure resources, resource groups, and subscriptions to logically organize them into a taxonomy. You can specify tags for the new Dynatrace resource in Azure by adding custom key/value pairs:

* For **Name**, enter the name of the tag corresponding to the Azure Dynatrace resource (for example, `owner`).
* For **Value**, enter the value of the tag corresponding to the Azure Dynatrace resource (for example, the owner's email account).

If you don't set any tags, all logs from the monitored resources on your Azure subscription are sent to Dynatrace.

### How to create tags after deployment

In the Azure portal, go to your new Dynatrace resource, and then select **Tags**. Alternatively, you can select **Monitored resources**, and then select **Edit tags** for the desired resources.

## Manage monitored resources in the Azure portal

After deploying the Azure Native Dynatrace Service, you can view, manage, and monitor your Azure resources, and you can install OneAgent on your Azure Virtual Machines and Azure App Services.

To view your list of resources that are sending logs and metrics data to Dynatrace, in the Azure portal, go to your Dynatrace resource and select **Monitored resources**. You can filter the list of resources displayed by **Resource name** (Azure resource name), **Resource type** (Azure resource type), **Resource group** (resource group name for the Azure resource), **Region** (location of the Azure resource), and **Logs to Dynatrace** (whether the resource is sending logs to Dynatrace).

## Deploy OneAgent on Azure Virtual Machines and Azure App Services

* You can deploy OneAgent after the Azure integration deployment.

To monitor your Azure Virtual Machines or Azure App Services, you can install Dynatrace OneAgent on these resources as an extension.

Install OneAgent on Virtual Machine

Install OneAgent on App Service

Install OneAgent on Azure Kubernetes Services

1. In the Azure portal, go to your Dynatrace resource and select **Virtual Machines**.
2. Select a Virtual Machine from the list, on which you want to install the OneAgent extension.
3. Select **Install extension**.
4. Optional Select whether to enable log analytics.
5. Optional Provide a [host group](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") for OneAgent.
6. Select **OK** to start the installation process.
7. When the installation is complete, the **OneAgent status** for the selected Virtual Machine displays **Installed**.

* To see details about the installed OneAgent, select your Virtual Machine and go to **Extensions**.
* To uninstall OneAgent, select your Virtual Machine, and then select **Uninstall extension**.

1. In the Azure portal, go to your Dynatrace resource and select **App Services**.
2. From the list, select the App Service on which you want to install the OneAgent extension.
3. Select **Install extension**.
4. Optional Select whether to enable log analytics.
5. Optional Provide a [host group](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") for OneAgent.
6. Select **OK** to start the installation process.
7. When the installation is complete, the **OneAgent status** for the selected Virtual Machine displays **Installed**.

* To see details about the installed OneAgent, select your App Service and go to **Extensions**.
* To uninstall OneAgent, select your App Service, and then select **Uninstall extension**.

1. In the Azure portal, go to your Dynatrace resource and select **Azure Kubernetes Service**.
2. From the list, select the Kubernetes cluster where you want to install the OneAgent Operator.
3. Select **Install extension**.
4. Select **OK** to start the installation process on the selected Azure Kubernetes cluster.
5. When the installation is complete, you can see OneAgent status for the selected Kubernetes clusters.

* To see the installed OneAgent details, select your Azure Kubernetes Service, and go to **Extensions and Applications**.
* To uninstall OneAgent Operator, select your Azure Kubernetes Service, and then select **Uninstall extension**.

If you cannot see the App Service in Dynatrace after enabling the integration, restart your App Service plan.

To run OneAgent on Virtual Machine Scale Sets with Dynatrace Azure integration, use the [Dynatrace OneAgent extension for Virtual Machines](#vm) and create a [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").

## Uninstall the Azure Native Dynatrace Service

To uninstall the Azure Native Dynatrace Service, you need to delete the Dynatrace resource. When the Dynatrace resource is deleted from Azure, logs and metrics are no longer sent to Dynatrace and all billing for Dynatrace through Azure Marketplace stops.

To delete the Dynatrace resource

1. In the Azure portal, go to your Dynatrace resource and select **Overview**.
2. Select **Delete**.
3. Enter the name of the application you want to delete, then select **Delete**.

## Start a free trial of Azure Native Dynatrace Service

Azure Marketplace offers a 30-day free trial of Azure Native Dynatrace Service. You can sign up using the trial plan published by Dynatrace. Before the free trial expires, you can upgrade it to a private offer customized for your organization.

To start your free trial

1. In the Azure portal, go to **Marketplace** and select **Azure Native Dynatrace Service**.
2. In the **Plan** dropdown, select **Dynatrace for Azure Trial**, then select **Subscribe**.
3. Follow the [setup](#setup) steps to set up the Azure Native Dynatrace Service.
4. Once the trial is finished:

   * If you decide to continue using Azure Native Dynatrace Service integration, purchase Dynatrace through the Azure Marketplace by selecting **Upgrade to Paid** in the **Azure resource**.
   * If you decide not to purchase Dynatrace, [uninstall Azure Native Dynatrace Service](#uninstall).

## How to request new features

If you have a feature request, use the [Microsoft Developer Community﻿](https://dt-url.net/po239hy) to suggest new features.

## Troubleshooting

* [I can't enable SSO integration﻿](https://dt-url.net/tq237c7)
* [I don't have permissions to configure SSO for a linked Dynatrace environment﻿](https://dt-url.net/3o038vp)
* [How can I get logs from an Azure subscription in another Azure tenant?﻿](https://dt-url.net/4rc37kk)
* [Azure resources not forwarding logs to Dynatrace﻿](https://dt-url.net/il438i2)

## Log ingest FAQ

* [What are the limits for Azure Native Dynatrace Service log ingest?﻿](https://dt-url.net/ine37te)
* [How does the Azure Native Dynatrace Service logging impact Azure costs?﻿](https://dt-url.net/da2380g)
* [Isn't it cheaper to send data with the existing Dynatrace Azure log forwarding to Dynatrace SaaS in AWS rather than to use Azure Native Dynatrace Service?﻿](https://dt-url.net/bp038gb)

## Related topics

* [Microsoft Azure Integrations](/managed/ingest-from/microsoft-azure-services/azure-integrations "Set up Dynatrace deep code monitoring on Azure using OneAgent or OpenTelemetry.")
* [Microsoft Azure Native Dynatrace Service﻿](https://learn.microsoft.com/en-us/azure/partner-solutions/dynatrace/)