---
title: Azure Power BI Embedded monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-power-bi
scraped: 2026-02-19T21:34:17.112816
---

# Azure Power BI Embedded monitoring

# Azure Power BI Embedded monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 10, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Power BI Embedded. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.201+
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

![Power bi](https://dt-cdn.net/images/dashboard-61-1468-85d8a9b03d.png)

## Available metrics

| Name | Description | Unit | Dimensions | Recommended |
| --- | --- | --- | --- | --- |
| QueryDuration | DAX query duration in last interval | MilliSecond |  | Applicable |
| QueryPoolJobQueueLength | Number of jobs in the queue of the query thread pool | Count |  | Applicable |
| memory\_metric | Memory ranging 0-3 GB for A1, 0-5 GB for A2, 0-10 GB for A3, 0-20 GB for A4, 0-50 GB for A5, and 0-100 GB for A6 | Byte |  | Applicable |
| memory\_thrashing\_metric | Average memory thrashing | Percent |  |  |
| qpu\_high\_utilization\_metric | QPU high utilization in last minute, `1` for high QPU utilization, otherwise `0` | Count |  |  |
| qpu\_metric | QPU ranging 0-100 for S1, 0-200 for S2, and 0-400 for S4 | Count |  | Applicable |
| workload\_memory\_metric | The usage of memory in your capacity resource per workload | Byte | Workload | Applicable |
| workload\_qpu\_metric | The query processing unit (QPU) load on your capacity, per workload | Count | Workload | Applicable |