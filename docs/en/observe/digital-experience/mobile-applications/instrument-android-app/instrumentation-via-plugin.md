---
title: Dynatrace Android Gradle plugin
source: https://www.dynatrace.com/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin
scraped: 2026-02-15T09:01:16.340469
---

# Dynatrace Android Gradle plugin

# Dynatrace Android Gradle plugin

* Overview
* 6-min read
* Updated on Jan 21, 2026

You can use the Dynatrace Android Gradle plugin only for Android projects that use the [Android Gradle pluginï»¿](https://developer.android.com/studio/build/index.html) to build the app. You should apply the Dynatrace Android Gradle to the [top-level build fileï»¿](https://dt-url.net/top-level-build-file) (either `build.gradle` or `build.gradle.kts`), which is located in the root project directory. This approach allows the plugin to properly configure the Android subprojects and establish the auto-instrumentation process as part of the Android build process.

The Dynatrace Android Gradle plugin is hosted on [Maven Centralï»¿](https://central.sonatype.com/artifact/com.dynatrace.tools.android/gradle-plugin/overview), and the technical documentation is available as [DSL referenceï»¿](https://www.dynatrace.com/support/doc/javadoc/oneagent/android/gradle-plugin/dsl/).

In a couple of months, we'll stop setting cookies to file scheme domains for hybrid applications. See [Disable cookies for file domains](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/adjust-oneagent-configuration#file-domain-cookies "Learn how to configure the Dynatrace Android Gradle plugin to modify the OneAgent SDK configuration.") for more details and action items.

[Jetpack Compose auto-instrumentation](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#compose-instrumentation "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.") is enabled by default starting with Dynatrace Android Gradle plugin version 8.271.

## Requirements

* Gradle version 7.0.2+
* Android Gradle plugin version 7.0+
* JVM: Java 11+

## Instrumentation

The Dynatrace Android Gradle plugin uses bytecode instrumentation to instrument your app. It can instrument the source files of all subprojects and third-party libraries. Performance-wise, bytecode instrumentation is quick and has a low impact on the build time. By providing support for incremental builds and the build cache, the instrumentation of apps will be almost unnoticed.

### Instrumentation-specific capabilities

* Java and Kotlin: The Dynatrace Android Gradle plugin supports the instrumentation of Java and Kotlin classes. It also supports other JVM languages.
* Obfuscations and optimization: The auto-instrumentation process is completed before the [R8ï»¿](https://android-developers.googleblog.com/2018/11/r8-new-code-shrinker-from-google-is.html) Gradle task. If you use another tool for obfuscation, you must ensure that the obfuscation task is executed after the auto-instrumentation process.

  OneAgent for Android and its transitive dependencies provide ProGuard rules that are designed for R8. If you use third-party obfuscation tools, you are responsible for ensuring that these tools are configured to honor the required keep rules. Failure to do so may result in runtime errors due to incorrectly obfuscated classes.

  If you use Android Gradle Plugin features such as [`ignoreFrom`ï»¿](https://android-developers.googleblog.com/2025/11/configure-and-troubleshoot-r8-keep-rules.html) to filter out keep rules from dependencies, be aware that this may affect OneAgent functionality.
* Security and APK-hardening tools: Bytecode instrumentation happens before obfuscation and before [Android Dexer (D8)ï»¿](https://developer.android.com/studio/command-line/d8) transforms the `.class` bytecode into `.dex` bytecode that can be executed in the Android Runtime. Therefore, the plugin can ensure maximum compatibility with other security-focused and APK-hardening tools that calculate checksums for the DEX code, such as DexGuard and Arxan.

### Instrumentation-specific limitations

The Android Gradle plugin only instruments the `AndroidManifest.xml` and other `.class` files. It doesnât instrument the following components:

* Native code, such as code written with the [NDKï»¿](https://developer.android.com/ndk)
* Web components, such as `.html` and `.js` files
* Resource files, such as layout `.xml` files

### Compatibility with other monitoring tools

There might be compatibility issues with other performance monitoring plugins, especially when these plugins instrument OneAgent for Android. We recommend either using only one performance monitoring plugin or verifying via manual testing that the plugins you've chosen are compatible.

## Build

### Build-specific capabilities

The Dynatrace Android Gradle plugin supports Gradle build-specific capabilities, including the following:

* Faster incremental builds by modifying only classes and libraries, thereby reducing instrumentation time.
* [Build cacheï»¿](https://docs.gradle.org/current/userguide/build_cache.html) to reduce build time by reusing outputs produced by other builds.
* Dynatrace Android Gradle plugin version 8.257+ [Configuration cacheï»¿](https://docs.gradle.org/current/userguide/configuration_cache.html) to reduce build time by reusing the cached result of the configuration phase.
* [Apply Changesï»¿](https://developer.android.com/studio/run#apply-changes) for pushing code and resource changes to a running app without having to restart it. The app must be restarted only when the configuration of the plugin or OneAgent is changed.
* Build processes for [Android App Bundlesï»¿](https://developer.android.com/guide/app-bundle) and APKs.
* [Multiple APK buildsï»¿](https://developer.android.com/studio/build/configure-apk-splits#build-apks) via the `splits` block so that the instrumentation step is executed only once.
* Support for [Kotlin DSLï»¿](https://docs.gradle.org/current/userguide/kotlin_dsl.html) in `build.gradle.kts` files.

### Build-specific limitations

* **Android library projects**: The Dynatrace Android Gradle plugin auto-instruments only Android application projects. It doesn't support the auto-instrumentation of stand-alone Android library projects. Our plugin auto-instruments the internal libraries if you add them as a dependency to your Android application project.
* **Android Gradle plugin `excludes` property**: With the [`excludes`ï»¿](https://developer.android.com/reference/tools/gradle-api/7.4/com/android/build/api/variant/Instrumentation#excludes()) property of the Android Gradle plugin, you can disable instrumentation for specific classes. This property is similar to the [`exclude`](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#exclude-classes-and-methods "Learn how to configure the Dynatrace Android Gradle plugin to adjust the auto-instrumentation process.") property of the Dynatrace Android Gradle plugin. However, when you use the Dynatrace property, our plugin still instruments some very important classes to ensure that instrumentation is always valid. With the Android `excludes` property, all the specified classes aren't instrumented, which might negatively affect the instrumentation.

## Configuration

The Android Gradle plugin provides a wide range of configuration options to customize your Android application build and the monitored mobile user experience data.

The Gradle snippet from the **Instrumentation** page and the Gradle snippets from the documentation contain sample names for variant-specific configuration, such as `sampleConfig`. To understand this better, see how [variant-specific configurations](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#variant-specific-configs "Learn how to configure the Dynatrace Android Gradle plugin to adjust the auto-instrumentation process.") are used.

### Configure monitoring capabilities

The following options can be used to customize OneAgent SDK for Android monitoring capabilities and fine-tune the auto-instrumentation process.

* [User action monitoring](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#user-action-monitoring "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.")
* [User action monitoring for Jetpack Compose](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#compose-instrumentation "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.")
* [Web request monitoring](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#web-request-monitoring "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.")
* [Lifecycle monitoring](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#lifecycle-monitoring "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.")
* [Crash reporting](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#crash-reporting "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.")
* [Rage tap detection](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#rage-tap-detection "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.")
* [Location monitoring](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#location-monitoring "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.")

### Configure instrumentation processes

The plugin also provides additional configuration options to customize the instrumentation process:

* [Variant-specific configurations](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#variant-specific-configs "Learn how to configure the Dynatrace Android Gradle plugin to adjust the auto-instrumentation process.")
* [Auto-instrumentation deactivation](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#deactivate-auto-instrumentation "Learn how to configure the Dynatrace Android Gradle plugin to adjust the auto-instrumentation process.")
* [Automatic OneAgent startup](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#auto-startup "Learn how to configure the Dynatrace Android Gradle plugin to adjust the auto-instrumentation process.")
* [Exclusion of certain classes and methods](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#exclude-certain-classes-and-methods "Learn how to configure the Dynatrace Android Gradle plugin to adjust the auto-instrumentation process.")
* [Adjusting test case instrumentation](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#adjust-test-case-instrumentation "Learn how to configure the Dynatrace Android Gradle plugin to adjust the auto-instrumentation process.")

### Adjust OneAgent configuration

The following configuration options can be used to adjust the default OneAgent configuration:

* [Data privacy](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/adjust-oneagent-configuration#data-privacy "Learn how to configure the Dynatrace Android Gradle plugin to modify the OneAgent SDK configuration.")
* [Hybrid apps that use RUM JavaScript inside `WebView`](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/adjust-oneagent-configuration#hybrid-apps "Learn how to configure the Dynatrace Android Gradle plugin to modify the OneAgent SDK configuration.")
* [Adjust OneAgent behavior](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/adjust-oneagent-configuration#adjust-oneagent-behavior "Learn how to configure the Dynatrace Android Gradle plugin to modify the OneAgent SDK configuration.")

These options are especially helpful when used along with the automatic OneAgent startup. They can also be used to adjust the OneAgent configuration when approached with the manual startup, but you need to be careful because the settings can easily be overridden with `ConfigurationBuilder`.

### Adjust Dynatrace Android Gradle plugin configuration based on the project structure

Our plugin scans all subprojects and configures the auto-instrumentation process for your application modules. Other modules are unaffected by the plugin. In this case, you might need to adjust the instrumentation process for an Android project with:

* [Library modules](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-multi-module-projects#library-modules "Use the Dynatrace Android Gradle plugin for less common project architectures.")
* [Feature modules](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-multi-module-projects#feature-modules "Use the Dynatrace Android Gradle plugin for less common project architectures.")
* [Multiple application modules](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-multi-module-projects#multiple-application-modules "Use the Dynatrace Android Gradle plugin for less common project architectures.")
* [Multiple application modules and feature modules](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-multi-module-projects#application-and-feature-modules "Use the Dynatrace Android Gradle plugin for less common project architectures.")
* [One build file](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-multi-module-projects#one-build-file "Use the Dynatrace Android Gradle plugin for less common project architectures.")