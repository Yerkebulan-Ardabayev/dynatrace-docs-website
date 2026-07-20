---
title: Instrument mobile apps with Dynatrace Flutter plugin in RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/flutter
---

# Instrument mobile apps with Dynatrace Flutter plugin in RUM Classic

# Instrument mobile apps with Dynatrace Flutter plugin in RUM Classic

* How-to guide
* 1-min read
* Updated on Jun 22, 2026

The Dynatrace Flutter plugin adds the Dynatrace OneAgent for Android and iOS to your Flutter app and provides an API to use manual instrumentation for Flutter/Dart data capture.

For detailed technical documentation, see the [Dynatrace Flutter Plugin﻿](https://pub.dev/packages/dynatrace_flutter_plugin) page on the pub.dev site.

## Prerequisites

* Dynatrace version 1.203+
* Dart version 2.12+
* Flutter version 1.12.0+
* Gradle version 8.0+
* Android version 6.0+ (API 23+)
* Java 17+
* iOS version 15+

## Set up a Flutter mobile app

1. In Dynatrace, go to **Mobile**.
2. Select **Create mobile app**.
3. Enter a name for your application and select **Create mobile app**. The application settings page opens.
4. From the application settings, select **Instrumentation wizard** > **Flutter**.
5. Follow the steps described in the wizard.

### Demo

For example instrumentation of a compact app, see the **Example** tab of the [Dynatrace Flutter plugin﻿](https://pub.dev/packages/dynatrace_flutter_plugin/example) page.