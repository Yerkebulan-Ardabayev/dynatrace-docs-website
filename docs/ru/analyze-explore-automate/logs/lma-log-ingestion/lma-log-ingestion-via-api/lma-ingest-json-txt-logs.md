---
title: Ingest JSON and TXT logs
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api/lma-ingest-json-txt-logs
scraped: 2026-03-01T21:24:39.643174
---

# Ingest JSON and TXT logs

# Ingest JSON and TXT logs

* Latest Dynatrace
* Explanation
* 15-min read
* Updated on Feb 06, 2026

The Log ingestion API ingests logs in JSON, TXT, and OTLP formats. On this page, we will describe the JSON and text formats. For OTLP documentation, refer to the [OTLP](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs#otlp-structured-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.") formats.

The Log ingestion API is responsible for collecting the data and forwarding it to Dynatrace in batches.

* SaaS endpoints: `https://{your-environment-id}.live.dynatrace.com/api/v2/logs/ingest`.
  The Log ingestion API endpoint is available in your Dynatrace environment.
* Environment ActiveGate endpoints: `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/logs/ingest`.
  The Log ingestion API is automatically enabled after you [install an ActiveGate](/docs/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate")

For details regarding supported payloads, authentication, parameters, and body objects, refer to [Log Monitoring API v2 - POST ingest logs](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.").

For details regarding limitations, refer to [Log Management and Analytics default limits](/docs/analyze-explore-automate/logs/lma-limits "Default limits for the latest version of Dynatrace Log Management and Analytics.").

## Data transformation and automatic JSON parsing

The Log ingestion API collects and attempts to automatically transform log data. Each log record from the ingested batch is mapped to a single Dynatrace log record, which contains three special attributes: `timestamp`, `loglevel`, `content`, and key-value attributes. These four properties are set based on keys present in the input JSON object as follows.

### Timestamp

* `timestamp` is set based on the value of the first found key from the following list, evaluated in the order presented here, and is case-insensitive: `timestamp`, `@timestamp`, `_timestamp`, `eventtime`, `date`, `published_date`, `syslog.timestamp`, `time`, `epochSecond`, `startTime`, `datetime`, `ts`, `timeMillis`, `@t`.
* Supported formats are: `UTC milliseconds`, `RFC3339`, and `RFC3164`.

  For unsupported timestamp formats, the current timestamp is used, and the value of the unsupported format is stored in the `unparsed_timestamp` attribute.
* Log records older than the [log age limit](/docs/analyze-explore-automate/logs/lma-limits#log-ingestion-limits "Default limits for the latest version of Dynatrace Log Management and Analytics.") are discarded. Timestamps more than 10 minutes ahead of the current time are replaced with the current time.
* If there is no supported timestamp key in the log record, the default value is the current timestamp.
* If there is no timezone in the timestamp, the default timezone is UTC.

### Log level

* `loglevel` is set based on the value of the first found key from the following list, evaluated in the order presented here, and is case-insensitive: `loglevel`, `status`, `severity`, `level`, `syslog.severity`.
* The default value is `NONE`.

### Content

* `content` is set based on the value of the first found key from the following list, evaluated in the order presented here, and is case-insensitive: `content`, `message`, `payload`, `body`, `log`, `_raw` (supported only in the raw data model).
* The default value and handling depends on the data model used for processing the input.

### Attributes

* Log attributes contain all other keys from the input JSON object except those used for `timestamp`, `loglevel`, and `content`.
* First-level attributes should preferably map to semantic attributes for Dynatrace to map them to context. All attributes can be used in queries, though Semantic Dictionary helps Davis AI in the interpretation of the logs. See [Semantic Dictionary](/docs/semantic-dictionary "The Semantic Dictionary defines standardized field names used across monitoring data types like logs, events, spans, metrics, and entities.") for more details.
* Automatic attribute. The `dt.auth.origin` attribute is automatically added to every log record ingested via API. This attribute is the public part of the API key that the log source authorizes to connect to the generic log ingest API.

Attribute processing differs depending on tenant and environment type:

* Logs on Grail with OpenPipeline custom processing (Dynatrace SaaS version 1.295+, Environment ActiveGate version 1.295+): Supports rich data types, enabling the use of diverse attributes in queries. Keys are case-sensitive.
* Logs on Grail with OpenPipeline routed to Classic Pipeline: All attribute keys are lowercased and all attribute values are stringified. All attributes can be used in queries.

## Data models

There are two data models that identify how structured logs are processed by log ingestion endpoints: **raw** and **flattened**. The difference between the two is in how attributes with object values are transformed.

If this configuration option is not specified, the default behavior depends on when your environment was created.

* For Dynatrace version 1.331+: Raw.
* For Dynatrace versions 1.330 and earlier: Flattened.

Escaping in output examples is for visualization purposes only. `\"` is billed as one character.

### Raw data model

The raw data model preserves the original log structure and context, maintaining data integrity. This results in easy interaction and querying, because log record representation in Dynatrace remains the same as in the source.

We recommend using this approach for highly nested JSON logs, as it maintains the semantic meaning and relationships between data points.

When using log shippers such as [Fluentbit](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-fluent-bit "Integrate Fluent Bit to stream logs to Dynatrace."), [Fluentd](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-fluentd-k8s "Integrate Fluentd with Dynatrace to stream logs from nodes and pods to Dynatrace.") or [Logstash](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-logstash "Integrate Logstash to stream logs from nodes and pods to Dynatrace."), avoid using JSON parsers on the shipper side and let Dynatrace handle the JSON parsing instead. This approach reduces processing overhead on your log shipper and ensures consistent parsing behavior.

The raw data model transforms the content of structured logs as described in the sections below.

#### Attributes with non-primitive types

Object attribute types are preserved as JSON strings. Further Dynatrace ingest stages (**OpenPipeline**, **Logs app**) support this format for easy log processing and analysis.

Array types are preserved as arrays but the contained types are unified to a single type.

* Complex values (such as arrays or objects) are mapped to JSON string values.
* If any value in the array is a string, or if any value must be converted to a string (e.g., an object or array), the target type of the entire array is string.
* If all values in the source array are numeric, the target array type is numeric.
* Null values are considered compatible with any type.

#### Content handling

The selected input content field is always selected regardless of its type, and is converted to string type if necessary.

An example of a supported content attribute with an array value is given below.

If no attribute from the supported content attributes is present in the input, the target `content` attribute is set to an empty string.

The first attribute from the supported content attributes list is selected for the output `content` field.

The `_raw` attribute is used as `content` only if no higher-priority supported content attribute is present.

### Flattened data model



The flattened data model provides direct access to attribute values through simple key paths.

This approach is provided for compatibility reasons. It might also suit specific use cases, for example, when all nested JSON values need to be available at the root level.

#### Attributes with non-primitive types

In the flattened data model, nested objects in your log attributes are transformed into flat value pairs.

When a log attribute contains an object, each nested property becomes a separate attribute. This process works for attributes up to level five, while attributes beyond that level are skipped.

Array types are preserved as arrays but the contained types are unified to a single type.

* Complex values (such as arrays or objects) are mapped to JSON string values.
* If any value in the array is a string, or if any value must be converted to a string (e.g., an object or array), the target type of the entire array is string.
* If all values in the source array are numeric, the target array type is numeric.
* Null values are considered compatible with any type.

##### Name conflicts

When attributes are saved in a flattened fashion on the Dynatrace side, there may be name collisions if attributes on different levels share the same name. Dynatrace resolves this by prefixing duplicate attributes with `overwritten[COUNTER].`. The counter value indicates how many times the attribute name has been already encountered as a duplicate. For example:

* If a second conflict arises, an index is added starting with 1:

#### Content related behavior

The rules below define how the `content` field is selected and constructed.

##### No supported content attribute found

In case no supported content attribute is found, the whole JSON representation of the log event is set as the `content` field of the output log record. The original JSON is preserved as-is.

The `_raw` field is not among the supported content fields for this data model.

##### Complex values in supported content attributes

Any attribute that is an object, including `content`, is treated as a standard attribute.

## Log ingestion API attribute handling

The Log Ingestion API additionally accepts log attributes through:

* Query parameters
* Special header: `X-Dynatrace-Attr`

These attributes are merged with those provided in the log record body according to the rules described below.

### Query parameter attributes

* All query parameters passed to the Log ingestion API endpoint are added to the log record body attributes.
* If a parameter key appears multiple times, all values are captured as an array attribute.
* Keys and values follow the same attribute parsing rules as body attributes.
* Certain parameters are processed by the API for internal purposes and never appear as log record attributes, even if explicitly provided (such as those used in the **XâDynatraceâOptions** header). For the complete list of reserved parameter names and their processing behavior, see the [API documentation](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs#parameters "Push custom logs to Dynatrace via the Log Monitoring API v2.").

#### Example

### Header-based attributes (X-Dynatrace-Attr)

The API supports a special header for passing additional attributes:

`X-Dynatrace-Attr: region=eu-central-1&team=core`

Rules:

* Keys and values follow the same attribute parsing rules as query parameters.
* Multi-value behavior is also supported inside the header attributes.
* Same reserved parameter names restrictions apply.

### Attributes precedence rules

When attributes appear in multiple places, the Log ingestion API applies attribute precedence while still preserving body values for auditability. The attributes are applied in the following order:

* Query Parameters (highest precedence)
* X-Dynatrace-Attr header
* Log record body (lowest precedence; existing ingestion path)

#### Override behavior

When attributes from query parameters or the header override body attributes:

* The final attribute value is set according to the attribute source precedence rules.
* The values already present in the log body are preserved and mirrored under `overwrittenN.<attribute_key>`.
  Where N is an incrementing integer (1, 2, â¦) depending on how many body-originating values had to be preserved. This ensures uniqueness even when multiple conflicts occur.
* Only values originating from the log body are preserved under the `overwrittenN.*` keys. Attributes overridden by higher-precedence sources do not generate overwritten copies.

#### Example

### Billing behavior

Attributes provided through query parameters or headers are included in billing calculations.

For multi-value attributes, the attribute key contributes to billing only once, regardless of how many values are present.

## Related topics

* [Log Monitoring API v2 - POST ingest logs](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.")
* [Automatic log enrichment](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api/lma-log-data-transformation "Log ingestion API automatically transforms log data into output values for the loglevel attribute.")