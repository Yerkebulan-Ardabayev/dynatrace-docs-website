---
title: OneAgent for iOS configuration keys
source: https://www.dynatrace.com/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys
scraped: 2026-02-20T21:22:29.073770
---

# OneAgent for iOS configuration keys

# OneAgent for iOS configuration keys

* How-to guide
* 11-min read
* Updated on Jan 02, 2026

Configuration keys are essentially properties you can set to your preferences for auto-instrumentation. Add the keys to your app's [`Info.plist` file](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration."), as required to fine-tune auto-instrumentation.

The following tables include all configuration keys for iOS auto-instrumentation.

## General

Key

Key type

Description

Default value

`DTXApplicationID`

Required

string

Identifies your mobile app. Auto-instrumentation reports an error if the key isn't present.

`DTXBeaconURL`

Required

string

This key's value is used to identify your environment within Dynatrace. Auto-instrumentation reports an error if the key is not present.

`DTXAutoStart`

boolean

When set to `false`, OneAgent doesn't start automatically, so you should [start it manually](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#start-oneagent "Enrich mobile user experience monitoring using OneAgent SDK for iOS.").

`true`

`DTXStartupLoadBalancing`

boolean

When set to `true`, enables agent-side load balancing on startup, which avoids unbalanced load on the server when multiple OneAgents simultaneously establish a connection to the ActiveGate.

`false`

`DTXLogLevel`

string

If this key is present with a valid value, [OneAgent logging](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/logging-for-ios "Turn on debug logging for OneAgent.") is automatically enabled with the set value. If a key isn't present or doesn't have a valid value, automatic logging is turned off and must be turned on manually via API call.

**Possible values**: `OFF`, `SEVERE`, `WARNING`, `INFO`, `ALL`

`OFF`

`DTXStartupWithGrailEnabled`

boolean

When set to `true`, the New RUM Experience is enabled on the first app start, before the cluster configuration is received. This setting has no effect after the first app start. Once cluster configuration is received, it permanently overrides this flag.

`false`

## User actions

Key

Key type

Description

Default value

`DTXInstrumentAutoUserAction`

boolean

