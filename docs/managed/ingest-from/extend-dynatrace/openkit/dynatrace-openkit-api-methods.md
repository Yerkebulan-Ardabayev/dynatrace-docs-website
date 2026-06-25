---
title: Dynatrace OpenKit API methods
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods
scraped: 2026-05-12T11:33:50.412672
---

# Dynatrace OpenKit API methods

# Dynatrace OpenKit API methods

* 34-min read
* Updated on Feb 22, 2024

Dynatrace OpenKit offers a number of API methods that enable you to integrate OpenKit into your application. The sections below describe how to use each of these OpenKit methods.

## Obtain an OpenKit instance

To obtain a new OpenKit instance, use `DynatraceOpenKitBuilder`.

Java

.NET

C++

C

JavaScript

```
String applicationID = "application-id";



long deviceID = Util.getDeviceID();



String endpointURL = "https://tenantid.beaconurl.com/mbeacon";



OpenKit openKit = new DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID).build();
```

```
string applicationID = "application-id";



long deviceID = Util.GetDeviceID();



string endpointURL = "https://tenantid.beaconurl.com/mbeacon";



IOpenKit openKit = new DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID).Build();
```

```
const char* applicationID = "application-id";



int64_t deviceID = Util::GetDeviceID();



const char* endpointURL = "https://tenantid.beaconurl.com/mbeacon";



std::shared_pointer<openkit::IOpenKit> openKit =



openkit::DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID).build();
```

```
const char* applicationID = "application-id";



int64_t deviceID = GetDeviceID();



const char* endpointURL = "https://tenantid.beaconurl.com/mbeacon";



struct OpenKitConfigurationHandle* configurationHandle = createOpenKitConfiguration(endpointURL, applicationID, deviceID);



struct OpenKitHandle* openKitHandle = createDynatraceOpenKit(configurationHandle);



destroyOpenKitConfiguration(configurationHandle);
```

```
const applicationID: string = 'application-id';



const deviceID: number = Util.getDeviceID();



const endpointURL: string = 'https://tenantid.beaconurl.com/mbeacon';



const openkit = new OpenKitBuilder(endpointURL, applicationID, deviceID).build();
```

* `endpointURL` is the Dynatrace endpoint that OpenKit communicates with. You can find the endpoint URL in your custom application settings. See [Instrument your application using Dynatrace OpenKit](/managed/ingest-from/extend-dynatrace/openkit/instrument-your-application-using-dynatrace-openkit "Learn how to use Dynatrace OpenKit to instrument all non-web and mobile-based digital touchpoints in your environment, whether or not theyâre traditional rich client applications, smart IoT applications, or even Alexa skills.") for more information.
* `applicationID` is the unique identifier of the application. You can find the application ID in your custom application settings. See [Instrument your application using Dynatrace OpenKit](/managed/ingest-from/extend-dynatrace/openkit/instrument-your-application-using-dynatrace-openkit "Learn how to use Dynatrace OpenKit to instrument all non-web and mobile-based digital touchpoints in your environment, whether or not theyâre traditional rich client applications, smart IoT applications, or even Alexa skills.") for more information.
* `deviceID` is a unique identifier, which can be used to uniquely identify a device.

In addition to the mandatory parameters described above, the builder provides additional methods to further customize OpenKit. These include device-specific information like the operating system, manufacturer, or model ID.

Java

.NET

C++

C

JavaScript

| Method name | Description | Default value | Since version |
| --- | --- | --- | --- |
| `withApplicationVersion` | Sets the application version | OpenKit version | 1.0.1 |
| `withOperatingSystem` | Sets the operating system name | `OpenKit <OpenKit version>` | 1.0.1 |
| `withManufacturer` | Sets the manufacturer | `Dynatrace` | 1.0.1 |
| `withModelID` | Sets the model ID | `OpenKitDevice` | 1.0.1 |
| `withBeaconCacheMaxRecordAge` | Sets the maximum age of an entry in the beacon cache in milliseconds | 1 h 45 min | 1.0.1 |
| `withBeaconCacheLowerMemoryBoundary` | Sets the lower memory boundary of the beacon cache in bytes | 80 MB | 1.0.1 |
| `withBeaconCacheUpperMemoryBoundary` | Sets the upper memory boundary of the beacon cache in bytes | 100 MB | 1.0.1 |
| `withLogger` | Sets a custom `Logger` replacing the currently set one | `DefaultLogger` | 1.0.1 |
| `withTrustManager` | Sets a custom `SSLTrustManager` replacing the currently set one | `SSLStrictTrustManager` | 1.0.1 |
| `withDataCollectionLevel` | Sets the data collection level | `DataCollectionLevel.USER_BEHAVIOR` | 1.1.0 |
| `withCrashReportingLevel` | Sets the crash reporting level | `CrashReportingLevel.OPT_IN_CRASHES` | 1.1.0 |
| `withLogLevel` | Sets the default log level when the built-in logger is used | `LogLevel.WARN` | 2.0.0 |
| `withHttpRequestInterceptor` | Sets the Interceptor for requests to Dynatrace backends | `NullHttpRequestInterceptor` | 2.2.0 |
| `withHttpResponseInterceptor` | Sets the Interceptor for responses received from Dynatrace backends | `NullHttpResponseInterceptor` | 2.2.0 |

