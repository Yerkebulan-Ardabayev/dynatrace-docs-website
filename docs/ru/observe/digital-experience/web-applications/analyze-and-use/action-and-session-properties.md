---
title: Leverage user action and user session properties for web applications
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/analyze-and-use/action-and-session-properties
scraped: 2026-02-23T21:27:20.711743
---

# Leverage user action and user session properties for web applications

# Leverage user action and user session properties for web applications

* How-to guide
* 3-min read
* Published Jan 27, 2022

User action properties and user session properties provide a powerful and flexible means of adding information to each user action and user session. You can leverage these properties for deeper visibility into all the details of your users' interactions with your application.

Action and session properties are metadata key-value pairs that are derived from captured data. This metadata is "promoted" from request attributes, CSS selector attributes, meta tags, and more. Action and session properties come in handy when you need to create powerful queries, segmentations, or aggregations on captured metadata. You can use action and session properties to create calculated application metrics. You can also view these properties on the multidimensional analysis page, the **User sessions** page, and the **User sessions query** page.

See the sections below to learn where you can find the values that are captured as custom user action and session properties and how you can take full advantage of these properties.

Before you can leverage user action and session properties, you need to define these properties in your application settings. For details, see [Define user action and user session properties for web applications](/docs/observe/digital-experience/web-applications/additional-configuration/define-user-action-and-session-properties "Define custom string, numeric, and date properties for your monitored web applications.").

## User session analysis

The **[User sessions](/docs/observe/digital-experience/session-segmentation/new-user-sessions "Learn about user session segmentation and filtering attributes.")** page offers the option to filter user sessions by action and session properties. For example, if you're running a loyalty program, you can add a `loyalty_status` property to learn whether a user in a monitored user session is a `Silver`, `Gold`, or `Platinum` member. You can then filter for `Platinum` or `Gold` customers on the **User sessions** page.