Turns on the ability to automatically [create user actions](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#user-actions "Explore the list of features that are available after you instrument your application with OneAgent.") for user interactions with the app, such as button clicks. Set the value to `false` to disable automatic creation of user actions.

`true`

`DTXExcludedControlClasses`

array

An array of items where each item contains the name of a UI control class (or sub-class) to exclude from automatic control instrumentation. Each item in the array is a case-sensitive string that must exactly match the name of the class to be excluded.

`DTXExcludedControls`

array

Defines an array of items where each item contains a type of view or control to exclude from automatic creation of user actions. Each item in the array is a case-insensitive string.

**Possible values**: `Button`, `DatePicker`, `Slider`, `Stepper`, `Switch`, `RefreshControl`, `ToolBar`, `SegmentedControl`, `TableView`, `TabBar`, `AlertView`, `AlertAction`, `PageView`, `NavigationController`, `CollectionView`, `ActionSheet`, `PickerView`

`DTXUIActionNamePrivacy`[1](#fn-1-1-def)

boolean

When set to `true`, enables [user action masking](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#mask-user-actions "Enrich mobile user experience monitoring using OneAgent SDK for iOS.").

* **UIKit-based apps**. OneAgent replaces control titles in user action names with generic control types.
* **SwiftUI-based apps**. OneAgent doesn't report the child events that contain the control titles of "touch" user actions.

As a result, all `Touch on <control title>` user action names are changed to `Touch on <generic control type>`. For example, `Touch on Account 123456` becomes `Touch on Button`.

`false`

`DTXDetectRageTaps`

boolean

Defines if [rage tap detection](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#rage-taps "Explore the list of features that are available after you instrument your application with OneAgent.") is enabled or not. Use this feature as a measure of user frustration. Set the value to `false` to stop detecting rage taps.

`true`

`DTXSendEmptyAutoAction`

boolean

Determines whether to send automatic user actions that don't contain any web requests or lifecycle actions.

`true`

`DTXAutoActionMaxDurationMilliseconds`

number

Sets the amount of time to retain an automatic user action before deletion. The purpose is to detect all web requests that occur when an automatic user action is active. If an automatic user action has pending web requests that are taking longer to complete, OneAgent waits for this amount of time for the web requests to complete before leaving the user action.

**Possible values**: from `100` ms (= 0.1 seconds) to `540000` ms (= 9 minutes)

`60000` ms

`DTXAutoActionTimeoutMilliseconds`

number

Sets the value for how long a particular automatic user action is active. The purpose is to detect all web requests that occur when an automatic user action is active. If the automatic user action has completed web requests, OneAgent leaves the action at the end of this time.

**Possible values**: from `100` ms (= 0.1 seconds) to `5000` ms (= 5 seconds)

`500` ms

1

Available for OneAgent for iOS version 8.249+

## Web requests

Key

Key type

Description

Default value

`DTXInstrumentWebRequestTiming`

boolean

Turns on automatic [web request timing and tagging](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#web-requests "Explore the list of features that are available after you instrument your application with OneAgent."). To [disable automatic web request timing and tagging](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#disable-auto-request-instrumentation "Enrich mobile user experience monitoring using OneAgent SDK for iOS."), set the value to `false`.

`true`

`DTXURLFilters`

array

An array of items where each item contains the URL filters to exclude web requests from monitoring. Each item in the array should be a URL string or regular expression matching the URL your want to filter.

`DTXFilterURLProtocolDuplicates`

boolean

Required if NSURLProtocol subclassing is used and duplicate web requests may appear.

`false`

## Lifecycle monitoring

Key

Key type

Description

Default value

`DTXInstrumentLifecycleMonitoring`

boolean

Enables automatic [lifecycle detection](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#lifecycle "Explore the list of features that are available after you instrument your application with OneAgent.") for iOS `ViewController` classes. To disable automatic lifecycle monitoring, set the value to `false`.

`true`

`DTXInstrumentFrameworks`[1](#fn-2-1-def)

obsolete

boolean

Enables automatic lifecycle instrumentation of UI classes from third-party frameworks that are bundled with the application. Set the value to `true` to enable automatic third-party framework lifecycle instrumentation. This configuration requires OneAgent for iOS to scan all frameworks bundled with your application, which can result in a noticeable performance impact at the application start.

`false`

`DTXExcludedLifecycleClasses`

array

An array of items where each item contains the name of a class to exclude from automatic lifecycle instrumentation. Each item in the array is a case-sensitive string that must exactly match the name of the class to be excluded.

1

Obsolete starting with OneAgent for iOS version 8.331

## Hybrid apps



Key

Key type

Description

Default value

`DTXHybridApplication`

boolean

For [hybrid apps](/docs/observe/digital-experience/mobile-applications/instrument-hybrid-app "Learn how you can instrument various types of hybrid and cross-platform mobile apps."), set the value to `true`. This is necessary to share the same visit for user actions created by the RUM JavaScript.

`false`

`DTXSetCookiesForDomain`

array[string]

For hybrid apps that use the RUM JavaScript, [cookies must be set](/docs/observe/digital-experience/mobile-applications/instrument-hybrid-app#set-up-oneagent "Learn how you can instrument various types of hybrid and cross-platform mobile apps.") for each instrumented domain or server that the app communicates with. You can specify domains, host, or IP addresses. Domains and sub-domains must start with a dot.

`DTXSetSecureCookiesForDomain`

array[string]

For hybrid apps that use the RUM JavaScript, [cookies must be set](/docs/observe/digital-experience/mobile-applications/instrument-hybrid-app#set-up-oneagent "Learn how you can instrument various types of hybrid and cross-platform mobile apps.") for each instrumented domain or server that the app communicates with. You can specify domains, host, or IP addresses. Domains and sub-domains must start with a dot.
This configuration key is similar to `DTXSetCookiesForDomain`, but the `Secure` cookie attribute is added for cookies that are set by Dynatrace. This ensures that the browser sends these cookies only over secure connections.

`DTXInstrumentWebViewTiming`

boolean

Turns on automatic [web request timing and tagging for requests passed to `WKWebView`](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#web-requests-wkwebview "Explore the list of features that are available after you instrument your application with OneAgent."). This doesn't work for requests issued from JavaScript inside `WKWebView`. Set the value to `false` to disable automatic web request timing and tagging.

`true`

`DTXWebViewStandInDelegate`[1](#fn-3-1-def)

obsolete

boolean

Use different instrumentation mode for `WKWebView` delegates to prevent circular instrumentation on delegate switching involving a subclass.

`false`

1

Obsolete starting with OneAgent for iOS version 8.257

## Privacy and security

Key

Key type

Description

Default value

`DTXUserOptIn`

boolean

When set to `true`, activates [user opt-in mode](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

When user opt-in mode is enabled, you need to ask each user for permission to capture their data; then, you store their data privacy preferences. For details, see [Configure data privacy](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#privacy "Enrich mobile user experience monitoring using OneAgent SDK for iOS.").

`false`

`DTXCrashReportingEnabled`

boolean

Enables [crash reporting](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#crashes "Explore the list of features that are available after you instrument your application with OneAgent."). To disable crash reporting, set the value to `false`.

`true`

`DTXInstrumentGPSLocation`

boolean

When set to `true`, enables [location monitoring](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#location "Explore the list of features that are available after you instrument your application with OneAgent."). The location is captured when the app uses `CLLocationManager` and sends the captured location as a metric to the server. The OneAgent SDK for iOS doesn't perform GPS location capture on its own; to protect the privacy of the end user, it only captures a precision of three fractional digits.

`false`

`DTXPublicKeyPins`

array[string]

Includes the `getPKHashFromCertificate.py` script outputs used to enable the [Public Key Hash Pinning](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/configuration-settings#pkh-pinning "Configure auto-instrumentation for iOS apps using advanced settings.") feature for your mobile app.

`DTXAgentCertificatePath`

string

Defines the path to a (self-signed) certificate in `DER` format, which is used as an additional anchor to validate HTTPS communication. This key is needed if `DTXAllowAnyCert` is `false` and a self-signed certificate is used on the server.

`null`

`DTXAllowAnyCert`

boolean

Allows the use of self-signed certificates. When set to `true`, OneAgent for iOS accepts self-signed certificates (certificates that are not signed by a `root-CA`). This configuration key doesn't impact mobile app connections. It's only used for OneAgent communication, but doesn't overrule the host-name validation.

`false`

`DTXWriteLogsToFile`

boolean

When set to `true`, enables OneAgent to write logs to the device's local storage. This flag is required to be set to `true` for using the [`shareLogsFile`](/docs/manage/data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace#log-sharing "Find out what types of end-user data may be captured during Dynatrace monitoring and the methods that are available for masking personal end-user data.") API, which allows sharing of logs via an iOS sharing sheet (`UIActivityViewController`). This feature is not available on tvOS.

`false`

`DTXANRReportingEnabled`

boolean

Enables reporting of "Application Not Responding" (ANR) errors. To disable ANR reporting, set this value to `false`.

`true`

`DTXANRTimeout`

number

Sets the "Application Not Responding" (ANR) detection timeout. Change this value to adapt the timeout required for an ANR to be detected.

**Possible values**: from `1` second to `20` seconds

`2`

## SwiftUI

Key

Key type

Description

Default value

`DTXSwiftUIEnableSessionReplayInstrumentation`[1](#fn-4-1-def)

boolean

When set to `true`, enables [Session Replay for your SwiftUI apps](/docs/observe/digital-experience/session-replay/session-replay-ios#sr-swiftui "Prerequisites and the procedure for enabling Session Replay for your iOS apps.").

`false`

`DTXExcludedSwiftUIFiles`[1](#fn-4-1-def)

array[string]

Includes relative paths of files and directories that are [excluded from the SwiftUI instrumentation](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#exclude-swift-files "Use the Dynatrace SwiftUI instrumentor to monitor your SwiftUI apps."). The paths are relative to the project root, which is the directory where the `.xcodeproj` file is located.

`DTXSwiftUIExcludedControls`[3](#fn-4-3-def)

array[string]

Specifies SwiftUI controls that are [globally excluded from the SwiftUI instrumentation](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#exclude-controls-global "Use the Dynatrace SwiftUI instrumentor to monitor your SwiftUI apps.").

**Possible values**: all values under [Supported controls](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#supported-controls "Use the Dynatrace SwiftUI instrumentor to monitor your SwiftUI apps.")

`DTXSwiftUIInstrumentSimulatorBuilds`[1](#fn-4-1-def)

boolean

When set to `true`, enables the [SwiftUI instrumentation for simulator builds](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#instrument-simulator-builds "Use the Dynatrace SwiftUI instrumentor to monitor your SwiftUI apps.").

`DTXSwiftUIIgnoreDeploymentTarget`[1](#fn-4-1-def)

boolean

When set to `true`, allows you to [generate builds for deployment targets of iOS 13 and earlier](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#builds-for-unsupported-deployment-targets "Use the Dynatrace SwiftUI instrumentor to monitor your SwiftUI apps.").

`DTXSwiftUIManualPlaceholder`[1](#fn-4-1-def)

boolean

When set to `true`, [enables line number mapping](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#line-number-mapping-objective-c "Use the Dynatrace SwiftUI instrumentor to monitor your SwiftUI apps.") for legacy Objective-C projects. Note that additional configuration is required.

`DTXCleanSwiftUILogsByCount`[2](#fn-4-2-def)

number

Sets the number of builds after which the [SwiftUI instrumentor logs are deleted](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#enable-log-cleanup "Use the Dynatrace SwiftUI instrumentor to monitor your SwiftUI apps.").

**Possible values**: from `1` to `1000`

`DTXCleanSwiftUILogsByAgeDays`[2](#fn-4-2-def)

number

Sets the number of days after which the [SwiftUI instrumentor logs are deleted](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#enable-log-cleanup "Use the Dynatrace SwiftUI instrumentor to monitor your SwiftUI apps.").

**Possible values**: from `1` to `500`

1

Available for OneAgent for iOS version 8.249+

2

Available for OneAgent for iOS version 8.257+

3

Available for OneAgent for iOS version 8.263+