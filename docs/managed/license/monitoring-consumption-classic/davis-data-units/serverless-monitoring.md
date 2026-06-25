---
title: DDUs for serverless functions
source: https://docs.dynatrace.com/managed/license/monitoring-consumption-classic/davis-data-units/serverless-monitoring
scraped: 2026-05-12T11:52:02.760066
---

# DDUs for serverless functions

# DDUs for serverless functions

* 2-min read
* Published Mar 30, 2021

Dynatrace monitors serverless compute technologies through integration with cloud platform providers and tracing integrations.

## Metrics captured from cloud provider integrations

Cloud services (including serverless functions and serverless containers) that are monitored using cloud vendor integrations for Amazon CloudWatch, Azure Monitor, or Google Cloud Operation Suite typically consume custom metrics. For details, see [DDUs for custom metrics](/managed/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").

## Application and platform Logs

Dynatrace allows for the ingestion of log files from your serverless cloud services, which consumes Davis data units. For details, see [DDUs for log files](/managed/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.").

## AWS Lambda tracing

For [AWS Lambda tracing integration](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension "Monitor Lambda functions written in Python, Node.js, and Java."), monitoring consumption is based on Davis data units. Dynatrace counts the total number of invocations (for example, requests) of the monitored functions. For each invocation, .002 DDUs are deducted from your available quota.

For example, if you monitor 1 function and that function is invoked 1 million times, DDU consumption will be calculated as follows: `1 function Ã 1 million invocations Ã 0.002 DDU weight = 2,000 DDUs per month per function`.

## Azure Function tracing

Azure Functions provide many different hosting options, with different tracing integration possibilities. [Tracing Azure Functions on the App Service (Dedicated) plan](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/integrate-oneagent-on-azure-functions "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions using an Azure site extension.") consumes host units.

For [Tracing Azure Functions on consumption plan](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions on serverless hosting plans"), monitoring consumption is based on Davis data units. Dynatrace counts the total number of invocations (for example, requests) of the monitored functions. For each invocation, .002 DDUs are deducted from your available quota.

For example, if you monitor 1 function and that function is invoked 1 million times, DDU consumption will be calculated as follows: `1 function Ã 1 million invocations Ã 0.002 DDU weight = 2,000 DDUs per month per function`.

## Google Functions tracing

For [Google Functions tracing](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions "Set up monitoring for Google Cloud Functions."), monitoring consumption is based on Davis data units. Dynatrace counts the total number of invocations (for example, requests) of the monitored functions. For each invocation, .002 DDUs are deducted from your available quota.

For example, if you monitor 1 function and that function is invoked 1 million times, DDU consumption will be calculated as follows: `1 function Ã 1 million invocations Ã 0.002 DDU weight = 2,000 DDUs per month per function`.

## Tracing integrations with application-only monitoring

Tracing serverless compute services such as Azure container instances or AWS Fargate consumes host units. For more information, see [Serverless functions](/managed/license/monitoring-consumption-classic/application-and-infrastructure-monitoring#serverless-functions "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.").

For details on host unit calculation and monitoring consumption for serverless monitoring using [Application-only monitoring â including PaaS and some Serverless](/managed/license/monitoring-consumption-classic/application-and-infrastructure-monitoring#application-only-monitoring "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.").

## Related topics

* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)
* [License Dynatrace](/managed/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Extending Dynatrace (Davis data units)](/managed/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).")
* [DDUs for metrics](/managed/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.")
* [Extend metric observability](/managed/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.")