---
title: Instrument your application using Dynatrace OpenKit
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/openkit/instrument-your-application-using-dynatrace-openkit
scraped: 2026-05-12T12:05:16.580400
---

# Instrument your application using Dynatrace OpenKit

# Instrument your application using Dynatrace OpenKit

* 1-min read
* Updated on Apr 25, 2024

Monitoring data sent via Dynatrace OpenKit is encapsulated into an entity that represents your application and is called **custom application**. Therefore, to monitor your application, you need to define and instrument the custom application following the instructions below.

## Create and instrument an application

To create a custom application in Dynatrace and instrument it

1. In Dynatrace, go to **Custom Applications**.
2. Select **Create custom application**.
3. Enter a name for your custom application, and choose an icon to visually represent your application in the Dynatrace web UI.
4. Select **Monitor custom application**. Your custom application settings page opens.
5. From the application settings, select **Instrumentation wizard** and then select your technology to download the latest [OpenKit library](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-libraries-on-github "Check out the Dynatrace OpenKit libraries on GitHub.").
6. Use the downloaded library and the **Beacon URL** and **Application ID** provided in the instrumentation wizard to instrument your application.
7. Optional In the instrumentation wizard, select **View incoming beacons** to show incoming beacons as they arrive, with only a couple of seconds delay. This view also provides information about potential issues.

Below is a basic example that shows how to use Dynatrace OpenKit to send monitoring data to Dynatrace. For more details, see [Dynatrace OpenKit API methods](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods "Read how Dynatrace OpenKit can be used from the developer's point of view.").

Java

.NET

C++

C

JavaScript

```
// Obtain an OpenKit instance



String applicationID = "application-id";                // Your application's ID



long deviceID = 42;                                     // Replace with a unique value per device/installation



String endpointURL = "https://tenantid.beaconurl.com/mbeacon";  // Dynatrace endpoint URL



OpenKit openKit = new DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID)



.withApplicationVersion("1.0.0.0")



.withOperatingSystem("Windows 10")



.withManufacturer("MyCompany")



.withModelID("MyModelID")



.build();



// Wait up to 10 seconds for OpenKit to complete initialization



long timeoutInMilliseconds = 10 * 1000;



boolean success = openKit.waitForInitCompletion(timeoutInMilliseconds);



// Create session



String clientIP = "8.8.8.8";



Session session = openKit.createSession(clientIP);



// Identify user



session.identifyUser("jane.doe@example.com");



// Create root and child actions



String rootActionName = "rootActionName";



RootAction rootAction = session.enterAction(rootActionName);



String childActionName = "childAction";



Action childAction = rootAction.enterAction(childActionName);



// Leave action



childAction.leaveAction();



rootAction.leaveAction();



// Finish session



session.end();



// Terminate OpenKit instance



openKit.shutdown();
```

```
// Obtain an OpenKit instance



string applicationID = "application-id";                        // Your application's ID



long deviceID = 42L;                                            // Replace with a unique value per device/installation



string endpointURL = "https://tenantid.beaconurl.com/mbeacon";  // Dynatrace endpoint URL



IOpenKit openKit = new DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID)



.WithApplicationVersion("1.0.0.0")



.WithOperatingSystem("Windows 10")



.WithManufacturer("MyCompany")



.WithModelID("MyModelID")



.Build();



// Wait up to 10 seconds for OpenKit to complete initialization



int timeoutInMilliseconds = 10 * 1000;



bool success = openKit.WaitForInitCompletion(timeoutInMilliseconds);



// Create session



string clientIP = "8.8.8.8";



ISession session = openKit.CreateSession(clientIP);



// Identify user



session.IdentifyUser("jane.doe@example.com");



// Create root and child actions



string rootActionName = "rootActionName";



IRootAction rootAction = session.EnterAction(rootActionName);



string childActionName = "childAction";



IAction childAction = rootAction.EnterAction(childActionName);



// Leave action



childAction.LeaveAction();



rootAction.LeaveAction();



// Finish session



session.End();



// Terminate OpenKit instance



openKit.ShutDown();
```