| Method name | Description | Default value | Since version |
| --- | --- | --- | --- |
| `WithApplicationVersion` | Sets the application version | OpenKit version | 1.0.1 |
| `WithOperatingSystem` | Sets the operating system name | `OpenKit <OpenKit version>` | 1.0.1 |
| `WithManufacturer` | Sets the manufacturer | `Dynatrace` | 1.0.1 |
| `WithModelID` | Sets the model ID | `OpenKitDevice` | 1.0.1 |
| `WithBeaconCacheMaxRecordAge` | Sets the maximum age of an entry in the beacon cache in milliseconds | 1 h 45 min | 1.0.1 |
| `WithBeaconCacheLowerMemoryBoundary` | Sets the lower memory boundary of the beacon cache in bytes | 80 MB | 1.0.1 |
| `WithBeaconCacheUpperMemoryBoundary` | Sets the upper memory boundary of the beacon cache in bytes | 100 MB | 1.0.1 |
| `WithLogger` | Sets a custom `ILogger` replacing the currently set one | `DefaultLogger` | 1.0.1 |
| `WithTrustManager` | Sets a custom `ISSLTrustManager` replacing the currently set one | `SSLStrictTrustManager` | 1.0.1 |
| `WithDataCollectionLevel` | Sets the data collection level | `DataCollectionLevel.USER_BEHAVIOR` | 1.1.0 |
| `WithCrashReportingLevel` | Sets the crash reporting level | `CrashReportingLevel.OPT_IN_CRASHES` | 1.1.0 |
| `WithLogLevel` | Sets the default log level when the built-in logger is used | `LogLevel.WARN` | 2.0.0 |
| `WithHttpRequestInterceptor` | Sets the Interceptor for requests to Dynatrace backends | `NullHttpRequestInterceptor` | 2.2.0 |
| `WithHttpResponseInterceptor` | Sets the Interceptor for responses received from Dynatrace backends | `NullHttpResponseInterceptor` | 2.2.0 |

| Method name | Description | Default value | Since version |
| --- | --- | --- | --- |
| `withApplicationVersion` | Sets the application version | OpenKit version | 1.0.0 |
| `withOperatingSystem` | Sets the operating system name | `OpenKit <OpenKit version>` | 1.0.0 |
| `withManufacturer` | Sets the manufacturer | `Dynatrace` | 1.0.0 |
| `withModelID` | Sets the model ID | `OpenKitDevice` | 1.0.0 |
| `withBeaconCacheMaxRecordAge` | Sets the maximum age of an entry in the beacon cache in milliseconds | 1 h 45 min | 1.0.0 |
| `withBeaconCacheLowerMemoryBoundary` | Sets the lower memory boundary of the beacon cache in bytes | 80 MB | 1.0.0 |
| `withBeaconCacheUpperMemoryBoundary` | Sets the upper memory boundary of the beacon cache in bytes | 100 MB | 1.0.0 |
| `withLogger` | Sets a custom `ILogger` replacing the currently set one | `DefaultLogger` | 1.0.0 |
| `withTrustManager` | Sets a custom `ISSLTrustManager` replacing the currently set one | `SSLStrictTrustManager` | 1.0.0 |
| `withDataCollectionLevel` | Sets the data collection level | `DataCollectionLevel::USER_BEHAVIOR` | 1.0.0 |
| `withCrashReportingLevel` | Sets the crash reporting level | `CrashReportingLevel::OPT_IN_CRASHES` | 1.0.0 |
| `withLogLevel` | Sets the default log level when the built-in logger is used | `LogLevel.WARN` | 2.0.0 |
| `withHttpRequestInterceptor` | Sets the Interceptor for requests to Dynatrace backends | `NullHttpRequestInterceptor` | 2.2.0 |
| `withHttpResponseInterceptor` | Sets the Interceptor for responses received from Dynatrace backends | `NullHttpResponseInterceptor` | 2.2.0 |

| Method name | Description | Default value | Since version |
| --- | --- | --- | --- |
| `useApplicationVersionForConfiguration` | Sets the application version | OpenKit version | 1.0.0 |
| `useOperatingSystemForConfiguration` | Sets the operating system name | `OpenKit <OpenKit version>` | 1.0.0 |
| `useManufacturerForConfiguration` | Sets the manufacturer | `Dynatrace` | 1.0.0 |
| `useModelIDForConfiguration` | Sets the model ID | `OpenKitDevice` | 1.0.0 |
| `useBeaconCacheBehaviorForConfiguration` | Sets caching behavior for the beacon cache | 1 h 45 min retention, 80 MB lower memory boundary, 100 MB upper memory boundary | 1.0.0 |
| `useLoggerForConfiguration` | Sets a custom `ILogger` replacing the currently set one | A default logger, logging to `stdout`, is used as fallback | 1.0.0 |
| `useTrustModeForConfiguration` | Sets a custom `ISSLTrustManager` replacing the currently set one | `STRICT_TRUST` | 1.0.0 |
| `useDataCollectionLevelForConfiguration` | Sets the data collection level | `DATA_COLLECTION_LEVEL_USER_BEHAVIOR` | 1.0.0 |
| `useCrashReportingLevelForConfiguration` | Sets the crash reporting level | `CRASH_REPORTING_LEVEL_OPT_IN_CRASHES` | 1.0.0 |
| `useDefaultLogLevelForConfiguration` | Sets the default log level when the built-in logger is used | `LogLevel.WARN` | 2.0.0 |
| `useHttpRequestInterceptorForConfiguration` | Sets the Interceptor for requests to Dynatrace backends | `NullHttpRequestInterceptor` | 2.2.0 |
| `useHttpResponseInterceptorForConfiguration` | Sets the Interceptor for responses received from Dynatrace backends | `NullHttpResponseInterceptor` | 2.2.0 |

| Method name | Description | Default value | Since version |
| --- | --- | --- | --- |
| `withApplicationVersion` | Sets the application version | OpenKit version | 1.0.0 |
| `withOperatingSystem` | Sets the operating system name | `OpenKit <OpenKit version>` | 1.0.0 |
| `withManufacturer` | Sets the manufacturer | `Dynatrace` | 1.0.0 |
| `withModelID` | Sets the model ID | `OpenKitDevice` | 1.0.0 |
| `withUserLanguage` | Sets the user language |  | 1.0.0 |
| `withScreenResolution` | Sets the screen resolution |  | 1.0.0 |
| `withScreenOrientation` | Sets the screen orientation |  | 1.0.0 |
| `withCommunicationChannel` | Sets the communication channel | `HttpCommunicationChannel` | 1.0.0 |
| `withRandomNumberProvider` | Sets the random number provider | `DefaultRandomNumberProvider` | 1.0.0 |
| `withLoggerFactory` | Sets the logger factory | `ConsoleLoggerFactory` | 1.0.0 |
| `withDataCollectionLevel` | Sets the data collection level | `2` (User Behavior) | 1.0.0 |
| `withCrashReportingLevel` | Sets the crash reporting level | `2` (OptIn) | 1.0.0 |
| `withLogLevel` | Sets the default log level when the built-in logger is used | `LogLevel.Info` | 1.0.0 |

## SSL/TLS security

