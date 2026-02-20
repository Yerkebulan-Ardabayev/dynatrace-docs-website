---
title: Mask sensitive data with the OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/redact
scraped: 2026-02-20T21:14:45.458343
---

# Mask sensitive data with the OpenTelemetry Collector

# Mask sensitive data with the OpenTelemetry Collector

* Latest Dynatrace
* How-to guide
* 5-min read
* Updated on Jan 12, 2026

Telemetry data can often include sensitive data (such as [PIIï»¿](https://en.wikipedia.org/wiki/Personal_data)), which may need to be redacted due to security and regulatory reasons. While this can be implemented on the application side, it typically is best to handle this centrally using gateways such as the Collector. This enables the single-point management of redaction rules across all your applications and services, without the need to update your code each time a new redaction rule is required.

This page shows sample Collector configurations for the redaction of specific sensitive data (for example, credit card numbers or email addresses) which may appear in telemetry data and which should be masked/redacted before leaving your network.

## Prerequisites

* One of the following Collector distributions with the [transformï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/transformprocessor) and/or [redactionï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/redactionprocessor) processors:

  + The [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Learn about the Dynatrace OTel Collector.")
  + [OpenTelemetry Contrib](/docs/ingest-from/opentelemetry/collector#collector-contrib "Learn about the Dynatrace OTel Collector.")
  + A [custom Builder version](/docs/ingest-from/opentelemetry/collector#collector-builder "Learn about the Dynatrace OTel Collector.")
* The [Dynatrace API endpoint URL](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported
* An [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope (only required for SaaS and ActiveGate)

See [Collector Deployment](/docs/ingest-from/opentelemetry/collector/deployment "How to deploy Dynatrace OTel Collector.") and [Collector Configuration](/docs/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.

## Redaction processor versus transform processor

The following examples make use of these two Collector [processorsï»¿](https://opentelemetry.io/docs/collector/architecture/#processors):

* the [transform processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/transformprocessor/README.md)
* the [redaction processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/redactionprocessor/README.md)

While the following examples use both processors to mask data, each processor has its own distinct purpose. The redaction processor is straightforward and takes a list of values, based on which matching data will be completely redacted. On the other hand, the purpose of the transform processor is more versatile and goes beyond mere data redaction.

For data redaction, typically either processor can be used and you may want to choose the one best for your use case. For example, for full data redaction, the redaction processor may be easier to use. On the other hand, partial data redaction can only be achieved with the transform processor. In addition, the transform processor can also filter by data in the body of logs, whereas the redaction processor only has access to attributes.

## Limitations and considerations

The examples provided on this page are samples demonstrating common redaction scenarios. Note the following:

* The examples may not be exhaustive for all use cases. You may need to adapt them to your specific requirements.
* The regex patterns and attribute matching only work when the entire attribute value matches the pattern to be redacted. Partial matches within larger strings may require more complex patterns or additional processing.
* The span name is stored as a separate field in the OTLP message structure, not as an attribute. Therefore, redaction processors targeting attributes will not affect span names by default. See the [Span names](#span-names) example for how to handle this.
* Processor order in pipelines matters. Apply transform/redaction before routing or exporting, and keep related processors adjacent so downstream steps see the sanitized data.

## Demo configuration

This YAML document is a basic Collector configuration skeleton, containing basic, general components (that is, receivers, exporters, and the pipeline definition).

```
receivers:



otlp:



protocols:



grpc:



endpoint: 0.0.0.0:4317



http:



endpoint: 0.0.0.0:4318



processors:



PLACEHOLDER-FOR-PROCESSOR-CONFIGURATIONS



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



"Authorization": "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



traces:



receivers: [otlp]



processors: [PLACEHOLDER-FOR-PROCESSOR-REFERENCES]



exporters: [otlp_http]



metrics:



receivers: [otlp]



processors: [PLACEHOLDER-FOR-PROCESSOR-REFERENCES]



exporters: [otlp_http]



logs:



receivers: [otlp]



processors: [PLACEHOLDER-FOR-PROCESSOR-REFERENCES]



exporters: [otlp_http]
```

Make sure to replace the placeholder values in the document with the respective configurations:

* `PLACEHOLDER-FOR-PROCESSOR-CONFIGURATIONS`: the relevant processor configuration
* `PLACEHOLDER-FOR-PROCESSOR-REFERENCES`: referencing the applicable processor objects for the individual signal types

### IP addresses

Using the transform processor, we mask the attribute `client.address` with the [`set` statementï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/pkg/ottl/ottlfuncs/README.md#set).

```
transform:



error_mode: ignore



trace_statements:



- context: span



statements: &filter-statements



# this will not only mask end user client IP addresses,



# but also the address of a server acting as a client when establishing a connection to another server



- set(attributes["client.address"], "<masked-clientip-ot>")



metric_statements:



- context: datapoint



statements: *filter-statements



log_statements:



- context: log



statements: *filter-statements
```

### Email addresses

Using the transform processor, we mask the attribute `user.email` with the [`set` statementï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/pkg/ottl/ottlfuncs/README.md#set).

```
transform:



error_mode: ignore



trace_statements:



- context: span



statements: &filter-statements



- set(attributes["user.email"], "<masked-email-ot>")



metric_statements:



- context: datapoint



statements: *filter-statements



log_statements:



- context: log



statements: *filter-statements
```

### Dynatrace API tokens

Using the redaction processor, we use the regular expression `dt0[a-z]0[1-9]\.[A-Za-z0-9]{24}\.([A-Za-z0-9]{64})` to mask all occurrences of [Dynatrace API tokens](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") in our telemetry data.

```
redaction:



allow_all_keys: true



blocked_values:



- dt0[a-z]0[1-9]\.[A-Za-z0-9]{24}\.([A-Za-z0-9]{64})



summary: info
```

### Usernames

Using the transform processor, we mask the attributes `user.id`, `user.name`, and `user.full_name` with the [`set` statementï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/pkg/ottl/ottlfuncs/README.md#set).

```
transform:



error_mode: ignore



trace_statements:



- context: span



statements: &filter-statements



- set(attributes["user.id"], "<masked-userid-ot>")



- set(attributes["user.name"], "<masked-username-ot>")



- set(attributes["user.full_name"], "<masked-userfullname-ot>")



metric_statements:



- context: datapoint



statements: *filter-statements



log_statements:



- context: log



statements: *filter-statements
```

### Credit card numbers

Using the transform processor, we configure three [`replace_all_patterns` statementsï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/pkg/ottl/ottlfuncs/README.md#replace_all_patterns) to mask any occurrences of credit card numbers and mask everything but the last four digits.

```
transform:



error_mode: ignore



trace_statements:



- context: span



statements: &filter-statements



- replace_all_patterns(attributes, "value", "^3\\s*[47](\\s*[0-9]){9}((\\s*[0-9]){4})$", "<masked-pcard$$2-ot>") where IsValidLuhn(attributes["value"])



- replace_all_patterns(attributes, "value", "^(5[1-5]([0-9]){2}|222[1-9]|22[3-9]\\d|2[3-6]\\d{2}|27[0-1]\\d|2720)(\\s*[0-9]){8}\\s*([0-9]{4})$", "<masked-pcard$$4-ot>") where IsValidLuhn(attributes["value"])



- replace_all_patterns(attributes, "value", "^4(\\s*[0-9]){8,14}\\s*(([0-9]\\s*){4})$", "<masked-pcard$$2-ot>") where IsValidLuhn(attributes["value"])



metric_statements:



- context: datapoint



statements: *filter-statements



log_statements:



- context: log



statements: *filter-statements
```

For credit card numbers, it is also possible to use the built-in, [standard OTTL function `IsValidLuhn()`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/pkg/ottl/ottlfuncs#isvalidluhn) instead of regular expressions, if you prefer to block values altogether instead of just masking them.

### IBAN numbers



Using the redaction processor, we use the regular expression `^[A-Z]{2}[0-9]{2}(\\s*[A-Z0-9]){8,30}$` to mask all IBAN occurrences in our telemetry data.

```
redaction:



allow_all_keys: true



blocked_values:



- "^[A-Z]{2}[0-9]{2}(\\s*[A-Z0-9]){8,30}$"



summary: info
```

### Span names

Span names are not stored as attributes in the OTLP message structure, so attribute-based redaction does not apply to them.
There are multiple ways of redacting and simplifying span names:

#### Generate a new span name

Recommended

`set_semconv_span_name` is available from Collector Contrib version 0.142.0 and .

Use the transform processor's [`set_semconv_span_name`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/transformprocessor#set_semconv_span_name) to derive a low-cardinality name that is compliant with OpenTelemetry semantic conventions. This will use the (low-cardinality) `http.request.method` and `http.route` to generate a new span name. It keeps the name consistent with HTTP/RPC/messaging/database conventions and avoids leaking identifiers.

```
transform:



error_mode: ignore



trace_statements:



- context: span



statements:



- set_semconv_span_name("1.37.0")
```

#### Redact the span name explicitly

```
transform:



error_mode: ignore



trace_statements:



- context: span



statements:



- replace_pattern(name, "(GET /api/v1/users/)\\d+", "$$1{id}")
```

Configuration validation

[Validate your settings](/docs/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Components

For our configuration, we use the following components.

### Receivers

Under `receivers`, we specify the standard `otlp` receiver as active receiver component for our Collector instance.

### Processors

Under `processors`, we place the configuration for the relevant processor instances.

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipelines

Under `service`, we eventually assemble all the configured objects into pipelines for the individual telemetry signals (traces, etc.) and have the Collector instance run the configured tasks.

## Related topics

* [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")