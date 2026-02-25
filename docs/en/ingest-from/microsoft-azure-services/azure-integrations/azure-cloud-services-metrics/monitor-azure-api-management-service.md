---
title: Azure API Management Service monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-api-management-service
scraped: 2026-02-25T21:26:34.063881
---

# Azure API Management Service monitoring

# Azure API Management Service monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Nov 15, 2023

For information about differences between classic services and other services, see [Migrate from Azure classic (formerly 'built-in') services to cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Migrate Azure classic services to their new versions.").

Dynatrace ingests metrics from Azure Metrics API for Azure API Management Service. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

## Available metrics

This service monitors a part of Azure API Management (Microsoft.ApiManagement/service). While you have this service configured, you can't have Azure Application Service (built-in) (depracated) service turned on.

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| Overall duration of gateway requests | Overall Duration of Gateway Requests in milliseconds | Location, Hostname | MilliSecond |  |
| Duration of backend requests | Duration of Backend Requests in milliseconds | Location, Hostname | MilliSecond |  |
| Capacity | Utilization metric for ApiManagement service. Note: For skus other than Premium, 'Max' aggregation will show the value as 0. | Location | Percent | Applicable |
| Total event hub events | Number of events sent to EventHub | Location | Count | Applicable |
| Successful event hub events | Number of successful EventHub events | Location | Count | Applicable |
| Failed event hub events | Number of failed EventHub events | Location | Count | Applicable |
| Rejected event hub events | Number of rejected EventHub events (wrong configuration or unauthorized) | Location | Count |  |
| Throttled event hub events | Number of throttled EventHub events | Location | Count |  |
| Timed out event hub events | Number of timed out EventHub events | Location | Count |  |
| Dropped event hub events | Number of events skipped because of queue size limit reached | Location | Count |  |
| Size of event hub events | Total size of EventHub events in bytes | Location | Byte |  |
| Requests | Gateway request metrics with multiple dimensions | Location, Hostname, Last error reason, Backend response code, Gateway response code, Backend response code category, Gateway response code category | Count | Applicable |
| Network connectivity status of resources (preview) | Network Connectivity status of dependent resource types from API Management service | Location, Resource type | Count |  |
| Web socket messages (preview) | Count of WebSocket messages based on selected source and destination | Location, Source, Destination | Count |  |
| Web socket connection attempts (preview) | Count of WebSocket connection attempts based on selected source and destination | Location, Source, Destination, State | Count |  |