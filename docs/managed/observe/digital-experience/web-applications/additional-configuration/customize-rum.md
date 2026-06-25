---
title: Customize Real User Monitoring with the JavaScript API for web applications
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/customize-rum
scraped: 2026-05-12T11:35:07.229095
---

# Customize Real User Monitoring with the JavaScript API for web applications

# Customize Real User Monitoring with the JavaScript API for web applications

* How-to guide
* 16-min read
* Updated on Mar 05, 2026

Dynatrace enables you to extend its default Real User Monitoring functionality using the RUM JavaScript API. It allows you to create custom user actions, report errors, enable Session Replay, and much more.

The RUM JavaScript API comes included in the RUM JavaScript, which is injected automatically by OneAgent. If you haven't installed OneAgent, you can use [agentless monitoring](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.") to insert the RUM JavaScript manually.

## Capabilities

The RUM JavaScript API, which is called directly from your application code, offers lots of additional capabilities.

* **Create custom user actions**  
  If you want to monitor certain functionality of your application that Dynatrace doesn't capture automatically, you can define your own custom user actions.  
  Suppose that you want to monitor a specific UI element that shows up in response to a user's click but doesn't trigger a web request. In such a case, Dynatrace won't consider this click a user action. With the RUM JavaScript API, you can still monitor such user interactions.
* **Define custom names for user actions**  
  You can use the RUM JavaScript API to [define your own user action names](/managed/observe/digital-experience/web-applications/initial-setup/create-custom-names-for-user-actions "Customize automatically generated user action names for your web applications.") and override the default naming behavior.
* **Report errors**  
  Sometimes there are errors that Dynatrace cannot recognize by default. You can use the RUM JavaScript API error reporting functionality to report errors, which then show up in the [**Errors** section](/managed/observe/digital-experience/web-applications/analyze-and-use/performance-analysis#top-errors "Understand the available types of performance analysis that are provided by Dynatrace.") of the application overview page.
* **Add and extend third-party monitoring**  
  When the resource timing module is active, all resources from the resource timings are captured. Images and JavaScript files are captured with a third-party module. You can use the RUM JavaScript API to capture additional resources.
* **Add user tags**  
  With [user tags](/managed/observe/digital-experience/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace."), you can [track the user behavior of specific users](/managed/observe/digital-experience/web-applications/additional-configuration/identify-individual-users-for-session-analysis "Tag individual users via the JavaScript API for session analysis.") throughout your application environment and across sessions, devices, and browsers.
* **Report properties**  
  You can use the RUM JavaScript API to report session and user action properties. Note that you first need to [define session and user action properties within the RUM application settings](/managed/observe/digital-experience/web-applications/additional-configuration/define-user-action-and-session-properties "Define custom string, numeric, and date properties for your monitored web applications."). Otherwise, Dynatrace will discard submitted properties.
* **Enable or disable Session Replay**  
  Using the RUM JavaScript API, you can enable or disable the [Session Replay](/managed/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.") feature.

## Documentation

The RUM JavaScript API documentation provides information on all RUM customization options and also contains useful code samples. You can either access the JavaScript API documentation online or download a ZIP archive from your environment to view the guide offline.

Online RUM JavaScript API guide

Offline RUM JavaScript API guide

To access the online guide, go to [JavaScript API documentationï»¿](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html).

To download the RUM JavaScript API guide from your environment

1. In Dynatrace, go to **Settings** > **Web and mobile monitoring** > **Advanced setup**.
2. Under **JavaScript tag API**, select **Download documentation and samples**.

## Difference between RUM JavaScript APIs

Note that Dynatrace provides two APIs related to Dynatrace Real User Monitoring.

* The RUM JavaScript API, which is explained in this topic, is designed to extend out-of-the-box features of Real User Monitoring for your application.
* The [RUM JavaScript REST API](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code "Learn how you can use the Dynatrace API to set up and maintain your manually injected applications using the Real User Monitoring JavaScript API.") is often used to get the most recent RUM JavaScript for [agentless RUM](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications."). You must then manually insert the RUM JavaScript tag or code into each HTML page of your application. With this API, you can also obtain a list of all manually inserted applications in your environment and verify the most recent version of the RUM JavaScript.

## Related topics

* [RUM JavaScript API documentationï»¿](https://docs.dynatrace.com/javascriptapi/doc/interfaces/dtrum_types.DtrumApi.html)