All OpenKit communication to the backend happens via HTTPS. By default, OpenKit expects valid server certificates. However, it is possible, if needed, to bypass certificate validation. You can configure a custom trust manager using the builder.

We do not recommend bypassing TLS/SSL server certificate validation, since this allows man-in-the-middle attacks.

Java

.NET

C++

C

JavaScript

```
class MyCustomTrustManager implements SSLTrustManager {



// implement interface methods



}



SSLTrustManager trustManager = new MyCustomTrustManager()



OpenKit openKit = new DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID)



.withTrustManager(trustManager)



.build();
```

```
class MyCustomTrustManager : ISSLTrustManager



{



// implement interface methods



}



ISSLTrustManager trustManager = new MyCustomTrustManager()



OpenKit openKit = new DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID)



.WithTrustManager(trustManager)



.Build();
```

```
class MyCustomTrustManager : public openkit::ISSLTrustManager



{



// implement interface methods



};



std::shared_ptr<openkit::ISSLTrustManager> trustManager = std::make_shared<MyCustomTrustManager>()



OpenKit openKit = new DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID)



.withTrustManager(trustManager)



.build();
```

```
void applySslOptions(CURL* curl)



{



// set CURL options accordingly



}



struct TrustManagerHandle* trustManager = createCustomTrustManager(&applySslOptions);



// create OpenKit configuration and assign custom trust manager



struct OpenKitConfigurationHandle* configurationHandle = createOpenKitConfiguration(endpointURL, applicationID, deviceID);



useTrustModeForConfiguration(configurationHandle, CUSTOM_TRUST, trustManager);



// create OpenKit instance



struct OpenKitHandle* openKitHandle = createDynatraceOpenKit(configurationHandle);
```

```
class MyCustomTrustCommunicationChannel implements CommunicationChannel {



// implement interface methods



}



const trustCommunicationChannel = new MyCustomTrustCommunicationChannel();



const openkit = new OpenKitBuilder(endpointURL, applicationID, deviceID)



.withCommunicationChannel(trustCommunicationChannel)



.build();
```

## Enable verbose logging

By default, OpenKit uses a logger implementation that logs to `stdout`. If the default logger is used, you can enable verbose logging via `DynatraceOpenKitBuilder`. When the verbose mode is enabled, info and debug messages are logged.

You can also configure a custom logger. For details, see [Dynatrace OpenKit logging](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-logging "Learn how logging works with OpenKit.").

## Initialize OpenKit

When obtaining an OpenKit instance from the builder, the instance starts an automatic initialization phase. By default, initialization is performed asynchronously.

There might be situations when you need to ensure that initialization is completed before proceeding with the program logic, for example, in case of short-lived applications where a valid init and shutdown cannot be guaranteed. For such applications, OpenKit allows to wait for the initialization in two ways:

* **With timeout**: The calling threads waits a given amount of time for OpenKit to initialize. The method returns `false` in case the timeout expired or a shutdown was performed in the meantime and `true` to indicate successful initialization.
* **Without timeout**: The calling thread blocks until OpenKit is initialized. In case of misconfiguration this might block the calling thread indefinitely. The return value indicates whether the OpenKit instance has been initialized or a shutdown was performed meanwhile.

Java

.NET

C++

C

JavaScript

```
// wait until the OpenKit instance is fully initialized



boolean success = openKit.waitForInitCompletion();



// wait up to 10 seconds for OpenKit to complete initialization



long timeoutInMilliseconds = 10 * 1000;



boolean success = openKit.waitForInitCompletion(timeoutInMilliseconds);
```

```
// wait until the OpenKit instance is fully initialized



bool success = openKit.WaitForInitCompletion();



// wait up to 10 seconds for OpenKit to complete initialization



int timeoutInMilliseconds = 10 * 1000;



bool success = openKit.WaitForInitCompletion(timeoutInMilliseconds);
```

```
// wait until the OpenKit instance is fully initialized



bool success = openKit->waitForInitCompletion();



// wait up to 10 seconds for OpenKit to complete initialization



int64_t timeoutInMilliseconds = 10 * 1000;



bool success = openKit->waitForInitCompletion(timeoutInMilliseconds);
```

```
// wait until the OpenKit instance is fully initialized



bool success = waitForInitCompletion(openKit);



// wait up to 10 seconds for OpenKit to complete initialization



int64_t timeoutInMilliseconds = 10 * 1000;



bool success = waitForInitCompletionWithTimeout(openKit, timeoutInMilliseconds);
```

```
// wait until the OpenKit instance is fully initialized



openKit.waitForInit((initializedSuccessfully) => {});



// wait up to 10 seconds for OpenKit to complete initialization



const timeoutInMilliseconds = 10 * 1000;



openKit.waitForInit(() => {}, timeoutInMilliseconds);
```

In addition, OpenKit enables you to verify whether or not it's been initialized.

Java

.NET

C++

C

JavaScript

```
boolean isInitialized = openKit.isInitialized();



if (isInitialized) {



System.out.println("OpenKit is initialized");



} else {



System.out.println("OpenKit is not yet initialized");



}
```

```
bool isInitialized = openKit.IsInitialized;



if (isInitialized)



{



Console.WriteLine("OpenKit is initialized");



}



else



{



Console.WriteLine("OpenKit is not yet initialized");



}
```

```
bool isInitialized = openKit->isInitialized();



if (isInitialized)



{



std::cout << "OpenKit is initialized" << std::endl;



}



else



{



std::cout << "OpenKit is not yet initialized" << std::endl;



}
```

```
bool isInitialized = isInitialized(openKit);



if (isInitialized)



{



printf("OpenKit is initialized\n");



}



else



{



printf("OpenKit is not yet initialized\n");



}
```

```
const isInitialized = openKit.isInitialized();



if (isInitialized) {



console.log('OpenKit is initialized');



} else {



console.log('OpenKit is not yet initialized');



}
```

## Create a session

You can create a new session using the OpenKit instance obtained from the builder. When creating a new session, you can also provide an IP address.

* If a valid IPv4 or IPv6 address is provided, it is assigned to the session.
* If no IP address or an invalid IP address is provided, the IP address of the session is auto-detected and assigned on the server side.

Java

.NET

C++

C

JavaScript

