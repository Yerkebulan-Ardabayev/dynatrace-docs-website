---
title: Get started
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/get-started
scraped: 2026-02-17T21:20:21.852194
---

# Get started

# Get started

* Latest Dynatrace
* How-to guide
* 1-min read
* Updated on Dec 10, 2025

The Dynatrace full-stack observability platform combined with Traceloop's OpenLLMetry OpenTelemetry SDK can seamlessly provide comprehensive insights into Large Language Models (LLMs) in production environments. By observing AI models, businesses can make informed decisions, optimize performance, and ensure compliance with emerging AI regulations.

## Instrument your application

1. Create a Dynatrace token so OpenLLMetry can report data to your Dynatrace tenant.

   Create a Dynatrace Token

   To create a Dynatrace token

   1. In Dynatrace, go to **Access Tokens**.  
      To find **Access Tokens**, press **Ctrl/Cmd+K** to search for and select **Access Tokens**.
   2. In **Access Tokens**, select **Generate new token**.
   3. Enter a **Token name** for your new token.
   4. Give your new token the following permissions:
   5. Search for and select all of the following scopes.

      * **Ingest metrics** (`metrics.ingest`)
      * **Ingest logs** (`logs.ingest`)
      * **Ingest OpenTelemetry traces** (`openTelemetryTrace.ingest`)
   6. Select **Generate token**.
   7. Copy the generated token to the clipboard. Store the token in a password manager for future use.

      You can only access your token once upon creation. You can't reveal it afterward.
2. Initialize OpenLLMetry with the token to collect all the relevant KPIs.

   How you initialize the framework depends on the language.

   Python

   Node.js

   The Dynatrace backend exclusively works with delta values and requires the respective aggregation temporality. Make sure your metrics exporter is configured accordingly, or set the [`OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE`ï»¿](https://opentelemetry.io/docs/specs/otel/metrics/sdk_exporters/otlp/) environment variable to `DELTA`.

   We can leverage OpenTelemetry to provide autoinstrumentation that collects traces and metrics of your AI workloads, particularly [OpenLLMetryï»¿](https://dt-url.net/0sa3uau) that can be installed with the following command:

   ```
   pip install traceloop-sdk
   ```

   Afterward, add the following code at the beginning of your main file.

   ```
   from traceloop.sdk import Traceloop



   headers = { "Authorization": "Api-Token <YOUR_DT_API_TOKEN>" }



   Traceloop.init(



   app_name="<your-service>",



   api_endpoint="https://<YOUR_ENV>.live.dynatrace.com/api/v2/otlp", # or OpenTelemetry Collector URL



   headers=headers



   )
   ```

   We can leverage OpenTelemetry to provide autoinstrumentation that collects traces and metrics of your AI workloads, particularly [OpenLLMetryï»¿](https://dt-url.net/0sa3uau) that can be installed with the following command:

   ```
   npm i @opentelemetry/exporter-trace-otlp-proto @traceloop/node-server-sdk
   ```

   Afterward, add the following code at the beginning of your main file.

   ```
   import {OTLPTraceExporter} from "@opentelemetry/exporter-trace-otlp-proto";



   import * as traceloop from "@traceloop/node-server-sdk";



   const exporter = new OTLPTraceExporter({



   url: "https://<YOUR_ENV>.live.dynatrace.com/api/v2/otlp", // or OpenTelemetry Collector URL



   headers: { Authorization: "Api-Token <YOUR_DT_API_TOKEN>" },



   });



   traceloop.initialize({



   appName: "<your-service>",



   exporter: exporter



   });
   ```

   Currently, OpenLLMetry for Node.js doesn't support Metrics.