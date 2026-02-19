---
title: Stream Logs with Cribl
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-cribl
scraped: 2026-02-19T21:32:15.900584
---

# Stream Logs with Cribl

# Stream Logs with Cribl

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Jun 12, 2025

You can send logs, metrics, and traces to Dynatrace using Cribl Stream via OpenTelemetry Protocol (OTLP) or send only logs using Cribl Stream via HTTP and API ingestion.

The [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector "Learn about the Dynatrace OTel Collector.") offers various ingestion and transformation capabilities, making it a versatile tool for processing log data from a variety of sources.

## Key Features

* **Multiple Endpoint Types:** Connect to Dynatrace Cloud (SaaS), ActiveGate, or specify a manual endpoint URL.
* **Secure Authentication:** Uses Dynatrace API tokens for secure data transmission.
* **Persistent Queue:** Buffers data during connectivity issues to prevent data loss.
* **Custom HTTP Headers:** Add tracking information or metadata to your log transmissions.
* **Forwarding Logs, Metrics, and Traces:** Send all telemetry data types to Dynatrace.

## Deploy Integration Using OpenTelemetry

Setting up a direct integration of telemetry data via Cribl Stream OTLP Destination takes just a few simple steps:

1. **Get API key to ingest telemetry data.**

   * Generate a new token with the appropriate scope. Refer to Dynatrace documentation for details.
2. **Configure Cribl Stream OTLP Destination.**

   * In Cribl Stream, navigate to **Data > Destinations** and add a new **Dynatrace OTLP** destination.
   * Configure your Dynatrace endpoint (SaaS or ActiveGate).
   * Provide your Dynatrace environment ID and API access token.
3. **Route your telemetry data.**

   * Create routes in Cribl Stream to direct your telemetry data to the Dynatrace OTLP Destination.
   * Deploy your configuration to start sending data.
4. **Process incoming data with Dynatrace OpenPipeline.**

   * Enrich and contextualize data.
   * Extract metrics, or create business events from logs, metrics, and traces.

Please consult the [Cribl product documentationï»¿](https://docs.cribl.io/stream/destinations-dynatrace-otlp/) for additional configuration details.

## Deploy Integration Using HTTP and API

Setting up a direct integration of logs via Cribl Stream HTTP Destination takes just a few simple steps:

1. **Get API key to ingest logs.**

   * Generate a new token with the appropriate scope. Refer to Dynatrace documentation for details.
2. **Configure Cribl Stream HTTP Destination.**

   * In Cribl Stream, navigate to **Data > Destinations** and add a new **Dynatrace HTTP** destination.
   * Select your endpoint type (Cloud, ActiveGate, or Manual).
   * Provide your Dynatrace environment ID and API access token.
3. **Route your log data.**

   * Create routes in Cribl Stream to direct your log data to the Dynatrace HTTP Destination.
   * Deploy your configuration to start sending logs.
4. **Process incoming logs and events with Dynatrace OpenPipeline.**

   * Enrich and contextualize data.
   * Extract metrics, or create business events from logs.

Please consult the [Cribl product documentationï»¿](https://docs.cribl.io/stream/destinations-dynatrace-http/) for additional configuration details.