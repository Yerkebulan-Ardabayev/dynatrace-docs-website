---
title: Adjust OneAgent configuration via Dynatrace Android Gradle plugin
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/adjust-oneagent-configuration
scraped: 2026-05-12T11:33:17.022098
---

# Adjust OneAgent configuration via Dynatrace Android Gradle plugin

# Adjust OneAgent configuration via Dynatrace Android Gradle plugin

* How-to guide
* 3-min read
* Updated on Mar 05, 2026

The following configuration options can be used to modify the default configuration of the OneAgent. They are especially useful when used along with the automatic OneAgent startup feature.

They can also be used to adjust the OneAgent configuration when the manual startup approach is approached. In this case, you have to be careful because these settings might get overridden with the `ConfigurationBuilder`.

## Change data privacy settings (opt-in mode)

With user opt-in mode, each user of your application can set their data privacy preferences and decide whether they want or don't want to share their information. When the opt-in mode is enabled, you need to ask each user for permission to capture their data; then, you store their data privacy preferences. For details, see [User opt-in mode](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

To activate the user opt-in mode (when you use the [automatic OneAgent startup](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#auto-startup "Learn how to configure the Dynatrace Android Gradle plugin to adjust the auto-instrumentation process.")), enable the [`userOptIn`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.VariantConfiguration.html#com.dynatrace.tools.android.dsl.VariantConfiguration:userOptIn) property.

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



userOptIn true



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



userOptIn(true)



}



}



}
```

Use the OneAgent SDK to [change user's data privacy preferences](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#data-privacy "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK.").

## Configure hybrid applications

For hybrid applications, the native mobile app is monitored via OneAgent, while the browser part is observed by the [Dynatrace RUM JavaScript](/managed/observe/digital-experience/web-applications/additional-configuration/customize-rum "Find out how to customize Real User Monitoring using the JavaScript API."). For this reason, hybrid application monitoring requires some additional configuration. See [Instrument hybrid apps](/managed/observe/digital-experience/mobile-applications/instrument-hybrid-app "Learn how you can instrument various types of hybrid and cross-platform mobile apps.") for more information.

All properties related to hybrid application monitoring are part of [HybridWebView DSLï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.HybridOptions.html), so configure them via the [`hybridWebView` blockï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.VariantConfiguration.html#com.dynatrace.tools.android.dsl.VariantConfiguration:hybridWebView(org.gradle.api.Action)).

### Enable hybrid application monitoring

You can activate the hybrid application monitoring feature with the [`enabled`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.HybridOptions.html#com.dynatrace.tools.android.dsl.HybridOptions:enabled) property.

### Specify domains, hostnames, and IP addresses

For hybrid applications that use the RUM JavaScript inside `WebView`, OneAgent must set cookies for each instrumented domain or server your application communicates with. When the hybrid application monitoring feature is enabled, OneAgent generates these cookies for every specified domain and stores them in the `CookieManager`. Dynatrace uses these cookies to identify mobile and web sessions within your application and merge these sessions into the same "hybrid" session.

To specify your domains, hostnames, and IP addresses, use either the [`domains`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.HybridOptions.html#com.dynatrace.tools.android.dsl.HybridOptions:domains) or the [`httpsDomains`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.HybridOptions.html#com.dynatrace.tools.android.dsl.HybridOptions:httpsDomains) property. Domains and subdomains must start with a period (`.`).

#### `domains` property

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



hybridWebView {



enabled true



domains '.<domain1>', '.<domain2>'



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



hybridWebView {



enabled(true)



domains(".<domain1>", ".<domain2>")



}



}



}



}
```

#### `httpsDomains` property

If you use the `httpsDomains` property, the `Secure` cookie attribute is added for all cookies that Dynatrace sets. This ensures that the browser sends these cookies only over secure connections.

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



hybridWebView {



enabled true



httpsDomains 'https://.<domain1>', 'https://.<domain2>'



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



hybridWebView {



enabled(true)



httpsDomains("https://.<domain1>", "https://.<domain2>")



}



}



}



}
```

### Disable cookies for file domains

Dynatrace Android Gradle plugin version 8.271+

To set cookies for file domains (starting with `file://`), Dynatrace uses [`setAcceptFileSchemeCookies`ï»¿](https://developer.android.com/reference/android/webkit/CookieManager#setAcceptFileSchemeCookies(boolean)). However, this API is no longer recommended because of security issues; we plan to stop adding cookies to file scheme domains in a couple of months.

If you want to secure your application right now, set `fileDomainCookies` to `false`, and Dynatrace won't add cookies to file scheme domains.

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



hybridWebView {



enabled true



fileDomainCookies false



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



hybridWebView {



enabled(true)



fileDomainCookies(false)



}



}



}



}
```

## Enable load balancing

OneAgent allows you to enable client-side load balancing that helps avoid unbalanced load on the server when multiple OneAgents simultaneously establish a connection to the ActiveGate.

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



agentBehavior {



startupLoadBalancing true



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



agentBehavior {



startupLoadBalancing(true)



}



}



}



}
```

## Enable the New RUM Experience on first app start

OneAgent allows you to enable the New RUM Experience on the first app start, before the cluster configuration is received. This setting has no effect after the first app start. Once cluster configuration is received, it permanently overrides this flag. This feature is disabled by default.

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



agentBehavior {



startupWithGrailEnabled true



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



agentBehavior {



startupWithGrailEnabled(true)



}



}



}



}
```