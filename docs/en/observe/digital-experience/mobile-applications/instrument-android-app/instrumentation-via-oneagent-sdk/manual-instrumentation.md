---
title: Manually instrument your application using OneAgent SDK for Android
source: https://www.dynatrace.com/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation
scraped: 2026-02-17T05:00:32.208456
---

# Manually instrument your application using OneAgent SDK for Android

# Manually instrument your application using OneAgent SDK for Android

* How-to guide
* 2-min read
* Updated on Jan 10, 2024

When you can't use the [Dynatrace Android Gradle plugin](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin "Learn how the Dynatrace Android Gradle plugin can auto-instrument your Android application project.") due to certain technical limitations, opt for standalone manual instrumentation with OneAgent SDK for Android.

Follow the steps below to manually instrument your application using OneAgent SDK for Android.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Ensure that the Maven Central repository is declared.**](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation#step-declare-maven-central "Use OneAgent SDK for Android to manually instrument your Android application.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Include the OneAgent library as a dependency to your project.**](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation#step-include-OneAgent-library "Use OneAgent SDK for Android to manually instrument your Android application.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Start OneAgent manually.**](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation#step-start-one-agent "Use OneAgent SDK for Android to manually instrument your Android application.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Capture additional data via OneAgent SDK for Android.**](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation#step-capture-additional-data "Use OneAgent SDK for Android to manually instrument your Android application.")

When you use standalone manual instrumentation, nothing is done automatically. Ensure that every important part of your application is manually instrumented. Otherwise, OneAgent won't be able to monitor your application and send monitoring data to Dynatrace.

1. Ensure that the Maven Central repository is declared.

   OneAgent for Android is hosted on [Maven Centralï»¿](https://central.sonatype.com/artifact/com.dynatrace.agent/agent-android). In the Gradle settings file, verify that `mavenCentral()` is added to the `repositories` blocks under `dependencyResolutionManagement`. Check the [official Android documentationï»¿](https://dt-url.net/gradle-settings-file) to see what the Gradle settings file should look like.

   Projects with previous Android template: Ensure that the Maven Central repository is declared.

   You might need to add `mavenCentral()` to all `repositories` blocks in the [top-level build fileï»¿](https://dt-url.net/top-level-build-file).
2. Include the OneAgent library as a dependency to your project.

   When you use Gradle as a build automation tool, add the OneAgent library as an `implementation` or `api` dependency in one or more modules. The integration depends on the parts that you want to instrument and the project architecture that you use for your Android project.

   Use version `8.+` so that Gradle can automatically update the OneAgent library when a new minor version is available. When Dynatrace releases a new major version, manually upgrade to the new versionâthe new major version might contain breaking changes, so manual adjustments are usually required.

   **Single-module Android project**

   Add the OneAgent library as an `implementation` dependency in your Android application module.

   Groovy

   Kotlin

   ```
   dependencies {



   implementation 'com.dynatrace.agent:agent-android:8.+'



   }
   ```

   ```
   dependencies {



   implementation("com.dynatrace.agent:agent-android:8.+")



   }
   ```

   **Multi-module Android projects with feature modules**

   Add the OneAgent library as an `api` dependency in your base module (Android application module). If you use internal Android library modules that need to be instrumented, add the OneAgent library as an `implementation` dependency to these internal Android library modules.
3. Start OneAgent manually.

   Use the [`Dynatrace.startup(Application, Configuration)`ï»¿](https://www.dynatrace.com/support/doc/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#startup(android.app.Application,com.dynatrace.android.agent.conf.Configuration)) API method, and start OneAgent manually in the [`Application.onCreate`ï»¿](https://developer.android.com/reference/android/app/Application#onCreate()) method.

   Java

   Kotlin

   ```
   public class YourApplication extends Application {



   @Override



   public void onCreate() {



   super.onCreate();



   // provide the application context as parameter



   Dynatrace.startup(this, new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconUrl>")



   ... // additional configuration



   .buildConfiguration());



   }



   }
   ```

   ```
   class YourApplication : Application() {



   override fun onCreate() {



   super.onCreate()



   // provide the application context as parameter



   Dynatrace.startup(this, DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconUrl>")



   ... // additional configuration



   .buildConfiguration())



   }



   }
   ```

   If you need to start OneAgent at a later stage, use the [`Dynatrace.startup(Activity, Configuration)`ï»¿](https://www.dynatrace.com/support/doc/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#startup(android.app.Activity,com.dynatrace.android.agent.conf.Configuration)) API method. Provide an active `Activity` as a parameter so that OneAgent can immediately monitor it.

   Java

   Kotlin

   ```
   Dynatrace.startup(yourActiveActivity, new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconUrl>")



   ... // additional configuration



   .buildConfiguration());
   ```

   ```
   Dynatrace.startup(yourActiveActivity, DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconUrl>")



   ... // additional configuration



   .buildConfiguration())
   ```

   To get the correct application identification keys (`applicationId` and `beaconUrl`), access the [mobile instrumentation wizard](/docs/observe/digital-experience/mobile-applications/instrument-android-app/get-started-with-android-monitoring#instrumentation-wizard "Learn the steps you need to perform to instrument your Android app for monitoring with Dynatrace.") for your application.

   If your application supports Direct Boot, never call the `Dynatrace.startup` API method from a Direct Boot aware component. Also, check [Adjust communication with OneAgent SDK for Android](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/adjust-oneagent-communication "Configure communication with OneAgent to report the user experience data to Dynatrace.") to make sure that OneAgent can transmit data to Dynatrace.
4. Capture additional data via [OneAgent SDK for Android](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK.").

   For instance, you can create custom actions, report errors, tag specific users, and more.