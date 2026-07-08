---
title: Automatically instrument your Python application with OpenTelemetry
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/walkthroughs/python/python-auto
---

# Automatically instrument your Python application with OpenTelemetry

# Automatically instrument your Python application with OpenTelemetry

* How-to guide
* 2-min read
* Published Apr 20, 2023

This walkthrough shows how to add observability to your Python application using automatic instrumentation for OpenTelemetry Python.

Enrichment with OneAgent

It is currently not possible to [enrich](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.") automatically instrumented services with host-relevant information. To achieve this, you'd need to switch to manual instrumentation.

## Step 1 Get the Dynatrace access details

### Determine the API base URL

For details on how to assemble the base OTLP endpoint URL, see [Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."). The URL should end in `/api/v2/otlp`.

### Get API access token

To generate an access token, in Dynatrace, go to ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

[Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api#authentication "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") has more details on the format and the necessary access scopes.

## Step 2 Instrument your application

The following example uses `opentelemetry-distro` to configure all available and applicable instrumentation libraries automatically. Instead, you could also skip steps 1 and 2 and selectively add instrumentation libraries by [installing `opentelemetry-instrumentation`﻿](https://pypi.org/project/opentelemetry-instrumentation/) and the applicable [instrumentation libraries﻿](https://github.com/open-telemetry/opentelemetry-python-contrib/blob/main/instrumentation/README.md) manually.

1. Use [pip﻿](https://pypi.org/project/pip/) to install the following packages.

   ```
   pip install opentelemetry-distro



   pip install opentelemetry-exporter-otlp
   ```
2. Run the following command to initialize and bootstrap the automatic instrumentation.

   ```
   opentelemetry-bootstrap -a install
   ```
3. Configure the following environment variables to set the service and export details, substituting `[URL]` and `[TOKEN]` with the values for the [base URL](#base-url) and [access token](#access-token).

   ```
   OTEL_EXPORTER_OTLP_ENDPOINT=[URL]



   OTEL_EXPORTER_OTLP_HEADERS="Authorization=Api-Token%20[TOKEN]"



   OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=delta



   OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf



   OTEL_SERVICE_NAME="python-quickstart"
   ```

   URL encoding in environment variables

   Please note that the space in `OTEL_EXPORTER_OTLP_HEADERS` is encoded as `%20` as the variable [follows the correlation context convention﻿](https://opentelemetry.io/docs/specs/otel/protocol/exporter/#specifying-headers-via-environment-variables) and its [value needs to be percent-encoded﻿](https://github.com/w3c/baggage/blob/main/baggage/HTTP_HEADER_FORMAT.md#value).
4. Run your application with the `opentelemetry-instrument` agent.

   ```
   opentelemetry-instrument python myapp.py
   ```

## Step 3 optional Add telemetry signals manually Optional

As automatic instrumentation on Python does not provide pre-configured tracer and meter providers, you'd need to follow the [initialization](/managed/ingest-from/opentelemetry/walkthroughs/python/python-manual#instrument "Learn how to instrument your Python application using OpenTelemetry and Dynatrace.") and [instrumentation](/managed/ingest-from/opentelemetry/walkthroughs/python/python-manual#add-telemetry-signals-manually "Learn how to instrument your Python application using OpenTelemetry and Dynatrace.") steps at [Manually instrument your Python application with OpenTelemetry](/managed/ingest-from/opentelemetry/walkthroughs/python/python-manual "Learn how to instrument your Python application using OpenTelemetry and Dynatrace."), if you wish to manually add custom signals (such as traces and metrics) on top of automatic instrumentation.

## Step 4 Ensure context propagation

Context propagation is particularly important when network calls (for example, REST) are involved.

With automatic instrumentation, this should be automatically taken care of by the instrumentation libraries. If the used network libraries are not be covered by that, you would need to switch to [manual instrumentation](/managed/ingest-from/opentelemetry/walkthroughs/python/python-manual "Learn how to instrument your Python application using OpenTelemetry and Dynatrace.") instead and handle propagation manually.

## Step 5 optional Configure data capture to meet privacy requirements Optional

While Dynatrace automatically captures all OpenTelemetry attributes, only attribute values specified in the allowlist are stored and displayed in the Dynatrace web UI. This prevents accidental storage of personal data, so you can meet your privacy requirements and control the amount of monitoring data stored.

To view your custom attributes, you need to allow them in the Dynatrace web UI first. To learn how to configure attribute storage and masking, see [Attribute redaction](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Learn how to enable and configure the OneAgent Span Sensor for OpenTelemetry data.").

## Step 6 Verify data ingestion into Dynatrace

Once you have finished the instrumentation of your application, perform a couple of test actions to create and send demo traces, metrics, and logs and verify that they were correctly ingested into Dynatrace.

To do that for traces, go to **Distributed Traces** and select the **Ingested traces** tab. If you use OneAgent, select **PurePaths** instead.

For metrics and logs, go to **Metrics** or **Logs**.

## Related topics

* [Enrich ingested data with Dynatrace-specific fields](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")