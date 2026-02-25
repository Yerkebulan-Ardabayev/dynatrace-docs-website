---
title: Ingest OTLP logs
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/otlp-api/ingest-logs
scraped: 2026-02-25T21:34:07.164311
---

# Ingest OTLP logs

# Ingest OTLP logs

* Latest Dynatrace
* Reference
* 3-min read
* Updated on Feb 10, 2026

OpenTelemetry supports attributes at different levels in an OpenTelemetry log request, such as the resource level, scope level, and record level.

The Log ingestion API collects and attempts to automatically transform log data.

## Data transformation

Each log record from the ingested batch is mapped to a single Dynatrace log record, which contains three special attributes: `timestamp`, `loglevel`, `content`, and a set of other key-value attributes. These properties are set based on keys present in the input object as follows.

### Timestamp

* Set based on the **Timestamp** field of the input log record.

* If the `timestamp` cannot be set based on the **Timestamp** field, `timestamp` is determined based on the OTLP log record. See the differences between data models in the [Log ingestion API processing](#otlp-structured-logs) section below for more details.

* Supported timestamp formats: `UTC milliseconds`, `RFC3339`, and `RFC3164`.
* The default value is the current timestamp and the default timezone is UTC if it's missing in timestamp.
* Log events older than the **Log Age** limit are discarded. Timestamps more than 10 minutes ahead of the current time are replaced with the current time. See the [Ingestion limits](#ingestion-limits) section for details.

### Log level

* Set based on the **SeverityText** field (first priority) or **SeverityNumber** field (second priority) of the input log record.

* If the `loglevel` cannot be set based on the **SeverityText** or **SeverityNumber** field, `loglevel` is determined based on the OTLP log record. See the differences between data models in the section [Log ingestion API processing](#otlp-structured-logs) below for more details.

* The default value is `NONE`.

### Content

* The content is set based on the **Body** field of the input log record.

* If the **Body** field is not a string type, the value is stringified. In case of complex types, it is stringified as a JSON string. For kvlist\_value type, see the differences between data models in the [Log ingestion API processing](#otlp-structured-logs) section below for more details.

### Attributes

* Contains all other attributes from the input record's attributes contained in the sections: **Resource**, **InstrumentationScope**, and **Attributes**.
* The `TraceID` and `SpanID` attributes are mapped to the `trace_id` and `span_id` fields, and their values are converted to hexadecimal representation (e.g., `0xCAFEBABE`).
* Automatic attribute. The `dt.auth.origin` attribute is automatically added to every log record ingested via API. This attribute is the public part of the API key that the log source authorizes to connect to the generic log ingest API.

All attributes should preferably map to **semantic attributes** for Dynatrace to interpret them correctly.

* Logs on Grail: All attributes can be used in queries, though Semantic Dictionary helps Davis AI in the interpretation of the logs. Refer to the [Semantic Dictionary](/docs/semantic-dictionary "The Semantic Dictionary defines standardized field names used across monitoring data types like logs, events, spans, metrics, and entities.") for more details.
* Log Monitoring Classic: Refer to the [Semantic attributes (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api/log-classic-semantic-attributes "Supported semantic attributes that are indexed in Log Monitoring Classic.") for more details.

## Data types

Dynatrace supports OpenTelemetry data types as described in the sections below.

### Scalar value

Scalar values are transformed as follows:

* Logs on Grail with OpenPipeline custom processing (Dynatrace SaaS version 1.295+, Environment ActiveGate version 1.295+): All JSON data types (string, number, boolean, null) are supported. All attributes can be used in queries. Keys are case-sensitive.
* Logs on Grail with OpenPipeline routed to Classic Pipeline: All attribute keys are lowercased and all attribute values are stringified. All attributes can be used in queries.
* Log Monitoring Classic: All attribute keys are lowercased and all attribute values are stringified. Custom attributes and semantic attributes can generally be used in queries.

### Byte array

Byte arrays are converted to base64-encoded strings. For example, the following array

```
[0x68, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0x77, 0x6f, 0x72, 0x6c, 0x64]
```

is transformed and ingested as `aGVsbG8gd29yZA==`.

### Array

Array attribute values are converted to arrays of a uniform type. The target type is chosen according to the following rules:

* Complex values, such as arrays, or objects are mapped to JSON string values.
* If any value in the array is a string, or if any value must be converted to a string (e.g., an object or array), the target type of the entire array is string.
* If all values in the source array are numeric, the target array type is numeric.
* Null values are considered compatible with any type.

### Map

Map processing depends on the data model used. See [Log ingestion API processing](#otlp-structured-logs) below for more details.

## Ingestion limits

See [Log Management and Analytics default limits](/docs/analyze-explore-automate/logs/lma-limits "Default limits for the latest version of Dynatrace Log Management and Analytics.") and [Log Monitoring default limits (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/log-monitoring-limits "Default limits for the latest version of Dynatrace Log Monitoring.") for the limits applied to ingested log requests, their attributes, and their attribute values.

## Log ingestion API processing

There are two data models that identify how structured logs are processed by log ingestion endpoints: **raw** and **flattened**. The difference between the two is in how attributes with object/dictionary values are transformed.

If this configuration option is not specified, the default behavior depends on when your environment was created.

* For Dynatrace version 1.331+: Raw.
* For Dynatrace versions 1.330 and earlier: Flattened.

Escaping in output examples is for visualization purposes only. `\"` is billed as one character.

### Raw data model

The raw data model transforms the content of structured logs as described in the sections below. All the following examples apply to Log ingestion API endpoints available on Environment ActiveGate and SaaS.

When using log shippers such as [Fluentbit](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-fluent-bit "Integrate Fluent Bit to stream logs to Dynatrace."), [Fluentd](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-fluentd-k8s "Integrate Fluentd with Dynatrace to stream logs from nodes and pods to Dynatrace.") or [Logstash](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-logstash "Integrate Logstash to stream logs from nodes and pods to Dynatrace."), avoid using JSON parsers on the shipper side and let Dynatrace handle the JSON parsing instead. This approach reduces processing overhead on your log shipper and ensures consistent parsing behavior.

#### Maps and arrays in attributes

For the raw data model, the map attribute values are turned into a JSON string, and the array attribute values are turned into an array of the uniform type.

#### Map in body

In this case, the **Body** field of the input log record is converted to a JSON string.

#### Body as array

In this case, the array in the body is stringified.

#### Timestamp

If the `timestamp` cannot be set based on the **Timestamp** field, `timestamp` is determined based on the attributes of the OTLP log record and is set based on the value of the first key found from the following list, evaluated in the order presented in the list, and is case-insensitive: `timestamp`, `@timestamp`, `_timestamp`, `eventtime`, `date`, `published_date`, `syslog.timestamp`, `time`, `epochSecond`, `startTime`, `datetime`, `ts`, `timeMillis`, `@t`.

#### Log level

If the `loglevel` cannot be set based on the **SeverityText** or **SeverityNumber** field, `loglevel` is determined based the attributes of the OTLP log record and is set based on the value of the first key from the following list, evaluated in the order presented in the list, and is case-insensitive: `loglevel`, `status`, `severity`, `level`, `syslog.severity`.

#### Name conflicts

In the raw data model, OTLP resource attributes and OTLP attributes are copied into Dynatrace top-level attributes, and the OTLP body is copied into the content.

Dynatrace prefixes duplicate attributes with an incrementing counter, for example `overwritten1.myattribute`. The counter value indicates how many times the attribute has been encountered as a duplicate. This avoids name collisions when attributes at different OTLP levels share the same name.

### Flattened data model

With the flattened data model, the content of structured logs is transformed as described in the sections below. All the following examples apply to Log ingestion API endpoints available on Environment ActiveGate and SaaS.

#### Maps and arrays in attributes

In this case, the map attribute values are flattened, i.e. replaced with keys concatenated using a dot (.) until a simple value is reached in the hierarchy, and the array attribute values are turned into a custom string.

Flattening proceeds up to the maximum nesting level specified by the **Nested objects** limit. Structures nested deeper than this are replaced with the string value `<truncated due to nesting limit>`. See the [Ingestion limits](#ingestion-limits) section for details.

#### Map in body

If the **Body** field is of **kvlist\_value** type (a list of key-value pairs), the structure is processed in the same way as log record attributes, including flattening and conflict resolution.

Attributes found in **Body** may also be used for setting the `timestamp`, `loglevel`, and `content` attributes of the log record, as described below.

#### Body as array

In this case, the array in the body is stringified.

#### Timestamp

If the `timestamp` cannot be set based on the **Timestamp** field, `timestamp` is set determined based on one of the following, evaluated in order:

1. The content of the body (if the body is a map).
2. The attributes of the OTLP log record.

If the timestamp is taken from the body or OTLP log record, it is set based on the value of the first key found from the following list, evaluated in the order presented in the list, and is case-insensitive: `timestamp`, `@timestamp`, `_timestamp`, `eventtime`, `date`, `published_date`, `syslog.timestamp`, `time`, `epochSecond`, `startTime`, `datetime`, `ts`, `timeMillis`, `@t`.

#### Log level

If the `loglevel` cannot be set based on the **SeverityText** or **SeverityNumber** field, `loglevel` is determined based on one of the following, evaluated in order:

1. The content of the body (if the body is a map).
2. The attributes of the OTLP log record.

If the `loglevel` is taken from the body or OTLP log record, it is set based on the value of the first key from the following list, evaluated in the order presented in the list, and is case-insensitive: `loglevel`, `status`, `severity`, `level`, `syslog.severity`.

#### Content

If the **Body** field is of **kvlist\_value** type (a list of key-value pairs), `content` is set based on the value of the first key found in **Body** from the following list, evaluated in the order presented in the list: `content`, `message`, `payload`, `body`, `log`.

If no attribute is found among supported content keys, `content` is set to an empty string.

#### Name conflicts

When attributes are saved in a flattened fashion on the Dynatrace side, there may be name collisions if attributes on different levels share the same name. Dynatrace resolves this by prefixing duplicate attributes with `overwritten[COUNTER].`. The counter value indicates how many times the attribute name has been already encountered as a duplicate.

For example, if you have three attributes all named `my.attribute` on the resource, scope, and log levels:

* the resource attribute is ingested as `my.attribute`
* the scope attribute is ingested as `overwritten1.my.attribute`
* the log attribute is ingested as `overwritten2.my.attribute`

## Additional attributers handling

The Log ingestion API additionally accepts log attributes through:

* Query parameters
* Special header: `X-Dynatrace-Attr`

These attributes are merged with those provided in the OpenTelemetry log request according to the rules described below.

### Query parameter attributes

* All query parameters passed to the Log ingestion API endpoint are added to the log record attributes.
* If a parameter key appears multiple times, all values are captured as an array attribute.
* Keys and values follow the same attribute parsing rules as log request attributes.
* Certain parameters are processed by the API for internal purposes and never appear as log record attributes, even if explicitly provided (such as those used in the **XâDynatraceâOptions** header). For the complete list of reserved parameter names and their processing behavior, see the [API documentation](/docs/dynatrace-api/environment-api/opentelemetry/post-logs#parameters "Send OpenTelemetry logs to Dynatrace via API.").

#### Example

### Header-based attributes (X-Dynatrace-Attr)

The API supports a special header for passing additional attributes:

```
otlphttp:



endpoint: /api/v2/otlp



headers:



X-Dynatrace-Attr: region=eu-central-1&team=core
```

Rules:

* Keys and values follow the same attribute parsing rules as query parameters.
* Multi-value behavior is also supported inside the header attributes.
* Same reserved parameter names restrictions apply.

### Attributes precedence rules

When attributes appear in multiple places, the Log ingestion API applies attribute precedence while still preserving body values for auditability. The attributes are applied in the following order:

* Query Parameters (highest precedence)
* X-Dynatrace-Attr header
* OpenTelemetry log request (lowest precedence; existing ingestion path)

#### Override behavior

When attributes from query parameters or the header override log request attributes:

* The final attribute value is set according to the attribute source precedence rules.
* The values already present in the log request are preserved and mirrored under `overwrittenN.<attribute_key>`.
  Where N is an incrementing integer (1, 2, â¦) depending on how many log request-originating values had to be preserved. This ensures uniqueness, even when multiple conflicts occur.
* Only values originating from the log request are preserved under the `overwrittenN.*` keys. Attributes overridden by higher-precedence sources do not generate overwritten copies.

#### Example

### Billing behavior

Attributes provided through query parameters or headers are included in billing calculations.

For multi-value attributes, the attribute key contributes to billing only once, regardless of how many values are present.

## Related topics

* [OpenTelemetry logs ingest API](/docs/dynatrace-api/environment-api/opentelemetry/post-logs "Send OpenTelemetry logs to Dynatrace via API.")