```
// create a session and pass an IP address



String clientIPAddress = "12.34.56.78";



Session sessionWithArgument = openKit.createSession(clientIPAddress);



// create a session and let the IP be assigned on the server side



// this overloaded method is available since OpenKit Java 1.4.0



Session sessionWithoutArgument = openKit.createSession();
```

```
// create a session and pass an IP address



string clientIPAddress = "12.34.56.78";



ISession sessionWithArgument = openKit.CreateSession(clientIPAddress);



// create a session and let the IP be assigned on the server side



// this overloaded method is available since OpenKit .NET 1.4.0



ISession sessionWithoutArgument = openKit.CreateSession();
```

```
// create a session and pass an IP address



const char* clientIPAddress = "12.34.56.78";



std::shared_ptr<openkit::ISession> sessionWithArgument = openKit->createSession(clientIPAddress);



// create a session and let the IP be assigned on the server side



// this overloaded method is available since OpenKit Native 1.1.0



std::shared_ptr<openkit::ISession> sessionWithoutArgument = openKit->createSession();
```

```
// create a session and pass an IP address



const char* clientIPAddress = "12.34.56.78";



SessionHandle* sessionWithArgument = createSession(openKit, clientIPAddress);



// create a session and let the IP be assigned on the server side



// this function is available since OpenKit Native 1.1.0



SessionHandle* sessionWithoutArgument = createSessionWithAutoIpDetermination(openKit);
```

```
// create a session and pass an IP address



const clientIPAddress = "12.34.56.78";



const sessionWithArgument = openKit.createSession(clientIpAddress);



// create a session and let the IP be assigned on the server side



const sessionWithoutArgument = openKit.createSession();
```

## Tag specific users

