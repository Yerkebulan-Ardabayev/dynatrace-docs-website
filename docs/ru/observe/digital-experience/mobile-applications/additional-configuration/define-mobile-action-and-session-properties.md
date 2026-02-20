---
title: Define user action and user session properties for mobile applications
source: https://www.dynatrace.com/docs/observe/digital-experience/mobile-applications/additional-configuration/define-mobile-action-and-session-properties
scraped: 2026-02-20T21:16:06.666367
---

# Define user action and user session properties for mobile applications

# Define user action and user session properties for mobile applications

* How-to guide
* 2-min read
* Published Jan 27, 2022

Dynatrace captures a lot of information about the performance of your applications. You can enrich this information with valuable metadata and then convert the metadata into user action and user session properties.

Action and session properties are metadata key-value pairs that you can filter across Dynatrace analysis views. These properties come in handy when you need to create powerful queries, segmentations, or aggregations on the captured metadata. You can use these properties on the **User sessions** and **User sessions query** pages. For a deeper understanding of how to leverage these properties, see [Leverage user action and user session properties for mobile applications](/docs/observe/digital-experience/mobile-applications/analyze-and-use/action-and-session-properties-mobile "User action and session properties, which are metadata key-value pairs, provide added visibility and deeper analysis of your end users' experience. Using these properties for your applications, you can filter user sessions, add calculated metrics, create charts, and more.").

