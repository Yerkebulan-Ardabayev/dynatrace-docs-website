---
title: Instrument iOS apps in RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app
---

# Instrument iOS apps in RUM Classic

# Instrument iOS apps in RUM Classic

* Overview
* 1-min read
* Updated on Jun 10, 2026

The process of monitoring the user experience of your native mobile apps is fundamentally different from monitoring browser-based web applications. This is because mobile-app monitoring involves the compilation, packaging, and shipment of a monitoring library along with your own mobile application package.

To monitor your mobile app with Dynatrace, you'll need to instrument OneAgent for iOS, which provides visibility into activity lifecycle, user actions, web requests, crashes, and more.

For the supported iOS versions, check [Technology support | Mobile app Real User Monitoring](/managed/ingest-from/technology-support#mobile-rum "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

### Instrumentation

* [Get started with iOS monitoring in RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/get-started-with-ios-monitoring "Learn the steps you need to perform to instrument your iOS app for monitoring with Dynatrace.")
* [Set up OneAgent for your iOS apps in RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios "Set up user experience monitoring for iOS apps within Dynatrace.")
* [Instrument SwiftUI controls in RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls "Use the Dynatrace SwiftUI instrumentor to monitor your SwiftUI apps.")
* [OneAgent for iOS auto-instrumentation features in RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features "Explore the list of features that are available after you instrument your application with OneAgent.")
* [Info.plist file in RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration.")

### Customization

* [OneAgent for iOS advanced configuration in RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/configuration-settings "Configure auto-instrumentation for iOS apps using advanced settings.")
* [OneAgent for iOS configuration keys in RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.")
* [OneAgent SDK for iOS in RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios "Enrich mobile user experience monitoring using OneAgent SDK for iOS.")
* [OneAgent for iOS debug logging in RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/logging-for-ios "Turn on debug logging for OneAgent.")

### Data privacy

[Configure data privacy settings for mobile applications in RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.")

[User privacy for iOS](/managed/manage/data-privacy-and-security/data-privacy/user-privacy-for-ios "Learn about what kind of data OneAgent collects when you need to report your app privacy to Apple.")

Starting with OneAgent for iOS version 8.335, Dynatrace stopped supporting Xcode 16. We only support Xcode 26+.

Also, be aware that [Apple's App Store submission guidelines﻿](https://dt-url.net/we038fb) will restrict support to applications built with a minimum of Xcode 26 around April 2026.

Starting with OneAgent for iOS version 8.343, Dynatrace will stop supporting iOS 12, iOS 13, and iOS 14. The new minimum supported version is iOS 15. Version 8.341 is the last OneAgent for iOS version to support iOS 12 - 14.

Starting with OneAgent for iOS version 8.323, Dynatrace will stop supporting `static builds` and `Carthage` as integration methods.

We recommend migrating to a supported alternative like Swift Package Manager to ensure continued compatibility and updates.

OneAgent for iOS version 8.249 is the last version that supports the 32-bit architecture.