---
title: Validate integration
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension/troubleshoot-lambda
scraped: 2026-03-01T21:18:07.213458
---

# Validate integration

# Validate integration

* Troubleshooting
* 1-min read
* Published Aug 30, 2021

This topic is about the classic AWS Lambda integration. Check out [Trace Lambda functions](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/trace-lambda-functions "Monitor AWS Lambda functions.") for the latest experience.

To address the issues regarding Dynatrace AWS Lambda extension integration, start with the logs and error messages.

## Logs

To get extensive log output on Lambda, add the variables below.

* For **Node.js**

  ```
  DT_LOGGING_DESTINATION: stdout



  DT_LOGGING_NODEJS_FLAGS: Exporter=true,LambdaSensor=true
  ```
* For **Python**

  ```
  DT_LOGGING_DESTINATION: stdout



  DT_LOGGING_PYTHON_FLAGS: dynatrace=True
  ```
* For **Java**

  ```
  DT_LOGGING_DESTINATION: stdout



  DT_LOGGING_JAVA_FLAGS: log-Transformer=true,log-OpenTelemetryUtils=true,log-AsyncClassRetransformer=true,log-ClassValue=true
  ```

  `logOpenTelemetryUtils=true` is required for `use-inmemory-exporter` (for debugging span-related problems).

## Error messages

* **WARNING [â¦] Unexpectedly got HTTP response with Content-Length (...)**

  This error message is displayed if you don't have port 9999 enabled for your ActiveGate. Go to [AWS PrivateLink and VPC endpointsï»¿](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-services-overview.html) and set up a VPC that allows outbound communication on port 9999 to the ActiveGate endpoint.

## OpenTelemetry interoperability

### Python

OneAgent will not enable OpenTelemetry interoperability when it detects that the installed OpenTelemetry API version is incompatible. In this case, a line similar to the following is logged:

```
[Dynatrace] 2022-07-27 08:55:01.852 UTC [9-dfaf4836] INFO    [dynatrace.inject.agent] opentelemetry-api version (1.10.0) is not compatible with Dynatrace SDK (1.9.1).
```

It is possible to override the compatibility check via configuration. For instance, when you configure OneAgent using the [environment variables](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-method "Monitor Lambda functions written in Python, Node.js, and Java."), add:

`DT_OPEN_TELEMETRY_OVERRIDE_MAX_API_VERSION=1.11.1`

to allow OpenTelemetry APIs up to version `1.11.1`.

Overriding the version compatibility check might result in runtime errors and should be used with **caution**. You should verify if these errors still occur if an officially supported version of the OpenTelemetry API is used or when temporarily disabling the OpenTelemetry interoperability. If this resolves the problem, please use the older OpenTelemetry API until the newer version is officially supported.