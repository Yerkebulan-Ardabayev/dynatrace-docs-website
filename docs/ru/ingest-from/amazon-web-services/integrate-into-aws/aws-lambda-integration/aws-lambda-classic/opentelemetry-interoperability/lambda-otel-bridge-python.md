---
title: OpenTelemetry interoperability in Python
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/lambda-otel-bridge-python
scraped: 2026-02-26T21:27:51.384122
---

# OpenTelemetry interoperability in Python

# OpenTelemetry interoperability in Python

* How-to guide
* 10-min read
* Updated on Feb 19, 2026

OpenTelemetry interoperability connects the [Dynatrace AWS Lambda extension](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension "Monitor Lambda functions written in Python, Node.js, and Java.") to the OpenTelemetry Python instrumentation to use the instrumentation packages and extensions. You can then monitor technologies like databases or messaging frameworks that aren't supported by Dynatrace AWS Lambda extension out of the box.

## Before you start

* Ensure that [OpenTelemetry interoperability is enabled](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability#enable "Enable and use OpenTelemetry interoperability in AWS Lambda.").
* Verify that the installed OpenTelemetry Python API version is compatible with the Dynatrace AWS Lambda extension. The following tables list the compatible versions:

  | OneAgent version | Maximum OpenTelemetry API version |
  | --- | --- |
  | 1.331+ | 1.39.x |
  | 1.329+ | 1.38.x |
  | 1.323+ | 1.36.x |

### Older versions

| OneAgent version | Maximum OpenTelemetry API version |
| --- | --- |
| 1.321+ | 1.35.x |
| 1.319+ | 1.34.x |
| 1.315+ | 1.32.x |
| 1.313+ | 1.31.x |
| 1.311+ | 1.30.x |
| 1.307+ | 1.29.x |
| 1.303+ | 1.27.x |
| 1.299+ | 1.26.x |
| 1.295+ | 1.25.x |
| 1.291+ | 1.24.x |
| 1.285+ | 1.22.x |
| 1.281+ | 1.21.x |
| 1.277+ | 1.20.x |
| 1.273+ | 1.19.x |
| 1.269+ | 1.18.x |
| 1.265+ | 1.17.x |
| 1.259+ | 1.15.x |
| 1.257+ | 1.14.x |
| 1.253+ | 1.13.x |
| 1.249+ | 1.12.x |
| 1.243+ | 1.11.x |
| 1.239+ | 1.9.x |
| 1.235+ | 1.8.x |
| 1.233+ | 1.7.x |

## Use OpenTelemetry Python instrumentation

OpenTelemetry for Python provides several instrumentation packages in their [OpenTelemetry Python contributions repositoryï»¿](https://opentelemetry-python-contrib.readthedocs.io/).

Example: Instrument package in a Python Lambda function via instrumentation package

The following code example shows how to instrument [PostgreSQLï»¿](https://www.postgresql.org/) queries in a Python Lambda function by using the [aiopgï»¿](https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/aiopg/aiopg.html) instrumentation package.

```
import json



import aiopg



from opentelemetry.instrumentation.aiopg import AiopgInstrumentor



AiopgInstrumentor().instrument()



def lambda_handler(event, context):



return {



'statusCode': 200,



'body': json.dumps(execute_query())



}



def execute_query():



result = []



with aiopg.connect(database='my_db') as conn:



with conn.cursor() as cur:



cur.execute("SELECT 'hello db';")



for row in cur:



result.append(row)



return result
```

To instrument [boto3ï»¿](https://boto3.readthedocs.io), the AWS SDK for Python, OpenTelemetry provides the [botocoreï»¿](https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/botocore/botocore.html) instrumentation package.

Example: Instrument AWS SDK for Python to monitor a DynamoDB database

The code example below shows how the `botocore` instrumentation can be used to add observability for calls to a [DynamoDBï»¿](https://aws.amazon.com/dynamodb/) database (Dynatrace version 1.244+).

```
import boto3



import json



from opentelemetry.instrumentation.botocore import BotocoreInstrumentor



BotocoreInstrumentor().instrument()



dynamodb = boto3.resource('dynamodb')



table = dynamodb.Table('MyTable')



def lambda_handler(event, handler):



result = table.get_item(Key={'mykey': 42})



return {



"statusCode": 200,



"answer": json.dumps(result.get("Item"))



}
```

![DynamoDB service screen](https://dt-cdn.net/images/dynamodb-python-nodejs-954-c0c7c41ba8.png)

## Use OpenTelemetry Python API

[OpenTelemetry Pythonï»¿](https://github.com/open-telemetry/opentelemetry-python) can be used in an SDK-like approach to trace additional operations that aren't covered by an instrumentation package.

```
import json



from opentelemetry import trace



def lambda_handler(event, context):



tracer = trace.get_tracer(__name__)



with tracer.start_as_current_span("do work"):



# do work



with tracer.start_as_current_span("do some more work") as span:



span.set_attribute("foo", "bar")



# do some more work



return {



'statusCode': 200,



'body': json.dumps('Hello from Hello world from OpenTelemetry Python!')



}
```

These spans are displayed on the **Code level** tab.

![OpenTelemetry lambda](https://dt-cdn.net/images/2021-08-26-17-01-15-1618-ffa40d6d97.png)

## Trace AWS SQS and SNS messages with Python

OneAgent version 1.253+ for SQS OneAgent version 1.257+ for SNS

You can use open-source instrumentation packages to trace AWS SQS and SNS messages and collect them via the Dynatrace AWS Lambda extension.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Install the required dependencies**](#dependencies-python)[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Send an SQS/SNS message**](#send-message-python)[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Receive an SQS/SNS message**](#receive-message-python)

### Step 1 Install the required dependencies

SQS

SNS

```
pip install -U "opentelemetry-api>=1.12" "opentelemetry-instrumentation-boto3sqs>=0.34b0"
```

At this point, [`opentelemetry-instrumentation-boto3sqs`ï»¿](https://pypi.org/project/opentelemetry-instrumentation-boto3sqs/) is a separate package from [`opentelemetry-instrumentation-botocore`ï»¿](https://pypi.org/project/opentelemetry-instrumentation-botocore/). The latter instruments all AWS SDK calls, but lacks enhanced support for SQS.

If you install the dependencies into a Lambda function or layer, you can use the `-t` option to specify a target directory where the installed packages should be copied.

```
pip install -U "opentelemetry-instrumentation-botocore>=0.36b0"
```

### Step 2 Send an SQS/SNS message

The [boto3ï»¿](https://pypi.org/project/boto3/) package is available out of the box if the code runs in AWS Lambda, but you can also install it using `pip install -U boto3`.

This code defining a function named `lambda_handler` can be used

* Inside AWS Lambda (we recommend monitoring it with our AWS Lambda layer)
* Outside AWS Lambda (monitoring is performed with OpenTelemetry and exported to Dynatrace via OTLP/HTTP ingest)

  You might want to remove the function parameters and return value.

SQS

SNS

```
from opentelemetry.instrumentation.boto3sqs import Boto3SQSInstrumentor



Boto3SQSInstrumentor().instrument()



import json



import boto3



from datetime import datetime



QUEUE_URL = "<Your SQS Queue URL>"



sqs = boto3.client("sqs")



def lambda_handler(event, context):



sent = []



for i in range(5):



res = sqs.send_message(QueueUrl=QUEUE_URL, MessageBody=f"hello #{i} at {datetime.now()}")



sent.append(res["MessageId"])



return {



"statusCode": 200,



"body": json.dumps({"produced_messages": sent})



}
```

```
from opentelemetry.instrumentation.botocore import BotocoreInstrumentor



BotocoreInstrumentor().instrument()



import json



import boto3



from datetime import datetime



TOPIC_ARN = "<Your SNS topic ARN>"



sns = boto3.client("sns")



def lambda_handler(event, context):



res = sns.publish(TopicArn=TOPIC_ARN, Message=f"hello at {datetime.now()}")



return {



"statusCode": 200,



"body": json.dumps({"produced_message": res["MessageId"]})



}
```

### Step 3 Receive an SQS/SNS message



SQS

SNS

You can trace SQS messages forwarded from

* **An SQS topic**

  Receiving messages works out of the box when you use an AWS Lambda with an SQS trigger monitored with the Dynatrace AWS Lambda extension. Because a span can have only a single parent, if your Lambda function receives a batch of multiple messages, you need to manually create spans to process every single message if you want to track them separately and have them linked to the sender.

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

  Example: Receive messages with AWS Lambda SQS trigger

  If you invoke the sender and have deployed the example, it will be invoked automatically by SQS.

  ```
  from pprint import pformat



  import boto3



  import json



  from opentelemetry import trace, propagate



  from opentelemetry.semconv.trace import SpanAttributes, MessagingOperationValues



  tracer = trace.get_tracer("lambda-sqs-triggered")



  def lambda_handler(event, context):



  recvcount = 0



  print("Trigger", pformat(event))



  messages = event.get("Records") or ()



  # Lambda SQS event uses lowerCamelCase in its attribute names



  for msg in messages:



  recvcount += 1



  print("Processing", msg["messageId"])



  parent = _extract_parent(msg, from_sns_payload=False)



  with tracer.start_as_current_span("manual-trigger-process", context=parent, kind=trace.SpanKind.CONSUMER, attributes={



  SpanAttributes.MESSAGING_MESSAGE_ID : msg["messageId"],



  SpanAttributes.MESSAGING_URL : msg["eventSourceARN"],



  SpanAttributes.MESSAGING_SYSTEM : msg["eventSource"],



  SpanAttributes.MESSAGING_OPERATION : MessagingOperationValues.PROCESS.value,



  }):



  # ... Here your actual processing would go...



  pass



  print("Processed", recvcount, "messages")



  def _extract_parent(msg, from_sns_payload=False):



  if from_sns_payload:



  try:



  body = json.loads(msg.get("body", "{}"))



  except json.JSONDecodeError:



  body = {}



  carrier = {key: value["Value"] for key, value in body.get("MessageAttributes", {}).items() if "Value" in value}



  else:



  carrier = {key: value["stringValue"] for key, value in msg.get("messageAttributes", {}).items() if "stringValue" in value}



  return propagate.extract(carrier)
  ```

  The resulting path looks as follows:

  ![Distributed trace detail view, showing AWS SQS messages sent, which trigger a Lambda where they are processed.](https://dt-cdn.net/images/triggered-invoke-1636-a740dc26ec.png)

  The invoked Lambda function is a child of one of the messages by which it's triggered. Since there can only be one parent, the other manual-triggerâprocess spans aren't linked directly to the Lambda invocation in which they are handled. Often, there's more than one Lambda invocation node for a batch of messages. In those cases, AWS distributed the batch over multiple Lambda invocations. This can happen even if the messages are delivered within your configured batch window time and number less than your configured batch size.

  Example: Call the SQS receive APIs manually

  If you have deployed the example that uses the `receive` API in code, you need to invoke it manually and it will attempt to read all messages from the queue.

  This example uses the boto3sqs instrumentation. If you don't want to use it, you need to uncomment the `MessageAttributeNames` argument in the `receive_message` function, otherwise, SQS will omit data required to link the message to its sender from the retrieved data.

  This code can also be used outside a Lambda function and [monitored with OpenTelemetry](/docs/ingest-from/opentelemetry/walkthroughs/python "Learn how to instrument your Python application using OpenTelemetry and Dynatrace.") without the Dynatrace AWS Lambda extension.

  ```
  from opentelemetry.instrumentation.boto3sqs import Boto3SQSInstrumentor



  Boto3SQSInstrumentor().instrument()



  from pprint import pformat



  import boto3



  import json



  from opentelemetry import trace, propagate



  from opentelemetry.semconv.trace import SpanAttributes, MessagingOperationValues



  QUEUE_URL = '<Your SQS Queue URL>'



  sqs = boto3.client("sqs")



  tracer = trace.get_tracer("lambda-receive-function")



  def lambda_handler(event, context):



  recvcount = 0



  while True:



  msg_receive_result = sqs.receive_message(



  MaxNumberOfMessages=10,



  QueueUrl=QUEUE_URL,



  WaitTimeSeconds=1, # WaitTime of zero would use sampled receive, may return empty even if there is a message



  # This argument is only required if you do not use the boto3sqs instrumentation:



  #MessageAttributeNames=list(propagate.get_global_textmap().fields)



  )



  print("Received", pformat(msg_receive_result))



  if not msg_receive_result.get('Messages'):



  break



  messages = msg_receive_result.get("Messages")



  # receive result uses PascalCase in its attribute names



  for msg in messages:



  recvcount += 1



  print("Processing", msg["MessageId"])



  parent = _extract_parent(msg, from_sns_payload=False)



  with tracer.start_as_current_span("manual-receive-process", context=parent, kind=trace.SpanKind.CONSUMER, attributes={



  SpanAttributes.MESSAGING_MESSAGE_ID: msg["MessageId"],



  SpanAttributes.MESSAGING_URL: QUEUE_URL,



  SpanAttributes.MESSAGING_SYSTEM: "aws.sqs",



  SpanAttributes.MESSAGING_OPERATION: MessagingOperationValues.PROCESS.value,



  }):



  # ... Here your actual processing would go...



  print("Delete result", sqs.delete_message(



  QueueUrl=QUEUE_URL,



  ReceiptHandle=msg['ReceiptHandle'],



  ))



  print("Processed", recvcount, "messages")



  def _extract_parent(msg, from_sns_payload=False):



  if from_sns_payload:



  try:



  body = json.loads(msg.get("Body", "{}"))



  except json.JSONDecodeError:



  body = {}



  carrier = {key: value["Value"] for key, value in body.get("MessageAttributes", {}).items() if "Value" in value}



  else:



  carrier = {key: value["StringValue"] for key, value in msg.get("MessageAttributes", {}).items() if "StringValue" in value}



  return propagate.extract(carrier)
  ```

  Creating the `manual-receive-process` span manually is necessary because the boto3sqs instrumentation doesn't set the sender as a parent for the processing span, but uses [OpenTelemetry linksï»¿](https://opentelemetry.io/docs/concepts/signals/traces/#span-links), which are currently not supported by Dynatrace. For the `manual-receive-process` span linking to work correctly, you need to configure the Dynatrace AWS Lambda extension to allow setting parent spans manually. See the [previous example](#py-sqs-trigger) for guidance.

  Invoking first the code that sends SQS messages, then the manual receive code, deployed as Lambda functions, results in two traces:

  + The first trace shows the flow of the message from the sender to the processor:

    ![Distributed trace detail view, showing AWS SQS messages sent and processed in another process.](https://dt-cdn.net/images/sdk-send-process-1643-dc267e8011.png)

    There are additional `Requests to public networks` nodes because the boto3 package uses HTTP requests to send SQS messages, which are captured by Dynatrace HTTP instrumentation.

    You'll notice that the invocation and receive node of the second Lambda invocation are missing from this trace, even though the `manual-receive-process` nodes are there. This is because the Lambda function was triggered independently of the message flow, and just happened to receive the message as part of its handler code.
  + The second trace in Dynatrace shows the Lambda invocation until it's cut in two by setting the explicit parent:

    ![Distributed trace detail view, showing AWS SQS messages received with the Python boto3 SDK.](https://dt-cdn.net/images/sdk-receive-1637-72b227938f.png)
* **An SNS topic**

  For SNS messages that are forwarded to SQS, the message format depends on the [raw message deliveryï»¿](https://docs.aws.amazon.com/sns/latest/dg/sns-large-payload-raw-message-delivery.html) configuration on the SNS subscription.

AWS Lambda functions that are triggered by SNS are supported out of the box when monitored with the Dynatrace AWS Lambda extension.

SNS topics can be configured via a subscription to forward messages to an SQS queue. Messages in the SQS queue can then be consumed by a Lambda function. Tracing the received messages in the SQS-triggered AWS Lambda function works out of the box when AWS Lambda is monitored with the Dynatrace AWS Lambda extension. However, the tracer can only select a single parent, and if your Lambda function receives batches of multiple messages, special handling is required to track each message separately.

For details, see how to [receive an SQS message](#receive-sqs-python).

## Related topics



* [OpenTelemetry interoperability](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability "Enable and use OpenTelemetry interoperability in AWS Lambda.")
* [Trace Python, Node.js, and Java Lambda functions](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension "Monitor Lambda functions written in Python, Node.js, and Java.")