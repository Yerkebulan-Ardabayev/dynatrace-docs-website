---
title: Ingest JSON and TXT logs (Logs Classic)
source: https://docs.dynatrace.com/managed/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api/log-classic-ingest-json-txt-logs
---

# Ingest JSON and TXT logs (Logs Classic)

# Ingest JSON and TXT logs (Logs Classic)

* Explanation
* 5-min read
* Updated on May 04, 2026

Log Monitoring Classic

The Log ingestion API ingests logs in JSON, TXT, and OTLP formats. On this page, we will describe the JSON and text formats. For OTLP documentation, refer to the [OTLP](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs#otlp-structured-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.") formats.

Ingest endpoint will collect and attempt to automatically transform any log data containing the following JSON elements:

* Log content
* Timestamp
* Key-Values attributes

For details regarding limitations refer to [Log Monitoring default limits (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/log-monitoring-limits "Default limits for the latest version of Dynatrace Log Monitoring.").

## Data transformation and automatic JSON parsing

The Log ingestion API collects and attempts to automatically transform log data. Each log record from the ingested batch is mapped to a single Dynatrace log record, which contains three special attributes: `timestamp`, `loglevel`, `content`, and key-value attributes. These four properties are set based on keys present in the input JSON object as follows.

### Timestamp

* `timestamp` is set based on the value of the first found key from the following list, evaluated in the order presented in the list: `timestamp`, `@timestamp`, `_timestamp`, `eventtime`, `date`, `published_date`, `syslog.timestamp`, `time`, `epochSecond`, `startTime`, `datetime`, `ts`, `timeMillis`, `@t`.
* Supported formats are Unix epoch time in UTC, `RFC3339`, and `RFC3164`.
  Unix epoch time can be displayed in seconds, milliseconds, and Dynatrace version 1.339+ fractional seconds.

  For unsupported timestamp formats, the current timestamp is used, and the value of the unsupported format is stored in the `unparsed_timestamp` attribute.
* Log records older than the [log age limit](/managed/analyze-explore-automate/log-monitoring/log-monitoring-limits "Default limits for the latest version of Dynatrace Log Monitoring.") are discarded. Timestamps more than 10 minutes ahead of the current time are replaced with the current time.
* If there is no supported timestamp key in the log record, the default value is the current timestamp.
* If there is no timezone in the timestamp, the default timezone is UTC.

### Log level

* `loglevel` is set based on the value of the first found key from the following list, evaluated in the order presented in the list: `loglevel`, `status`, `severity`, `level`, `syslog.severity`.
* The default value is `NONE`.

### Content

* `content` is set based on the value of the first found key from the following list, evaluated in the order presented in the list: `content`, `message`, `payload`, `body`, `log`.
* The default value is an empty string.

### Attributes

* Log attributes contain all other keys from the input JSON object except those used for `timestamp`, `loglevel`, and `content`.
* First-level attributes should preferably map to semantic attributes for Dynatrace to map them to context. See [Semantic attributes (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api/log-classic-semantic-attributes "Supported semantic attributes that are indexed in Log Monitoring Classic.") for more details.
* All attribute keys are lowercased and all attribute values are stringified. Custom attributes and semantic attributes can generally be used in queries.
* Automatic attribute. The `dt.auth.origin` attribute is automatically added to every log record ingested via API. This attribute is the public part of the API key that the log source authorizes to connect to the generic log ingest API.

#### Attributes with non-primitive types

Nested objects in your log attributes are transformed into flat value pairs.

When a log attribute contains an object, each nested property becomes a separate attribute. This process works for attributes up to level five, while attributes beyond that level are skipped.

Array types are preserved as arrays but the contained types are unified to a single type.

* Complex values (such as arrays or objects) are mapped to JSON string values.
* If any value in the array is a string, or if any value must be converted to a string (e.g., an object or array), the target type of the entire array is string.
* If all values in the source array are numeric, the target array type is numeric.
* Null values are considered compatible with any type.

| Input | Log ingestion API endpoint output |
| --- | --- |
| ```  {  "content": "Transaction successfully processed.",  "transaction": {  "id": "TXN12345",  "amount": 250.75  },  "auditTrail": [  "Created",  "Approved",  3  ]  } ``` | ```  {  "content": "Transaction successfully processed.",  "transaction.id": "TXN12345",  "transaction.amount": 250.75,  "auditTrail": ["Created", "Approved", "3"]  } ``` |

##### Name conflicts

When attributes are saved in a flattened fashion on the Dynatrace side, there may be name collisions if attributes on different levels share the same name. Dynatrace resolves this by prefixing duplicate attributes with `overwritten[COUNTER].`. The counter value indicates how many times the attribute name has been already encountered as a duplicate. For example:

| Input | Log ingestion API endpoint output |
| --- | --- |
| ```  {  "host.name": "abc",  "host": {"name": "xyz"}  } ``` | ```  {  "host.name": "abc",  "overwritten1.host.name": "xyz"  } ``` |

* If a second conflict arises, an index is added starting with 1:

| Input | Log ingestion API endpoint output |
| --- | --- |
| ```  {  "service.instance.id": "abc",  "service": {"instance.id": "xyz", "instance": {"id": "123"}}  } ``` | ```  {  "service.instance.id": "abc",  "overwritten1.service.instance.id": "xyz",  "overwritten2.service.instance.id": "123"  } ``` |

#### Content related behavior

The rules below define how the `content` field is selected and constructed.

##### No supported content attribute found

In case no supported content attribute is found, the whole JSON representation of the log event is set as the `content` field of the output log record. The original JSON is preserved as-is.

Escaping in output examples is for visualization purposes only. `\"` is billed as one character.

| Input | Log ingestion API endpoint output |
| --- | --- |
| ```  {  "transaction": {  "id": "TXN12345",  "amount": 250.75  }  } ``` | ```  {  "content": "{\"transaction\":{\"id\":\"TXN12345\",\"amount\":250.75}}",  "transaction": {  "id": "TXN12345",  "amount": 250.75  }  } ``` |

##### Complex values in supported content attributes

Any attribute that is an object, including `content`, is treated as a standard attribute.

| Input | Log ingestion API endpoint output |
| --- | --- |
| ```  {  "payload": "This will be used for content.",  "message": {  "id": "TXN12345",  "amount": 250.75  }  } ``` | ```  {  "content": "This will be used for content.",  "message.id": "TXN12345",  "message.amount": 250.75  } ``` |

## Log ingestion API attribute handling

The Log Ingestion API additionally accepts log attributes through:

* Query parameters
* Special header: `X-Dynatrace-Attr`

These attributes are merged with those provided in the log record body according to the rules described below.

### Query parameter attributes

* All query parameters passed to the Log ingestion API endpoint are added to the log record body attributes.
* If a parameter key appears multiple times, all values are captured as a multivalue attribute.
* Keys and values follow the same attribute parsing rules as body attributes.
* Certain parameters are processed by the API for internal purposes and never appear as log record attributes, even if explicitly provided (such as those used in the **X‑Dynatrace‑Options** header). For the complete list of reserved parameter names and their processing behavior, see the [API documentation](/managed/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs#parameters "Push custom logs to Dynatrace via the Log Monitoring API v2.").

#### Example

| Request URL | Resulting attributes |
| --- | --- |
| `POST /api/v2/logs/ingest?env=prod&env=blue&team=payments`  ```  {  "content": "Transaction successfully processed."  } ``` | ```  {  "content": "Transaction successfully processed.",  "env": ["prod", "blue"],  "team": "payments"  } ``` |

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
  Where N is an incrementing integer (1, 2, …) depending on how many body-originating values had to be preserved. This ensures uniqueness even when multiple conflicts occur.
* Only values originating from the log body are preserved under the `overwrittenN.*` keys. Attributes overridden by higher-precedence sources do not generate overwritten copies.

#### Example

| Request | Resulting attributes |
| --- | --- |
| Query: `POST /api/v2/logs/ingest?team=frontend`  Body:  ```  {  "content": "Transaction successfully processed.",  "team": "backend"  } ``` | ```  {  "content": "Transaction successfully processed.",  "team": "frontend",  "overwritten1.team": "backend"  } ``` |

## Related topics

* [Log ingestion API (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Learn how Dynatrace ingests log data and what are potential limits such ingestion.")
* [Log Monitoring API v2 - POST ingest logs](/managed/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.")