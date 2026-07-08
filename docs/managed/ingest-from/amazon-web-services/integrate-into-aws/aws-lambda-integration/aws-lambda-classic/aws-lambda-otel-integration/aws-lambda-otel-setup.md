---
title: Monitor AWS Lambda with OpenTelemetry
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/aws-lambda-otel-setup
---

# Monitor AWS Lambda with OpenTelemetry

# Monitor AWS Lambda with OpenTelemetry

* How-to guide
* 3-min read
* Updated on Jan 22, 2026

Dynatrace provides enhancements to OpenTelemetry for AWS Lambda such as exporters, additional instrumentation, and helper libraries to simplify the monitoring of AWS Lambda.

For a list of language-specific packages that you can use in combination with the native OpenTelemetry SDKs and APIs or AWS Distribution for OpenTelemetry, see [Trace .NET Lambda functions](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration "Trace AWS Lambda functions using a .NET runtime").

## Prerequisites

* Dynatrace version 1.240+
* OneAgent version 1.193+ for all OneAgents participating in a trace
* In Dynatrace, go to **Settings** > **Preferences** > **OneAgent features** and activate the **Forward Tag 4 trace context extension** OneAgent feature.

## Installation

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Select a monitoring solution and configuration method**](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/aws-lambda-otel-setup#choose-config-method "Prerequisites for monitoring AWS Lambda with OpenTelemetry")[![Step 2 optional](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Step 2 optional")

**Specify a Dynatrace API endpoint**](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/aws-lambda-otel-setup#specify-endpoint "Prerequisites for monitoring AWS Lambda with OpenTelemetry")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Apply the configuration to your AWS Lambda function**](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/aws-lambda-otel-setup#apply-config "Prerequisites for monitoring AWS Lambda with OpenTelemetry")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Instrument the function code**](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/aws-lambda-otel-setup#instrument-code "Prerequisites for monitoring AWS Lambda with OpenTelemetry")

## Step 1 Set the monitoring solution and configuration method

Configuration options regarding Lambda layers don't apply here.

1. Go to **Deploy Dynatrace**.
2. Select **Start installation** > **AWS Lambda**.

3. On the **Enable Monitoring for AWS Lambda Functions** page, set **Select a runtime** to **.NET**.

   This automatically sets **Monitoring solution** to **AWS Lambda OpenTelemetry package**.
4. Set **Select a configuration method** to your preferred configuration method. Make sure you set all properties for the chosen configuration method.

## Step 2 optional Specify a Dynatrace API endpoint Optional

If you don't want to use the default public Dynatrace endpoint, specify a custom Dynatrace API endpoint where you want to receive monitoring data.

To reduce network latency, you typically deploy a Dynatrace ActiveGate close to (in the same region as) the AWS Lambda function that you want to monitor.

### Step 3 Apply the configuration to your AWS Lambda function

To apply the configuration, select one of the options below, depending on your configuration method.

Configure with JSON file

Copy the JSON snippet into a file named `dtconfig.json` located in the root folder of your AWS Lambda Functions deployment.

Configure with environment variables

On **Enable Monitoring for AWS Lambda Functions**, under **Use the following values to define environment variables for your AWS Lambda function**, there's a snippet with all required environment variables. Be sure to add these environment variables and their values to your Lambda function configuration. For details, see [Configuring environment variables﻿](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-config).

## Step 4 Instrument the function code

Adding the required API calls to monitor function invocations via OpenTelemetry is specific to languages and their respective OpenTelemetry distribution.

To get detailed instructions for different languages supported by Dynatrace, see [Trace .NET Lambda functions](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration "Trace AWS Lambda functions using a .NET runtime").

## Known limitations

The Dynatrace instrumentation doesn't capture the IP addresses of outgoing HTTP requests. If the called service isn't monitored with Dynatrace, this results in **unmonitored hosts**.