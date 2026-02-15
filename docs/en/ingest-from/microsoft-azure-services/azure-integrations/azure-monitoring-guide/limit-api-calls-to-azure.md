---
title: Limit API calls to Azure
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/limit-api-calls-to-azure
scraped: 2026-02-15T21:23:51.542589
---

# Limit API calls to Azure

# Limit API calls to Azure

* Latest Dynatrace
* Explanation
* 3-min read
* Updated on Oct 09, 2025

When monitoring large Azure environments (thousands of resources per Azure subscription), there is a risk that Dynatrace will reach Azure API throttling limits. Follow this guide to limit API calls to Azure and help to guarantee full Azure monitoring.

## Azure throttling limits

There are two types of Azure throttled requests that we need to take into account:

1. [Throttled requests in Resource Managerï»¿](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/request-limits-and-throttling#subscription-and-tenant-limits)âAzure throttles subscription-level and tenant-level read operations.

   * Dynatrace uses Azure Resource Manager queries to collect built-in services and metrics for all services.
2. [Throttled requests in Azure Resource Graphï»¿](https://learn.microsoft.com/en-us/azure/governance/resource-graph/concepts/guidance-for-throttled-requests#understand-throttling-headers)

   * Dynatrace uses Azure Resource Graph queries to collect all services that are not built-in.

## Dynatrace Azure anti-throttling mechanism

Dynatrace collects Azure resources and metrics every 5 min by default to avoid making API calls every minute. However, the frequency of polling depends on the Azure throttling limit.

Dynatrace calculates how many requests need to be sent to Azure during the upcoming hour. If the number of expected requests exceeds the configured throttling limit (12,000 requests/hour), Dynatrace changes the polling frequency to collect data with an interval of no more than 15 minutes.

## How to avoid Azure throttling

To provide full Dynatrace monitoring, it is important to avoid Azure throttling limits. To decrease API calls to Azure, you can do one of the following.

* Adjust the Azure service principal configuration to your environment on the Azure side.
* Limit the number of monitored resources using monitoring by tags on the Dynatrace side.

See below for details.

### Azure service principal configuration

You have three options to configure [Azure service principalï»¿](https://docs.microsoft.com/en-us/azure/active-directory/develop/app-objects-and-service-principals), depending on your Azure environment.

* Recommended One Azure service principal - one Azure subscription

  + Throttling limit: 12,000 requests/hour per Azure subscription
* One big Azure subscription that exceeds the throttling limit

  Split monitoring between Azure service principals:

  + You can create several Azure service principals for the same Azure subscription setting the `--scope` of each service principal to separate Azure resource groups.
    Copy the following command and edit it to replace the placeholders with actual values as described below.

    ```
    az ad sp create-for-rbac --name <YourServicePrincipalName> --role reader --scopes /subscriptions/<YourSubscriptionID>/resourceGroups/<YourResourceGroupID> --query "{ClientID:appId,TenantID:tenant,SecretKey:password}"
    ```

    Be sure to replace the placeholders (`<...>`) with your values:

    - `<YourServicePrincipalName>` - the name of the service principal that will be created for Dynatrace to access Azure.
    - `<YourSubscriptionID>`- the name of the subscription you would like to monitor.
    - `<YourResourceGroupID>` - the name of the specific resource group you would like to monitor.
  + You can create several Azure service principals setting the `--scope` to subscription level and add multiple credentials monitoring the same Azure subscription in Dynatrace, but different services.

    For example:

    - One monitoring `Azure Virtual machines (built-in)` service
    - Another monitoring `Azure SQL (built-in)`, `Azure Storage Blob Services`, `Azure Storage Queue Services`, `Azure Storage Table Services`, and `Azure Storage File Services`, but not monitoring `Azure Virtual machines (built-in)`.

    Remember that the scope of monitored services needs to be different for each credential and must not be left with the default configuration. Otherwise, metric values for overlapping services might be incorrect.
* (not recommended) One Azure service principal - many Azure subscriptions

  If the first option is not suitable in your situation, configure an Azure service principal to monitor up to twenty Azure subscriptions.

  Remember that the number of API calls depends on how large your Azure subscriptions are. If you notice that the Dynatrace integration for Azure monitoring is not working correctly, consider decreasing the number of subscriptions per Azure service principal.

### Limit monitored resources using monitoring based on tags - Dynatrace configuration

If you don't need to monitor all Azure resources in your subscriptions, you can use monitoring by tags to decrease Azure API calls.

If you have a lot of subscriptions, monitoring based on tags might not be enough to avoid throttling, and you should still prepare a proper [Azure service principal configuration](#service-principal).

* Monitoring by tags mostly allows you to limit the calls for metrics and sub-resources (for example, Microsoft.ServiceBus/namespaces/queues for all resources of type Microsoft.ServiceBus/namespaces).
* Calls for top-level resources still need to be made for each subscription.

You can choose to monitor resources based on existing Azure tags, as Dynatrace automatically imports them from service instances.  
To monitor resources based on tags

1. Go to **Settings** > **Cloud and virtualization** > **Azure**.
2. On the Azure overview page, select the **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") icon for the Azure instance.
3. Set **Resources to be monitored** to **Monitor resources selected by tags**.
4. Enter key/value pairs to identify resources to exclude from monitoring or include in monitoring.
   You can enter multiple key/value pairs: each time you enter a pair, another empty row is displayed for you to edit as needed.
5. Select **Save** to save your configuration.

   To import the Azure tags automatically into Dynatrace, turn on **Capture Azure tags automatically**.

## Related topics

* [Microsoft Azure monitoring](/docs/observe/infrastructure-observability/cloud-platform-monitoring/azure-monitoring "Monitor Azure with Dynatrace")