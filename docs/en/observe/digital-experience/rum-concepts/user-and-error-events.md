---
title: User and error events
source: https://www.dynatrace.com/docs/observe/digital-experience/rum-concepts/user-and-error-events
scraped: 2026-03-06T21:26:34.294869
---

# User and error events


* Classic
* Explanation
* 6-min read
* Updated on Mar 05, 2026

Besides detecting user actions, Dynatrace also captures additional events known as user events and error events. These events occur within a user session, but they're not directly generated via user interaction with UI controls.

## User events

User events are page changes, rage clicks, rage taps, and user tagging events.

### Page change

A page change event signifies that a user has navigated to a different page on a website. For example, if you navigated to a website "payment" page, the user session would show the following events.

* `Load: loading of page /payment`
* `Page change: /payment`

For more details, see RUM web: Page change events and Pages and page groups.

### Rage event

When your application doesn't respond quickly or there's a user interface issue, users might repeatedly click the screen or a UI control in frustration. Dynatrace detects such behavior as a rage event: a rage click for a web application and a rage tap for a mobile application.

Three or more rapid clicks or taps within the same area are considered to be a rage event. Rage events commonly reflect slow load times or failed resources. Detected rage events affect the user experience score, but when required, you can choose to exclude rage clicks and rage taps from score calculation. See Configure user experience score thresholds to learn more.

You also have the option to completely disable rage event detection.

