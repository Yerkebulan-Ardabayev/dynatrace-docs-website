---
title: Automate alerts with API
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/set-up-anomaly-detectors-via-api
scraped: 2026-03-01T21:14:46.009638
---

# Automate alerts with API

# Automate alerts with API

* Latest Dynatrace
* Tutorial
* Updated on Jan 28, 2026

The latest Dynatrace platform provides general-purpose AI services covering various functionalities. Usually, the platform handles the authentication and routing to the right environment for you. However, Dynatrace offers you an option to call an API from outside of the platform. In this guide, you'll learn how to set up DQL-based ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** custom alerts via API.

## Who this is for

This article is for any users who want to be able to set up and manage their DQL-based ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** custom alerts via API.

## What you will learn

In this article, you'll learn how to set up a custom alert via API.

## Before you begin

DQL-based ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** custom alerts use the `builtin:davis.anomaly-detectors` schema.

### Prior knowledge

* [Anomaly detection](/docs/dynatrace-intelligence/anomaly-detection "How Dynatrace detects anomalies in your environment.")
* [Adjust the sensitivity of anomaly detection](/docs/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection "Learn how to adapt the sensitivity of problem detection in Dynatrace.")
* [AI models](/docs/dynatrace-intelligence/reference/ai-models "Learn about AI models that Dynatrace Intelligence uses.")
* [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.") or [Platform tokens](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Create personalised platform tokens to access Dynatrace services via the API in your user context.")
* [How to access platform APIsï»¿](https://developer.dynatrace.com/develop/access-platform-apis-from-outside/)

### Prerequisites

You need the following permissions to be able to set up custom alerts using API:

* `settings:schemas:read`
* `settings:objects:read`
* Grail-specific permissions for the data you want to query (such as `storage:buckets:read`, `storage:logs:read`, `storage:events:read`,`storage:metrics:read`)

If you intend to create or edit existing configurations, you also need the following permissions:

* `settings:objects:write`
* `iam:service-users:use` is mandatory only if you plan to use service users, which is recommended for automation

If you plan to run custom alerts without using service user as an actor, `davis:analyzers:execute` is a mandatory permission.

### Authentication

To authenticate API access and set up a custom alert, you need to use an OAuth client or a platform token. Classic authentication methods like username and password won't work.

![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** doesn't work on classic endpoints.

To authenticate API access with OAuth client, you need to

1. Create an OAuth client with all the permissions listed in [Prerequisites](#api-prerequisites).
2. Generate a bearer token from the created client.

To learn more about creating an OAuth client and generating a bearer token, see [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

If you want to use the platform token instead, create a platform token for a chosen user or environment. To learn more about creating and managing platform tokens, see [Platform tokens](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Create personalised platform tokens to access Dynatrace services via the API in your user context.").

A platform token will only work within the limits of the assigned user's permissions. This means that a selected scope is only granting access if that user has the respective permissions.

Once you've completed the steps above, you'll be able to call the Settings 2.0 API, authenticating with a platform token or the bearer token you generated from the OAuth client. An example Settings 2.0 endpoint URL can be seen below:

```
https://{your-environment-id}.apps.dynatrace.com/platform/classic/environment-api/v2/settings/objects
```

## Create a custom alert configuration

To create a custom alert configuration

1. Get the platform token or the bearer token generated during the [Authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").
2. Call the app function via the endpoint URL.
3. Create a new settings object using a schemaID for DQL-based custom alerts, `builtin:davis.anomaly-detectors`, and a platform token or an OAuth client. This will create a custom alert settings object. An example of the call for the new settings object can be seen below:

   ```
   curl 'https://{your-environment-id}.apps.dynatrace.com/platform/classic/environment-api/v2/settings/objects' \



   -X POST \



   -H 'Accept: application/json; charset=utf-8' \



   -H 'Content-Type: application/json; charset=utf-8' \



   -H 'Authorization: Bearer {your-bearer-token}' \



   -d '[



   {



   "schemaId": "builtin:davis.anomaly-detectors",



   "scope": "environment",



   "value": {



   "enabled": true,



   "title": "Low disk space alert",



   "description": "",



   "source": "Rest-API",



   "executionSettings": {



   "actor": null,



   "queryOffset": null



   },



   "analyzer": {



   "name": "dt.statistics.ui.anomaly_detection.StaticThresholdAnomalyDetectionAnalyzer",



   "input": [



   {



   "key": "query",



   "value": "timeseries avg(dt.host.disk.free), by:{dt.entity.host, dt.entity.disk}"



   },



   {



   "key": "threshold",



   "value": "10"



   },



   {



   "key": "alertCondition",



   "value": "BELOW"



   },



   {



   "key": "alertOnMissingData",



   "value": "false"



   },



   {



   "key": "violatingSamples",



   "value": "3"



   },



   {



   "key": "slidingWindow",



   "value": "5"



   },



   {



   "key": "dealertingSamples",



   "value": "5"



   }



   ]



   },



   "eventTemplate": {



   "properties": [



   {



   "key": "dt.source_entity",



   "value": "{dims:dt.entity.host}"



   },



   {



   "key": "event.type",



   "value": "CUSTOM_ALERT"



   },



   {



   "key": "event.description",



   "value": "The disk {dims:dt.entity.disk.name} runs out of space. Free up space or resize disk."



   },



   {



   "key": "event.name",



   "value": "Low amount of disk space available on host {dims:dt.entity.host.name}"



   }



   ]



   }



   }



   }



   ]'
   ```

### Parameters

An anomaly detection configuration consists of the following fields:

* `enabled`: a boolean parameter. If set to `true`, it'll indicate that the config is enabled and is being picked up for the evaluation.
* `title`: the title of your custom alert configuration. You can set it to any name you like.
* `description`: a free-text parameter describing your custom alert configuration.
* `source`: a free-text parameter that can be used to group and filter configs on the UI. For example, setting source as `kubernetes` on some configs can be used for filtering all `kubernetes` configs in the app. If `source` isn't set, a default value indicating that it comes from REST API will be used.
* `executionSettings`: this object contains an optional field, `queryOffset`. When `queryOffset` is set to any value of type `integer`, it offsets the sliding evaluation window. This can be used to avoid evaluating the last few data points in metrics that are latency associated.
* `analyzer`: this object indicates an anomaly detection model and associated parameters that will be used in the configuration. To learn more about anomaly detection models, see [AI models](/docs/dynatrace-intelligence/reference/ai-models "Learn about AI models that Dynatrace Intelligence uses.").
* `eventTemplate`: this object determines the content of the events generated when the configured anomaly is detected.

#### `analyzer` object fields

An `analyzer` object has additional fields that need to be configured for your custom alert to work.

* `name`: the name of the anomaly detection model that will be used evaluate your query. There are three models to choose from:

  + `dt.statistics.ui.anomaly_detection.StaticThresholdAnomalyDetectionAnalyzer`
  + `dt.statistics.ui.anomaly_detection.AutoAdaptiveAnomalyDetectionAnalyzer`
  + `dt.statistics.ui.anomaly_detection.SeasonalBaselineAnomalyDetectionAnalyzer`
* `input`: a list of parameters that specifies how your custom alert works.

  + `numberOfSignalFluctuations`: a parameter available only for an auto-adaptive custom alert model. It controls how many times the signal fluctuation needs to be added to the baseline to produce the actual threshold for alerting. The default value is `1`.
  + `tolerance`: a parameter available only for a seasonal baseline custom alert model. A higher tolerance means a broader confidence band and leads to a lower number of triggered events. The default value is `4`.
  + `alertCondition`: a condition for alerting.

    - `ABOVE`âa value above the threshold. Available for all models.
    - `BELOW`âa value below the threshold. Available for all models.
    - `OUTSIDE`âa value outside of either upper or lower threshold. Available for auto-adaptive and seasonal baselining models.
  + `alertOnMissingData`: a boolean parameter. If set to `true`, data missing from the evaluation window will be treated as a violation of the configured threshold.
  + `threshold`: a parameter available for static threshold models. This is a numerical value to be compared against when evaluating the configuration. It needs to be provided in the base unit of the data being queried, for example, in milliseconds for a duration metric.
  + `violatingSamples`: a numerical value, maximum `60`. This parameter indicates how many data points in the sliding window should go above, below, or outside the configured threshold to raise an alert.
  + `slidingWindow`: a numerical value, maximum `60`. This parameter indicates how many data points we continuously look at when evaluating how many samples have violated the threshold.

    The sliding window must be greater than or equal to the value set for `violatingSamples`.
  + `delalertingSamples`: a numerical value, maximum `60`. This parameter indicates how many samples need to avoid violating the threshold for the event to be closed.
  + `query`: a DQL query that is evaluated by the configuration. The query result must be of the type `timeseries`, either by using `timeseries` or `makeTimeseries` DQL commands.

    The query must have a time interval explicitly set to `interval:1m`. You can't set timeframes using `from:` and `to:` DQL operators with this configuration.

#### `eventTemplate` object fields

The `eventTemplate` object has additional fields that need to be configured for your custom alert to work.

* `properties`: key-value pairs of properties that show up in the generated events.

  + Required `event.name` : a title for events generated by this custom alert. You can set it to any name you like.
  + Required `event.description`: a free-text parameter describing your custom alert configuration.
  + Required `event.type`: the type of the raised event, such as `CUSTOM_INFO`, `ERROR_EVENT`, `AVAILABILITY_EVENT`, `PERFORMANCE_EVENT`, `RESOURCE_CONTENTION_EVENT`, `CUSTOM_ALERT`, `CUSTOM_ANNOTATION`, `CUSTOM_CONFIGURATION`, `CUSTOM_DEPLOYMENT`, `MARKED_FOR_TERMINATION`.

    To check all available event types, see [Dynatrace Intelligence Semantic Dictionary](/docs/semantic-dictionary/model/davis "Get to know the Semantic Dictionary models related to Davis AI."). You can also include your custom events here.

## Conclusion

You have learned how to set up and configure a custom alert via API. Now you can make direct calls to custom alerts and use DQL-based anomaly detection via API configuration.

## Related topics

* [Anomaly detection](/docs/dynatrace-intelligence/anomaly-detection "How Dynatrace detects anomalies in your environment.")
* [AI models](/docs/dynatrace-intelligence/reference/ai-models "Learn about AI models that Dynatrace Intelligence uses.")
* [Settings API - GET objects](/docs/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.")
* [Settings API - POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.")
* [Settings API - PUT an object](/docs/dynatrace-api/environment-api/settings/objects/put-object "Edit a settings object via the Dynatrace API.")
* [Settings API - DELETE an object](/docs/dynatrace-api/environment-api/settings/objects/del-object "Delete a settings object via the Dynatrace API.")