---
title: OneAgent for iOS advanced configuration in RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/configuration-settings
---

# OneAgent for iOS advanced configuration in RUM Classic

# OneAgent for iOS advanced configuration in RUM Classic

* How-to guide
* 3-min read
* Updated on Dec 15, 2025

The auto-instrumentation process instruments your iOS apps for monitoring with OneAgent. The instrumentation process is an automated way of adding OneAgent to an app without manually modifying its source code. An auto-instrumented app is equivalent to an app that is manually instrumented for basic data collection. This level of instrumentation provides visibility into the real user experience delivered by your app. It also enables crash detection and performance monitoring related to app start-up and web request response times.

## RUM only

### Custom URL session

For RUM, the `Dynatrace.setURLSession` API can be used to set a custom `URLSession`, allowing more advanced network communication configuration.

This can be used, for example, to set up certificate pinning or add custom headers, similar to the configurations described in the RUM Classic examples below.

## RUM Classic only

### Set up PKH pinning with Dynatrace

You can use the **Public Key Hash Pinning** (PKH) feature for authentication.

Public key pinning is risky and will cause problems if not set up correctly. If you make a mistake, your app might pin a set of keys that validates authentication today but stops working at some unknown point in the future. In such a case, your app will no longer be able to connect to the server and will most likely stop working until it's updated with a new set of keys.

1. Go to the OneAgent distribution package, open the **Certificate Pinning** folder, and run the `getPKHashFromCertificate.py` script to generate hashes from your certificates.

   ```
   python getPKHashFromCertificate.py <path to your cert>.<der|pem> --type <DER | PEM>
   ```

   The output should look like this:

   ```
   CERTIFICATE INFO



   ----------------



   subject= *****



   issuer= *****



   SHA1 Fingerprint= ******



   ---------------------- DTXDomainPins item ----------------------



   DTXPKHash: SomePublicKeyHash=



   DTXPKHashAlgoritm: DTXAlgorithmRsa2048
   ```
2. In your [`Info.plist` file](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration."), use the script output as an array under the [`DTXPublicKeyPins` configuration key](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#privacy-and-security "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.").

   ```
   <key>DTXPublicKeyPins</key>



   <array>



   <dict>



   <key>DTXPKHash</key>



   <string>SomePublicKeyHash=</string>



   <key>DTXPKHashAlgoritm</key>



   <string>DTXAlgorithmRsa2048</string>



   </dict>



   <dict>...script output 2...</dict>



   <dict>...script output 3...</dict>



   </array>
   ```

If you don't have the OneAgent distribution package, you can download it from your mobile app settings.

1. Go to **Mobile**.
2. Select the mobile application that you want to configure.
3. Select **More** (**…**) > **Edit** in the upper-right corner of the tile with your application name.
4. From the application settings, select **Instrumentation wizard**.
5. Select **iOS**, and then switch to the **Developer** tab.
6. Select **Download OneAgent**.

### Use custom HTTP headers

If the HTTP requests of OneAgent don't fulfill the security requirements of your server infrastructure, you can modify the HTTP headers of OneAgent with `Dynatrace.setBeaconHeaders([String : String]?)`. This feature allows you to add an `Authorization` header to the HTTP requests and immediately reconnect to the Cluster ActiveGate when the token has expired. To delete the old headers, call `Dynatrace.setBeaconHeaders(nil)`.

```
Dynatrace.setBeaconHeaders(["Cookie" : "n1=v1; n2=v2", "MyHeader" : "MyHeader", "Authorization" : "API-Token aa11bb22cc33dd44ee55"]) //set headers onto beacon



let headers: Dictionary<String, String>? = Dynatrace.beaconHeaders()    //request the headers that have been set



//listen for communication problems (for example, if beacon header contains a token that can expire required to pass a firewall)



NotificationCenter.default.addObserver(forName: NSNotification.Name(rawValue: Dynatrace.getCommunicationProblemNotificationName()), object: nil, queue: nil) { _ in



//for example, update beacon header with new token



}
```