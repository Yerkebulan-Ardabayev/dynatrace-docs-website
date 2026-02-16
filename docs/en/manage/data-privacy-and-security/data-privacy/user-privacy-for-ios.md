---
title: User privacy for iOS
source: https://www.dynatrace.com/docs/manage/data-privacy-and-security/data-privacy/user-privacy-for-ios
scraped: 2026-02-16T21:31:43.694447
---

# User privacy for iOS

# User privacy for iOS

* Latest Dynatrace
* 3-min read
* Updated on Nov 21, 2024

Starting December 8, 2020, Apple requires you to provide information about your app's privacy practices, including the practices of third-party partners like Dynatrace.

On this page, you'll find information about what kind of data [Dynatrace OneAgent for iOS](/docs/observe/digital-experience/mobile-applications/instrument-ios-app "Instrument mobile application monitoring for iOS apps, customize the auto-instrumentation, and capture additional data via manual instrumentation.") captures by default. The data categories and types reflect the Apple questionnaire, but note that the answers reflect the out-of-the-box, default state. For a detailed description of individual data types, see [App privacy details on the App Storeï»¿](https://developer.apple.com/app-store/app-privacy-details/) on the Apple developer portal.

OneAgent may capture additional data through your [manual instrumentation](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios "Enrich mobile user experience monitoring using OneAgent SDK for iOS."). If you instrument your app to capture additional data, make sure you reflect it in your app privacy questionnaire.

Category

Data type

Captured by default?

Notes

Contact Info

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Health & Fitness

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Financial Info

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Location

Precise Location

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

By default, [location monitoring](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#location "Explore the list of features that are available after you instrument your application with OneAgent.") is disabled.

If you've set the [`DTXInstrumentGPSLocation` configuration key](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#privacy-and-security "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") to `true`, select this data type.

Precise Location

Coarse Location

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Sensitive Info

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Contacts

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

User Content

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Browsing History

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Search History

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Identifiers

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Purchases

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Usage Data

Product Interaction

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable") Yes

If you use auto-instrumentation for iOS, taps and clicks the users perform in your mobile app are reported as [user actions](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#user-actions "Explore the list of features that are available after you instrument your application with OneAgent."). Also, Dynatrace captures [rage taps](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#rage-taps "Explore the list of features that are available after you instrument your application with OneAgent."). You can configure the capturing of product interaction data via the [configuration keys related to user actions](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#user-actions "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.").

If you've set the [`DTXInstrumentAutoUserAction`](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#user-actions "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") and [`DTXDetectRageTaps`](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#user-actions "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") configuration keys to `false`, don't select this data type.

Usage Data

Advertising Data

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Usage Data

Other Usage Data

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Diagnostics

Crash Data

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable") Yes

By default, [crash reposting](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#crashes "Explore the list of features that are available after you instrument your application with OneAgent.") is enabled. If you use [Session Replay](/docs/observe/digital-experience/session-replay/session-replay-ios "Prerequisites and the procedure for enabling Session Replay for your iOS apps."), OneAgent also captures masked screenshots and reports several screenshots captured before the crash.

If you've set the [`DTXCrashReportingEnabled` configuration key](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#privacy-and-security "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") to `false` and disabled Session Replay, don't select this data type.

Diagnostics

Performance Data

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable") Yes

By default, monitoring of [lifecycle events](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#lifecycle "Explore the list of features that are available after you instrument your application with OneAgent."), [web requests](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#web-requests "Explore the list of features that are available after you instrument your application with OneAgent."), and [user actions](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#user-actions "Explore the list of features that are available after you instrument your application with OneAgent.") is enabled. You can configure the capturing of performance data data via the configuration keys related to [user actions](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#user-actions "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps."), [web requests](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#web-requests "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps."), and
[lifecycle monitoring](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#lifecycle-monitoring "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.").

If you've set all of the following [configuration keys](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") to `false`, don't select this data type.

* `DTXInstrumentLifecycleMonitoring`
* `DTXInstrumentWebRequestTiming`
* `DTXInstrumentWebViewTiming`
* `DTXInstrumentAutoUserAction`

Diagnostics

Other Diagnostic Data

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable") Yes

OneAgent captures the following diagnostic data:

* Battery level
* Built-in RAM
* Free RAM
* Device model
* CPU type
* Carrier name
* Network connection type, for example, mobile, WiFi, or LAN
* Network technology, for example, 2G, 3G, 4G, 5G, 802.11x
* Screen resolution
* Orientation (portrait or landscape)
* App version
* App name
* User language
* iOS version
* New user (on the first session)

Diagnostics

`shareLogsFile`

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

The `shareLogsFile` API allows you to share locally stored log files via an iOS sharing sheet (`UIActivityViewController`). For more information, see [Log sharing](/docs/manage/data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace#log-sharing "Find out what types of end-user data may be captured during Dynatrace monitoring and the methods that are available for masking personal end-user data.").

Surroundings

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Body

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Other Data

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No