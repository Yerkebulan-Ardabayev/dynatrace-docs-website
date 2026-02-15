---
title: Trace Python, Node.js, and Java Lambda functions
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension
scraped: 2026-02-15T09:05:59.697710
---

# Trace Python, Node.js, and Java Lambda functions

# Trace Python, Node.js, and Java Lambda functions

* How-to guide
* 14-min read
* Updated on Jan 23, 2026

This page refers to the classic AWS Lambda integration. For the latest version, see [Trace Lambda functions](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/trace-lambda-functions "Monitor AWS Lambda functions.").

Dynatrace provides you with a dedicated AWS Lambda layer that contains the Dynatrace extension for AWS Lambda. You need to add the publicly available layer for your runtime and region to your function. Then, based on your configuration method, Dynatrace provides a template or configuration for your AWS Lambda function.

## Incoming invocations

Dynatrace can monitor incoming invocations only if they are invoked via:

* AWS SDK Lambda Invoke API
* API gateway
* Lambda function URL
* AWS SQS
* AWS SNS

For other invocation types, OneAgent can't capture any specific information or connect the trace to any parent. Invocations via the AWS SDK require the client to be instrumented with Dynatrace to connect the trace.

## Prerequisites

* A supported AWS Lambda [runtime](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration#support-lifecycle "AWS Lambda capabilities and integration options"). The Dynatrace extension supports AWS Lambda functions written in **Node.js**, **Python**, or **Java**.
  Both **64-bit ARM** ([AWS Graviton2 processorsï»¿](https://aws.amazon.com/ec2/graviton/)) and **64-bit x86** architectures are supported.
* Java The following RAM requirements need to be met:

  + If [Lambda SnapStartï»¿](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) is enabled and OneAgent version is 1.267+, memory needs to be set to a minimum of 512 MB.
  + If [Lambda SnapStartï»¿](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) is not enabled and OneAgent version is 1.265 or earlier, memory needs to be set to a minimum of 1,500 MB.
    To configure memory in the AWS Lambda console, go to **General** > **Basic settings** and set **Memory**.

  A new configuration of the memory size affects the amount of virtual CPU available to the function; to learn more about it, see [Monitoring overhead](#monitoring-overhead) below.

  + Note that the RAM requirements for Node.js and Python Lambda functions might be significantly lower. The compute power in AWS Lambda scales with the allocated memory, and with low memory settings the function execution time becomes much slower.
* Activate the **Forward Tag 4 trace context extension** OneAgent feature. Go to **Settings** > **Preferences** > **OneAgent features**.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Enable AWS Lambda**](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#activate-aws-lambda "Monitor Lambda functions written in Python, Node.js, and Java.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Choose a configuration method**](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-method "Monitor Lambda functions written in Python, Node.js, and Java.")[![Step 3 optional](https://dt-cdn.net/images/dotted-step-3-e2082c1921.svg "Step 3 optional")

**Specify a Dynatrace API endpoint**](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-endpoint "Monitor Lambda functions written in Python, Node.js, and Java.")[![Step 4 optional](https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Step 4 optional")

**Enable Real User Monitoring**](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-rum "Monitor Lambda functions written in Python, Node.js, and Java.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Define an AWS layer name**](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-layer "Monitor Lambda functions written in Python, Node.js, and Java.")[![Step 6 optional](https://dt-cdn.net/images/dotted-step-6-fbd29ea893.svg "Step 6 optional")

**Deployment**](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#deployment "Monitor Lambda functions written in Python, Node.js, and Java.")[![Step 7](https://dt-cdn.net/images/step-7-35139ef2d6.svg "Step 7")

**Configuration options**](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#config-options "Monitor Lambda functions written in Python, Node.js, and Java.")[![Step 8](https://dt-cdn.net/images/step-8-72c2162189.svg "Step 8")

**Dynatrace AWS integration**](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#aws-integration "Monitor Lambda functions written in Python, Node.js, and Java.")

## Step 1 Enable AWS Lambda

To get started

1. In Dynatrace Hub, select **AWS Lambda**.
2. Select **Set up**.

3. Follow the instructions to enable monitoring of AWS Lambda functions.

## Step 2 Choose a configuration method

Dynatrace OneAgent is distributed as a Lambda layer that can be enabled and configured manually or using well-known Infrastructure as Code (IaC) solutions.
The Lambda layer is stored in the Dynatrace AWS account `725887861453`.

On the **Enable Monitoring for AWS Lambda Functions** page, use the **How will you configure your AWS Lambda functions?** list to select your preferred method, and then make sure you set all properties for the selected method before copying the generated configuration snippets.

Configure with JSON file

If you select this method, Dynatrace provides you with:

* An environment variable to add to your AWS Lambda function
* A JSON snippet that you need to copy into the `dtconfig.json` file in the root folder of your Lambda deployment
* Lambda layer ARN

When using this method, make sure that you add the Dynatrace Lambda layer to your function. You can do this through the AWS console (**Add layer** > **Specify an ARN** and paste the ARN displayed on the deployment page) or by using an automated solution of your choice.

**Enter environment variables via the AWS Console**

![Lambda environment variables cropped](https://dt-cdn.net/images/lambda-environment-variables-cropped-776-af551d0520.png)

**Enter the Lambda layer ARN via the AWS Console**

![Specify a layer by providing the ARN](https://dt-cdn.net/images/lambda-add-layer-822-ab8535b8d9.jpg)

Configure with environment variables

When using this method, make sure that you add the Dynatrace Lambda layer to your function. The layer, as well as the environment variables, can be set either manually through the AWS console (**Add layer** > **Specify an ARN** and paste the ARN displayed on the deployment page) or by using an automated solution of your choice.

[Client-side decryption of environment variables (Security in Transit)ï»¿](https://dt-url.net/tz234sd) is not supported.

If you select this method, Dynatrace provides you with:

* Values to define environment variables for the AWS Lambda functions that you want to monitor

  ![Lambda environment variables](https://dt-cdn.net/images/lambda-env-variables-1614-77850f4051.png)
* Lambda layer ARN

  ![Specify a layer by providing the ARN](https://dt-cdn.net/images/lambda-add-layer-822-ab8535b8d9.jpg)

Configure and deploy using Terraform

Terraform is a popular Infrastructure as Code (IaC) solution. If you select this method, Dynatrace provides you with:

* A template to define the AWS Lambda function. This includes all the configuration that you need to deploy and configure the Dynatrace AWS Lambda extension together with your functions.
* Lambda layer ARN

Configure and deploy using AWS SAM

The AWS Serverless Application Model (SAM) is an open-source framework for building serverless applications.

If you select this method, Dynatrace provides you with a template to define the AWS Lambda function. This includes all the configuration that you need to integrate the Dynatrace AWS Lambda extension.

Configure and deploy using the serverless framework

The Serverless Application option is a framework for deploying serverless stacks.

If you select this method, Dynatrace provides you with a template to define the AWS Lambda function. This includes all the configuration that you need to integrate the Dynatrace AWS Lambda extension.

Configure and deploy using AWS CloudFormation

AWS CloudFormation is an IaC solution that enables provisioning of a wide range of AWS services.

If you select this method, Dynatrace provides you with a template to define the AWS Lambda function. This includes all the configuration that you need to integrate the Dynatrace AWS Lambda extension.

## Step 3 optional Specify a Dynatrace API endpoint Optional

This is an optional step that enables you to specify a Dynatrace API endpoint to which monitoring data will be sent.

The typical scenario is to deploy a Dynatrace ActiveGate in close proximity (the same region) to the Lambda functions that you want to monitor in order to reduce network latency, which can impact the execution and cold start time of your Lambda functions for, usually, one network request by OneAgent per Lambda invocation (which happens at the end of the invocation). See the [Monitoring overhead](#monitoring-overhead) section for typical overhead numbers.

## Step 4 optional Enable Real User Monitoring Optional

This is an optional step to use Real User Monitoring (RUM), which provides you with deep insights into user actions and performance via the browser or in mobile apps.

### Configure AWS

* Make sure the `x-dtc` header is allowed in the CORS settings of your monitored Lambda functions.

  RUM for Lambda functions requires a specific header (`x-dtc`) to be sent with XHR calls to AWS. To enable it, the CORS settings of your AWS deployment must allow the `x-dtc` header during preflight (`OPTIONS`) requests. To configure CORS and allow the `x-dtc` header for your specific setup, see [Enable CORS on a resource using the API Gateway consoleï»¿](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-cors-console.html) in AWS documentation.

### Configure Dynatrace

To configure the `x-dtc` header for calls to your Lambda functions

1. Go to **Web**, **Mobile**, **Frontend**, or **Custom Applications**, depending on your application type.
2. Select the application you want to connect with your Lambda function.
3. Select the browse menu (**â¦**) in the upper-right corner and select **Edit**.
4. Select **Capturing** > **Async web requests and SPAs**.
5. Make sure that your framework of choice is enabled. If your framework is not listed, enable **Capture XmlHttpRequest (XHR)** for generic support of `XHR`.
6. Select **Capturing** > **Advanced setup**.
7. Scroll down to the **Enable Real User Monitoring for cross-origin XHR calls** section and enter a pattern that matches the URL to your Lambda functions. Example: `TheAwsUniqueId.execute-api.us-east-1.amazonaws.com`
8. Select **Save**. After a few minutes, the header will be attached to all calls to your Lambda function and requests from your browser will be linked to the backend.

Failed requests

If requests start failing after enabling this option, review your CORS settings. To learn how to configure CORS, see [Enable CORS on a resource using the API Gateway consoleï»¿](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-cors-console.html) in AWS documentation.

![Service Flow for AWS Lambda function](https://dt-cdn.net/images/aws-lambda1-service-flow-1430-f09d3a9ebe.png)

## Step 5 Define an AWS layer name

Select the AWS region and the runtime of the Lambda function to be monitored. These settings are required to provide the correct layer ARN.

## Step 6 Deployment

Copy the configuration snippets into your deployment and use your deployment method of choice to enable the layer and set the configuration for your Lambda functions.

## Step 7 Configuration options

### Configure the AWS API Gateway

* If inbound (non-XHR) requests to your Lambda functions are not connected to the calling application, configure the API Gateway to pass through the Dynatrace tag. To do this, enable **Use Lambda Proxy Integration** on the **Integration Request** configuration page of the API Gateway.
* If the API Gateway is configured from the Lambda configuration page, this setting will be enabled by default. For more information, see [Enable CORS on a resource using the API Gateway consoleï»¿](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-cors-console.html).

AWS Lambda also supports [**non-proxy integration**ï»¿](https://dt-url.net/8u03rh3), whichâwithout some additional configurationâprevents Dynatrace from

* Tracing calls from other monitored applications
* [RUM](/docs/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.") detection (web and mobile)

Node.jsPython To make tracing calls from other monitored applications/RUM detection work in this scenario, create a custom mapping template in the integration requests configuration.

1. In the AWS API Gateway Console, go to **Resources** and select a request method (for example, **GET**).
2. Select **Mapping Templates** and then select **Add mapping template**.
3. Add the following content to the template:

   ```
   {



   "path": "$context.path",



   "httpMethod": "$context.httpMethod",



   "headers": {



   #foreach($param in ["x-dynatrace", "traceparent", "tracestate", "x-dtc", "referer", "host", "x-forwarded-proto", "x-forwarded-for", "x-forwarded-port"])



   "$param": "$util.escapeJavaScript($input.params().header.get($param))"



   #if($foreach.hasNext),#end



   #end    },



   "requestContext": {



   "stage": "$context.stage"



   }



   }
   ```

   The `x-dtc` header is specific to tracing RUM scenarios, whereas the remaining headers are generally needed to link traces together and extract relevant information, such as web request metadata.
4. Select **Save** to save your configuration.
5. Redeploy your API.

### Fetch token from AWS Secrets Manager

OneAgent version 1.295+

Instead of specifying the authentication token explicitly in the configuration, you can configure OneAgent to fetch a token stored in [AWS Secrets Managerï»¿](https://dt-url.net/r403pii).

Prerequisites

* Make sure you granted the `secretsmanager:GetSecretValue` permission for the authentication token secret ARN to the Lambda function monitored by OneAgent. For details, see [Authentication and access control for AWS Secrets Managerï»¿](https://dt-url.net/7n03p10) in the AWS Secrets Manager documentation.
* Make sure the secret value contains only the plaintext authentication token value (without quotes). Note that

  + Secrets with JSON structure are not supported. For details, see [Create an AWS Secrets Manager secretï»¿](https://dt-url.net/fy23pdx) in the AWS Secrets Manager documentation.
  + When you retrieve the secret value, Secrets Manager returns by default only the current secret version (`AWSCURRENT` label). For details, see [What's in a Secrets Manager secret?ï»¿](https://dt-url.net/1f43pq8) in the AWS Secrets Manager documentation.

To fetch the token for a tracing connection, set the token secret ARN either to the environment variable `DT_CONNECTION_AUTH_TOKEN_SECRETS_MANAGER_ARN` or the JSON property `Connection.AuthTokenSecretsManagerArn`.

This option always overrides `DT_CONNECTION_AUTH_TOKEN` (`Connection.AuthToken`). If the fetch fails, OneAgent won't be able to export trace data.

A fetch accesses AWS Secrets Manager only once, during the Lambda function's initialization phase; this causes an increase of the Lambda function's cold start duration.

The Node.js and Python layers use the AWS SDK version provided by the AWS Lambda runtime to access the secret.

To [fetch the token for log collection](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/collector#aws-secrets-manager "Collect logs from AWS Lambda functions"), set another fetch.

### Filter cold starts

One of the important metrics for Lambda is the frequency of cold starts. A cold start happens when a new instance of a Lambda function is invoked. Such cold starts take longer and add latency to your requests.

A high cold-start frequency can indicate errors or an uneven load pattern that can be mitigated using provisioned concurrency. Dynatrace reports such cold starts as a property on the distributed trace.

To analyze cold starts, select **View all requests** on the Lambda service details page.

![Service details page for AWS Lambda function](https://dt-cdn.net/images/aws-lambda4-requests-936-7d63249911.png)

In the request filter, select **Function cold start** in the **Request property** section.

This displays a page that you can filter by invocations containing **Only cold start** or **No cold start**.

![Screen to filter by invocations containing a Only cold start or No cold start](https://dt-cdn.net/images/aws-lambda6-cold-starts-1430-4ec4dd6209.png)

### Monitoring overhead

Enabling monitoring unavoidably induces overhead to the monitored function execution. Overhead depends on several factors, such as function runtime technology, configuration, and concrete function characteristics such as code size or execution duration and complexity.

The amount of memory configured for a function directly impacts the compute resources assigned to the function instance. For more details, see [Memory and computing powerï»¿](https://docs.aws.amazon.com/lambda/latest/operatorguide/computing-power.html).

The worst-case scenario on measured overhead is a function with an empty function handler and minimum memory configuration.

#### Cold start overhead

* For **Python**, cold start overhead is about 1,000 ms.
* For **Node.js**, cold start overhead is about 700 ms.
* For **Java**, cold start overhead may exceed 1,000 ms.

For the cold start benchmarking process, hello-world functions (only returning a response) were tested with 512 MB of allocated memory. It is important to note that the observed overhead may vary based on a few factors:

* **Configured memory**: A Lambda function is allocated CPU proportional to the [memory configuredï»¿](https://dt-url.net/4w022aa) which can influence its cold start performance. Functions with higher memory allocations typically exhibit faster initialization times due to the increased CPU allocation.
* **Function implementation**: The complexity of the actual function implementationâincluding external dependencies, initialization logic, and the runtime environmentâcan significantly impact the cold start duration.
* **Runtime version**: The specific runtime version or container image used can also influence cold start times.

When conducting performance evaluations, we recommend considering these factors, as they may affect the benchmarking results in real-world scenarios.

For the minimum memory configuration requirement, see [Requirement for Java Lambda functions](#lambda-java-rt-mem-limit).

#### Response time latency

Latency depends on the function implementation, but is typically less than 10%. This means that the time it takes until the caller of a Lambda function receives a response might increase by 10% when the OneAgent layer is added, compared to when OneAgent is not active/present.

#### Code space overhead

The following table contains uncompressed layer sizes.

| Runtime | Code space (MB) | Code space with log collector included (MB) |
| --- | --- | --- |
| Node.js | ~1MB | ~16MB |
| Python | ~3MB | ~18MB |
| Java | ~5MB | ~20MB |

## Step 8 Dynatrace AWS integration

While not mandatory, we recommend that you set up Dynatrace Amazon CloudWatch integration. This allows data ingested via AWS integration to be seamlessly combined with the data collected by the Dynatrace AWS Lambda extension.

![AWS Lambda metrics Invocations](https://dt-cdn.net/images/aws-lambda3-metric-936-b279d25a8e.png)

## Known limitations

* The Dynatrace AWS Lambda extension does not support the capture of [method-level request attributes](/docs/observe/application-observability/services/request-attributes/capture-request-attributes-based-on-method-arguments "Learn how to create request attributes based on Java, .NET, or PHP method arguments and how to use them on the serviceâs overview page. Also find out how you can aggregate the captured values of request attributes as well as how you can access objects, in case the value to be captured is a complex object.").
* Most Dynatrace AWS Lambda extensions don't capture IP addresses of outgoing HTTP requests. This results in **unmonitored hosts** if the called service isn't monitored with Dynatrace.
* Getting auth token from AWS Secrets Manager is not supported if [Lambda SnapStartï»¿](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) is enabled.
* **Outgoing requests to another AWS Lambda function:** In a monitored AWS Lambda function, the following libraries are supported for outgoing requests to another AWS Lambda function:

  + For Java: AWS SDK version 1 for Java
  + For Node.js: AWS SDK for JavaScript in Node.js:

    - [version 2ï»¿](https://www.npmjs.com/package/aws-sdk)
    - [version 3ï»¿](https://github.com/aws/aws-sdk-js-v3) (OneAgent version 1.263+)
  + For Python: AWS SDK for Python (Boto3)
* **Outgoing HTTP requests:** In a monitored AWS Lambda function, the following libraries/HTTP clients are supported for outgoing HTTP requests:

  + For Java: Apache HTTP Client 3.x, 4.x
  + For Node.js:

    - Built-in [`http.request`ï»¿](https://nodejs.org/api/http.html#http)
    - Built-in [`fetch API`ï»¿](https://nodejs.org/docs/latest/api/globals.html#fetch) (OneAgent version 1.285+)
  + For Python: `requests`, `aiohttp-client`, `urllib3`, `redis-py` (OneAgent version 1.289+)
* **Additional requirements for incoming calls for Java only:**
  To correctly monitor the configured handler method

  + The configured handler class has to implement the handler method by itself. If the handler method is only defined in a base class, you have to add an override in the handler class, calling the base handler method within (usually `super.handleRequest(...)`).
  + The handler method has to have a `Context` ([`com.amazonaws.services.lambda.runtime.Context`ï»¿](https://github.com/aws/aws-lambda-java-libs/blob/main/aws-lambda-java-core/src/main/java/com/amazonaws/services/lambda/runtime/Context.java)) parameter.
  + We recommend [following best practiceï»¿](https://docs.aws.amazon.com/lambda/latest/dg/java-handler.html) by deriving your Lambda handler class from [com.amazonaws.services.lambda.runtime.RequestHandlerï»¿](https://github.com/aws/aws-lambda-java-libs/blob/main/aws-lambda-java-core/src/main/java/com/amazonaws/services/lambda/runtime/RequestHandler.java) overrriding `handleRequest` and configuring that as handler method.
    However, as long as the previous requirements are fulfilled, OneAgent supports any valid handler function, even if not derived from that base interface.
  + The [AWS Lambda events libraryï»¿](https://github.com/aws/aws-lambda-java-libs/tree/master/aws-lambda-java-events) must be used by your function as the types defined in the `com.amazonaws.services.lambda.runtime.events` package are used by OneAgent to match the corresponding [invocation types for incoming calls](#incoming-calls-types).
* **Node.js sensors and instrumentations for ES modules:**

  + The Node.js AWS Lambda extension sensors (instrumentations) don't support ECMAScript modules. This means that the extension won't properly monitor outgoing calls (for example, HTTP or AWS SDK requests).
  + OpenTelemetry instrumentations don't support ECMAScript modules by default.

    There is a way to make OpenTelemetry instrumentations work with ECMAScript modules, but it's experimental and has some limitations. For details, [Instrumentation for ES Modules In NodeJS (experimental)ï»¿](https://dt-url.net/r10379k).
* [AWS Lambda Managed Instancesï»¿](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances.html) deployment mode is not supported. This new hosting option allows deploying Lambda functions on AWS-managed EC2 instance clusters. The Dynatrace Lambda extension and code module layers currently do not support this deployment mode.

## Related topics

* [Limit API calls to AWS using tags](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/limit-api-calls-to-aws-using-tags "Add and configure AWS tags to limit AWS resources.")