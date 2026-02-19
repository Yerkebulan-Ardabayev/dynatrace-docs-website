---
title: Set up OpenTelemetry monitoring for Azure Functions on Consumption Plan
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions
scraped: 2026-02-19T21:29:07.127993
---

# Set up OpenTelemetry monitoring for Azure Functions on Consumption Plan

# Set up OpenTelemetry monitoring for Azure Functions on Consumption Plan

* Latest Dynatrace
* How-to guide
* 3-min read
* Updated on Mar 31, 2025

Dynatrace version 1.240+ OneAgent version 1.193+

Dynatrace uses [OpenTelemetryï»¿](https://dt-url.net/y903u4j) to monitor Azure Functions invocations.
For that purpose, Dynatrace provides language-specific packages, such as [`Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Core` for .NET](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-dotnet "Monitor Azure Functions with OpenTelemetry for .NET and Dynatrace."), that can be used in combination with default OpenTelemetry SDKs and APIs.

## Installation

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Activate the OneAgent feature**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions#oneagent-feature "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Select a configuration method**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions#choose-config-method "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.")[![Step 3 optional](https://dt-cdn.net/images/dotted-step-3-e2082c1921.svg "Step 3 optional")

**Specify a Dynatrace API endpoint**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions#specify-endpoint "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Apply the configuration to your function app**](#apply-config)[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Instrument the function code**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions#instrument-code "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.")

### Step 1 Activate the OneAgent feature

Go to **Settings** > **Preferences** > **OneAgent features** and activate the **Forward Tag 4 trace context extension** OneAgent feature.

### Step 2 Select a configuration method

1. In Dynatrace,  **Search** for **Deploy OneAgent** app and select it.
2. Under **Download Dynatrace OneAgent**, select **Set up** > **Azure Functions**.
3. On the **Enable Monitoring for Azure Functions** page, under **How will you configure your Azure Functions?**, select your preferred configuration method from the dropdown menu.

### Step 3 optional Specify a Dynatrace API endpoint Optional

If you don't want to use the default public Dynatrace endpoint, specify a custom Dynatrace API endpoint where you want to receive monitoring data.

To reduce network latency, you typically deploy a Dynatrace ActiveGate close to (in the same region as) the Azure Function that you want to monitor.

### Step 4 Apply the configuration to your function app

To apply the configuration, select one of the options below, depending on your configuration method.

Configure with JSON file

Configure with environment variables

Copy the JSON snippet into a file named `dtconfig.json` located in the root folder of your Azure Functions deployment.

On **Enable Monitoring for Azure Functions**, under **Use the following values to configure your monitored Azure Functions**, there's a snippet with all required environment variables. Be sure to add these environment variables and their values to your function app configuration:

1. In Azure Portal, go to your function app.
2. In **Settings**, select **Configuration**.
3. Edit any existing environment variables so that the names and values match those in [Dynatrace](#variables-dynatrace), or, if your function app doesn't have any existing variables, select **New application setting** and add the names and values for all the variables in [Dynatrace](#variables-dynatrace).

Leave the settings not listed by Dynatrace unchanged.

### Step 5 Instrument the function code

Adding the required API calls to monitor function invocations via OpenTelemetry is specific to languages and their respective OpenTelemetry distribution:

* **.NET (C#):** [Trace Azure Functions written in .NET](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-dotnet "Monitor Azure Functions with OpenTelemetry for .NET and Dynatrace.")
* **Node.js (Javascript):** [Trace Azure Functions written in Node.js](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-nodejs "Monitor Azure Functions with OpenTelemetry for Node.js and Dynatrace.")
* **Python:** [Trace Azure Functions written in Python](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-python "Monitor Azure Functions with OpenTelemetry for Python and Dynatrace.")

## Known limitations

The Dynatrace Azure Functions integration doesn't capture the IP addresses of outgoing HTTP requests. If the called service isn't monitored with Dynatrace OneAgent, this results in **unmonitored hosts**.

## Related topics

* [Monitor Azure Functions on App Service Plan for Windows](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/integrate-oneagent-on-azure-functions "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions using an Azure site extension.")
* [Set up Dynatrace on Microsoft Azure](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")