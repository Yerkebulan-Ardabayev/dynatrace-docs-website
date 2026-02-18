---
title: OneAgent for iOS auto-instrumentation features
source: https://www.dynatrace.com/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features
scraped: 2026-02-18T05:55:10.354270
---

# OneAgent for iOS auto-instrumentation features

# OneAgent for iOS auto-instrumentation features

* Explanation
* 4-min read
* Updated on Feb 03, 2026

Auto-instrumentation with OneAgent for iOS occurs during runtime. The resulting application is instrumented to the levels configured in the application's [`Info.plist` file](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration.").

The following features are automatically instrumented when you [set up OneAgent](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios "Set up user experience monitoring for iOS apps within Dynatrace.") for your project. These features are enabled by default, but you can disable or configure them by adding [configuration keys](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") to your application's `Info.plist` file.

Use auto-instrumentation in combination with [manual instrumentation](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios "Enrich mobile user experience monitoring using OneAgent SDK for iOS.") to capture additional data. For example, you might want to manually instrument certain actions, report values, or tag specific users.

## Automatic OneAgent startup

OneAgent for iOS is initialized automatically at library load timeâthis is when the binary for the OneAgent library is loaded into a mobile application at application startup. This happens before `applicationWillFinishLaunching`, where OneAgent can be started manually.

Set the [`DTXAutoStart` configuration key](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#general "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") to `false` to disable automatic OneAgent startup. In that case, you'll need to [start OneAgent manually](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#start-oneagent "Enrich mobile user experience monitoring using OneAgent SDK for iOS.").

## Lifecycle monitoring

OneAgent collects data on the following events.

* `AppStart` (application start event)

  + Automatic OneAgent startup: Measures the timespan from when OneAgent starts to when the [`application(_:didFinishLaunchingWithOptions:)`ï»¿](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) method is called.
  + Manual OneAgent startup: Measures the timespan from when the [OneAgent manual startup API](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#start-oneagent "Enrich mobile user experience monitoring using OneAgent SDK for iOS.") is called to when the `application(_:didFinishLaunchingWithOptions:)` method is called. When the manual startup API is called after `application(_:didFinishLaunchingWithOptions:)`, the `AppStart` event is not generated.
* `Display`: Measures the timespan from loading a view to when the view appears on the screen. Timestamps of the `viewDidLoad`, `viewWillAppear`, and `viewDidAppear` calls of the `ViewController` classes are displayed in the user action waterfall analysis and are marked as a **Lifecycle event**.
* `Redisplay`: Measures the timespan from loading a view to when the view reappears on the screen. Timestamps of the `viewWillAppear` and `viewDidAppear` calls of the `ViewController` classes are displayed in the user action waterfall analysis and are marked as a **Lifecycle event**.

Set the [`DTXInstrumentLifecycleMonitoring` configuration key](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#lifecycle-monitoring "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") to `false` to disable automatic lifecycle monitoring. Also, check other keys in the [**Lifecycle monitoring**](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#lifecycle-monitoring "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") section for more configuration options.

To learn which lifecycle events are reported for SwiftUI, see [Instrument SwiftUI controls | Lifecycle monitoring](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#lifecycle "Use the Dynatrace SwiftUI instrumentor to monitor your SwiftUI apps.").

## Crash reporting

OneAgent captures all unhandled exceptions and sends the [crash](/docs/observe/digital-experience/rum-concepts/user-and-error-events#crash "Learn about user and error events and the types of user and error events captured by Dynatrace.") report to the server. The crash report includes the occurrence time and the full stack trace of the exception.

The crash details are sent only when the user reopens the mobile application (so on the next application launch). However, if the user doesn't open the application within 10 minutes, the crash report is deleted. This is because Dynatrace doesn't send crash reports that are older than 10 minutes (as such reports can no longer be correlated on the Dynatrace Cluster).

Set the [`DTXCrashReportingEnabled` configuration key](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#privacy-and-security "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") to `false` to disable crash reporting.

## Web request monitoring

OneAgent automatically instruments and tags your web requests. To track web requests, OneAgent adds the `x-dynatrace` HTTP header with a unique value to the web request. This is required to correlate the server-side monitoring data to the corresponding mobile web request.

Set the [`DTXInstrumentWebRequestTiming` configuration key](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#web-requests "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") to `false` to disable web request monitoring. Also, check other keys in the [**Web requests**](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#web-requests "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") section to configure web request timing and tagging.

To learn how to manually instrument web requests, see [Measure web requests](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#measure-web-requests "Enrich mobile user experience monitoring using OneAgent SDK for iOS.").

## Web request monitoring for requests passed to `WKWebView`

OneAgent automatically instruments and tags web requests that are passed to `WKWebView`.

Note that OneAgent does not monitor requests issued inside `WKWebView`. Such requests are handled by the [RUM JavaScript](/docs/observe/digital-experience/web-applications/additional-configuration/customize-rum "Find out how to customize Real User Monitoring using the JavaScript API.") if you've properly configured your [hybrid application monitoring](/docs/observe/digital-experience/mobile-applications/instrument-hybrid-app "Learn how you can instrument various types of hybrid and cross-platform mobile apps.") with Dynatrace.

Set the [`DTXInstrumentWebViewTiming` configuration key](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#hybrid "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") to `false` to disable automatic web request timing and tagging for requests passed to `WKWebView`.

## User action detection



OneAgent detects and times user actions such as button taps, view actions, and other UI control interactions. OneAgent creates user actions based on the UI components that trigger these actions and automatically combines user action data with other monitoring data, such as information on web requests and crashes. OneAgent extends the lifetime of user actions to properly aggregate them with other events that are executed in a background thread or immediately after a user action.

Set the [`DTXInstrumentAutoUserAction` configuration key](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#user-actions "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") to `false` to disable automatic creation of user actions. Also, check other configuration keys in the [**User actions**](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#user-actions "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") section to control user action detection.

Using OneAgent for iOS, you can also perform the following actions related to user actions.

* [Create custom actions](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#create-custom-user-action "Enrich mobile user experience monitoring using OneAgent SDK for iOS.")
* [Cancel custom and autogenerated user action](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#cancel-action "Enrich mobile user experience monitoring using OneAgent SDK for iOS.")
* [Use custom control titles](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#custom-control-names "Enrich mobile user experience monitoring using OneAgent SDK for iOS.")
* [Modify autogenerated actions](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#modify-auto-actions "Enrich mobile user experience monitoring using OneAgent SDK for iOS.")
* [Mask user actions](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#mask-user-actions "Enrich mobile user experience monitoring using OneAgent SDK for iOS.")

To learn how OneAgent constructs user action names, see [User action naming](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#user-action-naming "Enrich mobile user experience monitoring using OneAgent SDK for iOS.").

## Rage tap detection

When your mobile application doesn't respond quickly or there's a user interface issue, your users might repeatedly tap the screen or affected UI control. OneAgent detects such behavior as a [rage tap](/docs/observe/digital-experience/rum-concepts/user-and-error-events#rage-event "Learn about user and error events and the types of user and error events captured by Dynatrace.").

Set the [`DTXDetectRageTaps` configuration key](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#user-actions "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") to `false` to stop detecting rage taps.

## Location monitoring

ð´ Disabled by default

OneAgent can capture the location of your application's end users and send the captured location as a metric to the server. To protect the privacy of your users, OneAgent captures GPS coordinates with a precision of two decimal places (~1 km accuracy).

Set the [`DTXInstrumentGPSLocation` configuration key](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#privacy-and-security "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") to `true` to enable location capturing.