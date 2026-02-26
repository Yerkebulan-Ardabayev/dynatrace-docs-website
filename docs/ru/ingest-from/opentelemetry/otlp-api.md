---
title: Dynatrace OTLP API endpoints
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/otlp-api
scraped: 2026-02-26T21:17:36.933371
---

# Dynatrace OTLP API endpoints

# Dynatrace OTLP API endpoints

* Latest Dynatrace
* Explanation
* 8-min read
* Updated on Jan 09, 2026

The [OpenTelemetry Protocol (OTLP)ï»¿](https://opentelemetry.io/docs/specs/otlp/) is the principal network protocol for the exchange of telemetry data between OpenTelemetry-backed services and applications.

Dynatrace provides native OTLP endpoints with the following services:

* The Dynatrace SaaS platform.
* ActiveGate instances.

Alternatively, you can deploy the [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector "Learn about the Dynatrace OTel Collector.") as an intermediary service application to batch requests and improve network performance, or to transform requests before forwarding them to Dynatrace (for example, [mask sensitive data](/docs/ingest-from/opentelemetry/collector/use-cases/redact "Configure the OpenTelemetry Collector to mask sensitive data before forwarding to Dynatrace.")).

## Default ingest paths

The ingest paths used by Dynatrace for the individual signal types follow the [standard OpenTelemetry pathsï»¿](https://opentelemetry.io/docs/specs/otel/protocol/exporter/#endpoint-urls-for-otlphttp).

| Signal Type | Path |
| --- | --- |
| Traces | `/v1/traces` |
| Metrics | `/v1/metrics` |
| Logs | `/v1/logs` |

Depending on the configuration, you may need to append these paths individually to the base URLs of the following service endpoints when specifying the export URLs. This can happen either in-code, when using [manual instrumentation](/docs/ingest-from/opentelemetry/walkthroughs "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace."), or using the standard [environment variablesï»¿](https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter/#endpoint-configuration).

## Export to Dynatrace

### Base URLs

The following addresses provide the base URLs for your OTLP ingest configuration. Use the URL applicable to your type of environment and replace the relevant part with your [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
You will also use the base URL if you define the `OTEL_EXPORTER_OTLP_ENDPOINT` environment variable, see [Environment variables](#environment-variables).

| API Type | Base URL |
| --- | --- |
| Dynatrace SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp` |
| Environment ActiveGate[1](#fn-1-1-def) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp` |
| Containerized Environment ActiveGate[2](#fn-1-2-def) | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/otlp` |

1

Environment ActiveGates listen by default on port `9999`. If you changed that port, adjust the port in the URL accordingly.

2

A [PVC](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/activegate-pvc "Set up a persistent storage for containerized ActiveGate to be used as temporary storage for ingested data.") is required for this setup.

If you copy your environment ID from the browser's address bar, make sure to remove `.apps`.

* Incorrect base URL: `https://{your-environment-id}.live.apps.dynatrace.com/api/v2/otlp`
* Correct base URL: `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`

Otherwise, the API calls will return an error that looks like this:

```
not retryable error: Permanent error: rpc error: code = Unimplemented desc = error exporting items, request to https://<environment>.live.apps.dynatracelabs.com/api/v2/otlp/v1/logs responded with HTTP Status Code 404
```

### URL examples

The following example URLs illustrate combinations of base URLs and paths for signal types.

#### Dynatrace SaaS

#### Environment ActiveGate

Information enrichment

Vanilla OTLP exports to ActiveGate require manual enrichment of Dynatrace host information to have the proper topology information.

To do so, make sure your traces have the correct mapping resource attributes set. The list of applicable attributes can be found in (or imported from) the [enrichment files](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.").

### API limitations

Calls to Dynatrace API endpoints have the following limitations.

* gRPC is not supported.
  API calls need to use HTTP.
  You can use a Collector to transform a gRPC OTLP request to its HTTP counterpart, see [Transform OTLP gRPC to HTTP with the OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/use-cases/grpc "Configure the OpenTelemetry Collector to transform a gRPC OTLP request to HTTP.").
* JSON is not supported for Protocol Buffers.
  Binary format must be used.

### Environment variables

When you configure your application to export to Dynatrace, one way is to configure certain environment variables as described below.

```
OTEL_EXPORTER_OTLP_ENDPOINT=[YOUR_BASE_URL]



OTEL_EXPORTER_OTLP_HEADERS="Authorization=Api-Token [YOUR_TOKEN]"



OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
```

For more information about language-specific configuration, see [Instrument your application](/docs/ingest-from/opentelemetry/walkthroughs "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.").

### Authentication and access tokens

For exports to SaaS and ActiveGate, authentication is handled using an API access token and the `Authorization` HTTP header.
For more information on access tokens, see [Dynatrace API - Tokens and authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

To create an access token, in Dynatrace, go to ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.
Use the appropriate access scopes for the signals that you want to export.
You can combine scopes in a single token, and also add scopes to an existing token.

* Traces: `openTelemetryTrace.ingest`
* Metrics: `metrics.ingest`
* Logs: `logs.ingest`

### Network requirements

Verify that the following are true:

* TCP port is not blocked

  Because OTLP communication with ActiveGate takes place over the ports 443 (for SaaS and Managed) or 9999 (for Environment ActiveGates), make sure that the TCP port in question is not blocked by a firewall or any other network management solution you might be using.
* Your system's certificate trust store is up to date

  To avoid possible SSL certificate issues with expired or missing default root certificates, make sure that your system's certificate trust store is up to date.

## Export to the Collector

Using the Collector as an intermediate gateway allows you to streamline and optimize your telemetry data and requests centrally. See [OpenTelemetry Collector use cases](/docs/ingest-from/opentelemetry/collector/use-cases "Configure your Collector instance for different use cases.") for more information and sample configurations for popular Collector use cases.

See [Dynatrace OTel Collector](/docs/ingest-from/opentelemetry/collector "Learn about the Dynatrace OTel Collector.") for more details on how to configure a Collector instance.

gRPC conversion

As Dynatrace currently requires OTLP exports with HTTP, you can use the Collector to convert gRPC exports to HTTP.

See [Transform OTLP gRPC to HTTP with the OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/use-cases/grpc "Configure the OpenTelemetry Collector to transform a gRPC OTLP request to HTTP.") for more details.

### Authentication and TLS

Whether you need to use TLS and authenticate your requests against the Collector depends on your particular Collector setup/configuration. By default, the [OTLP receiverï»¿](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.145.0/receiver/otlpreceiver/README.md) is configured for plain-text HTTP and does not require authentication.

The eventual outbound connection from the Collector to Dynatrace always requires authentication and TLS.

### Network requirements

Verify that the following are true:

* Network ports not blocked

  Make sure the network ports required by the configured receiver instances are not blocked by a firewall or any other network management solution used as part of your infrastructure.

## Related topics

* [OpenTelemetry Protocol (OTLP) ingest API](/docs/dynatrace-api/environment-api/opentelemetry "Use Dynatrace API as a target for OpenTelemetry exporters to ingest OpenTelemetry metrics, logs, and traces.")