1. Go to ![Session Segmentation](https://dt-cdn.net/images/session-segmentation-512-5278e8fa16.png "Session Segmentation") **Session Segmentation**.
2. In **Filter by**, select one of the property types, for example, **Session date properties** or **User action string properties**, and then choose the required property.
3. Select the property value or values according to your needs.
4. Select a session to view its details and the available session properties.
5. From the user session details page you can drill down into user actions. Expand a user action, and then select **Perform waterfall analysis**. From this page, you can check the available action properties as well as all reported values.

   ![User action analysis](https://dt-cdn.net/images/user-action-analysis-1639-89f7ffac81.png)
6. In the upper-right corner, select **Analyze user action** to dive even deeper. Under **User action properties**, select the action property for further analysis.

## Additional insights with USQL

User action and session properties can greatly improve your analytics capabilities when using the [Dynatrace User Sessions Query Language (USQL)](/docs/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.") for analytics that require advanced filtering or persistent filtering across analysis views. Also, when you want to keep track of the monetary values and conversion goals that are key to the success of your business, you can construct queries based on the unique values of the individual user action or session properties that have been defined for your environment.

To use action and session properties in USQL

1. Go to ![Query user sessions](https://dt-cdn.net/images/query-user-sessions-512-77c5a8da9f.png "Query user sessions") **Query User Sessions**.
2. Enter the required query. The following custom properties are available:

   | Custom property | Table | Action property | Session property |
   | --- | --- | --- | --- |
   | `<dataType>Properties.<propertyKey>` | `useraction` | Applicable |  |
   | `<dataType>Properties.<propertyKey>` | `usersession` |  | Applicable |
   | `useraction.<dataType>Properties.<propertyKey>` | `useraction` | Applicable |  |
   | `useraction.<dataType>Properties.<propertyKey>` | `usersession` | Applicable |  |
   | `usersession.<dataType>Properties.<propertyKey>` | `useraction` |  | Applicable |
   | `usersession.<dataType>Properties.<propertyKey>)` | `usersession` |  | Applicable |

   The `<dataType>` part can take the following values:

   * `string`
   * `long`
   * `double`
   * `date`
3. Select **Run query**.

In the example below, you can see how many request errors the Silver, Gold, and Platinum customers have faced.

```
SELECT stringProperties.loyalty_status AS "Loyalty status", COUNT(useraction.requestErrorCount) AS "HTTP error count" FROM usersession WHERE stringProperties.loyalty_status IS NOT NULL GROUP BY stringProperties.loyalty_status
```

![Gain additional insights with USQL](https://dt-cdn.net/images/use-properties-usql-1642-60372d3301.png)

## Integration via User session API

The [User sessions API](/docs/dynatrace-api/environment-api/rum/user-sessions "Learn what the Dynatrace User Sessions Query language API offers."), in combination with our [User Sessions Query Language (USQL)](/docs/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more."), enables you to access all user action and session data, including properties and values.

Extending the loyalty program example above, you can leverage the problem information and loyalty status information via the User session API by querying the user sessions that were impacted by the problem after the problem was closed. This allows you to use the information to, for example, set up personalized marketing campaigns.

Here are some sample queries you may want to leverage:

* Gold member user sessions on an application within a certain timeframeâyou can leverage this for problems that impact an entire application.

  ```
  SELECT userId, stringProperties.loyalty_status FROM usersession WHERE stringProperties.loyalty_status = "Gold" AND userType = "REAL_USER" AND useraction.application = "easyTravel" AND startTime > 1531741985241 AND endTime < 1531932305287
  ```
* Platinum member users on a specific application hitting a specific page within a certain timeframeâyou can leverage this for problems that impact a specific page.

  ```
  SELECT userId, stringProperties.loyalty_status, useraction.targetUrl FROM usersession WHERE stringProperties.loyalty_status = "Platinum" AND userType = "REAL_USER" AND useraction.application = "easyTravel" AND startTime > 1531741985241 AND endTime < 1531932305287 AND useraction.targetUrl = "https://easytravel.perform-2018.dynalabs.io/special-offers.jsp"
  ```

## Dashboards

For web, mobile, and custom applications, you can [create a query](#usql) with action and session properties and then pin the resulting chart to one of your dashboards.

For web applications, you can additionally create calculated metrics based on custom properties, use these metrics to create a chart and then pin this chart to your dashboards. This can be done in [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

The generic **Web property pack** is used in the following example to track the marketing campaigns on [Dynatrace.comï»¿](https://www.dynatrace.com/) to view the following:

* Overall traffic by continent
* Top campaigns by continent
* Slowest landing experience by marketing campaign

![Web property pack](https://dt-cdn.net/images/dynatrace-com-marketing-campaigns-anonym-1600x951-1600-59971b5148.png)

## Session properties export

You can export captured user session properties, along with all other user session data, within user session export streams.

For more details, see [Export user sessions](/docs/observe/digital-experience/session-segmentation/export-session-data "Set up Dynatrace to export user session data to a provided webhook endpoint.").

## Multidimensional analysis



You can also leverage custom properties in [Multidimensional analysis](/docs/observe/digital-experience/web-applications/analyze-and-use/multi-dimensional-analysis "Find out how Dynatrace Real User Monitoring enables you to dig deep into your user actions and perform analysis across numerous dimensions."). For instance, you can analyze user actions based on your custom properties or you can filter data by property values.

To use custom properties on the **Multidimensional analysis** page

1. Go to **Web** and select your application.
2. Under **Impact of user actions on performance**, select **Analyze performance**.
3. Scroll down to **Detail analysis for selected timeframe**, and select the required custom property in **Analyze by**.

   ![Using custom properties on the Multidimensional analysis page](https://dt-cdn.net/images/use-properties-mda-2-2134-eb53554356.png)
4. Optional In **Filter by**, set the required filters. For example, you can filter by user action properties.

   ![Filtering by property on the Multidimensional analysis page](https://dt-cdn.net/images/mda-filter-by-properties-2132-bc8eab93c3.png)
5. Scroll down to see more details. You can use the additional property values for further insight into your application's performance and success.

## Calculated metrics, charts, and alerts

To extend usefulness, create a [calculated metric](/docs/observe/digital-experience/web-applications/additional-configuration/rum-calculated-metrics-web "Create calculated metrics as well as custom charts based on calculated metrics for your web applications.") with your user action properties. You can create a metric either from the [**Multidimensional analysis** page](#mda) or from your application settings. After you add a metric, you can use it to create custom charts and alerts.

To create a metric from the **Multidimensional analysis** page

1. From the **Multidimensional analysis** page, scroll down to **Detail analysis for selected timeframe**, and set the required options in **Analyze by** and, if required, in **Filter by**.
2. Select **Create metric**.
3. Optional Change the metric name and metric key.

   ![Creating a calculated metric with data filtered by action property](https://dt-cdn.net/images/creating-calculated-metric-with-data-filtered-by-action-property-2134-e9027de910.png)
4. Select **Create metric** to save the metric.
5. Optional Select **Create a chart** or **Create alert**. For details, see [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") and [Metric events](/docs/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace").

To create a metric from your web application settings

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Metrics**, and then select **Add metric**.
5. Select the required metric, and specify a **Metric name** and **Metric key for API usage**.
6. Optional In **Filter by**, set the required filters. For example, you can filter by user action properties.
7. Select **Create metric**.
8. Optional From the list of metrics, expand the created metric, and select **Create a chart** or **Create alert**. For details, see [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") and [Metric events](/docs/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace").

## Related topics

* [Define user action and user session properties for web applications](/docs/observe/digital-experience/web-applications/additional-configuration/define-user-action-and-session-properties "Define custom string, numeric, and date properties for your monitored web applications.")
* [Mastering session and user action properties for enhanced analyticsï»¿](https://www.youtube.com/watch?v=b8Vj0EoaDeM)