```
// Obtain an OpenKit instance



const char* applicationID = "application-id";                        // Your application's ID



int64_t deviceID = 42;                                               // Replace with a unique value per device/installation



const char* endpointURL = "https://tenantid.beaconurl.com/mbeacon";  // Dynatrace endpoint URL



std::shared_pointer<openkit::IOpenKit> openKit =



openkit::DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID)



.withApplicationVersion("1.0.0.0")



.withOperatingSystem("Windows 10")



.withManufacturer("MyCompany")



.withModelID("MyModelID")



.build();



// Wait up to 10 seconds for OpenKit to complete initialization



int64_t timeoutInMilliseconds = 10 * 1000;



bool success = openKit->waitForInitCompletion(timeoutInMilliseconds);



// Create session



const char* clientIP = "8.8.8.8";



std::shared_ptr<openkit::ISession> session = openKit->createSession(clientIP);



// Identify user



session->identifyUser("jane.doe@example.com");



// Create root and child actions



const char* rootActionName = "rootActionName";



std::shared_ptr<IRootAction> rootAction = session->enterAction(rootActionName);



const char* childActionName = "childAction";



std::shared_ptr<IRootAction> childAction = rootAction->enterAction(childActionName);



// Leave action



childAction->leaveAction();



rootAction->leaveAction();



// Finish session



session->end();



// Terminate OpenKit instance



openKit->shutdown();
```

```
// Obtain an OpenKit instance



const char* applicationID = "application-id";                        // Your application's ID



int64_t deviceID = 42;                                               // Replace with a unique value per device/installation



const char* endpointURL = "https://tenantid.beaconurl.com/mbeacon";  // Dynatrace endpoint URL



struct OpenKitConfigurationHandle* configurationHandle = createOpenKitConfiguration(endpointURL, applicationID, deviceID);



useApplicationVersionForConfiguration(configurationHandle, "1.0.0.0");



useOperatingSystemForConfiguration(configurationHandle, "Windows 10");



useManufacturerForConfiguration(configurationHandle, "MyCompany");



useModelIDForConfiguration(configurationHandle, "MyModelID");



struct OpenKitHandle* openKit = createDynatraceOpenKit(configurationHandle);



// Wait up to 10 seconds for OpenKit to complete initialization



int64_t timeoutInMilliseconds = 10 * 1000;



bool success = waitForInitCompletionWithTimeout(openKit, timeoutInMilliseconds);



// Create session



const char* clientIP = "8.8.8.8";



struct SessionHandle* session = createSession(openKit, clientIP);



// Identify user



identifyUser(session, "jane.doe@example.com");



// Create root and child actions



const char* rootActionName = "rootActionName";



struct RootActionHandle* rootAction = enterRootAction(session, rootActionName);



const char* childActionName = "childAction";



struct ActionHandle* childAction = enterAction(rootAction, childActionName);



// Leave action



leaveAction(childAction);



leaveRootAction(rootAction);



// Finish session



endSession(session);



// Terminate OpenKit instance



shutdownOpenKit(openKit);
```

```
// Obtain an OpenKit instance



const endpointURL: string = 'https://tenantid.beaconurl.com/mbeacon'; // Dynatrace endpoint URL



const applicationID: string = 'application-id'; // Your application's ID



const deviceID: number = 42; // Replace with a unique value per device/installation



const openkit = new OpenKitBuilder(endpointURL, applicationID, deviceID)



.withApplicationVersion('1.0.0.0')



.withOperatingSystem("Windows 10")



.withManufacturer("MyCompany")



.withModelID("MyModelID")



.build();



const timeoutInMilliseconds = 10 * 1000;



openKit.waitForInit((success) => {



if (success) {



// Create session



const clientIP = '8.8.8.8';



const session: Session = openkit.createSession(clientIP);



// Identify user



session.identifyUser('jane.doe@example.com');



// Create root and child actions



string rootActionName = 'rootActionName';



const rootAction = session.enterAction(rootActionName);



string childActionName = 'childAction';



const childAction = rootAction.enterAction(childActionName);



// Leave action



childAction.leaveAction();



rootAction.leaveAction();



// Finish session



session.end();



// Terminate OpenKit instance



openkit.shutdown();



}



}, timeoutInMilliseconds);
```

You can find your application ID and the endpoint URL in the instrumentation wizard (from your application settings, select **Instrumentation wizard**).

For custom applications, user identification is achieved by passing `deviceID`, which should be unique for each user or device. Then `deviceID` is marked as the **Internal user ID** in the Dynatrace web UI.

## Customize instrumentation

After creating a custom application in Dynatrace and instrumenting your actual application with OpenKit, check the pages below to customize and troubleshoot the instrumentation and configure your custom application.

