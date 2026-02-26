---
title: OpenTelemetry interoperability in Java
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/lambda-otel-bridge-java
scraped: 2026-02-26T21:30:27.361407
---

# OpenTelemetry interoperability in Java

# OpenTelemetry interoperability in Java

* Reference
* 7-min read
* Updated on Sep 19, 2024

OneAgent version 1.225+

OpenTelemetry interoperability connects the [Dynatrace AWS Lambda extension](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension "Monitor Lambda functions written in Python, Node.js, and Java.") to the OpenTelemetry Java API to use the instrumentation packages and extensions. You can then monitor technologies like databases or messaging frameworks that aren't supported by Dynatrace AWS Lambda extension out of the box.

## Before you start

Ensure that [OpenTelemetry interoperability is enabled](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability#enable "Enable and use OpenTelemetry interoperability in AWS Lambda.").

## Use OpenTelemetry Java instrumentation

OpenTelemetry for Java provides several instrumentation packages in their [OpenTelemetry Java instrumentation repositoryï»¿](https://github.com/open-telemetry/opentelemetry-java-instrumentation) that can be used in combination with the Dynatrace AWS Lambda extension for additional visibility into certain technologies.

Example: Instrument AWS SDK for Java to monitor a DynamoDB database

Dynatrace version 1.277+ The following example shows how the [OpenTelemetry AWS SDK instrumentationï»¿](https://github.com/open-telemetry/opentelemetry-java-instrumentation/tree/main/instrumentation/aws-sdk) packages can be used to monitor calls to a DynamoDB database.

Depending on the AWS SDK version you use, add one of the following packages to your package manager configuration (for example, Maven or Gradle).

Once the package has been added as a dependency, instrumentation is automatically added to capture requests to DynamoDB.

For the instrumentation to capture an item, query the item from DynamoDB using the AWS SDK, as in the code example below.

```
import java.util.Map;



import com.amazonaws.services.lambda.runtime.Context;



import com.amazonaws.services.lambda.runtime.RequestHandler;



import com.amazonaws.services.lambda.runtime.events.APIGatewayV2HTTPEvent;



import com.amazonaws.services.lambda.runtime.events.APIGatewayV2HTTPResponse;



import software.amazon.awssdk.services.dynamodb.DynamoDbClient;



import software.amazon.awssdk.services.dynamodb.model.AttributeValue;



import software.amazon.awssdk.services.dynamodb.model.GetItemRequest;



public class SimpleDynamoDBSample implements RequestHandler<APIGatewayV2HTTPEvent, APIGatewayV2HTTPResponse> {



public APIGatewayV2HTTPResponse handleRequest(APIGatewayV2HTTPEvent input, Context context) {



GetItemRequest request = GetItemRequest.builder()



.key(Map.of("mykey", AttributeValue.fromN("42")))



.tableName("MyTable")



.build();



try (DynamoDbClient dynamoDbClient = DynamoDbClient.builder().build()) {



dynamoDbClient.getItem(request);



} catch (Exception e) {



return APIGatewayV2HTTPResponse.builder().withBody("error!").withStatusCode(500).build();



}



return APIGatewayV2HTTPResponse.builder().withBody("success!").withStatusCode(200).build();



}



}
```

After running the code example above, you'll see the DynamoDB database and individual requests in the related database service.

![DynamoDB service screen.](https://dt-cdn.net/images/mytable-1080-8529dae1d2.png)

## Use OpenTelemetry Java API

[OpenTelemetry Javaï»¿](https://opentelemetry.io/docs/instrumentation/java/) can be used in an SDK-like approach to trace additional operations that aren't covered by Dynatrace out of the box.

```
@Override



public String handleRequest(Object input, Context context) {



Tracer tracer = GlobalOpenTelemetry.getTracer("instrumentation-library-name", "1.0.0");



Span span = tracer.spanBuilder("do some work").startSpan();



try {



span.setAttribute("foo", "bar");



// ....



return "Hello from OpenTelemetry Java!";



} finally {



span.end();



}



}
```

The Dynatrace AWS Lambda extension captures only spans created via tracers from `GlobalOpenTelemetry` and might not work if you try to manually (re)configure `GlobalOpenTelemetry`.

## Trace AWS SQS messages with Java

OneAgent version 1.267+

You can use open-source instrumentation packages to trace AWS SQS and SNS messages and collect them via the Dynatrace AWS Lambda extension.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Install the required dependencies**](#dependencies-java)[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Send an SQS/SNS message**](#send-message-java)[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Receive an SQS/SNS message**](#receive-message-java)

### Step 1 Install the required dependencies

To enable automatic instrumentation of SQS messages, make sure you have installed the following.

1. AWS SDK version 2.2+ for sending the messages.

   You can use the v1 and v2 SDK in the same Lambda function if you need version v1 in your function.
2. [io.opentelemetry.instrumentation:opentelemetry-aws-sdk-2.2-autoconfigureï»¿](https://central.sonatype.com/artifact/io.opentelemetry.instrumentation/opentelemetry-aws-sdk-2.2-autoconfigure/1.27.0-alpha) version 1.27+ added as a runtime-only dependency.

   The full set of dependencies used in the examples, in Gradle format, is as follows.

   ```
   dependencies {



   // Instrumentation for SQS dependencies



   implementation(platform('io.opentelemetry.instrumentation:opentelemetry-instrumentation-bom-alpha:1.27.0-alpha'))



   runtimeOnly('io.opentelemetry.instrumentation:opentelemetry-aws-sdk-2.2-autoconfigure')



   // Only needed if you want to trace messages from batches separately



   implementation('io.opentelemetry:opentelemetry-api') // (Version taken from otel-instrumentation BOM)



   // Dependencies for the AWS SDK itself -- you should already have this in your Lambda if you send SQS messages



   implementation(platform('software.amazon.awssdk:bom:2.20.85'))



   implementation('software.amazon.awssdk:sqs') // Uses version from above BOM



   // Basic AWS Lambda dependencies -- you should already have this in your Lambda



   implementation('com.amazonaws:aws-lambda-java-events:3.6.0') // SQSEvent input, etc



   implementation('com.amazonaws:aws-lambda-java-core:1.2.1') // RequestHandler interface, etc



   }
   ```

### Step 2 Send an SQS message

The example below shows a Lambda handler that sends a SQS message.

```
package com.dynatrace.example.lambda;



import com.amazonaws.services.lambda.runtime.Context;



import com.amazonaws.services.lambda.runtime.RequestHandler;



import software.amazon.awssdk.services.sqs.SqsClient;



import software.amazon.awssdk.services.sqs.model.SendMessageResponse;



public class MessageSender implements RequestHandler<Object, Void> {



private static final SqsClient client = SqsClient.create();



@Override



public Void handleRequest(Object input, Context context) {



final SendMessageResponse resp = client.sendMessage(builder -> builder



.queueUrl("[your SQS-queue URL]")



.messageBody("[your payload]")



);



System.out.printf("Sent message with ID %s (send request ID %s)%n",



resp.messageId(),



resp.responseMetadata().requestId());



return null;



}



}
```

Note that no extra code is required for tracing because the `runtimeOnly` dependency added in the first
step automatically installs a handler that creates a span behind the scenes in the `sendMessage` call using
the OpenTelemetry API, and OneAgent picks up that span automatically.

Additionally, you need to [enable the OneAgent OpenTelemetry integration](#before-you-start) and set the environment variable
[`OTEL_INSTRUMENTATION_AWS_SDK_EXPERIMENTAL_USE_PROPAGATOR_FOR_MESSAGING`ï»¿](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/instrumentation/aws-sdk/README.md#settings-for-the-aws-sdk-instrumentation) to `true` in your Lambda function's configuration.

### Step 3 Receive an SQS/SNS message



Receiving messages works out of the box when you use an AWS Lambda with an SQS trigger monitored with the Dynatrace AWS Lambda extension.

Because a span can have only a single parent, if your Lambda function receives a batch of multiple messages, you need to manually create spans to process each message if you want to track them separately and have them linked to the sender.

* If that is enough for you, or you have a maximum batch size of one configured, or you send messages only rarely, no additional code or configuration is required.
* If you want to gain more insights into a batch scenario with multiple messages, you first need to apply some configuration to allow you to override the parent span.

  To [configure the Dynatrace AWS Lambda extension](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-method "Monitor Lambda functions written in Python, Node.js, and Java.") to allow setting parent spans manually:

  + For the environment variables configuration method, set the `DT_OPEN_TELEMETRY_ALLOW_EXPLICIT_PARENT` environment variable to `true`:

    ```
    DT_OPEN_TELEMETRY_ALLOW_EXPLICIT_PARENT=true
    ```
  + For the JSON file configuration method, in `dtconfig.json`, set the following field to `true`:

    ```
    {



    ...other configuration properties...



    "OpenTelemetry": {



    "AllowExplicitParent": "true"



    }



    }
    ```

  Then new spans can be created with the parent span extracted from each received SQS message.

The following code processes messages one by one and links them to the sender as a parent span.

```
package com.dynatrace.example.lambda;



import java.util.Map;



import com.amazonaws.services.lambda.runtime.Context;



import com.amazonaws.services.lambda.runtime.RequestHandler;



import com.amazonaws.services.lambda.runtime.events.SQSEvent;



import io.opentelemetry.api.GlobalOpenTelemetry;



import io.opentelemetry.api.trace.Span;



import io.opentelemetry.api.trace.Tracer;



import io.opentelemetry.context.Scope;



import io.opentelemetry.context.propagation.TextMapGetter;



public class MessageIngress implements RequestHandler<SQSEvent, Void> {



private static final Tracer tracer = GlobalOpenTelemetry.getTracer("message-ingress-app");



@Override



public Void handleRequest(SQSEvent input, Context context) {



for (SQSEvent.SQSMessage message: input.getRecords()) {



Span span = tracer



.spanBuilder(message.getEventSource() + " process")



.setSpanKind(SpanKind.CONSUMER) // MUST be either CONSUMER or SERVER



.setParent(GlobalOpenTelemetry



.getPropagators()



.getTextMapPropagator()



.extract(



io.opentelemetry.context.Context.current(),



message.getMessageAttributes(),



SqsMessageRecordGetter.INSTANCE))



.startSpan();



try (Scope ignored = span.makeCurrent()) {



handleMessage(message);



} catch (Throwable e) {



span.recordException(e);



throw e;



} finally {



span.end();



}



}



return null;



}



private void handleMessage(SQSEvent.SQSMessage message) {



// This is where your actual handling code would go



System.out.printf("Handling message with ID %s...%n", message.getMessageId());



}



private enum SqsMessageRecordGetter implements TextMapGetter<Map<String, SQSEvent.MessageAttribute>> {



INSTANCE;



@Override



public Iterable<String> keys(Map<String, SQSEvent.MessageAttribute> carrier) {



return carrier.keySet();



}



@Override



public String get(Map<String, SQSEvent.MessageAttribute> carrier, String key) {



if (carrier == null) {



return null;



}



SQSEvent.MessageAttribute messageAttribute = carrier.get(key);



return messageAttribute == null ? null : messageAttribute.getStringValue();



}



}



}
```

This code requires a dependency on the OpenTelemetry Java API and enabling the OpenTelemetry integration in OneAgent as explained above in [Use OpenTelemetry Java API](#use-opentelemetry-java-api).

When you deploy the two Lambda functions, add OneAgent, create an SQS queue that the `MessageSender` sends to, and add a trigger to `MessageIngress` to receive from that queue, and then invoke the `MessageSender` function (for example, using the default test event), you should get a distributed trace that looks something like this:

![Screenshot of a single Distributed Trace showing an AWS Lambda that sends a SQS message and another one that receives it, along with a manually created process span](https://dt-cdn.net/images/pp-sqs-java-doc-1202-337e331f59.png)

You may wonder why both the receiving function and the processing span are direct children of the `Sqs.SendMessage`
span instead of the processing span being a child of the receiving lambda function.

This structure is required to be prepared for batch receives. When you send multiple messages to the queue quickly, your receiver can process a batch of up to 10 messages at once. In this case, there are multiple sender spans from different traces, and the trace structure implemented in the sample code ensures that each process span is linked to the `Sqs.SendMessage` span of the respective message. Because a span can have only a single parent, the receiving Lambda invoke span can be a child of only one (random) sender.

## Related topics

* [OpenTelemetry interoperability](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability "Enable and use OpenTelemetry interoperability in AWS Lambda.")
* [Trace Python, Node.js, and Java Lambda functions](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension "Monitor Lambda functions written in Python, Node.js, and Java.")