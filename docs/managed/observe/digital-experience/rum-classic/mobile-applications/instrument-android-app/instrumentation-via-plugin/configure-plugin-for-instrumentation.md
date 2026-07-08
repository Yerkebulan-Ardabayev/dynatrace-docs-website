---
title: Configure Dynatrace Android Gradle plugin for instrumentation processes in RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation
---

# Configure Dynatrace Android Gradle plugin for instrumentation processes in RUM Classic

# Configure Dynatrace Android Gradle plugin for instrumentation processes in RUM Classic

* How-to guide
* 11-min read
* Updated on Mar 26, 2026

The following configuration options allow you to customize the instrumentation process of the Dynatrace Android Gradle plugin.

## Variant-specific configurations

The plugin allows you to specify multiple variant-specific configurations, where each variant-specific configuration can be applied to multiple [Android build variants﻿](https://dt-url.net/android-build-variants). You need to provide a variant-specific configuration for every variant. If the plugin is unable to find a variant-specific configuration for a certain Android build variant, it cancels the build and throws an error. This protection feature can be deactivated with the [`strictMode`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.DynatraceExtension.html#com.dynatrace.tools.android.dsl.DynatraceExtension:strictMode) property.

The association is determined by the regex, that is specified in the [`variantFilter`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.VariantConfiguration.html#com.dynatrace.tools.android.dsl.VariantConfiguration:variantFilter) property, and the variant name of the Android build variant. The regex is case-sensitive and if no product flavor is defined, the build type in the variant name is lower case. If multiple variant-specific configurations match the same variant, the first configuration is selected and applied.

The following sample shows how you can specify a variant-specific configuration in the `dynatrace` block:

Groovy

Kotlin

```
dynatrace {



configurations {



dev {



// build type name is upper case because a product flavor is used



variantFilter "Debug"



// other variant-specific properties



}



demo {



// the first product flavor name is always lower case



variantFilter "demo"



// other variant-specific properties



}



prod {



// build type name is upper case because a product flavor is used



variantFilter "Release"



// other variant-specific properties



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("dev") {



// build type name is upper case because a product flavor is used



variantFilter("Debug")



// other variant-specific properties



}



create("demo") {



// the first product flavor name is always lower case



variantFilter("demo")



// other variant-specific properties



}



create("prod") {



// build type name is upper case because a product flavor is used



variantFilter("Release")



// other variant-specific properties



}



}



}
```

For example, you can have an app that has two product flavors, `demo` and `paid`, and two default build types, `debug` and `release`. The plugin can be used to specify a variant-specific configuration for all debug build variants, `demoDebug` and `paidDebug`, and another two variant-specific configurations for the two variants, `demoRelease` and `paidRelease`.

The association between variant-specific configurations from the plugin and the Android build variants can be printed with the `printVariantAffiliation` task. For example, the following sample shows the console output of the above example:

```
> Task :app:printVariantAffiliation



Variant 'demoDebug' will use configuration 'dev'



Variant 'demoRelease' will use configuration 'demo'



Variant 'paidDebug' will use configuration 'dev'



Variant 'paidRelease' will use configuration 'prod'
```

### Separate development and production monitoring data

If you don't want to pollute your production monitoring data with monitoring data from your `debug` builds, separate the development data from the production monitoring data.

To do this, create two mobile apps in Dynatrace. Generate two variant-specific configurations and use the provided `applicationId` and `beaconUrl` values from the `Instrumentation` page.

Groovy

Kotlin

```
dynatrace {



configurations {



debug {



variantFilter "[dD]ebug"



autoStart {



applicationId '<DebugApplicationID>'



beaconUrl '<ProvidedBeaconURL>'



}



}



prod {



variantFilter "[rR]elease"



autoStart {



applicationId '<ProductionApplicationID>'



beaconUrl '<ProvidedBeaconURL>'



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("debug") {



variantFilter("[dD]ebug")



autoStart {



applicationId("<DebugApplicationID>")



beaconUrl("<ProvidedBeaconURL>")



}



}



create("prod") {



variantFilter("[rR]elease")



autoStart {



applicationId("<ProductionApplicationID>")



beaconUrl("<ProvidedBeaconURL>")



}



}



}



}
```

If you prefer to not monitor your `debug` builds, disable the variant-specific configuration that is responsible for your `debug` builds.

Groovy

Kotlin

```
dynatrace {



configurations {



debug {



variantFilter "[dD]ebug"



enabled false



}



prod {



variantFilter "[rR]elease"



autoStart {



applicationId '<ProductionApplicationID>'



beaconUrl '<ProvidedBeaconURL>'



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("debug") {



variantFilter("[dD]ebug")



enabled(false)



}



create("prod") {



variantFilter("[rR]elease")



autoStart {



applicationId("<ProductionApplicationID>")



beaconUrl("<ProvidedBeaconURL>")



}



}



}



}
```

## Deactivate auto-instrumentation

You can deactivate auto-instrumentation for all variants or for a specific variant.

### Deactivate all variants

To deactivate auto-instrumentation for all variants, deactivate the plugin with the [`pluginEnabled`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.DynatraceExtension.html#com.dynatrace.tools.android.dsl.DynatraceExtension:pluginEnabled) property. The plugin still adds OneAgent SDK as Gradle dependency to ensure that the compiler can compile the manually instrumented source files.

With this setting, the verification step of the plugin is deactivated. Also, the auto-start feature is deactivated and the app stops being monitored. If you start the agent manually, the app is monitored, but OneAgent can capture only mobile user experience data that is instrumented by manual calls to the OneAgent SDK.

You can deactivate auto-instrumentation for all variants or for a specific variant.

Groovy

Kotlin

```
dynatrace {



pluginEnabled false



configurations {



dev {



// variant-specific properties



}



prod {



// variant-specific properties



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



pluginEnabled(false)



configurations {



create("dev") {



// variant-specific properties



}



create("prod") {



// variant-specific properties



}



}



}
```

### Deactivate one variant

If you want to deactivate auto-instrumentation for a specific variant, explicitly deactivate the variant-specific configuration via the [`enabled`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.VariantConfiguration.html#com.dynatrace.tools.android.dsl.VariantConfiguration:enabled) property. The following example shows how you can deactivate all `debug` build types (variant `demoDebug` and `paidDebug`):

Groovy

Kotlin

```
dynatrace {



configurations {



dev {



enabled false



variantFilter "Debug"



}



prod {



// variant-specific properties



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("dev") {



enabled(false)



variantFilter("Debug")



}



create("prod") {



// variant-specific properties



}



}



}
```

Skip auto-instrumentation when no variant-specific configuration is available

You can deactivate the `strictMode` property and only define a variant-specific configuration for the variant you want to instrument. The plugin doesn’t instrument Android build variants when no variant-specific configuration matches the given Android build variant.

If you don't deactivate the `strictMode` property, the plugin cancels the build and throws an error.
We don't recommend this approach, because the strict mode feature should protect you from building variants with no variant-specific configuration. Deactivate auto-instrumentation via the `enabled` property of your variant-specific configuration.

Groovy

Kotlin

```
dynatrace {



strictMode false



configurations {



prod {



variantFilter "Release"



// other variant-specific properties



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



strictMode(false)



configurations {



create("prod") {



variantFilter("Release")



// other variant-specific properties



}



}



}
```

## Automatic OneAgent startup

To obtain the correct startup parameters, go to **Instrumentation wizard** in Dynatrace.

1. Go to **Mobile**.
2. Select the mobile application that you want to configure.
3. Select **More** (**…**) > **Edit** in the upper-right corner of the tile with your application name.
4. From the application settings, select **Instrumentation wizard**.
5. Select **Android**, and then go to either the **Groovy (build.gradle)** or the **Kotlin (build.gradle.kts)** tab.
6. Use the preconfigured snippet (see the step called **Apply the Dynatrace plugin and add the plugin configuration**) that is already populated with the configuration values from your mobile app.

All OneAgent start-up related properties are part of the [AutoStart DSL﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.StartOptions.html) and must be configured via the [`autoStart` block﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.VariantConfiguration.html#com.dynatrace.tools.android.dsl.VariantConfiguration:autoStart(org.gradle.api.Action)):

Groovy

Kotlin

```
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

The automatic OneAgent startup feature starts OneAgent in the `Application.onCreate` method. If your app supports Direct Boot, you have to deactivate the automatic OneAgent startup feature. You should also read [Adjust communication with OneAgent SDK for Android in RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/adjust-oneagent-communication "Configure communication with OneAgent to report the user experience data to Dynatrace.") to ensure that OneAgent is able to transmit the data to the cluster.

### Deactivate automatic OneAgent startup

You can disable the automatic OneAgent startup with the [`enabled`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.StartOptions.html#com.dynatrace.tools.android.dsl.StartOptions:enabled) property. You cannot specify the `applicationId` and the `beaconUrl` properties because these values must be used in the manual startup call.

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



autoStart.enabled false



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



autoStart.enabled(false)



}



}



}
```

It is recommended to add the startup call to the `Application.onCreate` method. For more information, see [OneAgent SDK for Android > Start OneAgent](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#start-oneagent "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK.").

`autoStart.enabled` starts OneAgent automatically once per application. OneAgent cannot be started again in the same application to point to a different `appId` and `beaconUrl`, multiple concurrent initializations are unsupported.

Additional configuration changes specified via `DynatraceConfigurationBuilder` override the configuration values defined via the Dynatrace Android Gradle plugin DSL.

## Exclude certain classes and methods

By default, the Dynatrace Android Gradle plugin instruments all packages. If you want to exclude certain classes, you have two options:

* Exclude a list of packages, classes, and methods
* Use a custom exclude filter

### Exclude a list of packages, classes, and methods via the `packages`, `classes`, and `methods` properties

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



exclude {



packages "com.mypackage", "com.another.example"



classes "com.example.MyClass"



methods "com.example.ExampleClass.exampleMethod", "com.example.ExampleClass\$InnerClass.anotherMethod"



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



exclude {



packages("com.mypackage", "com.another.example")



classes("com.example.MyClass")



methods("com.example.ExampleClass.exampleMethod", "com.example.ExampleClass\$InnerClass.anotherMethod")



}



}



}



}
```

These properties contain some additional features:

* `packages` automatically excludes sub-packages
* `classes` automatically excludes inner classes
* `methods` automatically excludes all methods with the same name (regardless of the method signature)

Escape the `$` character for inner classes as shown in the above example.

### Use the custom exclude filter

This option allows you to define a finer granular exclusion logic via additional filter rules. In the filter you can define a [regex﻿](https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html) for `className`, `methodName`, and `methodDescription`.

* For the `className` property, the fully qualified name is used.
* A class name matches when the specified expression is found somewhere in the class name
* A method name matches when the specified expression is found somewhere in the method name
* A [method description﻿](https://docs.oracle.com/javase/specs/jvms/se8/html/jvms-4.html#jvms-4.3.3) matches when the specified expression is found somewhere in the method description

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



exclude {



// exclude all inner classes



filter {



className "\$"



}



// exclude all methods that fulfill this requirements



filter {



// the class is part of the "com.example" package



className "^com\\.example\\."



// the method name contain the phrase "webrequest" (uppercase notation is ignored for two letters)



methodName "[wW]eb[rR]equest"



// where the last parameter is a String and where the return value is void



methodDescription "Ljava/lang/String;\\)V"



}



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



exclude {



// exclude all inner classes



filter {



className("\$")



}



// exclude all methods that fulfill this requirements



filter {



// the class is part of the "com.example" package



className("^com\\.example\\.")



// the method name contain the phrase "webrequest" (uppercase notation is ignored for two letters)



methodName("[wW]eb[rR]equest")



// where the last parameter is a String and where the return value is void



methodDescription("Ljava/lang/String;\\)V")



}



}



}



}



}
```

## Adjust test case instrumentation

The plugin only executes the auto-instrumentation step when the app is built. Therefore, the behavior of [local unit tests﻿](https://developer.android.com/training/testing/unit-testing/local-unit-tests) and [instrumented unit tests﻿](https://developer.android.com/training/testing/unit-testing/instrumented-unit-tests) is different.

### Local unit tests

Local unit tests use instrumented classes from your source folder, but uninstrumented libraries. There should be no impact on the unit tests, as the plugin mostly instruments Android-specific classes and method calls are ignored when OneAgent is not started. This is also valid for method calls to OneAgent SDK.

### Local unit tests with Robolectric

[Robolectric﻿](https://robolectric.org/) allows you to simulate Android in your local unit tests. Robolectric uses instrumented classes from your source folder, but uninstrumented libraries.

If you have [disabled the automatic OneAgent startup](#disable-auto-startup) and started OneAgent manually in the `Application` class, OneAgent runs and monitors your Robolectric test cases. In this case, adjust your configuration by either [separating development and production monitoring data](#separate-development-and-prod-data) or [using a different build type for unit tests](#use-diff-build-type-unit-tests).

### Instrumented unit tests

To run instrumented unit tests on a device or emulator, the Android build generates two APK files:

* The APK file of the app you want to test. The plugin is part of this build process and auto-instruments the APK file.
* A test APK file that contains the class for testing the other APK. The plugin is also part of this build process, but it doesn't auto-instrument these test APKs.

Because the APK is instrumented, every instrumented unit test is monitored. In this case, you should adjust your configuration by either [separating development and production monitoring data](#separate-development-and-prod-data) or [using a different build type for unit tests](#use-diff-build-type-unit-tests).

### Use a different build type for unit tests

For a customized instrumentation behavior for your unit tests, generate a new build type for your unit tests with the plugin.

Groovy

Kotlin

```
android {



buildTypes {



// build type used for unit tests in the CI



CI {



initWith debug



applicationIdSuffix ".debugTesting"



}



}



}
```

```
android {



buildTypes {



// build type used for unit tests in the CI



create("CI") {



initWith(getByName("debug"))



applicationIdSuffix = ".debugTesting"



}



}



}
```

For example, if you want to monitor your `debug` builds used by the developers and you don't want to monitor the unit test execution in the CI, use the following configuration:

Groovy

Kotlin

```
dynatrace {



configurations {



developer {



variantFilter "[dD]ebug"



autoStart {



applicationId '<DebugApplicationID>'



beaconUrl '<ProvidedBeaconURL>'



}



}



ciTesting {



// deactivate instrumentation for CI tests



variantFilter "CI"



enabled false



}



prod {



variantFilter "[rR]elease"



autoStart {



applicationId '<ProductionApplicationID>'



beaconUrl '<ProvidedBeaconURL>'



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("developer") {



variantFilter("[dD]ebug")



autoStart {



applicationId("<ProductionApplicationID>")



beaconUrl("<ProvidedBeaconURL>")



}



}



create("ciTesting") {



// deactivate instrumentation for CI tests



variantFilter("CI")



enabled(false)



}



create("prod") {



variantFilter("[rR]elease")



autoStart {



applicationId("<DebugApplicationID>")



beaconUrl("<ProvidedBeaconURL>")



}



}



}



}
```

When you execute the unit tests with the `debug` variant, unit tests are monitored because the instrumentation is deactivated only for the `CI` variant.