You can tag the user assigned to a session. This enables you to search and filter specific user sessions and analyze individual user behavior over time in the backend. See [User tagging](/managed/observe/digital-experience/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace.") for more details.

Java

.NET

C++

C

JavaScript

```
session.identifyUser("jane.doe@example.com");
```

```
session.IdentifyUser("jane.doe@example.com");
```

```
session->identifyUser("jane.doe@example.com");
```

```
identifyUser(session, "jane.doe@example.com");
```

```
session.identifyUser("jane.doe@example.com");
```

When the [user opt-in mode](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.") is enabled for your application, it might affect user tagging and reporting of custom events, user actions, values, and errors. The exact data types not reported to Dynatrace depend on the data collection level set by a particular user. For details, refer to [Data collection levels](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

## Finish a session

When a session is no longer needed, you should end it explicitly. Although all open sessions are automatically ended when OpenKit is shut down, it's highly recommended to manually end sessions that are no longer in use.

Java

.NET

C++

C

JavaScript

```
session.end();



session = null; // not needed, just used to indicate that the session is no longer valid.
```

```
session.End();



session = null; // not needed, just used to indicate that the session is no longer valid.
```

```
session->end();



session = nullptr; // not needed, just used to indicate that the session is no longer valid.
```

```
endSession(session);



session = NULL; // good pratice, as the allocated memory is freed in endSession
```

```
session.end();
```

## Report a crash

You can report unexpected application [crashes](/managed/observe/digital-experience/rum-concepts/user-and-error-events#crash "Learn about user and error events and the types of user and error events captured by Dynatrace.") on a session. The crash details are sent immediately after you've reported a crash.

Java

.NET

C++

C

JavaScript

```
private static int div(int numerator, int denominator) {



return numerator / denominator;



}



public static void divWithCrash() {



int numerator = 5;



int denominator = 0;



try {



System.out.println("Got: " + div(numerator, denominator));



} catch (Exception e) {



String errorName = e.getClass().getName();



String reason = e.getMessage();



String stackTrace = getStackTraceAsString(e); // get the stacktrace as string, similar as e.printStackTrace()



// and now report the application crash via the session



session.reportCrash(errorName, reason, stackTrace);



}



}
```

```
private static int Div(int numerator, int denominator)



{



return numerator / denominator;



}



public static void DivWithCrash()



{



int numerator = 5;



int denominator = 0;



try



{



Console.WriteLine("Got: " + Div(numerator, denominator));



}



catch (Exception e)



{



string errorName = e.GetType().ToString();



string reason = e.Message;



string stackTrace = e.StackTrace;



// and now report the application crash via the session



session.ReportCrash(errorName, reason, stackTrace);



}



}
```

```
static int32_t div(int32_t numerator, int32_t denominator)



{



if (denominator == 0)



{



throw std::logic_error("Division by zero");



}



return numerator / denominator;



}



static void divWithCrash()



{



int32_t numerator = 5;



int32_t denominator = 0;



try



{



int32_t result = div(numerator, denominator);



std::cout << "Got: " << result << std::endl;



}



catch (std::logic_error& e)



{



const char* errorName = "std::logic_error"; // if RTTI is enabled, typeid could be used



const char* reason = e.what();



const char* stackTrace = nullptr; // use a valid const char* if a stack trace can be generated



// and now report the application crash via the session



session->reportCrash(errorName, reason, stackTrace);



}



}
```

```
const char* errorName = "application crash";



const char* reason = "some reason indicator";



const char* stackTrace = NULL; // use a valid const char* if a stack trace can be generated



// and now report the application crash via the session



reportCrash(session, errorName, reason, stackTrace);
```

```
const error = new Error('Some error');



// and now report the application crash via the session



session.reportCrash(e.name, e.message, e.stack);
```

## Create custom and child actions

You can define and report custom actions. After you create a custom action, you can add a [child action](/managed/observe/digital-experience/rum-concepts/user-actions#child-actions "Learn what user actions are and how they help you understand what users do with your application.") to it or enhance an action with additional information before finally closing it. You should create custom actions from a session and child actions from a custom action.

Java

.NET

C++

C

JavaScript

```
String rootActionName = "rootActionName";



String childActionName = "childActionName";



// create a custom action for a session



RootAction rootAction = session.enterAction(rootActionName);



// create a child action for the custom action



Action childAction = rootAction.enterAction(childActionName);
```

```
string rootActionName = "rootActionName";



string childActionName = "childActionName";



// create a custom action for a session



IRootAction rootAction = session.EnterAction(rootActionName);



// create a child action for the custom action



IAction childAction = rootAction.EnterAction(childActionName);
```

```
const char* rootActionName = "rootActionName";



const char* childActionName = "childActionName";



// create a custom action for a session



std::shared_ptr<openkit::IRootAction> rootAction = session->enterAction(rootActionName);



// create a child action for the custom action



std::shared_ptr<openkit::IAction> childAction = rootAction->enterAction(childActionName);
```

```
const char* rootActionName = "rootActionName";



const char* childActionName = "childActionName";



// create a custom action for a session



RootActionHandle* rootAction = enterRootAction(session, rootActionName);



// create a child action for the custom action



ActionHandle* childAction = enterAction(rootAction, childActionName);
```

```
const rootActionName = "rootActionName";



const childActionName = "childActionName";



// create a custom action for a session



const rootAction = session.enterAction(rootActionName);



// create a child action for the custom action



const childAction = rootAction.enterAction(childActionName);
```

The maximum duration of a user action in custom apps is 10 minutes. When a user action takes longer than this, such an action is discarded and not reported to Dynatrace.

There's no limit on the number of child actions attached to a custom action. However, note that you can have only one level of child actionsâyou can't create a child action for another child action (child actions can't have their own child actions). Also, refer to [User session structure for individual user](/managed/observe/digital-experience/rum-concepts/user-session#session-structure-dep-on-app-type "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.").

Child actions are not displayed on the [user session details page](/managed/observe/digital-experience/session-segmentation/new-user-sessions#session-details-page "Learn about user session segmentation and filtering attributes."), but you can view them on the [waterfall analysis page](/managed/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis "Learn how to analyze all user action monitoring data through waterfall analysis.") for a custom action to which these child actions are attached.

When the [user opt-in mode](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.") is enabled for your application, it might affect user tagging and reporting of custom events, user actions, values, and errors. The exact data types not reported to Dynatrace depend on the data collection level set by a particular user. For details, refer to [Data collection levels](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

## End an action

To record accurate timing information for actions, you should leave actions once they're finished.

Java

.NET

C++

C

JavaScript

```
Action parentAction = action.leaveAction(); // returns the appropriate custom action



Action parent = parentAction.leaveAction(); // will always return null
```

```
IAction parentAction = action.LeaveAction(); // returns the appropriate custom action



IAction parent = parentAction.LeaveAction(); // will always return null
```

```
std::shared_ptr<openkit::IRootAction> parentAction = action->leaveAction(); // returns the appropriate custom action



parentAction->leaveAction(); // return type is void
```

```
leaveAction(action); // return type is void



leaveRootAction(rootAction); // return type is void
```

```
const parentAction = action.leaveAction(); // returns the appropriate custom action



const parent = parentAction.leaveAction(); // will always return null
```

## Cancel an action

Canceling an action is similar to leaving an action, except that the action is discarded and is not sent to Dynatrace. Open child objects, like child actions and web request tracers, are discarded as well. Child objects that have been closed previously are sent to the backend and might be processed, depending on the event type.

Java

.NET

C++

C

```
Action parentAction = action.cancelAction(); // returns the appropriate custom action



Action parent = parentAction.cancelAction(); // will always return null
```

```
IAction parentAction = action.CancelAction(); // returns the appropriate custom action



IAction parent = parentAction.CancelAction(); // will always return null
```

```
std::shared_ptr<openkit::IRootAction> parentAction = action->cancelAction(); // returns the appropriate custom action



parentAction->cancelAction(); // return type is void
```

```
cancelAction(action); // return type is void



cancelRootAction(rootAction); // return type is void
```

## Report an event

You can report named events on actions.

Java

.NET

C++

C

JavaScript

```
String eventName = "eventName";



action.reportEvent(eventName);



// also report on the RootAction



rootAction.reportEvent(eventName);
```

```
string eventName = "eventName";



action.ReportEvent(eventName);



// also report on the RootAction



rootAction.ReportEvent(eventName);
```

```
const char* eventName = "eventName";



action->reportEvent(eventName);



// also report on the RootAction



rootAction->reportEvent(eventName);
```

```
const char* eventName = "eventName";



reportEventOnAction(action, eventName);



// also report on the RootAction



reportEventOnRootAction(rootAction, eventName);
```

```
const eventName = "eventName";



action.reportEvent(eventName);



// also report on the RootAction



rootAction.reportEvent(eventName);
```

When the [user opt-in mode](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.") is enabled for your application, it might affect user tagging and reporting of custom events, user actions, values, and errors. The exact data types not reported to Dynatrace depend on the data collection level set by a particular user. For details, refer to [Data collection levels](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

## Report a value

The `reportValue` method allows you to report key-value pairs of metadata that you can later view in the Dynatrace web UI and convert into [user action and user session properties](/managed/observe/digital-experience/custom-applications/analyze-and-use/action-and-session-properties-custom "User action and session properties, which are metadata key-value pairs, provide added visibility and deeper analysis of your end users' experience. Using these properties for your applications, you can filter user sessions, add calculated metrics, create charts, and more."). The reported values must be part of a user action.

You can report values of the following data types:

* 32-bit integer
* 64-bit integer
* Double
* String

Java

.NET

C++

C

JavaScript

```
// first report a 32-bit int value



String keyIntType = "intType";



int valueInt = 42;



action.reportValue(keyIntType, valueInt);



// then let's report a 64-bit long value



String keyLongType = "longType";



long valueLong = Long.MIN_VALUE;



action.reportValue(keyLongType, valueLong);



// then let's report a double value



String keyDoubleType = "doubleType";



double valueDouble = 3.141592653589793;



action.reportValue(keyDoubleType, valueDouble);



// and also a string value



String keyStringType = "stringType";



String valueString = "The quick brown fox jumps over the lazy dog";



action.reportValue(keyStringType, valueString);
```

```
// first report a 32-bit int value



string keyIntType = "intType";



int valueInt = 42;



action.ReportValue(keyIntType, valueInt);



// then let's report a 64-bit long value



string keyLongType = "longType";



long valueLong = long.MinValue;



action.ReportValue(keyLongType, valueLong);



// then let's report a double value



string keyDoubleType = "doubleType";



double valueDouble = 3.141592653589793;



action.ReportValue(keyDoubleType, valueDouble);



// and also a string value



string keyStringType = "stringType";



string valueString = "The quick brown fox jumps over the lazy dog";



action.ReportValue(keyStringType, valueString);
```

```
// first report a 32-bit integer value



const char* keyIntType = "intType";



int32_t valueInt = 42;



action->reportValue(keyIntType, valueInt);



// then let's report a 64-bit integer value



const char* keyLongType = "longType";



int64_t valueLong = LLONG_MIN;



action->reportValue(keyLongType, valueLong);



// then let's report a double value



const char* keyDoubleType = "doubleType";



double valueDouble = 3.141592653589793;



action->reportValue(keyDoubleType, valueDouble);



// and also a string value



const char* keyStringType = "stringType";



const char* valueString = "The quick brown fox jumps over the lazy dog";



action->reportValue(keyStringType, valueString);
```

```
// first report a 32-bit integer value



const char* keyIntType = "intType";



int32_t valueInt = 42;



reportIntValueOnAction(action, keyIntType, valueInt);



// then let's report a 64-bit integer value



const char* keyLongType = "longType";



int64_t valueLong = LLONG_MIN;



reportInt64ValueOnAction(keyLongType, valueLong);



// then let's report a double value



const char* keyDoubleType = "doubleType";



double valueDouble = 3.141592653589793;



reportDoubleValueOnAction(action, keyDoubleType, valueDouble);



// and also a string value



const char* keyStringType = "stringType";



const char* valueString = "The quick brown fox jumps over the lazy dog";



reportStringValueOnAction(action, keyStringType, valueString);
```

```
// first report a numeric value



const keyNumberName = 'My reported numeric value';



const numericValue = 42;



action.reportValue(keyNumberName, numericValue);



// and also a string value



const keyStringName = 'My reported string value';



const stringValue = 'The quick brown fox jumps over the lazy dog';



action.reportValue(keyStringName, stringValue);
```

To view the reported values in Dynatrace, go to the details of the user action that should contain that metadata and scroll down to the **Reported values** section.

![User action details page with SDK-reported values](https://dt-cdn.net/images/user-action-details-with-reported-values-2048-b44e8bca3e.png)

User action details page with SDK-reported values

To add action and session properties based on the reported values and then use these properties to create powerful queries, segmentations, and aggregations, see [Define user action and user session properties for custom applications](/managed/observe/digital-experience/custom-applications/additional-configuration/define-custom-action-and-session-properties "Send metadata to Dynatrace and define action and session properties for your monitored custom applications.").

When the [user opt-in mode](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.") is enabled for your application, it might affect user tagging and reporting of custom events, user actions, values, and errors. The exact data types not reported to Dynatrace depend on the data collection level set by a particular user. For details, refer to [Data collection levels](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

## Report an error

You can report an [error](/managed/observe/digital-experience/rum-concepts/user-and-error-events#error "Learn about user and error events and the types of user and error events captured by Dynatrace.") including its name (`errorName`) and error code (`errorCode`).

Java

.NET

C++

C

JavaScript

```
String errorName = "Unknown Error";



int errorCode = 42;



action.reportError(errorName, errorCode);
```

```
string errorName = "Unknown Error";



int errorCode = 42;



action.ReportError(errorName, errorCode);
```

```
const char* errorName = "Unknown Error";



int32_t errorCode = 42;



action->reportError(errorName, errorCode);
```

```
const char* errorName = "Unknown Error";



int32_t errorCode = 42;



// report error on a child action



reportErrorOnAction(action, errorName, errorCode);



// report error on a custom action



reportErrorOnRootAction(rootAction, errorName, errorCode);
```

```
const errorName = 'Unknown error';



const errorCode = 42;



action.reportError(errorName, errorCode);
```

You can also report the following additional information on the error:

* Required `errorName`âThe human-readable name of the error.
* Optional `causeName`âThe cause leading to the reported error, for example, the exception's class name.
* Optional `causeDescription`âThe description of the cause leading to the error, for example, the exception's description.
* Optional `stackTrace` or `causeStackTrace`âThe stack trace of the cause leading to the error.

The code snippet below shows how to report errors with additional information.

Java

.NET

C++

C

```
public void restrictedMethod() {



if (!isUserAuthorized()) {



// user is not authorized - report this as an error



String errorName = "Authorization error";



String causeName = "User not authorized";



String causeDescription = "The current user is not authorized to call restrictedMethod.";



String stackTrace = null; // no stack trace is reported



action.reportError(errorName, causeName, causeDescription, stackTrace);



return;



}



// ... further processing ...



}
```

```
public void RestrictedMethod()



{



if (!IsUserAuthorized())



{



// user is not authorized - report this as an error



string errorName = "Authorization error";



string causeName = "User not authorized";



string causeDescription = "The current user is not authorized to call restrictedMethod.";



string stackTrace = null; // no stack trace is reported



action.ReportError(errorName, causeName, causeDescription, stackTrace);



return;



}



// ... further processing ...



}
```

```
void RestrictedClass::restrictedMethod()



{



if (!isUserAuthorized())



{



const char* errorName = "Authorization error";



const char* causeName = "User not authorized";



const char* causeDescription = "The current user is not authorized to call restrictedMethod.";



const char* causeStackTrace = nullptr; // no stack trace is reported



// report the error on IAction



action->reportError(errorName, causeName, causeDescription, causeStackTrace);



// report the error on IRootAction



rootAction->reportError(errorName, causeName, causeDescription, causeStackTrace);



return;



}



// ... further processing



}
```

```
void restrictedFunction()



{



if (!isUserAuthorized())



{



const char* errorName = "Authorization error";



const char* causeName = "User not authorized";



const char* causeDescription = "The current user is not authorized to call restrictedFunction.";



const char* causeStackTrace = NULL; // no stack trace is reported



// report error on child action



reportErrorCauseOnAction(action, errorName, causeName, causeDescription, causeStackTrace);



// report error on custom action



reportErrorCauseOnRootAction(rootAction, errorName, causeName, causeDescription, causeStackTrace);



return;



}



// ... further processing



}
```

OpenKit Java and OpenKit .NET offer a convenience API to directly report caught exceptions, as demonstrated in the example below.

Java

.NET

```
try {



// call a method that is throwing an exception



callMethodThrowingException();



} catch(Exception caughtException) {



// report the caught exception as error via OpenKit



String errorName = "Unknown Error";



action.reportError(errorName, caughtException);



}
```

```
try



{



// call a method that is throwing an exception



CallMethodThrowingException();



}



catch(Exception caughtException)



{



// report the caught exception as error via OpenKit



string errorName = "Unknown Error";



action.ReportError(errorName, caughtException);



}
```

When the [user opt-in mode](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.") is enabled for your application, it might affect user tagging and reporting of custom events, user actions, values, and errors. The exact data types not reported to Dynatrace depend on the data collection level set by a particular user. For details, refer to [Data collection levels](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

## Trace web requests

One of the most powerful OpenKit features is web request tracing. When the application starts a web request, for example, HTTP GET, a special tag can be attached to the header. This header allows Dynatrace to correlate actions with a server-side distributed trace. An example is shown below.

Java

.NET

C++

C

JavaScript

```
// create URL and open URLConnection



URL url = new URL("http://www.my-backend.com/api/v3/users");



URLConnection urlConnection = url.openConnection();



// create the WebRequestTracer



WebRequestTracer webRequestTracer = action.traceWebRequest(urlConnection);



webRequestTracer.start();



// consume data



BufferedReader in = new BufferedReader(new InputStreamReader(uc.getInputStream()));



String inputLine;



while ((inputLine = in.readLine()) != null) {



// TODO - do something useful with response



}



in.close();



// stop web request tracing when done



webRequestTracer.stop(200); // would use the HTTP response code normally.



// --------------------------------------------



// alternative solution not using URLConnection



// --------------------------------------------



String url = "http://www.my-backend.com/api/v3/users";



// create the WebRequestTracer



WebRequestTracer webRequestTracer = action.traceWebRequest(url);



// this is the HTTP header name & value which needs to be added to the HTTP request.



String headerName = OpenKitConstants.WEBREQUEST_TAG_HEADER;



String headerValue = webRequestTracer.getTag();



webRequestTracer.start();



// perform the request here & do not forget to add the HTTP header



webRequestTracer.setBytesSent(12345);     // 12345 bytes sent



webRequestTracer.setBytesReceived(67890); // 67890 bytes received



webRequestTracer.stop(200);               // 200 was the response code
```

```
string url = "http://www.my-backend.com/api/v3/users";



// create the WebRequestTracer



IWebRequestTracer webRequestTracer = action.TraceWebRequest(url);



// this is the HTTP header name & value which needs to be added to the HTTP request.



string headerName = OpenKitConstants.WEBREQUEST_TAG_HEADER;



string headerValue = webRequestTracer.Tag;



// perform the request here & do not forget to add the HTTP header



using (HttpClient httpClient = new HttpClient()) {



// start timing



webRequestTracer.Start();



// set the tag



httpClient.DefaultRequestHeaders.Add(headerName, headerValue);



// ... perform the request and process the response ...



// set metadata



webRequestTracer.SetBytesSent(12345);     // 12345 bytes sent



webRequestTracer.SetBytesReceived(67890); // 67890 bytes received



webRequestTracer.Stop(200);               // 200 was the response code



}
```

```
const char* url = "http://www.my-backend.com/api/v3/users";



// create the WebRequestTracer



std::shared_ptr<openkit::IWebRequestTracer> webRequestTracer = action->traceWebRequest(url);



// this is the HTTP header name & value which needs to be added to the HTTP request.



const char* headerName = openkit::WEBREQUEST_TAG_HEADER;



const char* headerValue = webRequestTracer->getTag();



// start timing



webRequestTracer->start();



// set the tag on httpRequest



// Note: how to set this, depends on the HTTP client library in use



httpRequest.addHeader(headerName, headerValue);



// ... perform the request and process the response ...



// set metadata



webRequestTracer->setBytesSent(12345);     // 12345 bytes sent



webRequestTracer->setBytesReceived(67890); // 67890 bytes received



webRequestTracer->stop(200);               // 200 was the response code
```

```
const char* url = "http://www.my-backend.com/api/v3/users";



// create the WebRequestTracer on child action



WebRequestTracerHandle* webRequestTracer = traceWebRequestOnRootAction(rootAction, url);



// Alterantively web requests can be created on a child action like below



// WebRequestTracerHandle* webRequestTracer = traceWebRequestOnAction(action, url);



// this is the HTTP header name & value which needs to be added to the HTTP request.



const char* headerName = WEBREQUEST_TAG_HEADER;



const char* headerValue = getTag(webRequestTracer);



// start timing



startWebRequest(webRequestTracer)



// set the tag on httpRequest



// Note: how to set this, depends on the HTTP client library in use



addCustomHeaderToWebRequest(httpRequest, headerName, headerValue);



// ... perform the request and process the response ...



// set metadata



setBytesSent(webRequestTracer, 12345);     // 12345 bytes sent



setBytesReceived(webRequestTracer, 67890); // 67890 bytes received



stopWebRequest(webRequestTracer, 200);     // 200 was the response code



// After calling stopWebRequest the allocated memory is freed and therefore



// webRequestTracer is no longer valid.



webRequestTracer = NULL;
```

```
const url = 'http://www.my-backend.com/api/v3/users';



// create the WebRequestTracer



const webRequestTracer = action.traceWebRequest(url);



const headerName = webRequestTagHeader; // webRequestTagHeader can be imported



const headerValue = webRequestTracer.getTag();



webRequestTracer.start();



// perform the request here & do not forget to add the HTTP header



webRequestTracer.setBytesSent(12345);



webRequestTracer.setBytesReceived(67890);



webRequestTracer.stop(200); // stop the web request tracer, with the response code
```

## Configure data privacy

You can dynamically adjust data privacy settings and build your custom applications in compliance with data protection laws and regulations. The privacy API methods allow you to dynamically change the data collection level and activate or deactivate crash reporting.

### Data collection levels

The table below describes the available data collection levels and shows whether [user tags](/managed/observe/digital-experience/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace.") and custom user actions, events, values, and errors are reported for a particular level.

| Level | Description | User tags, custom events, and custom values | Custom user actions and errors |
| --- | --- | --- | --- |
| **Off**  Monitoring data is not sent | No personal data is sent; all identifiers are randomized on every launch.[1](#fn-1-1-def) | Not applicable | Not applicable |
| **Performance**  Only performance, automatically captured data is sent | No personal data is sent; all identifiers are randomized on every launch. | Not applicable | Applicable |
| **User behavior**  Performance data and user data is sent | Personal data is sent; OneAgent recognizes and reports users who revisit in the future.[2](#fn-1-2-def) | Applicable | Applicable |

1

A single `Loading <App>` event is sent to track the number of users that opted out.

2

If you haven't configured user tagging and custom event or value reporting, the **User behavior** level works similarly to the **Performance** level.

### Crash reporting levels

The following crash reporting levels are available.

| Level name | Crash reporting | Use this level whenâ¦ |
| --- | --- | --- |
| **Off** | Not applicable Disabled | You don't need to collect crash reports. |
| **Opt out crashes** | Not applicable Disabled | The user of your application has disallowed the collection of crash reports. |
| **Opt in crashes**  default | Applicable Enabled | The user of your application has allowed the collection of crash reports. |

### Set data collection and crash reporting levels

The code examples below show you how to work with the API:

Java

.NET

C++

C

JavaScript

```
import com.dynatrace.openkit.DataCollectionLevel;



import com.dynatrace.openkit.CrashReportingLevel;



OpenKit openKit = new DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID)



// set a data collection level (user allowed you to capture performance and personal data)



.withDataCollectionLevel(DataCollectionLevel.USER_BEHAVIOR)



// allow crash reporting (user allowed you to collect information on crashes)



.withCrashReportingLevel(CrashReportingLevel.OPT_IN_CRASHES)



.build();
```

Possible values for the data collection level:

* `DataCollectionLevel.OFF`
* `DataCollectionLevel.PERFORMANCE`
* `DataCollectionLevel.USER_BEHAVIOR`

Possible values for the crash reporting level:

* `CrashReportingLevel.OFF`
* `CrashReportingLevel.OPT_OUT_CRASHES`
* `CrashReportingLevel.OPT_IN_CRASHES`

```
using Dynatrace.OpenKit;



var openKit = new DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID)



// set a data collection level (user allowed you to capture performance and personal data)



.WithDataCollectionLevel(DataCollectionLevel.USER_BEHAVIOR)



// allow crash reporting (user allowed you to collect information on crashes)



.WithCrashReportingLevel(CrashReportingLevel.OPT_IN_CRASHES)



.Build();
```

Possible values for the data collection level:

* `DataCollectionLevel.OFF`
* `DataCollectionLevel.PERFORMANCE`
* `DataCollectionLevel.USER_BEHAVIOR`

Possible values for the crash reporting level:

* `CrashReportingLevel.OFF`
* `CrashReportingLevel.OPT_OUT_CRASHES`
* `CrashReportingLevel.OPT_IN_CRASHES`

```
#include "OpenKit/OpenKit.h"



auto openKit = openkit::DynatraceOpenKitBuilder builder(endpointURL.c_str(), applicationID.c_str(), deviceID);



// set a data collection level (user allowed you to capture performance and personal data)



builder.withDataCollectionLevel(openkit::DataCollectionLevel::USER_BEHAVIOR)



// allow crash reporting (user allowed you to collect information on crashes)



.withCrashReportingLevel(openkit::CrashReportingLevel::OPT_IN_CRASHES)



.build();
```

Possible values for the data collection level:

* `DataCollectionLevel::OFF`
* `DataCollectionLevel::PERFORMANCE`
* `DataCollectionLevel::USER_BEHAVIOR`

Possible values for the crash reporting level:

* `CrashReportingLevel::OFF`
* `CrashReportingLevel::OPT_OUT_CRASHES`
* `CrashReportingLevel::OPT_IN_CRASHES`

```
#include "OpenKit/OpenKit-c.h"



struct OpenKitConfigurationHandle* configurationHandle = createOpenKitConfiguration(endpointURL, applicationID, deviceID);



// set a data collection level (user allowed you to capture performance and personal data)



useDataCollectionLevelForConfiguration(configurationHandle, DATA_COLLECTION_LEVEL_USER_BEHAVIOR);



// allow crash reporting (user allowed you to collect information on crashes)



useCrashReportingLevelForConfiguration(configurationHandle, CRASH_REPORTING_LEVEL_OPT_IN_CRASHES);



struct OpenKitHandle* openKitHandle = createDynatraceOpenKit(configurationHandle);



destroyOpenKitConfiguration(configurationHandle);
```

Possible values for the data collection level:

* `DATA_COLLECTION_LEVEL_OFF`
* `DATA_COLLECTION_LEVEL_PERFORMANCE`
* `DATA_COLLECTION_LEVEL_USER_BEHAVIOR`

Possible values for the crash reporting level:

* `CRASH_REPORTING_LEVEL_OFF`
* `CRASH_REPORTING_LEVEL_OPT_OUT_CRASHES`
* `CRASH_REPORTING_LEVEL_OPT_IN_CRASHES`

```
import { CrashReportingLevel, DataCollectionLevel, OpenKitBuilder } from '@dynatrace/openkit-js';



const openkit = new OpenKitBuilder(endpointURL, applicationID, deviceID)



// set a data collection level (user allowed you to capture performance and personal data)



.withDataCollectionLevel(DataCollectionLevel.UserBehavior)



// allow crash reporting (user allowed you to collect information on crashes)



.withCrashReportingLevel(CrashReportingLevel.OptInCrashes)



.build();
```

Possible values for the data collection level:

* `DataCollectionLevel.Off`
* `DataCollectionLevel.Performance`
* `DataCollectionLevel.UserBehavior`

Possible values for the crash reporting level:

* `CrashReportingLevel.Off`
* `CrashReportingLevel.OptOutCrashes`
* `CrashReportingLevel.OptInCrashes`

## Terminate an OpenKit instance

When an OpenKit instance is no longer needed, for example, when the application using OpenKit is shut down, you can clear the obtained instance by invoking. A call to shutdown blocks the calling thread up to 10 seconds, while the OpenKit flushes data that hasn't been transmitted yet to the backend.

Java

.NET

C++

C

JavaScript

```
openKit.shutdown();
```

```
openKit.Shutdown();
```

```
openKit->shutdown();
```

```
shutdownOpenKit(openKit);
```

```
openKit.shutdown();
```