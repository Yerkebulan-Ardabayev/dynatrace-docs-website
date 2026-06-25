---
title: Trace Lambda functions
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/trace-lambda-functions
scraped: 2026-05-12T11:22:50.161523
---

# Trace Lambda functions

# Trace Lambda functions

* How-to guide
* 8-min read
* Updated on Apr 23, 2026

Dynatrace provides you with a dedicated AWS Lambda layer that contains the Dynatrace extension for AWS Lambda. You need to add the publicly available layer for your runtime and region to your function. Then, based on your configuration method, Dynatrace provides a template or configuration for your AWS Lambda function.

## Capabilities

Dynatrace provides extensive Python, Node.js, Java, and Go monitoring capabilities:

* Automatic distributed tracing across AWS services such as [API Gateway](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-api-gateway "Monitor Amazon API Gateway and view available metrics."), [SQS](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-simple-queue-service-sqs "Monitor Amazon Simple Queue Service (Amazon SQS) and view available metrics."), [SNS](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-simple-notification-service-sns "Monitor Amazon Simple Notification Service (Amazon SNS) and view available metrics.") and seamless integration with other AWS services. For more details, refer to [AWS Lambda integration](/managed/ingest-from/amazon-web-services/integrate-into-aws "Learn how to integrate Dynatrace into AWS platform.").