Below you can find the information on how to configure such properties as well as related configuration examples. To exploit action and session properties, you first need to send the required metadata to Dynatrace and then [add properties in the Dynatrace web UI](#add-properties).

## Send metadata to Dynatrace

Before you can define action and session properties, you first need to start transferring the required metadata to Dynatrace. There are two ways of doing this:

* [Report custom values via SDK](#report-value-sdk)
* [Define request attributes](#add-request-attribute)

### Report a value via SDK

You can report custom values in the source code of your mobile app via an API call. Our native SDKs and plugins for cross-platform frameworks offer a variant of the `reportValue` call to do this.

[Android](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#report-value) [iOS](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#report-value) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#report-values) [Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#reportValues) [Xamarin](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#report-values) [![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI").NET MAUI](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/maui#report-values) 

To report values for the native part of Cordova apps, follow the instructions for Android or iOS. For the web part, use the [RUM JavaScript API](/docs/observe/digital-experience/web-applications/additional-configuration/customize-rum "Find out how to customize Real User Monitoring using the JavaScript API.").

You can report values of the following data types:

| Framework | `int` | `long` | `double` | `string` | `date` |
| --- | --- | --- | --- | --- | --- |
| Android | Applicable | Applicable | Applicable | Applicable | Not applicable |
| iOS | Applicable | Not applicable | Applicable | Applicable | Not applicable |
| React Native | Applicable | Not applicable | Applicable | Applicable | Not applicable |
| Flutter | Applicable | Not applicable | Applicable | Applicable | Not applicable |
| Xamarin | Applicable | Not applicable | Applicable | Applicable | Not applicable |
| .NET MAUI | Applicable | Not applicable | Applicable | Applicable | Not applicable |
| Cordova (web part) RUM JavaScript API | Not applicable | Applicable | Applicable | Applicable | Applicable |

To check if the data that you report in your app's code reaches Dynatrace, go to the details of the user action that should contain the data, and scroll down to the **Reported values** section.

![User action details page with SDK-reported values](https://dt-cdn.net/images/user-action-details-with-reported-values-2048-b44e8bca3e.png)

### Define a request attribute

Additionally, you can add the required metadata to server-side requests, define request attributes, and then use these attributes to create action and session properties.

Request attributes are derived from web request URLs, HTTP request headers, and other request metadata. These attributes represent key-value pairs that you can filter across many Dynatrace analysis and distributed tracing views.

For more details, see [Request attributes](/docs/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.").

## Add action and session properties

After you've reported values via your app's code or defined request attributes, the information that Dynatrace captures is enriched with valuable metadata. You can "promote" this metadata to action and session properties in your app's settings.

You can save the metadata on different "storage levels":

* **User action property**: The data is stored in the defined property on the user action level for each user action where Dynatrace can retrieve the metadata.
* **User session property**. The most recent captured value is stored in the defined property on a session level.
* **Both options**: The data is stored in the defined property on both the user action and session levels.

To define an action or session property

1. Go to **Frontend** and select the application that you want to configure.
2. Select **More** (**â¦**) > **Edit**.
3. From the application settings, select **Session and user action properties**, and select **Add property**.
4. Select an **Expression type** and, if required, a **Data type**.

   * If you've added metadata to requests and [defined request attributes](#add-request-attribute), select **Server-side request attribute**.
   * If you've [reported custom values via SDK](#report-value-sdk), select **SDK reported value**.
5. Specify a **Name** or **Request attribute name**, **Display name**, and **Key**.

   | Option | Explanation |
   | --- | --- |
   | Name Request attribute name | For the SDK-reported value type, it's the name of the reported value from your application's code. **Name** is case-sensitive, so it must exactly match the entry from your code. For the server-side request attribute type, it's the name of the request attribute set in **Settings** > **Server-side service monitoring** > **Request attributes**. |
   | Display name | The name of the property that is used in the Dynatrace web UI, for example, on the session details page or user action details page. |
   | Key | The name of the property that is used to identify and later locate the property in [USQL](/docs/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more."). |
6. Choose at least one [storage type](#storage-levels)âuser action property, session property, or both.
7. For the session property storage type, select one of the aggregation types.
8. Optional To restrict the captured values, enable **Apply cleanup rule**, and specify a [regular expression](/docs/manage/tags-and-metadata/reference/regular-expressions-in-dynatrace "Learn how to use regular expressions in the context of Dynatrace.").

## Examples of action and session properties

Below you can find examples of several action and session properties that we've configured for our easyTravel sample web application.

Journey ID

Member status

Total purchase amount

Credit card

![Journey ID](https://dt-cdn.net/images/property-journey-id-2136-1e20f89c85.png)

The **Journey ID** property, which contains a `long` data type value, is added to each user action and user session within the easyTravel app. For a user session, the value of the last user action is saved.

![Member status property](https://dt-cdn.net/images/property-member-status-2136-1665ea176c.png)

The **Member status** property captures a loyalty program membership status for the whole session. In this case, we do not care about individual user actions as loyalty status is usually the same for the whole session.

![Purchase amount property](https://dt-cdn.net/images/property-purchase-amount-2136-8a92eff1b1.png)

The **Total purchase amount** property represents the total price of all journeys booked via our easyTravel app. Note that this session property is actually the sum of `purchase_amount` values from multiple user actions.

![Credit card type property](https://dt-cdn.net/images/property-credit-card-type-2136-8a271f7d47.png)

The **Credit card type** is an example of how we've "promoted" a server-side request attribute to action and session properties.

## Limitations



* You can define a maximum of 200 properties per application.
* You can define a maximum of 20 action properties per application.
* Action and session properties of the `String` data type are limited to 100 characters after applying the cleanup rule.
* You can use up to 20 properties per application free of charge. Additional properties consume DEM units.
  See [DEM units](/docs/license/monitoring-consumption-classic/digital-experience-monitoring-units#dem-units "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units.") (pay attention to the **Session property** and **Action property** entries in the table) and [Free tier of action and session properties](/docs/license/monitoring-consumption-classic/digital-experience-monitoring-units#free-action-and-session-properties "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units.") for more information.

## Notes

* Dynatrace begins capturing action and session properties only after you [define these properties in your app's settings](#add-properties).
* You can check how many properties you're already using and how many more you can add. Go to your app settings > **Session and user action properties**, and scroll down to **Property usage quotas**.

## Related topics

* [Leverage user action and user session properties for mobile applications](/docs/observe/digital-experience/mobile-applications/analyze-and-use/action-and-session-properties-mobile "User action and session properties, which are metadata key-value pairs, provide added visibility and deeper analysis of your end users' experience. Using these properties for your applications, you can filter user sessions, add calculated metrics, create charts, and more.")
* [Mastering session and user action properties for enhanced analyticsï»¿](https://www.youtube.com/watch?v=b8Vj0EoaDeM)