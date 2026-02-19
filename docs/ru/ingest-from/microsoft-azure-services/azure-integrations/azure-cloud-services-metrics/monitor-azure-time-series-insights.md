---
title: Azure Time Series Insights (Environment, Event Source) monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-time-series-insights
scraped: 2026-02-19T21:25:30.656854
---

# Azure Time Series Insights (Environment, Event Source) monitoring

# Azure Time Series Insights (Environment, Event Source) monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Sep 23, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Time Series Insights (Environment, Event Source). You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
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

![Timeseries](https://dt-cdn.net/images/2021-03-12-11-41-03-1622-e3c1ff7533.png)

![Time series event sources](https://dt-cdn.net/images/azure-time-series-insights-event-sources-dashboard-1920-7ec38ddb3d.png)

## Available metrics

| Name | Description | Unit | Recommended (Environment) | Recommended (Event Source) |
| --- | --- | --- | --- | --- |
| IngressReceivedMessages | The number of messages read from all Event Hub or IoT Hub event sources | Count | Applicable | Applicable |
| IngressReceivedInvalidMessages | The number of invalid messages read from the event source | Count | Applicable | Applicable |
| IngressStoredBytes | The total size of events successfully processed and available for query | Byte | Applicable | Applicable |
| IngressReceivedBytes | The number of bytes read from all event sources | Byte | Applicable | Applicable |
| IngressStoredEvents | The number of flattened events successfully processed and available for query | Count | Applicable | Applicable |
| IngressReceivedMessagesTimeLag | The difference between the time that the message is enqueued in the event source and the time it is processed in ingress | Second | Applicable | Applicable |
| IngressReceivedMessagesCountLag | The difference between the sequence number of the last enqueued message in the event source partition and the sequence number of messages being processed in ingress | Count | Applicable | Applicable |
| WarmStorageMaxProperties | The maximum number of properties used allowed by the environment for S1/S2 SKU and the maximum number of properties allowed by warm store for PAYG SKU | Count | Applicable |  |
| WarmStorageUsedProperties | The number of properties used by the environment for S1/S2 SKU and number of properties used by warm store for PAYG SKU | Count | Applicable |  |