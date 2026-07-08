---
title: OpenTelemetry interoperability in Node.js
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/lambda-otel-bridge-nodejs
---

# OpenTelemetry interoperability in Node.js

# OpenTelemetry interoperability in Node.js

* How-to guide
* 9-min read
* Updated on Apr 28, 2026

OneAgent version 1.229+

OpenTelemetry interoperability connects the [Dynatrace AWS Lambda extension](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension "Monitor Lambda functions written in Python, Node.js, and Java.") to the OpenTelemetry Node.js instrumentation to use the instrumentation packages and extensions. You can then monitor technologies like databases or messaging frameworks that aren't supported by Dynatrace AWS Lambda extension out of the box.

## Before you start

* Ensure that [OpenTelemetry interoperability is enabled](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability#enable "Enable and use OpenTelemetry interoperability in AWS Lambda.").
* Verify that the installed JavaScript OpenTelemetry API is compatible with the Dynatrace AWS Lambda extension. The following table lists the compatible versions:

  | OneAgent version | Maximum OpenTelemetry API version |
  | --- | --- |
  | 1.297+ | 1.9.x |
  | 1.289+ | 1.8.x |
  | 1.283+ | 1.7.x |
  | 1.279+ | 1.6.x |
  | 1.261+ | 1.4.x |
  | 1.259+ | 1.3.x |
  | 1.257+ | 1.2.x |
  | 1.241+ | 1.1.x |
  | 1.229+ | 1.0.x |

## Use OpenTelemetry Node.js instrumentation

When using an OpenTelemetry Node.js instrumentation, the configuration of all necessary OpenTelemetry SDK components and the registration of a TracerProvider are automatically handled by the Dynatrace AWS Lambda extension, so you don't need to register another TracerProvider.

Instrumentation packages for JavaScript can be found in the [OpenTelemetry JavaScript contributions repository﻿](https://github.com/open-telemetry/opentelemetry-js-contrib). Note that

* Some instrumentations might interfere with the Dynatrace HTTP and Lambda instrumentations and are automatically suppressed. These include [@opentelemetry/instrumentation-http﻿](https://github.com/open-telemetry/opentelemetry-js/tree/main/experimental/packages/opentelemetry-instrumentation-http) and [@opentelemetry/instrumentation-aws-lambda﻿](https://github.com/open-telemetry/opentelemetry-js-contrib/tree/main/plugins/node/opentelemetry-instrumentation-aws-lambda).
* [@opentelemetry/auto-instrumentations-node﻿](https://github.com/open-telemetry/opentelemetry-js-contrib/tree/instrumentation-aws-lambda-v0.26.0/metapackages/auto-instrumentations-node) use is discouraged, as it includes many different instrumentations.
* If [`opentelemetry/instrumentation-aws-sdk`﻿](https://www.npmjs.com/package/@opentelemetry/instrumentation-aws-sdk) is used to instrument [AWS SDK V3﻿](https://github.com/aws/aws-sdk-js-v3), provided by the Node.js v18 and v20 Lambda runtimes, it will work for instrumentation version 0.36.0+.

Example: Instrument calls in your Node.js Lambda function via instrumentation package

The following code example shows how to instrument [PostgreSQL﻿](https://www.postgresql.org/) calls in your Node.js Lambda function by using the [opentelemetry-instrumentation-pg﻿](https://github.com/open-telemetry/opentelemetry-js-contrib/tree/main/plugins/node/opentelemetry-instrumentation-pg) instrumentation package.

```
const { registerInstrumentations } = require('@opentelemetry/instrumentation');



const { PgInstrumentation } = require('@opentelemetry/instrumentation-pg');



// You must create the PgInstrumentation (and other instrumentations)



// before loading any corresponding modules, such as `require('pg')`.



registerInstrumentations({



instrumentations: [



new PgInstrumentation(),



],



});



const { Client } = require('pg');



exports.handler = async function myHandler(event, context) {



let client;



try {



client = new Client(/* DB connection information */);



await client.connect();



const result = await client.query('SELECT * FROM users;');



return result.rows;



} finally {



client?.end();



}



}
```

To instrument the [AWS SDK for JavaScript﻿](https://aws.amazon.com/sdk-for-javascript/), OpenTelemetry provides the [`opentelemetry/instrumentation-aws-sdk`﻿](https://www.npmjs.com/package/@opentelemetry/instrumentation-aws-sdk) instrumentation package.

Example: Instrument AWS SDK for JavaScript to monitor a DynamoDB database

The following code example shows how the [`opentelemetry/instrumentation-aws-sdk`﻿](https://www.npmjs.com/package/@opentelemetry/instrumentation-aws-sdk) instrumentation package can be used to add observability for calls to a DynamoDB database (Dynatrace version 1.244+).

```
const AWS = require('aws-sdk');



const { registerInstrumentations } = require('@opentelemetry/instrumentation');



const { AwsInstrumentation } = require('@opentelemetry/instrumentation-aws-sdk');



registerInstrumentations({



instrumentations: [



new AwsInstrumentation()



]



});



exports.handler = function(event, context) {



const ddb = new AWS.DynamoDB();



const dbParamsGetDelete = {



TableName: 'E2E_test_table',



Key: {



'svnr': { N: '1234'}



}



};



ddb.getItem(dbParamsGetDelete, function(err, data) {



if (err) {



console.error('Error', err);



} else {



console.log('Success', data.Item);



}



});



};
```

## Use OpenTelemetry Node.js API

[OpenTelemetry JavaScript﻿](https://github.com/open-telemetry/opentelemetry-js) can be used in an SDK-like approach to trace additional operations that aren't covered by an instrumentation package.

```
const opentelemetry = require('@opentelemetry/api');



const tracer = opentelemetry.trace.getTracer('my-package-name');



exports.handler = function(event, context) {



// create a span using the OTel API



const span = tracer.startSpan('do some work');



span.setAttribute('foo', 'bar');



span.end();



// ...



const response = {



statusCode: 200,



body: JSON.stringify('Hello from Node.js'),



};



return response;



};
```

## Trace AWS SQS and SNS messages with Node.js

OneAgent version 1.253+ for SQS OneAgent version 1.257+ for SNS

You can use [@opentelemetry/instrumentation-aws-sdk﻿](https://www.npmjs.com/package/@opentelemetry/instrumentation-aws-sdk) package to trace AWS SQS and SNS messages and collect the traces via Dynatrace AWS Lambda extension.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Install the required dependencies**](#dependencies-node)[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Set up tracing**](#set-up-tracing-node)[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Send an SQS/SNS message**](#sqs-message-node)[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Receive an SQS/SNS message**](#receive-message-node)

### Step 1 Install the required dependencies

```
npm install @opentelemetry/api @opentelemetry/instrumentation-aws-sdk @opentelemetry/instrumentation aws-sdk
```

### Step 2 Set up tracing

Use the following code to set up tracing for sending SQS messages to an SQS queue from a Dynatrace-monitored Node.js application:

```
const { AwsInstrumentation } = require('@opentelemetry/instrumentation-aws-sdk');



const { registerInstrumentations } = require('@opentelemetry/instrumentation');



// The instrumentation must be registered before importing the aws-sdk module!



registerInstrumentations({



instrumentations: [



new AwsInstrumentation()



]



});



// You can now import the aws-sdk module if needed:



const AWS = require('aws-sdk');
```

### Step 3 Send an SQS/SNS message

* Via Node.js HTTP server:

  When you make a request to the HTTP server, a message is sent to an SQS queue or SNS topic. If you send a message before the trace root span exists, make sure to create the trace root span manually. For details on the span manual creation with OpenTelemetry, see [Use OneAgent with OpenTelemetry data](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel "Learn how to send OpenTelemetry data to a Dynatrace OneAgent.").

  Example

  In this code example, a trace root span for the incoming HTTP request is created by the tracer.

  ```
  const http = require("http");



  const AWS = require('aws-sdk');



  const sqs = new AWS.SQS();



  const sns = new AWS.SNS();



  const server = http.createServer((req, res) => {



  const messageSendCallback = function (err, message) {



  if (err) {



  console.log("failed to send a message: " + err);



  res.writeHead(500);



  res.end("failure");



  } else {



  console.log("Success", message.MessageId);



  res.writeHead(200);



  res.end("success");



  }



  }



  if (req.url === "/send-sqs-message") {



  const params = {



  DelaySeconds: 10,



  MessageBody: "[your payload]",



  QueueUrl: "[your SQS-queue URL]"



  };



  sqs.sendMessage(params, messageSendCallback);



  } else if (req.url === "/send-sns-message") {



  const params = {



  Message: "[your payload]",



  TopicArn: "[your SNS-topic ARN]"



  };



  sns.publish(params, messageSendCallback);



  } else {



  res.writeHead(404);



  res.end("not found");



  }



  });



  server.on("close", () => { console.log("Closing server") });



  server.listen(8004, () => {



  console.log("server started!");



  });
  ```

  The second node in the distributed trace named `sqs-minimal-sample-nodejs-receiver-trigger send` represents the sent SQS message and is generated by the [aws-sdk﻿](https://www.npmjs.com/package/aws-sdk) instrumentation.

  Because `aws-sdk` package uses HTTP requests to send SQS messages, there is a call to `Requests to public networks`, which are captured by the OneAgent HTTP instrumentation. The call `invoke` comes from the AWS Lambda function subscribed to the SQS queue, which is monitored by the Dynatrace AWS Lambda extension.
* Via AWS Lambda function

  You can send an SQS or SNS message from an AWS Lambda function monitored by the Dynatrace AWS Lambda extension.

  SQS

  SNS

  ```
  const AWS = require('aws-sdk');



  exports.handler = function (event, context, callback) {



  const sqs = new AWS.SQS();



  const params = {



  DelaySeconds: 10,



  MessageBody: "[your payload]",



  QueueUrl: "[your SQS-queue URL]"



  };



  sqs.sendMessage(params, function (err, data) {



  if (err) {



  context.succeed({



  statusCode: 500,



  body: err,



  });



  } else {



  console.log("SQS-Success", data.MessageId);



  context.succeed({



  statusCode: 200,



  body: "SQS-Success",



  });



  }



  });



  }
  ```

  ```
  const AWS = require('aws-sdk');



  exports.handler = function (event, context, callback) {



  const sns = new AWS.SNS();



  const params = {



  Message: "[your payload]",



  TopicArn: "[your SNS-topic ARN]"



  };



  sns.publish(params, function (err, data) {



  if (err) {



  context.succeed({



  statusCode: 500,



  body: err,



  });



  } else {



  console.log("SNS-Success", data.MessageId);



  context.succeed({



  statusCode: 200,



  body: "SNS-Success",



  });



  }



  });



  }
  ```

### Step 3 Receive an SQS/SNS message

SQS

SNS

You can trace SQS messages forwarded from

* An SQS topic

  The Dynatrace AWS Lambda extension automatically extracts the parent and creates a Lambda span when an AWS Lambda function is triggered by AWS SQS.
  When a batch of multiple messages is received, only the last message is considered and used for parent propagation.

  To [configure the Dynatrace AWS Lambda extension](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-method "Monitor Lambda functions written in Python, Node.js, and Java.") to allow setting parent spans manually:

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
* An SNS topic

  For SNS messages that are forwarded to SQS, the message format depends on the [raw message delivery﻿](https://docs.aws.amazon.com/sns/latest/dg/sns-large-payload-raw-message-delivery.html) configuration on the SNS subscription.

  | Raw message delivery | Message format | Example |
  | --- | --- | --- |
  | Enabled | The SNS message attributes are converted to SQS message attributes and the parent can be directly extracted from the `MessageAttributes` of the SQS message. | + [Receive a batch of multiple messages](#receive-example) |
  | Disabled | The SNS message and its `MessageAttributes` are delivered as a serialized JSON string in the body of the received SQS message. To correctly link the receive span, the parent needs to be extracted from the `MessageAttributes` of the serialized SNS message. | + [Receive a batch of multiple messages](#receive-example)   Additional configuration is required for this example. When calling the `extractParent` method, set the value of the `fromSnsPayload` parameter to `true`. |

AWS Lambda functions that are triggered by SNS are supported out of the box when monitored with the Dynatrace AWS Lambda extension.

SNS topics can be configured via a subscription to forward messages to an SQS queue. Messages in the SQS queue can then be consumed by a Lambda function. Tracing the received messages in the SQS-triggered AWS Lambda function works out of the box when AWS Lambda is monitored with the Dynatrace AWS Lambda extension. However, the tracer can only select a single parent, and if your Lambda function receives batches of multiple messages, special handling is required to track each message separately.

For details, see how to [receive an SQS message](#receive-sqs-node).

## Related topics

* [OpenTelemetry interoperability](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability "Enable and use OpenTelemetry interoperability in AWS Lambda.")
* [Trace Python, Node.js, and Java Lambda functions](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension "Monitor Lambda functions written in Python, Node.js, and Java.")