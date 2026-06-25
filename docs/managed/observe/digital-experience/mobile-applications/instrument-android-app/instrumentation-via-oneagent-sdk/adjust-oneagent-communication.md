---
title: Adjust communication with OneAgent SDK for Android
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/adjust-oneagent-communication
scraped: 2026-05-12T11:33:19.081187
---

# Adjust communication with OneAgent SDK for Android

# Adjust communication with OneAgent SDK for Android

* How-to guide
* 5-min read
* Updated on Mar 05, 2026

After instrumentation is complete, check the following aspects regarding communication with OneAgent.

## Network security configuration

If your Android app has [network security configuredï»¿](https://developer.android.com/training/articles/security-config), ensure that the HTTP traffic to the `beaconUrl` endpoint is not blocked by the network security configuration.

## Firewall

Ensure that the GET and POST requests to the `beaconUrl` endpoint are not blocked by a firewall.

## Include certificates

For HTTPS communication, OneAgent verifies the server certificate and the hostname. OneAgent communication fails if the verification steps aren't completed.

If your Cluster ActiveGate doesn't have a certificate issued by a trusted intermediate or root Certificate Authority (CA), provide the server certificate for SSL communication in the [Network Security Configuration fileï»¿](https://developer.android.com/training/articles/security-config.html) (for Android API level 24+).

To use the Network Security Configuration feature, add a `domain-config` section to your `network_security_config.xml` file.

```
<domain-config>



<domain includeSubdomains="true">your.domain.com</domain>



<trust-anchors>



<certificates src="@raw/your_server_certificate" />



</trust-anchors>



</domain-config>
```

Include certificates for apps with Android API level 23 and earlier

Deprecated

If you need to provide a server certificate for apps with Android API level 23 and earlier, include the certificate in a `KeyStore` object and provide this object to OneAgent by [performing a manual startup via the `DynatraceConfigurationBuilder` API](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#start-oneagent "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK."). The `KeyStore` object must hold the certificate chain of the Cluster ActiveGate to which you want to connect.

This option was deprecated with OneAgent SDK for Android version 8.257. From this version, only use the `KeyStore` configuration for older Android versions.

If you use both the Network Security Configuration feature and the `KeyStore` configuration, the latter takes precedence.

Java

Kotlin

```
KeyStore trusted = KeyStore.getInstance("BKS");



try (InputStream in = getResources().openRawResource(R.raw.mykeystore)) {



trusted.load(in, "myverysecretpassword".toCharArray());



}



Dynatrace.startup(this, new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withKeyStore(trusted)



.buildConfiguration());
```

```
val trusted = KeyStore.getInstance("BKS")



resources.openRawResource(R.raw.mykeystore).use { inputStream ->



trusted.load(inputStream, "myverysecretpassword".toCharArray())



}



Dynatrace.startup(this, DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withKeyStore(trusted)



.buildConfiguration()



)
```

Temporarily disable certificate validation

Deprecated

You can also deactivate certificate validation. However, use this option with caution and not in the production code. Otherwise, deactivating the certificate validation might dismantle the connection authenticity. Also, note that the hostname verification cannot be deactivated.

This option was deprecated with OneAgent SDK for Android version 8.257.

#### Via Dynatrace Android Gradle plugin

You can deactivate the certificate validation via the [`certificateValidation` propertyï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.DebugOptions.html#com.dynatrace.tools.android.dsl.DebugOptions:certificateValidation).

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



debug {



certificateValidation false



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



certificateValidation(false)



}



}



}



}
```

#### Via OneAgent SDK

You can also deactivate the certificate validation with the [`ConfigurationBuilder.withCertificateValidation(boolean)`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/conf/ConfigurationBuilder.html#withCertificateValidation(boolean)) method.

Java

Kotlin

```
Dynatrace.startup(this, new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withCertificateValidation(false)



.buildConfiguration());
```

```
Dynatrace.startup(this, DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withCertificateValidation(false)



.buildConfiguration())
```

## Certificate pinning

To use certificate pinning, follow the instructions provided by Android at [Network security configuration > Pin certificatesï»¿](https://developer.android.com/training/articles/security-config#CertificatePinning).

## Custom HTTP headers

If HTTP requests of OneAgent don't fulfill the security requirements of your server infrastructure, you can modify the HTTP headers of OneAgent with the `Dynatrace.setBeaconHeaders(Map<String, String>)` method. This feature allows you to add an `Authorization` header to the HTTP requests and immediately reconnect to the Cluster ActiveGate when the token has expired.

To delete the old headers, call `Dynatrace.setBeaconHeaders(null)`.

#### Basic authorization

When the authorization information is already available at the app start, call the `Dynatrace.setBeaconHeaders` method before the starting up `Dynatrace.startup` method. Every HTTP request of the OneAgent will then have the correct headers.

Java

Kotlin

```
Map<String, String> headers = new HashMap<>();



