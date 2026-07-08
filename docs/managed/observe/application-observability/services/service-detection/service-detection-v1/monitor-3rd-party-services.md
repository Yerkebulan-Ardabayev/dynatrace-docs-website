---
title: Monitor third-party services
source: https://docs.dynatrace.com/managed/observe/application-observability/services/service-detection/service-detection-v1/monitor-3rd-party-services
---

# Monitor third-party services

# Monitor third-party services

* How-to guide
* 2-min read
* Updated on Feb 21, 2023

Dynatrace captures and monitors all outgoing requests from your monitored server-side services. This includes web requests that your server-side components send out across the internet.

* Most of them probably are not important to you, so Dynatrace collects them into a special service called **Requests to public networks**.
* Some of them, however, probably *are* important to you—for example, if your application relies on the performance and availability of third-party service providers. For this reason, Dynatrace provides a way to monitor third-party services with important HTTP requests as standalone services

Note that currently, the feature doesn't support gRPC requests.

## Monitor a third-party service as a separate service

To configure Dynatrace to monitor a third-party service provider as a separate service

1. Go to **Services**.
2. To find the **Requests to public networks** service, place the cursor in the **Filter by** field, and select **External services** > **Third party services**.

   ![3rd party service 1](https://dt-cdn.net/images/3rd-party-service-1-1075-9e270ec960.png)

   3rd party service 1
3. On the **Requests to public networks** page, select **View requests** to list details about aggregated requests.
4. Scroll down to the **top domains** table of domains and select the domain that you want to monitor as a separate service.  
   The page is now filtered by this domain name.
5. In the upper-right corner of the page, select **More** (**…**) > **Monitor as separate service**.

   ![3rd party service 2](https://dt-cdn.net/images/3rd-party-service-2-1178-b6dda96df9.png)

   3rd party service 2

   The confirmation message is displayed at the bottom of the page.

The requests to that domain are monitored as a standalone service. This service:

* Appears on the **Services** page as a standalone service.
* Appears in Smartscape, Service flow, and elsewhere as a standalone service. This enables you to track the response time better.
* Can be pinned to your dashboards as a dedicated tile.
* Generates alerts when the services experiences performance problems.

Only new data is mapped to the standalone service. Any existing data remains unaffected in the **Requests to public networks** service.

## Revert to third-party service status

If you no longer want to have a recategorized third-party service set up as a standalone service, you can return it to third-party status.

1. Go to **Services**.
2. Find and open the required service.
3. Select **More** (**…**) > **Revert to 3rd party service status**.

   ![3rd party service 3](https://dt-cdn.net/images/3rd-party-service-3-842-21ac60233d.png)

   3rd party service 3

## Service detection rules API

Alternatively, you can set a custom rule for service detection that will map certain requests to a standalone service. For more information, see [Service detection rules API](/managed/dynatrace-api/configuration-api/service-api/detection-rules "Learn what the Dynatrace service detection rules config API offers."). You'll need the **opaque web requests** type of rules.

## Related topics

* [Service detection API](/managed/dynatrace-api/configuration-api/service-api/detection-rules "Learn what the Dynatrace service detection rules config API offers.")