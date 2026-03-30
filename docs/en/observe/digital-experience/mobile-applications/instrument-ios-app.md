---
title: Instrument iOS apps
source: https://www.dynatrace.com/docs/observe/digital-experience/mobile-applications/instrument-ios-app
scraped: 2026-03-05T21:26:00.148955
---

# Instrument iOS apps


* Classic
* Overview
* 1-min read
* Updated on Feb 09, 2026

The process of monitoring the user experience of your native mobile apps is fundamentally different from monitoring browser-based web applications. This is because mobile-app monitoring involves the compilation, packaging, and shipment of a monitoring library along with your own mobile application package.

To monitor your mobile app with Dynatrace, you'll need to instrument OneAgent for iOS, which provides visibility into activity lifecycle, user actions, web requests, crashes, and more.

Explore our new [demo mobile applicationï»¿](https://dt-url.net/332226v) to get a feel of how the instrumentation with Dynatrace works. This sample application showcases the main features provided by the OneAgent SDK for iOS.

For the supported iOS versions, check [Technology support | Mobile app Real User Monitoring](../../../ingest-from/technology-support.md#mobile-rum "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

### Instrumentation

* Get started with iOS monitoring
* Set up OneAgent for your iOS apps
* Instrument SwiftUI controls
* OneAgent for iOS auto-instrumentation features
* Info.plist file

### Customization

* OneAgent for iOS advanced configuration
* OneAgent for iOS configuration keys
* OneAgent SDK for iOS
* OneAgent for iOS debug logging

### Data privacy

Configure data privacy settings for mobile applications

User privacy for iOS

Starting with OneAgent for iOS version 8.335, Dynatrace stopped supporting Xcode 16. We only support Xcode 26+.

Also, be aware that [Apple's App Store submission guidelinesï»¿](https://dt-url.net/we038fb) will restrict support to applications built with a minimum of Xcode 26 around April 2026.

Starting with OneAgent for iOS version 8.323, Dynatrace will stop supporting `static builds` and `Carthage` as integration methods.

We recommend migrating to a supported alternative like Swift Package Manager to ensure continued compatibility and updates.

OneAgent for iOS version 8.249 is the last version that supports the 32-bit architecture.