headers.put("Cookie", "n1=v1; n2=v2");



headers.put("ExampleHeader", "ExampleValue");



headers.put("Authorization", basicAuthorization(username, password));



Dynatrace.setBeaconHeaders(headers);



Dynatrace.startup(this, new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.buildConfiguration());
```

```
val headers = HashMap<String, String>()



headers["Cookie"] = "n1=v1; n2=v2"



headers["ExampleHeader"] = "ExampleValue"



headers["Authorization"] = basicAuthorization(username, password)



Dynatrace.setBeaconHeaders(headers)



Dynatrace.startup(this, DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.buildConfiguration()



)
```

If the authorization information is not available at the app start, call the [`Dynatrace.setBeaconHeaders`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#setBeaconHeaders-java.util.Map-) method when the information is available. The startup `Dynatrace.startup` method should still be called in the `Application.onCreate` method to track the correct start time. OneAgent will be automatically deactivated when the server sends an invalid status code response. The `Dynatrace.setBeaconHeaders` method will activate OneAgent and will immediately reconnect to the Cluster ActiveGate.

#### Authorization with a token

If you use an authorization procedure, which requires you to regularly update a token, then you should add a `CommunicationProblemListener`. The listener must be added via the `DynatraceConfigurationBuilder` in the `Dynatrace.startup` method.

Java

Kotlin

```
Dynatrace.startup(this, new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withCommunicationProblemListener(new YourDynatraceListener())



.buildConfiguration());
```

```
Dynatrace.startup(this, DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withCommunicationProblemListener(YourDynatraceListener())



.buildConfiguration())
```

When you use a [`CommunicationProblemListener`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/comm/CommunicationProblemListener.html), OneAgent communication behavior is slightly different from the normal behavior. If the Cluster ActiveGate reacts with an invalid status code, like `403 Forbidden`, OneAgent won't reconnect to the server. Instead, OneAgent will wait until you have specified the correct headers with the method `Dynatrace.setBeaconHeaders`. In this case, OneAgent will notify the `CommunicationProblemListener` asynchronously in a background thread via the [`onFailure(int, String, String)`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/comm/CommunicationProblemListener.html#onFailure-int-java.lang.String-java.lang.String-) interface method. The following code snippet shows a sample implementation for the `CommunicationProblemListener` interface:

Java

Kotlin

```
public class YourDynatraceListener implements CommunicationProblemListener {



@Override



public void onFailure(int responseCode, String responseMessage, String body) {



String token = refreshToken();



Dynatrace.setBeaconHeaders(generateAuthorizationHeader(token));



}



@Override



public void onError(Throwable throwable) {



//do nothing



}



}
```

```
class YourDynatraceListener : CommunicationProblemListener {



override fun onFailure(responseCode: Int, responseMessage: String?, body: String?) {



String token = refreshToken()



Dynatrace.setBeaconHeaders(generateAuthorizationHeader(token))



}



override fun onError(throwable: Throwable?) {



//do nothing



}



}
```

The interface method [`onError(Throwable)`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/comm/CommunicationProblemListener.html#onError-java.lang.Throwable-) is asynchronously called when a communication problem occurs, such as a connection timeout or an SSL handshake error. In this case, OneAgent waits for a certain time and then reconnects to the Cluster ActiveGate. Normally you don't have to react on this callback method.

## Offline monitoring

For efficiency, Dynatrace does not accept monitoring data older than 10 minutes. If the app is not connected to the internet for a longer period, OneAgent discards the old monitoring data and stops monitoring the app until the device establishes a new network connection.