* OpenTelemetry support for trace and metric ingestion.
* Native log ingestion from Lambda functions. Dynatrace supports log ingestion directly via the AWS Lambda Telemetry API, reducing dependency on CloudWatch. For more details, refer to [AWS Lambda log collection](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/collector "Collect logs from AWS Lambda functions").
* [Cold start](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/trace-lambda-functions#filter-cold-start "Monitor AWS Lambda functions.") detection and optimization.
* Infrastructure-as-Code support (Terraform, AWS SAM, Serverless Framework).

See our [supported technologies matrix](/managed/ingest-from/technology-support#aws-monitor-hub "Find technical details related to Dynatrace support for specific platforms and development frameworks.") for details on supported frameworks and [runtimesï»¿](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html) for AWS supported runtimes.

### Incoming invocations

For AWS Lambda invocations, Dynatrace offers generic support for all trigger types. OneAgent can capture specific information or connect the trace to any parent and therefore add additional information only for invocations made via:

* AWS SDK Lambda Invoke API
* API gateway
* Lambda function URL
* AWS SQS
* AWS SNS
* AWS Application Load Balancer

For other invocation types, OneAgent can't capture any specific information or connect the trace to any parent. Invocations via the AWS SDK require the client to be instrumented with Dynatrace to connect the trace.

## Steps

### Enable monitoring for AWS Lambda functions

To get started

1. Go to **Deploy Dynatrace**.
2. Select **Start installation** > **AWS Lambda**.

3. Follow the instructions to enable monitoring of AWS Lambda functions.

#### Choose a configuration method

Dynatrace OneAgent is distributed as a Lambda layer that can be enabled and configured manually or using well-known Infrastructure as Code (IaC) solutions.
The Lambda layer is stored in the Dynatrace AWS account `585768157899`.

The wizard provides you with various configuration options and configuration snippets you can use in your deployment automation of choice.

Configure with JSON file

If you select this method, Dynatrace provides you with:

* An environment variable to add to your AWS Lambda function
* A JSON snippet that you need to copy into the `dtconfig.json` file in the root folder of your Lambda deployment
* Lambda layer ARN

When using this method, make sure that you add the Dynatrace Lambda layer to your function. You can do this through the AWS console (**Add layer** > **Specify an ARN** and paste the ARN displayed on the deployment page) or by using an automated solution of your choice.

**Enter environment variables via the AWS Console**

![Lambda environment variables cropped](https://dt-cdn.net/images/lambda-environment-variables-cropped-776-af551d0520.png)

Lambda environment variables cropped

**Enter the Lambda layer ARN via the AWS Console**

![Specify a layer by providing the ARN](https://dt-cdn.net/images/lambda-add-layer-822-ab8535b8d9.jpg)

Specify a layer by providing the ARN

Configure with environment variables

Environment variables can be used for configuration, but we advise using the Secrets Manager as the recommended approach for fetching a security token. For more details, refer to [Fetch token from AWS Secrets Manager](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/trace-lambda-functions#aws-secrets-manager "Monitor AWS Lambda functions.").

When using this method, make sure that you add the Dynatrace Lambda layer to your function. The layer, as well as the environment variables, can be set either manually through the AWS console (**Add layer** > **Specify an ARN** and paste the ARN displayed on the deployment page) or by using an automated solution of your choice.

[Client-side decryption of environment variables (Security in Transit)ï»¿](https://dt-url.net/tz234sd) is not supported.

If you select this method, Dynatrace provides you with:

* Values to define environment variables for the AWS Lambda functions that you want to monitor

  ![AWS Lambda environment variables](https://dt-cdn.net/images/lambda-env-variables-updated-1614-488fcb4f1c.png)

  AWS Lambda environment variables
* Lambda layer ARN

  ![Specify a layer by providing the ARN](https://dt-cdn.net/images/lambda-add-layer-822-ab8535b8d9.jpg)

  Specify a layer by providing the ARN

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

#### Specify a Dynatrace API endpoint

Required

Specify a public Dynatrace API endpoint to which monitoring data will be sent.

It must be an ActiveGate-based URL with environment ID (for example, `https://<public-active-gate>:9999/e/<environment-id>`)

The typical scenario is to deploy a Dynatrace ActiveGate in close proximity (same region) to the Lambda functions that you want to monitor in order to reduce network latency, which can impact the execution and cold start time of your Lambda functions for (usually one) network request by OneAgent per Lambda invocation (which happens at the end of the invocation). See <#monitoring-overhead> section for typical overhead numbers.

### Enable Real User Monitoring

Optional

This is an optional step to use Real User Monitoring (RUM), which provides you with deep insights into user actions and performance via the browser or in mobile apps.

#### Configure the AWS API Gateway

* If inbound (non-XHR) requests to your Lambda functions are not connected to the calling application, configure the API Gateway to pass through the Dynatrace tag. To do this, enable **Use Lambda Proxy Integration** on the **Integration Request** configuration page of the API Gateway.
* If the API Gateway is configured from the Lambda configuration page, this setting will be enabled by default. For more information, see [Enable CORS on a resource using the API Gateway consoleï»¿](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-cors-console.html).

AWS Lambda also supports [**non-proxy integration**ï»¿](https://dt-url.net/8u03rh3), whichâwithout some additional configurationâprevents Dynatrace from

* Tracing calls from other monitored applications
* [RUM](/managed/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.") detection (web and mobile)

To make tracing calls from other monitored applications/RUM detection work in this scenario, create a custom mapping template in the integration requests configuration.

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

#### Configure AWS

Make sure the `x-dtc` header is allowed in the CORS settings of your monitored Lambda functions.

RUM for Lambda functions requires a specific header (`x-dtc`) to be sent with XHR calls to AWS. To enable it, the CORS settings of your AWS deployment must allow the `x-dtc` header during preflight (`OPTIONS`) requests. To configure CORS and allow the `x-dtc` header for your specific setup, see [Enable CORS on a resource using the API Gateway consoleï»¿](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-cors-console.html) in AWS documentation.

#### Configure Dynatrace

To configure the `x-dtc` header for calls to your Lambda functions

1. Go to **Web**, **Mobile**, **Frontend**, or **Custom Applications**, depending on your application type.
2. Select the application you want to connect with your Lambda function.
3. Select the browse menu (**â¦**) in the upper-right corner and select **Edit**.
4. Select **Capturing** > **Async web requests and SPAs**.
5. Make sure that your framework of choice is enabled. If your framework is not listed, enable **Capture XmlHttpRequest (XHR)** for generic support of `XHR`.
6. Select **Capturing** > **Advanced setup**.
7. Scroll down to the **Enable Real User Monitoring for cross-origin XHR calls** section and enter a pattern that matches the URL to your Lambda functions. For example: `TheAwsUniqueId.execute-api.us-east-1.amazonaws.com`
8. Select **Save**. After a few minutes, the header will be attached to all calls to your Lambda function and requests from your browser will be linked to the backend.

Failed requests

If requests start failing after enabling this option, review your CORS settings. To learn how to configure CORS, see [Enable CORS on a resource using the API Gateway consoleï»¿](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-cors-console.html) in AWS documentation.

### Deployment

Copy the configuration snippets into your deployment and use your deployment method of choice to enable the layer and set the configuration for your Lambda functions.

### Configuration options

#### Fetch token from AWS Secrets Manager

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

For details on fetching the token for log collection, refer to [Fetch token from AWS Secrets Manager](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/collector#aws-secrets-manager "Collect logs from AWS Lambda functions").

## Monitoring overhead

Enabling monitoring unavoidably induces overhead to the monitored function execution. Overhead depends on several factors, such as function runtime technology, configuration, and concrete function characteristics such as code size or execution duration and complexity.

The amount of memory configured for a function directly impacts the compute resources assigned to the function instance. For more details, see [Memory and computing powerï»¿](https://docs.aws.amazon.com/lambda/latest/operatorguide/computing-power.html).

The worst-case scenario on measured overhead is a function with an empty function handler and minimum memory configuration.

### Cold start overhead

* For **Node.js**, cold start overhead is about 900 ms.
* For **Java**, cold start overhead is about 1,500 ms.
* For **Python**, cold start overhead is about 1,000 ms.
* For **Go**, cold start overhead is about 600 ms.

For the cold start benchmarking process, hello-world functions (only returning a response) were tested with 512 MB of allocated memory. It is important to note that the observed overhead may vary based on a few factors:

* **Configured memory**: A Lambda function is allocated CPU proportional to the [memory configuredï»¿](https://dt-url.net/4w022aa) which can influence its cold start performance. Functions with higher memory allocations typically exhibit faster initialization times due to the increased CPU allocation.
* **Function implementation**: The complexity of the actual function implementationâincluding external dependencies, initialization logic, and the runtime environmentâcan significantly impact the cold start duration.
* **Runtime version**: The specific runtime version or container image used can also influence cold start times.

When conducting performance evaluations, we recommend considering these factors, as they may affect the benchmarking results in real-world scenarios.

### Response time latency

Latency depends on the function implementation, but is typically less than 10%. This means that the time it takes until the caller of a Lambda function receives a response might increase by 10% when the OneAgent layer is added, compared to when OneAgent is not active/present.

### Code space overhead

The following table contains uncompressed layer sizes.

| Runtime | Code space | Code space with log collector included |
| --- | --- | --- |
| Node.js | ~23 MB | ~32 MB |
| Java | ~25 MB | ~32 MB |
| Python | ~16 MB | ~24 MB |
| Go | ~25 MB | ~28 MB |

## Dynatrace AWS integration

While not mandatory, we recommend that you set up Dynatrace Amazon CloudWatch integration. This allows data ingested via AWS integration to be seamlessly combined with the data collected by the Dynatrace AWS Lambda extension.

For more details, refer to [Amazon CloudWatch Metric Streams](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-metrics-ingest/cloudwatch-metric-streams "Ingest metrics from your AWS accounts using Amazon CloudWatch Metric Streams.").

## Filter cold starts

One of the important metrics for Lambda is the frequency of cold starts. A cold start happens when a new instance of a Lambda function is invoked. Such cold starts take longer and add latency to your requests.

A high cold-start frequency can indicate errors or an uneven load pattern that can be mitigated using provisioned concurrency. Dynatrace reports such cold starts as a property on the distributed trace.

To analyze cold starts

1. Select **View all requests** on the Lambda service details page.

2. In the request filter, select **Function cold start** in the **Request property** section.

3. Filter by invocations containing **Only cold start** or **No cold start**.

## Known limitations

### General limitations

* HTTP connect timeouts, flush timeouts, and backoff thresholds are not configurable.
* OneAgent running on AWS Lambda does not support functionalities that require OneAgent reconfiguration through the server-side user interface.
* OneAgent for AWS Lambda uses only local settings defined via environment variables or config files, instead of pulling configuration from the Dynatrace cluster. As a result, any settings defined at the cluster level are ignored, and defaults apply unless explicitly overridden.
* Most Dynatrace AWS Lambda extensions don't capture IP addresses of outgoing HTTP requests. This results in **unmonitored hosts** if the called service isn't monitored with Dynatrace.
* [AWS Lambda Managed Instancesï»¿](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances.html) deployment mode is not supported. This new hosting option allows deploying Lambda functions on AWS-managed EC2 instance clusters. The Dynatrace Lambda extension and code module layers currently do not support this deployment mode.

### .NET limitations

* .NET: ASP.NET core, code-level attack & vulnerability evaluation and several metrics are not supported within AWS Lambda.

### Node.js limitations

* `aws-sdk` tracing support is available for CommonJS only. ECMAScript Lambda deployments will not have AWS-SDK tracing available.
* You must enable monitoring for ESM Lambda functions. This feature is currently `opt-in`. To enable ESM Support for incoming AWS Lambda invocations, set the `DT_ENABLE_ESM_LOADERS` environment variable to `true`. Enabling ESM support increases memory consumption.
* Node.js handlers from bundlers (for example, [esbuildï»¿](https://esbuild.github.io/) or [viteï»¿](https://vite.dev/)) might not be visible to OneAgent because of the modified export structure through the bundling process.

  How to enable auto-instrumentation for Node.js handlers bundled via a bundler

  You can use a simple wrapper script to enable auto-instrumentation.

  Here's a sample AWS Lambda handler written in TypeScript (`index.ts`):

  ```
  import { Context, APIGatewayProxyResult, APIGatewayEvent } from 'aws-lambda';



  export const handler = async (event: APIGatewayEvent, context: Context): Promise<APIGatewayProxyResult> => {



  console.log(`Event: ${JSON.stringify(event, null, 2)}`);



  console.log(`Context: ${JSON.stringify(context, null, 2)}`);



  return {



  statusCode: 200,



  body: JSON.stringify({



  message: 'hello world',



  }),



  };



  };
  ```

  1. Bundle the function code using the bundler of your choice.
  2. If this results in code that cannot be automatically instrumented by OneAgent, create a wrapper file (for example, `handler_wrap.mjs`) to expose the handler in a way that OneAgent can instrument.

     For ESM Lambda deployments:

     ```
     // handler_wrap.mjs



     export { handler } from "./index.mjs";
     ```

     For CommonJS Lambda deployments:

     ```
     const bundleDist = require("./dist/index");



     exports.handler = bundleDist.handler;
     ```
  3. In your AWS Lambda runtime configuration, set the handler to `handler_wrap.handler`.

  OneAgent will now be able to detect and instrument the function correctly.
  Using a bundler introduces additional limitations on the visibility of dependencies. For details, see [OneAgent Node.js known limitations](/managed/ingest-from/technology-support/application-software/nodejs#limitations "Read about Dynatrace support for Node.js applications.").

### Go limitations

#### General limitations:

* Go applications for AWS Lambda must be built with dynamic linking enabled. To enable dynamic linking, set `CGO_ENABLED=1` and use the system linker.

  Example

  ```
  CGO_ENABLED=1



  go build -ldflags '-linkmode=external' -o myapp main.go
  ```
* Go applications do not require a special runtime. The OS-only runtime is used. `Go 1.x` runtime is deprecated and not supported.

#### Versioning limitations

* Go support for AWS Lambda requires OneAgent version 1.333+. It is not backwards-compatible with older OneAgent versions.
* [External metadata](/managed/ingest-from/technology-support/application-software/go/support/supported-go-versions#external-metadata "Find out which Go versions are supported by Dynatrace.") support for Go in AWS Lambda is not supported. As a result, third-party library versions or newly released Go versions are not automatically supported. New version support is shipped with the usual OneAgent release cycle and requires OneAgent to be updated to take effect.
* [AWS-Lambda-Goï»¿](https://github.com/aws/aws-lambda-go) SDK v1.18.0+ is required for Go applications.

#### Deployment limitations

* Deployment is possible through a container image or ZIP file. In both cases, dynamic linking must be enabled.

  ZIP file archive

  The archive must contain the binary, and the application must be linked against glibc v2.34 or older. Since statically linked applications are not supported, linking against such an old version of glibc requires building in Ubuntu 20.04 or older.

  Container image

  The application must be compiled with a matching glibc version. Both AWS base images and non-AWS base images are supported.
* To set the path to the OneAgent library, use the `LD_PRELOAD` environment variable.

  ```
  LD_PRELOAD=/opt/dynatrace_layer/agent/lib64/liboneagentproc.so
  ```

### Dynatrace Managed limitations

* Managed offline clusters are not supported.