---
title: Define user action and user session properties for web applications
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/additional-configuration/define-user-action-and-session-properties
scraped: 2026-02-23T21:36:15.839119
---

# Define user action and user session properties for web applications

# Define user action and user session properties for web applications

* How-to guide
* 8-min read
* Updated on Feb 12, 2026

Dynatrace captures a lot of information about the performance of your web application. You can enrich this information with valuable metadata and turn this metadata into user action and user session properties.

Action and session properties represent key-value pairs that you can filter across several Dynatrace analysis views. These properties come in handy when you need to create powerful queries, segmentations, and aggregations on the captured metadata. You can use action and session properties to create calculated application metrics. You can also see them in the multidimensional analysis view, **User sessions** page, and **User sessions query** page. To acquire a deeper understanding of how to leverage these properties, visit [Leverage user action and user session properties for web applications](/docs/observe/digital-experience/web-applications/analyze-and-use/action-and-session-properties "User action and session properties, which are metadata key-value pairs, provide added visibility and deeper analysis of your end users' experience. Using these properties for your web applications, you can filter user sessions, add calculated metrics, create charts, and more.").

Below you can find the information on how to configure such properties as well as related configuration examples. To exploit action and session properties, you first need to [add properties in the Dynatrace web UI](#add-properties) and then start transferring the required metadata to Dynatrace.

## Add a custom property

Use custom-defined properties to configure string, numeric, and date properties for your monitored [user actions](/docs/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.") and [user sessions](/docs/observe/digital-experience/rum-concepts/user-session "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more."). Dynatrace then captures property values as part of each of your users' journeys. You can leverage property values for unrivaled visibility into all the details of your users' interactions with your application. You can define custom user action and session properties that are specific to each application.

### Expression types

Dynatrace can capture metadata from the following sources (**expression types**):

* CSS selector
* JavaScript variable
* JavaScript API
* JavaScript function
* Meta tag
* Cookie value

  Requirements for Cookie value

  If you want to use `Cookie value` as a data source, ensure that the cookies don't have the `HttpOnly` attribute. Otherwise, the RUM JavaScript won't be able to read the cookie values because `HttpOnly` cookies are inaccessible to JavaScript.
* Query string
* Server-side request attribute
* XHR/fetch response header (available since RUM JavaScript version 1.253 for XHR/fetch and since RUM JavaScript version 1.257 for Angular)

  Requirements for XHR/fetch response header

  If you want to use `XHR/fetch response header` as a data source, ensure the following:

  + In your application settings, enable the **Capture fetch() requests**, **Capture XmlHttpRequest (XHR)**, or **Angular** options. For detailed instructions, see [Activate generic JavaScript frameworks support](/docs/observe/digital-experience/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions#enable-generic-js-frameworks "Understand why you need to activate specific JavaScript frameworks for XHR-action support and learn how to configure Real User Monitoring for XHR actions.") or [Activate support for Angular](/docs/observe/digital-experience/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions#enable-specific-js-frameworks "Understand why you need to activate specific JavaScript frameworks for XHR-action support and learn how to configure Real User Monitoring for XHR actions.").

    Capturing metadata from XHR/fetch response headers is not supported for AngularJS.
  + For CORS and XHR requests, Dynatrace can capture metadata only from the [CORS-safelisted response headersï»¿](https://developer.mozilla.org/en-US/docs/Glossary/CORS-safelisted_response_header). If you want data to be extracted from other headers, leverage the [`Access-Control-Expose-Headers` headerï»¿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Expose-Headers).

    - `Access-Control-Expose-Headers: Content-Encoding, Destination, Basket-value` to expose the specified headers
    - `Access-Control-Expose-Headers: *` to expose all headers except the `Authorization` header for requests without credentials
    - `Access-Control-Expose-Headers: *, Authorization` to expose all headers for requests without credentials

### Data types

Dynatrace can save the captured metadata as one of the following data types:

| Data type | Note |
| --- | --- |
| `String` | Action and session properties of the `String` data type are limited to 1,000 characters before applying the cleanup rule. |
| Number | `Double` or `Long` |
| `Date` | Only available for the `JavaScript API` [expression type](#expression-types)âmetadata should be captured via the [RUM JavaScript API](/docs/observe/digital-experience/web-applications/additional-configuration/customize-rum "Find out how to customize Real User Monitoring using the JavaScript API."). |

### Storage types

You can save the metadata on different "storage levels".

* **User action property**: The data is stored in the defined property on the user action level for each user action where the RUM JavaScript can retrieve the metadata.
* **User session property**. The most recent captured value is stored in the defined property on a session level.
* **Both options**: The data is stored in the defined property on both the user action and session levels.

### Define a custom property

To define a custom property

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Capturing** > **Session and action properties**.
5. Select **Add property** > **Custom-defined property**.
6. Configure the property:

   * Select an [**Expression type**](#expression-types). If applicable, also choose a [**Data type**](#data-types) and **String length**.
   * Enter the designation of the expression type you want to use, for example, the CSS selector attribute or meta tag name. For the **Server-side request attribute** type, select a [request attribute name](/docs/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.").
   * Optional Define a **Display name**, which is the name of the property that is used in the Dynatrace web UI, for example, on the session details page or user action details page.
   * Specify a **Key**, which is the name of the property that is used to identify and later locate the property in [USQL](/docs/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.") and **User sessions** page.

     A **Key** that has been used in the past can't be reused [as long as the data is retained](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods "Check retention times for various data types.") in your environment. This is because the captured data still references the old property configuration.
   * Optional Turn off **Comply with "Do Not Track" browser settings** only if the property contains no personally identifiable information.

     This option is only available for certain expression types and if you've enabled the **[Comply with "Do Not Track" browser settings](/docs/observe/digital-experience/web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr#do-not-track-gdpr "Learn about the privacy settings that Dynatrace provides to ensure that your web applications comply with the data-privacy regulations of your region.")** in the data privacy section of your application settings.
   * Choose at least one [storage type](#storage-levels)âuser action property, session property, or both. For the session property storage type, select one of the aggregation types.
   * Optional To restrict the captured values, turn on **Apply cleanup rule**, and specify a [regular expression](/docs/manage/tags-and-metadata/reference/regular-expressions-in-dynatrace "Learn how to use regular expressions in the context of Dynatrace.").

     The regex is applied to the captured value: if you try to capture a string that is, for example, 1000 characters long, only the first 100 characters are captured, and the regex is applied to these 100 characters.

## Add a property pack



Use property packs to link analytics data to performance insights. You can do this by integrating tools, such as web analytics and performance monitoring, into Dynatrace. A host of property packs are available, for example, Adobe, Google, Intercom, and Tealeaf.

To add a property from a property pack

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Capturing** > **Session and action properties**.
5. Select **Add property** > **Property packs**, and then choose the required property pack from the dropdown list.
6. In the **Configure properties** column, select **Add** for the properties that you want to add, and then select **Next**.
7. Choose at least one [storage type](#storage-levels)âuser action property, session property, or bothâfor each of the added properties.
8. Select **Create property**.

## Examples of action and session properties

Here are some sample definitions that work for our easyTravel test application.

* In this example, the `member_status` property captures a loyalty program membership status.

  ![User action and session properties - CSS selector example 1](https://dt-cdn.net/images/example1-2220-a488e55380.png)
* `averagepersonprice` captures the average price per person of a journey booked using our easyTravel portal.

  ![User action and session properties - CSS selector example 1](https://dt-cdn.net/images/example2-2195-bfc15d8a6d.png)
* The `author` property captures the name of the developer of the easyTravel application from a metadata tag.

  ![User action and session properties - meta tag example](https://dt-cdn.net/images/example3-2246-bef8792b1a.png)
* In the following example, a JavaScript string variable captures the userâs `appversion` during the session.

  ![User action and session properties - JavaScript variable example](https://dt-cdn.net/images/javascript-variable-1488-c376427e90.png)
* Starting with RUM JavaScript version 1.295 it is possible to extract data from JSON.
  In the following example, a JavaScript string variable captures the `userid` property of a JSON stored as a string in the `sessionStorage`.

  ![Developer Tools](https://dt-cdn.net/images/userid-devtools-2544-09723cd81f.png)

  To indicate that a string needs to be parsed as JSON, use the `$` character before the name of the property (even if the property name starts with `$`, add another `$` in front).
  In this example, the string stored in `sessionStorage.user` will be retrieved, and the `$` character indicates that the string needs to be parsed as JSON and then `userid` will be captured.

  ![Userid property](https://dt-cdn.net/images/userid-1732-1c6b552622.png)

## Use case

You can integrate Adobe Analytics with Dynatrace to facilitate collaboration among the different teams in your business. To find out how you can do this, visit [Tightening the communication within BizDevOps with Adobe Analytics & Dynatraceï»¿](https://www.dynatrace.com/news/blog/tightening-the-communication-within-bizdevops-with-adobe-analytics-dynatrace/) and [Actionable insights with our Adobe Analytics integration and new web propertiesï»¿](https://www.dynatrace.com/news/blog/actionable-insights-with-our-adobe-analytics-integration-and-new-web-properties/).

## Limitations

* You can define a maximum of 200 properties per application.
* You can define a maximum of 20 action properties per application.
* Action and session properties of the `String` data type are limited to 1,000 characters before applying the cleanup rule.
* You can use up to 20 properties per application free of charge. Additional properties consume DEM units.
  See [DEM units](/docs/license/monitoring-consumption-classic/digital-experience-monitoring-units#dem-units "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units.") (pay attention to the **Session property** and **Action property** entries in the table) and [Free tier of action and session properties](/docs/license/monitoring-consumption-classic/digital-experience-monitoring-units#free-action-and-session-properties "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units.") for more information.

## Notes

* Dynatrace begins capturing action and session properties only after you [define these properties in your application settings](#add-properties).
* Session properties aren't available for ongoing live sessions. The properties become available only after a session ends.
* The metadata is captured at the end of a user action.  
  If you want to capture the metadata at the start of a user action, select **JavaScript API** as an [expression type](#expression-types) when you [add a custom property](#add-properties), and then use the [RUM JavaScript API](/docs/observe/digital-experience/web-applications/additional-configuration/customize-rum "Find out how to customize Real User Monitoring using the JavaScript API.") to report the required values, specifically, the [addActionPropertiesï»¿](https://www.dynatrace.com/support/doc/javascriptapi/doc/types/dtrum.html#addactionproperties) and the [sendSessionPropertiesï»¿](https://www.dynatrace.com/support/doc/javascriptapi/doc/types/dtrum.html#sendsessionproperties) methods.
* You can check how many properties you're already using and how many of them you can still add.

  1. Go to **Web**.
  2. Select the application that you want to configure.
  3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
  4. From the application settings, select **Capturing** > **Session and action properties**.
  5. Scroll down to **Property usage quotas**.

## Related topics

* [Leverage user action and user session properties for web applications](/docs/observe/digital-experience/web-applications/analyze-and-use/action-and-session-properties "User action and session properties, which are metadata key-value pairs, provide added visibility and deeper analysis of your end users' experience. Using these properties for your web applications, you can filter user sessions, add calculated metrics, create charts, and more.")
* [Mastering session and user action properties for enhanced analyticsï»¿](https://www.youtube.com/watch?v=b8Vj0EoaDeM)