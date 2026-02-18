---
title: Azure Network Watcher (Connection Monitor, Connection Monitor Preview) monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-network-watcher
scraped: 2026-02-18T05:58:33.201962
---

# Azure Network Watcher (Connection Monitor, Connection Monitor Preview) monitoring

# Azure Network Watcher (Connection Monitor, Connection Monitor Preview) monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Sep 23, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Network Watcher (Connection Monitor, Connection Monitor Preview). You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

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

![Conn monitor](https://dt-cdn.net/images/cm-dashboard-1-3137-226998a645.png)

![Conn monitor preview](https://dt-cdn.net/images/cm-dashboard-1414-d3238a9386.png)

## Available metrics

**Connection Monitor**

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| AverageRoundtripMs | The average network round-trip time (ms) for connectivity monitoring probes sent between source and destination | MilliSecond | Applicable |
| ProbesFailedPercent | The percentage of connectivity monitoring probes failed | Percent | Applicable |

**Connection Monitor Preview**

| Name | Description | Unit | Dimensions | Recommended |
| --- | --- | --- | --- | --- |
| AverageRoundtripMs | The average network RTT for connectivity monitoring probes sent between source and destination | MilliSecond |  |  |
| ChecksFailedPercent | The percentage of failed checks for a test | Percent | Source address, Source endpoint name, Source resource ID, Destination address, Destination endpoint name, Destination resource ID, Destination port, Test group name, Test configuration name | Applicable |
| ProbesFailedPercent | The percentage of connectivity monitoring probes failed | Percent |  |  |
| RoundTripTimeMs | The RTT for checks sent between source and destination | MilliSecond | Source address, Source endpoint name, Source resource ID, Destination address, Destination endpoint name, Destination resource ID, Destination port, Test group name, Test configuration name | Applicable |