* [Dynatrace OpenKit libraries on GitHub](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-libraries-on-github "Check out the Dynatrace OpenKit libraries on GitHub.")
* [Dynatrace OpenKit API methods](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods "Read how Dynatrace OpenKit can be used from the developer's point of view.")
* [Dynatrace OpenKit logging](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-logging "Learn how logging works with OpenKit.")
* [Troubleshooting Dynatrace OpenKit instrumentation](/managed/ingest-from/extend-dynatrace/openkit/troubleshoot-dynatrace-openkit-instrumentation "Learn how to solve problems that you may encounter when instrumenting Dynatrace OpenKit.")
* [Configure cost and traffic control for custom applications](/managed/observe/digital-experience/custom-applications/additional-configuration/configure-cost-and-traffic-control-custom "Leverage the cost and traffic control setting in Dynatrace to reduce session usage for custom applications.")
* [Ignore web request errors for custom applications](/managed/observe/digital-experience/custom-applications/additional-configuration/web-request-errors-custom "Stop treating certain HTTP response codes as errors for your custom applications.")
* [Create custom user action names for custom applications](/managed/observe/digital-experience/custom-applications/additional-configuration/naming-rules-custom "Customize automatically generated user action names for your custom applications.")
* [Configure key user actions for custom applications](/managed/observe/digital-experience/custom-applications/additional-configuration/configure-key-user-actions-custom "Mark a user action as a key user action and configure Apdex rating for key user actions of your custom applications.")
* [Adjust Apdex settings for custom applications](/managed/observe/digital-experience/custom-applications/additional-configuration/configure-apdex-custom "Configure the user-satisfaction performance thresholds for your custom application and its key user actions.")
* [Change user experience score thresholds for custom applications](/managed/observe/digital-experience/custom-applications/additional-configuration/configure-user-experience-score-custom "Adjust the user experience score thresholds to meet the specific requirements of your custom application.")
* [Create calculated metrics for custom applications](/managed/observe/digital-experience/custom-applications/additional-configuration/rum-calculated-metrics-custom "Create calculated metrics as well as custom charts based on calculated metrics for your custom applications.")
* [Create USQL custom metrics for custom applications](/managed/observe/digital-experience/custom-applications/additional-configuration/custom-metrics-from-user-sessions-custom-apps "Every time a user session is closed, Dynatrace can extract metrics and store them as time series. Learn how to set up and use USQL custom metrics for custom applications.")
* [Define user action and user session properties for custom applications](/managed/observe/digital-experience/custom-applications/additional-configuration/define-custom-action-and-session-properties "Send metadata to Dynatrace and define action and session properties for your monitored custom applications.")
* [Customize IP address detection for custom applications](/managed/observe/digital-experience/custom-applications/additional-configuration/customize-ip-address-detectio-custom "Change the way Dynatrace determines client IP addresses for your custom applications.")
* [Map internal IP addresses to locations for custom applications](/managed/observe/digital-experience/custom-applications/additional-configuration/map-internal-ip-addresses-to-locations-custom "Configure Dynatrace to use local addresses to understand where the users of your custom applications are.")
* [Configure first-party, third-party, and CDN resource detection for custom applications](/managed/observe/digital-experience/custom-applications/additional-configuration/configure-third-party-and-cdn-content-detection-custom "Manually define third-party and CDN providers along with auto-detected providers for your custom applications.")
* [Use OneAgent as a beacon endpoint for custom applications](/managed/observe/digital-experience/custom-applications/additional-configuration/oneagent-as-beacon-forwarder-custom "Use Dynatrace OneAgent as a beacon endpoint for custom applications.")
* [Delete a custom application](/managed/observe/digital-experience/custom-applications/additional-configuration/delete-application-custom "Delete your custom applications via the Dynatrace web UI or API.")

## Analyze and use RUM data

Once your custom application starts sending monitoring data to Dynatrace, you can analyze this data just like you do for any other application. See the pages below for more information.

* [Analyze user sessions of custom applications](/managed/observe/digital-experience/custom-applications/analyze-and-use/user-session-analysis-custom "Filter user sessions, view sessions of an individual user, and examine crashes, request errors, and report errors for your custom applications.")
* [Check user experience metrics for custom applications](/managed/observe/digital-experience/custom-applications/analyze-and-use/check-usage-metrics-custom "Learn how to use Dynatrace to check the user experience metrics of your custom application.")
* [Analyze web requests for custom applications](/managed/observe/digital-experience/custom-applications/analyze-and-use/analyze-web-requests-custom "Leverage Dynatrace to monitor web requests for your custom applications.")
* [View crash reports for custom applications](/managed/observe/digital-experience/custom-applications/analyze-and-use/crash-reports-custom "Check the latest crash reports for your custom applications.")
* [Leverage user action and user session properties for custom applications](/managed/observe/digital-experience/custom-applications/analyze-and-use/action-and-session-properties-custom "User action and session properties, which are metadata key-value pairs, provide added visibility and deeper analysis of your end users' experience. Using these properties for your applications, you can filter user sessions, add calculated metrics, create charts, and more.")

The image below shows the overview page of our test custom application.

![Custom application overview page](https://dt-cdn.net/images/custom-app-overview-page-1632-8f4bd766b2.png)

Custom application overview page