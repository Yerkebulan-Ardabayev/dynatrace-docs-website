---
title: Enable debug logging for Dynatrace Android Gradle plugin or OneAgent SDK
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/instrument-android-app/debug-logging-oneagent
scraped: 2026-05-12T12:05:48.090151
---

# Enable debug logging for Dynatrace Android Gradle plugin or OneAgent SDK

# Enable debug logging for Dynatrace Android Gradle plugin or OneAgent SDK

* How-to guide
* 2-min read
* Updated on Mar 05, 2026

Activate debug logging for Dynatrace Android Gradle plugin or OneAgent SDK.

Do not enable debug logging for your production applications.

Use debug flags explicitly for debugging purposes, not for production. Remove these flags when building your PlayStore or production app because additional logging might slow down your mobile app or write sensitive information into the device logs.

## Activate debug logging mode

You can activate the debug logs via the Dynatrace Android Gradle plugin or OneAgent SDK for Android.

### Dynatrace Android Gradle plugin

Enable debug logging via the [`agentLogging`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.DebugOptions.html#com.dynatrace.tools.android.dsl.DebugOptions:agentLogging) property.

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



debug {



agentLogging true



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



debug {



agentLogging(true)



}



}



}



}
```

### OneAgent SDK

Enable debug logging using the [`ConfigurationBuilder.withDebugLogging(boolean)`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/conf/ConfigurationBuilder.html#withDebugLogging(boolean)) method.

Java

Kotlin

```
Dynatrace.startup(this, new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withDebugLogging(true)



.buildConfiguration());
```

```
Dynatrace.startup(this, DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withDebugLogging(true)



.buildConfiguration())
```

## Retrieve logs from the device

OneAgent for Android uses the default log framework from Android. You can use the [**Logcat** windowï»¿](https://developer.android.com/studio/debug/am-logcat.html) in Android Studio or the [command-line logcat toolï»¿](https://developer.android.com/studio/command-line/logcat.html) to view log messages.

To retrieve the Android logs via the **Logcat** window in Android Studio

1. Connect your device to your computer or run the emulator.

   Note that your device should be [set up for developmentï»¿](https://developer.android.com/studio/run/device.html#setting-up).
2. In Android Studio, select **View** > **Tool Windows** > **Logcat**, and then select your device.
3. Create a filter.

   New Logcat

   Previous Logcat

   Follow the steps below if you've enabled the [new Logcat toolï»¿](https://developer.android.com/studio/releases#logcat) in Android Studio Dolphin or if you're using Android Studio Electric Eel.

   * Enter `tag~:^dtx|^caa` in the filter box.
   * If you've adjusted the formatting option, switch to the default **Standard View** option.

     ![New Logcat window](https://dt-cdn.net/images/logcat-window-1479-0ae2bb9420.png)

     New Logcat window

   Follow the steps below if you're using the previous version of Logcat.

   * Enter the name of a filter, for example, **Dynatrace OneAgent**, in the **Filter Name** box.
   * Enter the `^dtx|^caa` regex in the **Log tag** box.

     ![Previous version of the Logcat window](https://dt-cdn.net/images/oldlogcat-520-f4d55b692e.png)

     Previous version of the Logcat window
4. Launch the instrumented app by using the debug flags.
5. Copy and paste the log lines into a text file.