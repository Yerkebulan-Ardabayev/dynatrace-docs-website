---
title: Get started with iOS monitoring
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/get-started-with-ios-monitoring
scraped: 2026-05-12T11:32:52.882328
---

# Get started with iOS monitoring

# Get started with iOS monitoring

* How-to guide
* 1-min read
* Updated on Sep 19, 2022

To monitor your mobile app with Dynatrace, you first need to create an application in Dynatrace and then instrument your actual mobile app with OneAgent for iOS.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create an application in Dynatrace**

Create a mobile application in the Dynatrace web UI](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios#create-app-in-ui "Set up user experience monitoring for iOS apps within Dynatrace.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Set up OneAgent**

Instrument your app via CocoaPods, Swift Package Manager, or manual approach](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios#set-up-oneagent "Set up user experience monitoring for iOS apps within Dynatrace.")[![Step 3 optional](https://dt-cdn.net/images/dotted-step-3-e2082c1921.svg "Step 3 optional")

**Instrument SwiftUI controls**

Instrument SwiftUI buttons, stepper, toggles, and more](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls "Use the Dynatrace SwiftUI instrumentor to monitor your SwiftUI apps.")

After instrumenting your iOS app with OneAgent, you might want to fine-tune the instrumentation according to your needs:

* Adjust the [auto-instrumentation features](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features "Explore the list of features that are available after you instrument your application with OneAgent.") via [configuration keys](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.").
* Capture additional data via [manual instrumentation](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios "Enrich mobile user experience monitoring using OneAgent SDK for iOS.").
* [Configure the data privacy settings](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.") for your iOS apps; for example, set up the user opt-in mode or mask user actions.
* Learn what [data OneAgent for iOS captures](/managed/manage/data-privacy-and-security/data-privacy/user-privacy-for-ios "Learn about what kind of data OneAgent collects when you need to report your app privacy to Apple.") to complete or update the App Store Connect questionnaire on data privacy.