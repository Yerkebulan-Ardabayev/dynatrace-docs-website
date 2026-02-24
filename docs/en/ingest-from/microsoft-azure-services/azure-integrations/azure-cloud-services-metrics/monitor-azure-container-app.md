---
title: Azure Container App monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-container-app
scraped: 2026-02-24T21:34:31.806486
---

# Azure Container App monitoring

# Azure Container App monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Aug 31, 2023

Dynatrace ingests metrics from Azure Metrics API for Azure Container App. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

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

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| Reserved cores | Number of reserved cores for container app revisions | Revision | Count | Applicable |
| Replica count | Number of replicas count of container app | Revision | Count | Applicable |
| Requests | Requests processed | Replica, Revision, Status code, Status code category | Count | Applicable |
| Replica restart count | Restart count of container app replicas | Replica, Revision | Count | Applicable |
| Network in bytes | Network received bytes | Replica, Revision | Byte | Applicable |
| Total reserved cores | Number of total reserved cores for the container app |  | Count | Applicable |
| Network out bytes | Network transmitted bytes | Replica, Revision | Byte | Applicable |
| CPU usage | CPU consumed by the container app, in nano cores. 1,000,000,000 nano cores = 1 core | Replica, Revision | Count | Applicable |
| Memory working set bytes | Container App working set memory used in bytes. | Replica, Revision | Byte | Applicable |