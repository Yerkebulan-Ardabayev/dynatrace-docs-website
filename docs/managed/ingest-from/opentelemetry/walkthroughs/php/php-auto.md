---
title: Automatically instrument your PHP application with OpenTelemetry
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/walkthroughs/php/php-auto
scraped: 2026-05-12T12:15:16.706329
---

# Automatically instrument your PHP application with OpenTelemetry

# Automatically instrument your PHP application with OpenTelemetry

* How-to guide
* 2-min read
* Published Apr 20, 2023

This walkthrough shows how to add observability to your PHP application using the OpenTelemetry PHP libraries and tools.

Enrichment with OneAgent

It is currently not possible to [enrich](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.") automatically instrumented services with host-relevant information. To achieve this, you'd need to switch to manual instrumentation.

## Step 1 Get the Dynatrace access details

### Determine the API base URL

For details on how to assemble the base OTLP endpoint URL, see [Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."). The URL should end in `/api/v2/otlp`.

### Get API access token

To generate an access token, in Dynatrace, go to ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

[Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api#authentication "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") has more details on the format and the necessary access scopes.

## Step 2 Instrument your application

1. Ensure you have an adequate build environment for your system set up, consisting of GCC, Make, and Autoconfig.
2. Build and install the instrumentation library, using [pickleï»¿](https://github.com/FriendsOfPHP/pickle).

   ```
   php pickle.phar install opentelemetry
   ```
3. Add the newly compiled library as extension to your `php.ini`.

   ```
   extension=opentelemetry.so
   ```
4. Restart PHP and verify that the extension was loaded.

   * From the command line, with `php -m`
   * As part of a web server, by calling `phpinfo()`
5. Install the SDK and other dependencies.

   * Required Install the [SDK for OpenTelemetry PHPï»¿](https://dt-url.net/41039bh).
   * Optional Depending on the libraries your application is using, you might want to add other instrumentation libraries to the dependencies. You'll find the list of supported libraries in the [OpenTelemetry Registryï»¿](https://dt-url.net/zf239yc).
   * Required You must use [composer autoloadingï»¿](https://dt-url.net/s2439p5), as this is the mechanism that all auto-instrumentation packages use to register themselves.
6. Configure the following environment variables.

   ```
   OTEL_PHP_AUTOLOAD_ENABLED=true



   OTEL_SERVICE_NAME=php-quickstart



   OTEL_PROPAGATORS=baggage,tracecontext



   OTEL_EXPORTER=otlp



   OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf



   OTEL_EXPORTER_OTLP_ENDPOINT=[URL]



   OTEL_EXPORTER_OTLP_HEADERS="Authorization=Api-Token [TOKEN]"



   OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=delta
   ```

   Substitute `[URL]` and `[TOKEN]` with the [respective values](#dynatrace-docs--otlp-export).

## Step 3 Ensure context propagation

Context propagation is particularly important when network calls (for example, REST) are involved.

With automatic instrumentation, this should be automatically taken care of by the instrumentation libraries. If the used network libraries are not be covered by that, you would need to switch to [manual instrumentation](/managed/ingest-from/opentelemetry/walkthroughs/python/python-manual "Learn how to instrument your Python application using OpenTelemetry and Dynatrace.") instead and handle propagation manually.

## Step 4 optional Configure data capture to meet privacy requirements Optional

While Dynatrace automatically captures all OpenTelemetry attributes, only attribute values specified in the allowlist are stored and displayed in the Dynatrace web UI. This prevents accidental storage of personal data, so you can meet your privacy requirements and control the amount of monitoring data stored.

To view your custom attributes, you need to allow them in the Dynatrace web UI first. To learn how to configure attribute storage and masking, see [Attribute redaction](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Learn how to enable and configure the OneAgent Span Sensor for OpenTelemetry data.").

## Step 5 Verify data ingestion into Dynatrace

Once you have finished the instrumentation of your application, perform a couple of test actions to create and send demo traces, metrics, and logs and verify that they were correctly ingested into Dynatrace.

To do that for traces, go to **Distributed Traces** and select the **Ingested traces** tab. If you use OneAgent, select **PurePaths** instead.

For metrics and logs, go to **Metrics** or **Logs**.

## Related topics

* [Enrich ingested data with Dynatrace-specific fields](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")