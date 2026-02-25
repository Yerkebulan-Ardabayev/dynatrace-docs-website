---
title: Instrument mobile apps with Dynatrace Flutter plugin
source: https://www.dynatrace.com/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/flutter
scraped: 2026-02-25T21:20:26.909447
---

# Instrument mobile apps with Dynatrace Flutter plugin

# Instrument mobile apps with Dynatrace Flutter plugin

* How-to guide
* 1-min read
* Updated on Nov 26, 2024

The Dynatrace Flutter plugin adds the Dynatrace OneAgent for Android and iOS to your Flutter app and provides an API to use manual instrumentation for Flutter/Dart data capture.

For detailed technical documentation, see the [Dynatrace Flutter Pluginï»¿](https://pub.dev/packages/dynatrace_flutter_plugin) page on the pub.dev site.

## Prerequisites

* Dynatrace version 1.203+
* Dart version 2.12+
* Flutter version 1.12.0+
* Gradle version 7.0+
* Android version 5.0+ (API 21+)
* Java 11+
* iOS version 12+

## Set up a Flutter mobile app

1. In Dynatrace, go to **Mobile**.
2. Select **Create mobile app**.
3. Enter a name for your application and select **Create mobile app**. The application settings page opens.
4. From the application settings, select **Instrumentation wizard** > **Flutter**.
5. Follow the steps described in the wizard.

### Demo

For example instrumentation of a compact app, see the **Example** tab of the [Dynatrace Flutter pluginï»¿](https://pub.dev/packages/dynatrace_flutter_plugin/example) page.