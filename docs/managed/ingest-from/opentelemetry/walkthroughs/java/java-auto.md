---
title: Automatically instrument your Java application with OpenTelemetry
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/walkthroughs/java/java-auto
scraped: 2026-05-12T12:12:08.020183
---

# Automatically instrument your Java application with OpenTelemetry

# Automatically instrument your Java application with OpenTelemetry

* How-to guide
* 1-min read
* Published Apr 18, 2023

This walkthrough shows how to add observability to your Java application using the automatic instrumentation agent for OpenTelemetry Java.

Enrichment with OneAgent

It is currently not possible to [enrich](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.") automatically instrumented services with host-relevant information. To achieve this, you'd need to switch to manual instrumentation.

## Step 1 Get the Dynatrace access details

### Determine the API base URL

For details on how to assemble the base OTLP endpoint URL, see [Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

The URL should end in `/api/v2/otlp`.

### Get API access token

To generate an access token, in Dynatrace, go to ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

[Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api#authentication "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") has more details on the format and the necessary access scopes.

## Step 2 Instrument your application

1. Download the [latest `opentelemetry-javaagent.jar`ï»¿](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/latest/download/opentelemetry-javaagent.jar) agent file and save it to a directory accessible to your application (for example, `libs`).
2. Configure the following environment variables to set the service and protocol details. If you export using OTLP, also set the URL and token variables to [the respective values](#dynatrace-docs--otlp-export).

   ```
   OTEL_EXPORTER_OTLP_ENDPOINT=[URL]



   OTEL_EXPORTER_OTLP_HEADERS="Authorization=Api-Token [TOKEN]"



   OTEL_RESOURCE_ATTRIBUTES="service.name=java-quickstart,service.version=1.0.1"



   OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=delta
   ```
3. Include the `-javaagent` parameter in your Java invocation command and specify the path to the agent file. For example, if you started your application from the command line:

   ```
   java -javaagent:/PATH/TO/opentelemetry-javaagent.jar -jar myapplication.jar
   ```

## Step 3 Ensure context propagation

Context propagation is particularly important when network calls (for example, REST) are involved.

If you are using automatic instrumentation and your networking libraries are covered by automatic instrumentation, this will be automatically taken care of by the instrumentation libraries. Otherwise, your code needs to take this into account.

## Step 4 optional Configure data capture to meet privacy requirements Optional

While Dynatrace automatically captures all OpenTelemetry attributes, only attribute values specified in the allowlist are stored and displayed in the Dynatrace web UI. This prevents accidental storage of personal data, so you can meet your privacy requirements and control the amount of monitoring data stored.

To view your custom attributes, you need to allow them in the Dynatrace web UI first. To learn how to configure attribute storage and masking, see [Attribute redaction](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Learn how to enable and configure the OneAgent Span Sensor for OpenTelemetry data.").

## Step 5 Verify data ingestion into Dynatrace

Once you have finished the instrumentation of your application, perform a couple of test actions to create and send demo traces, metrics, and logs and verify that they were correctly ingested into Dynatrace.

To do that for traces, go to **Distributed Traces** and select the **Ingested traces** tab. If you use OneAgent, select **PurePaths** instead.

For metrics and logs, go to **Metrics** or **Logs**.

## Related topics

* [Enrich ingested data with Dynatrace-specific fields](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")