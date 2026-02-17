---
title: User actions
source: https://www.dynatrace.com/docs/observe/digital-experience/rum-concepts/user-actions
scraped: 2026-02-17T04:49:54.134123
---

# User actions

# User actions

* Explanation
* 12-min read
* Updated on Jul 11, 2024

A user action is an interaction with an end-user interface that involves a call to a web server, which can potentially have multiple nested calls. It is a transformation from one view to another view that is triggered by a user input, for example, a page load, click, or touch.

## User action types for web applications

Web applications

The following types of user actions are available in Dynatrace for [web applications](/docs/observe/digital-experience/rum-concepts/applications#web "Learn about monitored applications in Real User Monitoring and the different application types supported by Dynatrace."):

* [Load actions](#load-action)
* [XHR actions](#xhr-action)
* [Custom actions](#custom-action)

The key difference among these action types is the way action duration is calculated and the list of available metrics.

### Load actions

A load action is defined as an actual page loading in your browser. If you type a URL in your browser and use **Enter**, a load action occurs. During this action type, many resources are loaded, including images, HTML, and CSS.

#### Load action duration

The action duration is the time required for the complete load action. More specifically, the start time of the user action equals the W3C `navigationStart` time. If this attribute is not available, the start time equals the time when the [RUM JavaScript](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats "Select a format for the RUM JavaScript snippet that best fits your specific use case") is initialized in the browser. The end time is when the last `onload` handler has completed its task. The `onload` handler is an event handler in JavaScript that's used to call the execution of JavaScript after a page, frame, or image has completely loaded. If any [`XMLHttpRequests`](#xhr-action) are started by an `onload` handler, the user action ends when the `XMLHttpRequest` is complete.

![Page load cycle](https://dt-cdn.net/images/pageload-1886-93237e4321.png)

#### Load action timings

The following measures are used to chart the duration of specific steps in the load action process.

Measure

Description

Definition in terms of W3C specification

**DNS lookup**

The time taken to resolve the hostname for a target URL

`window.performance.timing.domainLookupEnd` â `window.performance.timing.domainLookupStart`

**TCP connect**

The time taken to establish a TCP connection to the server (including SSL)

`window.performance.timing.connectEnd` â `window.performance.timing.connectStart`

**Secure connect**

The time taken to secure the connection established to the server  
This includes the SSL handshake and SOCKS.

`window.performance.timing.connectEnd` â `window.performance.timing.secureConnectionStart`

**Redirect time**

The time taken to follow any HTTP redirects

`window.performance.timing.redirectEnd` â `window.performance.timing.redirectStart`

**Request**

The time taken to request the page from the server until the first byte is received

`window.performance.timing.responseStart` â `window.performance.timing.requestStart`

**Response**

The time taken to receive the response

`window.performance.timing.responseEnd` â `window.performance.timing.responseStart`

**Time to first byte (TTFB)**

The time taken until the first byte of the response is received from the server, relevant application caches, or a local resource

`window.performance.timing.responseStart`

**Server time**

The time spent on server-side processing for a page

`window.performance.timing.responseStart` â `window.performance.timing.requestStart`

**Network time**

The time taken to request and receive resources (including DNS lookup, redirect, and TCP connect time)

`window.performance.timing.responseEnd` â `window.performance.timing.fetchStart` â (`window.performance.timing.responseStart` â `window.performance.timing.requestStart`)

**Frontend time**

The time taken by the browser to render a page

`User action duration` â `Server time` â `Network time`

**Processing**

The time between DOM loading and Load event start

`window.performance.timing.loadEventStart` â `window.performance.timing.domLoading`

**Application cache**

The time spent checking any relevant application caches  
This includes the time before the connection to the server is established.

`window.performance.timing.domainLookupStart` â `window.performance.timing.fetchStart`

**OnDomContentLoaded**

The time taken to execute `OnDomContentLoaded` handlers

`window.performance.timing.domContentLoaded` â `window.performance.timing.domLoading`

**OnLoad**

The time taken to process the load event

`window.performance.timing.loadEventEnd` â `window.performance.timing.loadEventStart`

**Callback**

The time taken to execute XHR callbacks

N/A

**First paint**

The time taken to render the first non-default background element

N/A

**First input start**

The moment when the user first interacts with a page, for example, clicks a UI control

N/A

**First input delay**

The time from the first interaction with the page to when the user agent can respond to that interaction

N/A

**First contentful paint**

The time taken to render the first bit of content, such as text or images

N/A

**Largest contentful paint**

The time taken to render the largest element in the viewport

N/A

**Cumulative layout shift**

The score measuring the unexpected shifting of visible webpage elements for a load action

N/A

**Visually complete**

The time taken to fully render content in the viewport

N/A

**Speed index**

The score measuring how quickly the visible parts of the page are rendered

N/A

**User action duration**

The time taken to complete the page load  
This includes load time of XHR requests initiated before `loadEventEnd` and load time of dynamic resources and script executions triggered by DOM modifications.

N/A

### XHR actions

Dynatrace continuously tracks user interactions with each page. If user interaction leads to `XmlHttpRequests` or `fetch()` calls, an XHR action is created. Dynatrace also detects if there are additional XHRs triggered in the callback of the initial XHR and so on. In this case, Dynatrace waits until all requests are finished. By monitoring the DOM, Dynatrace can also identify resources that have been added in the callbacks. Dynatrace then waits until those resources have finished downloading before ending the action.

An XHR action starts with the user's click on a control on a web page. All [metrics](/docs/observe/digital-experience/rum-concepts/user-action-metrics "Learn what metrics Dynatrace calculates for user actions and find out what each metric indicates.") are calculated in relation to this point in time and are based on the initial XHR that triggers the user action.

By default, RUM captures certain interaction types. You can configure RUM to detect even more interaction types. For details, see [Capture additional interaction types for web applications](/docs/observe/digital-experience/web-applications/additional-configuration/capture-interaction-types "Choose which interaction types RUM should detect for your web applications.").

#### XmlHttpRequest

Most modern applications, including single-page applications, rely on a single load action that downloads the framework and initializes the page. After that, the [DOMï»¿](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction) of the page is changed via JavaScript, and all communication with the web server is done via [`XmlHttpRequest`](/docs/observe/digital-experience/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions "Understand why you need to activate specific JavaScript frameworks for XHR-action support and learn how to configure Real User Monitoring for XHR actions.").

![XHR actions](https://dt-cdn.net/images/xhractions-1785-0de9863dfd.png)

#### Fetch API

The [Fetch APIï»¿](https://fetch.spec.whatwg.org/) provides an interface for fetching resources, including resources across the network. It is similar to `XMLHttpRequest`, but the API provides a more flexible feature set. The generic definitions of `Request`, `Response`, and other network request objects in Fetch allow them to be used at any time they are needed, whether it's for service workers, Cache API, or anything that handles or modifies requests and responses. Fetch also supports the Cross Origin Resource Sharing (CORS).

User actions based on the Fetch API appear in Dynatrace as XHR actions. You can configure RUM to [automatically detect and capture Fetch API request information](/docs/observe/digital-experience/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions "Understand why you need to activate specific JavaScript frameworks for XHR-action support and learn how to configure Real User Monitoring for XHR actions.").

### Custom user actions

Rather than relying on default user action generation, you may want to fine-tune your Real User Monitoring by adding additional user actions directly into your application's HTML. This can be useful if our automated user-action generation doesn't catch specific actions or you want to introduce specific fine-grained timings into your application monitoring. For example, you can measure how long it takes to open a JavaScript-only dropdown menu, or you can measure the duration time of some JavaScript code. To define custom actions, use the [RUM JavaScript API](/docs/observe/digital-experience/web-applications/additional-configuration/customize-rum "Find out how to customize Real User Monitoring using the JavaScript API.").

## User action duration

Below, you can find information on the maximum user action duration in Dynatrace and the user action contributors for web applications.

### Maximum user action duration

The maximum user action duration depends on the application type.

Web application

Mobile app

Custom app

The maximum duration of a web user action is 3 minutes. When a user action takes longer than this, Dynatrace reports such an action as a 3-minute action.

The maximum duration of a mobile user action depends on the action type.

* **Autogenerated actions**

  By default, the maximum duration of a mobile autogenerated user action is set to 1 minute. You can increase this limit up to 9 minutes, though we don't recommend doing that. For Android, see [Configure user action monitoring](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#configure-user-action-monitoring "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent."); for iOS, use the [`DTXAutoActionMaxDurationMilliseconds` configuration key](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#user-actions "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.").

  If an autogenerated user action takes longer than the configured maximum duration, such an action is closed and reported to Dynatrace with a duration slightly longer than the configured maximum duration.
* **Custom actions**

  The maximum duration of a mobile custom action is 9 minutes.

  If a custom action takes longer than 9 minutes and is not closed, such an action is discarded and not reported to Dynatrace.

The maximum duration of a user action in custom apps is 10 minutes. When a user action takes longer than this, such an action is discarded and not reported to Dynatrace.

### User action contributors for web applications

The duration of a user action can be broken down into three components:

* **Server time**: The time spent on server-side processing for a page
* **Network time**: The time taken to request and receive resources (including DNS lookup, redirect, and TCP connect time)
* **Frontend time**: The time taken by the browser to render a page

These components contribute to the overall duration of a user action.

The user action duration is calculated as follows.

**User action duration** = (`loadEventEnd` or `endTimeOfLastXHR`) â `actionStart`

In this calculation

actionStart
:   `navigationStart` for page loads or "click time" for XHR actions and user navigations, such as a click on a button or a link

endTimeOfLastXHR
:   When XHR calls are triggered during the process and aren't completed before `loadEventEnd`, then the end time of the last XHR call is used instead of the `loadEventEnd` time.

The user action contributors are calculated as follows.

**Server time** = `responseStart` â `requestStart`

**Network time** = (`requestStart` â `actionStart`) + (`responseEnd` â `responseStart`)

**Frontend time** = `User action duration` â `Server time` â `Network time`

View the examples of user action contributors below.

User action contributors for a single instance of a user action within a user session

![User session view](https://dt-cdn.net/images/user-session-view-updated-2472-c33e411c76.png)

User action contributors aggregated for one user action, in other words, across all user action instances

![User action view](https://dt-cdn.net/images/useractionview-1785-9f221a3aac.png)

User action contributors aggregated for the entire application

![Application overview](https://dt-cdn.net/images/appoverview-1789-db21269b45.png)

## User action naming rules

Many applications allow users to accomplish the same goal using different UI controls and following different paths. When monitoring such applications, it can be difficult to differentiate between actions that have the same result and goal but are executed using different parts of the application UI. Likewise, if the application is translated into multiple languages, the same application function or UI element can appear under varying names. With user action naming rules, Dynatrace can detect such subtle variations and intelligently group user actions that achieve the same goal into logical groups for monitoring.

Dynatrace automatically removes certain common `sessionid` tokens from user action names, for example, `jsessionid` for Java containers, default `sessionid` for PHP, and `CFID` and `CFTOKEN` for ColdFusion. Nonetheless, there are numerous session ID variations that may be present in your environment. If Dynatrace doesn't automatically recognize and remove session IDs from certain user action names you encounter, you'll need to configure custom naming rules for your [web](/docs/observe/digital-experience/web-applications/initial-setup/create-custom-names-for-user-actions "Customize automatically generated user action names for your web applications."), [mobile](/docs/observe/digital-experience/mobile-applications/additional-configuration/naming-rules-mobile "Customize automatically generated user action names for your mobile applications."), and [custom applications](/docs/observe/digital-experience/custom-applications/additional-configuration/naming-rules-custom "Customize automatically generated user action names for your custom applications.").

When you configure custom naming rules for your web, mobile, and custom applications, remember that your input in the **Add placeholder** and **Add naming rule** sections is case-sensitive. Only the already configured user action name can be set to case-insensitive.

## Child actions

Child actions are actions attached to the main, or parent, user action. You can create child actions for web, mobile, and custom applications.

For web applications, you can create child actions using the RUM JavaScript API, specifically, the [`enterXhrAction`ï»¿](https://www.dynatrace.com/support/doc/javascriptapi/doc/types/dtrum.html#enterxhraction) method.

For mobile and custom applications, Dynatrace offers an API method for creating a child action.

[Android SDK](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#child-actions) [iOS SDK](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#create-child-action) [Xamarin](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#manual-sub-action) [![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI").NET MAUI](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/maui#manual-sub-action) [Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#a-namecustomsubactionacreate-custom-sub-actions) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#create-custom-sub-actions) [OpenKit](/docs/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods#create-custom-actions) 

The possible child action nesting depends on the application type and technology used.

Web applications

There's no limit on the number of child actions attached to a parent action, and there's no limit on the number of levels.

However, note that child actions are not displayed on the [user session details page](/docs/observe/digital-experience/session-segmentation/new-user-sessions#session-details-page "Learn about user session segmentation and filtering attributes."), and child action nesting is not preserved on the [waterfall analysis page](/docs/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis "Learn how to analyze all user action monitoring data through waterfall analysis.") for a parent action to which these child actions are attached.

Android, iOS

There's no limit on the number of child actions attached to a parent action. However, note that you can have only nine levels of child actionsâyou can create one parent action and nine levels of child actions (when child action A is added to a parent action, child action B is added to child action A, child action C is added to child action B, and so on). Also, refer to [User session structure for individual user](/docs/observe/digital-experience/rum-concepts/user-session#session-structure-dep-on-app-type "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.").

Child actions are not displayed on the [user session details page](/docs/observe/digital-experience/session-segmentation/new-user-sessions#session-details-page "Learn about user session segmentation and filtering attributes."), but you can view them on the [waterfall analysis page](/docs/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis "Learn how to analyze all user action monitoring data through waterfall analysis.") for a parent action to which these child actions are attached. Even though the child action nesting is not fully preserved in the waterfall analysis view and all child actions are displayed as child actions of level 1, you can still grasp the action nesting from the timings.

Flutter, React Native, Xamarin, .NET MAUI, OpenKit

There's no limit on the number of child actions attached to a custom action. However, note that you can have only one level of child actionsâyou can't create a child action for another child action (child actions can't have their own child actions). Also, refer to [User session structure for individual user](/docs/observe/digital-experience/rum-concepts/user-session#session-structure-dep-on-app-type "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.").

Child actions are not displayed on the [user session details page](/docs/observe/digital-experience/session-segmentation/new-user-sessions#session-details-page "Learn about user session segmentation and filtering attributes."), but you can view them on the [waterfall analysis page](/docs/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis "Learn how to analyze all user action monitoring data through waterfall analysis.") for a custom action to which these child actions are attached.

## Key user actions

Most applications include user actions that are particularly important to the success of your digital business. Examples of these actions are signups, checkouts, and product searches. Such key user actions might take longer to execute than others, or they might have the requirement to be of a shorter-than-average duration.

For instance, consider that you've set your global [Apdex threshold](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") to 3 seconds. While this threshold might be acceptable for the majority of user actions, it might not be acceptable for a signup user action. Alternatively, there could be a search action that is quite complex and requires more time than the allotted 3 seconds.

You can mark a user action as a key user action and configure Apdex rating for key user actions in your [web](/docs/observe/digital-experience/web-applications/additional-configuration/configure-key-user-actions-web "Mark a user action as a key user action and configure Apdex rating for key user actions of your web applications."), [mobile](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-key-user-actions-mobile "Mark a user action as a key user action and configure Apdex rating for key user actions of your mobile applications."), and [custom application](/docs/observe/digital-experience/custom-applications/additional-configuration/configure-key-user-actions-custom "Mark a user action as a key user action and configure Apdex rating for key user actions of your custom applications.") settings.

## Related topics

* [Create custom user action names for web applications](/docs/observe/digital-experience/web-applications/initial-setup/create-custom-names-for-user-actions "Customize automatically generated user action names for your web applications.")
* [Create custom user action names for mobile applications](/docs/observe/digital-experience/mobile-applications/additional-configuration/naming-rules-mobile "Customize automatically generated user action names for your mobile applications.")
* [Create custom user action names for custom applications](/docs/observe/digital-experience/custom-applications/additional-configuration/naming-rules-custom "Customize automatically generated user action names for your custom applications.")
* [Configure key user actions for web applications](/docs/observe/digital-experience/web-applications/additional-configuration/configure-key-user-actions-web "Mark a user action as a key user action and configure Apdex rating for key user actions of your web applications.")
* [Configure key user actions for mobile applications](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-key-user-actions-mobile "Mark a user action as a key user action and configure Apdex rating for key user actions of your mobile applications.")
* [Configure key user actions for custom applications](/docs/observe/digital-experience/custom-applications/additional-configuration/configure-key-user-actions-custom "Mark a user action as a key user action and configure Apdex rating for key user actions of your custom applications.")