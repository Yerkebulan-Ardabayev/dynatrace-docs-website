---
title: OpenTelemetry interoperability
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability
scraped: 2026-02-22T21:21:26.039667
---

# OpenTelemetry interoperability

# OpenTelemetry interoperability

* 1-min read
* Updated on Apr 24, 2023

With Dynatrace interoperability for OpenTelemetry, you can use the instrumentation packages available from OpenTelemetry to monitor technologies (like databases or messaging frameworks) that aren't supported by the Dynatrace AWS Lambda extension out-of-the box. The Dynatrace AWS Lambda extension automatically captures the additional span instrumentation and integrates it with any other telemetry captured without any need to configure additional OpenTelemetry exporters.

[OpenTelemetryï»¿](https://dt-url.net/y903u4j) is a collection of tools, APIs, and SDKs. You can use it to instrument, generate, collect, and export telemetry data (metrics, logs, and traces) for analysis to get insights into your software's performance and behavior. OpenTelemetry interoperability connects [Dynatrace AWS Lambda extension](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension "Monitor Lambda functions written in Python, Node.js, and Java.") to OpenTelemetry API for the respective instrumentation.

## Enable OpenTelemetry interoperability

* For the [environment variables configuration method](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-method "Monitor Lambda functions written in Python, Node.js, and Java."), set the value of the `DT_OPEN_TELEMETRY_ENABLE_INTEGRATION` environment variable to `true`.
* For the [JSON file configuration method](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-method "Monitor Lambda functions written in Python, Node.js, and Java."), set the respective property to `true` in the `dtconfig.json` file. For example:

  ```
  {



  ...other configuration properties...



  "OpenTelemetry": {



  "EnableIntegration": true



  }



  }
  ```

## Learn more

To learn more about how OpenTelemetry interoperability works, see

* [OpenTelemetry interoperability in Python](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/lambda-otel-bridge-python "Connect Dynatrace AWS Lambda extension to the OpenTelemetry Python instrumentation via OpenTelemetry interoperability.")
* [OpenTelemetry interoperability in Node.js](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/lambda-otel-bridge-nodejs "Connect Dynatrace AWS Lambda extension to the OpenTelemetry Node.js instrumentation via OpenTelemetry interoperability.")
* [OpenTelemetry interoperability in Java](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/lambda-otel-bridge-java "Connect Dynatrace AWS Lambda extension to the OpenTelemetry Java API via OpenTelemetry interoperability.")

## Related topics

* [Trace Python, Node.js, and Java Lambda functions](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension "Monitor Lambda functions written in Python, Node.js, and Java.")