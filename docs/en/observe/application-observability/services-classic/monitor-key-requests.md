---
title: Monitor key requests
source: https://www.dynatrace.com/docs/observe/application-observability/services-classic/monitor-key-requests
scraped: 2026-02-06T16:30:14.195296
---

# Monitor key requests

# Monitor key requests

* Latest Dynatrace
* How-to guide
* 5-min read
* Updated on Jan 21, 2026

Switch to Enhanced endpoints for SDv1

Setting up key requests is not available for environments created in Dynatrace version 1.330+.

Instead of defining key requests as described on this page, we strongly recommend enabling the [**Enhanced endpoints for SDv1** feature](/docs/observe/application-observability/services/enhanced-endpoints-sdv1 "Utilize the Enhanced endpoints for SDv1 feature to gain deeper insights into your application's performance and improve your ability to monitor and troubleshoot service interactions.") that allows showing all endpoints in [![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**](/docs/observe/application-observability/services/services-app "Maintain centralized control over service health, performance, and resources with the Services app."), not just key requests.

*Key requests* are requests that need special attention, either because they're a critical measure of the success of your business (for example, a login request or a shopping-cart checkout request) or because they provide vital technical functionality that your application relies on.

* Key requests feature [dedicated metrics](/docs/analyze-explore-automate/metrics-classic/built-in-metrics#key-requests "Explore the complete list of built-in Dynatrace metrics.") that you can manage via the web UI or [API](#manage-api). You can create dedicated dashboard tiles for charting key requests, with direct access from your dashboard, and analyze key request long-term metric history in [request charts](/docs/observe/application-observability/services-classic#request-charting "Learn about Dynatrace's classic service monitoring").
* Alerting is always enabled for key requests, even when they contribute less than 1% of throughput. They also provide custom thresholds.
* Data retention periods of key requests are maintained as follows:

  Data type

  Retention period

  [Detailed code-level data](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods#purepath "Check retention times for various data types.")

  10 days

  [Aggregated code-level data](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods#request-attributes "Check retention times for various data types.")

  35 days

  [Long-term metric history](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods#metrics-classic "Check retention times for various data types.")

  5 years

Key requests are highlighted in **Key requests/endpoints** of each service overview page. This visibility is particularly valuable for low-volume, high-importance requests that would otherwise appear at the bottom of **Top requests**.

The number of key requests is limited:

* 500 key requests per environment across all services.
* 100 key requests per service.

When you reach that limit, consider using [calculated service metrics](/docs/observe/application-observability/services/calculated-service-metric "Learn how to create a calculated metric based on web requests."), which offer you a more flexible approach.

## Create a key request (via web UI)

To mark a specific request as a key request

1. Go to **Services** (previous Dynatrace) or ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic**.
2. Select the relevant service from the list.
3. On the service overview page, select a **View** button (such as **View requests**, **View dynamic requests**, or **View resource requests**).
4. Scroll down to **Top requests** and select a request you want to mark as a key request.
5. On the request overview page, select **More** (**â¦**) > **Mark as key request** or **Pin to dashboard**.

   ![Set key request](https://dt-cdn.net/images/key-request-1000-c04070fc96.png)

After you manually identify a key request, its trend lines are retained perpetually.

## Show key requests on a dashboard

To create a dashboard tile for a specific request

1. Go to **Services** (previous Dynatrace) or ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic**.
2. Select the relevant service from the list.
3. On the service overview page, select **View** (**View requests**, **View dynamic requests**, or **View resource requests**).
4. Scroll down to **Key requests/endpoints** and select a request you want to show on a dashboard.
5. On the request overview page, select **More** (**â¦**) > **Pin to dashboard**.  
   A new request-specific tile that shows the most important metrics for that particular request is then added to your dashboard.

Dashboard tiles include only data collected after the request has been marked as key request.

## Rename key requests

Key request detection is name-based. When you apply a [request naming rule](/docs/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming "Adjust request naming and define the operations your services offer."), it can affect key requests. If you want Dynatrace to continue detecting renamed requests as key requests, you need to add the new name to the list of key request names.

1. Go to **Services** (previous Dynatrace) or ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic** and select the service you want to configure.
2. Select **More** (**â¦**) > **Settings**.
3. On the **Service settings** page, go to the **Key requests** tab and select **Add item** to add the name to which the request naming rules apply.

## Anomaly detection with key requests

Dynatrace assumes that low-volume requests are of less importance than high-volume and key requests. This means that requests that contribute less than 1% to the overall load of a service won't raise alerts unless their impact is significant enough that the service's overall response time or failure rate is affected. Because this default treatment is not appropriate for all low-volume requests, you should manually tag any important low-volume requests as key requests to ensure that they have standard alerting thresholds.

### Request-specific alerting thresholds

Because certain requests may have specific response-time and failure-rate patterns, while others may have strict SLA thresholds, Dynatrace enables you to define custom alerting thresholds when anomalies are detected related to the performance of key requests. If set, key-request-level thresholds override service-level thresholds. To learn how to set request-level thresholds, see [**Thresholds for a specific web request**](/docs/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-services#key-request "Learn how to adapt the sensitivity of problem detection for services.").

## Calculated service metric

As an alternative way to focus on particular requests, you can create a [calculated service metric](/docs/observe/application-observability/services/calculated-service-metric "Learn how to create a calculated metric based on web requests."), based on the requests you need. This approach provides you more flexibility with alertingâyou can use the calculated metric just like any built-in metric provided by Dynatrace.

## Manage key requests via Settings API

You can manage key request configurations via the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

To be able to use the API you need an access token with **Read settings** (`settings.read`) and **Write settings** (`settings.write`) scopes. To learn how to obtain it, see [Create an access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.").

### Create key request configuration

Follow the steps below to create a new key request configuration. Note that this procedure overwrites any existing configuration. If you want to modify an existing configuration, see the [**Update key request configuration**](#update-api) section below.

1. To learn the format of the settings object, query its schema via the [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") call. The ID of key request schema is `builtin:settings.subscriptions.service`.
2. Create the JSON object for your settings.  
   Note that the scope of a key request is always a service. You must specify the service by its Dynatrace entity ID. To find out the entity ID of your service, use the [GET entities list](/docs/dynatrace-api/environment-api/entity-v2/get-entities-list "View a list of monitored entities via Dynatrace API.") request.
   Example JSON

   ```
   [



   {



   "schemaId": "builtin:settings.subscriptions.service",



   "scope": "SERVICE-123456789",



   "value": {



   "keyRequestNames": [



   "/cart/checkout"



   ]



   }



   }



   ]
   ```
3. Use the [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") endpoint to send your configuration.

### Update key request configuration

1. To learn the format of the settings object, query its schema via the [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") call. The ID of key request schema is `builtin:settings.subscriptions.service`.  
   Note that the scope of a key request is always a service. You must specify the service by its Dynatrace entity ID. To find out the entity ID of your service, use the [GET entities list](/docs/dynatrace-api/environment-api/entity-v2/get-entities-list "View a list of monitored entities via Dynatrace API.") request.
2. Query the current configuration via the [GET objects](/docs/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") call.
3. Create the JSON for your update.

   1. Use the **updateToken** value from the previous step.
   2. Modify the list of requests in the **keyRequestNames** array as needed.
      Example JSON

      ```
      {



      "updateToken": "vu9U3hXY3q0ATAAkMG",



      "value": {



      "keyRequestNames": [



      "/cart/checkout",



      "/cart"



      ]



      }



      }
      ```
4. Use the [PUT an object](/docs/dynatrace-api/environment-api/settings/objects/put-object "Edit a settings object via the Dynatrace API.") endpoint to send your configuration.

## Related topics

* [Service analysis timings](/docs/observe/application-observability/services-classic/service-analysis-timing "Find out what each time in service analysis means.")
* [Calculated metrics for services](/docs/observe/application-observability/services/calculated-service-metric "Learn how to create a calculated metric based on web requests.")
* [Mute monitoring of service requests](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-monitoring-mute "Mute the monitoring of certain service requests so that you can focus on the performance of requests that affect your customers.")