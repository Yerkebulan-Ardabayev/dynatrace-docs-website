---
title: Custom messaging services
source: https://docs.dynatrace.com/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/define-messaging-services
---

# Custom messaging services

# Custom messaging services

* How-to guide
* 8-min read
* Updated on Jun 29, 2026

Dynatrace automatically detects event-based message queue handlers. To get insight into applications using non-standard or non-event-based message queue handlers, you must first define a custom messaging service for your consumers.

For Java applications, you can enable features to [instrument Kafka listeners or SQS pollers automatically](#automatic-instrumentation) instead of manually defining a messaging service.

## Define a messaging service

To define a custom messaging service for your consumers

1. Go to **Settings** > **Service detection** > **Custom service detection**.
2. Select whether your messaging service is based on **Java**, **.NET**, **Node.js**, or **Go**, and then select **Define messaging service**.
3. Define the name of your messaging service, choose your messaging technology from the list, and then select **Find entry point**.
4. Select the process that contains your entry point from the list and select **Continue**.
5. Find the class you want to instrument, select the required class or file, and select **Continue**.
6. Java .NET To instrument the class, you can

   * **Use the selected class** for instrumenting methods of the selected class only.
   * **Use an implemented interface or superclass** for instrumenting methods in any interface or superclass in the class hierarchy. In such cases, select **Load inheritance** to load all available superclasses and interfaces, and then select the one you need.

   Node.js Select the file containing the custom service. Dynatrace presents a list of methods that can be used as a custom service. Select the desired method to complete the configuration.

   Go Select the Go package containing the method that processes the messages.
7. Select the methods you want to instrument and select **Finish**.

   See the requirements for [Apache Kafka](#kafka), [Amazon SQS SDK](#sqs-sdk) and [Spring Cloud AWS SQS](#spring-sqs) in the section below.

   The **Define custom service** page displays the newly added entry point and methods.
8. Optional Add more entry points if needed.
9. Optional Restrict the new custom service to certain process groups. See the [Restrict a custom service to specific process groups](#restrict) section below.
10. Review the entry point and methods to be instrumented.
11. In the lower-right corner of the page, select **Save**.
12. .NET Node.js Go Restart your consumer application so that the custom messaging service can be detected.

### Amazon SQS SDK

Java

.NET

Go

Custom incoming messaging services for the AWS SQS SDK must define a method in your code that is responsible for processing a single SQS message. Only such methods can be used as an entry point for AWS SQS SDK messaging services. The defined method must have exactly one `Message` parameter (and any number of other parameters) defined.

Select a method that has one of the following arguments. The full package path is required.

* [AWS SDKv1 SQS﻿](https://dt-url.net/4942e9a) `com.amazonaws.services.sqs.model.Message`
* [AWS SDKv2 SQS﻿](https://dt-url.net/pd62ee9) `software.amazon.awssdk.services.sqs.model.Message`

The required tracing attributes for incoming tagging (`x-dynatrace`, `traceparent` and `tracestate`) are automatically added by OneAgent. To disable this option,

1. Set the `optionDisableSqsReceiveAutomaticTracingMessageAttributesJava` property to `true`.
2. In the SDK API, set the `messageAttributeNames` on the `ReceiveMessageRequest` to the tracing attributes mentioned above or to `.*` or `All` to receive all message attributes.

Custom incoming messaging services for the AWS SQS SDK must define a method in your code that is responsible for processing a single SQS message. Only such methods can be used as an entry point for AWS SQS SDK messaging services. The defined method must have exactly one `Message` parameter (and any number of other parameters) defined.

Select a method that has an `Amazon.SQS.Model.Message` object as an argument. The argument can be placed anywhere in the parameter list.

The required tracing attributes for incoming tagging (`x-dynatrace`, `traceparent`, and `tracestate`) are automatically added by OneAgent.

OneAgent version 1.341+

Only supported on Linux. The Go application must include debug information.

Custom incoming messaging services for the AWS SDK Go v2 must define a method in your code that is responsible for processing a single SQS message. Only such methods can be used as an entry point for AWS SDK Go v2 messaging services. The selected method must have a pointer to a [`github.com/aws/aws-sdk-go-v2/service/sqs/types.Message`﻿](https://github.com/aws/aws-sdk-go-v2/blob/da11d7e1daa3ff669ea621230c4ed130e73e4ae0/service/sqs/types/types.go#L148) struct as its first argument
(and may have any number of other arguments).

The required tracing attributes for incoming tagging (`x-dynatrace`, `traceparent`, and `tracestate`) are automatically added by OneAgent.

### Apache Kafka

Custom messaging services for Apache Kafka must define a method in your code that is responsible for processing a single Kafka message. Only such methods can be used as an entry point for Kafka messaging services.

Java

.NET

Node.js

Select a method that has a [Kafka﻿](https://dt-url.net/ka03s3d) `org.apache.kafka.clients.consumer.ConsumerRecord` as an argument. The full package path is required.

Select a method that has a Kafka `ConsumeResult` or `Message` object as an argument. The argument can be placed anywhere in the parameter list.

If the selected method doesn't have an argument, the context will be propagated via `ThreadLocal` (on .NET Framework 4.5) or via `AsyncLocal` (on .NET Framework 4.6+ and .NET Core 2.0+).

Asynchronous methods without any arguments or without the Kafka type arguments (`ConsumeResult` or `Message`) are only supported on .NET Framework 4.6+ and .NET Core 2.0+.

OneAgent version 1.233+:

OneAgent automatically detects message handlers registered through the `eachMessage`-handler as an argument for `consumer.run()`.

OneAgent version 1.327+:

OneAgent automatically detects message handlers registered via the `eachBatch`-handler passed to `consumer.run()`.
To enable this functionality:

1. Go to **Settings** > **Preferences** > **OneAgent features**.
2. Turn on the **Node.js KafkaJs Consumer Automatic Detection** toggle.

Additionally, iterate the `batch.messages` array using `forEach` or `map`. Do not use `for...of` loop; it is not supported for automatic detection.

Example using automatic detection

```
await consumer.run({



/* ... */



eachBatch: async (pl: EachBatchPayload) => {



/* alternatively can be used pl.batch.messages.map(...) */



pl.batch.messages.forEach((msg) => {



/* ... */



});



},



/* ... */



});
```

If you enable this new variant and already have a custom messaging service configured, disable the custom service at the tenant level:

1. Go to **Settings** > **Service detection** > **Custom service detection**.
2. Select the **NodeJS Services** tab.
3. Toggle off the existing service name for the process that will use this automatic detection.

If you need to use a `for...of` loop, use the custom messaging service variant (via Custom service detection).

OneAgent version 1.325 or earlier:

To detect an `eachBatch`-handler,

1. Create an exported function with `EachMessagePayload` as the first argument and select that function as a custom service. Note that for the function to be detectable, it must be imported from a file that's separate from the file where `eachBatch`-handler is stored.
2. Adapt the `eachBatch`-handler to call the exported function for every message in the batch.

Example using defined custom service

```
// file: handlers.ts



export async function processSingleMessage(msg: EachMessagePayload) : Promise<void> {}



// file: eachBatchHandler.ts



import { processSingleMessage } from "./handlers";



async function eachBatchHandler(pl: EachBatchPayload): Promise<void> {



/* ... */



for (const message of pl.batch.messages) {



/* ... */



const singlePayload: EachMessagePayload = {



message: message,



topic: pl.batch.topic,



partition: pl.batch.partition



};



await processSingleMessage(singlePayload);



/* ... */



}



}
```

### Spring Cloud AWS SQS

Java

* If you use the `@SqsListener` annotation or the [MessageListener﻿](https://dt-url.net/7p02e18) interface, no further configuration is needed.
* If you use the [SqsTemplate﻿](https://dt-url.net/kq02erd), a custom messaging service for Spring Cloud AWS SQS incoming must define a method in your code that is responsible for processing a single SQS message. This method can be used as an entry point for Spring Cloud AWS SQS messaging services. The defined method must have exactly one `Message` parameter (and any number of other parameters).

Select a method that has exactly one [Spring Cloud AWS SQS﻿](https://dt-url.net/fq02e9l) `org.springframework.messaging.Message` parameter, no [AWS SDKv1 SQS﻿](https://dt-url.net/4942e9a) `com.amazonaws.services.sqs.model.Message` and [AWS SDKv2 SQS﻿](https://dt-url.net/pd62ee9) `software.amazon.awssdk.services.sqs.model.Message` parameters and any amount of other parameters. The full package path is required.

The required tracing attributes for incoming tagging (`x-dynatrace`, `traceparent` and `tracestate`) are automatically added by OneAgent. To disable this option, set the `optionDisableSqsReceiveAutomaticTracingMessageAttributesJava` property to `true`. In Spring, the message attribute names to receive is set to `All` by default.

## Priority of messaging services

If you have several custom services defined, the evaluation goes from top to bottom, applying the first matching rule. If for some reason you have the same class and method defined in several custom services, make sure to prioritize the services accordingly.

## Edit messaging service

You can edit any custom service at any time. For changes to take effect, you need to restart the affected processes, unless real-time updates are activated for **Java** and **PHP**. For **.NET**, **Node.js** and **Go**, you must restart the process.

To edit a custom service, select the service's **Edit** button in the list of services. You can

* Activate or deactivate existing entry points.
* Add or delete entry points.
* Add or delete methods in entry points.
* Restrict the custom service to certain process groups. See the [Restrict a custom service to specific process groups](#restrict) section below.

### Real-time updates

Updates to Java and PHP custom messaging services can be applied in near real time, without process restarts. To activate this feature, go to **Settings** > **Server-side service detection** > **Deep monitoring** > **Real-time updates to Java and PHP services** and enable the dedicated switches.

Note that with real-time updates, you do not need to restart processes; however, such updates might cause CPU spikes when deployed.

## Restrict a messaging service to specific process groups

You can restrict usage of any custom service to certain process groups. Custom service rules apply in specified process groups only and are ignored in other process groups. You can restrict a custom service when you create it or edit it.

To restrict a custom service

1. On the **Define custom service** or **Edit service** page, expand the **Optionally restrict custom service rules by process groups** dropdown menu.
2. Select **Add process group** and select the process group where you want to apply the custom service.
3. Select **Add**.
4. In the lower-right corner of the **Define custom service** or **Edit service** page, select **Save**.

## Automatic instrumentation

For specific technologies, Dynatrace can create a custom messaging service for you by automatically instrumenting a method.

### Apache Kafka

Java

1. Go to **Settings** > **Preferences** > **OneAgent features**.
2. Turn on **Java Kafka - discover listeners automatically [Opt-In]**.

After you enable it, Dynatrace will automatically create a trace for each message by instrumenting the iterators and iterables returned by the corresponding methods (`.iterator()` and `.records(...)`) of a `ConsumerRecords` object. Note that for traces to be complete, the `next()` and `hasNext()` methods of the returned iterator must be properly called until the list is fully processed and `hasNext()` returns `false`.

Best practices for complete traces

If your code contains a `break;` statement in a loop or an `Exception` is thrown, traces will be incomplete. To avoid incomplete traces, you can

* Enable the OneAgent `enableEscapedPathClosure` option to automatically close the last trace. Note that this option has a significant performance cost.
* Use the following code structure for receiving and processing messages:

  ```
  // Example from Apache Kafka v3 using ConsumerRecords.iterator()



  private void consumeRecords(Properties props, String topic) {



  try (KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props)) {



  consumer.subscribe(Collections.singletonList(topic));



  // When Java Kafka - discover listeners automatically [Opt-In] feature is enabled, Dynatrace instruments the Iterators and Iterables from this object



  ConsumerRecords<String, String> records = consumer.poll(500);



  if (records.isEmpty()) {



  return;



  }



  // Ensure that this for-loop does NOT have a "break;" statement



  for (ConsumerRecord<String, String> record : records) {



  try {



  processSingleRecord(sqsClient, message);



  } catch (Exception ex) {



  // Handle the exception, then continue the for-loop



  }



  }



  }



  }



  private void processSingleRecord(ConsumerRecord<String, String> record) {



  // Process the message



  }
  ```

### Amazon SQS SDK

Java

1. Go to **Settings** > **Preferences** > **OneAgent features**.
2. Turn on **Java AWS SQS SDK - instrument pollers automatically [Opt-In]**.

After you enable it, Dynatrace will automatically create a trace for each message by instrumenting the iterators and iterables returned by the corresponding methods (`.iterator()` and `.records(...)`) of a `ReceiveMessageResult.getMessages()` (SDK v1) or `ReceiveMessageResponse.messages()` (SDK v2) object. Note that for traces to be complete, the `next()` and `hasNext()` methods of the returned iterator must be properly called until the list is fully processed and `hasNext()` returns `false`.

Best practices for complete traces

If your code contains a `break;` statement in a loop or an `Exception` is thrown, traces will be incomplete. To avoid incomplete traces, you can

* Enable the OneAgent `enableEscapedPathClosure` option to automatically close the last trace. Note that this option has a significant performance cost.
* Use the following code structure for receiving and processing messages:

```
// Example from AWS SDK v2



private void receiveMessages(SqsClient sqsClient) {



ReceiveMessageResponse response = sqsClient.receiveMessage(ReceiveMessageRequest.builder()



.maxNumberOfMessages(10)



.queueUrl(queueUrl)



.build());



if (response == null || !response.hasMessages()) {



return;



}



// with the feature enabled, this list will be instrumented by Dynatrace



List<Message> messages = response.messages();



// ensure that this for-loop does NOT have a "break;" statement



for (Message message : messages) {



try {



processSingleMessage(message);



} catch (Exception ex) {



// handle the exception, then continue the for-loop



}



}



}



private void processSingleMessage(Message message) {



// process the message



}
```

## Related topics

* [Custom services API](/managed/dynatrace-api/configuration-api/service-api/custom-services-api "Learn what the Dynatrace custom services config API offers.")