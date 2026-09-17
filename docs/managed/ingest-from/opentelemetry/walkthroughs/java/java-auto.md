---
title: Automatically instrument your Java application with OpenTelemetry
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/walkthroughs/java/java-auto
---

# Automatically instrument your Java application with OpenTelemetry

# Automatically instrument your Java application with OpenTelemetry

* How-to guide
* 1-min read
* Updated on Aug 04, 2026

This walkthrough shows how to add observability to your Java application using the automatic instrumentation agent for OpenTelemetry Java.

Enrichment with OneAgent

It is currently not possible to [enrich](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.") automatically instrumented services with host-relevant information. To achieve this, you'd need to switch to manual instrumentation.

## Step 1 Get the Dynatrace access details

### Determine the API base URL

For details on how to assemble the base OTLP endpoint URL, see [Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

The URL should end in `/api/v2/otlp`.

### Get an authentication token

To authenticate with Dynatrace, use a [platform token](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") or a [Classic access token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.").

* **Platform token**:

  1. Go to [My platform tokens﻿](https://myaccount.dynatrace.com/platformTokens).
  2. Create a platform token with the scope matching your signal type: `openpipeline:logs:ingest` for logs, `openpipeline:metrics:ingest` for metrics, or `openpipeline:traces:ingest` for traces.
  3. Use `Authorization: Bearer <your-platform-token>` as the header value.
* **Classic access token**:

  1. Go to ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.
  2. Generate a token with the scope matching your signal type: `logs.ingest` for logs, `metrics.ingest` for metrics, or `openTelemetryTrace.ingest` for traces.
  3. Use `Authorization: Api-Token <your-classic-access-token>` as the header value.

[Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api#authentication "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") has more details on authentication formats and the required scopes.

## Step 2 Instrument your application

1. Download the [latest `opentelemetry-javaagent.jar`﻿](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/latest/download/opentelemetry-javaagent.jar) agent file and save it to a directory accessible to your application (for example, `libs`).
2. Configure the following environment variables to set the service and protocol details. If you export using OTLP, also set the URL and token variables to [the respective values](#dynatrace-docs--otlp-export).

   Platform token

   Classic access token

   ```
   OTEL_EXPORTER_OTLP_ENDPOINT=[URL]



   OTEL_EXPORTER_OTLP_HEADERS="Authorization=Bearer [TOKEN]"



   OTEL_RESOURCE_ATTRIBUTES="service.name=java-quickstart,service.version=1.0.1"



   OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=delta
   ```

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