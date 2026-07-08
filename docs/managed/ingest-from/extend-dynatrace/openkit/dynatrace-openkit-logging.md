---
title: Dynatrace OpenKit logging
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-logging
---

# Dynatrace OpenKit logging

# Dynatrace OpenKit logging

* 3-min read
* Updated on Nov 03, 2022

There are two different ways to log with OpenKit:

* Configure OpenKit to use the built-in console logger
* Configure OpenKit to use a custom logger implementation

## Logging via console logger

OpenKit includes a console logger. By default, any error or warning message is logged to `stdout`. When you set a log level, all log events with the same or higher prior levels are logged.

OpenKit uses the following log levels:

| Log level | Priority | Description |
| --- | --- | --- |
| Debug | 0 | For debugging and development. Not recommended for production due to a high volume of log entries. |
| Info | 10 | General OpenKit flow. |
| Warning | 20 | Warnings encountered in OpenKit library, including API usage problems. |
| Error | 30 | Errors that cannot be handled by OpenKit. |

Java

.NET

C++

C

JavaScript

```
OpenKit openKit = new DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID)



.withLogLevel(LogLevel.DEBUG) // enable Debug, Info, Warning, and Error log events



.build();
```

```
IOpenKit openKit = new DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID)



.WithLogLevel(LogLevel.DEBUG) // enable Debug, Info, Warning, and Error log events



.Build();
```

```
std::shared_pointer<openkit::IOpenKit> openKit =



openkit::DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID)



.withLogLevel(LogLevel::LOG_LEVEL_DEBUG) // enable Debug, Info, Warning, and Error log events



.build();
```

```
struct OpenKitConfigurationHandle* configurationHandle = createOpenKitConfiguration(endpointURL, applicationID, deviceID);



useDefaultLogLevelForConfiguration(configurationHandle, LOGLEVEL_DEBUG);



struct OpenKitHandle* openKitHandle = createDynatraceOpenKit(configurationHandle);
```

```
const openKit = new OpenKitBuilder(endpointURL, applicationID, deviceID)



.withLogLevel(LogLevel.Debug) // enable Debug, Info, Warning, and Error log events



.build();
```

## Logging via custom logger

You can also configure OpenKit with a custom logger implementation. Implement a custom logger to log OpenKit messages using the logging framework of your choice.

Java

.NET

C++

C

JavaScript

```
import com.dynatrace.openkit.api.Logger;



class MyCustomLoggerImpl implements Logger {



// implement interface methods



}



Logger customLogger = new MyCustomLoggerImpl();



OpenKit openKit = new DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID)



.withLogger(customLogger)



.build();
```

```
using Dynatrace.OpenKit.API.ILogger;



class MyCustomLoggerImpl : ILogger



{



// implement interface methods



}



ILogger customLogger = new MyCustomLoggerImpl();



IOpenKit openKit = new DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID)



.WithLogger(customLogger)



.Build();
```

```
class MyCustomLoggerImpl : public openkit::ILogger



{



// implement interface methods



};



std::shared_ptr<openkit::ILogger> customLogger = std::make_shared<MyCustomLoggerImpl>();



std::shared_pointer<openkit::IOpenKit> openKit =



openkit::DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID)



.withLogger(customLogger)



.build();
```

```
bool levelEnabledFunction(LOG_LEVEL level)



{



// return true if level is enabled, false otherwise



}



void logFunction(LOG_LEVEL level, const char* traceStatement)



{



// write trace statement



}



// create custom logger



struct LoggerHandle* loggerHandle = createLogger(&levelEnabledFunction, &logFunction);



// create OpenKit configuration and assign logger handle



struct OpenKitConfigurationHandle* configurationHandle = createOpenKitConfiguration(endpointURL, applicationID, deviceID);



useLoggerForConfiguration(configurationHandle, loggerHandle);



struct OpenKitHandle* openKitHandle = createDynatraceOpenKit(configurationHandle);
```

```
class MyCustomLoggerFactory implements LoggerFactory {



// implement interface methods



}



const customLogger = new MyCustomLoggerFactory();



const openKit = new OpenKitBuilder(endpointURL, applicationID, deviceID)



.withLoggerFactory(customLogger)



.build();
```