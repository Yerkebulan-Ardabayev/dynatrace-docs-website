---
title: Cloud provider log forwarding (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/cloud-provider-log-forwarding
scraped: 2026-02-17T21:33:13.971092
---

# Cloud provider log forwarding (Logs Classic)

# Cloud provider log forwarding (Logs Classic)

* Overview
* 3-min read
* Updated on Jan 18, 2023

Log Monitoring Classic

Dynatrace version 1.230+

For the newest Dynatrace version, see [Cloud provider log forwarding](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-cloud-provider-log-forwarding "Configure AWS, Azure and Google Cloud log forwarding to stream log data to Dynatrace using API.").

DDU consumption for Log Monitoring

DDU pricing applies to cloud Log Monitoring. See [DDUs for Log Monitoring](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.") for details.

## Amazon Web Services

Stream or forward your logs from Amazon CloudWatch, AWS S3 or other AWS sources.

### Stream logs via Amazon Data Firehose

Dynatrace integration with Amazon Data Firehose provides a simple and safe way to ingest AWS logs.

To enable AWS log forwarding,

1. Create Amazon Data Firehose instance.
2. Configure it with your Dynatrace environment as a destination.
3. Connect your CloudWatch log groups by creating a subscription filter or send logs directly to Firehose from services that support it (for example, VPC Flow Logs).
   Firehose and other created cloud resources incur AWS costs according to the standard AWS billing policy.

To learn more, see [Stream logs via Amazon Data Firehose (Logs Classic)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lm-stream-logs-with-firehose "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput.").

### Log ingestion from Amazon S3

You can stream logs from AWS S3 to Dynatrace using a serverless architecture.

The log forwarder offers:

* Out of the box parsing of AWS services, see [Supported AWS Servicesï»¿](https://github.com/dynatrace-oss/dynatrace-aws-s3-log-forwarder#supported-aws-services)
* Processing mechanism for any other use case including 3rd party logs written to s3, see [Log Processingï»¿](https://github.com/dynatrace-oss/dynatrace-aws-s3-log-forwarder/blob/main/docs/log_processing.md#log-processing)
* Cross-region support, see [S3 buckets on different AWS Regionsï»¿](https://github.com/dynatrace-oss/dynatrace-aws-s3-log-forwarder/blob/main/docs/log_forwarding.md#forward-logs-from-s3-buckets-on-different-aws-regions)
* Multiple AWS account support, see [S3 buckets on different AWS accountsï»¿](https://github.com/dynatrace-oss/dynatrace-aws-s3-log-forwarder/blob/main/docs/log_forwarding.md#forward-logs-from-s3-buckets-on-different-aws-accounts)

For detailed instructions on how to set up log ingestion from AWS S3, see [documentation on GitHubï»¿](https://github.com/dynatrace-oss/dynatrace-aws-s3-log-forwarder).

### AWS Lambda log collection

You can collect logs directly from your AWS Lambda functions and send them to Dynatrace for analysis. The solution is an alternative to the CloudWatch log forwarder with benefits in terms of cost and latency, and is also easier to set up, particularly if AWS Lambda tracing is already in place. As part of the OneAgent installation process, this feature provides a streamlined solution for collecting logs from your Lambda functions. For more information, see [AWS Lambda documentation page](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/collector "Collect logs from AWS Lambda functions").

### AWS log monitoring using log forwarder Deprecated

You can stream logs from Amazon CloudWatch into Dynatrace logs via an ActiveGate.

To enable AWS log forwarding, you need to deploy our special-purpose CloudFormation stack into your AWS account. The stack consists of a Kinesis Firehose instance and a Lambda function. These resources incur AWS costs according to standard AWS billing policy. The same applies to included self-monitoring resources (CloudWatch dashboards and metrics).

For detailed instructions on how to set up AWS log forwarding, see [Log monitoring with AWS log forwarder](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/aws-log-forwarder#prereq "Use AWS log forwarding to ingest AWS logs.").

### Stream logs via Amazon Data Firehose

Dynatrace integration with Amazon Data Firehose provides a simple and safe way to ingest AWS logs.

To enable AWS log forwarding, you need to create Amazon Data Firehose instance and configure it with your Dynatrace environment as a destination. Then you can connect your CloudWatch log groups by creating a Subscription Filter or send logs directly to Firehose from services that support it (e.g. VPC flow logs). Firehose and other created cloud resources incur AWS costs according to the standard AWS billing policy.

## Microsoft Azure

Azure log forwarding allows you to stream Azure logs from Azure Event Hubs into Dynatrace logs via an Azure Function App instance. It supports both Azure resource logs and activity logs.

Azure log forwarding is performed directly through Cluster API. If you don't want to use direct ingest through the Cluster API, you have to use an existing ActiveGate for log ingestion.

Deployment of Azure log forwarder results in creating the following resources:

* Storage account (`Microsoft.Storage/storageAccounts`)
* Storage Account Blob Service (`Microsoft.Storage/storageAccounts/blobServices`)
* Azure App Service plan (`Microsoft.Web/serverfarms`)
* Azure Function App (`Microsoft.Web/sites`)

Azure log forwarder uses Linux based Azure function by default. Windows based function is not supported.

For details about the resources created, see the [Azure Resource Manager file on GitHubï»¿](https://github.com/dynatrace-oss/dynatrace-azure-log-forwarder/blob/master/deployment/dynatrace-azure-forwarder.json)

For detailed instruction on how to set up Azure log forwarding see, [Azure Logs](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure#prereq "Use Azure log forwarding to ingest Azure logs.").

## Google Cloud

To set up Google Cloud monitoring for metrics and logs, you'll run the deployment script in Google Cloud Shell. During setup, a new Pub/Sub subscription will be created. GKE will run two containers: a metric forwarder and a log forwarder. After installation, you'll get metrics, logs, dashboards, and alerts for your configured services in Dynatrace. Instructions will depend on the location where you want the deployment script to run:

* [On a new GKE Autopilot cluster created automatically](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster."). Recommended
* [On an existing GKE standard or GKE Autopilot cluster](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-on-existing-cluster "Deploy log and metric monitoring for Google Cloud services on an existing standard GKE or GKE Autopilot cluster").

Depending on where you want log ingestion to be performed, you may need additional resources. For example, for Managed deployments, there is a possibility to use an AG for log ingestion. But you have to do it manually since the installation script does not deploy it.

For all log ingestion options, see [Log ingestion](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#ingestion "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

## Related topics

* [DDUs for Log Monitoring Classic](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.")