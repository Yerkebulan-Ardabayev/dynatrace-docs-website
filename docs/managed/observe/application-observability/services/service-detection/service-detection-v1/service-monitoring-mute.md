---
title: Mute monitoring of service requests
source: https://docs.dynatrace.com/managed/observe/application-observability/services/service-detection/service-detection-v1/service-monitoring-mute
---

# Mute monitoring of service requests

# Mute monitoring of service requests

* How-to guide
* 4-min read
* Published Jan 29, 2021

Dynatrace monitors all server-side server requests end-to-end. When the performance or success rate of a specific request degrades, Dynatrace raises an alert. However, not all high-load requests are important and not all slow requests should raise alerts.

A good example of these are heartbeat requests. Heartbeat requests commonly arrive in high volume and frequency. These requests can distort the overall median response times of services. Such requests can trigger response-time alerts that distract you from the performance of the important requests that actually affect the user experience of your applications.

To better focus on the performance of requests that affect your customers, you can exclude unimportant requests from monitoring by muting them. After you mute a request,

* Automatic alerts for the muted request will no longer be generated.
* The muted request will be excluded from the [service charts](/managed/observe/application-observability/services-classic#charts "Learn about Dynatrace's classic service monitoring").

Muting requests or endpoints for unified services is not supported.

## Mute a request

1. Go to **Services**.
2. On the **Services** page, select the service that receives the request you want to mute.
3. Select **View requests**.
4. Select the request you want to mute.
5. On the request **Details** page, select **More** (**…**) > **Mute**.

The request’s **Details** page displays the message **This request has been muted.** Going forward, Dynatrace will not alert on this request and record its data separately.

Muted service requests remain accessible (and even remain visible in request lists for a limited period of time) but their response times are no longer factored into overall metrics and charts.

## Adjust reference periods for alerting

In some cases, muting a high-volume request can result in fake response-time degradation alerts. This only happens in rare cases and the reason is the displayed shift in the median and the corresponding change in the underlying request distribution. If this happens, it’s best to reset the reference period for alerts on this service. By doing this, Dynatrace will establish new performance baselines that exclude the muted request.

To adjust alerting reference periods for your specific service

1. Go to **Services**.
2. On the **Services** page, select the service that receives the request you’ve muted.
3. On the service page, select **More** (**…**) > **Edit**.
4. Select **Anomaly detection**.
5. In the **Reference period** section, select **Reset**.

## List and unmute muted requests

Data for muted requests is still being recorded, but in a separate place.

To list all muted requests

1. Go to **Services**.
2. On the **Services** page, select the service that receives the request you’ve muted.
3. In the **Muted requests** section, select **View muted requests**.  
   Here you have access to all previously muted requests.

To unmute a request

1. Select the muted request.
2. On the **Details** page, select **More** (**…**) > **Unmute**.

The request is removed from the muted request list, new data is recorded normally again, and alerting is re-enabled for that request.

## Mute a request via Settings API

You can manage muted requests via the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

To be able to use the API you need an access token with **Read settings** (`settings.read`) and **Write settings** (`settings.write`) scopes. To learn how to obtain it, see [Create an access token](/managed/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.").

### Create muted request configuration

This procedure overwrites any existing configuration. If you want to modify an existing configuration, see the [**Update Muted request configuration**](#muted-request-api-update) section below.

1. To learn the format of the settings object, query its schema via the [GET a schema](/managed/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") call. The ID of muted request schema is `builtin:settings.mutedrequests`.
2. Create the JSON object for your settings.  
   Because muted requests are always scoped to a service, you must specify the service by its Dynatrace entity ID. To find out the entity ID of your service, use the [GET entities list](/managed/dynatrace-api/environment-api/entity-v2/get-entities-list "View a list of monitored entities via Dynatrace API.") request.

Example JSON

```
[



{



"schemaId": "builtin:settings.mutedrequests",



"scope": "SERVICE-123456789",



"value": {



"mutedRequestNames": [



"/health"



]



}



}



]
```

3. Use the [POST an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") endpoint to send your configuration.

### Update muted request configuration

1. To learn the format of the settings object, query its schema via the [GET a schema](/managed/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") call. The ID of muted request schema is `builtin:settings.mutedrequests.service`.  
   Because muted requests are always scoped to a service, you must specify the service by its Dynatrace entity ID. To find out the entity ID of your service, use the [GET entities list](/managed/dynatrace-api/environment-api/entity-v2/get-entities-list "View a list of monitored entities via Dynatrace API.") request.
2. Query the current configuration via the [GET objects](/managed/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") call.
3. Create the JSON for your update.

   1. Use the **updateToken** value from the previous step.
   2. Modify the list of requests in the **mutedRequestNames** array as needed.
      Example JSON

      ```
      {



      "updateToken": "vu9U3hXY3q0ATAAkMG",



      "value": {



      "mutedRequestNames": [



      "/health"



      ]



      }



      }
      ```
4. Use the [PUT an object](/managed/dynatrace-api/environment-api/settings/objects/put-object "Edit a settings object via the Dynatrace API.") endpoint to send your configuration.

## Related topics

* [Monitor key requests](/managed/observe/application-observability/services-classic/monitor-key-requests "Discover how to closely monitor requests that are critical to your business.")