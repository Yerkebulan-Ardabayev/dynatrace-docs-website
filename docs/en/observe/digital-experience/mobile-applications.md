---
title: Mobile applications
source: https://www.dynatrace.com/docs/observe/digital-experience/mobile-applications
scraped: 2026-03-06T21:14:02.066070
---

# Mobile applications


* Classic
* Overview
* 1-min read
* Published Feb 06, 2023

Mobile applications are native mobile apps on iOS or Android as well as hybrid applications accessed through a browser.

### Instrument Android apps

* [Instrument your application via Dynatrace Android Gradle plugin](mobile-applications/instrument-android-app/instrumentation-via-plugin/instrumentation-via-plugin.md "Perform the steps in this topic before you begin instrumenting your app with the Dynatrace Android Gradle plugin.")
* [Configure monitoring capabilities of Dynatrace Android Gradle plugin](mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities.md "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.")
* [Configure Dynatrace Android Gradle plugin for instrumentation processes](mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation.md "Learn how to configure the Dynatrace Android Gradle plugin to adjust the auto-instrumentation process.")
* [Adjust OneAgent configuration via Dynatrace Android Gradle plugin](mobile-applications/instrument-android-app/instrumentation-via-plugin/adjust-oneagent-configuration.md "Learn how to configure the Dynatrace Android Gradle plugin to modify the OneAgent SDK configuration.")
* [Change Dynatrace Android Gradle plugin configuration based on the project structure](mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-multi-module-projects.md "Use the Dynatrace Android Gradle plugin for less common project architectures.")
* [Troubleshooting Dynatrace Android Gradle plugin](mobile-applications/instrument-android-app/instrumentation-via-plugin/faqs.md "Learn about the problems that might occur while using the Dynatrace Android Gradle plugin.")
* [Instrumentation via OneAgent SDK for Android](mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android.md "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK.")
* [Adjust communication with OneAgent SDK for Android](mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/adjust-oneagent-communication.md "Configure communication with OneAgent to report the user experience data to Dynatrace.")
* [Manually instrument your application using OneAgent SDK for Android](mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation.md "Use OneAgent SDK for Android to manually instrument your Android application.")

### Instrument iOS apps

* [Get started with iOS monitoring](mobile-applications/instrument-ios-app/instrumentation/get-started-with-ios-monitoring.md "Learn the steps you need to perform to instrument your iOS app for monitoring with Dynatrace.")
* [Set up OneAgent for your iOS apps](mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios.md "Set up user experience monitoring for iOS apps within Dynatrace.")
* [Instrument SwiftUI controls](mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls.md "Use the Dynatrace SwiftUI instrumentor to monitor your SwiftUI apps.")
* [OneAgent for iOS auto-instrumentation features](mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features.md "Explore the list of features that are available after you instrument your application with OneAgent.")
* [Info.plist file](mobile-applications/instrument-ios-app/instrumentation/info-plist-file.md "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration.")
* [OneAgent for iOS advanced configuration](mobile-applications/instrument-ios-app/customization/configuration-settings.md "Configure auto-instrumentation for iOS apps using advanced settings.")
* [OneAgent for iOS configuration keys](mobile-applications/instrument-ios-app/customization/ios-configuration-keys.md "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.")
* [OneAgent SDK for iOS](mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios.md "Enrich mobile user experience monitoring using OneAgent SDK for iOS.")
* [OneAgent for iOS debug logging](mobile-applications/instrument-ios-app/customization/logging-for-ios.md "Turn on debug logging for OneAgent.")

### Instrument hybrid apps

[Instrument hybrid apps](mobile-applications/instrument-hybrid-app.md "Learn how you can instrument various types of hybrid and cross-platform mobile apps.")

### Cross-platform frameworks

* [Instrument mobile apps with Dynatrace Cordova plugin](mobile-applications/cross-platform-frameworks/apache-cordova.md "Set up Dynatrace to monitor hybrid mobile apps with the Cordova plugin.")
* [Instrument mobile apps with Dynatrace Flutter plugin](mobile-applications/cross-platform-frameworks/flutter.md "Learn how to auto-instrument your Flutter applications with OneAgent.")
* [Instrument mobile apps with Dynatrace React Native plugin](mobile-applications/cross-platform-frameworks/react-native.md "Auto-instrument your React Native applications with OneAgent.")
* [Instrument mobile apps with Dynatrace Xamarin NuGet package](mobile-applications/cross-platform-frameworks/xamarin-nuget.md "Monitor Xamarin apps with Dynatrace OneAgent.")
* [Instrument mobile apps with Dynatrace .NET MAUI NuGet package](mobile-applications/cross-platform-frameworks/maui.md "Monitor .NET MAUI applications with Dynatrace OneAgent.")

