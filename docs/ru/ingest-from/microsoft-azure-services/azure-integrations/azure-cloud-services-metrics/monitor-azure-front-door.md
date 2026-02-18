---
title: Azure Front Door (classic) monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-front-door
scraped: 2026-02-17T21:31:09.161905
---

# Azure Front Door (classic) monitoring

# Azure Front Door (classic) monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Sep 27, 2023

The Azure Front Door (classic) overview page gives you visibility into the number of served client requests, latency, and the efficiency of your routing.

## Prerequisites

* Dynatrace version 1.196+
* Environment ActiveGate version 1.195+

This service monitors previous (classic) offering of [Azure Front Doorï»¿](https://dt-url.net/rz0390g).

For information regarding the latest Microsoft [Azure Front Door Standard and Premiumï»¿](https://learn.microsoft.com/en-us/azure/frontdoor/front-door-overview) service, `Front Door and CDN profile`, see [Azure Front Door Standard/Premium and CDN profiles monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-front-door-cdn-profiles "Monitor Azure Front Door Standard/Premium and CDN profiles and view available metrics.").

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

![Frontdoor dash](https://dt-cdn.net/images/frontdoor-1600-ab764051bd.png)

## Available metrics

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| BackendHealthPercentage | Percentage of successful health probes from the HTTP/S proxy to backends | Percent | Applicable |
| BackendRequestCount | Number of requests sent from the HTTP/S proxy to backends | Count | Applicable |
| BackendRequestLatency | Time from when the request was sent by the HTTP/S proxyMySQL to the backend until the HTTP/S proxy received the last response byte from the backend | MilliSeconds | Applicable |
| BillableResponseSize | Number of billable bytes (minimum 2KB per request) sent as responses from HTTP/S proxy to clients | Bytes |  |
| RequestCount | Number of client requests served by the HTTP/S proxy | Count | Applicable |
| RequestSize | Number of bytes sent as requests from clients to the HTTP/S proxy | Bytes | Applicable |
| ResponseSize | Number of bytes sent as responses from HTTP/S proxy to clients | Bytes | Applicable |
| TotalLatency | Time calculated from when the client request was received by the HTTP/S proxy until the client acknowledged the last response byte from the HTTP/S proxy | MilliSeconds | Applicable |
| WebApplicationFirewallRequestCount | Number of client requests processed by the Web Application Firewall | Count | Applicable |