---
title: Monitor AWS Lambda
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration
scraped: 2026-05-12T11:14:22.725864
---

# Monitor AWS Lambda

# Monitor AWS Lambda

* Explanation
* 3-min read
* Updated on Feb 17, 2026

Dynatrace provides end-to-end observability for AWS Lambda functions through distributed tracing, log correlation, and AI-powered insights using auto-instrumentation without code changes. The OneAgent AWS Lambda extension collects logs directly from Lambda functions, offering an alternative to CloudWatch via Firehose with lower cost, lower latency, and easier setup.

[#### Trace Lambda functions

Monitor AWS Lambda functions.

* How-to guide

Read this guide](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/trace-lambda-functions)[#### Trace .NET Lambda functions

Trace AWS Lambda functions using a .NET runtime

* How-to guide

Read this guide](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration)

[#### AWS Lambda log collection

Collect logs from AWS Lambda functions

* How-to guide

Read this guide](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/collector)[#### Monitor AWS Lambda (built-in)

Monitor AWS Lambda (built-in) and view available metrics.

* How-to guide

Read this guide](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/aws-lambda-cloudwatch-metrics/lambda-builtin)

[#### Integrate Dynatrace Lambda Layer on container images

Deploy Dynatrace Lambda Layers when deployed via a container image.

* How-to guide

Read this guide](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/deploy-oa-latest-lambda-container-images)

## Integrations

AWS Lambda instrumentation is available for the following runtimes:

| Runtime | Lambda layer version[1](#fn-1-1-def) | Applies to Lambda Classic |
| --- | --- | --- |
| Python | 1.321 (or later) | Yes |
| Node.js | 1.319 (or later) | Yes |
| Java | 1.319 (or later) | Yes |
| .NET | Coming soon | Yes |
| Go | 1.333 (or later) | Log Monitoring only |

1

Managed offline clusters are not supported.

For more details, see [Technology support](/managed/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

## Monitoring consumption

For AWS Lambda, monitoring consumption is based on Davis data units. See [Serverless monitoring](/managed/license/monitoring-consumption-classic/davis-data-units/serverless-monitoring "Understand how serverless monitoring consumption is calculated.") for details.

## Related topics

* [Dynatrace OneAgent](/managed/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.")