---
title: User and error events
source: https://www.dynatrace.com/docs/observe/digital-experience/rum-concepts/user-and-error-events
scraped: 2026-02-19T21:33:54.291861
---

# User and error events

# User and error events

* Explanation
* 6-min read
* Updated on Apr 16, 2024

Besides detecting [user actions](/docs/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application."), Dynatrace also captures additional events known as user events and error events. These events occur within a [user session](/docs/observe/digital-experience/rum-concepts/user-session "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more."), but they're not directly generated via user interaction with UI controls.

## User events

User events are page changes, rage clicks, rage taps, and user tagging events.

### Page change

A page change event signifies that a user has navigated to a different page on a website. For example, if you navigated to a website "payment" page, the user session would show the following events.

* `Load: loading of page /payment`
* `Page change: /payment`

For more details, see [RUM web: Page change events](/docs/whats-new/saas/sprint-218#page-change "Release notes for Dynatrace SaaS, version 1.218") and [Pages and page groups](/docs/observe/digital-experience/web-applications/initial-setup/pages-and-pagegroups "Learn how to use and define pages and page groups in Dynatrace Real User Monitoring.").

### Rage event

When your application doesn't respond quickly or there's a user interface issue, users might repeatedly click the screen or a UI control in frustration. Dynatrace detects such behavior as a rage event: a rage click for a web application and a rage tap for a mobile application.

Three or more rapid clicks or taps within the same area are considered to be a rage event. Rage events commonly reflect slow load times or failed resources. Detected rage events affect the [user experience score](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score "User experience score is a metric used to categorize user sessions as Frustrating, Tolerable, or Satisfying."), but when required, you can choose to exclude rage clicks and rage taps from score calculation. See [Configure user experience score thresholds](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score#configure "User experience score is a metric used to categorize user sessions as Frustrating, Tolerable, or Satisfying.") to learn more.

You also have the option to completely disable rage event detection.

* Web applications In your application settings, select **Behavior analytics** > **Usability analytics** and turn off **Detect rage clicks**.
* Android See [Rage tap detection](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#rage-tap-detection "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.").
* iOS Set the `DTXDetectRageTaps` [configuration key](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#user-actions "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") to `false`.

In Dynatrace, you can also [check sessions with rage events](/docs/observe/digital-experience/session-segmentation/new-user-sessions#rage-events "Learn about user session segmentation and filtering attributes.") to view the details of a rage click or rage tap event.

See also [Discover frustrating user experiences with automatic rage click detectionï»¿](https://www.dynatrace.com/news/blog/discover-frustrating-user-experiences-with-automatic-rage-click-detection/).

### User tagging

One of the key features of Real User Monitoring is the ability to uniquely identify individual users across different browsers, devices, and user sessions. This is achieved by assigning a user tag, which is comprised of a username, nickname, or email, to a user session. When a user is tagged in your application, Dynatrace reports a user tagging event.

You can tag users when they log in or when an already logged-in session is used or restored upon application relaunch, as the user tag isn't persisted when the application restarts.

For web applications, you can [set up user tagging](/docs/observe/digital-experience/web-applications/additional-configuration/identify-individual-users-for-session-analysis "Tag individual users via the JavaScript API for session analysis.") using either the RUM JavaScript API or your application's page metadata.

For mobile and custom applications, Dynatrace offers a variant of a "user tagging" method.

[Android SDK](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#tag-specific-users) [iOS SDK](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#tag-specific-users) [Cordova](https://www.npmjs.com/package/@dynatrace/cordova-plugin#identify-user) [Xamarin](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#identify-user) [![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI").NET MAUI](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/maui#identify-user) [Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#identifyUser) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#identify-a-user) [OpenKit](/docs/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods#tag-specific-users) 

With user tags, you can analyze a specific user's behavior and experience via user session analysis. See [Focus on sessions of an individual user](/docs/observe/digital-experience/session-segmentation/new-user-sessions#individual-user "Learn about user session segmentation and filtering attributes.") and [User details](/docs/observe/digital-experience/session-segmentation/analyze-all-sessions-of-a-single-user "Learn about user behavior by analyzing the user profile (user experience score) and session activity.") for more information.

## Error events

Error events include errors and crashes.

Source maps and symbol files

To help you identify the origin of detected JavaScript errors and mobile crashes in your code, Dynatrace uses source maps and symbol files. See [Source map support for JavaScript error analysis](/docs/observe/digital-experience/web-applications/analyze-and-use/source-map-support-for-javascript-error-analysis "Learn how source maps make it easy to analyze, reproduce, and fix JavaScript errors.") for web applications and [Upload and manage symbol files for mobile applications](/docs/observe/digital-experience/mobile-applications/analyze-and-use/upload-and-manage-symbol-files "Learn about deobfuscation (Android) and symbolication (iOS and tvOS) and your options for uploading and managing symbol files in Dynatrace.").

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

[Web](https://www.dynatrace.com/support/doc/javascriptapi/doc/types/dtrum.html#reportcustomerror) [Android SDK](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#report-errors) [iOS SDK](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#report-error) [Cordova](https://www.npmjs.com/package/@dynatrace/cordova-plugin#report-error) [Xamarin](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#report-errors) [![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI").NET MAUI](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/maui#report-errors) [Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#reportValues) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#report-values) [OpenKit](/docs/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods#report-errors) 

Dynatrace offers numerous configuration options related to errors. For web applications, you can [fine-tune error detection for each error type](/docs/observe/digital-experience/web-applications/additional-configuration/configure-errors "Configure your application to capture or ignore request, custom, and JavaScript errors."), for example, configure request error rules, add custom error rules, or ignore JavaScript errors. For [mobile](/docs/observe/digital-experience/mobile-applications/additional-configuration/web-request-errors-mobile "Stop treating certain response HTTP codes as errors for your mobile applications.") and [custom applications](/docs/observe/digital-experience/custom-applications/additional-configuration/web-request-errors-custom "Stop treating certain HTTP response codes as errors for your custom applications."), you can opt to ignore web request errors.

Note that errors affect both the [user experience score](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score "User experience score is a metric used to categorize user sessions as Frustrating, Tolerable, or Satisfying.") and [Apdex rating](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance."). However, you can [change user experience score thresholds](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score#configure "User experience score is a metric used to categorize user sessions as Frustrating, Tolerable, or Satisfying."), [adjust Apdex settings](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings#adjust-apdex "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance."), and [exclude errors from Apdex calculations](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings#error-impact "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") in your application settings.

You can leverage performance, multidimensional, and user session analysis to get information on errors that occur in your application. You can check various error details such as the estimated error count, provider, technology, and more. For details, see the following pages.

* [Performance analysis | Top errors](/docs/observe/digital-experience/web-applications/analyze-and-use/performance-analysis#top-errors "Understand the available types of performance analysis that are provided by Dynatrace.")
* [Multidimensional analysis based on error type](/docs/observe/digital-experience/web-applications/analyze-and-use/multi-dimensional-analysis#by-error-type "Find out how Dynatrace Real User Monitoring enables you to dig deep into your user actions and perform analysis across numerous dimensions.")
* [Analyze individual user actions | Errors](/docs/observe/digital-experience/web-applications/analyze-and-use/analyze-individual-user-actions#errors "Understand how you can access user action detail pages and analyze user actions.")
* [User session analysis | View error details](/docs/observe/digital-experience/session-segmentation/new-user-sessions#errors "Learn about user session segmentation and filtering attributes.")

### Crash



Mobile and custom applications

When your application crashes, Dynatrace automatically reports a crash event. Dynatrace captures crashes and sends the crash report to the server. The crash report includes the occurrence time and the full stack trace of the exception.

For custom applications, Dynatrace doesn't automatically report crashes. You need to [manually report them](/docs/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods#report-crash "Read how Dynatrace OpenKit can be used from the developer's point of view.").

In Dynatrace, a crash is a fatal issue that terminates the application. Non-fatal issues, such as caught exceptions and [errors](#error), are not counted as crashes. ANRs (Application Not Responding) are not monitored by Dynatrace.

Some crashes might not be reported, as when the application user experiences network issues like an unstable or unavailable internet connection. This is because Dynatrace doesn't send crash reports that are older than 10 minutes (as such reports can no longer be correlated on the Dynatrace Cluster).

#### Disable crash reporting

Crash reporting is enabled by default, but you can deactivate this feature.

* Android See details for [Dynatrace Android Gradle plugin](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#crash-reporting "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.") or [OneAgent SDK for Android](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#crash-reporting "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK.").
* iOS See [Crash reporting](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#crashes "Explore the list of features that are available after you instrument your application with OneAgent.").
* Cross-platform frameworks Adjust the configuration file (`dynatrace.config.<extension>`) by adding the `crashReporting false` (Android) or `"DTXCrashReportingEnabled": false` (iOS) line. Note that this only disables monitoring of the native crashes.

  See details for the following frameworks.

  [Cordova](https://www.npmjs.com/package/@dynatrace/cordova-plugin#2-configuration-with-dynatrace) [Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#configurationStructure) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#structure-of-the-dynatracejs-file) [Xamarin](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#config-file) [![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI").NET MAUI](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/maui#config-file)

#### Report a crash manually

For some technologies, you can report a crash manually.

[Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#crashReporting) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#manually-report-a-crash) [Xamarin](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#report-crash) [![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI").NET MAUI](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/maui#report-crash) [OpenKit](/docs/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods#report-crash) 

#### Analyze and use crash data

To view the complete sequence of user actions that preceded a crash, leverage user session analysis. You can also open a crash report to get all the code-level information and quickly trace the root cause of a crash. For additional details, see the following pages.

* [User session analysis | Examine crashes](/docs/observe/digital-experience/session-segmentation/new-user-sessions#crashes "Learn about user session segmentation and filtering attributes.")
* [View crash reports for mobile applications](/docs/observe/digital-experience/mobile-applications/analyze-and-use/crash-reports-mobile "Check the latest crash reports for your mobile applications.")
* [View crash reports for custom applications](/docs/observe/digital-experience/custom-applications/analyze-and-use/crash-reports-custom "Check the latest crash reports for your custom applications.")

With Session Replay on crashes, you receive additional context for your crash analysis. You can watch video-like screen recordings that replay the user actions immediately preceding a detected crash. This feature is available for [Android](/docs/observe/digital-experience/session-replay/session-replay-android "Set up Session Replay for your Android apps to learn which actions your users perform.") and [iOS](/docs/observe/digital-experience/session-replay/session-replay-ios "Prerequisites and the procedure for enabling Session Replay for your iOS apps.").

Note that crashes drastically affect the [user experience score](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score "User experience score is a metric used to categorize user sessions as Frustrating, Tolerable, or Satisfying."). See [Calculate the user experience score](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score#calculate "User experience score is a metric used to categorize user sessions as Frustrating, Tolerable, or Satisfying.") to see why crashed sessions are usually rated as **Frustrating**.