* Web applications In your application settings, select **Behavior analytics** > **Usability analytics** and turn off **Detect rage clicks**.
* Android See Rage tap detection.
* iOS Set the `DTXDetectRageTaps` [configuration key](../mobile-applications/instrument-ios-app/customization/ios-configuration-keys.md#user-actions "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") to `false`.

In Dynatrace, you can also [check sessions with rage events](../session-segmentation/new-user-sessions.md#rage-events "Learn about user session segmentation and filtering attributes.") to view the details of a rage click or rage tap event.

See also [Discover frustrating user experiences with automatic rage click detectionï»¿](https://www.dynatrace.com/news/blog/discover-frustrating-user-experiences-with-automatic-rage-click-detection/).

### User tagging

One of the key features of Real User Monitoring is the ability to uniquely identify individual users across different browsers, devices, and user sessions. This is achieved by assigning a user tag, which is comprised of a username, nickname, or email, to a user session. When a user is tagged in your application, Dynatrace reports a user tagging event.

You can tag users when they log in or when an already logged-in session is used or restored upon application relaunch, as the user tag isn't persisted when the application restarts.

For web applications, you can set up user tagging using either the RUM JavaScript API or your application's page metadata.

For mobile and custom applications, Dynatrace offers a variant of a "user tagging" method.

Android SDK iOS SDK [Cordova](https://www.npmjs.com/package/@dynatrace/cordova-plugin#identify-user) [Xamarin](../mobile-applications/cross-platform-frameworks/xamarin-nuget.md#identify-user) [![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI").NET MAUI](../mobile-applications/cross-platform-frameworks/maui.md#identify-user) [Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#identifyUser) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#identify-a-user) OpenKit 

With user tags, you can analyze a specific user's behavior and experience via user session analysis. See [Focus on sessions of an individual user](../session-segmentation/new-user-sessions.md#individual-user "Learn about user session segmentation and filtering attributes.") and User details and session activity.") for more information.

## Error events

Error events include errors and crashes.

Source maps and symbol files

To help you identify the origin of detected JavaScript errors and mobile crashes in your code, Dynatrace uses source maps and symbol files. See Source map support for JavaScript error analysis for web applications and Upload and manage symbol files for mobile applications and symbolication (iOS and tvOS) and your options for uploading and managing symbol files in Dynatrace.").

### Error

Dynatrace reports an error whenever a browser throws a JavaScript exception, a web request results in an error, a custom error is sent via API, and for other reasons.

The following error types are captured depending on your application type.

| Error type | Description | Web | Mobile | Custom |
| --- | --- | --- | --- | --- |
| Request error | Detected by the browser and OneAgent on your servers | Applicable | Applicable | Applicable |
| Reported error | Manually reported via dedicated "report an error" API method | Not applicable | Applicable | Applicable |
| Custom error | Manually reported via the RUM JavaScript API | Applicable | Not applicable | Not applicable |
| JavaScript error | JavaScript exceptions thrown by the browser | Applicable | Not applicable | Not applicable |

To report a custom error for a web application or a reported error for a mobile or a custom application, use a dedicated API method.

[Web](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#reportcustomerror) Android SDK iOS SDK [Cordova](https://www.npmjs.com/package/@dynatrace/cordova-plugin#report-error) [Xamarin](../mobile-applications/cross-platform-frameworks/xamarin-nuget.md#report-errors) [![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI").NET MAUI](../mobile-applications/cross-platform-frameworks/maui.md#report-errors) [Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#reportValues) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#report-values) OpenKit 

Dynatrace offers numerous configuration options related to errors. For web applications, you can fine-tune error detection for each error type, for example, configure request error rules, add custom error rules, or ignore JavaScript errors. For mobile and custom applications, you can opt to ignore web request errors.

Note that errors affect both the user experience score and Apdex rating. However, you can change user experience score thresholds, [adjust Apdex settings](scores-and-ratings/apdex-ratings.md#adjust-apdex "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance."), and [exclude errors from Apdex calculations](scores-and-ratings/apdex-ratings.md#error-impact "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") in your application settings.

You can leverage performance, multidimensional, and user session analysis to get information on errors that occur in your application. You can check various error details such as the estimated error count, provider, technology, and more. For details, see the following pages.

* [Performance analysis | Top errors](../web-applications/analyze-and-use/performance-analysis.md#top-errors "Understand the available types of performance analysis that are provided by Dynatrace.")
* [Multidimensional analysis based on error type](../web-applications/analyze-and-use/multi-dimensional-analysis.md#by-error-type "Find out how Dynatrace Real User Monitoring enables you to dig deep into your user actions and perform analysis across numerous dimensions.")
* [Analyze individual user actions | Errors](../web-applications/analyze-and-use/analyze-individual-user-actions.md#errors "Understand how you can access user action detail pages and analyze user actions.")
* [User session analysis | View error details](../session-segmentation/new-user-sessions.md#errors "Learn about user session segmentation and filtering attributes.")

### Crash

Mobile and custom applications

When your application crashes, Dynatrace automatically reports a crash event. Dynatrace captures crashes and sends the crash report to the server. The crash report includes the occurrence time and the full stack trace of the exception.

For custom applications, Dynatrace doesn't automatically report crashes. You need to manually report them.

In Dynatrace, a crash is a fatal issue that terminates the application. Non-fatal issues, such as caught exceptions and [errors](#error), are not counted as crashes. ANRs (Application Not Responding) are not monitored by Dynatrace.

Some crashes might not be reported, as when the application user experiences network issues like an unstable or unavailable internet connection. This is because Dynatrace doesn't send crash reports that are older than 10 minutes (as such reports can no longer be correlated on the Dynatrace Cluster).

#### Disable crash reporting

Crash reporting is enabled by default, but you can deactivate this feature.

* Android See details for Dynatrace Android Gradle plugin or OneAgent SDK for Android.
* iOS See [Crash reporting](../mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features.md#crashes "Explore the list of features that are available after you instrument your application with OneAgent.").
* Cross-platform frameworks Adjust the configuration file (`dynatrace.config.<extension>`) by adding the `crashReporting false` (Android) or `"DTXCrashReportingEnabled": false` (iOS) line. Note that this only disables monitoring of the native crashes.

  See details for the following frameworks.

  [Cordova](https://www.npmjs.com/package/@dynatrace/cordova-plugin#2-configuration-with-dynatrace) [Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#configurationStructure) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#structure-of-the-dynatracejs-file) [Xamarin](../mobile-applications/cross-platform-frameworks/xamarin-nuget.md#config-file) [![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI").NET MAUI](../mobile-applications/cross-platform-frameworks/maui.md#config-file)

#### Report a crash manually

For some technologies, you can report a crash manually.

[Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#crashReporting) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#manually-report-a-crash) [Xamarin](../mobile-applications/cross-platform-frameworks/xamarin-nuget.md#report-crash) [![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI").NET MAUI](../mobile-applications/cross-platform-frameworks/maui.md#report-crash) OpenKit 

#### Analyze and use crash data

To view the complete sequence of user actions that preceded a crash, leverage user session analysis. You can also open a crash report to get all the code-level information and quickly trace the root cause of a crash. For additional details, see the following pages.

* [User session analysis | Examine crashes](../session-segmentation/new-user-sessions.md#crashes "Learn about user session segmentation and filtering attributes.")
* View crash reports for mobile applications
* View crash reports for custom applications

With Session Replay on crashes, you receive additional context for your crash analysis. You can watch video-like screen recordings that replay the user actions immediately preceding a detected crash. This feature is available for Android and iOS.

Note that crashes drastically affect the user experience score. See Calculate the user experience score to see why crashed sessions are usually rated as **Frustrating**.