---
title: Azure Native Dynatrace Service
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-platform/azure-native-integration
scraped: 2026-02-18T05:47:37.584208
---

# Azure Native Dynatrace Service

# Azure Native Dynatrace Service

* Latest Dynatrace
* Explanation
* 17-min read
* Updated on Jul 23, 2024

Azure Marketplace integration enables you to build a streamlined experience for purchasing, configuring, and managing Dynatrace directly inside the Azure portal. After setting up the integration, Dynatrace appears as an Azure native service, and you can manage its configuration from Azure Portal.

Capabilities and limitations

**Capabilities:**

* **Seamless onboarding:** Easy onboarding to Dynatrace SaaS as an integrated service on Azure via Azure Marketplace. To set up the integration:

  + No event hubs, cloud functions, or configurations are required

* **Unified billing:** Get a single bill for all the resources you consume on Azure, including all Dynatrace SaaS consumption.
* **Single sign-on:** You don't need separate credentials for the Dynatrace portal. Sign in once on the Azure portal and seamlessly transition to Dynatrace when needed.
* **Log monitoring:** Enables forwarding of subscription activity and resource logs to Dynatrace. For details, see [Log Monitoring Classic](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.").

* **OneAgent deployment:** You get a unified management experience of Dynatrace OneAgents. You can install and uninstall Dynatrace OneAgents as extensions on Azure Virtual Machines and Azure App Services.

**Limitations:**

* The integration will create a new Dynatrace environment and account; it can't run on an existing Dynatrace environment.

Azure Marketplace

The Azure Native Dynatrace service is available via the [Azure marketplaceï»¿](https://dt-url.net/9n039mv).

For getting a customized private offer for the Azure Native Dynatrace Service, reach out to Dynatrace sales via email to [sales@dynatrace.com](mailto:sales@dynatrace.com).

## Prerequisites

Activate the private plan for Azure Native Dynatrace Service

The Azure Native Dynatrace Service is available via a [private planï»¿](https://dt-url.net/3d03xln). To have Dynatrace create a private plan for you, [contact Dynatraceï»¿](https://dt-url.net/m003xf1). Once you accept the offer, the private plan for Azure Native Dynatrace Service will be accessible on Azure Marketplace.

Register the Dynatrace resource provider

To create and manage the Dynatrace resources using the Azure Portal, you need to register a Dynatrace resource provider named `Dynatrace.Observability` in your Azure subscription.

How to register the Dynatrace resource provider

On the Azure Portal

Using the Azure CLI

Follow the instructions on [Azure resource providers and typesï»¿](https://dt-url.net/fu03x5j).

Run the command below, making sure to replace `<subscription-id>` with your own subscription ID.

```
az provider register --namespace Dynatrace.Observability --subscription <subscription-id>
```

Set up permissions

#### General permissions

* You need a `Contributor` permission to the Azure subscription.

The first user creating the first Dynatrace resource and environment in a subscription becomes the Dynatrace account owner of the Dynatrace account that is created during the integration deployment. For all subsequent Dynatrace resources and environments that are created in the same subscription by other users, the account owner will also have full permissions.

#### SSO permissions

If you use Microsoft Entra ID as your identity provider, you can establish single sign-on (SSO) from the Azure portal to Dynatrace. If you use a different identity provider or you don't want to establish SSO, you can skip this section.

To enable single sign-on authentication for your Dynatrace resource, you need to [set up SSO in Microsoft Entra ID](/docs/manage/identity-access-management/user-and-group-management/access-saml/idp-specific/saml-azure#configuration "Learn how to configure Dynatrace SSO in Azure.").

After setting up SSO in Active Directory, you can enable SSO during or after the Azure integration deployment.

## Set up the integration

When you first deploy the Azure Native Dynatrace Service, a new Dynatrace environment hosted on a new Dynatrace resource is created.

* The Dynatrace resource is created in the Azure subscription and resource group that you select during the installation deployment. You can configure, manage, and troubleshoot issues on your Dynatrace resource from the Azure Portal.
* The Dynatrace environment is created in the same Azure region in which you create the Dynatrace resource. In this new environment:

  + After you [install OneAgent](#oa), you can start monitoring [metrics](/docs/analyze-explore-automate/metrics-classic "Learn about metrics classic that Dynatrace offers.") from your Azure resources. You can also collect metrics from the [default services](/docs/ingest-from/microsoft-azure-services/azure-platform/azure-native-integration#default "Set and configure your Dynatrace SaaS environment using Azure Marketplace.")
  + You can collect [logs](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.") from your Azure resources
  + You do not need an environment ActiveGate for this integration.

To set up the integration

1. Go to the Azure subscription where you want to create the Dynatrace resource.
2. Select **Resources**, and then select **Create**.
3. Search for **Azure Native Dynatrace Service**. You should see the message that a private product is available.
4. Select the tile **Azure Native Dynatrace Service**.
5. In the list for choosing a plan, select the private plan that you accepted in [Activate the private plan for Azure Native Dynatrace Service](#step-1) and then select **Subscribe**.
6. On **Create a new Dynatrace environment**, select **Create**.
7. In **Basics**, for **Resource group**, specify whether to create a new resource group or use an existing one.

   A resource group is a container that holds related resources for an Azure solution. For more information, see [Azure Resource Group overviewï»¿](https://dt-url.net/xv43x96).
8. Enter a **Resource name** for the Dynatrace resource, and then select a **Region** from the dropdown menu. The Dynatrace resource in Azure and the Dynatrace environment will be created in the selected region.
9. Select your **Pricing plan**, and then select **Next: Metrics and Logs**.
10. Optional Select whether to **Send subscription activity logs** and/or **Send Azure resource logs**. For details, see [Configure metrics and logs](#metrics-logs).

    If you select **Send Azure resource logs for all defined services**, Azure resource logs are sent for all defined resources by default, which means logs are collected for all supported resources. To filter the specific set of Azure resources sending logs to Dynatrace, you can use Azure resource tags. Tag rules are:

    * Azure resources with `Include` tags send logs to Dynatrace.
    * Azure resources with `Exclude` tags don't send logs to Dynatrace.
    * If there's a conflict between inclusion and exclusion rules, exclusion takes priority.

      There is a limit of 20 entries for either `Include` or `Exclude` tags.
11. Select **Next: Single sign-on**.
12. Optional Choose whether to **Enable SSO through Microsoft Entra ID**.

    * If you don't want to enable this feature, select **Next: Tags**.
    * If you want to enable this feature, select it, select the Dynatrace application ID that is displayed, and then select **Next: Tags**.
13. Optional [Specify tags](#tags) for the new Dynatrace resource, and then select **Next: Review + create**.
14. Verify if the information submitted is correct, and then select **Create**. When the deployment is complete, you can select **Go to resource** to navigate to the specific Dynatrace resource.

## Link multiple Azure subscriptions to one Dynatrace environment Optional

Ensure that your Azure account has access to the Dynatrace account with the following permissions:

* View Account
* View Environment
* Install OneAgent
* Manage Monitoring Settings

For more details, see [Environment permissions](/docs/manage/identity-access-management/permission-management/role-based-permissions#environment "Role-based permissions").

After deploying the Azure integration, you can:

* Link more Azure subscriptions to your newly created Dynatrace environment.
* Link more Dynatrace environments to a single Azure subscription.

  When linking multiple Azure subscriptions and creating the resource, you must have Dynatrace Account privileges `tenant-manage-settings` and `tenant-agent-install` permissions. For more information on how to configure these permissions, see [Role-based permissions](/docs/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions").

Follow the steps below, making sure to repeat the procedure for every subscription that you want to link.

1. Go to Azure Portal and search for `Azure Native Dynatrace Service` from the top search bar.
2. Select **Azure Native Dynatrace Service**.
3. Select **Create**.
4. In **Basics**, for **Resource group**, specify whether to create a new resource group or use an existing one.

   A resource group is a container that holds related resources for an Azure solution. For more information, see [Azure Resource Group overviewï»¿](https://dt-url.net/xv43x96).
5. Enter a **Resource name** and then select a **Region** from the dropdown menu.

   The Dynatrace environment to link and your new Dynatrace resource must be in the same region.
6. Select the **Dynatrace environment** to link to the Azure subscription, and then select **Next: Metrics and Logs**.
7. Optional Select whether to **Send subscription activity logs** and/or **Send Azure resource logs**. For details, see [Configure metrics and logs](#metrics-logs).

   If you select **Send Azure resource logs for all defined services**, Azure resource logs are sent for all defined resources by default, which means that logs are collected for all supported resources. To filter the specific set of Azure resources sending logs to Dynatrace, you can use Azure resource tags. Tag rules are:

   * Azure resources with `Include` tags send logs to Dynatrace.
   * Azure resources with `Exclude` tags don't send logs to Dynatrace.
   * If there's a conflict between inclusion and exclusion rules, exclusion takes priority.
8. Skip **Next: Single sign-on** (you can only configure SSO after deployment) and then select **Next: Tags**.
9. Optional [Specify tags](#tags) for the new Dynatrace resource, and then select **Next: Review + create**.
10. Verify if the information submitted is correct, and then select **Create**. When the deployment is complete, you can select **Go to resource** to navigate to the specific Dynatrace resource.

## Access your Dynatrace environment

After you set up the integration, you can access your Dynatrace environment directly from Azure Portal.

In Azure Portal, go to your Dynatrace resource and select **Overview**. All details of your Dynatrace environment will appear there, including direct links to the following web UI pages:

* **Dashboards** - For details, see [Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.").
* **Log Viewer** - For details, see [Log viewer (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer "Learn how to use Dynatrace log viewer to analyze log data.").
* **Smartscape topology** - For details, see [Visualize your environment through Smartscape Classic](/docs/analyze-explore-automate/smartscape-classic "Learn how Smartscape Classic visualizes all the entities and dependencies in your environment.").

## Configure metrics and logs

### Metrics

* You can activate [metrics](/docs/analyze-explore-automate/metrics-classic "Learn about metrics classic that Dynatrace offers.") after the Azure integration deployment.

Collect metrics from Virtual Machines and App Services

To start collecting metrics from your Virtual Machines and App Services, you need to [install Dynatrace OneAgent on these resources as an extension](#oa) .

Collect metrics from cloud services

All services and metrics are enabled by default. You can disable them if needed by selecting the delete button from the list of services.
After Dynatrace connects to your Azure environment, it immediately starts monitoring Azure's built-in services for the service principal you have defined. [Classic (formerly 'built-in') Azure metrics](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/default-azure-metrics "The list of classic metrics Dynatrace collects by default for Azure monitoring.") lists the metrics of Azure cloud services monitored by default.

### Manage cloud services

All cloud services are monitored by default, but you can quickly disable them from the list or re-enable them as needed.

To add services to monitoring

1. Go to **Settings** > **Cloud and virtualization** > **Azure**.
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

To see the complete list of Azure cloud services and learn about the metrics collected for each of them, see [All Azure cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics "Monitor Azure services with Dynatrace and view available metrics.").

Alternatively, you can check the list of supported Azure services within in-product Dynatrace Hub (search for **Azure**) or in the [web version of Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?query=azure).

To add and configure metrics

1. Go to **Settings** > **Cloud and virtualization** > **Azure**.
2. On the Azure overview page, find the connection that you want to change and select **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") in that row.
3. Under **Services**, select **Manage services**.
4. Select the service for which you want to add metrics. The service details page lists the metrics you are already monitoring for that service.
5. Select **Add metric**.
6. From the **Add new metric** list, select the metric and then select **Add metric**.
7. Select ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") to expand the metric details and configure the metric.
8. Select **Apply** to save your configuration.

After you select the cloud services and save your changes, monitoring of the newly added services starts automatically.

### Logs

* You can activate [logs](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.") either [during the Azure integration deployment](#setup) or [after deployment](#how-to-logs).

You can set up two types of logs from Azure to Dynatrace: [subscription activity logs](#activity) and [Azure resource logs](#resource).

#### Subscription activity logs

Subscription activity logs provide insights into the operations (PUT, POST, DELETE) performed on each Azure resource in your subscription (the management plane). For each Azure subscription, there's a single activity log.

#### Azure resource logs

Azure resource logs provide insights into operations that were performed within an Azure resource (the data plane), such as getting a secret from a key vault or making a request to a database. The content of resource logs varies by the Azure service and resource type.

All Azure services in the [Azure Monitor log categoriesï»¿](https://dt-url.net/fja38sr) ingest logs, including Microsoft Entra ID and [Azure Monitor Integration Serviceï»¿](https://dt-url.net/dpc38am).

For a list of Azure resource logs, see [Supported categories for Azure Monitor resource logsï»¿](https://dt-url.net/ea03xvn).

#### How to activate logs after deployment

Activate subscription activity logs

Activate Azure resource logs

1. On the Azure Portal, go to your Dynatrace resource and select **Metrics and logs**.
2. Select **Send subscription activity logs**.
3. Select **Save**.

1. On the Azure Portal, go to your Dynatrace resource and select **Metrics and logs**.
2. Select **Send Azure resource logs for all defined sources**.

   When selecting this option, Azure resource logs are sent for all defined resources by default, which means that logs are collected for all supported resources.
3. Optional If you want to filter the specific set of Azure resources sending logs to Dynatrace, you can use Azure resource tags. Tag rules are:

   * Azure resources with `Include` tags send logs to Dynatrace.
   * Azure resources with `Exclude` tags don't send logs to Dynatrace.
   * If there's a conflict between inclusion and exclusion rules, exclusion takes priority.
4. Select **Save**.

Azure Native Dynatrace Service automatically enables log forwarding in the Azure subscription where the Dynatrace resource is enabled. Log forwarding is enabled for all supported services and resources. Tag filtering rules can be defined to include or exclude certain Azure resources from sending logs.

Azure Native Dynatrace Service uses Dynatrace access token called `azure-native-integration` which is rotated every 24 hours.

## Create tags

* You can create [tags](/docs/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.") either [during the Azure integration deployment](#setup) or [after deployment](#how-to-tags).

You can apply tags to your Azure resources, resource groups, and subscriptions to logically organize them into a taxonomy. You can specify tags for the new Dynatrace resource in Azure by adding custom key/value pairs:

* For **Name**, enter the name of the tag corresponding to the Azure Dynatrace resource (for example, `owner`).
* For **Value**, enter the value of the tag corresponding to the Azure Dynatrace resource (for example, the owner's email account).

If you don't set any tags, all logs from the monitored resources on your Azure subscription are sent to Dynatrace.

### How to create tags after deployment

On the Azure Portal, go to your new Dynatrace resource, and then select **Tags**. Alternatively, you can select **Monitored resources**, and then select **Edit tags** for the desired resources.

## Manage monitored resources in Azure Portal

After deploying the Azure Native Dynatrace Service, you can view, manage, and monitor your Azure resources, and you can install OneAgent on your Azure Virtual Machines and Azure App Services.

To view your list of resources, on the Azure Portal, go to your Dynatrace resource and select **Monitored resources**. You can filter the list of resources displayed by **Resource name** (Azure resource name), **Resource type** (Azure resource type), **Resource group** (resource group name for the Azure resource), **Region** (location of the Azure resource), and **Logs to Dynatrace** (whether the resource is sending logs to Dynatrace).

## Deploy OneAgent on Azure Virtual Machines and Azure App Services

* You can deploy OneAgent after the Azure integration deployment.

To monitor your Azure Virtual Machines or Azure App Services, you can install Dynatrace OneAgent on these resources as an extension.

Install OneAgent on Virtual Machine

Install OneAgent on App Service

1. On the Azure Portal, go to your Dynatrace resource and select **Virtual Machines**.
2. Select a Virtual Machine from the list, on which you want to install the OneAgent extension.
3. Select **Install extension**.
4. Optional Select whether to enable log analytics.
5. Optional Provide a [host group](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") for OneAgent.
6. Select **OK** to start the installation process.
7. When the installation is complete, the **OneAgent status** for the selected Virtual Machine displays **Installed**.

* To see details about the installed OneAgent, select your Virtual Machine and go to **Extensions**.
* To uninstall OneAgent, select your Virtual Machine, and then select **Uninstall extension**.

1. On the Azure Portal, go to your Dynatrace resource and select **App Services**.
2. From the list, select the App Service on which you want to install the OneAgent extension.
3. Select **Install extension**.
4. Optional Select whether to enable log analytics.
5. Optional Provide a [host group](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") for OneAgent.
6. Select **OK** to start the installation process.
7. When the installation is complete, the **OneAgent status** for the selected Virtual Machine displays **Installed**.

* To see details about the installed OneAgent, select your App Service and go to **Extensions**.
* To uninstall OneAgent, select your App Service, and then select **Uninstall extension**.

If you cannot see the App Service in Dynatrace after enabling the integration, restart your App Service plan.

To run OneAgent on Virtual Machine Scale Sets with Dynatrace Azure integration, use the [Dynatrace OneAgent extension for Virtual Machines](#vm) and create a [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").

## Uninstall the Azure Native Dynatrace Service

To uninstall the Azure Native Dynatrace Service, you need to delete the Dynatrace resource. When the Dynatrace resource is deleted from Azure, logs and metrics are no longer sent to Dynatrace and all billing for Dynatrace through Azure Marketplace stops.

To delete the Dynatrace resource

1. On the Azure Portal, go to your Dynatrace resource and select **Overview**.
2. Select **Delete**.
3. Enter the name of the application you want to delete, then select **Delete**.

## How to request new features

If you have a feature request, use the [Microsoft Developer Communityï»¿](https://dt-url.net/po239hy) to suggest new features.

## Troubleshooting

* [I can't enable SSO integrationï»¿](https://dt-url.net/tq237c7)
* [I don't have permissions to configure SSO for a linked Dynatrace environmentï»¿](https://dt-url.net/3o038vp)
* [How can I get logs from an Azure subscription in another Azure tenant?ï»¿](https://dt-url.net/4rc37kk)
* [Azure resources not forwarding logs to Dynatraceï»¿](https://dt-url.net/il438i2)

## Log ingest FAQ

* [What are the limits for Azure Native Dynatrace Service log ingest?ï»¿](https://dt-url.net/ine37te)
* [How does the Azure Native Dynatrace Service logging impact Azure costs?ï»¿](https://dt-url.net/da2380g)
* [Isn't it cheaper to send data with the existing Dynatrace Azure log forwarding to Dynatrace SaaS in AWS rather than to use Azure Native Dynatrace Service?ï»¿](https://dt-url.net/bp038gb)

## Related topics

* [Microsoft Azure Integrations](/docs/ingest-from/microsoft-azure-services/azure-integrations "Set up Dynatrace deep code monitoring on Azure using OneAgent or OpenTelemetry.")