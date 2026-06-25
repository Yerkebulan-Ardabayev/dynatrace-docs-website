---
title: Instrument your application via Dynatrace Android Gradle plugin
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/instrumentation-via-plugin
scraped: 2026-05-12T11:33:01.629670
---

# Instrument your application via Dynatrace Android Gradle plugin

# Instrument your application via Dynatrace Android Gradle plugin

* How-to guide
* 1-min read
* Updated on Sep 06, 2023

If your project has library modules, feature modules, multiple application modules, or just one build file, first check the corresponding section in [Change Dynatrace Android Gradle plugin configuration based on the project structure](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-multi-module-projects "Use the Dynatrace Android Gradle plugin for less common project architectures."). The steps required to set up the Dynatrace Android Gradle plugin might be slightly different for applications with such architectures.

Follow the steps below to instrument your Android app with the Dynatrace Android Gradle plugin.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Ensure that the Maven Central repository is declared.**](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/instrumentation-via-plugin#step-declare-maven-central "Perform the steps in this topic before you begin instrumenting your app with the Dynatrace Android Gradle plugin.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Add our plugin to the build script classpath.**](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/instrumentation-via-plugin#step-add-plugin "Perform the steps in this topic before you begin instrumenting your app with the Dynatrace Android Gradle plugin.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Apply our plugin and add its configuration snippet.**](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/instrumentation-via-plugin#step-apply-plugin-and-add-config-snippet "Perform the steps in this topic before you begin instrumenting your app with the Dynatrace Android Gradle plugin.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Customize the plugin configuration.**](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/instrumentation-via-plugin#step-customize-plugin-config "Perform the steps in this topic before you begin instrumenting your app with the Dynatrace Android Gradle plugin.")[![Step 5 optional](https://dt-cdn.net/images/dotted-step-5-52040ae237.svg "Step 5 optional")

**Enhance mobile user experience data by using the OneAgent SDK for Android.**](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/instrumentation-via-plugin#step-use-oneagent-sdk "Perform the steps in this topic before you begin instrumenting your app with the Dynatrace Android Gradle plugin.")

1. Ensure that the Maven Central repository is declared.

   Dynatrace is hosted on Maven Central. In the Gradle settings file, verify that `mavenCentral()` is added to the `repositories` blocks under `pluginManagement` and `dependencyResolutionManagement`. Check the [official Android documentationï»¿](https://dt-url.net/gradle-settings-file) to see what the Gradle settings file should look like.

   Projects with previous Android template: Ensure that the Maven Central repository is declared.

   You might need to add `mavenCentral()` to all `repositories` blocks in the [top-level build fileï»¿](https://dt-url.net/top-level-build-file).

2. Add our plugin to the build script classpath.

   In the [top-level build fileï»¿](https://dt-url.net/top-level-build-file), add the `buildscript` block with the `dependencies` block inside and add the classpath of the Dynatrace Android Gradle plugin (`com.dynatrace.tools.android:gradle-plugin`).

   Groovy

   Kotlin

   ```
   // add this entire block



   buildscript {



   dependencies {



   classpath 'com.dynatrace.tools.android:gradle-plugin:8.+'



   }



   }



   // this block already exists



   plugins {



   id 'com.android.application' version '8.1.0' apply false



   id 'com.android.library' version '8.1.0' apply false



   }
   ```

   ```
   // add this entire block



   buildscript {



   dependencies {



   classpath("com.dynatrace.tools.android:gradle-plugin:8.+")



   }



   }



   // this block already exists



   plugins {



   id("com.android.application") version "8.1.0" apply false



   id("com.android.library") version "8.1.0" apply false



   }
   ```

   Projects with previous Android template: Add our plugin to the build script classpath.

   In the top-level build file, find the `dependencies` block inside the `buildscript` block, and add the classpath of the Dynatrace Android Gradle plugin (`com.dynatrace.tools.android:gradle-plugin`) after the build script classpath of the [Android Gradle pluginï»¿](https://developer.android.com/studio/build/index.html) (`com.android.tools.build:gradle`).

   Groovy

   Kotlin

   ```
   buildscript {



   repositories {



   google()



   mavenCentral() // hosts Dynatrace Android Gradle plugin



   }



   dependencies {



   // build script classpath of Android Gradle plugin



   classpath 'com.android.tools.build:gradle:<version>'



   // build script classpath of Dynatrace Android Gradle plugin; add this line to build.gradle file



   classpath 'com.dynatrace.tools.android:gradle-plugin:8.+'



   }



   }
   ```

   ```
   buildscript {



   repositories {



   google()



   mavenCentral() // hosts Dynatrace Android Gradle plugin



   }



   dependencies {



   // build script classpath of Android Gradle plugin



   classpath("com.android.tools.build:gradle:<version>")



   // build script classpath of Dynatrace Android Gradle plugin; add this line to build.gradle.kts file



   classpath("com.dynatrace.tools.android:gradle-plugin:8.+")



   }



   }
   ```

   Projects with Gradle Plugin DSL: Add our plugin to the Gradle Plugin DSL block.

   In the top-level build file, find the [pluginsï»¿](https://docs.gradle.org/current/userguide/plugins.html#sec:plugins_block) block, and add the id `com.dynatrace.instrumentation` of the Dynatrace [Plugin Marker Artifactsï»¿](https://docs.gradle.org/current/userguide/plugins.html#sec:plugin_markers). After `plugins` block add plugin configuration of the [Android instrumentation wizard](/managed/observe/digital-experience/mobile-applications/instrument-android-app/get-started-with-android-monitoring#instrumentation-wizard "Learn the steps you need to perform to instrument your Android app for monitoring with Dynatrace.") to have the correct `applicationId` and `beaconUrl` values.

   Groovy

   Kotlin

   ```
   plugins {



   id 'com.android.application' version '8.5.0' apply false



   id 'com.dynatrace.instrumentation' version '8.+' apply true



   }



   dynatrace {



   configurations {



   sampleConfig {



   autoStart {



   applicationId = '<YourApplicationID>'



   beaconUrl = '<ProvidedBeaconURL>'



   }



   }



   }



   }
   ```

   ```
   plugins {



   id("com.android.application") version "8.5.0" apply false



   id("com.dynatrace.instrumentation") version "8.+" apply true



   }



   dynatrace {



   configurations {



   create("sampleConfig") {



   autoStart {



   applicationId("<YourApplicationID>")



   beaconUrl("<ProvidedBeaconURL>")



   }



   }



   }



   }
   ```

   Skip step 3. The `apply` statement is not needed, when you are using the Gradle Plugin DSL.

   Use version `8.+` so that Gradle can automatically update our plugin when a new minor version is available. When Dynatrace releases a new major version, manually upgrade to the new versionâthe new major version might contain breaking changes, so manual adjustments are usually required.

3. Apply our plugin and add its configuration snippet.

   Apply the Dynatrace Android Gradle plugin with the `com.dynatrace.instrumentation` plugin ID in the top-level build file.

   Then, add the code snippet from step 3 (**Apply the Dynatrace plugin and add the plugin configuration**) of the [Android instrumentation wizard](/managed/observe/digital-experience/mobile-applications/instrument-android-app/get-started-with-android-monitoring#instrumentation-wizard "Learn the steps you need to perform to instrument your Android app for monitoring with Dynatrace.") to have the correct `applicationId` and `beaconUrl` values.

   Groovy

   Kotlin

   ```
   apply plugin: 'com.dynatrace.instrumentation'



   dynatrace {



   configurations {



   sampleConfig {



   autoStart {



   applicationId '<YourApplicationID>'



   beaconUrl '<ProvidedBeaconURL>'



   }



   }



   }



   }
   ```

   ```
   apply(plugin = "com.dynatrace.instrumentation")



   configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



   configurations {



   create("sampleConfig") {



   autoStart {



   applicationId("<YourApplicationID>")



   beaconUrl("<ProvidedBeaconURL>")



   }



   }



   }



   }
   ```

   You can change the `sampleConfig` configuration name to something more meaningful. You can also define different configurations for different [Android build variantsï»¿](https://dt-url.net/android-build-variants). For example, you can report your `debug` and `release` variants to different mobile applications in Dynatrace by using [variant-specific configurations](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#variant-specific-configs "Learn how to configure the Dynatrace Android Gradle plugin to adjust the auto-instrumentation process.").

4. Customize the plugin configuration.

   The Gradle snippet that you've copied from the Android instrumentation wizard contains the default plugin configuration. The same configuration is used for all Android build variants, and our plugin uses the default sensors and default OneAgent configuration values. For this reason, you might want to [adjust the configuration](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin#configuration "Learn how the Dynatrace Android Gradle plugin can auto-instrument your Android application project.") of the Dynatrace Android Gradle plugin.

5. Optional Enhance mobile user experience data by using the OneAgent SDK for Android.

   With [OneAgent SDK for Android](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK."), you can enrich the mobile user experience data. For example, user tagging or custom value reporting is only available via the OneAgent SDK.