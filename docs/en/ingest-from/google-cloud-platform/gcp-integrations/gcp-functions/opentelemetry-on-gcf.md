---
title: Set up OpenTelemetry monitoring for Google Cloud Functions
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf
scraped: 2026-03-06T21:29:42.968498
---

# Set up OpenTelemetry monitoring for Google Cloud Functions


* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Mar 31, 2025

Dynatrace uses [OpenTelemetryï»¿](https://dt-url.net/y903u4j) to monitor Google Cloud Functions invocations.

For that purpose, Dynatrace provides language-specific packagesâsuch as `@dynatrace/opentelemetry-gcf` for Node.js, `dynatrace-opentelemetry-gcf` for Python, and `Dynatrace.OpenTelemetry.Instrumentation.GoogleCloudFunctions` for .NETâthat can be used in combination with default OpenTelemetry SDKs and APIs.

## Prerequisites

* Dynatrace version 1.240+
* OneAgent version 1.193+ for all OneAgents participating in a trace
* Go to **Settings** > **Preferences** > **OneAgent features** and activate the **Forward Tag 4 trace context extension** OneAgent feature.

## Installation

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Select a configuration method**](opentelemetry-on-gcf.md#choose-config-method "Monitor Google Cloud Functions with OpenTelemetry and Dynatrace.")[![Step 2 optional](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Step 2 optional")

**Specify a Dynatrace API endpoint**](opentelemetry-on-gcf.md#specify-endpoint "Monitor Google Cloud Functions with OpenTelemetry and Dynatrace.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Apply the configuration to your Google Cloud function**](opentelemetry-on-gcf.md#apply-config "Monitor Google Cloud Functions with OpenTelemetry and Dynatrace.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Instrument the function code**](opentelemetry-on-gcf.md#instrument-code "Monitor Google Cloud Functions with OpenTelemetry and Dynatrace.")

## Step 1 Select a configuration method

1. In Dynatrace,  **Search** for **Deploy OneAgent** app and select it.
2. Under **Download Dynatrace OneAgent**, select **Set up** > **Google Cloud Functions**.
3. On the **Enable Monitoring for Google Cloud Functions** page, under **How will you configure your Google Cloud Functions?**, select your preferred method from the dropdown menu. Make sure you set all properties for the selected method before copying the generated configuration snippets.

## Step 2 optional Specify a Dynatrace API endpoint Optional

If you don't want to use the default public Dynatrace endpoint, specify a custom Dynatrace API endpoint where you want to receive monitoring data.

To reduce network latency, you typically deploy a Dynatrace ActiveGate close to (in the same region as) the Google Cloud function that you want to monitor.

### Step 3 Apply the configuration to your Google Cloud function

Configure with JSON file

Copy the JSON snippet into a file named `dtconfig.json` located in the root folder of your Google Cloud Functions deployment.

Configure with environment variables

On **Enable Monitoring for Google Cloud Functions**, under **Use the following values to configure your monitored Google Cloud Functions**, there's a snippet with all required environment variables. Be sure to add these environment variables and their values to your Google Cloud function configuration. For details, see [Using environment variablesï»¿](https://cloud.google.com/functions/docs/configuring/env-var).

## Step 4 Instrument the function code

Adding the required API calls to monitor function invocations via OpenTelemetry is specific to languages and their respective OpenTelemetry distribution:

* **Node.js:** Integrate on Google Cloud Functions Node.js
* **Python:** Integrate on Google Cloud Functions Python
* **Go:** Integrate on Google Cloud Functions GoLang
* **.NET:** Integrate on Google Cloud Functions .NET

## Known limitations

The Dynatrace Google Cloud Functions integration doesn't capture the IP addresses of outgoing HTTP requests. If the called service isn't monitored with Dynatrace OneAgent, this results in **unmonitored hosts**.

## Related topics

* Set up Dynatrace on Google Cloud
* OneAgent platform and capability support matrix
* [Google Cloud monitoringï»¿](https://www.dynatrace.com/technologies/google-cloud-monitoring/)