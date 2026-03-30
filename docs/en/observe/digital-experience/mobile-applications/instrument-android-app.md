---
title: Instrument Android apps
source: https://www.dynatrace.com/docs/observe/digital-experience/mobile-applications/instrument-android-app
scraped: 2026-03-05T21:26:31.388242
---

# Instrument Android apps


* Classic
* Overview
* 2-min read
* Updated on Oct 07, 2025

The process of monitoring the user experience of native mobile applications is different from monitoring browser-based web applications. This is because mobile app monitoring involves the compilation, packaging, and shipment of a monitoring library along with your own mobile application package.

To leverage Dynatrace for your Android app, check the get started guide for an overview of the required steps.

You can also explore our new [demo mobile applicationï»¿](https://dt-url.net/rs0229z) to get a feel of how the instrumentation with Dynatrace works. This sample application showcases the main features provided by the Dynatrace Android Gradle Plugin and the OneAgent SDK for Android.

Jetpack Compose auto-instrumentation is enabled by default starting with Dynatrace Android Gradle plugin version 8.271.

Jetpack Compose auto-instrumentation for Session Replay is enabled by default starting with Dynatrace Android Gradle plugin version 8.325.

### Dynatrace Android Gradle plugin

* Instrument your application via Dynatrace Android Gradle plugin
* Configure monitoring capabilities of Dynatrace Android Gradle plugin
* Configure Dynatrace Android Gradle plugin for instrumentation processes
* Adjust OneAgent configuration via Dynatrace Android Gradle plugin
* Change Dynatrace Android Gradle plugin configuration based on the project structure
* Troubleshooting Dynatrace Android Gradle plugin

### OneAgent SDK for Android

* Instrumentation via OneAgent SDK for Android
* Adjust communication with OneAgent SDK for Android
* Manually instrument your application using OneAgent SDK for Android

### Data privacy

Configure data privacy settings for mobile applications

Data safety guidance for Android

### Troubleshooting

[Mobile applications: Issues with mobile RUMï»¿](https://dt-url.net/82038db)

[Mobile applications: General issues with Dynatrace Android Gradle pluginï»¿](https://dt-url.net/b9238e6)

[Mobile applications: Build issues with Dynatrace Android Gradle pluginï»¿](https://dt-url.net/wd438of)

We no longer support Java 8 for the Dynatrace Android Gradle plugin version 8.261+, as Java 11 is required for the latest version of the Android Gradle plugin API.

## Related topics

* Configure Session Replay for Android
* Instrument mobile apps with Dynatrace Xamarin NuGet package