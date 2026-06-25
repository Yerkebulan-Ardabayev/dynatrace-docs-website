---
title: Azure Front Door Standard/Premium and CDN profiles monitoring
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-front-door-cdn-profiles
scraped: 2026-05-12T11:26:05.780666
---

# Azure Front Door Standard/Premium and CDN profiles monitoring

# Azure Front Door Standard/Premium and CDN profiles monitoring

* How-to guide
* 2-min read
* Published Jun 19, 2024

The Azure Front Door Standard/Premium, and CDN profiles overview pages give you visibility into the number of served client requests, latency, and the efficiency of your routing.

## Prerequisites

* Dynatrace version 1.295+
* Environment ActiveGate version 1.195+

For information regarding the previous (classic) offering of Microsoft [Azure Front Door](https://dt-url.net/rz0390g), see [Azure Front Door (classic) monitoring](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-front-door "Monitor Azure Front Door (classic) and view available metrics.").

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to **Technologies & Processes**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**…**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**…**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

Clone hide azure

### Azure Front Door Standard/Premium

![Azure Front Door Standard and Premium](https://dt-cdn.net/images/azure-front-door-standard-premium-2450-49c7ec2e00.png)

Azure Front Door Standard and Premium

### Azure Front Door CDN profiles

![Azure Front Door CDN profiles](https://dt-cdn.net/images/azure-front-door-cdn-profiles-2446-8cac8d26e2.png)

Azure Front Door CDN profiles

## Available metrics

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| ByteHitRatio | This is the ratio of the total bytes served from the cache compared to the total response bytes | Percent | Applicable |
| OriginHealthPercentage | The percentage of successful health probes from AFDX to backends. | Percent |  |
| OriginLatency | The time calculated from when the request was sent by AFDX edge to the backend until AFDX received the last response byte from the backend. | MilliSeconds |  |
| OriginRequestCount | The number of requests sent from AFDX to origin. | Count |  |
| Percentage4XX | The percentage of all the client requests for which the response status code is 4XX | Percent | Applicable |
| Percentage5XX | The percentage of all the client requests for which the response status code is 5XX | Percent | Applicable |
| RequestCount | The number of client requests served by the HTTP/S proxy | Count | Applicable |
| RequestSize | The number of bytes sent as requests from clients to AFDX. | Bytes |  |
| ResponseSize | The number of bytes sent as responses from HTTP/S proxy to clients | Bytes | Applicable |
| TotalLatency | The time calculated from when the client request was received by the HTTP/S proxy until the client acknowledged the last response byte from the HTTP/S proxy | MilliSeconds | Applicable |
| WebApplicationFirewallRequestCount | The number of client requests processed by the Web Application Firewall | Count |  |