### Additional configuration

* [Configure cost and traffic control for mobile applications](mobile-applications/additional-configuration/configure-cost-and-traffic-control-mobile.md "Leverage the cost and traffic control setting in Dynatrace to reduce session usage for mobile apps.")
* [Configure data privacy settings for mobile applications](mobile-applications/additional-configuration/configure-rum-privacy-mobile.md "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.")
* [Ignore web request errors for mobile applications](mobile-applications/additional-configuration/web-request-errors-mobile.md "Stop treating certain response HTTP codes as errors for your mobile applications.")
* [Create custom user action names for mobile applications](mobile-applications/additional-configuration/naming-rules-mobile.md "Customize automatically generated user action names for your mobile applications.")
* [Configure key user actions for mobile applications](mobile-applications/additional-configuration/configure-key-user-actions-mobile.md "Mark a user action as a key user action and configure Apdex rating for key user actions of your mobile applications.")
* [Adjust Apdex settings for mobile applications](mobile-applications/additional-configuration/configure-apdex-mobile.md "Configure the user-satisfaction performance thresholds for your mobile application and its key user actions.")
* [Change user experience score thresholds for mobile applications](mobile-applications/additional-configuration/configure-user-experience-score-mobile.md "Adjust the user experience score thresholds to meet the specific requirements of your mobile application.")
* [Create calculated metrics for mobile applications](mobile-applications/additional-configuration/rum-calculated-metrics-mobile.md "Create calculated metrics as well as custom charts based on calculated metrics for your mobile applications.")
* [Create USQL custom metrics for mobile applications](mobile-applications/additional-configuration/custom-metrics-from-user-sessions-mobile-apps.md "Every time a user session is closed, Dynatrace can extract metrics and store them as time series. Learn how to set up and use USQL custom metrics for mobile applications.")
* [Define user action and user session properties for mobile applications](mobile-applications/additional-configuration/define-mobile-action-and-session-properties.md "Send metadata to Dynatrace and define action and session properties for your monitored mobile applications.")
* [Customize IP address detection for mobile applications](mobile-applications/additional-configuration/customize-ip-address-detection-mobile.md "Change the way Dynatrace determines client IP addresses for your mobile applications.")
* [Map internal IP addresses to locations for mobile applications](mobile-applications/additional-configuration/map-internal-ip-addresses-to-locations-mobile.md "Configure Dynatrace to use local addresses to understand where the users of your mobile applications are.")
* [Configure first-party, third-party, and CDN resource detection for mobile applications](mobile-applications/additional-configuration/configure-third-party-and-cdn-content-detection-mobile.md "Manually define third-party and CDN providers along with auto-detected providers for your mobile applications.")
* [Use OneAgent as a beacon endpoint for mobile applications](mobile-applications/additional-configuration/oneagent-as-beacon-forwarder-mobile.md "Use Dynatrace OneAgent as a beacon endpoint for mobile applications.")
* [Delete a mobile application](mobile-applications/additional-configuration/delete-application-mobile.md "Delete your mobile applications via the Dynatrace web UI or API.")

### Analyze and use RUM data

* [Analyze user sessions of mobile applications](mobile-applications/analyze-and-use/mobile-user-session-analysis.md "Filter user sessions, view sessions of an individual user, and examine crashes, request errors, and report errors for your mobile applications.")
* [Check user experience metrics for mobile applications](mobile-applications/analyze-and-use/check-usage-metrics-mobile.md "Learn how to use Dynatrace to check the user experience metrics of your mobile application.")
* [Analyze web requests for mobile applications](mobile-applications/analyze-and-use/analyze-web-requests-mobile.md "Leverage Dynatrace to monitor web requests for your mobile applications.")
* [View crash reports for mobile applications](mobile-applications/analyze-and-use/crash-reports-mobile.md "Check the latest crash reports for your mobile applications.")
* [Upload and manage symbol files for mobile applications](mobile-applications/analyze-and-use/upload-and-manage-symbol-files.md "Learn about deobfuscation (Android) and symbolication (iOS and tvOS) and your options for uploading and managing symbol files in Dynatrace.")
* [Leverage user action and user session properties for mobile applications](mobile-applications/analyze-and-use/action-and-session-properties-mobile.md "User action and session properties, which are metadata key-value pairs, provide added visibility and deeper analysis of your end users' experience. Using these properties for your applications, you can filter user sessions, add calculated metrics, create charts, and more.")

### Troubleshooting

[General limitations for RUM mobile applications](mobile-applications/general-limitations.md "General limitations related to RUM for your mobile applications.")

[Troubleshooting RUM for mobile applications](mobile-applications/troubleshooting.md "Troubleshoot and fix issues related to RUM for your mobile applications.")